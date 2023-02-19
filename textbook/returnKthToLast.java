/*
2.2 Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list
 */

package textbook;

import java.util.*;

public class returnKthToLast {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<String>();
        list.add("10");
        list.add("20");
        list.add("30");

        kthToLast(list, 2);

    }

    public static void kthToLast(LinkedList list, int k) {
        int len = list.size();
        System.out.println(list.get(len - k));
    }
}
