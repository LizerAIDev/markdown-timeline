#!/usr/bin/env python3
"""Tests for markdown-timeline"""
import sys
import os
import pytest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import load_events, generate, SAMPLE_EVENTS, EVENT_TEMPLATE


def test_load_sample_events():
    events = load_events()
    assert len(events) == 6
    assert events[0]["title"] == "Project Kickoff"


def test_load_from_yaml(tmp_path):
    yaml_file = tmp_path / "events.yaml"
    yaml_file.write_text("events:\n  - date: 2024-01-01\n    title: New Year\n    description: Happy new year\n")
    events = load_events(str(yaml_file))
    assert len(events) == 1
    assert events[0]["title"] == "New Year"


def test_load_nonexistent_file():
    events = load_events("/nonexistent/file.yaml")
    assert len(events) == len(SAMPLE_EVENTS)


def test_generate_output(tmp_path):
    output = tmp_path / "timeline.html"
    generate(SAMPLE_EVENTS, str(output))
    assert output.exists()
    content = output.read_text()
    assert "<!DOCTYPE html>" in content
    assert "Project Kickoff" in content
    assert "timeline" in content.lower()


def test_events_sorted():
    events = [
        {"date": "2024-12-01", "title": "Late", "description": "test"},
        {"date": "2024-01-01", "title": "Early", "description": "test"},
    ]
    tmp = Path("/tmp/test_sorted.html")
    generate(events, str(tmp))
    content = tmp.read_text()
    early_pos = content.find("Early")
    late_pos = content.find("Late")
    assert early_pos < late_pos  # Early should appear first


def test_event_template_format():
    html = EVENT_TEMPLATE.format(
        date="2024-01-01",
        title="Test Event",
        description="Test description"
    )
    assert "2024-01-01" in html
    assert "Test Event" in html
    assert "Test description" in html
