from codes import CPU, assemble
import sys

skip = False
filename = None

def help_menu():
    print("REQUIRED: ")
    print("-f [filename]: pass in a filename to assemble (no spaces)")
    print("OPTIONAL: ")
    print("-h: print this help menu")
    print("-s: skips inputting commands")

if len(sys.argv) == 1:
    help_menu()
    exit(0)

if len(sys.argv) != 1:
    if sys.argv[1] == "-h":
        help_menu()
        exit(0)

    if "-s" in sys.argv:
        skip = True
    
    if "-f" in sys.argv:
        idx = sys.argv.index("-f")
        filename = sys.argv[idx + 1]

if filename is None:
    print("Please enter a filename using the -f flag.")
    exit(1)

args = assemble(filename)
cpu = CPU(*args)

def menu():
    print("Available commands:")
    print("If stuck in an infinite loop, CTRL+C or CMD+. to stop the program completely.")
    print("Enter memory address in hexadecimal prefixed by 0x to output that memory value.")
    print("To see multiple values, input [ADDR] - [ADDR], (ex. 0x5 - 0x10). Limit of 15 values at once.")
    print("Enter Q, quit, E or exit to stop execution. Enter nothing or S to step. Enter C or continue to continue until the end of execution.")
    print("Enter P or print to print the state of the cpu. Enter H or help for a reminder of this menu.\n")


if not skip:
    menu()

while True:
    print(cpu)
    cont = False
    done = False
    if not skip:
        while not cont:
            inp = input("Command: ")
            print() 
            inp = inp.strip().upper()
            if inp.find("X") != -1:
                # multiple memory addresses
                if inp.find("-") != -1:
                    addrs = inp.split(" - ")
                    if(len(addrs) < 2):
                        print("Wrong number of memory addresses. Must input \"[ADDR] - [ADDR]\", ex. \"0x5 - 0x10\".")
                        continue
                    addr1 = int(addrs[0], 0)
                    addr2 = int(addrs[1], 0)
                    if not (0 <= addr1 <= 1023) or not (0 <= addr2 <= 1023):
                        print("Invalid memory address")
                        continue
                    if addr2 < addr1:
                        print("Second memory address is less than the second.")
                        continue
                    if(addr2 - addr1 > 14):
                        print("Trying to print too much data. Printing only first 15 addresses:")
                        addr2 = addr1 + 14
                    for i in range(addr1, addr2 + 1):
                        data = cpu._memory[i]
                        if(i - addr1) % 5 != 4 and i != addr2:
                            print(f"{hex(i)}: {hex(data)} | ", end='')
                        else:
                            print(f"{hex(i)}: {hex(data)}")
                    print()
                    continue
                # singular memory address
                try:
                    addr = int(inp, 0)
                    if not 0 <= addr <= 1023:
                        raise ValueError()
                    
                    data = cpu._memory[addr]
                    print(f"{hex(addr)}: {hex(data)} ({data} in base 10)")
                except ValueError:
                    print("Invalid memory address")
                    continue
            if inp == "Q" or inp == "QUIT":
                print("Stopping execution")
                print(cpu)
                exit()
            if inp == "H" or inp == "HELP":
                menu()
            if done:
                continue
            if inp == "S" or inp == "":
                cont = True
            if inp == "C" or inp == "CONTINUE":
                cont = True
                skip = True
            if inp == "P" or inp == "PRINT":
                print(cpu)
    try:
        if not done:
            cpu.step()
    except Exception as e:
        if isinstance(e, EOFError):
            print("Execution over: You can still probe memory. Input Q to quit.")
            cont = False
            skip = False
            continue
        inst = cpu._program[cpu._index]
        print(f"Error in instruction: {inst}")
        print(e)
        exit()

