#!/usr/bin/env python3
"""
Shuffle options in all JSON question files, update correct_answer,
and regenerate corresponding MD files.
"""

import json
import os
import random
import sys


OPTION_KEYS = ["option_1", "option_2", "option_3", "option_4"]


def shuffle_question_options(question, rng):
    """Shuffle the four options of a question and update correct_answer."""
    correct_keys = question.get("correct_answer", [])
    correct_values = {question[k] for k in correct_keys if k in question}

    options = [(k, question[k]) for k in OPTION_KEYS if k in question]
    rng.shuffle(options)

    new_correct_keys = []
    for new_key, (_, value) in zip(OPTION_KEYS, options):
        question[new_key] = value
        if value in correct_values:
            new_correct_keys.append(new_key)

    question["correct_answer"] = new_correct_keys
    return question


def shuffle_json_file(json_path, seed=42):
    """Load, shuffle options in-place, save JSON, return data."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rng = random.Random(seed)
    shuffled = [shuffle_question_options(q, rng) for q in data]

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(shuffled, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return shuffled


def option_number(key):
    """Return the 1-based number for option_1 -> 1, etc."""
    return int(key.split("_")[1])


def generate_ims_db_md(data):
    """Generate MD in IMS_DB style: ### Q{n}. {question} with 'Option N' answer."""
    total = len(data)
    lines = [
        f"# IMS DB Application Programmer - {total} Questions",
        "",
        f"**Total Questions:** {total}",
        "",
        "---",
        "",
    ]

    for q in data:
        num = q["questionnumber"]
        question_text = q["question"]
        topic = q["topic"]
        difficulty = q["difficulty"]
        choice_type = q["choice_type"]
        correct_keys = q.get("correct_answer", [])
        correct_nums = sorted(option_number(k) for k in correct_keys)
        correct_str = ", ".join(f"Option {n}" for n in correct_nums)

        lines.append(f"### Q{num}. {question_text}")
        lines.append("")
        lines.append(f"**Topic:** {topic}")
        lines.append(f"**Difficulty:** {difficulty}")
        lines.append(f"**Type:** {choice_type}")
        lines.append("")
        for i, key in enumerate(OPTION_KEYS, start=1):
            lines.append(f"{i}. {q[key]}")
        lines.append("")
        lines.append(f"**Correct Answer:** {correct_str}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def generate_ims_dc_md(data):
    """Generate MD in IMS_DC style: ## Question {n} with numeric answer."""
    total = len(data)
    lines = [
        f"# IMS DC Application Programmer - {total} Questions",
        "",
        f"This file contains {total} questions covering IMS DC (Data Communications) topics for application programmers.",
        "",
        "---",
        "",
    ]

    for q in data:
        num = q["questionnumber"]
        question_text = q["question"]
        topic = q["topic"]
        difficulty = q["difficulty"]
        choice_type = q["choice_type"]
        correct_keys = q.get("correct_answer", [])
        correct_nums = sorted(option_number(k) for k in correct_keys)
        correct_str = ", ".join(str(n) for n in correct_nums)

        lines.append(f"## Question {num}")
        lines.append("")
        lines.append(f"**Topic:** {topic}  ")
        lines.append(f"**Difficulty:** {difficulty}")
        lines.append(f"**Type:** {choice_type}")
        lines.append("")
        lines.append(f"**Question:** {question_text}")
        lines.append("")
        lines.append("**Options:**")
        for i, key in enumerate(OPTION_KEYS, start=1):
            lines.append(f"{i}. {q[key]}")
        lines.append("")
        lines.append(f"**Correct Answer:** {correct_str}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def detect_md_style(data):
    """Detect MD style based on question topics in the JSON data."""
    for q in data:
        topic = q.get("topic", "")
        if "IMS DC" in topic:
            return "ims_dc"
    return "ims_db"


def process_json_file(json_path, seed=42):
    """Shuffle options in a JSON file and regenerate its MD file."""
    print(f"Processing: {json_path}")
    data = shuffle_json_file(json_path, seed=seed)

    base = os.path.splitext(json_path)[0]
    md_path = base + ".md"

    style = detect_md_style(data)
    if style == "ims_dc":
        md_content = generate_ims_dc_md(data)
    else:
        md_content = generate_ims_db_md(data)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"  -> Updated JSON: {json_path}")
    print(f"  -> Regenerated MD: {md_path} (style={style})")

    dist = {}
    for q in data:
        for k in q.get("correct_answer", []):
            dist[k] = dist.get(k, 0) + 1
    print(f"  -> Correct answer distribution: {dist}")


def find_and_process_all(root_dir, seed=42):
    """Recursively find all JSON files and process them."""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in filenames:
            if fname.endswith(".json"):
                json_path = os.path.join(dirpath, fname)
                try:
                    process_json_file(json_path, seed=seed)
                except Exception as e:
                    print(f"  ERROR processing {json_path}: {e}", file=sys.stderr)


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    find_and_process_all(root)
    print("\nDone.")
