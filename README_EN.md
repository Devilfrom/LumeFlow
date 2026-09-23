<div align="center">
  <img src="docs/images/lumeflow-logo.svg" width="360" alt="LumeFlow">
</div>

<div align="center">
  <a href="https://github.com/Devilfrom/LumeFlow/stargazers"><img src="https://img.shields.io/github/stars/Devilfrom/LumeFlow?style=social" alt="stars"></a>
  <img src="https://img.shields.io/badge/version-0.5.0-blue" alt="version">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL3.0-green" alt="license"></a>
  <a href="https://hub.docker.com/r/devilfrom/lumeflow/tags"><img src="https://img.shields.io/docker/pulls/devilfrom/lumeflow" alt="docker pulls"></a>

  <h4>
    <a href="README.md">🇨🇳 Chinese</a>
    <span> | </span>
    <a href="README_EN.md">🇬🇧 English</a>
  </h4>
</div>

---

## 📑 Table of Contents

<details open>
  <summary>Expand / Collapse</summary>

- [💡 What is LumeFlow](#-what-is-lumeflow)
- [🌟 Key Features](#-key-features)
- [🎬 Get Started](#-get-started)
- [📚 Documentation](#-documentation)
- [❓ FAQ](#-faq)
- [🛠️ How to Contribute](#-how-to-contribute)
- [🚀 Acknowledgements](#-acknowledgements)
- [📜 License & Usage Restrictions](#-license--usage-restrictions)
- [✨ Star History](#-star-history)

</details>

---

## 💡 What is LumeFlow

**LumeFlow** is an open-source RAG engine built on a deep fork of [RAGFlow](https://github.com/infiniflow/ragflow). It refines RAGFlow's powerful retrieval-augmented generation into a **simpler, more practical solution tailored for real-world (especially Chinese-language) scenarios**.

> The name blends "Lumen" (light) and "Flow" — letting your accumulated knowledge shine and your Q&A flow naturally.

On top of RAGFlow's high-quality parsing and traceable citations, LumeFlow addresses several pain points in production: a standalone admin console, tightened frontend permissions, stronger document parsing, image-aware answers, and a brand-new document-writing mode.

**In short:** LumeFlow is the "industry-specific solution" of RAGFlow for Chinese application scenarios.

## 🌟 Key Features

### 🛡️ **Management Mode**
An additional admin console lets administrators centrally handle **user management, team management, configuration management, file management, and knowledge-base management** — making multi-tenant operations and daily maintenance effortless.

### 🔐 **Permission Reclaiming**
The frontend proactively restricts user permissions and hides unnecessary entries, **simplifying the UI and reducing misoperations** so even casual users can get started quickly.

### 🔍 **Enhanced Parsing**
Replaces the native DeepDoc algorithm with [MinerU](https://github.com/opendatalab/MinerU) for superior parsing results, with native **image parsing** — complex PDFs, PPTs, and scans are segmented accurately.

### 🖼️ **Text-Image Output**
When answering, the model can return the **source images associated with cited text blocks**, so answers come with both provenance and visuals — ideal for manuals, blueprints, and image-heavy documents.

### 📝 **Document Writing Mode**
A brand-new "document mode" interaction turns the Q&A process into structured documents — the AI doesn't just answer questions, it **helps you write documents**.

## 🎬 Get Started

> [!TIP]
> We recommend the one-command Docker launch — no local build toolchain required.

Video demo & tutorial:

[![LumeFlow Introduction and User Guide](https://i0.hdslb.com/bfs/archive/f7d8da4a112431af523bfb64043fe81da7dad8ee.jpg@672w_378h_1c.avif)](https://www.bilibili.com/video/BV1UJLezaEEE)

Quick start with Docker:

```bash
# Clone the repository
git clone https://github.com/Devilfrom/LumeFlow.git
cd LumeFlow

# Start all services (core engine + admin console)
docker compose -f docker/docker-compose.yml up -d
```

After startup:

- Main frontend: <http://localhost>
- Admin console: <http://localhost:8888>

> [!CAUTION]
> Default MySQL / admin credentials live in `docker/.env` and `docker-compose.yml`. **Change them before any production use.**

## 📚 Documentation

Full documentation site (powered by docsify): [xdxsb.top/ragflow-plus](https://xdxsb.top/ragflow-plus)

The docs cover quick start, advanced tips, API reference, image building, the blog series, and FAQ — see the `docs/` directory in the repository.

## ❓ FAQ

- For common issues, check the [FAQ](docs/question/README.md) or browse the GitHub Issues section.
- If unresolved, try [DeepWiki](https://deepwiki.com/Devilfrom/LumeFlow) or [zread](https://zread.ai/Devilfrom/LumeFlow) to chat with the AI assistant, which solves most common problems.
- If the problem persists, open a GitHub Issue — the AI assistant will respond automatically.

## 🛠️ How to Contribute

1. **Fork** this repository (<https://github.com/Devilfrom/LumeFlow>)
2. Clone your fork locally:

   ```bash
   git clone git@github.com:<your-username>/LumeFlow.git
   ```
3. Create a new branch:

   ```bash
   git checkout -b my-branch
   ```
4. Commit with a descriptive message:

   ```bash
   git commit -m 'Provide a clear and descriptive commit message'
   ```
5. Push changes to GitHub:

   ```bash
   git push origin my-branch
   ```
6. Submit a PR and wait for review.

## 🚀 Acknowledgements

This project is based on the following open-source projects:

- [ragflow](https://github.com/infiniflow/ragflow)
- [v3-admin-vite](https://github.com/un-pany/v3-admin-vite)
- [minerU](https://github.com/opendatalab/MinerU)

Thanks to all contributors:

<a href="https://github.com/Devilfrom/LumeFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Devilfrom/LumeFlow" />
</a>

## 📜 License & Usage Restrictions

1. **AGPLv3 License**
   Since the project contains third-party AGPLv3 code, it must comply with all AGPLv3 terms:

   - Any **derivative works** (including modifications or combined code) must remain AGPLv3 licensed and open-sourced.
   - If provided via **network services**, users have the right to obtain the corresponding source code.

2. **Commercial Use**

   - **Allowed**: AGPLv3 permits commercial use, including SaaS and enterprise deployments.
   - **Unmodified Code**: Even without modifications, you must still comply with AGPLv3:
     - Provide the complete source code (even if unchanged).
     - If offered as a network service, allow users to download the source code (AGPLv3 Section 13).
   - **No Closed-Source Commercial Use**: Closed-source commercial use (not releasing modified code) requires written permission from all copyright holders, including upstream AGPLv3 authors.

3. **Disclaimer**
   This project is provided without warranties. Users are responsible for compliance. For legal advice, consult a professional lawyer.

## ✨ Star History

![Stargazers over time](https://starchart.cc/Devilfrom/LumeFlow.svg)
