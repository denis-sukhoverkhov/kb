from typing import Dict, Iterator, List


class TreeNode:
    id: int
    data: Dict[str, str]
    children_ids: List[int]
    parent_id: int

    def __init__(
        self,
        id,
        children_ids,
    ):
        self.id = id
        self.children_ids = children_ids


class Tree:
    def __init__(
        self,
    ):
        self.nodes = {
            1: TreeNode(id=1, children_ids=[2, 4, 7]),
            2: TreeNode(id=2, children_ids=[5]),
            4: TreeNode(id=4, children_ids=[6]),
            5: TreeNode(id=5, children_ids=[]),
            6: TreeNode(id=6, children_ids=[]),
            7: TreeNode(id=7, children_ids=[10, 11, 12]),
            10: TreeNode(id=10, children_ids=[]),
            11: TreeNode(id=11, children_ids=[]),
            12: TreeNode(id=12, children_ids=[]),
        }

    def load_tree_from_json(self, data):
        pass

    def iterate_down_from_node(self, node_id: int) -> Iterator[TreeNode]:  # напишите
        node = self.nodes[node_id]

        childs = node.children_ids

        for i in childs:
            yield self.nodes[i]

        for i in childs:
            yield from self.iterate_down_from_node(i)


if __name__ == "__main__":
    t = Tree()

    r = t.iterate_down_from_node(1)
    for i in r:
        print(i.id)
