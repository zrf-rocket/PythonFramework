import json
import os.path

_CACHE = {}


def read_trace_list(name: str = "summary") -> list:
    json_file = f"./cases/{name}.json"
    if os.path.exists(json_file):
        with open(json_file, "r", encoding="utf-8") as f:
            trace_list = json.loads(f.read())

        return trace_list


def read_markdown(name: str = "markdown_test") -> tuple:
    file_path = f'./cases/{name}.md'
    with open(file_path, encoding="utf-8") as f:
        contents = f.read()
    return file_path, contents
