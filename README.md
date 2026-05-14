# Markdown Timeline Generator | 时间线生成器

[English](#english) · [中文](#中文)

---

## English

Convert a simple YAML event list into a beautiful, responsive HTML timeline — perfect for project roadmaps, changelogs, and history pages.

### Features

- **Simple YAML input** — define events in a clean, readable format
- **Dark theme** — modern, responsive design with hover effects
- **Mobile-friendly** — adapts to any screen size
- **Zero JS** — pure HTML/CSS, no JavaScript dependencies

### Quick Start

```bash
# Install dependency
pip install pyyaml

# Generate sample timeline
python main.py

# Generate from your YAML file
python main.py events.yaml
```

### Input Format

```yaml
events:
  - date: "2024-01-15"
    title: "Project Kickoff"
    description: "Initial planning phase"
  - date: "2024-06-01"
    title: "Launch Day"
    description: "Public release"
```

### Output

A dark-themed, responsive HTML timeline with:
- Alternating left/right layout
- Hover animations
- Mobile-responsive design
- No external dependencies

---

## 中文

将简单的 YAML 事件列表转换为精美、响应式的 HTML 时间线——非常适合项目路线图、变更日志和历史页面。

### 功能

- **简洁的 YAML 输入** — 以清晰易读的格式定义事件
- **暗色主题** — 现代响应式设计，带悬停效果
- **移动端友好** — 适配任何屏幕尺寸
- **零 JS** — 纯 HTML/CSS，无 JavaScript 依赖

### 快速开始

```bash
# 安装依赖
pip install pyyaml

# 生成示例时间线
python main.py

# 从你的 YAML 文件生成
python main.py events.yaml
```

### 输入格式

```yaml
events:
  - date: "2024-01-15"
    title: "项目启动"
    description: "初始规划阶段"
  - date: "2024-06-01"
    title: "发布日"
    description: "公开发布"
```

### 输出

一个暗色主题的响应式 HTML 时间线：
- 左右交替布局
- 悬停动画效果
- 移动端自适应
- 无外部依赖

---

*By Lizer | [github.com/LizerAIDev](https://github.com/LizerAIDev)*
