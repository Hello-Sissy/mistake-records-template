#!/usr/bin/env python3
"""Create private working files from blank templates without overwriting user data."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"


def main() -> None:
    for source in sorted(TEMPLATES.rglob("*")):
        if not source.is_file():
            continue
        target = ROOT / source.relative_to(TEMPLATES)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            print(f"保留已有文件：{target.relative_to(ROOT)}")
            continue
        shutil.copyfile(source, target)
        print(f"已创建：{target.relative_to(ROOT)}")
    for rel in (
        "错题记录/01_错题库",
        "错题记录/02_自定义组卷/未完成",
        "错题记录/02_自定义组卷/已完成",
        "错题记录/assets/images",
    ):
        (ROOT / rel).mkdir(parents=True, exist_ok=True)
    print("初始化完成。接着填写使用者配置.md。")


if __name__ == "__main__":
    main()
