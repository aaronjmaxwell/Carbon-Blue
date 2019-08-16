/* Load the System library. */
using System;

public class ExampleTwo {
    public static void Main() {
        /* Notice a an explict float requires an appended *f*, whereas a double is implicitly
        assumed when a decimal is used.  Also, char must use single quotes.*/
        int integer = 1;
        float flt = 1f;
        bool spock = true;
        string name = "Aaron";
        char letter = 'z';
        double dbl = 3.14;
        /* C# supports type inference, like JavaScript, by guessing depending the assigned value.
        However, that type is fixed at compile time. In the example below, the compiler assumes that
        x and y are integers, therefor s will also be an integer. */
        var x = 1;
        var y = 2;
        var s = x + y;
        System.Console.WriteLine(s);
    }
}
