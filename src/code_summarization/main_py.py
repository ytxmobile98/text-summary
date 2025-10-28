import json
from pathlib import Path
from tree_sitter import Language, Parser, Tree
import tree_sitter_python as python_language
from tree_sitter_utils import output_tree

CURDIR = Path(__file__).parent.resolve()

PY_DIR = CURDIR / "examples" / "py"
PY_FILE = PY_DIR / "fibonacci.py"


def main():
    parser = Parser(Language(python_language.language()))

    with open(PY_FILE, "r", encoding="utf-8") as f:
        code = f.read()
    tree: Tree = parser.parse(bytes(code, "utf8"))

    output = output_tree(tree)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
