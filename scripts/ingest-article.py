#!/usr/bin/env python3
"""Ephemeral article ingest for ghost-writer.

Reads txt/md/pdf/docx using only tools already installed in the user's
environment. Prints markdown-ish body to stdout. Does not persist the source.
"""
import sys
import os
import subprocess
import shutil

TEXT_EXTS = {'.txt', '.md'}

# Ordered by preference. First available wins.
PDF_TOOLS = [
    ['pdftotext', '{path}', '-'],
    ['pandoc', '{path}', '-t', 'plain'],
]
DOCX_TOOLS = [
    ['pandoc', '{path}', '-t', 'plain'],
    ['docx2txt', '{path}', '-'],
]

def first_available(cmds):
    for cmd in cmds:
        if shutil.which(cmd[0]):
            return cmd
    return None

def run_tool(cmd, path):
    rendered = [path if p == '{path}' else p for p in cmd]
    return subprocess.run(rendered, capture_output=True, text=True, check=True).stdout

def ingest(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext in TEXT_EXTS:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    if ext == '.pdf':
        cmd = first_available(PDF_TOOLS)
        if not cmd:
            raise RuntimeError("No PDF extractor found. Install pdftotext or pandoc, or paste the text.")
        return run_tool(cmd, path)
    if ext == '.docx':
        cmd = first_available(DOCX_TOOLS)
        if not cmd:
            raise RuntimeError("No DOCX extractor found. Install pandoc or docx2txt, or paste the text.")
        return run_tool(cmd, path)
    raise ValueError(f"Unsupported format: {ext}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ingest-article.py <path>", file=sys.stderr)
        sys.exit(1)
    print(ingest(sys.argv[1]))
