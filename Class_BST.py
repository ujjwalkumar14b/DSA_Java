class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(root, val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = build_tree(root.left, val)
    else:
        root.right = build_tree(root.right, val)
    return root


def pre_order(root):
    if root is None:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)


# Helper method to collect elements in sorted order
def get_in_order(root, lst):
    if root is None:
        return
    get_in_order(root.left, lst)
    lst.append(root.data)
    get_in_order(root.right, lst)


def is_found(root, val):
    if root is None:
        return False
    if root.data == val:
        return True
    if val < root.data:
        return is_found(root.left, val)
    else:
        return is_found(root.right, val)


def delete(root, val):
    if root is None:
        return None
    if val < root.data:
        root.left = delete(root.left, val)
    elif val > root.data:
        root.right = delete(root.right, val)
    else:
        return None
    return root


def mirror_bst(root):
    if root is None:
        return root
    temp = mirror_bst(root.left)
    root.left = mirror_bst(root.right)
    root.right = temp
    return root


# Works for both lists and arrays in Python
def sorted_to_balanced(arr, left, right):
    if left > right:
        return None
    mid = left + (right - left) // 2
    root = Node(arr[mid])
    root.left = sorted_to_balanced(arr, left, mid - 1)
    root.right = sorted_to_balanced(arr, mid + 1, right)
    return root


def bst_to_balanced_bst(root):
    lst = []
    get_in_order(root, lst)
    return sorted_to_balanced(lst, 0, len(lst) - 1)

# Works for both lists and arrays in Python
def sorted_to_balanced(arr, left, right):
    if left > right:
        return None
    mid = left + (right - left) // 2
    root = Node(arr[mid])
    root.left = sorted_to_balanced(arr, left, mid - 1)
    root.right = sorted_to_balanced(arr, mid + 1, right)
    return root


def bst_to_balanced_bst(root):
    lst = []
    # 1. Store in-order traversal (gives a sorted list)
    get_in_order(root, lst)

    # 2. Build a balanced BST from the sorted list
    return sorted_to_balanced(lst, 0, len(lst) - 1)
   

if __name__ == "__main__":
    sorted_arr = [3, 5, 6, 8, 10, 12]
    root = None

    for i in sorted_arr:
        root = build_tree(root, i)

    print("InOrder: ", end="")
    in_order(root)
    print()

    sorted_root = sorted_to_balanced(sorted_arr, 0, len(sorted_arr) - 1)
    print("Sorted to Balanced PreOrder: ", end="")
    pre_order(sorted_root)
    print()

    # Unbalanced BST set up manually
    bst = Node(8)
    bst.left = Node(6)
    bst.left.left = Node(5)
    bst.left.left.left = Node(3)

    bst.right = Node(10)
    bst.right.right = Node(11)
    bst.right.right.right = Node(12)

    # Balance the skewed tree
    bst = bst_to_balanced_bst(bst)

    print("Balanced BST PreOrder: ", end="")
    pre_order(bst)
    print()


     sorted_arr = [3, 5, 6, 8, 10, 12]
    root = None

    for i in sorted_arr:
        root = build_tree(root, i)

    print("InOrder: ", end="")
    in_order(root)
    print()

    sorted_root = sorted_to_balanced(sorted_arr, 0, len(sorted_arr) - 1)
    print("Sorted to Balanced PreOrder: ", end="")
    pre_order(sorted_root)
    print()

    # Unbalanced BST set up manually
    bst = Node(8)
    bst.left = Node(6)
    bst.left.left = Node(5)
    bst.left.left.left = Node(3)

    bst.right = Node(10)
    bst.right.right = Node(11)
    bst.right.right.right = Node(12)

    # Balance the skewed tree
    bst = bst_to_balanced_bst(bst)

    print("Balanced BST PreOrder: ", end="")
    pre_order(bst)
    print()
