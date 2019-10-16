def findMergeNode(head1, head2):
    node1 = head1
    node2 = head2
    while (node1 != node2):
        node1 = node1.next if(node1.next != None) else head2
        node2 = node2.next if(node2.next != None) else head1
    return node1.data
