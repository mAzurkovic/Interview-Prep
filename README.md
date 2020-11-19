# Interview Preperation
> A repo that holds my LC solutions and other interview related prep notes...

## ToDo
- [x] Arrays
- [x] Strings
- [ ] Two pointer
- [ ] Sliding window
- [x] Linked Lists
- [ ] Trees
- [ ] Graphs
- [ ] DFS anf BFS
- [ ] Sorting
- [ ] Searching
- [ ] Python collections
- [x] Stacks/Queues

## Interviews so far (2020)
- Microsoft Software Engineer, phone screen
- Unity Software Engineer, assessment
- Snowflake Software Engineer, assessment
- Neurio Firmware Engineer, phone screen
- Splunk ML Software Engineer, phone screen
- Microsoft Software Engineer, final interview
- Amazon Software Engineer, assesment

## Notes

### DFS
> Time: O(|V| + |E|), Space: O(|V|)
* Uses stacks - either call stack (i.e. use recursion) or stack data structure (i.e. `deque`)
* Need a hash set (`set()`) to keep track of visited/seen nodes
* **Step 1**: Check if stack is not empty and loop
* **Step 2**: Set the current node to the top of the stack (`stack.pop()`)
* **Step 4**: If the current node has not been visited (i.e. `node not in seen`), then **do some stuff to it** and add it seen (`seen.add(current)`)
* **Step 3**: Iterate through the child nodes add to the stack if they are not `NULL`, and then loop again
* If tree, must use the `seen` set to keep track, do not need it for trees

### BFS
> Time: O(|V| + |E|), Space: O(|V|)
* Uses a queue and iteration, implimentation is the exact same only use queue instead of stack
* Instead of popping the top of the stack, dequeue the queue (using `.popleft()` from `collections`)
* **Step 1**: Check if queue is not empty
* **Step 2**: Dequeue to get the current node to be proccessed
* **Step 3**: Check if the current node has been visited (check the hashset), and if not, proccess it
* **Step 4**: For each child add it to the queue, and loop again

### Merge Sort
> Time: O(nlogn), Space: O(n)
* Recursivly split the array up into left and right halves
* Then merge these halves together in sorted order using another helper function




