from tree_sitter import Tree, Node


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
