package textbook;

import java.util.*;

public class myQueue<T> {
    Stack<T> stack1;
    Stack<T> stack2;

    public myQueue() {
        stack1 = new Stack<T>();
        stack2 = new Stack<T>();

    }

    public int size() {
        return stack1.size() + stack2.size();

    }

    public void add(T item) {
        stack1.push(item);

    }

    public T remove() {
        combineStack();
        return stack1.pop();

    }

    public T peek() {
        combineStack();
        return stack1.peek();

    }

    public void combineStack() {
        if (stack1.isEmpty()) {
            while (!stack2.isEmpty()) {
                stack1.push(stack2.pop());

            }
        }
    }

}
