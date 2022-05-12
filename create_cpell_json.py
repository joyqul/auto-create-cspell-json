#! python3
"""
A simple script to get all invalid words and create a cspell.json file
"""
import sys
import re
import json
from typing import Optional, List


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
    json_data = {}
    try: 
        with open("cspell.json", "r", encoding="utf-8") as f:
            json_data = json.load(f)
            existed_words: List[str] = json_data.get('words', [])
            invalid_words.update(existed_words)
    except:
        pass

    with open("cspell.json", "w", encoding="utf-8") as f:
        json_data.update({
            "version": json_data.get("version", "0.2"),
            "language": json_data.get("language", "en"),
            "enableFiletypes": json_data.get("enableFiletypes", ["py"]),
            "words": sorted(list(invalid_words))
        })
        json.dump(json_data, f, indent=2)


if __name__ == "__main__":
    create_cpell_json()
