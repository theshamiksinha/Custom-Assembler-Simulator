# GIGAssembler
## Assembly-to-Binary Assembler

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
