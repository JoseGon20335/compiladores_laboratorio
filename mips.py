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

    def generate(self):

        self.code.insert(1, "\n# VIRTUAL TABLES")

        self.method_table = {}
        actual = None
        method_temp = []

        for line in self.codigo_intermedio:
            
            tempT = []

            current = ""
            stringFlag = False

            for i in line:
                if i == " " and not stringFlag:
                    tempT.append(current)
                    current = ""
                elif i == '"':
                    stringFlag = not stringFlag
                    current += i
                else:
                    current += i

            if current != "":
                tempT.append(current)

            if tempT[0] == "CLASS":
                if actual != None:
                    self.method_table[actual] = method_temp
                    method_temp = []

                actual = tempT[1]
                hereda = None

                if "INHERITS" in tempT[2]:
                    if len(tempT[3].split(",")) > 1:
                        hereda = tempT[3].split(",")[0]
                        hereda.replace("'", "")
                        hereda.replace("[", "")
                        hereda.replace("]", "")
                    else:
                        hereda = tempT[3].replace("'", "")
                        hereda.replace("[", "")
                        hereda.replace("]", "")


                    for key, value in self.method_table.items():
                        if key == hereda:
                            for i in self.method_table[key]:
                                method_temp.append(i)
            if "FUNCTION" in tempT[0]:
                actual = tempT[1].split(".")[1]
                method_temp_function = []
                for i in method_temp:
                    newAdd = i.split(".")[1]
                    method_temp_function.append(i)

                if actual not in method_temp_function:
                    method_temp.append(tempT[1])

                else:
                    indexTemp = method_temp_function.index(actual)
                    method_temp[indexTemp] = tempT[1]

        self.method_table[actual] = method_temp
        
        for key, value in self.method_table.items():
            self.code.append(f"vy_{key}:")
            for i in value:
                self.code.append(f"     . word {i}")

        for key, value in self.method_table.items():
            for i in range(len(value)):
                value[i] = value[i].split(".")[1]

        self.code.append("")
        self.code.append(".text")
        self.code.append("")
        self.code.append("main:")
        self.code.append("    jal CLASS_Main")
        self.code.append("")

        self.declare_class = False
        self.is_first_class = True

        # Agregar funciones de básicas
        self.code.append("\n# ------> FUNCIONES BÁSICAS")

        # out_string
        self.code.append("out_string:")
        self.code.append(f"    li $v0, 4")         # Código de syscall para imprimir una cadena
        self.code.append(f"    syscall")           # Imprimir la cadena
        self.code.append(f"    jr $ra\n\n")        # Regresar al caller

        # out_int
        self.code.append("out_int:")
        self.code.append(f"    li $v0, 1")         # Código de syscall para imprimir un entero
        self.code.append(f"    syscall")           # Imprimir el entero
        self.code.append(f"    jr $ra\n\n")        # Regresar al caller

        # substr
        self.code.append("substr:")
        self.code.append("    move $a0, $s1")      # Mover la dirección de la cadena al registro $a0
        self.code.append("    move $a1, $s2")      # Mover la posición inicial al registro $a1
        self.code.append("    move $a2, $s3")      # Mover la longitud al registro $a2
        self.code.append(f"    li $s4, 0")         # Inicializar el contador en 0 para el ciclo
        self.code.append("    add $s5, $s2, $s3")  # Sumar la posición inicial y la longitud para obtener la posición final

        # Reservar espacio en el heap para la nueva subcadena
        self.code.append("\n# ------> RESERVAR ESPACIO EN EL HEAP PARA LA NUEVA SUBCADENA")
        self.code.append("    addi $a2, $a2, 1")   # Aumentar la longitud en 1 para el carácter nulo
        self.code.append("    move $a0, $a2")      # Mover la longitud al registro $a0
        self.code.append("    li $v0, 9")          # Syscall para sbrk
        self.code.append("    syscall")            # Reservar espacio en el heap
        self.code.append("    move $s6, $v0")      # Mover la dirección del heap al registro $s6
        self.code.append("    move $t5, $s6")

        # Copiar los caracteres de la cadena original a la nueva subcadena
        self.code.append("\n# ------> COPIAR LOS CARACTERES DE LA CADENA ORIGINAL A LA NUEVA SUBCADENA")
        self.code.append("substr_loop:")
        self.code.append("    beq $s4, $s5, substr_end")  # Si el contador es igual a la posición final, terminar el ciclo
        self.code.append("    blt $s4, $s2, skip_char")  # Si el contador es menor continuar el ciclo

        self.code.append("\n# ------> COPIAR CARACTERES")
        self.code.append("    lb $t3, 0($s1)")      # Cargar el carácter de la cadena original
        self.code.append("    sb $t3, 0($s6)")      # Guardar el carácter en la nueva subcadena
        self.code.append("    addi $s6, $s6, 1")    # Incrementar el contador

        self.code.append("\n# ------> SALTO DE CARACTERES")
        self.code.append("skip_char:")
        self.code.append("    addi $s4, $s4, 1")   # Incrementar el contador
        self.code.append("    addi $s1, $s1, 1")   # Incrementar la dirección de la cadena
        self.code.append("    j substr_loop")      # Regresar al inicio del ciclo

        # substr_end
        self.code.append("\n# ------> TERMINAR LA FUNCIÓN substr")
        self.code.append("substr_end:")
        self.code.append("    sb $zero, 0($s6)")          # Agregar el carácter nulo al final de la nueva subcadena
        self.code.append("    move $v0, $t5")             # Mover la dirección de la nueva subcadena al registro $v0
        self.code.append("    jr $ra\n\n")                # Regresar al caller

        self.code.append("\n# ------> SAVE REGISTROS TEMPORALES EN EL STACK")
        self.code.append("save_registers:")
        self.code.append("    addi $sp, $sp, -36")  # Decrementar el stack pointer
        self.code.append("    sw $t0, 0($sp)")      # Guardar el valor de $t0 en el stack
        self.code.append("    sw $t1, 4($sp)")      # Guardar el valor de $t1 en el stack
        self.code.append("    sw $t2, 8($sp)")      # Guardar el valor de $t2 en el stack
        self.code.append("    sw $t3, 12($sp)")     # Guardar el valor de $t3 en el stack
        self.code.append("    sw $t4, 16($sp)")     # Guardar el valor de $t4 en el stack
        self.code.append("    sw $t5, 20($sp)")     # Guardar el valor de $t5 en el stack
        self.code.append("    sw $t6, 24($sp)")     # Guardar el valor de $t6 en el stack
        self.code.append("    sw $t7, 28($sp)")     # Guardar el valor de $t7 en el stack
        self.code.append("    sw $t8, 32($sp)")     # Guardar el valor de $t8 en el stack
        self.code.append("    jr $ra\n\n")          # Regresar al caller

        self.code.append("\n# ------> RESTAURAR REGISTROS TEMPORALES DEL STACK")
        self.code.append("restore_registers:")
        self.code.append("    lw $t0, 0($sp)")      # Cargar el valor de $t0 desde el stack
        self.code.append("    lw $t1, 4($sp)")      # Cargar el valor de $t1 desde el stack
        self.code.append("    lw $t2, 8($sp)")      # Cargar el valor de $t2 desde el stack
        self.code.append("    lw $t3, 12($sp)")     # Cargar el valor de $t3 desde el stack
        self.code.append("    lw $t4, 16($sp)")     # Cargar el valor de $t4 desde el stack
        self.code.append("    lw $t5, 20($sp)")     # Cargar el valor de $t5 desde el stack
        self.code.append("    lw $t6, 24($sp)")     # Cargar el valor de $t6 desde el stack
        self.code.append("    lw $t7, 28($sp)")     # Cargar el valor de $t7 desde el stack
        self.code.append("    lw $t8, 32($sp)")     # Cargar el valor de $t8 desde el stack
        self.code.append("    addi $sp, $sp, 36")   # Incrementar el stack pointer
        self.code.append("    jr $ra\n\n")          # Regresar al caller

        for line in self.intermediate_code:
            # Separar la línea en tokens; pero no separar los strings
            tokens = []

            current_token = ""
            inside_string = False

            for char in line:
                if char == " " and not inside_string:
                    tokens.append(current_token)
                    current_token = ""
                elif char == '"':
                    inside_string = not inside_string
                    current_token += char
                else:
                    current_token += char
            if current_token:  # Añadir el último token si no está vacío
                tokens.append(current_token)

            # ----------------- DECLARAR CLASE -----------------
            if "CLASS" in line:
                
                self.inside_first_func = True

                if self.first_class:

                    clases = ["Object", "IO"]

                    for clase in clases:

                        # Crear clase Object antes de la primera clase
                        self.code.append(f"\n# ------> CREAR CLASE {clase}")
                        self.code.append(f"CLASS_{clase}:")  # Llamar a la clase

                        size = 8  # +4 para el tipo de la clase + 4 para tabla virtual
                        self.last_class_size = size

                        reg = self.return_next_register()  # Obtener un registro temporal para el tamaño

                        self.code.append(f"\n# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE Object")
                        self.code.append(f"    li $a0, {size}")    # Tamaño de la clase
                        self.code.append("    li $v0, 9")       # syscall para sbrk (reservar espacio en el heap
                        self.code.append("    syscall")         # Realizar syscall
                        self.code.append(f"    move {reg}, $v0")  # Mover la dirección del heap al registro temporal

                        # Guardar en un espacio de heap el nombre de la clase
                        heap_reg = self.heap_save_string(clase)
                        self.code.append(f"    sw {heap_reg}, 0({reg})")  # Guardar el nombre de la clase en el heap

                        self.code.append("    move $s6, $s7")          # Cambiar s7 a s6
                        self.code.append(f"    move $s7, {reg}")       # Guardar la dirección de la instancia de la clase en $s7

                        self.liberated_register(reg)                               # Liberar el registro temporal
                        self.liberated_register(heap_reg)                           # Liberar el registro temporal

                        # Regresar a donde se estaba
                        self.code.append("    jr $ra\n")

                        self.first_class = False

                if "END" not in tokens[0]:
                    self.class_before_func = True
                    self.global_vars = {}

                    # Al inicio de la clase
                    class_name = tokens[1]
                    self.code.append(f"\nCLASS_{class_name}:")

                    size = int(tokens[-1]) + 8  # +4 para el tipo de la clase
                    self.last_class_size = size

                    reg = self.return_next_register()  # Obtener un registro temporal para el tamaño

                    self.code.append(f"\n# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE {class_name}")
                    self.code.append(f"    li $a0, {size}")    # Tamaño de la clase
                    self.code.append("    li $v0, 9")       # syscall para sbrk (reservar espacio en el heap
                    self.code.append("    syscall")         # Realizar syscall
                    self.code.append(f"    move {reg}, $v0")  # Mover la dirección del heap al registro temporal
                    
                    # Guardar en un espacio de heap el nombre de la clase
                    heap_reg = self.heap_save_string(class_name)
                    self.code.append(f"    sw {heap_reg}, 0({reg})")  # Guardar el nombre de la clase en el heap

                    # Guardar en un espacio de heap la tabla virtual
                    self.code.append(f"    la $t0, vt_{class_name}")
                    self.code.append(f"    sw $t0, 4({reg})")  # Guardar la dirección de la tabla virtual en el heap


                    if "Main" in class_name:
                        self.code.append(f"    move $s7, {reg}")     # Guardar la dirección de la instancia de la clase en $s7
                        self.class_dec = True
                    else:
                        # mover s7 a s6
                        self.code.append("    move $s6, $s7")          # Cambiar s7 a s6
                        self.code.append(f"    move $s7, {reg}")       # Guardar la dirección de la instancia de la clase en $s7

                    self.liberated_register(reg)                               # Liberar el registro temporal
                    self.liberated_register(heap_reg)                           # Liberar el registro temporal

            # ----------------- DECLARAR FUNCIONES -----------------
            elif "FUNCTION" in line:

                self.inside_first_func = False

                if "END" in tokens[0]:
                    # Al final de la función
                    self.code.append(f"\n# ------> FIN DE LA FUNCIÓN {tokens[2]}")
                    self.code.append("    move $sp, $fp")  # Restaurar el stack pointer al frame pointer actual
                    self.code.append("    lw $fp, 0($sp)")  # Restaurar el frame pointer al valor previo
                    self.code.append("    lw $ra, 4($sp)") # Restaurar el return address
                    self.code.append("    addi $sp, $sp, 8")  # Ajustar el stack pointer después de recuperar el frame pointer


                    if "Main.main" not in tokens[2]:
                        # Regresar al caller
                        self.code.append("    jr $ra\n")       

                else:        
                    # 'size' es el espacio necesario para las variables locales
                    size = int(tokens[-1]) + 4 # +4 para almacenar clase que llama a la función

                    self.last_function_size = size

                    if(self.class_dec):
                        # Pasarle como parámetro la dirección de la clase
                        self.code.append("    jal Main.main\n")

                        self.class_dec = False
                        self.class_before_func = False

                        # ------- Agregar Funciones Personalizadas de la Clase --------

                    elif(self.class_before_func):
                        self.code.append(f"    jr $ra\n")
                        self.class_before_func = False


                    self.code.append(f"\n{tokens[1]}:")

                    if "Main.main" not in tokens[1]:
                        self.code.append("    move $s1, $a0")

                    self.code.append(f"# ------> INICIALIZAR MEMORIA DE LA FUNCIÓN {tokens[1]}")
                    self.code.append("    addi $sp, $sp, -8")  # Mover el stack pointer para hacer espacio para $fp y $ra
                    self.code.append("    sw $ra, 4($sp)")    # Guardar el return address
                    self.code.append("    sw $fp, 0($sp)")    # Guardar el frame pointer

                    # Ahora sí, actualizar el frame pointer y reservar espacio para las variables locales
                    self.code.append("    move $fp, $sp")      # Actualizar el frame pointer
                    self.code.append(f"    addi $sp, $sp, -{size}")  # Ajustar el stack pointer para las variables locales

                    # Guardar la dirección de la clase que llama a la función en primera posición
                    # La dirección se pasa como parámetro
                    if "Main.main" in tokens[1]:
                        self.code.append("    sw $s7, 0($sp)")  # Guardar la dirección de la clase que llama a la función
                    
                    else:
                        self.code.append("    sw $s1, 0($sp)")  # Guardar la dirección de la clase que llama a la función

            # ----------------- CREAR NUEVO OBJETO -----------------
            elif len(tokens) == 4 and "new" in tokens[2]:

                # nombre de la clase
                class_name = tokens[3]

                # Llamar a la clase
                self.code.append(f"\n# ------> CREAR NUEVO OBJETO {class_name}")
                self.code.append(f"    jal CLASS_{class_name}")  # Llamar a la clase

                # Almacenar en registro
                registro = tokens[0].split('[')[1].split(']')[0]    # numero de registro

                # Revisar si registro es global o local
                if "sp_GLOBAL" in tokens[0] and self.inside_first_func:
                    index = int(registro) + 8 # Extraer el índice de sp_GLOBAL
                    # Guardar en {index}$s6 la dirección guardada en $s7
                    self.code.append(f"    sw $s7, {index}($s6)")
                                          
                elif "sp_GLOBAL" in tokens[0]:
                    index = int(registro) + 8 # Extraer el índice de sp_GLOBAL
                    self.code.append("    lw $s2, 0($sp)")  # Almacenar en $s2 la dirección de la clase actual
                    self.code.append(f"    sw $s7, {index}($s2)")  # Guardar la dirección de la clase en el stack global

                elif "sp" in tokens[0]:
                    index = int(registro) + 4
                    self.code.append(f"    sw $s7, {index}($sp)")  # Guardar la dirección de la clase en el stack local

                elif "REGISTRO" in tokens[0]:
                    registro = registro.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                    self.code.append(f"    move $t{registro}, $s7")


                # Regresar el valor de $s6 a $s7
                self.code.append("    move $s7, $s6")

                # Eliminar el \t del inicio de la línea
                name_var = tokens[0].split('\t')[1]
                self.global_vars[name_var] = class_name

            # ----------------- OPERACIONES Y LLAMADAS A FUNCIONES -----------------
            elif "CALL" in tokens:

                # Main.main
                if "Main.main" in line:
                    continue

                # ----------------- QUIEN LLAMA A LA FUNCIÓN -----------------
                # clase que llama a una función
                clase_calling = tokens[3].split('.')[0]
                registro_to_save = None

                # sp_GLOBAL[index] 
                if "sp_GLOBAL" in clase_calling:
                    index = int(clase_calling.split('[')[1].split(']')[0]) + 8
                    registro_to_save = int(tokens[0].split('[')[1].split(']')[0])
                    
                    # Buscar en la dirección de la clase en el heap de la clase
                    self.code.append("\n# ------> sp_GLOBAL[index] ")

                    # Almacenar en $s2 la dirección de la clase actual
                    self.code.append("    lw $s2, 0($sp)")

                    # Almacenar en $s1 la dirección de la clase que llama a la función
                    self.code.append(f"    lw $s1, {index}($s2)")

                # sp[index]
                elif "sp" in clase_calling:
                    index = int(clase_calling.split('[')[1].split(']')[0]) + 4
                    registro_to_save = int(tokens[0].split('[')[1].split(']')[0])

                    # Buscar el la dirección de la clase en el stack de la función
                    self.code.append("\n# ------> sp[index] ")

                    # Almacenar en $s1 el contenido de la dirección de la clase que llama a la función
                    self.code.append(f"    lw $s1, {index}($sp)")
                    
                # REGISTRO[index]
                elif "REGISTRO" in clase_calling:
                    registro = clase_calling.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                    registro_to_save = int(tokens[0].split('[')[1].split(']')[0])

                    if "@" in registro:
                        # eliminar los dos ultimos caracteres
                        registro = registro[:-2]

                    # Buscar el la dirección de la clase en el registro temporal
                    self.code.append("\n# ------> REGISTRO[index] ")

                    # Almacenar en $s1 la dirección de la clase que llama a la función
                    self.code.append(f"    move $s1, {registro}")

                else:
                    # Almacenar en registro_to_save la dirección de la clase que llama a la función
                    registro_to_save = int(tokens[0].split('[')[1].split(']')[0])

                    # Almacenar en $2 la dirección de la clase actual
                    self.code.append("    lw $s2, 0($sp)")
                    # Almacenar en $s1 la dirección de la clase que llama a la función
                    self.code.append("    move $s1, $s2")

                # ----------------- FUNCION LLAMADA -----------------
                # OUT_STRING
                if "out_string" in line:
                    string_to_print = None
                    registro_to_print = None

                    self.code.append("\n# ------> OUT_STRING")

                    # Eliminar out_string(____) del ultimo token
                    patron = r'out_string\("([^"]+)"\)'                 # Patron para obtener la cadena a imprimir
                    string_to_print = re.search(patron, tokens[-1])     # Buscar la cadena a imprimir

                    # ----------------- Si es una cadena (FUNCIONA) -----------------

                    if string_to_print:                                 # Si se encontró la cadena
                        string_to_print = string_to_print.group(1)

                        # Almacenar la cadena en el heap
                        heap_reg = self.heap_save_string(string_to_print)

                        # Pasarle la dirección de la cadena a la función
                        self.code.append(f"    move $a0, {heap_reg}")

                        # Liberar el registro temporal
                        self.liberated_register(heap_reg)

                    # ----------------- Si es un registro o variable -----------------

                    else:
                        # Buscar si es una variable global, local o un registro
                        patron2 = r'out_string\((sp_GLOBAL\[\d+\]|sp\[\d+\]|REGISTRO\[\d+\])\)'  # Patrón para obtener la referencia
                        registro_to_print = re.search(patron2, tokens[-1])  # Buscar la referencia

                        if registro_to_print:  # Si se encontró la referencia
                            registro_to_print = registro_to_print.group(1)  # Obtener la referencia

                            # Si es una variable global (sp_GLOBAL)
                            if "sp_GLOBAL" in registro_to_print:
                                index = int(registro_to_print.split('[')[1].split(']')[0]) + 8 # Extraer el índice de sp_GLOBAL
                                
                                # Almacenr en $s1 la dirección de la clase
                                self.code.append("    lw $s1, 0($sp)")

                                # Cargar la dirección de la cadena desde sp_GLOBAL
                                self.code.append(f"    lw $a0, {index}($s1)")

                            # Si es una variable local (sp)
                            elif "sp" in registro_to_print:
                                index = int(registro_to_print.split('[')[1].split(']')[0])  + 4 # Extraer el índice de sp
                                self.code.append(f"    lw $a0, {index}($sp)")  # Cargar la dirección de la cadena desde sp

                            # Si es un registro (REGISTRO)
                            elif "REGISTRO" in registro_to_print:
                                registro = registro_to_print.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                                self.code.append(f"    move $a0, {registro}")  # Mover el valor del registro al $a0

                    # Imprimir la cadena
                    self.code.append("    jal out_string\n")        

                # OUT_INT
                elif "out_int" in line:
                    self.code.append("\n# ------> OUT_INT")

                    # Eliminar out_int(____) del ultimo token
                    patron = r'out_int\((sp_GLOBAL\[\d+\]|sp\[\d+\]|REGISTRO\[\d+\])\)'  # Patrón para obtener la referencia
                    registro_to_print = re.search(patron, tokens[-1])  # Buscar la referencia

                    # Si se encontró la referencia
                    if registro_to_print:
                        registro_to_print = registro_to_print.group(1)  # Obtener la referencia

                        # Si es una variable global (sp_GLOBAL)
                        if "sp_GLOBAL" in registro_to_print:
                            index = int(registro_to_print.split('[')[1].split(']')[0]) + 8 # Extraer el índice de sp_GLOBAL
                            
                            # Almacenr en $s1 la dirección de la clase
                            self.code.append("    lw $s1, 0($sp)")

                            # Cargar el valor de la variable global
                            self.code.append(f"    lw $a0, {index}($s1)")

                        # Si es una variable local (sp)
                        elif "sp" in registro_to_print:
                            index = int(registro_to_print.split('[')[1].split(']')[0])  + 4 # Extraer el índice de sp
                            self.code.append(f"    lw $a0, {index}($sp)")  # Cargar el valor de la variable local

                        # Si es un registro (REGISTRO)
                        elif "REGISTRO" in registro_to_print:
                            registro = registro_to_print.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                            self.code.append(f"    move $a0, {registro}")  # Mover el valor del registro al $a0

                        else:
                            self.code.append(f"    li $a0, {registro_to_print}")

                    # Imprimir el entero
                    self.code.append("    jal out_int\n")

                # type_name
                elif "type_name" in line:

                    # REGISTRO1 = CALL algo.type_name()
                    registro1 = tokens[0].split('[')[1].split(']')[0]
                    
                    algo = tokens[3].split('.')[0]

                    self.code.append("\n# ------> REGISTRO1 = CALL algo.type_name()")

                    # Si es una variable global (sp_GLOBAL)
                    if "sp_GLOBAL" in algo:
                        index = int(algo.split('[')[1].split(']')[0]) + 8
                        self.code.append("    lw $s1, 0($sp)")
                        self.code.append(f"    lw $s1, {index}($s1)")

                    # Si es una variable local (sp)
                    elif "sp" in algo:
                        index = int(algo.split('[')[1].split(']')[0]) + 4
                        self.code.append(f"    lw $s1, {index}($sp)")

                    # Si es un registro (REGISTRO)
                    elif "REGISTRO" in algo:
                        registro = algo.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                        self.code.append(f"    move $s1, {registro}")

                    # Obtener el string del nombre de la clase
                    self.code.append("    lw $s2, 0($s1)")

                    # Almacenar el string en registro1
                    self.code.append(f"    move $t{registro1}, $s2\n")

                # substr
                elif "substr" in line:
                    # REGISTRO1 = CALL REGISTRO2.substr(algo, algo)
                    registro1 = tokens[0].split('[')[1].split(']')[0]
                    registro2 = tokens[3].split('.')[0]

                    algo1 = tokens[3].split('(')[1].split(',')[0]
                    algo2 = tokens[3].split(',')[1].split(')')[0]

                    if algo2 == "":
                        algo2 = tokens[4].split(')')[0]

                    self.code.append("\n# ------> REGISTRO1 = CALL REGISTRO2.substr(algo1, algo2)")

                    # revisar si registro2 es global o local o registro
                    if "sp_GLOBAL" in registro2:
                        index = int(registro2.split('[')[1].split(']')[0]) + 8
                        self.code.append("    lw $s1, 0($sp)")
                        self.code.append(f"    lw $s1, {index}($s1)")

                    elif "sp" in registro2:
                        index = int(registro2.split('[')[1].split(']')[0]) + 4
                        self.code.append(f"    lw $s1, {index}($sp)")

                    elif "REGISTRO" in registro2:
                        registro = registro2.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                        self.code.append(f"    move $s1, {registro}")
                    

                    # Cargar el valor de algo1
                    if algo1.isdigit():
                        self.code.append(f"    li $s2, {algo1}")
                    else:
                        # Si es una variable global (sp_GLOBAL)
                        if "sp_GLOBAL" in algo1:
                            index = int(algo1.split('[')[1].split(']')[0]) + 8
                            self.code.append("    lw $s2, 0($sp)")
                            self.code.append(f"    lw $s2, {index}($s2)")

                        # Si es una variable local (sp)
                        elif "sp" in algo1:
                            index = int(algo1.split('[')[1].split(']')[0]) + 4
                            self.code.append(f"    lw $s2, {index}($sp)")

                        # Si es un registro (REGISTRO)
                        elif "REGISTRO" in algo1:
                            registro = algo1.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                            self.code.append(f"    move $s2, {registro}")

                    # Cargar el valor de algo2
                    if algo2.isdigit():
                        self.code.append(f"    li $s3, {algo2}")
                    else:
                        # Si es una variable global (sp_GLOBAL)
                        if "sp_GLOBAL" in algo2:
                            index = int(algo2.split('[')[1].split(']')[0]) + 8
                            self.code.append("    lw $s3, 0($sp)")
                            self.code.append(f"    lw $s3, {index}($s3)")

                        # Si es una variable local (sp)
                        elif "sp" in algo2:
                            index = int(algo2.split('[')[1].split(']')[0]) + 4
                            self.code.append(f"    lw $s3, {index}($sp)")

                        # Si es un registro (REGISTRO)
                        elif "REGISTRO" in algo2:
                            registro = algo2.replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                            self.code.append(f"    move $s3, {registro}")

                    # Pasarle los parámetros a la función
                    self.code.append("    move $a0, $s1")
                    self.code.append("    move $a1, $s2")
                    self.code.append("    move $a2, $s3")
                    
                    # Cortar y guardar la cadena en el heap
                    self.code.append("    jal substr")

                    # Guardar el valor de retorno en el registro
                    self.code.append(f"    move $t{registro1}, $v0\n")

                else:
                    # Nombre de la función
                    function_name = tokens[3].split('.')[1].split('(')[0]

                    # Llamar a la función
                    self.code.append(f"\n# ------> LLAMAR A LA FUNCIÓN {function_name}")

                    # Determinar qué número representa la función. Buscar en self.method_table
                    # self.method_table contiene {CLASS : [metodo1, metodo2, ...], ...}

                    class_calling = tokens[3].split('.')[0]

                    if "@" in class_calling:
                        class_calling = class_calling.split('@')[1]

                    
                    if "sp_GLOBAL" in class_calling or "sp" in class_calling or "REGISTRO" in class_calling:
                        class_calling = self.global_vars[tokens[3].split('.')[0]]

                        result_type = self.function_return_type(class_calling, function_name)
                        self.global_vars[tokens[0].replace("\t", "")] = result_type

                    else:
                        result_type = self.function_return_type(class_calling, function_name)
                        self.global_vars[tokens[0].replace("\t", "")] = result_type

                    
                    array_funciones_clase = self.method_table[class_calling]
                    indice_funcion = array_funciones_clase.index(function_name)


                    # Si no OVERRIDE TYPE @
                    if "@" not in tokens[3].split('.')[0]:
                        # En $s1 se encuentra la dirección de la clase que llama a la función
                        reg_temp = self.return_next_register()

                        # Acceder a la tabla virtual de la clase que llama a la función
                        self.code.append("    lw $s2, 4($s1)")

                        # Cargar la dirección de la función
                        self.code.append(f"    lw {reg_temp}, {indice_funcion*4}($s2)")



                    # ----------------- PASAR PARÁMETROS  Y LLAMAR FUNCIÓN -----------------

                    # Pasarle a la función la dirección de la clase que llama a la función
                    self.code.append("    move $a0, $s1")

                    # Pasarle a la función los parámetros
                    cant_parametros = len(tokens[3].split('.')[1].split('(')[1].split(')')[0].split(','))

                    # Si hay parámetros
                    if cant_parametros > 0:

                        if len(tokens) >= 5:
                            # combinar el tercero y cuarto token
                            tokens[3] = tokens[3] + "" + tokens[4]

                            #eliminar cuarto token
                            tokens.pop(4)

                        # Obtener los parámetros
                        parametros = tokens[3].split('(')[1].split(')')[0].split(',')
                        parametros = [parametro.strip() for parametro in parametros]



                        # Pasarle los parámetros a la función
                        for i in range(cant_parametros):
                            # Si es una variable global (sp_GLOBAL)
                            if "sp_GLOBAL" in parametros[i]:
                                index = int(parametros[i].split('[')[1].split(']')[0]) + 8 # Extraer el índice de sp_GLOBAL

                                # Acceder a la variable global desde sp
                                self.code.append("    lw $s2, 0($sp)")  # Almacenar en $s2 la dirección de la clase
                                self.code.append(f"    lw $s1, {index}($s2)")  # Almacenar en $s1 la dirección de la variable global

                                # Pasarle el valor a la función
                                self.code.append(f"    move $a{i+1}, $s1")

                            # Si es una variable local (sp)
                            elif "sp" in parametros[i]:
                                index = int(parametros[i].split('[')[1].split(']')[0]) + 4 # Extraer el índice de sp
                                self.code.append(f"    lw $s1, {index}($sp)")  # Cargar el valor de la variable local
                                
                                # Pasarle el valor a la función
                                self.code.append(f"    move $a{i+1}, $s1")

                            # Si es un registro (REGISTRO)
                            elif "REGISTRO" in parametros[i]:
                                registro = parametros[i].replace("REGISTRO", "$t").replace("[", "").replace("]", "")

                                # Pasarle el valor a la función
                                self.code.append(f"    move $a{i+1}, {registro}")

                            # Si es un número
                            elif parametros[i].isdigit():
                                # Pasarle el valor a la función
                                self.code.append(f"    li $a{i+1}, {parametros[i]}")

                            # Si es un string
                            elif '"' in parametros[i]:
                                # Almacenar la cadena en el heap
                                heap_reg = self.heap_save_string(parametros[i])

                                # Pasarle la dirección de la cadena a la función
                                self.code.append(f"    move $a{i+1}, {heap_reg}")

                                # Liberar el registro temporal
                                self.liberated_register(heap_reg)

                    # Guardar los registros temporales en el stack
                    self.code.append("    jal save_registers")

                     # Si no OVERRIDE TYPE @
                    if "@" not in tokens[3].split('.')[0]:
                        # Llamar a la función seg´un la dirección guardada en $t0
                        self.code.append(f"    jalr {reg_temp}")
                        self.liberated_register(reg_temp)

                    else:
                        # Llamar a la función por tu etiqueta directamente
                        self.code.append(f"    jal {class_calling}.{function_name}")

                    # Recuperar los registros temporales del stack
                    self.code.append("    jal restore_registers")

                    # Guardar el valor de retorno en el registro
                    self.code.append(f"    move $t{registro_to_save}, $v0\n")

            elif "isvoid" in line:
                # REGISTRO = isvoid REGISTRO
                registro1 = tokens[0].split('[')[1].split(']')[0]
                registro2 = tokens[3].split('[')[1].split(']')[0]

                self.code.append("\n# ------> REGISTRO = isvoid REGISTRO")

                # Cargar el valor del registro temporal 2
                self.code.append(f"    move $t0, $t{registro2}")

                # Comparar el valor del registro temporal 2 con $zero
                self.code.append(f"    beq $t0, $zero, isvoid_true{self.counter}")
                self.code.append(f"    li $t{registro1}, 0")
                self.code.append(f"    j isvoid_end{self.counter}")

                # Si el valor del registro temporal 2 es igual a $zero
                self.code.append(f"isvoid_true{self.counter}:")
                self.code.append(f"    li $t{registro1}, 1")

                # Terminar
                self.code.append(f"isvoid_end{self.counter}:")

                self.counter += 1

            # ----------------- IF -----------------
            elif "IF" in tokens[0]:
                self.code.append("\n# ------> IF")

                # IF registro[x] GOTO label
                if "REGISTRO" in tokens[1]:
                    registro = tokens[1].replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                    label = tokens[3]

                    self.code.append(f"    bne {registro}, $zero, {label}\n")

                # IF NOT registro[x] GOTO label
                elif "NOT" in tokens[1]:
                    registro = tokens[2].replace("REGISTRO", "$t").replace("[", "").replace("]", "")
                    label = tokens[4]

                    self.code.append(f"    beq {registro}, $zero, {label}\n")

            # ----------------- GOTO -----------------
            elif "GOTO" in tokens[0]:
                self.code.append("\n# ------> GOTO")

                # GOTO label
                label = tokens[1]

                self.code.append(f"    j {label}\n")

            # ----------------- LABEL -----------------
            elif "LABEL" in tokens[0]:
                self.code.append("\n# ------> LABEL")

                # LABEL label
                label = tokens[1]

                self.code.append(f"{label}:\n")
                
            # ----------------- DECLARAR VARIABLES -----------------
            elif "sp_GLOBAL" in tokens[0] and self.class_before_func:   # Si es una variable global definida antes de una función

                # sp_GLOBAL[index] = sp_GLOBAL[index];
                if "sp_GLOBAL" in tokens[2]:
                    # sp_GLOBAL[index] = sp_GLOBAL[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0]) + 8
                    index2 = int(tokens[2].split('[')[1].split(']')[0]) + 8

                    self.code.append("\n# ------> sp_GLOBAL[index] = sp_GLOBAL[index];")

                    # Cargar el valor de la variable global
                    self.code.append(f"    lw $t0, {index2}($s7)")
                    # Guardar el valor en la variable global
                    self.code.append(f"    sw $t0, {index1}($s7)")

                # sp_GLOBAL[index] = REGISTRO[index];
                elif "REGISTRO" in tokens[2]:
                    # sp_GLOBAL[index] = REGISTRO[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0]) + 8  # Índice para la variable global
                    registro = tokens[2].split('[')[1].split(']')[0]    # numero de registro

                    self.code.append("\n# ------> sp_GLOBAL[index] = REGISTRO[index];")
                    self.code.append(f"    sw $t{registro}, {index1}($s7)")  # Usar el registro directamente

                # sp_GLOBAL[index] = value;
                elif "=" in tokens[1]:
                    # sp_GLOBAL[index] = value;
                    index = int(tokens[0].split('[')[1].split(']')[0]) + 8  # Índice para la variable global
                    value = tokens[2]                                       # El valor a asignar

                    self.code.append("\n# ------> sp_GLOBAL[index] = value;")

                    # Inicializar la variable global en el stack
                    if value.isdigit():  # Si el valor es un dígito, lo tratamos como un número inmediato
                        value_reg = self.return_next_register()  # Obtener un registro temporal para el valor
                        self.code.append(f"    li {value_reg}, {value}")
                        self.code.append(f"    sw {value_reg}, {index}($s7)\n")
                        self.liberated_register(value_reg)  # Liberar el registro temporal
                        
                    else:
                        # Si el valor es una cadena, se almacenar en el heap y luego
                        # se almacena la dirección en el stack
                        heap_reg = self.heap_save_string(value)
                        self.code.append(f"    sw {heap_reg}, {index}($s7)\n")
                        self.liberated_register(heap_reg)  # Liberar el registro temporal


                # Llamar a la función
                class_calling = tokens[2]

                if "sp_GLOBAL" in class_calling or "sp" in class_calling or "REGISTRO" in class_calling:
                    if class_calling in self.global_vars.keys():
                        class_calling = self.global_vars[class_calling]
                        self.global_vars[tokens[0].split('\t')[1]] = class_calling

            elif "sp_GLOBAL" in tokens[0] and not self.class_before_func:   # Si es una variable global definida dentro de una función
                # almacenar en $s1 la dirección de la clase
                self.code.append("    lw $s1, 0($sp)")

                # sp_GLOBAL[index] = sp_GLOBAL[index];
                if "sp_GLOBAL" in tokens[2]:
                    # sp_GLOBAL[index] = sp_GLOBAL[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0]) + 8
                    index2 = int(tokens[2].split('[')[1].split(']')[0]) + 8

                    self.code.append("\n# ------> sp_GLOBAL[index] = sp_GLOBAL[index];")

                    # Cargar el valor de la variable global
                    self.code.append(f"    lw $t0, {index2}($s1)")
                    # Guardar el valor en la variable global
                    self.code.append(f"    sw $t0, {index1}($s1)")

                # sp_GLOBAL[index] = sp[index];
                elif "sp" in tokens[2]:
                    # sp_GLOBAL[index] = sp[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0]) + 8
                    index2 = int(tokens[2].split('[')[1].split(']')[0]) + 4

                    self.code.append("\n# ------> sp_GLOBAL[index] = sp[index];")

                    # Cargar el valor de la variable global
                    self.code.append(f"    lw $t0, {index2}($sp)")
                    # Guardar el valor en la variable global
                    self.code.append(f"    sw $t0, {index1}($s1)")

                # sp_GLOBAL[index] = REGISTRO[index];
                elif "REGISTRO" in tokens[2]:
                    # sp_GLOBAL[index] = REGISTRO[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0]) + 8  # Índice para la variable global
                    registro = tokens[2].split('[')[1].split(']')[0]    # numero de registro

                    self.code.append("\n# ------> sp_GLOBAL[index] = REGISTRO[index];")
                    self.code.append(f"    sw $t{registro}, {index1}($s1)")  # Usar el registro directamente

                # sp_GLOBAL[index] = value;
                elif "=" in tokens[1]:
                    # sp_GLOBAL[index] = value;
                    index = int(tokens[0].split('[')[1].split(']')[0]) + 8  # Índice para la variable global
                    value = tokens[2]                                       # El valor a asignar

                    self.code.append("\n# ------> sp_GLOBAL[index] = value;")

                    # Inicializar la variable global en el stack
                    if value.isdigit():  # Si el valor es un dígito, lo tratamos como un número inmediato
                        value_reg = self.return_next_register()  # Obtener un registro temporal para el valor
                        self.code.append(f"    li {value_reg}, {value}")
                        self.code.append(f"    sw {value_reg}, {index}($s1)\n")
                        self.liberated_register(value_reg)  # Liberar el registro temporal
                        
                    else:
                        # Si el valor es una cadena, se almacenar en el heap y luego
                        # se almacena la dirección en el stack
                        heap_reg = self.heap_save_string(value)
                        self.code.append(f"    sw {heap_reg}, {index}($s1)\n")
                        self.liberated_register(heap_reg)  # Liberar el registro temporal

                # Llamar a la función
                class_calling = tokens[2]

                if "sp_GLOBAL" in class_calling or "sp" in class_calling or "REGISTRO" in class_calling:
                    if class_calling in self.global_vars.keys():
                        class_calling = self.global_vars[class_calling]
                        self.global_vars[tokens[0].split('\t')[1]] = class_calling

            elif "sp" in tokens[0]:
                
                # PARAM
                if "PARAM" in line:
                    # sp[index] = PARAM_X
                    index = int(tokens[0].split('[')[1].split(']')[0]) + 4 # Índice para la variable local
                    data_type = tokens[2].split('.')[0]  # Tipo de dato
                    param = int(tokens[2].split('_')[1]) # Número del parámetro

                    self.code.append("\n# ------> sp[index] = PARAM_X")
                    
                    # almacenar $aX en sp[index]
                    self.code.append(f"    sw $a{param + 1}, {index}($sp)\n")

                    # Eliminar el \t del inicio de la línea
                    name_var = tokens[0].split('\t')[1]
                    self.global_vars[name_var] = data_type
                
                # sp[index] = sp[index];
                elif "sp" in tokens[2]:
                    # sp[index] = sp[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0]) + 4
                    index2 = int(tokens[2].split('[')[1].split(']')[0]) + 4

                    self.code.append("\n# ------> sp[index] = sp[index];")
                    self.code.append(f"    lw $t0, {index2}($sp)")  # Cargar el valor de la variable local
                    self.code.append(f"    sw $t0, {index1}($sp)")  # Guardar el valor en la variable local

                # sp[index] = sp_GLOBAL[index];
                elif "sp_GLOBAL" in tokens[2]:
                    # sp[index] = sp_GLOBAL[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0]) + 4 # Índice para la variable local
                    index2 = int(tokens[2].split('[')[1].split(']')[0]) + 8 # Índice para la variable global
                    class_dir = 0

                    self.code.append("\n# ------> sp[index] = sp_GLOBAL[index];")
                    # Cargar a $s1 la dirección de la clase
                    self.code.append(f"    lw $s1, 0($sp)")
                    # Cargar el valor de la variable global
                    self.code.append(f"    lw $t0, {index2}($s1)")
                    # Guardar el valor en la variable local
                    self.code.append(f"    sw $t0, {index1}($sp)")

                # sp[index] = REGISTRO[index];
                elif "REGISTRO" in tokens[2]:
                    # sp[index] = REGISTRO[index];
                    index = int(tokens[0].split('[')[1].split(']')[0]) + 4 # Índice para la variable local
                    registro = tokens[2].split('[')[1].split(']')[0]  # numero de registro

                    self.code.append("\n# ------> sp[index] = REGISTRO[index];")
                    self.code.append(f"    sw $t{registro}, {index}($sp)")  # Guardar el valor del registro en la variable local

                # sp[index] = value;
                elif "=" in tokens[1]:
                    # sp[index] = value;
                    index = int(tokens[0].split('[')[1].split(']')[0]) + 4 # Índice para la variable local
                    value = tokens[2]
                    self.code.append("\n# ------> sp[index] = value;")
                    if value.isdigit():  # Si el valor es un dígito
                        self.code.append(f"    li $t0, {value}")
                        self.code.append(f"    sw $t0, {index}($sp)")
                    else:
                        # Si el valor es una cadena, se almacenar en el heap y luego
                        # se almacena la dirección en el stack
                        heap_reg = self.heap_save_string(value)
                        self.code.append(f"    sw {heap_reg}, {index}($sp)\n")
                        self.liberated_register(heap_reg)  # Liberar el registro temporal

                # Llamar a la función
                class_calling = tokens[2]

                if "sp_GLOBAL" in class_calling or "sp" in class_calling or "REGISTRO" in class_calling:
                    if class_calling in self.global_vars.keys():
                        class_calling = self.global_vars[class_calling]
                        self.global_vars[tokens[0].split('\t')[1]] = class_calling

            elif "REGISTRO" in tokens[0]:
                # REGISTRO[index] = REGISTRO[index];
                if "REGISTRO" in tokens[2] and len(tokens) == 3:
                    # REGISTRO[index] = REGISTRO[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0])
                    index2 = int(tokens[2].split('[')[1].split(']')[0])

                    self.code.append("\n# ------> REGISTRO[index] = REGISTRO[index];")

                    # Almacenar el valor de un registro en otro registro
                    self.code.append(f"    move $t{index1}, $t{index2}")

                elif "sp" in tokens[2] and len(tokens) == 3:
                    # REGISTRO[index] = sp[index];
                    index1 = int(tokens[0].split('[')[1].split(']')[0])
                    index2 = int(tokens[2].split('[')[1].split(']')[0])

                    self.code.append("\n# ------> REGISTRO[index] = sp[index];")

                    # Almacenar el valor de una variable local en un registro
                    self.code.append(f"    lw $t{index1}, {index2}($sp)")

                elif len(tokens) == 3:
                    # REGISTRO[index] = value;
                    index = int(tokens[0].split('[')[1].split(']')[0])
                    value = tokens[2]

                    self.code.append("\n# ------> REGISTRO[index] = value;")
                    if value.isdigit():  # Si el valor es un dígito
                        self.code.append(f"    li $t{index}, {value}")

                    elif "true" in value or "false" in value:
                        
                        if "true" in value:
                            self.code.append(f"    li $t{index}, 1")
                        elif "false" in value:
                            self.code.append(f"    li $t{index}, 0")

                    elif "self" in value:
                        # Almacenar en $s1 la dirección de la clase
                        self.code.append(f"    lw $t{index}, 0($sp)")

                    # si es un string
                    else:
                        # Si el valor es una cadena, se almacenar en el heap y luego
                        # se almacena la dirección en el stack
                        heap_reg = self.heap_save_string(value)
                        self.code.append(f"    move $t{index}, {heap_reg}")
                        self.liberated_register(heap_reg)

                elif "not" in tokens[2]:
                    registro1 = tokens[0].split('[')[1].split(']')[0]
                    algo2 = tokens[3]

                    # revisar si algo2 es global, local o temporal
                    if "sp_GLOBAL" in algo2:
                        # colocar en $s1 la dirección de la clase
                        self.code.append("    lw $s1, 0($sp)")
                        # colocar en $s1 el valor de la variable global
                        index = int(algo2.split('[')[1].split(']')[0]) + 8
                        self.code.append(f"    lw $s1, {index}($s1)")  

                    elif "sp" in algo2:
                        # colocar en $s1 el valor de la variable local
                        index = int(algo2.split('[')[1].split(']')[0]) + 4
                        self.code.append(f"    lw $s1, {index}($sp)")

                    elif "REGISTRO" in algo2:
                        # colocar en $s1 el valor del registro
                        registro = algo2.split('[')[1].split(']')[0]
                        self.code.append(f"    move $s1, $t{registro}")

                    elif algo2.isdigit():
                        # colocar en $s1 el valor inmediato
                        self.code.append(f"    li $s1, {algo2}")

                    # comparar $s1 y $zero
                    self.code.append("\n# ------> NOT algo[index];")
                    self.code.append(f"    beq $s1, $zero, not_true{self.counter}")
                    self.code.append(f"    li $t{registro1}, 0")
                    self.code.append(f"    j not_end{self.counter}")
                    self.code.append(f"not_true{self.counter}:")
                    self.code.append(f"    li $t{registro1}, 1")
                    self.code.append(f"not_end{self.counter}:")
                    self.counter += 1

                # neg (convertir a numero negativo)
                elif "neg" in tokens[2]:
                    # REGISTRO = neg algo
                    registro = tokens[0].split('[')[1].split(']')[0]
                    algo = tokens[3]

                    # revisar si algo es global, local o temporal
                    if "sp_GLOBAL" in algo:
                        # colocar en $s1 la dirección de la clase
                        self.code.append("    lw $s1, 0($sp)")
                        # colocar en $s1 el valor de la variable global
                        index = int(algo.split('[')[1].split(']')[0]) + 8
                        self.code.append(f"    lw $s1, {index}($s1)")

                    elif "sp" in algo:
                        # colocar en $s1 el valor de la variable local
                        index = int(algo.split('[')[1].split(']')[0]) + 4
                        self.code.append(f"    lw $s1, {index}($sp)")

                    elif "REGISTRO" in algo:
                        # colocar en $s1 el valor del registro
                        registro = algo.split('[')[1].split(']')[0]
                        self.code.append(f"    move $s1, $t{registro}")

                    elif algo.isdigit():
                        # colocar en $s1 el valor inmediato
                        self.code.append(f"    li $s1, {algo}")

                    # negar $s1
                    self.code.append("\n# ------> neg algo;")
                    self.code.append(f"    neg $t{registro}, $s1")

                else:
                    # REGISTRO[index] = algo OPERADOR algo;
                    
                    # algo1
                    algo1 = tokens[2]

                    # algo2
                    algo2 = tokens[4]

                    if "sp_GLOBAL" in algo1:
                        # colocar en $s1 la dirección de la clase
                        self.code.append("    lw $s1, 0($sp)")
                        # colocar en $s1 el valor de la variable global
                        index = int(algo1.split('[')[1].split(']')[0]) + 8
                        self.code.append(f"    lw $s1, {index}($s1)")

                    elif "sp" in algo1:
                        # colocar en $s1 el valor de la variable local
                        index = int(algo1.split('[')[1].split(']')[0]) + 4
                        self.code.append(f"    lw $s1, {index}($sp)")

                    elif "REGISTRO" in algo1:
                        # colocar en $s1 el valor del registro
                        registro = algo1.split('[')[1].split(']')[0]
                        self.code.append(f"    move $s1, $t{registro}")

                    elif algo1.isdigit():
                        # colocar en $s1 el valor inmediato
                        self.code.append(f"    li $s1, {algo1}")

                    
                    if "sp_GLOBAL" in algo2:
                        # colocar en $s2 la dirección de la clase
                        self.code.append("    lw $s2, 0($sp)")
                        # colocar en $s2 el valor de la variable global
                        index = int(algo2.split('[')[1].split(']')[0]) + 8
                        self.code.append(f"    lw $s2, {index}($s2)")

                    elif "sp" in algo2:
                        # colocar en $s2 el valor de la variable local
                        index = int(algo2.split('[')[1].split(']')[0]) + 4
                        self.code.append(f"    lw $s2, {index}($sp)")

                    elif "REGISTRO" in algo2:
                        # colocar en $s2 el valor del registro
                        registro = algo2.split('[')[1].split(']')[0]
                        self.code.append(f"    move $s2, $t{registro}")

                    elif algo2.isdigit():
                        # colocar en $s2 el valor inmediato
                        self.code.append(f"    li $s2, {algo2}")

                    set_true = f"set_true{self.counter}"
                    continue_label = f"continue_label{self.counter}"

                    self.counter += 1

                    if  "==" in line or "<" in line or "<=" in line:
                        # comparar $s1 y $s2
                        if "==" in line:
                            self.code.append(f"    beq $s1, $s2, {set_true}")
                        elif "<=" in line:
                            self.code.append(f"    ble $s1, $s2, {set_true}")
                        elif "<" in line:
                            self.code.append(f"    blt $s1, $s2, {set_true}")

                        registro = tokens[0].split('[')[1].split(']')[0]

                        # si no se cumple la condición
                        self.code.append(f"    li $t{registro}, 0")
                        self.code.append(f"    j {continue_label}")
                        self.code.append(f"{set_true}:")
                        self.code.append(f"    li $t{registro}, 1")
                        self.code.append(f"{continue_label}:")

                    elif "+" in line or "-" in line or "*" in line or "/" in line:
                        # realizar la operación
                        registro = tokens[0].split('[')[1].split(']')[0]

                        if "+" in line:
                            self.code.append(f"    add $t{registro}, $s1, $s2")
                        elif "-" in line:
                            self.code.append(f"    sub $t{registro}, $s1, $s2")
                        elif "*" in line:
                            self.code.append(f"    mul $t{registro}, $s1, $s2")
                        elif "/" in line:
                            self.code.append(f"    div $t{registro}, $s1, $s2")

               
                    
            # ----------------- RETURN -----------------
            elif "RETURN" in line:
                # RETURN REGISTRO[index];
                if "REGISTRO" in tokens[1]:
                    # RETURN REGISTRO[index];
                    registro = tokens[1].split('[')[1].split(']')[0]

                    self.code.append("\n# ------> RETURN REGISTRO[index];")
                    self.code.append(f"    move $v0, $t{registro}")  # Mover el valor del registro al $v0

                # RETURN sp_GLOBAL[index];
                elif "sp_GLOBAL" in tokens[1]:
                    # RETURN sp_GLOBAL[index];
                    index = int(tokens[1].split('[')[1].split(']')[0]) + 8

                    self.code.append("\n# ------> RETURN sp_GLOBAL[index];")
                    # Cargar a $s1 la dirección de la clase
                    self.code.append(f"    lw $s1, 0($sp)")
                    self.code.append(f"    lw $v0, {index}($s1)")  # Cargar el valor de la variable global

                # RETURN sp[index];
                elif "sp" in tokens[1]:
                    # RETURN sp[index];
                    index = int(tokens[1].split('[')[1].split(']')[0]) + 4

                    self.code.append("\n# ------> RETURN sp[index];")
                    self.code.append(f"    lw $v0, {index}($sp)")  # Cargar el valor de la variable local

                # RETURN value;
                elif tokens[1].isdigit():
                    # RETURN value;
                    value = tokens[1]

                    self.code.append("\n# ------> RETURN value;")
                    self.code.append(f"    li $v0, {value}")  # Cargar el valor inmediato

                # RETURN true
                elif "true" in tokens[1]:
                    self.code.append("\n# ------> RETURN true;")
                    self.code.append(f"    li $v0, 1")  # Cargar el valor inmediato

                # RETURN false
                elif "false" in tokens[1]:
                    self.code.append("\n# ------> RETURN false;")
                    self.code.append(f"    li $v0, 0")  # Cargar el valor inmediato

                # RETURN self
                elif "self" in tokens[1]:
                    self.code.append("\n# ------> RETURN self;")
                    self.code.append(f"    lw $v0, 0($sp)")  # Cargar la dirección de la clase

                # RETURN string
                elif '"' in tokens[1]:
                    self.code.append("\n# ------> RETURN string;")
                    # Almacenar la cadena en el heap
                    heap_reg = self.heap_save_string(tokens[1])
                    self.code.append(f"    move $v0, {heap_reg}")  # Cargar la dirección de la cadena
                    self.liberated_register(heap_reg)  # Liberar el registro temporal

                # RETURN void
                elif "void" in tokens[1]:
                    self.code.append("\n# ------> RETURN void;")
                    self.code.append(f"    li $v0, 0")  # Cargar el valor inmediato

                # RETURN
                else:
                    self.code.append("\n# ------> RETURN;")
                    self.code.append(f"    li $v0, 0")  # Cargar el valor inmediato

        self.code.append("\n\n# ------> TERMINAR PROGRAMA")
        self.code.append("    li $v0, 10")  # código de salida
        self.code.append("    syscall")     # terminar ejecución

        return self.code

    def function_type(self, classTemp, functionTemp):
        name = classTemp + "." + functionTemp
        for key, table in self.symbol_table.records:
            if key == name:
                return table.type 

    def return_next_register(self):
        items = list(self.temp_usage.items())
        items = items[::-1]

        for key, value in items:
            if not value:
                self.temp_usage[key] = True
                return key
        print("ERROR: No hay registros disponibles")

    def liberated_register(self, register):
        if register in self.temp_usage:
            self.temp_usage[register] = False

    def push_stack(self, register):
        self.code.append("\n# ---> PUSH STACK")
        self.code.append(f"    addi $sp, $sp, -4")
        self.code.append(f"    sw {register}, 0($sp)\n")

    def pop_stack(self, register):
        self.code.append("\n# ---> POP STACK")
        self.code.append(f"    lw {register}, 0($sp)")
        self.code.append(f"    addi $sp, $sp, 4\n")

    def heap_allocation(self, size):
        register = self.return_next_register()
        self.code.append("\n# ---> ALLOCATION {size} BYTES")
        self.code.append(f"    li {register}, {size}")
        self.code.append(f"    move $a0, {register}")
        self.code.append(f"    li $v0, 9")
        self.code.append(f"    syscall")
        self.code.append(f"    move {register}, $v0")
        return register
    
    def heap_save_string(self, string):
        string = bytes(string, "utf-8").decode("unicode_escape")

        if string[0] == '"' or string[0] == "'":
            string = string[1:]
        if string[-1] == '"' or string[-1] == "'":
            string = string[:-1]

        size = len(string) + 1
        register = self.heap_allocation(size)
        register2 = self.return_next_register()

        self.code.append("\n# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)")

        for key, value in enumerate(string):
            self.code.append(f"    li {register2}, {ord(value)}")
            self.code.append(f"    sb {register2}, {key}({register})")

        self.code.append(f"    sb $zero, {size - 1}({register})\n")
        self.liberated_register(register2)
        return register