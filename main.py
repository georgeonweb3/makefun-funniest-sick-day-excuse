#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry. Writes one sick-day excuse to /output/entry.txt."""
import os

ENTRY = "Can't come in — my smart fridge locked me out of the kitchen at 3 a.m. and is now holding my lunch hostage for a software update."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

# Deterministic: same single line on every run, no network, no randomness.
