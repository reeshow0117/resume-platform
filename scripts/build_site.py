#!/usr/bin/env python3
"""构建简历平台静态产物:把 web/resume.html 复制到 dist/resume.html。"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent


def main():
    dist = ROOT / "dist"
    if not dist.exists():
        dist.mkdir(parents=True)
    shutil.copyfile(ROOT / "web" / "resume.html", dist / "resume.html")
    print("dist/resume.html 已更新")


if __name__ == "__main__":
    main()
