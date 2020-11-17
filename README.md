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
* Uses stacks - either call stack (i.e. use recursion) or stack data structure (i.e. `deque`)
* Need a hash set (`set()`) to keep track of visited/seen nodes
* While the stack is not empty, set the current node to the top of the stack (`stack.pop()`)
* If the current node has not been visited (i.e. `node not in seen`), then **do some stuff to it** and add it seen (`seen.add(current)`)
* Then add the child nodes to the stack if they are not `NULL`, and then loop again...
