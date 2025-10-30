from pathlib import Path
from tree_sitter import Language, Parser, Tree
import tree_sitter_java as java_language
from tree_sitter_utils import process_tree

CURDIR = Path(__file__).parent.resolve()

JAVA_DIR = CURDIR / "examples" / "java"
JAVA_FILE = JAVA_DIR / "Main.java"


def main():
    parser = Parser(Language(java_language.language()))

    with open(JAVA_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    tree: Tree = parser.parse(bytes(code, "utf8"))
    output = process_tree(tree)

    output.print_parse_tree()
    output.print_node_counts()


if __name__ == "__main__":
    main()
