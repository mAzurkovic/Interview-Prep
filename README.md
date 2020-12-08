# Interview Preperation
> A repo that holds my LC solutions and other interview related prep notes...

## ToDo
- [x] Arrays
- [x] Strings
- [ ] Two pointer
- [ ] Sliding window
- [x] Linked Lists
- [X] Trees
- [ ] Graphs
- [X] DFS anf BFS
- [X] Sorting
- [X] Searching
- [X] Python collections
- [x] Stacks/Queues

## Interviews so far (2020)
- Microsoft Software Engineer, phone screen
- Unity Software Engineer, assessment
- Snowflake Software Engineer, assessment
- Neurio Firmware Engineer, phone screen
- Splunk ML Software Engineer, phone screen
- Microsoft Software Engineer, final interview
- Amazon Software Engineer, assesment (debugging, coding, and now work simulation)

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

### Kadene's Algorithm
* Used for finding maximum contiguous subarray
* Works by tracking current sum of elements up to i
* If the current element is greater than the current sum, reset the current sum to the value of i
* Then compare to max sum

### 4 Pillars of OOP
1. **Abstraction**: Show only the essential features of an entity - i.e. in the real world, a TV remote only care about the buttons, not the electrical signals being 
generated and sent
2. **Encapsulation**: Wrapping up related data and functions together in a class. Can choose what to expose and hold private (`public`/`private`)
3. **Inheritance**: Creating a new class based on an existsing class - a child class inherits properties from a parent/super class, also allows for code reuse
4. **Polymorphism**: A subclass can define its own methods and properties that define its own unique behavior however still share from the parent class. Change methods from parent class.

### Linux Questions
* `uname -a`: Check kernel version of system
* `ifconfig` or `ip addr show <device>`: Check current IP on device (IPv6, ETH0, ...)
* `df`: Check disk space available on system
* `service <service-name> <status, start, stop>` or `systemctl <status, start, stop> <service>`: Manage and read services on a system
* `du -sh <directory>`: Check directory size
* `netstat -tulpn`: Check open ports on system
* `ps aux`: Check CPU usage from processes

### Python Questions
* Why use Python? It is a programming language that has objects, modules, threads, exceptions and memory managment. The befefits of it are it is easy to use, portable, lots of built-in data structures and capabilities
and has lots of great libraries.
* PEP 8? It is a Python coding convention and set of reccomendations to make code more readable and standardized.
* What is a module? A module lets you orginize related code locally (i.e. in the same file).
* How is it interpreted? It is not compiled into machine code and than ran. Instead it is interpreted into bytecode and ran on the Python specific intepreter (`.pyc` file)
* How to find bugs in Python? PyChecker is a static tool that lets us see bugs and syntax errors. Also have PyLint to verify that our code follows PEP 8 and VSCode is good.
* Difference between list and tuple? List is mutable, while tuple is not. We can use tuples for the keys in a hashmap.
* Arrays vs. lists? They store value in the same way at a low level, however arrays can only store a signle data type.
* What are the built in types? None, Integer, Float, complex, string, list, set, tuple, dictionary, forzenset, frozendict, file, slice.

