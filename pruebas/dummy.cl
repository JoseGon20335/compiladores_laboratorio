class Main inherits IO{

    daredevil : Int;
    kingpin : Int;

    elektra : Bool;

    karen : String;


    main() : Object {
    {
        kingpin <- 1;
        elektra <- true;
        daredevil <- kingpin + elektra;
        daredevil <- daredevil + 1;
        kingpin <- karen; -- this should fail
        self;
    }
    };

};