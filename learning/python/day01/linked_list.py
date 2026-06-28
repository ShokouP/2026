# Day 01 - Linked List
# Run: python linked_list.py

class Node:
    """Each node holds data and a pointer to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A chain of nodes. Only needs to track the head."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node at the head. O(1) - linked list's superpower."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """Insert a node after prev_node. Just reassign two pointers."""
        if prev_node is None:
            print("Error: prev_node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        """Delete the first node whose data == key."""
        current = self.head

        # Special case: head is the target
        if current is not None and current.data == key:
            self.head = current.next
            return

        # General case: find the node before the target
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with value {key} not found")
            return

        # Skip over the target node
        prev.next = current.next

    def search(self, key):
        """Return True if key exists in the list. O(n)."""
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def length(self):
        """Count nodes. O(n) - must walk the whole chain."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def display(self):
        """Print the list in a readable format."""
        if self.head is None:
            print("[empty]")
            return
        current = self.head
        parts = []
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        print(" -> ".join(parts) + " -> None")


# ============================================================
# Demo
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Day 01 - Linked List")
    print("=" * 50)

    ll = LinkedList()
    print("\nEmpty list:")
    ll.display()

    print("\nappend(3), append(7), append(12):")
    ll.append(3)
    ll.append(7)
    ll.append(12)
    ll.display()
    # Expected: 3 -> 7 -> 12 -> None

    print("\nprepend(1) - insert at head:")
    ll.prepend(1)
    ll.display()
    # Expected: 1 -> 3 -> 7 -> 12 -> None

    print("\nsearch(7):", ll.search(7))    # True
    print("search(99):", ll.search(99))    # False

    print("\nLength:", ll.length())         # 4

    print("\ndelete(7):")
    ll.delete(7)
    ll.display()
    # Expected: 1 -> 3 -> 12 -> None

    print("\ndelete(99) - not in list:")
    ll.delete(99)

    print("\nFinal length:", ll.length())   # 3

    print("\n" + "=" * 50)
    print("Key takeaways:")
    print("  Node = data + next pointer")
    print("  prepend = O(1)  (linked list strength)")
    print("  search  = O(n)  (linked list weakness)")
    print("  delete  = skip over the target node")
    print("=" * 50)
