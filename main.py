# coding=utf-8
__date__ = "29 September 2022"

import logging
import os
import sys

from analyzer.text_analyzer import TextAnalyzer

logger = logging.getLogger(__name__)

LOGGING_ENABLED = os.environ.get("LOGGING_ENABLED", "true")
DEBUG_ENABLED = os.environ.get("DEBUG_ENABLED", "false")
BASE_LENGTH = 11
STDIN_LABEL = "stdin"

_level = logging.DEBUG if DEBUG_ENABLED.lower() == "true" else logging.INFO

if LOGGING_ENABLED.lower() == "true":
    logging.basicConfig(level=_level)

if __name__ == "__main__":
    if not sys.stdin.isatty():
        print(f"\nProcessing {STDIN_LABEL}")
        print("-" * (BASE_LENGTH + len(STDIN_LABEL)) + "\n")
        stdin = sys.stdin.read()
        if stdin:
            TextAnalyzer(stdin).find_most_common()

    if len(sys.argv) == 1:
        print("You must supply at least one file to process.")
        sys.exit(1)

    for filename in sys.argv[1:]:
        print(f"\nProcessing {filename}")
        print("-" * (BASE_LENGTH + len(filename)) + "\n")
        with open(filename) as f:
            TextAnalyzer(f.read()).find_most_common()
