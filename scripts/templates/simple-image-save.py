"""Save image and video responses from matching hosts to the current directory"""
"""if file extensions, MIMEs or URL paths match"""

import mimetypes
import re
from datetime import datetime
from email.message import Message
from pathlib import Path
from urllib.parse import unquote, urlsplit

from mitmproxy import ctx, http


MEDIA_EXTENSIONS = {
    ".avif",
    ".bmp",
    ".gif",
    ".heic",
    ".heif",
    ".jpeg",
    ".jpg",
    ".m4v",
    ".mkv",
    ".mov",
    ".mp4",
    ".mpeg",
    ".mpg",
    ".png",
    ".svg",
    ".webm",
    ".webp",
}
DEFAULT_PATH_PREFIXES = "/image/,/images/,/video/,/videos/,/media/"
INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


class MediaSaver:
    def load(self, loader):
        loader.add_option(
            name="media_domain_suffix",
            typespec=str,
            default="example.com",
            help="Only save responses from this host suffix (for example: example.com).",
        )
        loader.add_option(
            name="media_path_prefixes",
            typespec=str,
            default=DEFAULT_PATH_PREFIXES,
            help="Comma-separated URL path prefixes that identify media responses.",
        )

    def response(self, flow: http.HTTPFlow) -> None:
        suffix = ctx.options.media_domain_suffix.strip().lower().lstrip(".")
        if not suffix:
            ctx.log.error("media_domain_suffix cannot be empty; response was not saved")
            return

        host = flow.request.pretty_host.lower().rstrip(".")
        if host != suffix and not host.endswith("." + suffix):
            return

        response = flow.response
        if response is None or not response.raw_content:
            return

        url_path = urlsplit(flow.request.pretty_url).path
        path = unquote(url_path)
        path_name = Path(path).name
        extension = Path(path_name).suffix.lower()
        content_type = response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        is_media = (
            content_type.startswith("image/")
            or content_type.startswith("video/")
            or extension in MEDIA_EXTENSIONS
            or any(
                path.startswith(prefix.strip())
                for prefix in ctx.options.media_path_prefixes.split(",")
                if prefix.strip()
            )
        )
        if not is_media:
            return

        filename = self._content_disposition_filename(
            response.headers.get("content-disposition", "")
        )
        if not filename:
            filename = path_name
        filename = self._safe_filename(filename)
        if not filename:
            filename = "media"

        if not Path(filename).suffix:
            guessed_extension = mimetypes.guess_extension(content_type) if content_type else None
            if guessed_extension:
                filename += guessed_extension

        try:
            destination = self._save_without_overwrite(filename, response.raw_content)
        except OSError as error:
            ctx.log.error(f"Could not save media response from {host}: {error}")
            return

        ctx.log.info(f"Saved media response to {destination}")

    @staticmethod
    def _content_disposition_filename(header: str) -> str:
        message = Message()
        message["content-disposition"] = header
        filename = message.get_filename() or ""
        return unquote(filename).replace("\\", "/").rsplit("/", 1)[-1]

    @staticmethod
    def _safe_filename(filename: str) -> str:
        filename = filename.replace("\\", "/").rsplit("/", 1)[-1]
        filename = INVALID_FILENAME_CHARS.sub("_", filename).strip(" .")
        if filename in {".", ".."}:
            return ""
        return filename

    @staticmethod
    def _save_without_overwrite(filename: str, content: bytes) -> Path:
        candidate = Path(filename)
        stem, extension = candidate.stem, candidate.suffix
        path = Path.cwd() / filename
        try:
            with path.open("xb") as output:
                output.write(content)
            return path
        except FileExistsError:
            pass

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        for duplicate in range(1000):
            duplicate_suffix = f"-{duplicate + 1}" if duplicate else ""
            path = Path.cwd() / f"{stem}-[{timestamp}{duplicate_suffix}]{extension}"
            try:
                with path.open("xb") as output:
                    output.write(content)
                return path
            except FileExistsError:
                continue
        raise FileExistsError(f"Could not find a unique filename for {filename!r}")


addons = [MediaSaver()]
