# Info
This document contains information about the CPU's architecture, instructions, and directives. If you are looking for information about the operation of the CPU and how to run it from the command line, please read [README.md](README.md).

# Architecture
- 4 general purpose registers, A B C D, 1 byte each (Referred to as R)
- 2 memory access registers, X Y, 2 bytes each (Referred to as S)
  - These registers can be loaded with values above 1023, but when accessing memory, it will wrap around (ex. 1024 corresponds to address 0)
- 1024 bytes of memory available, requires upper 2 bits of memory access registers
- Flags based on last operation: Negative, Zero
    - If result of an operation is Zero, Zero flag = 1, otherwise 0
    - If the MSB of a result is 1, then Negative flag = 1, otherwise 0
    - Data management instructions such as MOV or LDI do **not** set the flags, only logic/arithmetic operations do

# Instructions

## NOP
- `NOP`: NOP aka No Operation
  - Generally not used for actual program operation, this is an instruction that does nothing. It can be used in programs as a point to check the values in memory or within registers.

## Data Management
- `MOV R1/S1, R2/S2`: Move
  - Move data from register `R2/S2` to register `R1/S1`, registers must be same width
  - Ex. `MV X, Y` is good, `MV X, A` is invalid.
- `LDI R/S, IMM`: Load Immediate
  - Load register `R/S` with specified immediate in hex (0x), binary (0b), or decimal (no prefix)
  - Can load values -128 to 127 or 0 to 255 into A, B, C, D
  - Can load values 0 to 65535 into X, Y, with memory wraparound
  - 1 byte immediate for A, B, C, D
  - 2 byte immediate for X, Y
- `RDM R, S`: Read Memory
  - Read memory from address `S` and load into register `R`
- `WRM S, R`: Write Memory
  - Write data in register `R` to address `S`

## Branching
- `JMP LABEL`: Jump
  - Unconditionally jumps to instruction immediately following specified label
- `JNZ LABEL`: Jump if Not Zero
  - Jumps to instruction immediately following specified `LABEL` **if** the Zero flag is 0, otherwise continues to next instruction
- `JEZ LABEL`: Jump if Equals Zero
  - Jumps to instruction immediately following specified `LABEL` **if** the Zero flag is 1, otherwise continues to next instruction
- `JNE LABEL`: Jump if Negative
  - Jumps to instruction immediately following specified `LABEL` **if** the Negative flag is 1, otherwise continues execution to next instruction
- `JPZ LABEL`: Jump if Positive or Zero
  - Jumps to instruction immediately following specified `LABEL` **if** the Negative flag is 0, otherwise continues execution to next instruction

## Logic/Arithmetic Operations

- `ADD R1, R2, R3`: Add
  - R1 = R2 + R3, sets zero flag and negative flag
- `ADDI R1, R2, IMM`: Add Immediate
  - R1 = R2 + IMM, sets zero flag and negative flag
- `SUB R1, R2, R3`: Subtract
  - R1 = R2 - R3, sets zero flag and negative flag
- `SUBI R1, R2, IMM`: Subtract Immediate
  - R1 = R2 - IMM, sets zero flag and negative flag
- `INC S`: Increment
  - Increments X or Y register, does not set zero flag or negative flag
- `DEC S`: Decrement
  - Decrements X or Y register, does not set zero flag or negative flag
- `ORL R1, R2, R3`: Logical OR
  - R1 = R2 OR R3, bitwise or, sets zero flag but not negative flag
- `ANDL R1, R2, R3`: Logical AND
  - R1 = R2 AND R3, bitwise and, sets zero flag but not negative flag
- `XORL R1, R2, R3`L Logical XOR
  - R1 = R2 XOR R3, bitwise xor, sets zero flag but not negative flag
- `INV R1`: Invert
  - R1 = ~R1 (bitwise not), does not set zero flag or negative flag
- `CMP R1, R2`: Compare
  - If R1 == R2, sets zero flag and not negative flag
  - If R1 > R2, sets neither flag
  - If R1 < R2, sets negative flag
- `CMPI R1, IMM`: Compare Immediate
  - If R1 == IMM, sets zero flag and not negative flag
  - If R1 > IMM, sets neither flag
  - If R1 < IMM, sets negative flag
- `LSL R1, R2, IMM`: Logical Shift Left
  - This will shift R2 by IMM bits to the left and place the result in R1. IMM must be within 0 to 7 inclusive.
- `LSR R1, R2, IMM`: Logical Shift Right
  - This will shift R2 by IMM bits to the right and place the result in R1. IMM must be within 0 to 7 inclusive.

# Comments
Comments can be declared with `--`. Comments can start anywhere in the line, and anything after the `--` will be ignored.

# Directives

All directives aside from labels should be at the beginning of the program for proper usage.

Directives are not apart of the instruction set architecture, they are assembler specific commands handled at assembly time to organize code and data, not executed by the CPU. These are the valid directives for our assembler.

## Labels
Must be on a separate line from other code and must contain a colon. Labels must also be unique. Labels are **case-sensitive**.

Valid:
```
LDI A, 0x05
LDI B, 0x00
LOOP:
ADD B, B, A
SUBI A, A, 1
JNZ LOOP
```
Invalid:
```
LDI A, 0x05
LDI B, 0x00
LOOP: ADD B, B, A
SUBI A, A, 1
JNZ LOOP
```
Because the `LOOP` directive is on the same line as an instruction, it does not function properly.

## .byte ADDR DATA
Places `DATA` at address `ADDR` within the data segment of memory. `ADDR` and `DATA` can either be in hexadecimal (prefixed by 0x), binary (prefixed by 0b), or decimal (no prefix). `ADDR` must be a non-negative value less than or equal to 1023 (0x3FF), and `DATA` must be less than or equal to 255 (0xFF) for unsigned, or between 128 and -127 for signed. Negative values will be put in the register as 2's complement values.

Valid:
```
.byte 10 0b11
.byte 0x10 11
.byte 0b10 0x11
```

Invalid:
```
.byte 10
.byte 0x10 500
.byte 2000 0x10
```
The first example has only 1 argument, the second has a value of `DATA` over 256, and the third has an `ADDR` greater than 1023 (0x3FF in hex). 

## .list LENGTH ADDR DATA0 DATA1...
Places a list of length `LENGTH` with `DATA0` at address `ADDR`, `DATA1` at address `ADDR + 1`, etc. The max length for a list is a length of 10, then a new list must be created with another directive. The entries for the list **must** be on the same line to function properly. The length of the list must be in decimal, while the data and address can be in hexadecimal, binary, or decimal.

Valid:
```
.list 5 0x100 0x08 0x09 0x0A 0x0B 0x0C
.list 3 0x200 0x10 0x20 0x30
```

Invalid:
```
.list 3
.list 400 0x0B
.list 6 0xFF 0x0A 0x0B 0x0C 0x0D
0x0E 0x0F
```

In the first example, no address and no list elements are given. In the second, the length is over 10 and there are no list elements. In the third example, an address is given and the length is valid, but the list elements go over multiple lines.
