import json
from pathlib import Path
from tree_sitter import Language, Parser, Tree, Node
import tree_sitter_python as python_language

CURDIR = Path(__file__).parent.resolve()

PY_DIR = CURDIR / "examples" / "py"
PY_FILE = PY_DIR / "fibonacci.py"

parser = Parser(Language(python_language.language()))
with open(PY_FILE, "r", encoding="utf-8") as f:
    code = f.read()
tree: Tree = parser.parse(bytes(code, "utf8"))


def output_tree(tree: Tree) -> dict:

    node_counts = {}

    root_node = tree.root_node

    def process_node(node: Node, level: int = 0) -> dict:
        node_counts[node.type] = node_counts.get(node.type, 0) + 1

        return {
            "type": node.type,
            "level": level,
            "text": (node.text or b'').decode("utf-8"),
            "children": [],
        }

    out = process_node(root_node)

    def traverse(node: Node, result_node: dict, level: int = 0):
        for child in node.children:
            child_result = process_node(child, level + 1)
            result_node["children"].append(child_result)
            traverse(child, child_result, level + 1)

    traverse(root_node, out)
    return {
        "output_tree": out,
        "node_counts": node_counts,
    }


output = output_tree(tree)
print(json.dumps(output, indent=2, ensure_ascii=False))
