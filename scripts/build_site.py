#!/usr/bin/env python3
"""构建简历平台静态产物:把 web 下的页面复制到 dist。"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent

PAGES = ("resume.html", "admin.html")


def main():
    dist = ROOT / "dist"
    if not dist.exists():
        dist.mkdir(parents=True)
    for name in PAGES:
        shutil.copyfile(ROOT / "web" / name, dist / name)
    print("dist 页面已更新：" + "、".join(PAGES))


if __name__ == "__main__":
    main()
