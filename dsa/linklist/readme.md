## Linklist 
- A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.
- Unlike arrays, linked lists do not require contiguous memory allocation, allowing for efficient insertions and deletions.
- There are several types of linked lists:
  - **Singly Linked List**: Each node has a value and a pointer to the next node.
  - **Doubly Linked List**: Each node has a value, a pointer to the next node, and a pointer to the previous node.
  - **Circular Linked List**: The last node points back to the first node, forming a circle.
- Common operations on linked lists include:
  - Insertion: Adding a new node at the beginning, end, or a specific position.
  - Deletion: Removing a node from the beginning, end, or a specific position.
  - Traversal: Visiting each node in the list to access or modify its value.
- Linked lists are often used in scenarios where dynamic memory allocation is needed, such as implementing stacks, queues, and other abstract data types.


## Example of linked list

- Treasure Island is a classic example of a singly linked list. Each character in the story can be represented as a node, with each node pointing to the next character in the sequence. For instance, the first node could represent Jim Hawkins, pointing to the next node representing Long John Silver, and so on, until the last character points back to the first character, forming a circular linked list.
- The circular linked list allows for a continuous traversal of the characters, making it easy to revisit any character in the story without starting over from the beginning.
- The Train of Thought is another example of a linked list. Each thought can be represented as a node, with each node pointing to the next thought in the sequence. This allows for a continuous flow of ideas, where one thought leads to another, forming a chain of connected thoughts.


### Linked List VS Array
| Feature | Linked List | Array |
|---------|-------------|-------|
| Memory Allocation | Dynamic | Static |
| Size | Can grow or shrink | Fixed size |
| Insertion/Deletion | O(1) (if position is known) | O(n) |
| Access Time | O(n) | O(1) |   
| Dynamic Memory | Yes | No |