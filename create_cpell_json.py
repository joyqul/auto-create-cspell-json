#! python3
"""
A simple script to get all invalid words and create a cspell.json file
"""
import sys
import re
import json
from typing import Optional


def parse_invalid_word_from_line(line: str) -> Optional[str]:
    match_object = re.search(r"\((\w+)\)", line)
    if match_object:
        return match_object.group(1)


def create_cpell_json():
    invalid_words = set()
    for line in sys.stdin:
        found_invalid_word = parse_invalid_word_from_line(line)
        if found_invalid_word:
            invalid_words.add(found_invalid_word)
    json_data = {
        "version": "0.2",
        "language": "en",
        "enableFiletypes": ["py"],
        "words": sorted(list(invalid_words))
    }
    with open("cspell.json", "w", encoding="UTF-8") as f:
        json.dump(json_data, f, indent=2)


if __name__ == "__main__":
    create_cpell_json()
