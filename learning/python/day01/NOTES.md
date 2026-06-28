# Day 01 Notes - Linked List

## What I learned today

### In one sentence
A linked list is a chain of nodes. Each node holds data and a pointer to the next node.

### Array vs Linked List
| Operation | Array | Linked List |
|-----------|-------|-------------|
| Read by index | O(1) - instant | O(n) - must walk from head |
| Insert at head | O(n) - shift everything | O(1) - just one pointer change |
| Delete in middle | O(n) - shift everything | O(1) - skip over the target |

> "Arrays are fast to read, slow to write. Linked lists are slow to read, fast to write."

### Key concepts
- **Node**: basic unit, has `data` (value) and `next` (pointer to next node)
- **head**: entry point of the list. From head you can reach everything.
- **None / null**: marks the end of the chain. The last node's `next` is None.

### Common pitfalls
1. Forgetting `current = current.next` in a while loop -> infinite loop
2. Forgetting the special case "deleting the head node"
3. Operating on an empty list without checking

---

## What I did today
Ran `linked_list.py` - it created a linked list, added/removed/searched nodes.

## What I'm still unsure about
(Write anything that confused you here)

## What to try next
- Reverse a linked list
- Implement a stack using a linked list
- Doubly linked list (each node also points to the previous one)
- C++ version
