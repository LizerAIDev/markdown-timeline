# Markdown Timeline Generator | 时间线生成器

[![CI](https://github.com/LizerAIDev/markdown-timeline/actions/workflows/ci.yml/badge.svg)](https://github.com/LizerAIDev/markdown-timeline/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Convert YAML/Markdown event lists into beautiful, responsive HTML timelines.

将 YAML/Markdown 事件列表转为美观的响应式 HTML 时间线。

---

### Example / 示例

```bash
$ timeline
Timeline generated: timeline.html
  Events: 6
  Date range: 2024-01-15 → 2024-12-01
```

**Output** → [dark-themed HTML timeline](https://lizeraidev.github.io/markdown-timeline/timeline.html):

![Timeline preview](https://img.shields.io/badge/📅-Timeline_Generator-bc8cff?style=for-the-badge)

## Features / 功能

| Feature | Description |
|---------|-------------|
| 📅 YAML input | Define events in simple YAML format |
| 🎨 Dark theme | GitHub-dark styled responsive timeline |
| 📱 Mobile-friendly | CSS media queries for small screens |
| 📦 Sample data | Built-in sample events for quick start |
| ⚡ Lightweight | Only dependency: PyYAML |

## Quick Start / 快速开始

### Generate sample timeline

```bash
timeline
```

### Generate from your YAML file

```bash
# Create events.yaml
cat > events.yaml << 'EOF'
events:
  - date: 2024-01-15
    title: Project Kickoff
    description: Initial concept and planning
  - date: 2024-06-01
    title: Beta Release
    description: Public beta launch
  - date: 2024-12-01
    title: v1.0 Launch
    description: Official stable release
EOF

timeline events.yaml
```

### Install / 安装

```bash
pip install markdown-timeline-lizer
timeline events.yaml
```

## YAML Format / YAML 格式

```yaml
events:
  - date: YYYY-MM-DD
    title: Event Title
    description: Event description
```

## Tech Stack / 技术栈

- **Python 3.9+**
- **PyYAML** — YAML parser
- **Pure CSS** — No JavaScript, no frameworks

## License / 许可证

[MIT License](LICENSE)

---

<div align="center">

Made with ❤️ by [Lizer](https://github.com/LizerAIDev) | Powered by [Hermes Agent](https://hermes-agent.nousresearch.com)

</div>
