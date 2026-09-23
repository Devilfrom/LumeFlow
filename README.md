<div align="center">
  <img src="docs/images/lumeflow-logo.svg" width="360" alt="LumeFlow">
</div>

<div align="center">
  <a href="https://github.com/Devilfrom/LumeFlow/stargazers"><img src="https://img.shields.io/github/stars/Devilfrom/LumeFlow?style=social" alt="stars"></a>
  <img src="https://img.shields.io/badge/版本-0.5.0-blue" alt="版本">
  <a href="LICENSE"><img src="https://img.shields.io/badge/许可证-AGPL3.0-green" alt="许可证"></a>
  <a href="https://hub.docker.com/r/devilfrom/lumeflow/tags"><img src="https://img.shields.io/docker/pulls/devilfrom/lumeflow" alt="docker pulls"></a>

  <h4>
    <a href="README.md">🇨🇳 中文</a>
    <span> | </span>
    <a href="README_EN.md">🇬🇧 English</a>
  </h4>
</div>

---

## 📑 目录

<details open>
  <summary>展开 / 收起</summary>

- [💡 什么是 LumeFlow](#-什么是-lumeflow)
- [🌟 核心特性](#-核心特性)
- [🎬 快速开始](#-快速开始)
- [📚 项目文档](#-项目文档)
- [❓ 常见问题](#-常见问题)
- [🛠️ 如何贡献](#-如何贡献)
- [🚀 鸣谢](#-鸣谢)
- [📜 许可证与使用限制](#-许可证与使用限制)
- [✨ Star 历史](#-star-历史)

</details>

---

## 💡 什么是 LumeFlow

**LumeFlow** 是一个基于 [RAGFlow](https://github.com/infiniflow/ragflow) 深度二次开发的开源 RAG 引擎，目标是把这套强大的检索增强生成能力，打磨成**更简洁、更贴近中文实际场景**的一站式方案。

> 取意「Lumen（光）+ Flow（流）」——让沉淀的知识发光，让问答自然流淌。

在保留 RAGFlow 高质量解析与可追溯引用的基础上，LumeFlow 重点解决了真实落地中的几处痛点：独立后台管理、前台权限收敛、更强的文档解析、图文关联的回答，以及全新的文档撰写模式。

一句话总结：**LumeFlow 是 RAGFlow 在中文应用场景下的「行业特解」。**

## 🌟 核心特性

### 🛡️ **管理模式**
额外搭建一套后台信息管理系统，管理员可集中执行 **用户管理、团队管理、配置管理、文件管理、知识库管理** 等功能，让多租户与日常运维一目了然。

### 🔐 **权限回收**
前台系统对用户权限进行主动收缩，隐藏非必要入口，进一步**简化界面、降低误操作**，普通用户也能轻松上手。

### 🔍 **解析增强**
使用 [MinerU](https://github.com/opendatalab/MinerU) 替代原生 DeepDoc 解析算法，使文件解析效果更优，并原生**支持图片解析**，复杂排版 PDF / PPT / 扫描件也能精准切分。

### 🖼️ **图文输出**
模型在回答时，可输出与引用文本块**相关联的原始图片**，让答案不仅有出处、更有画面，特别适合说明书、图纸、带图文档等场景。

### 📝 **文档撰写模式**
提供全新的「文档模式」交互体验，把问答过程沉淀为结构化文档，让 AI 不只是回答问题，更能**帮你写文档**。

## 🎬 快速开始

> [!TIP]
> 推荐直接使用 Docker 一键启动，无需本地编译环境。

视频演示及操作教程：

[![LumeFlow 项目简介与操作指南](https://i0.hdslb.com/bfs/archive/f7d8da4a112431af523bfb64043fe81da7dad8ee.jpg@672w_378h_1c.avif)](https://www.bilibili.com/video/BV1UJLezaEEE)

使用 Docker 快速启动：

```bash
# 克隆仓库
git clone https://github.com/Devilfrom/LumeFlow.git
cd LumeFlow

# 启动全部服务（含主程序与后台管理系统）
docker compose -f docker/docker-compose.yml up -d
```

启动后访问：

- 主程序前台：<http://localhost>
- 后台管理系统：<http://localhost:8888>

> [!CAUTION]
> 默认的 MySQL / 后台管理员账号密码见 `docker/.env` 与 `docker-compose.yml`，**生产环境务必修改**。

## 📚 项目文档

完整文档站点（基于 docsify）：[xdxsb.top/ragflow-plus](https://xdxsb.top/ragflow-plus)

文档涵盖：快速开始、进阶技巧、API 接口、镜像构建、博客系列与常见问题，详见仓库 `docs/` 目录。

## ❓ 常见问题

- 使用过程中遇到问题，请先查阅 [常见问题](docs/question/README.md) 或仓库 Issues 是否有现成解答。
- 若仍未解决，可使用 [DeepWiki](https://deepwiki.com/Devilfrom/LumeFlow) 或 [zread](https://zread.ai/Devilfrom/LumeFlow) 与 AI 助手交流，多数常见问题可在此解决。
- 依旧无法解决，可提交仓库 Issue，将有 AI 助手自动解答。

## 🛠️ 如何贡献

1. Fork 本 GitHub 仓库（<https://github.com/Devilfrom/LumeFlow>）
2. 将 Fork 克隆到本地：
   `git clone git@github.com:<你的用户名>/LumeFlow.git`
3. 创建本地分支：
   `git checkout -b my-branch`
4. 提交信息需包含充分说明：
   `git commit -m '提交信息需包含充分说明'`
5. 推送更改到 GitHub（含必要提交信息）：
   `git push origin my-branch`
6. 提交 PR 等待审核

## 🚀 鸣谢

本项目基于以下开源项目开发：

- [ragflow](https://github.com/infiniflow/ragflow)
- [v3-admin-vite](https://github.com/un-pany/v3-admin-vite)
- [minerU](https://github.com/opendatalab/MinerU)

感谢所有贡献者：

<a href="https://github.com/Devilfrom/LumeFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Devilfrom/LumeFlow" />
</a>

## 📜 许可证与使用限制

1. **本仓库基于 AGPLv3 许可证**
   由于包含第三方 AGPLv3 代码，本项目必须遵循 AGPLv3 的全部条款。这意味着：
   - 任何**衍生作品**（包括修改或组合代码）必须继续使用 AGPLv3 并公开源代码。
   - 若通过**网络服务**提供本软件，用户有权获取对应源码。

2. **商用说明**
   - **允许商用**：本软件遵循 AGPLv3，允许商业使用，包括 SaaS 和企业内部部署。
   - **不修改代码**：若仅原样运行（不修改、不衍生），仍需遵守 AGPLv3，包括：
     - 提供完整的源代码（即使未修改）。
     - 若作为网络服务提供，需允许用户下载对应源码（AGPLv3 第 13 条）。
   - **不允许闭源商用**：如需闭源（不公开修改后的代码）商用，需获得所有代码版权持有人的书面授权（包括上游 AGPLv3 代码作者）。

3. **免责声明**
   本项目不提供任何担保，使用者需自行承担合规风险。若需法律建议，请咨询专业律师。

## ✨ Star 历史

![Stargazers over time](https://starchart.cc/Devilfrom/LumeFlow.svg)
