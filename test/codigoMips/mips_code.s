.data

# VIRTUAL TABLES
vt_Factorial:
    .word Factorial.factorial
vt_Fibonacci:
    .word Fibonacci.fibonacci
vt_Main:
    .word Main.main

.text

main:
    jal CLASS_Main


# ------> FUNCIONES BASICAS
out_string:
    li $v0, 4
    syscall
    jr $ra


out_int:
    li $v0, 1
    syscall
    jr $ra


substr:
    move $a0, $s1
    move $a1, $s2
    move $a2, $s3
    li $s4, 0
    add $s5, $s2, $s3

# ------> RESERVAR ESPACIO EN EL HEAP PARA LA NUEVA SUBCADENA
    addi $a2, $a2, 1
    move $a0, $a2
    li $v0, 9
    syscall
    move $s6, $v0
    move $t5, $s6

# ------> COPIAR LOS CARACTERES DE LA CADENA ORIGINAL A LA NUEVA SUBCADENA
substr_loop:
    beq $s4, $s5, substr_end
    blt $s4, $s2, skip_char

# ------> COPIAR CARACTERES
    lb $t3, 0($s1)
    sb $t3, 0($s6)
    addi $s6, $s6, 1

# ------> SALTO DE CARACTERES
skip_char:
    addi $s4, $s4, 1
    addi $s1, $s1, 1
    j substr_loop

# ------> TERMINAR LA FUNCION substr
substr_end:
    sb $zero, 0($s6)
    move $v0, $t5
    jr $ra



# ------> SAVE REGISTROS TEMPORALES EN EL STACK
save_registers:
    addi $sp, $sp, -36
    sw $t0, 0($sp)
    sw $t1, 4($sp)
    sw $t2, 8($sp)
    sw $t3, 12($sp)
    sw $t4, 16($sp)
    sw $t5, 20($sp)
    sw $t6, 24($sp)
    sw $t7, 28($sp)
    sw $t8, 32($sp)
    jr $ra



# ------> RESTAURAR REGISTROS TEMPORALES DEL STACK
restore_registers:
    lw $t0, 0($sp)
    lw $t1, 4($sp)
    lw $t2, 8($sp)
    lw $t3, 12($sp)
    lw $t4, 16($sp)
    lw $t5, 20($sp)
    lw $t6, 24($sp)
    lw $t7, 28($sp)
    lw $t8, 32($sp)
    addi $sp, $sp, 36
    jr $ra



# ------> CREAR CLASE Object
CLASS_Object:

# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE Object
    li $a0, 8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALLOCATION {size} BYTES
    li $t7, 7
    move $a0, $t7
    li $v0, 9
    syscall
    move $t7, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t6, 79
    sb $t6, 0($t7)
    li $t6, 98
    sb $t6, 1($t7)
    li $t6, 106
    sb $t6, 2($t7)
    li $t6, 101
    sb $t6, 3($t7)
    li $t6, 99
    sb $t6, 4($t7)
    li $t6, 116
    sb $t6, 5($t7)
    sb $zero, 6($t7)

    sw $t7, 0($t8)
    move $s6, $s7
    move $s7, $t8
    jr $ra


# ------> CREAR CLASE IO
CLASS_IO:

# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE Object
    li $a0, 8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALLOCATION {size} BYTES
    li $t7, 3
    move $a0, $t7
    li $v0, 9
    syscall
    move $t7, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t6, 73
    sb $t6, 0($t7)
    li $t6, 79
    sb $t6, 1($t7)
    sb $zero, 2($t7)

    sw $t7, 0($t8)
    move $s6, $s7
    move $s7, $t8
    jr $ra


CLASS_Factorial:

# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE Factorial
    li $a0, 16
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALLOCATION {size} BYTES
    li $t7, 10
    move $a0, $t7
    li $v0, 9
    syscall
    move $t7, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t6, 70
    sb $t6, 0($t7)
    li $t6, 97
    sb $t6, 1($t7)
    li $t6, 99
    sb $t6, 2($t7)
    li $t6, 116
    sb $t6, 3($t7)
    li $t6, 111
    sb $t6, 4($t7)
    li $t6, 114
    sb $t6, 5($t7)
    li $t6, 105
    sb $t6, 6($t7)
    li $t6, 97
    sb $t6, 7($t7)
    li $t6, 108
    sb $t6, 8($t7)
    sb $zero, 9($t7)

    sw $t7, 0($t8)
    la $t0, vt_Factorial
    sw $t0, 4($t8)
    move $s6, $s7
    move $s7, $t8

# ------> sp_GLOBAL[index] = value;
    li $t8, 0
    sw $t8, 8($s7)

    jr $ra


Factorial.factorial:
    move $s1, $a0
# ------> INICIALIZAR MEMORIA DE LA FUNCION Factorial.factorial
    addi $sp, $sp, -8
    sw $ra, 4($sp)
    sw $fp, 0($sp)
    move $fp, $sp
    addi $sp, $sp, -8
    sw $s1, 0($sp)

# ------> sp[index] = PARAM_X
    sw $a1, 4($sp)

    lw $s1, 8($sp)
    li $s2, 0
    beq $s1, $s2, set_true0
    li $t0, 0
    j continue_label0
set_true0:
    li $t0, 1
continue_label0:

# ------> IF
    bne $t0, $zero, label1


# ------> GOTO
    j label2


# ------> LABEL
label1:


# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 5
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 78
    sb $t7, 0($t8)
    li $t7, 111
    sb $t7, 1($t8)
    li $t7, 110
    sb $t7, 2($t8)
    li $t7, 101
    sb $t7, 3($t8)
    sb $zero, 4($t8)

    move $t4, $t8

# ------> GOTO
    j label3


# ------> LABEL
label2:

    lw $s1, 8($sp)
    li $s2, 1
    beq $s1, $s2, set_true1
    li $t0, 0
    j continue_label1
set_true1:
    li $t0, 1
continue_label1:

# ------> IF
    bne $t0, $zero, label4


# ------> GOTO
    j label5


# ------> LABEL
label4:


# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 5
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 78
    sb $t7, 0($t8)
    li $t7, 111
    sb $t7, 1($t8)
    li $t7, 110
    sb $t7, 2($t8)
    li $t7, 101
    sb $t7, 3($t8)
    sb $zero, 4($t8)

    move $t8, $t8

# ------> GOTO
    j label6


# ------> LABEL
label5:

    lw $s1, 8($sp)
    li $s2, 1
    sub $t0, $s1, $s2
    lw $s2, 0($sp)
    move $s1, $s2

# ------> LLAMAR A LA FUNCI�N factorial
    lw $s2, 4($s1)
    lw $t8, 0($s2)
    move $a0, $s1
    move $a1, $t0
    jal save_registers
    jalr $t8
    jal restore_registers
    move $t12, $v0

    lw $s1, 8($sp)
    move $s2, $t12
    mul $t0, $s1, $s2

# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 5
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 78
    sb $t7, 0($t8)
    li $t7, 111
    sb $t7, 1($t8)
    li $t7, 110
    sb $t7, 2($t8)
    li $t7, 101
    sb $t7, 3($t8)
    sb $zero, 4($t8)

    move $t8, $t8

# ------> LABEL
label6:


# ------> REGISTRO[index] = REGISTRO[index];
    move $t4, $t8

# ------> LABEL
label3:


# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 2
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 102
    sb $t7, 0($t8)
    sb $zero, 1($t8)

    move $t0, $t8

# ------> RETURN REGISTRO[index];
    move $v0, $t0

# ------> FIN DE LA FUNCION Factorial.factorial
    move $sp, $fp
    lw $fp, 0($sp)
    lw $ra, 4($sp)
    addi $sp, $sp, 8
    jr $ra


CLASS_Fibonacci:

# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE Fibonacci
    li $a0, 16
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALLOCATION {size} BYTES
    li $t7, 10
    move $a0, $t7
    li $v0, 9
    syscall
    move $t7, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t6, 70
    sb $t6, 0($t7)
    li $t6, 105
    sb $t6, 1($t7)
    li $t6, 98
    sb $t6, 2($t7)
    li $t6, 111
    sb $t6, 3($t7)
    li $t6, 110
    sb $t6, 4($t7)
    li $t6, 97
    sb $t6, 5($t7)
    li $t6, 99
    sb $t6, 6($t7)
    li $t6, 99
    sb $t6, 7($t7)
    li $t6, 105
    sb $t6, 8($t7)
    sb $zero, 9($t7)

    sw $t7, 0($t8)
    la $t0, vt_Fibonacci
    sw $t0, 4($t8)
    move $s6, $s7
    move $s7, $t8

# ------> sp_GLOBAL[index] = value;
    li $t8, 0
    sw $t8, 8($s7)

    jr $ra


Fibonacci.fibonacci:
    move $s1, $a0
# ------> INICIALIZAR MEMORIA DE LA FUNCION Fibonacci.fibonacci
    addi $sp, $sp, -8
    sw $ra, 4($sp)
    sw $fp, 0($sp)
    move $fp, $sp
    addi $sp, $sp, -8
    sw $s1, 0($sp)

# ------> sp[index] = PARAM_X
    sw $a1, 4($sp)

    lw $s1, 8($sp)
    li $s2, 0
    beq $s1, $s2, set_true4
    li $t4, 0
    j continue_label4
set_true4:
    li $t4, 1
continue_label4:

# ------> IF
    bne $t4, $zero, label7


# ------> GOTO
    j label8


# ------> LABEL
label7:


# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 5
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 78
    sb $t7, 0($t8)
    li $t7, 111
    sb $t7, 1($t8)
    li $t7, 110
    sb $t7, 2($t8)
    li $t7, 101
    sb $t7, 3($t8)
    sb $zero, 4($t8)

    move $t0, $t8

# ------> GOTO
    j label9


# ------> LABEL
label8:

    lw $s1, 8($sp)
    li $s2, 1
    beq $s1, $s2, set_true5
    li $t4, 0
    j continue_label5
set_true5:
    li $t4, 1
continue_label5:

# ------> IF
    bne $t4, $zero, label10


# ------> GOTO
    j label11


# ------> LABEL
label10:


# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 5
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 78
    sb $t7, 0($t8)
    li $t7, 111
    sb $t7, 1($t8)
    li $t7, 110
    sb $t7, 2($t8)
    li $t7, 101
    sb $t7, 3($t8)
    sb $zero, 4($t8)

    move $t8, $t8

# ------> GOTO
    j label12


# ------> LABEL
label11:

    lw $s1, 8($sp)
    li $s2, 1
    sub $t4, $s1, $s2
    lw $s2, 0($sp)
    move $s1, $s2

# ------> LLAMAR A LA FUNCI�N fibonacci
    lw $s2, 4($s1)
    lw $t8, 0($s2)
    move $a0, $s1
    move $a1, $t4
    jal save_registers
    jalr $t8
    jal restore_registers
    move $t12, $v0

    lw $s1, 8($sp)
    li $s2, 2
    sub $t4, $s1, $s2
    lw $s2, 0($sp)
    move $s1, $s2

# ------> LLAMAR A LA FUNCI�N fibonacci
    lw $s2, 4($s1)
    lw $t8, 0($s2)
    move $a0, $s1
    move $a1, $t4
    jal save_registers
    jalr $t8
    jal restore_registers
    move $t16, $v0

    move $s1, $t12
    move $s2, $t16
    add $t4, $s1, $s2

# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 5
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 78
    sb $t7, 0($t8)
    li $t7, 111
    sb $t7, 1($t8)
    li $t7, 110
    sb $t7, 2($t8)
    li $t7, 101
    sb $t7, 3($t8)
    sb $zero, 4($t8)

    move $t8, $t8

# ------> LABEL
label12:


# ------> REGISTRO[index] = REGISTRO[index];
    move $t0, $t8

# ------> LABEL
label9:


# ------> REGISTRO[index] = value;

# ---> ALLOCATION {size} BYTES
    li $t8, 2
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 102
    sb $t7, 0($t8)
    sb $zero, 1($t8)

    move $t0, $t8

# ------> RETURN REGISTRO[index];
    move $v0, $t0

# ------> FIN DE LA FUNCION Fibonacci.fibonacci
    move $sp, $fp
    lw $fp, 0($sp)
    lw $ra, 4($sp)
    addi $sp, $sp, 8
    jr $ra


CLASS_Main:

# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE Main
    li $a0, 32
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALLOCATION {size} BYTES
    li $t7, 5
    move $a0, $t7
    li $v0, 9
    syscall
    move $t7, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t6, 77
    sb $t6, 0($t7)
    li $t6, 97
    sb $t6, 1($t7)
    li $t6, 105
    sb $t6, 2($t7)
    li $t6, 110
    sb $t6, 3($t7)
    sb $zero, 4($t7)

    sw $t7, 0($t8)
    la $t0, vt_Main
    sw $t0, 4($t8)
    move $s7, $t8

# ------> sp_GLOBAL[index] = value;
    li $t8, 10
    sw $t8, 8($s7)

    jal Main.main


Main.main:
# ------> INICIALIZAR MEMORIA DE LA FUNCION Main.main
    addi $sp, $sp, -8
    sw $ra, 4($sp)
    sw $fp, 0($sp)
    move $fp, $sp
    addi $sp, $sp, -12
    sw $s7, 0($sp)

# ------> CREAR NUEVO OBJETO Factorial
    jal CLASS_Factorial
    lw $s2, 0($sp)
    sw $s7, 16($s2)
    move $s7, $s6

# ------> sp_GLOBAL[index] 
    lw $s2, 0($sp)
    lw $s1, 16($s2)

# ------> LLAMAR A LA FUNCI�N factorial
    lw $s2, 4($s1)
    lw $t8, 0($s2)
    move $a0, $s1
    lw $s2, 0($sp)
    lw $s1, 8($s2)
    move $a1, $s1
    jal save_registers
    jalr $t8
    jal restore_registers
    move $t4, $v0

    lw $s2, 0($sp)
    move $s1, $s2

# ------> OUT_INT
    move $a0, $t4
    jal out_int

    lw $s2, 0($sp)
    move $s1, $s2

# ------> OUT_STRING

# ---> ALLOCATION {size} BYTES
    li $t8, 9
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 10
    sb $t7, 0($t8)
    li $t7, 45
    sb $t7, 1($t8)
    li $t7, 45
    sb $t7, 2($t8)
    li $t7, 45
    sb $t7, 3($t8)
    li $t7, 45
    sb $t7, 4($t8)
    li $t7, 45
    sb $t7, 5($t8)
    li $t7, 45
    sb $t7, 6($t8)
    li $t7, 10
    sb $t7, 7($t8)
    sb $zero, 8($t8)

    move $a0, $t8
    jal out_string


# ------> CREAR NUEVO OBJETO Fibonacci
    jal CLASS_Fibonacci
    lw $s2, 0($sp)
    sw $s7, 24($s2)
    move $s7, $s6

# ------> sp_GLOBAL[index] 
    lw $s2, 0($sp)
    lw $s1, 24($s2)

# ------> LLAMAR A LA FUNCI�N fibonacci
    lw $s2, 4($s1)
    lw $t8, 0($s2)
    move $a0, $s1
    lw $s2, 0($sp)
    lw $s1, 8($s2)
    move $a1, $s1
    jal save_registers
    jalr $t8
    jal restore_registers
    move $t0, $v0

    lw $s2, 0($sp)
    move $s1, $s2

# ------> OUT_INT
    move $a0, $t0
    jal out_int


# ------> REGISTRO[index] = value;
    lw $t0, 0($sp)

# ------> RETURN REGISTRO[index];
    move $v0, $t0

# ------> FIN DE LA FUNCION Main.main
    move $sp, $fp
    lw $fp, 0($sp)
    lw $ra, 4($sp)
    addi $sp, $sp, 8


# ------> TERMINAR PROGRAMA
    li $v0, 10
    syscall
