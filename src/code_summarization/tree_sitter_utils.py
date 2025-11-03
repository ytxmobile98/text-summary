import json
import pprint
from tree_sitter import Tree, Node


class Output:
    parse_tree: dict = {}
    node_counts: dict = {}
    nodes_by_levels: dict[Node, int] = {}

    def print_parse_tree(self, file: str = "/dev/stdout"):
        with open(file, 'w') as f:
            print(
                json.dumps(self.parse_tree, indent=2, ensure_ascii=False),
                file=f,
            )

    def print_node_counts(self, file: str = "/dev/stdout"):
        with open(file, 'w') as f:
            print(
                json.dumps(self.node_counts, indent=2, ensure_ascii=False,
                           sort_keys=True),
                file=f,
            )


def process_tree(tree: Tree) -> Output:

    output = Output()
    node_counts = output.node_counts

    root_node = tree.root_node

    def process_node(node: Node, level: int = 0) -> dict:
        node_counts[node.type] = node_counts.get(node.type, 0) + 1

        output.nodes_by_levels[node] = level

        return {
            "type": node.type,
            "level": level,
            "text": (node.text or b'').decode("utf-8"),
            "children": [],
        }

    parse_tree = process_node(root_node)

    def traverse(node: Node, result_node: dict, level: int = 0):
        for child in node.children:
            child_result = process_node(child, level + 1)
            result_node["children"].append(child_result)
            traverse(child, child_result, level + 1)

    traverse(root_node, parse_tree)

    output.parse_tree = parse_tree
    output.nodes_by_levels = dict(sorted(
        output.nodes_by_levels.items(),
        key=lambda item: (item[0].start_point, item[0].end_point),
    ))
    return output


def print_dict(d: dict):
    print(json.dumps(d, indent=2, ensure_ascii=False, sort_keys=True))


def print_output(output: Output):
    print("Output tree:")
    print_dict(output.parse_tree)

    print("Node counts:")
    print_dict(output.node_counts)

    print("Nodes by levels:")
    pprint.pprint(output.nodes_by_levels)
