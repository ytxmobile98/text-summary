import json
from tree_sitter import Tree, Node


def process_tree(tree: Tree) -> tuple[dict, dict]:

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

    out_tree = process_node(root_node)

    def traverse(node: Node, result_node: dict, level: int = 0):
        for child in node.children:
            child_result = process_node(child, level + 1)
            result_node["children"].append(child_result)
            traverse(child, child_result, level + 1)

    traverse(root_node, out_tree)
    return out_tree, node_counts


def print_dict(d: dict):
    print(json.dumps(d, indent=2, ensure_ascii=False, sort_keys=True))


def print_output(out_tree: dict, node_counts: dict):
    print("Output tree:")
    print_dict(out_tree)

    print("Node counts:")
    print_dict(node_counts)
