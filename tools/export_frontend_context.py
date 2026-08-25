#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import os
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_OUTPUT = "frontend_context_export.md"

EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    ".next",
    ".nuxt",
    ".output",
    ".vercel",
    ".netlify",
    "node_modules",
    "dist",
    "build",
    "coverage",
    ".cache",
    ".parcel-cache",
    ".turbo",
    "storybook-static",
    "playwright-report",
    "test-results",
    "__pycache__",
    ".venv"
}

EXCLUDED_FILE_NAMES = {
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "bun.lockb",
    ".DS_Store",
    "Thumbs.db",
    "de.json",
    "es.json",
    "fr.json",
    "hy.json",
    "it.json",
    "nl.json",
    "pt.json",
    "ru.json",
    "sl.json"
}

EXCLUDED_PATTERNS = [
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
    "*.crt",
    "*.p12",
    "*.pfx",
    "*.sqlite",
    "*.sqlite3",
    "*.db",
    "*.log",
    "*.tmp",
    "*.temp",
    "*.map",
    "*.min.js",
    "*.min.css",
]

BINARY_EXTENSIONS = {
    ".bin",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".avif",
    ".ico",
    ".icns",
    ".svgz",
    ".mp4",
    ".mov",
    ".avi",
    ".webm",
    ".mp3",
    ".wav",
    ".ogg",
    ".flac",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".eot",
    ".zip",
    ".tar",
    ".gz",
    ".rar",
    ".7z",
    ".pdf",
    ".psd",
    ".fig",
}

TEXT_EXTENSIONS = {
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".css",
    ".scss",
    ".sass",
    ".less",
    ".html",
    ".json",
    ".md",
    ".mdx",
    ".yml",
    ".yaml",
    ".toml",
    ".mjs",
    ".cjs",
    ".vue",
    ".svelte",
    ".astro",
    ".txt",
    ".gitignore",
    ".dockerignore",
    ".editorconfig",
    ".npmrc",
}

SECRET_MARKERS = [
    "api_key",
    "apikey",
    "secret",
    "password",
    "passwd",
    "private_key",
    "token",
    "access_token",
    "refresh_token",
    "client_secret",
    "vite_",
]


def is_excluded_path(path: Path, root: Path) -> bool:
    relative_parts = path.relative_to(root).parts

    for part in relative_parts:
        if part in EXCLUDED_DIRS:
            return True

    name = path.name

    if name in EXCLUDED_FILE_NAMES:
        return True

    for pattern in EXCLUDED_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            return True

    return False


def is_binary_file(path: Path) -> bool:
    suffix = path.suffix.lower()

    if suffix in BINARY_EXTENSIONS:
        return True

    try:
        with path.open("rb") as file:
            chunk = file.read(2048)
    except OSError:
        return True

    return b"\0" in chunk


def is_probably_text_file(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True

    if path.name in TEXT_EXTENSIONS:
        return True

    return not is_binary_file(path)


def mask_suspicious_line(line: str) -> str:
    lower = line.lower()

    has_secret_marker = any(marker in lower for marker in SECRET_MARKERS)
    has_assignment = "=" in line or ":" in line

    if has_secret_marker and has_assignment:
        stripped = line.strip()

        if stripped.startswith("//") or stripped.startswith("#") or stripped.startswith("*"):
            return line

        return "[REDACTED POSSIBLE SECRET LINE]\n"

    return line


def read_text_safely(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")

    lines = text.splitlines(keepends=True)
    return "".join(mask_suspicious_line(line) for line in lines)


def get_language_for_markdown(path: Path) -> str:
    suffix = path.suffix.lower()

    mapping = {
        ".js": "javascript",
        ".jsx": "jsx",
        ".ts": "typescript",
        ".tsx": "tsx",
        ".css": "css",
        ".scss": "scss",
        ".sass": "sass",
        ".less": "less",
        ".html": "html",
        ".json": "json",
        ".md": "markdown",
        ".mdx": "mdx",
        ".yml": "yaml",
        ".yaml": "yaml",
        ".toml": "toml",
        ".mjs": "javascript",
        ".cjs": "javascript",
        ".vue": "vue",
        ".svelte": "svelte",
        ".astro": "astro",
        ".txt": "text",
    }

    if path.name in {".gitignore", ".dockerignore", ".editorconfig", ".npmrc"}:
        return "text"

    return mapping.get(suffix, "text")


def build_tree(files: list[Path], root: Path) -> str:
    lines: list[str] = []

    for file_path in files:
        relative = file_path.relative_to(root)
        lines.append(str(relative))

    return "\n".join(lines)


def collect_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for current_root, dirnames, filenames in os.walk(root):
        current_path = Path(current_root)

        dirnames[:] = [
            dirname
            for dirname in dirnames
            if dirname not in EXCLUDED_DIRS
            and not is_excluded_path(current_path / dirname, root)
        ]

        for filename in filenames:
            file_path = current_path / filename

            if is_excluded_path(file_path, root):
                continue

            if not file_path.is_file():
                continue

            if not is_probably_text_file(file_path):
                continue

            files.append(file_path)

    return sorted(files, key=lambda item: str(item.relative_to(root)))


def export_frontend(root: Path, output_path: Path) -> None:
    files = collect_files(root)

    generated_at = datetime.now(timezone.utc).isoformat()

    with output_path.open("w", encoding="utf-8") as output:
        output.write("# Frontend Context Export\n\n")
        output.write(f"Generated at: `{generated_at}`\n\n")
        output.write(f"Project root: `{root}`\n\n")
        output.write("Generated by: `tools/export_frontend_context.py`\n\n")
        output.write(
            "Note: `.env*`, dependencies, caches, build artifacts, locks, "
            "keys, binary files and probable secret lines are excluded or redacted.\n\n"
        )

        output.write("## File Tree\n\n")
        output.write("```text\n")
        output.write(build_tree(files, root))
        output.write("\n```\n\n")

        output.write("## Files\n\n")

        for file_path in files:
            relative = file_path.relative_to(root)
            language = get_language_for_markdown(file_path)
            content = read_text_safely(file_path)

            output.write(f"### `{relative}`\n\n")
            output.write(f"```{language}\n")
            output.write(content)

            if content and not content.endswith("\n"):
                output.write("\n")

            output.write("```\n\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export frontend source code to a Markdown context file."
    )

    parser.add_argument(
        "--root",
        type=str,
        default=".",
        help="Frontend project root. Default: current directory.",
    )

    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT,
        help=f"Output markdown file. Default: {DEFAULT_OUTPUT}",
    )

    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_path = Path(args.output).resolve()

    if not root.exists():
        raise SystemExit(f"Root does not exist: {root}")

    if not root.is_dir():
        raise SystemExit(f"Root is not a directory: {root}")

    export_frontend(root=root, output_path=output_path)

    print(f"Exported frontend context to: {output_path}")


if __name__ == "__main__":
    main()
