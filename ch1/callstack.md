# Basics of Call Stacks

-Known as a LIFO data structure so last in, first out.
- Programs use call stacks with the stacks being made up of __frame objects or frames__

__Frames__ contain info about single function call including which line of code called the function so that the execution can go back to when the function returns. This is highlighted in the file 'how-functions-work.py' file.

### The Basic Structure of Frame Objects
Frame objects generally contain the following:
- the return address or spot in the program where the execution should move when the function returns
- the arguments passed to the function call
- set of local variables created during the function call

#### How the Frame Object Works
1. A program calls the function, a frame object is created and placed on the top of the call stack. __Note:The frame stores any arguments passed to a() along with local variables that exist only inside the function.__
2. Next the function a() calls the function b() which causes a new frame object to be created and placed on the call stack above the frame object of a(). __Note: b has different local variables from a, so the local variables are used for the b frame object.__
3. b() calls c() and new frame object is created an placed on call stack.
4. As the functions return the frame objects associated with each function pop off the call stack.__Note: The program execution knows where to return to as that information is stored in the frame object.__

Every running program has a call stack and multithreaded programs have one call stack fro each thread.

## Recursive Functions and Stack Overflows
_Recursive functions_ are simply functions that call themselves. When there is not base case, a computer will continously call the recursive function and keep calling until the computer runs out of memory leading to a crash.

_Stack Overflow_ is a type of bug which occurs when a computer runs out of memory by the callstack growing until it fills up the computers memory.

Python and JS interpreters protect against this by crashing the program if too many function calls take place without returning a value.

_Maximum recursion depth_ is the limit the interpreter puts on functions not returning a value. Python sets the limit at 1000 while JS has a callstack limit of 10,000.

## Base Case
All recursive functions need a base case and a recursive call.

If there is no base case then successive recursive calls cause a stackoverflow. If no recursive case then it is not a recursive function.


