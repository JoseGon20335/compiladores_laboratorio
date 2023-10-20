class Main inherits IO {

  out : Int <-		-- out is our 'output'.  It's values are the primes.
    {
      out_string("2 is trivially prime.\n");
      2;
    };
  
  testee : Int <- out;	-- testee is a number to be tested for primeness.   
  divisor : Int;	-- divisor is a number which may factor testee.
  stop : Int <- 500;	-- stop is an arbitrary value limiting testee. 	
  dummy : Bool <- true;	-- dummy is a dummy variable to allow us to parse.
  chaos : String <- "Izalith";	-- chaos is a dummy variable to allow us to parse.
  gwyn : Bool <- true;	-- gwyn is a dummy variable to allow us to parse.
  entero : Int <- 0;	-- entero is a dummy variable to allow us to parse.

  main() : Object {	-- main() is an atrophied method so we can parse. 
     {
      while true loop 
      {

        entero <- entero + 1;	
        entero <- gwyn + 5;
        -- chaos <- gwyn + chaos;	-- this doesn't work.
        testee <- testee + dummy;
        divisor <- 2;

        while 
          if testee < divisor * divisor 
            then false 		-- can stop if divisor > sqrt(testee).
	  else if testee - divisor*(testee/divisor) = 0 
            then false 		-- can stop if divisor divides testee. 
            else true
          fi fi     
        loop 
          divisor <- divisor + dummy
        pool;        

        if testee < divisor * divisor	-- which reason did we stop for?
        then 	-- testee has no factors less than sqrt(testee).
          {
            out <- testee;	-- we could think of out itself as the output.
            out_int(out); 
            out_string(" is prime.\n");
          }
        else	-- the loop halted on testee/divisor = 0, testee isn't prime.
          0	-- testee isn't prime, do nothing.
	fi;   	

        if stop <= testee then 
          "halt".abort()	-- we could think of "halt" as SIGTERM.
        else 
          "continue"
        fi;       

      } 
    pool;
    }
  };
};