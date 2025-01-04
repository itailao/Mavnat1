def test_avl_tree():
    # Create an AVL Tree
    avl_tree = AVLTree()

    # Insert nodes
    print("Inserting nodes into AVL Tree...")
    nodes = [
        (10, "ten"),
        (20, "twenty"),
        (30, "thirty"),
        (15, "fifteen"),
        (25, "twenty-five"),
        (5, "five"),
        (1, "one"),
        (8, "eight")
    ]
    
    for key, value in nodes:
        node, edges, promotions = avl_tree.insert(key, value)
        print(f"Inserted node with key: {key}, value: {value}, edges: {edges}, promotions: {promotions}")

    # Searching for nodes
    print("\nSearching for nodes in AVL Tree...")
    for key, _ in nodes:
        result = avl_tree.search(key)
        if result[0] is None:
            print(f"Node with key {key} not found.")
        else:
            print(f"Node with key {key} found, edges: {result[1]}")

    # Perform finger search
    print("\nPerforming finger searches...")
    finger_search_keys = [1, 5, 15, 30]
    for key in finger_search_keys:
        result = avl_tree.finger_search(key)
        if result[0] is None:
            print(f"Finger search: Node with key {key} not found.")
        else:
            print(f"Finger search: Node with key {key} found, edges: {result[1]}")

    # Test if the tree is balanced
    print("\nChecking if the AVL Tree is balanced...")
    def check_balance(node):
        if node is None:
            return True
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        balance_factor = abs(left_height - right_height)
        if balance_factor > 1:
            print(f"Tree is unbalanced at node with key: {node.key}")
            return False
        return check_balance(node.left) and check_balance(node.right)

    is_balanced = check_balance(avl_tree.root)
    if is_balanced:
        print("AVL Tree is balanced.")

# Run the test
test_avl_tree()
