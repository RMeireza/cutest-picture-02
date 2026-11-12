#!/usr/bin/env python3
"""Cutest picture entry (v2): writes the bundled soft-3D baby penguin illustration to /output/entry.png.
The picture was drawn procedurally with PIL during development (see transcripts) and is shipped in
the repository; this program copies it, byte-identical on every run (no network)."""
import os, shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
