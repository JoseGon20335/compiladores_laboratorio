.data

# VIRTUAL TABLES
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


CLASS_Main:

# ------> RESERVAR ESPACIO EN EL HEAP PARA LA CLASE Main
    li $a0, 8
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
    jal Main.main


Main.main:
# ------> INICIALIZAR MEMORIA DE LA FUNCION Main.main
    addi $sp, $sp, -8
    sw $ra, 4($sp)
    sw $fp, 0($sp)
    move $fp, $sp
    addi $sp, $sp, -12
    sw $s7, 0($sp)
    lw $s2, 0($sp)
    move $s1, $s2

# ------> OUT_STRING

# ---> ALLOCATION {size} BYTES
    li $t8, 15
    move $a0, $t8
    li $v0, 9
    syscall
    move $t8, $v0

# ---> ALMACENAR CADENA EN HEAP (EN EL ESPACIO RESERVADO)
    li $t7, 72
    sb $t7, 0($t8)
    li $t7, 101
    sb $t7, 1($t8)
    li $t7, 108
    sb $t7, 2($t8)
    li $t7, 108
    sb $t7, 3($t8)
    li $t7, 111
    sb $t7, 4($t8)
    li $t7, 44
    sb $t7, 5($t8)
    li $t7, 32
    sb $t7, 6($t8)
    li $t7, 87
    sb $t7, 7($t8)
    li $t7, 111
    sb $t7, 8($t8)
    li $t7, 114
    sb $t7, 9($t8)
    li $t7, 108
    sb $t7, 10($t8)
    li $t7, 100
    sb $t7, 11($t8)
    li $t7, 46
    sb $t7, 12($t8)
    li $t7, 10
    sb $t7, 13($t8)
    sb $zero, 14($t8)

    move $a0, $t8
    jal out_string


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
