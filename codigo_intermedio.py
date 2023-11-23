#visitor_yapl.py
from antlr4 import *
from symbol_table import symbol_table, symbol
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from antlr_build.grammarYaplParser import grammarYaplParser
import re

class codigo_intermedio(grammarYaplVisitor):
    def __init__(self, output_file, symbol_tables, symbolic_names):
        super().__init__()
        self.output_file = output_file
        self.symbol_tables = symbol_tables
        self.symbolic_names = symbolic_names
        self.temp_counter = 0  
        self.label_counter = 0 
        self.output_code = []  
        # self.node_types = nodes_types

    def visitProgram(self, ctx:grammarYaplParser.ProgramContext):
        self.last_node_visited = ctx

        for class_def_ctx in ctx.class_def():
            self.visitClass_def(class_def_ctx)

    def visitClass_def(self, ctx:grammarYaplParser.Class_defContext):
        self.last_node_visited = ctx
        class_name = ctx.TYPE_ID(0).getText()
        inherits_from = None

        size = 0

        for table_class in self.symbol_tables.records:
            classTemp = self.symbol_tables.records[table_class]
            if classTemp.id == class_name:
                inherits_from = classTemp.inherit
                size = classTemp.byte

        if len(inherits_from) > 0:
            self.emit(f"CLASS {class_name} INHERITS {inherits_from} SIZE {size}")

        else:
            self.emit(f"CLASS {class_name} SIZE {size}")

        for feature_ctx in ctx.feature():
            if isinstance(feature_ctx, grammarYaplParser.MethodContext):
                self.visitMethod(feature_ctx)
            elif isinstance(feature_ctx, grammarYaplParser.AttributeContext):
                self.visitAttribute(feature_ctx)

        self.emit(f"END CLASS {class_name}\n")


        if class_name == "Main":
            self.emit(f"CALL Main.main")

    def visitMethod(self, ctx:grammarYaplParser.MethodContext):

        if ctx.RBRACE() and ctx.LBRACE():
            self.last_node_visited = ctx
            parametros = []

            function_name = ctx.OBJECT_ID().getText()
            function_class = self.buscar_clase(ctx)
            temp = self.new_temp()

            if ctx.formal():
                for formal_ctx in ctx.formal():
                    parametros.append(self.visitFormal(formal_ctx))

            classTemp = None
            foundTemp = False
            functionTemp = None

            for table_class in self.symbol_tables.records:
                if not foundTemp:
                    classFor = self.symbol_tables.records[table_class]
                    if classFor.id == function_class:
                        classTemp = classFor
                        foundTemp = True

                if foundTemp:
                    classFor = self.symbol_tables.records[table_class]
                    if classFor.id == function_name:
                        functionTemp = classFor
                        break
                    
            trueSize = functionTemp.byte

            self.emit(f"\nFUNCTION {function_class}.{function_name} SIZE {trueSize}")
        
            paramsNum = 0
            if functionTemp.params != []:
                for function in functionTemp.params:
                    self.emit(f"\tsp[{functionTemp.offset}] = {function}.PARAM_{paramsNum}")
                    paramsNum += 1
            
            if ctx.expr():
                result = self.visitExpr(ctx.expr())

            self.emit(f"\tRETURN {result}")
            self.emit(f"END FUNCTION {function_class}.{function_name}")
                    
    def visitAttribute(self, ctx:grammarYaplParser.AttributeContext):
        if ctx.ASSIGN():
            variable_name = ctx.OBJECT_ID().getText()
            var_value = self.visitExpr(ctx.expr())

            class_name = self.buscar_clase(ctx)
            table_class = None

            for table in self.symbol_tables.records:
                classFor = self.symbol_tables.records[table]
                if classFor.id == class_name:
                    table_class = classFor
                    break

            if table_class is not None:
                for table in self.symbol_tables.records:
                    classFor = self.symbol_tables.records[table]
                    if classFor.id == variable_name:
                        offset = classFor.offset
                        self.emit(f"\tsp_GLOBAL[{offset}] = {var_value}")
                        return
        
    def visitFormal(self, ctx:grammarYaplParser.FormalContext):
        self.last_node_visited = ctx

        return

        
        param_name = ctx.OBJECT_ID().getText()
        
        
        if self.buscar_en_tabla(param_name):
            
            existing_type = (self.buscar_en_tabla(param_name))['return_type']
            
            default_value = self.get_default_value_for_type(existing_type)
            self.emit(f"{param_name} = {default_value}")
            return param_name
        else:
            
            
            value = self.visitExpr(ctx.expr())
            temp = self.self.new_temp()
            self.emit(f"{temp} = {value}")
            return temp

    # def visitAddSub(self, ctx:grammarYaplParser.AddSubContext):
    #     left_operand = self.visit(ctx.expr())
    #     right_operand = self.visit(ctx.expr(1))
    #     temp = self.new_temp()

        
    #     if ctx.PLUS():
    #         self.emit(f"\t{temp} = {left_operand} + {right_operand}")
    #     elif ctx.MINUS():
    #         self.emit(f"\t{temp} = {left_operand} - {right_operand}")

    #     return temp

    def visitExpr(self, ctx:grammarYaplParser.ExprContext):
        self.last_node_visited = ctx
        
        if hasattr(ctx, 'DOT'):
            if ctx.DOT():
                # Obtener la expresión base (objeto en el que se invoca el método)
                base_expr = self.visitExpr(ctx.expr(0))

                # Crear un temporal si la base es una creación de objeto
                if "new " in base_expr:
                    temp0 = self.new_temp()
                    self.emit(f"\t{temp0} = {base_expr}")
                    base_expr = temp0

                # Verificar si hay una especificación de tipo con AT
                type_override = None
                if ctx.AT():
                    third_child = ctx.children[2]
                    if third_child.getSymbol().type == self.symbolic_names.index("TYPE_ID"):
                        type_override = third_child.getText()

                # Obtener el nombre del método
                method_name = ctx.OBJECT_ID().getText()

                # Manejo especial para el método 'type_name'
                if method_name == "type_name":
                    # type_element = self.nodes_types[ctx.expr(0)]
                    
                    type_element = self.inferir_tipo(ctx.expr(0))
                    
                    if "Int" in type_element or "String" in type_element or "Bool" in type_element:
                        temp = self.new_temp()
                        self.emit(f"\t{temp} = '{type_element}'")
                        return temp

                # Obtener argumentos si los hay
                arguments = [self.visitExpr(e) for e in ctx.expr()[1:]]

                # Generar código intermedio para la llamada al método
                temp = self.new_temp()
                if type_override:
                    self.emit(f"\t{temp} = CALL {base_expr}@{type_override}.{method_name}({','.join(arg for arg in arguments)})")
                else:
                    self.emit(f"\t{temp} = CALL {base_expr}.{method_name}({','.join(arg for arg in arguments)})")

                return temp
            
        elif hasattr(ctx, 'OBJECT_ID') and hasattr(ctx, 'LPAREN'):
            if ctx.OBJECT_ID() and ctx.LPAREN():
                method_name = ctx.OBJECT_ID().getText()
                
                arguments = [self.visitExpr(e) for e in ctx.expr()]
                
                class_name = self.buscar_clase(ctx)

                if "new " in class_name:
                    temp = self.new_temp()
                    self.emit(f"\t{temp} = {class_name}")

                    temp2 = self.new_temp()
                    self.emit(f"\t{temp2} = CALL {temp}.{method_name}({', '.join(str(arg) for arg in arguments)})")
            
                    return temp2
                
                else:
                    temp = self.new_temp()
                    self.emit(f"\t{temp} = CALL {class_name}.{method_name}({', '.join(str(arg) for arg in arguments)})")
            
                    return temp

        elif hasattr(ctx, 'IF'):
            if ctx.IF():
                condicion = ctx.expr()
                rama_then = ctx.expr(1)
                rama_else = ctx.expr(2)

                condition_temp = self.visitExpr(condicion)
                
                label_then = self.new_label()
                label_else = self.new_label()
                label_continue = self.new_label()

                temp_return = self.new_temp()
                self.emit(f"\tIF {condition_temp} GOTO {label_then}")
                self.emit(f"\tGOTO {label_else}")
                self.emit(f"LABEL {label_then}")

                result_then = self.visitExpr(rama_then)
                self.emit(f"\t{temp_return} = {result_then}")
                self.emit(f"\tGOTO {label_continue}")
                self.emit(f"LABEL {label_else}")

                result_else = self.visitExpr(rama_else)
                self.emit(f"\t{temp_return} = {result_else}")
                self.emit(f"LABEL {label_continue} \n")

                return temp_return
        elif hasattr(ctx, 'WHILE'):
            if ctx.WHILE():
                label_start = self.new_label()
                label_loop = self.new_label()
                label_end = self.new_label()
                self.emit(f"LABEL {label_start}")
                condition_temp = self.visitExpr(ctx.expr())

                if condition_temp is None:
                    a = 5
                self.emit(f"\tIF NOT {condition_temp} GOTO {label_end}")
                self.emit(f"\tGOTO {label_loop}")
                self.emit(f"LABEL {label_loop}")
                self.visitExpr(ctx.expr(1))
                self.emit(f"\tGOTO {label_start}")
                self.emit(f"LABEL {label_end} \n")

                return "Object"
        elif hasattr(ctx, 'LBRACE'):
            if ctx.LBRACE():
                result = None
                for expr_ctx in ctx.expr():
                    result = self.visitExpr(expr_ctx)
                return result

        elif hasattr(ctx, 'LET'):
            if ctx.LET():
                i = 0

                while True:
                    hijo_actual = ctx.children[i]

                    if hijo_actual.getText() == "IN" or hijo_actual.getText() == "in" or hijo_actual.getText() == "In" or hijo_actual.getText() == "iN":
                        result = self.visitExpr(ctx.expr()[-1])
                        return result

                    elif hijo_actual.getSymbol().type == self.symbolic_names.index("OBJECT_ID"):
                        hijo_actual_plus_1 = ctx.children[i + 1]
                        variable_name = hijo_actual.getText()

                        if hijo_actual_plus_1.getSymbol().type == self.symbolic_names.index("COLON"):
                            hijo_actual_plus_2 = ctx.children[i + 2]

                            if hijo_actual_plus_2.getSymbol().type == self.symbolic_names.index("TYPE_ID"):
                                hijo_actual_plus_3 = ctx.children[i + 3]

                                if hijo_actual_plus_3.getSymbol().type == self.symbolic_names.index("ASSIGN"):
                                    hijo_actual_plus_4 = ctx.children[i + 4]
                                    var_value = self.visitExpr(hijo_actual_plus_4)

                                    class_name = self.buscar_clase(ctx)
                                    function_name = self.buscar_funcion(ctx)
                                    table_class = None
                                    table_function = None

                                    for table in self.symbol_tables.records:
                                        table_temp = self.symbol_tables.records[table]
                                        if table_temp.id == class_name:
                                            table_class = self.symbol_tables.records[table]

                                        table_temp = self.symbol_tables.records[table]
                                        if table_temp.id == function_name:
                                            table_function = self.symbol_tables.records[table]
                                            break
                                    if table_class is not None:
                                        if table_class.id == variable_name:
                                            offset = table_class.offset
                                            self.emit(f"\tsp_GLOBAL[{offset}] = {var_value}")
                                    if table_function is not None:
                                        if table_function.id == variable_name:
                                            offset = table_function.offset
                                            self.emit(f"\tsp[{offset}] = {var_value}")

                                    hijo_actual_plus_5 = ctx.children[i + 5]
                                    if hijo_actual_plus_5.getSymbol().type == self.symbolic_names.index("COMMA"):
                                        i += 6
                                    else:
                                        i += 5
                                else:
                                    if hijo_actual_plus_3.getSymbol().type == self.symbolic_names.index("COMMA"):
                                        i += 4
                                    else:
                                        i += 3
                    else:
                        i += 1
        
        elif hasattr(ctx, 'NEW'):
            if ctx.NEW():
                temp = self.new_temp()
                clase = ctx.children[1].getText()
                temp = (f"new {clase}")
                return temp

        elif hasattr(ctx, 'NEG'):
            if ctx.NEG():
                operand = self.visitExpr(ctx.expr())
                temp = self.new_temp()
                self.emit(f"\t{temp} = NEG {operand}")
                return temp
        
        elif hasattr(ctx, 'ISVOID'):
            if ctx.ISVOID():
                
                operand = self.visitExpr(ctx.expr())
                temp = self.new_temp()
                self.emit(f"\t{temp} = isvoid {operand}")
                return temp

        elif hasattr(ctx, 'MULT') or hasattr(ctx, 'DIV'):
            if ctx.MULT() or ctx.DIV():
                left_operand = self.visitExpr(ctx.expr())
                right_operand = self.visitExpr(ctx.expr(1))
                temp = self.new_temp()
                if ctx.MULT():  
                    self.emit(f"\t{temp} = {left_operand} * {right_operand}")
                elif ctx.DIV():  
                    self.emit(f"\t{temp} = {left_operand} / {right_operand}")
                return temp

        elif hasattr(ctx, 'PLUS') and hasattr(ctx, 'MINUS'):
            if ctx.PLUS() or ctx.MINUS():
                left_operand = self.visitExpr(ctx.expr())
                right_operand = self.visitExpr(ctx.expr(1))
                temp = self.new_temp()
                if ctx.PLUS():
                    self.emit(f"\t{temp} = {left_operand} + {right_operand}")
                elif ctx.MINUS():
                    self.emit(f"\t{temp} = {left_operand} - {right_operand}")
                return temp

        # elif isinstance(ctx, grammarYaplParser.MinusContext):
        #     operand = self.visitExpr(ctx.expr())
        #     temp = self.new_temp()
        #     self.emit(f"\t{temp} = - {operand}")
        #     return temp

        elif hasattr(ctx, 'EQ') or hasattr(ctx, 'LE') or hasattr(ctx, 'LT'):
            if ctx.EQ() or ctx.LE() or ctx.LT():
                left_operand = self.visitExpr(ctx.expr())
                right_operand = self.visitExpr(ctx.expr(1))
                temp = self.new_temp()
                if ctx.EQ():
                    left_operand = self.visitExpr(ctx.expr())
                    right_operand = self.visitExpr(ctx.expr(1))
                    temp = self.new_temp()
                    self.emit(f"\t{temp} = {left_operand} == {right_operand}")
                elif ctx.LE():
                    self.emit(f"\t{temp} = {left_operand} <= {right_operand}")
                elif ctx.LT():  
                    self.emit(f"\t{temp} = {left_operand} < {right_operand}")
                return temp

        elif hasattr(ctx, 'NOT'):      
            if ctx.NOT():
                operand = self.visitExpr(ctx.expr())
                temp = self.new_temp()
                self.emit(f"\t{temp} = NOT {operand}")
                return temp
        
        elif hasattr(ctx, 'ASSIGN'):
            if ctx.ASSIGN():
                variable_name = ctx.OBJECT_ID().getText()
                var_value = self.visit(ctx.expr())

                class_name = self.buscar_clase(ctx)
                function_name = self.buscar_funcion(ctx)
                table_class = None
                table_function = None

                for table in self.symbol_tables.records:
                    table_temp = self.symbol_tables.records[table]
                    if table_temp.id == class_name:
                        table_class = self.symbol_tables.records[table]

                    table_temp = self.symbol_tables.records[table]
                    if table_temp.id == function_name and table_class is not None:
                        table_function = self.symbol_tables.records[table]
                        break
                        
                if table_class is not None:
                    if table_class.id == variable_name:
                        offset = table_class.offset
                        self.emit(f"\tsp_GLOBAL[{offset}] = {var_value}")
                        return f"sp_GLOBAL[{offset}]"

                if table_function is not None:
                    if table_class.id == variable_name:
                        offset = table_class.offset
                        self.emit(f"\tsp[{offset}] = {var_value}")
                        return f"sp[{offset}]"
        
        elif hasattr(ctx, 'LPAREN'):
            if ctx.LPAREN():
                return self.visitExpr(ctx.expr())

        elif hasattr(ctx, 'OBJECT_ID'):
            if ctx.OBJECT_ID():
                variable_name = ctx.OBJECT_ID().getText()

                class_name = self.buscar_clase(ctx)
                function_name = self.buscar_funcion(ctx)
                table_class = None
                table_function = None

                for table in self.symbol_tables.records:
                    table_temp = self.symbol_tables.records[table]
                    if table_temp.id == class_name:
                        table_class = self.symbol_tables.records[table]
                    table_temp = self.symbol_tables.records[table]
                    if table_temp.id == class_name and table_class is not None:
                        table_function = self.symbol_tables.records[table]
                        break

                if table_class is not None:
                    if table_class.id == variable_name:
                        offset = table_class.offset
                        return f"sp_GLOBAL[{offset}]"

                if table_function is not None:
                    if table_function.id == variable_name:
                        offset = table_class.offset
                        return f"sp[{offset}]"
                            
                if "num" in variable_name:
                    return variable_name

                temp = self.new_temp()
                self.emit(f"\t{temp} = {variable_name}")
                return temp

        elif isinstance(ctx, grammarYaplParser.SelfContext):
            # Obtener el nombre de la clase actual
            # Obtener el nombre de la clase actual para 'self'
            class_name = self.buscar_clase(ctx)

            if hasattr(ctx.parentCtx, 'DOT'):
                method_or_attribute_name = ctx.parentCtx.OBJECT_ID().getText()
                
            else:
                variable_name = ctx.getText()
                # variable_name = ctx.parentCtx.OBJECT_ID().getText()                    
                if "num" in variable_name:
                    return variable_name

                temp = self.new_temp()
                self.emit(f"\t{temp} = {variable_name}")
                return temp
        
        elif hasattr(ctx, 'INTEGER'):
            if ctx.INTEGER():
                return ctx.INTEGER().getText()
        
        elif hasattr(ctx, 'STRING'):
            if ctx.STRING():
                return ctx.STRING().getText()
        
        elif hasattr(ctx, 'TRUE') and hasattr(ctx, 'FALSE'):
            if ctx.TRUE() or ctx.FALSE():
                if ctx.TRUE():
                    return ctx.TRUE().getText()
                elif ctx.FALSE():
                    return ctx.FALSE().getText()
         
    def new_temp(self):
        self.temp_counter += 1
        return f"%t{self.temp_counter}%"
    
    def new_label(self):
        self.label_counter += 1
        return f"label{self.label_counter}"

    def emit(self, code):
        
        self.output_code.append(code)

    def get_default_value_for_type(self, type_name: str):
        default_values = {
            "Int": "0",
            "String": '""',
            "Bool": "false",
        }

        
        return default_values.get(type_name, "None")
    
    def buscar_en_tabla(self, name):
        for symbol in self.symbol_tables:
            if symbol['keyId'].split('.')[-1] == name:
                return symbol
        return None
                
    def buscar_clase(self, ctx):
        clase = ""
        nodo = ctx

        while nodo.parentCtx is not None:
            if isinstance(nodo.parentCtx, grammarYaplParser.Class_defContext):
                clase = nodo.parentCtx.children[1].getText() 
                break

            nodo = nodo.parentCtx
            
        return clase
    
    def write_to_file(self):
        
        self.output_code = self.reduce_labels(self.output_code)

        self.output_code = self.temps_to_registers(self.output_code)

        
        with open("test/codigoIntermedio/" + self.output_file + ".txt", 'w') as file:
            file.write('\n'.join(self.output_code))

        return self.output_code

    def extract_temp_vars(self, input_string):
        pattern = r'%t\d+%'
        temp_vars = re.findall(pattern, input_string)
        unique_temp_vars = list(set(temp_vars))

        return unique_temp_vars

    def reduce_labels(self, code):
        variables = {}
        new_code = []
        temp_vars = ["%t"+str(i)+"%" for i in range(1, len(code) + 1)]
        using_temp_vars = []
        first_pass = True

        for i in range(len(code)):
            
            line = code[i].lstrip().split()
            temp_var = ""

            
            full_text = " ".join(code[i:])
            temp_vars_in_line = self.extract_temp_vars(full_text)
            for var in using_temp_vars:
                if var not in temp_vars_in_line:
                    using_temp_vars.remove(var)
                    temp_vars.append(var)

            
            
            if len(line) >= 3 and line[1] == "=" and re.match(r"%t\d+%", line[0]):
                temp_var = line[0]

            else:
                new_code.append(code[i])
                continue

            
            available_var = None
            if temp_var in temp_vars:
                for temp in temp_vars:
                    if temp not in code[i] or first_pass:
                        available_var = temp
                        first_pass = False
                        break

                if available_var is None:
                    
                    available_var = f"t{len(temp_vars) + 1}"
                    temp_vars.append(available_var)

                line[0] = available_var

                found = False
                for j in range(i+1, len(code)):
                    code_temp = code[j]
                    if temp_var in code[j]:
                        code[j] = code[j].replace(temp_var, available_var)
                        found = True
                
                if found:
                    temp_vars.remove(available_var)
                    using_temp_vars.append(available_var)

            
            vars_in_line = self.extract_temp_vars(" ".join(line))

            for var in vars_in_line:
                found = False

                for j in range(i+1, len(code)):
                    if var in code[j]:
                        found = True
                        break

                if not found:
                    if var not in temp_vars:
                        temp_vars.append(var)

                    if var in using_temp_vars:
                        using_temp_vars.remove(var)
                else:
                    if var in temp_vars:
                        temp_vars.remove(var)
                    if var not in using_temp_vars:
                        using_temp_vars.append(var)

            
            temp_vars.sort(key=lambda x: int(x[2:-1]))

            new_code.append('\t'+" ".join(line))

        return new_code

    def temps_to_registers(self, code):
        output_code = []

        for code in self.output_code:
            
            temps = self.extract_temp_vars(code)

            
            for temp in temps:
                code = code.replace(temp, f"REGISTRO[{(int(temp[2:-1]) - 1) * 4}]")
            
            output_code.append(code)

        return output_code
    
    def buscar_funcion(self, ctx):
        funcion = ""
        nodo = ctx

        while nodo.parentCtx is not None:
            if isinstance(nodo.parentCtx, grammarYaplParser.FeatureContext):
                funcion = nodo.parentCtx.children[0].getText()
                break

            nodo = nodo.parentCtx
        
        return funcion
    
    def inferir_tipo(self, expr_ctx):
        # 
        if isinstance(expr_ctx, grammarYaplParser.ParenthesisContext):
            # Recursivamente llama a inferir_tipo con la expresión dentro de los paréntesis
            return self.inferir_tipo(expr_ctx.expr())
        # Si expr_ctx es un literal numérico, cadena o booleano
        if isinstance(expr_ctx, grammarYaplParser.IntegerContext):
            return "Int"
        elif isinstance(expr_ctx, grammarYaplParser.StringContext):
            return "String"
        elif isinstance(expr_ctx, grammarYaplParser.BoolContext):
            return "Bool"
        # Si expr_ctx es un contexto de 'isvoid'
        elif isinstance(expr_ctx, grammarYaplParser.IsvoidContext):
            # Normalmente, el resultado de 'isvoid' sería un booleano
            return "Bool"

        # Si expr_ctx es un identificador de objeto
        elif isinstance(expr_ctx, grammarYaplParser.Object_idContext):
            # Buscar el símbolo en la tabla de símbolos y devolver su tipo
            nombre_objeto = expr_ctx.getText()
            simbolo = None
            for i in self.symbol_tables.records:
                temp = self.symbol_tables.records[i]
                if temp.id == nombre_objeto:
                    simbolo = i
            if simbolo:
                return simbolo.type
            else:
                return "Unknown"

        # Si expr_ctx es una llamada a función o método
        elif hasattr(expr_ctx, 'DOT') or (hasattr(expr_ctx, 'OBJECT_ID') and hasattr(expr_ctx, 'LPAREN')):
            nombre_metodo = expr_ctx.OBJECT_ID(0).getText()
            simbolo_metodo = None
            for i in self.symbol_tables.records:
                temp = self.symbol_tables.records[i]
                if temp.id == nombre_metodo:
                    simbolo_metodo = i
            if simbolo_metodo and simbolo_metodo.returnType is not None:
                return simbolo_metodo.returnType
            else:
                return "Unknown"

        # Si expr_ctx es una creación de instancia (new Object)
        elif isinstance(expr_ctx, grammarYaplParser.NewContext):
            nombre_clase = expr_ctx.TYPE_ID().getText()
            simbolo_clase = None
            for i in self.symbol_tables.records:
                temp = self.symbol_tables.records[i]
                if temp.id == nombre_clase:
                    simbolo_clase = i
            if simbolo_clase:
                return nombre_clase 

        # Caso por defecto
        else:
            # Retorna un tipo genérico o desconocido
            return "Unknown"

