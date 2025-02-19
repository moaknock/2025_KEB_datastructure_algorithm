class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = TreeNode(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(data)
                    break
                current = current.right

    def search(self, data):
        current = self.root
        while current:
            if data == current.data:
                return True  # 값 찾음
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False  # 값 없음

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # 자식이 둘 있는 경우
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete(node.right, min_larger_node.data)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.data, end=" ")
            self._inorder_traversal(node.right)

if __name__ == "__main__":
    bst = BST()
    numbers = [10, 15, 8, 3, 9]

    for num in numbers:
        bst.insert(num)

    print("BST 중위 순회 결과:")
    bst.inorder_traversal()

    find_num = int(input("\n검색할 숫자 입력: "))
    if bst.search(find_num):
        print(f"{find_num}을(를) 찾았습니다.")
    else:
        print(f"{find_num}이(가) 존재하지 않습니다.")

    delete_num = int(input("\n삭제할 숫자 입력: "))
    bst.delete(delete_num)
    print(f"{delete_num} 삭제 후 BST 중위 순회:")
    bst.inorder_traversal()
