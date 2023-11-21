class A {
    var : Int <- 0;

    -- Función value: Devuelve el valor actual de 'var'.
    value() : Int { 
        var 
    };

    -- Función set_var: Establece el valor de 'var' y devuelve una instancia de sí misma.
    set_var(num : Int) : SELF_TYPE {
        {
            var <- num;
            self;
        }
    };

    -- Función method1: Ejemplo de método que simplemente devuelve la instancia actual.
    method1(num : Int) : SELF_TYPE {
        self
    };

    -- Función method2: Suma dos enteros y actualiza 'var' con el resultado.
    method2(num1 : Int, num2 : Int) : A {
        (let x : Int in
            {
                x <- num1 + num2;
                (new A).set_var(x);
            }
        )
    };

    -- Función method3: Niega el valor de un entero y actualiza 'var'.
    method3(num : Int) : A {
        (let x : Int in
            {
                x <- ~num;
                (new A).set_var(x);
            }
        )
    };

    -- Función method4: Calcula la diferencia entre dos enteros y actualiza 'var'.
    method4(num1 : Int, num2 : Int) : A {
        if num2 < num1 then
            (let x : Int in
                {
                    x <- num1 - num2;
                    (new A).set_var(x);
                }
            )
        else
            (let y : Int in
                {
                    y <- num2 - num1;
                    (new A).set_var(y);
                }
            )
        fi
    };

    -- Función method5: Calcula el factorial de un número y actualiza 'var'.
    method5(num : Int) : A {
        (let x : Int <- 1 in
            {
                (let y : Int <- 1 in
                    while y <= num loop
                        {
                           x <- x * y;
                           y <- y + 1;
                        }
                    pool
                );
                (new A).set_var(x);
            }
        )
    };
};

class B inherits A {

    -- Función method5: Calcula el cuadrado de 'numB' y actualiza 'var'.
    method5(numB : Int) : B {
        (let x : Int in
            {
                x <- numB * numB;
                (new B).set_var(x);
            }
        )
    };
};

class C inherits B {

    -- Función method6: Niega el valor de un entero y actualiza 'var' usando la clase A.
    method6(num : Int) : A {
        (let x : Int in
            {
                x <- ~num;
                (new A).set_var(x);
            }
        )
    };

    -- Función method5: Calcula el cubo de un número y actualiza 'var'.
    method5(num : Int) : B {
        (let x : Int in
            {
                x <- num * num * num;
                (new B).set_var(x);
            }
        )
    };
};

class D inherits B {

    -- Función method7: Determina si un número es divisible por 3.
    method7(num : Int) : Bool {
        (let x : Int <- num in
            if x < 0 then method7(~x) else
            if 0 = x then true else
            if 1 = x then false else
            if 2 = x then false else
                method7(x - 3)
            fi fi fi fi
        )
    };
};

class E inherits D {

    -- Función method6: Divide un número entre 8 y actualiza 'var'.
    method6(num : Int) : A {
        (let x : Int in
            {
                x <- num / 8;
                (new A).set_var(x);
            }
        )
    };
};

class Main inherits IO {
    char : String;
    avar : A; 
    a_var : A;
    flag : Bool <- true;

    -- Función is_even: Determina si un número es par.
    is_even(num : Int) : Bool {
        (let x : Int <- num in
            if x < 0 then is_even(~x) else
            if 0 = x then true else
            if 1 = x then false else
                is_even(x - 2)
            fi fi fi
        )
    };

    main() : Object {
        {
            avar <- (new A);
            avar.set_var(2);

            out_string("\nPAR O IMPAR\n");
            out_int(avar.value());
            if is_even(avar.value()) then
                out_string(" es par!\n")
            else
                out_string(" es impar!\n")
            fi;
            
            out_string("\nSUMA DE 3 Y 2\n");
            a_var <- (new A).set_var(3);
            avar <- (new B).method2(avar.value(), a_var.value());
            out_int(avar.value());
            out_string("\n");
            
            out_string("\nNEG DE SUMA\n");
            avar <- (new C).method6(avar.value());
            out_int(avar.value());
            out_string("\n");
            
            out_string("\nDIFERENCIA ENTRE 2 ENTEROS\n");
            a_var <- (new A).set_var(5);
            avar <- (new D).method4(avar.value(), a_var.value());
            out_int(avar.value());
            out_string("\n");

            out_string("\nMETODO 5 (C@A): 10! \n");
            avar <- (new C)@A.method5(avar.value());
            out_int(avar.value());
            out_string("\n");
            
            out_string("\nMETODO 5 (C@B): 6^2 \n");
            avar.set_var(6);
            avar <- (new C)@B.method5(avar.value());
            out_int(avar.value());
            out_string("\n");
            
        }
    };
};

