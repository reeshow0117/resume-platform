#!/usr/bin/env python3
"""简历防编造自检:对 verify_resume 跑断言集,保证引用溯源可信。

覆盖:合法稿通过、虚构编号被拦截、组织名篡改被拦截。
用法: python3 agent/selfcheck.py  (全部通过退出码 0,否则 1)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resume_gen import verify_resume


def main():
    passed, failed, total = 0, [], 3
    materials = {
        "S1": {"org": "腾讯", "role": "实习生", "period": "2026", "body": "- 做了A\n"},
        "P1": {"org": "某项目", "role": "作者", "period": "2025", "body": "- 做了B\n"},
    }
    # 正常:引用存在且组织名一致
    good = "## 实习\n### S1 | 腾讯 | 实习生 | 2026\n- 做了A [@S1]\n"
    if verify_resume(good, materials) == []:
        passed += 1
        print("  PASS 简历自检:合法稿通过")
    else:
        failed.append("合法稿")
        print("  FAIL 合法简历被误报")
    # 对抗:引用不存在的编号
    ghost = "### S1 | 腾讯 | 实习生 | 2026\n- 做了X [@S9]\n"
    if any("S9" in v for v in verify_resume(ghost, materials)):
        passed += 1
        print("  PASS 简历自检:虚构编号被拦截")
    else:
        failed.append("虚构编号")
        print("  FAIL 虚构编号未被发现")
    # 对抗:组织名被篡改
    tampered = "### S1 | 阿里巴巴 | 实习生 | 2026\n- 做了A [@S1]\n"
    if any("篡改" in v for v in verify_resume(tampered, materials)):
        passed += 1
        print("  PASS 简历自检:组织名篡改被拦截")
    else:
        failed.append("组织名篡改")
        print("  FAIL 组织名篡改未被发现")

    print(f"\n简历自检 {passed}/{total} 通过")
    if failed:
        print("未通过:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
