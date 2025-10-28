from pathlib import Path
from tree_sitter import Language, Parser, Tree
import tree_sitter_python as python_language
from tree_sitter_utils import process_tree, print_output

CURDIR = Path(__file__).parent.resolve()

PY_DIR = CURDIR / "examples" / "py"
PY_FILE = PY_DIR / "fibonacci.py"


def main():
    parser = Parser(Language(python_language.language()))

    with open(PY_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    tree: Tree = parser.parse(bytes(code, "utf8"))
    output_tree, node_counts = process_tree(tree)

    print("Output tree:")
    print_output(output_tree)

    print("Node counts:")
    print_output(node_counts)


if __name__ == "__main__":
    main()
