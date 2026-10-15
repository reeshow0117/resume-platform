# resume-platform

根据岗位 JD 和本机 Obsidian 资料库,自动重组并生成「单页 A4、中文衬线、右上证件照、
加粗 + ➢ 版式」的定制简历。独立于岗位看板(campus-jobs-board),单独部署、单独 CI。

## 结构
- `agent/` 后端(FastAPI):`server.py` 入口、`llm.py` 模型调用、`resume_gen.py` 选材生成、
  `resume_pdf.py` 认可版排版、`vault_loader.py` 读资料库、`access.py` 邀请码/额度、`selfcheck.py` 防编造自检
- `web/resume.html` 前端(与后端同源,填 JD / 生成 / 下载)
- `scripts/build_site.py` 构建 `dist/resume.html`
- `tests/` 离线回归(unittest + node 前端烟测)

## 本地运行
    python -m pip install -e '.[test]'
    uvicorn agent.server:app --host 127.0.0.1 --port 8000

## 隐私约定
资料库、证件照、输出、密钥(`.env`)均被 `.gitignore` 排除,严禁提交。
模型密钥只放部署服务器的受限环境文件,不进仓库、不进前端。
