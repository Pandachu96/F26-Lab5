# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 10/21/2026
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
# TO DO 2: Follow the instructions from the readme.me file to create the exact output.
with open("pythonStatements.txt", "r") as python_statements_file:
    python_statements = python_statements_file.readlines()
    for statement in python_statements:
        with open("output.txt", "a") as output_file:
            with open("machineCode.txt", "r") as machine_code_file:
                machine_code = machine_code_file.readlines()
                output_file.write(statement.split('#')[0].strip() + '\t' + 
                machine_code[python_statements.index(statement)].strip() + '\n')