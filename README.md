# GIGAssembler and simulator
## P-1 Assembly-to-Binary Assembler

This is an Assembly-to-Binary Assembler written in Python 3. It takes an input file code.txt containing assembly code and generates the corresponding binary code in the output file output.txt. If there are any errors in the assembly code, the assembler will print the errors and write them to output.txt as well.


This project is part of a college group project and is designed to fulfill the requirements specified in the instruction.pdf file, which provides the correct format and guidelines for writing assembly code.
## Prerequisites

To run the assembler, you need to have Python 3 installed on your system. You can check if Python is installed by running the following command in your terminal:

    python3 --version

If Python is not installed, you can download and install it from the official Python website: https://www.python.org/downloads/
## Usage

Place your assembly code in a file named code.txt. Make sure the assembly code follows the appropriate syntax and conventions.

Run the assembler by executing the following command in your terminal:

    python3 assembler.py

The assembler will read the code.txt file, process the assembly code, and generate the corresponding binary code in the output.txt file.

After execution, check the output.txt file for the generated binary code. If any errors were encountered during assembly, they will be printed and written to output.txt as well.

## Example
Here's an example of how the assembly code and output files would look like:

### "code.txt" (Input - Assembly Code)

    var var1
    var var2
    var var3
    ld R1 var1
    ld R2 var2
    st R3 var3
    jmp hlt_label
    add R1 R2 R3
    hlt_label: hlt
### "output.txt" (Output - Binary Code)
    0010000010000001
    0010000100000010
    0010100110000011
    0111100000000101
    0000000001010011
    1101000000000000
## P2 Simulator
The simulator should load a binary file into system memory and execute the code starting from address 0 until it encounters a "hlt" instruction.

Here's an overview of the distinct components mentioned in the question:

1) Memory (MEM): The memory component stores 256 bytes, initialized to 0s. It has read and write operations to access the data stored at a specific address.

2) Program Counter (PC): The program counter is a 7-bit register that keeps track of the current instruction's address. It is used to fetch the instruction from memory and update its value to point to the next instruction.

3) Register File (RF): The register file component is responsible for storing and accessing the values of different registers. It has 7 general-purpose registers (R0, R1, ..., R6) and a FLAGS register. The RF component provides read and write operations for these registers.

4) Execution Engine (EE): The execution engine fetches instructions from memory using the program counter, decodes the instruction, and executes it accordingly. It interacts with the memory and register file to perform operations specified by each instruction.

To solve this task, we can implement these components as separate classes: Memory, ProgramCounter, RegisterFile, and ExecutionEngine. The simulator will read the binary file, load it into memory, and start executing the instructions. After each instruction, it will output the program counter value and the values of the registers. Finally, it will print the memory dump of the entire memory.

have provided the Python code that implements these components and performs the simulation. You can run the code by providing a binary file as input, and it will execute the instructions, printing the program counter and register values, and displaying the memory dump.

Please make sure to adapt the code to match the specific instruction set and binary file format of your ISA, as the code provided is a general structure based on the given requirements.
