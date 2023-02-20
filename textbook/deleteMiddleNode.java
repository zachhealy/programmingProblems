/*
2.3 Delete Middle Node

Implement an algorithm to delete a node in the middle (i.e. any node but the first and last,
not necessarily the exact middle) of a singly linked list, given only access to that node

Example:
Input - the node c from the linked list a -> b -> c -> d -> e -> f
Result = nothing is returned but the new linked list looks like a -> b -> d -> e -> f

 */

package textbook;

import java.util.*;

public class deleteMiddleNode {
    public static void main(String[] args) {
        System.out.print("hello world");

    }

    public void delMiddleNode(LinkedListNode n) {
        if (n == null || n.next == null) {
            return;
        }
        LinkedListNode next = n.next;
        n.data = next.data;
        n.next = next.next;

    }

}
