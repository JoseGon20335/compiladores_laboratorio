import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import subprocess
import os
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
import antlr4
from prettytable import PrettyTable
from antlr_build.grammarYaplLexer import grammarYaplLexer
from antlr_build.grammarYaplParser import grammarYaplParser
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from visitor_yapl import visitor_yapl
from reader import *
from prettytable import PrettyTable

class YAPLCompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YAPL Compiler")
        self.root.configure(bg="#48494B")  

        # Número de líneas de código
        self.line_numbers = tk.Text(root, width=4, bg="#48494B", fg="#FFFFFF", font=("Courier New", 11), bd=0, highlightthickness=0)
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y, pady=10)
        self.line_numbers.tag_configure("center", justify="right")

        # Consola de entrada para código
        self.code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20, font=("Courier New", 11), bg="#011627", fg="#149414")
        self.code_input.config(insertbackground='white')
        self.code_input.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.code_input.tag_configure("line", justify="left")
        self.code_input.bind("<Key>", self.on_key_press) # Actualizar el número de líneas cuando se presiona una tecla
        self.code_input["yscrollcommand"] = self.update_line_numbers
        self.update_line_numbers()


        # Generate Syntax Tree button
        self.generate_tree_button = tk.Button(root, text="Syntax Tree", command=self.generate_tree)
        self.generate_tree_button.pack(pady=10)

        # Consola de salida
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20, font=("Courier New", 11), bg="#000000", fg="white")
        self.output_text.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.output_text.config(state=tk.DISABLED)  # Make the output text read-only

    def update_line_numbers(self, *args):
        # Como el número de líneas puede cambiar, se actualiza cada vez que se presiona una tecla
        # De esta forma, se mantiene actualizado el número de líneas
        line_count = str(self.code_input.get(1.0, tk.END)).count("\n") - 1 # -1 para quitar la línea en blanco al final (o al inicio)
        if line_count == 0:
            line_numbers_text = "1"
        else:
            line_numbers_text = "\n".join(str(i) for i in range(1, line_count + 2))
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete("1.0", tk.END)
        self.line_numbers.insert(tk.END, line_numbers_text)
        self.line_numbers.config(state=tk.DISABLED) # Read-only

    def on_key_press(self, event):
        self.update_line_numbers()

    def generate_tree(self):
        input_text = self.code_input.get(1.0, tk.END)
        #print(input_text)

        # Create a stream of characters from the input text
        input_stream = InputStream(input_text)

        # Create a lexer that reads from the input stream
        lexer = grammarYaplLexer(input_stream)

        # remove error listeners
        lexer.removeErrorListeners()

        # create a custom error listener
        error_listener = CustomErrorListener()

        # add the custom error listener
        lexer.addErrorListener(error_listener)

        # Create a token stream from the lexer
        token_stream = antlr4.CommonTokenStream(lexer)
        token_stream.fill()

        # # Create a parser that reads from the token stream
        # parser = grammarYaplParser(token_stream)
        # # Create an instance of your custom error listener
        # error_listener = CustomErrorListener()
        # # Attach the error listener to the parser
        # parser.addErrorListener(error_listener)
        # # Invoke the parser starting at the entry rule
        # tree = parser.program()
        error_output = ""
        for i in error_listener.return_errors():
            error_output += i + "\n"

        #print(tree.toStringTree(recog=parser))
        print("hola wena tarde")
        # Check if any syntax errors occurred
        if error_listener.has_errors:
            # Display the error messages in the output text
            error_message = "\n".join(error_output)
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, error_message)
            self.output_text.config(state=tk.DISABLED)
        else:
            # No syntax errors, proceed with generating the syntax tree
            # ...
            cmd = 'antlr4-parse antlr_build/grammarYapl.g4 program -gui'
            # Process and show the tree
            #self.run_command_with_input(cmd, input_text)
            responce = self.generate_table(input_text)
            
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, responce)
            self.output_text.config(state=tk.DISABLED)

    def run_command_with_input(self, cmd, input_text):
        # Start the command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

        program = 'program'

        # Send input text followed by ENTER
        process.stdin.write(input_text.encode())
        process.stdin.write(os.linesep.encode())
        process.stdin.flush()

        # Send program class defnition
        process.stdin.write(program.encode())
        process.stdin.write(os.linesep.encode())
        process.stdin.flush()

        # Send CTRL+Z
        process.stdin.write(chr(26).encode())
        process.stdin.flush()

        # Wait for the command to complete
        stdout, stderr = process.communicate()

        # Print the output and error messages
        decode = stdout.decode() + ' ' + stderr.decode()
        self.output_text.insert(tk.END, decode)

    # Read Tree and give table of symbols
    def generate_table(self, input_text):

        input_stream = InputStream(input_text)
        reader_instance = reader(input_stream)
        
        reader_instance.readTokensSintaxis()
        res = reader_instance.readSymbolTable()
        
        print(res)

        return res
        

if __name__ == "__main__":
    root = tk.Tk()
    gui = YAPLCompilerGUI(root)
    root.mainloop()