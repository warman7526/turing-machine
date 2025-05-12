# turing-machine
### By warman7526
---
This project is a way to write turing-machine style computational devices. There are two kinds, simple (traditional) and advanced. Simple designs are saved as `*.tm`, whereas advanced designs use `*.tmx`. In addition, ouput logs are outputted as `*.tmr` and external config files as `*.tmc`

## About Turing Machines
[This Wikipedia article](https://en.wikipedia.org/wiki/Turing_machine) has lots of info about turing machines and is well worth a read if you don't know what you're doing. Most examples in this documentation function as BB-3, a well known turing machine that you can find [here](https://en.wikipedia.org/wiki/Busy_beaver#List_of_busy_beavers) listed under ***3-state, 2-symbol busy beaver***

## Format of `.tm` files (Simple/Traditional Turing Machines)
### Defining rules
The most simple `.tm` file contains just the instructions ofr the machine to run on and would look similar to this:
```
A:1RB1R!
B:0RC1RB
C:1LC1LA
```
In this case we have 3 named instrucions, `A`, `B`, and `C`. Instructions can be named as any single non-whitespace charachter with the exception of `@`, `!`, and `:`.

The name is then followed by the rule defenition which is a string of 6 charachters, separated by a `:`. The charachters are read as two groups of 3, so for rule A in our example it is `1RB` & `1R!`. The first 3 describe what to do if the machine reads a 0 and the next 3 are for when a 1 is read instead.

The first number indicates what is to be written ontop of the existing data in that cell and can either be `0` or `1`. Then it is follwed by either `L` or `R` which tell the machine whether to move the read/write head left or right. Then another charachter is given depending on the next instruction to be executed, or, alternatively, you can use a `!` charachter to indicate that the program should halt.

So,  in our example, `A:1RB1R!` dictates that if the program is in state `A`, if a `0` is read, the head should write a `1`, move to the right and enter state `B`, or instead, if a `1` is read, then a `1`should be written (no change) and the head should move to the right, however then the program will halt and no further actions will be taken

### Setting other parameters
Additionally to defining rules for how the machine behaves, you can tweak the rules of how the simulation that it lives in will act, callled `config parameters`.

E.g.
- [x] hi
- [ ] hello