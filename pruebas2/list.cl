class List {
   -- Define operaciones en listas vacías.

   init(i : Int, rest : List) : List { self };

   isNil() : Bool { 
      {
         true;
      }
   };

   head()  : Int { 0 };

   tail()  : List { self };

   cons(i : Int) : List {
      -- Ahora se crea una instancia de Cons en lugar de List.
      {
         (new Cons).init(i, self);
      }
   };

};

class Cons inherits List {
   car : Int;  -- El elemento en esta celda de la lista
   cdr : List;  -- El resto de la lista

   init(i : Int, rest : List) : List {
      {
         car <- i;
         cdr <- rest;
         self;
      }
   };

   isNil() : Bool { 
      {
         false; 
      }
   };

   head()  : Int { car };

   tail()  : List { cdr };

};

class Main inherits IO {
   mylist : List;

   print_list(l : List) : Object {
      
      if l.isNil() then out_string("\n")
      
      else {
         out_int(l.head());
         out_string(" ");
         print_list(l.tail());
      }

      fi
   };

   main() : Object {
      {
         mylist <- new List.cons(10).cons(9).cons(2001).cons(2023).cons(10).cons(9).cons(2001).cons(2023);
         print_list(mylist);
      }
   };
};