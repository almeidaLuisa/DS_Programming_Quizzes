[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1LFNjRrK)
# Fall 2025 EEL3701C Lab 7 CPU

This EEL3701C lab is meant to introduce students to assembly language concepts. For usage instructions, keep reading. For information on the CPU, such as registers, instructions, and architecture, please read [info.md](info.md).

## Requirements

Before usage, ensure that python is installed on your computer. Command line usage of Python **is** required. For some users, Python will be invoked on the command line with just `python`, while others will have to type `python3`. You can find out which one works by running `python -h` or `python3 -h` in your terminal. If both work, use `python3`. For this tutorial, all the example commands will use `python3`, so if you use `python`, keep that in mind.

There are two main files: `runner.py` and `codes.py`. The code inside the files doesn't matter, but `codes.py` contains all the functionality of the CPU, while `runner.py` is what you will use to run your programs.

Just an additional note, if you run into an infinite loop, you can end the program execution with CTRL+C on Windows/Linux or CMD+. on MacOS. 

## Command Line Usage

`python3 runner.py [-h] [-f filename] [-s]`

- -h: Prints a help menu without executing any files.
- -f: Input a filename to assemble. If this argument is not used, the program will default to `program.lab7`.
- -s: Skip inputting commands and execute the program. If there is an infinite loop in your code, you will need to use CTRL+C or CMD+. to end program execution.

## Operation

If your program has successfully assembled, you will initially be greeted with a menu of available commands, the state of the registers and program counter, and the next instruction. From here, you have 6 available options:
- 0x\[address]: Shows the value in memory at a certain address. For example, running `ex2.lab7` by typing in `python3 runner.py -f ex2.lab7`, then typing in `0x200` will show the value `0xE3`.
- Q: Prints the status of the registers, then stops the execution of the program.
- S: Steps through a single instruction. You will see the registers update and the program counter increment. You can also step by just clicking enter and leaving the command line blank.
- C: Continue until the end of the program. You will not have the ability to enter commands during this time, and execution will continue until the program ends. If stuck in an infinite loop, you use CTRL+C or CMD+. to force exit the program.
- P: Prints the state of the CPU, including registers, program counter, and the next instruction. The state of the CPU is automatically printed after every step, but it can be done manually as well.
- H: Prints a reminder of all the commands. It is more condensed than this version, but still serves useful. 

## Example Programs

There are two programs provided for testing purposes: `ex1.lab7` and `ex2.lab7`. Use `ex1.lab7` to get used to the basic control flow and checking the value of registers. Use `ex2.lab7` to look at memory addresses. Specifically, check `0x200` at the start of the program, execute a couple lines, then check `0x200` again and see the value change. Also look at the code for both of these files, read the comments, and understand what they're doing. After this, you're set to continue the lab. Happy assembling!