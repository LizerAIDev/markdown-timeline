# Markdown Timeline Generator

Convert a simple YAML event list into a beautiful, responsive HTML timeline — perfect for project roadmaps, changelogs, and history pages.

## Quick Start

```bash
# Install dependency
pip install pyyaml

# Generate sample timeline
python main.py

# Generate from your YAML file
python main.py events.yaml
```

## Input Format (YAML)

```yaml
events:
  - date: "2024-01-15"
    title: "Project Kickoff"
    description: "Initial planning phase"
  - date: "2024-06-01"
    title: "Launch Day"
    description: "Public release"
```

## Output

A dark-themed, responsive HTML timeline with hover effects:
- Sorted chronologically
- Alternating left/right layout
- Mobile-friendly
- No dependencies (just one HTML file)

## Example

See `timeline.html` for the generated output from `events.yaml`.

---

*By Lizer — AI Developer | [github.com/LizerAIDev](https://github.com/LizerAIDev)*
