class Factorial {
  	var: Int <- 0;
  	
  	factorial(n: Int, m: Int) : Int {
		{
			( let f : Int in
			if n=0 then f<-1 else
			if n=1 then f<-1 else
				f<-n*factorial()
			fi fi);

			f;
		}
    };
  
  };

class Fibonacci {
	var: Int <- 0;
  	
    fibonacci() : Int {
        {
            ( let f : Int, g : Int in
            if 0 then f<-0 else
            if n=1 then f<-1 else
				{
					f<-fibonacci(n-1) + fibonacci(n-2);
				}
            fi fi);

            f;
        }
    };
  
  };

class Main inherits IO {
    n: Int <- 10;
  	facto: Factorial;
  	fibo: Fibonacci2;

  	main() : SELF_TYPE {
		{
			facto <- new Factorial;
			out_int(facto.factorial(n));

			out_string("\n------\n");
			
			fibo <- new Fibonacci;
			out_int(fibo.fibonacci(n));
			self;
		}
    };
	
};