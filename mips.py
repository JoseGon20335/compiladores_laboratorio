import re

class MIPS:
    def __init__(self, codigo_intermedio, symbol_table):
        self.codigo_intermedio = codigo_intermedio
        self.symbol_table = symbol_table
        self.code = [".code"]
        self.temp_stack = []
        self.counter = 0
        self.temp_usage ={
            f"$t{i}": False for i in range(9)
        }
        self.temp_if = 0