# use the length of the list
def kth_to_last_node1(k, head):
    if k < 1:
        raise ValueError(
            'Impossible to find less than first to last node: %s' % k
        )

    # Step 1: get the length of the list
    # Start at 1, not 0
    # else we'd fail to count the head node!
    list_length = 1
    current_node = head

    # Traverse the whole list,
    # counting all the nodes
    while current_node.next:
        current_node = current_node.next
        list_length += 1

    # If k is greater than the length of the list, there can't
    # be a kth-to-last node, so we'll return an error!
    if k > list_length:
        raise ValueError(
            'k is larger than the length of the linked list: %s' % k
        )

    # Step 2: walk to the target node
    # Calculate how far to go, from the head,
    # to get to the kth to last node
    how_far_to_go = list_length - k
    current_node = head
    for i in range(how_far_to_go):
        current_node = current_node.next

    return current_node
    

# maintain a kk-wide "stick" in one walk down the list.
def kth_to_last_node2(k, head):
    if k < 1:
        raise ValueError(
            'Impossible to find less than first to last node: %s' % k
        )

    left_node  = head
    right_node = head

    # Move right_node to the kth node
    for _ in range(k - 1):
        # But along the way, if a right_node doesn't have a next,
        # then k is greater than the length of the list and there
        # can't be a kth-to-last node! we'll raise an error
        if not right_node.next:
            raise ValueError(
                'k is larger than the length of the linked list: %s' % k
            )
        right_node = right_node.next

    # Starting with left_node on the head,
    # move left_node and right_node down the list,
    # maintaining a distance of k between them,
    # until right_node hits the end of the list
    while right_node.next:
        left_node  = left_node.next
        right_node = right_node.next

    # Since left_node is k nodes behind right_node,
    # left_node is now the kth to last node!
    return left_node
