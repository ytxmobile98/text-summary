from pathlib import Path
from tree_sitter import Language, Parser, Query, QueryCursor, Tree
import tree_sitter_java as java_language
from tree_sitter_queries import JAVA_QUERY
from tree_sitter_utils import process_tree

CURDIR = Path(__file__).parent.resolve()

JAVA_DIR = CURDIR / "examples" / "java"
JAVA_FILE = JAVA_DIR / "Main.java"


def main():
    language = Language(java_language.language())
    parser = Parser(language)

    with open(JAVA_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    # generate parse tree
    print("========== PARSE TREE ==========")
    tree: Tree = parser.parse(bytes(code, "utf8"))
    output = process_tree(tree)
    output.print_parse_tree()
    output.print_node_counts()
    print()

    # generate query captures
    print("========== CAPTURES ==========")
    query = Query(language, JAVA_QUERY)
    query_cursor = QueryCursor(query)
    captures = query_cursor.captures(tree.root_node)
    for capture_type, nodes in captures.items():
        for node in nodes:
            print(f"Capture Type: {capture_type},"
                  f" Text: {(node.text or b'').decode('utf-8')}")
    print()

    # generate query matches
    print("========== MATCHES ==========")
    matches = query_cursor.matches(tree.root_node)
    for i, d in matches:
        print(f"Match {i}:")
        for match_type, nodes in d.items():
            for node in nodes:
                print(f"  Match Type: {match_type},"
                      f" Text: {(node.text or b'').decode('utf-8')}")


if __name__ == "__main__":
    main()
