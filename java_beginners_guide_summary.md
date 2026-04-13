# Java: A Beginner's Guide — Professor-Level Summary
**Herbert Schildt, 6th Edition (Java SE 8)**

---

## Chapter 1 — Java Fundamentals

### The Real Reason Java Was Invented

Java was born in 1991 at Sun Microsystems, created by James Gosling and a team that included Patrick Naughton, Chris Warth, Ed Frank, and Mike Sheridan. The original name was "Oak." The goal had nothing to do with the Internet at the time — they needed a **platform-independent language** to control consumer electronics: toasters, microwaves, remote controls. Different manufacturers used different CPUs, and writing a new C++ compiler for every chip was prohibitively expensive. The solution they reached: compile not to machine code, but to a neutral intermediate form that a small, cheap runtime can interpret on any chip.

When the World Wide Web exploded around 1993–1995, the team realized they had already solved the Internet's biggest problem. A web page could ship a Java program — called an **applet** — that would download and run identically on every user's machine, regardless of OS or CPU. This is what launched Java to prominence.

### Why Bytecode Solves Two Problems at Once

When you compile a Java source file, the compiler (`javac`) does not produce native machine code. It produces **bytecode** — a compact, optimized set of instructions for a virtual machine called the **JVM (Java Virtual Machine)**. The same `.class` file runs on Windows, Linux, macOS, or any platform that has a JVM. This is "write once, run anywhere."

Bytecode also enables **security**: the JVM is a sandbox that intercedes between the program and your real hardware. An applet cannot reach outside the environment the JVM grants it. No raw pointer arithmetic, no direct memory access.

The performance concern is addressed by **HotSpot**, a just-in-time (JIT) compiler built into modern JVMs. HotSpot watches which sections of bytecode execute most often and compiles *only those hot paths* into native machine code at runtime. The rest remains interpreted. You get portability + security + near-native performance.

The flow is:
```
YourCode.java  →  javac  →  YourCode.class (bytecode)  →  JVM  →  runs on CPU
```

### The Three Pillars of OOP

Java is fundamentally object-oriented. Understanding the three pillars before writing code is not optional — they shape every design decision you will ever make in Java.

**Encapsulation** — data and the code that manipulates it are bound together in a single unit (the class), and the internal details are hidden. The `private` keyword hides fields from the outside world. You expose controlled access through `public` methods. This means the object protects its own integrity — nothing outside can corrupt its internal state accidentally.

**Polymorphism** — "one interface, multiple methods." The same method name means different things depending on which type of object you're calling it on. You call `area()` and get the right formula whether the shape is a Triangle or a Rectangle. You don't manage that decision in your code — Java does it at runtime. The phrase from the book: *"it is possible to design a generic interface to a group of related activities."*

**Inheritance** — one class can acquire the properties of another. A `Triangle` that inherits from `TwoDShape` automatically has `width`, `height`, and `showDim()` without rewriting them. It only defines what is unique to a triangle. This creates natural hierarchical classifications, exactly like the real world: a Red Delicious apple is-an apple is-a fruit is-a food.

### Dissecting the First Program Line by Line

```java
/*
 * This is a simple Java program.
 * Call this file Example.java.
 */
class Example {
    // A Java program begins with a call to main().
    public static void main(String args[]) {
        System.out.println("Java drives the Web.");
    }
}
```

**`class Example`** — In Java, all code lives inside a class. There is no notion of a "global function" as in C. This is not just a stylistic rule; it is the foundational constraint of the language. Everything is an object or belongs to one.

**`public`** on `main()` — The JVM lives outside your class. For it to call `main()` when your program starts, `main()` must be accessible from outside. `public` means visible to everyone.

**`static`** on `main()` — When your program starts, no objects of your class exist yet. A `static` method belongs to the class itself, not to any instance — so the JVM can call it before constructing anything. Without `static`, the JVM would need to create an instance, but it needs `main()` to know how to do that. `static` breaks the circular dependency.

**`void`** — `main()` returns nothing to the JVM.

**`String args[]`** — An array of Strings holding any command-line arguments. `java MyApp hello world` → `args[0]` is `"hello"`, `args[1]` is `"world"`. If you pass nothing, the array exists but is empty.

**`System.out.println(...)`** — `System` is a pre-defined class. `out` is a `PrintStream` object inside it, connected to the console. `println()` outputs a line and moves to the next line. The semicolon `;` terminates every statement. Java is not whitespace-sensitive.

**Rule**: The filename must exactly match the public class name, including capitalization. `Example` → `Example.java`. The compiler enforces this.

### Variables and Integer Division — A Critical Trap

```java
int var1 = 1024;
int var2 = var1 / 2;   // var2 = 512
```

Integer division discards the fractional part — it **truncates**, it does not round. `7 / 2` gives `3`, not `3.5`. To get `3.5` you must use `double`. This silent truncation causes bugs constantly.

```java
double x = 7.0;
double y = x / 2;   // y = 3.5  — correct
```

---

## Chapter 2 — Introducing Data Types and Operators

### Why Strong Typing Is a Feature, Not a Constraint

Java is **strongly typed**: every variable, every expression, every return value has a declared type, and the compiler checks all operations for compatibility. If you try to assign a `double` to an `int` without an explicit cast, the program will not compile. This catches type mismatches at compile time — before you ship, before you run a single test. In weakly typed languages, these mismatches silently corrupt data at runtime and appear as mysterious wrong answers.

### The Eight Primitive Types — The Real Numbers Behind Them

These are the only non-object building blocks in Java:

| Type | Bits | Range | Typical Use |
|------|------|-------|-------------|
| `byte` | 8 | –128 to 127 | Raw binary data, file I/O |
| `short` | 16 | –32,768 to 32,767 | Rarely used directly |
| `int` | 32 | –2,147,483,648 to 2,147,483,647 | Default integer, counters, indices |
| `long` | 64 | –9.2×10¹⁸ to 9.2×10¹⁸ | Timestamps, large counts |
| `float` | 32 | ~±3.4×10³⁸ (7 sig. digits) | Rarely used; use `double` |
| `double` | 64 | ~±1.8×10³⁰⁸ (15 sig. digits) | All floating-point work |
| `char` | 16 | 0 to 65,535 (Unicode) | Single characters |
| `boolean` | — | `true` or `false` only | Conditions, flags |

**Why `long` matters** — Consider this from the book:

```java
long ci;
long im;
im = 5280 * 12;       // feet per mile × inches per foot = 63,360
ci = im * im * im;    // cubic inches in a cubic mile
System.out.println("There are " + ci + " cubic inches in cubic mile.");
// Output: There are 254358061056000 cubic inches in cubic mile.
```

`254,358,061,056,000` does not fit in an `int` (max ~2.1 billion). Without `long`, this silently overflows and gives a completely wrong answer with no error.

**Why `double` over `float`** — All of Java's standard math library (`Math.sqrt()`, `Math.sin()`, `Math.pow()`, etc.) takes and returns `double`. Using `float` means constant casting and reduced precision. Always use `double` for floating-point work. The book demonstrates this directly:

```java
double x = 3, y = 4, z;
z = Math.sqrt(x*x + y*y);   // Pythagorean theorem
System.out.println("Hypotenuse is " + z);
// Output: Hypotenuse is 5.0
```

**Why `char` is 16-bit** — Java uses Unicode, not ASCII. ASCII covers 128 characters and only handles English. Unicode covers the entire range of human writing: Chinese, Arabic, Tamil, Greek, Hebrew, emoji. Java's `char` holds the Basic Multilingual Plane (0–65,535), sufficient for all modern scripts. The ASCII subset (0–127) is fully included, so all the familiar character tricks still work:

```java
char ch = 'X';
ch++;                          // 'Y' — next Unicode value
ch = 90;                       // decimal 90 = 'Z' in ASCII/Unicode
System.out.println(ch);        // prints: Z
```

**`boolean` is not numeric** — In C/C++, `if(1)` means true. In Java, `if(1)` is a compile error. Conditions must produce a genuine `boolean`. No implicit conversion exists between `boolean` and integers:

```java
boolean b = true;
if(b)                 System.out.println("This executes.");
if(b == true)         System.out.println("Same thing, but redundant.");
System.out.println("10 > 9 is " + (10 > 9));   // prints: 10 > 9 is true
```

### Literals in Detail

A **literal** is a fixed value written directly in source code:

```java
// Integer literals
int decimal = 255;
int hex     = 0xFF;          // Hexadecimal — prefix 0x
int octal   = 011;           // Octal — leading zero: this is 9, not 11!
int binary  = 0b11111111;    // Binary (JDK 7+) — prefix 0b

// Size qualifiers
long big    = 12L;           // L suffix → long literal
float f     = 3.14F;         // F suffix → float literal
double d    = 3.14;          // No suffix → double by default

// Readability underscores (JDK 7+) — compiler ignores the underscores
int million = 1_000_000;
long ssn    = 123_45_6789L;
```

The octal trap is subtle: `011` looks like eleven, but it is nine. Any integer literal starting with `0` is octal. Always write `9`, never `011`, unless you truly mean octal.

### Variable Scope — Where Variables Live and Die

A variable exists only within the block `{}` that contains its declaration. When the block exits, the variable is destroyed. This is called **scope**:

```java
public static void main(String args[]) {
    int x = 10;           // x lives for all of main()

    if (x == 10) {
        int y = 20;       // y lives only inside this if-block
        System.out.println(x + " " + y);   // fine: both visible
    }

    // y = 100;            // COMPILE ERROR — y no longer exists
    System.out.println(x); // fine: x still alive
}
```

A variable declared inside a `for` loop is scoped to the loop:

```java
for (int i = 0; i < 10; i++) {
    // i exists here
}
// i = 5;     // COMPILE ERROR — i is gone
```

**Java prevents shadowing** — Unlike C++, you cannot declare a variable in an inner scope with the same name as one in the outer scope. This eliminates an entire class of "which variable am I changing?" bugs.

### Type Conversion — Widening and Narrowing

Java automatically promotes (widens) values when moving from a smaller to a larger type — no precision is lost:

```
byte → short → int → long → float → double
```

```java
int  i = 100;
long L = i;       // automatic widening — no cast needed
double d = L;     // automatic widening — no cast needed
```

Going the other direction (narrowing) requires an explicit **cast**, because data may be lost:

```java
double x = 9.99;
int i = (int) x;    // i = 9 — fractional part is TRUNCATED, not rounded

int n = 257;
byte b = (byte) n;  // 257 in binary is 100000001
                    // only the bottom 8 bits survive: b = 1
```

The cast `(type)` is your explicit declaration to the compiler: "I understand this conversion may lose data. Do it."

**Promotion in expressions** — Any time you mix types in an arithmetic expression, Java promotes operands upward before computing. The rules:

1. `byte`, `short`, `char` → promoted to `int` first
2. If any operand is `long` → all promoted to `long`
3. If any operand is `float` → all promoted to `float`
4. If any operand is `double` → all promoted to `double`

The tricky consequence:

```java
byte b = 10;
b = b * b;          // COMPILE ERROR — b*b is promoted to int
b = (byte)(b * b);  // OK — explicit cast back to byte
```

Even though `100` fits in a `byte`, the result of the multiplication is already an `int` by promotion rules. The cast is mandatory.

### Short-Circuit Operators — Safety and Efficiency

`&&` and `||` are **short-circuit** versions of AND and OR. They stop evaluating as soon as the answer is determined:

```java
// Without short-circuit: DANGER
if (d != 0 & (n % d) == 0)   // & always evaluates BOTH sides
                               // if d is 0, n % d throws ArithmeticException

// With short-circuit: SAFE
if (d != 0 && (n % d) == 0)  // && checks left first
                               // if d == 0 (false), right side is NEVER evaluated
```

`&&` short-circuits on `false` (AND: false AND anything = false, skip right side).
`||` short-circuits on `true`  (OR: true OR anything = true, skip right side).

The non-short-circuit `&` and `|` always evaluate both sides. Use those only when the right side has a required side effect.

---

## Chapter 3 — Program Control Statements

### Console Input — The Line-Buffering Problem

Reading a single character from the keyboard uses `System.in.read()`:

```java
public static void main(String args[]) throws java.io.IOException {
    char ch;
    System.out.print("Press a key followed by ENTER: ");
    ch = (char) System.in.read();
    System.out.println("Your key is: " + ch);
}
```

`System.in` is **line-buffered**: characters don't become available to the program until you press ENTER. And when you press ENTER, the Enter key itself (carriage return `\r` and/or newline `\n`) is left in the input buffer. In programs that read multiple inputs in sequence, you must explicitly consume those leftover characters, or your next `read()` call will get a newline instead of the character the user typed.

### The `if` Statement and the `else` Binding Rule

The full `if` syntax:

```java
if (condition)
    statement_or_block;
else
    statement_or_block;
```

The critical rule: an `else` **always belongs to the nearest preceding `if` that is in the same block and has no `else` yet**. This matters in nested ifs:

```java
if (i == 10) {
    if (j < 20)  a = b;
    if (k > 100) c = d;
    else a = c;          // belongs to: if (k > 100)
}
else a = d;              // belongs to: if (i == 10)
```

The final `else` is NOT associated with `if(j < 20)` — that if is in a different block. It belongs to `if(i == 10)`. Misreading else-binding is one of the most common logic bugs in Java.

**The `if-else-if` ladder** — the clean way to check multiple exclusive conditions:

```java
if (condition1)      result1;
else if (condition2) result2;
else if (condition3) result3;
else                 default_result;
```

Conditions evaluate top-to-bottom. The first `true` match wins; the rest are skipped. The final `else` is the catch-all default.

### The `switch` Statement — Fall-Through Is a Feature

```java
switch (i) {
    case 1:
        System.out.println("i is one");
        break;
    case 2:
        System.out.println("i is two");
        break;
    default:
        System.out.println("i is something else");
}
```

**The `break` is not automatic.** Without it, execution **falls through** to the next case. This is not a bug — it is a designed feature you can use intentionally to group cases:

```java
switch (i) {
    case 1:
    case 2:
    case 3:
        System.out.println("i is 1, 2, or 3");  // one handler for three values
        break;
    case 4:
        System.out.println("i is 4");
        break;
}
```

Valid `switch` expression types: `byte`, `short`, `int`, `char`, `String` (JDK 7+), `enum`. Not `long`, not `float`, not `double`.

### The Three Loops and When to Use Each

**`for` loop** — when you know the count in advance:

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);   // prints 0 through 9
}
```

Three parts: initialization (runs once), condition (checked before each iteration), update (runs after each iteration). All three are optional. `for(;;)` is a valid infinite loop. You can have multiple control variables:

```java
for (int i = 0, j = 10; i < j; i++, j--) {
    System.out.println("i=" + i + "  j=" + j);
}
```

**`while` loop** — when you don't know the count; condition checked before entry:

```java
char ch = 'a';
while (ch <= 'z') {
    System.out.print(ch);
    ch++;
}
// prints: abcdefghijklmnopqrstuvwxyz
```

If the condition is false from the start, the body never executes. Zero iterations are possible.

**`do-while` loop** — body always executes at least once, condition checked afterward:

```java
do {
    System.out.print("Enter a letter between A and Z: ");
    ch = (char) System.in.read();
} while (ch < 'A' || ch > 'Z');
```

This is the natural structure for any "prompt, then validate" pattern — you always show the prompt at least once.

### `break` and `continue` — Including Labeled Forms

**`break`** exits the immediately enclosing loop or switch:

```java
for (int i = 0; i < 100; i++) {
    if (i * i >= 100) break;
    System.out.print(i + " ");
}
// prints: 0 1 2 3 4 5 6 7 8 9
```

**Labeled `break`** — Java's structured substitute for `goto`. You can exit any enclosing block by name:

```java
done:
for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
        for (int k = 0; k < 10; k++) {
            if (k == 5) break done;   // exits ALL THREE loops instantly
        }
    }
}
```

Without labeled break, escaping deeply nested loops requires awkward boolean flags. The label must be on a block that contains the `break` — you cannot jump forward or into an unrelated block.

**`continue`** skips to the next iteration of the loop:

```java
for (int i = 0; i <= 100; i++) {
    if (i % 2 != 0) continue;   // skip odd numbers
    System.out.println(i);       // only even numbers are printed
}
```

Labeled `continue` skips to the next iteration of a named outer loop — useful for inner loops that want to advance the outer loop without fully breaking out.

---

## Chapter 4 — Introducing Classes, Objects, and Methods

### Class = Blueprint, Object = Instance

A class definition does not create any object and allocates no memory. It defines a *type*:

```java
class Vehicle {
    int passengers;   // instance variable
    int fuelcap;      // instance variable
    int mpg;          // instance variable
}
```

This says "a Vehicle is something that has passengers, fuelcap, and mpg." No memory is used yet. To create an actual object:

```java
Vehicle minivan = new Vehicle();
```

`new` allocates memory on the heap and returns a **reference** — essentially a pointer to the memory location, but without pointer arithmetic. `minivan` holds that reference.

**Every object gets its own copies** of instance variables. Two `Vehicle` objects have separate `passengers`, `fuelcap`, and `mpg` — changing one does not affect the other:

```java
Vehicle minivan = new Vehicle();
Vehicle sportscar = new Vehicle();

minivan.passengers  = 7;
sportscar.passengers = 2;

// These are completely independent values
```

Access instance variables and call methods through the dot operator `.`:

```java
minivan.fuelcap = 16;
minivan.mpg = 21;
int range = minivan.fuelcap * minivan.mpg;   // 336 miles
```

### References Are Not Copies — The Most Important Concept

```java
Vehicle car1 = new Vehicle();
Vehicle car2 = car1;           // car2 now points to the SAME object
```

`car2 = car1` does NOT copy the object. It copies the *reference*. Both variables point at the same single object in memory. This is not intuitive if you come from languages that copy by value.

```java
car1.mpg = 26;
System.out.println(car2.mpg);   // prints 26 — same object!
```

If you later do `car2 = new Vehicle()`, `car2` now points to a new object, but `car1` still points to the original. Assignment changes where the reference points, not what the object contains.

### Methods — Defining Behavior

Methods operate on the object's instance variables. Inside a method, you reference instance variables directly (no dot operator needed — you're already inside the class):

```java
class Vehicle {
    int passengers;
    int fuelcap;
    int mpg;

    // No parameters, returns nothing
    void showRange() {
        System.out.println("Range is " + fuelcap * mpg);
    }

    // Returns a value
    int range() {
        return mpg * fuelcap;
    }

    // Takes a parameter, returns a double
    double fuelneeded(int miles) {
        return (double) miles / mpg;
    }
}
```

```java
Vehicle minivan = new Vehicle();
minivan.fuelcap = 16;
minivan.mpg = 21;

minivan.showRange();                    // prints: Range is 336
int r = minivan.range();                // r = 336
double g = minivan.fuelneeded(252);     // g = 12.0
```

When `showRange()` executes on `minivan`, the reference to `fuelcap` means `minivan.fuelcap`. The JVM knows which object is "current" because you called the method through that object's reference.

### Constructors — Guaranteed Initialization

A constructor runs automatically the moment an object is created with `new`. It has the same name as the class and no return type:

```java
class Vehicle {
    int passengers;
    int fuelcap;
    int mpg;

    // Parameterized constructor
    Vehicle(int p, int f, int m) {
        passengers = p;
        fuelcap    = f;
        mpg        = m;
    }

    int range() { return mpg * fuelcap; }
    double fuelneeded(int miles) { return (double) miles / mpg; }
}
```

Now object creation is atomic and safe:

```java
Vehicle minivan  = new Vehicle(7, 16, 21);   // all fields set immediately
Vehicle sportscar = new Vehicle(2, 14, 12);

System.out.println("Minivan range: " + minivan.range());     // 336
System.out.println("Sportscar range: " + sportscar.range()); // 168
```

Without a constructor, you'd set fields manually after creation. Forgetting one field leaves it at zero and silently produces wrong results. A constructor makes this impossible.

**Default constructor** — If you define no constructor at all, Java provides one automatically with no parameters that zero-initializes all fields. The moment you define your own constructor, the default disappears. If you want both a no-arg and a parameterized constructor, you must define both explicitly.

### The `this` Keyword

Inside any instance method or constructor, `this` refers to the *current object* — the object on which this method was called. The most common use: when a parameter has the same name as an instance variable, the parameter hides (shadows) the field:

```java
Vehicle(int passengers, int fuelcap, int mpg) {
    this.passengers = passengers;  // this.passengers = the field
                                   // passengers = the parameter
    this.fuelcap = fuelcap;
    this.mpg = mpg;
}
```

Without `this.`, `passengers = passengers` would assign the parameter to itself — the instance variable would never be set.

### Garbage Collection — Memory Without `free()`

Java allocates all objects on the **heap** via `new`. When no reference to an object remains, it becomes **unreachable**. The JVM's **Garbage Collector (GC)** reclaims this memory automatically. You never call `free()` or `delete` as you would in C/C++. This eliminates dangling pointers, double-free errors, and most memory leaks.

The trade-off: GC runs at the JVM's discretion, not yours. For most applications this is irrelevant. For real-time, latency-sensitive systems it requires explicit GC tuning.

---

## Chapter 5 — More Data Types and Operators

### Arrays — Fixed-Size Collections

An array is a contiguous sequence of same-type elements, indexed from zero:

```java
int nums[] = new int[10];    // 10 ints, all initialized to 0
nums[0] = 99;                // first element
nums[9] = 42;                // last element (index = length - 1)

// nums[10] = 1;              // ArrayIndexOutOfBoundsException at runtime!
```

Java strictly enforces bounds. An out-of-bounds index is a runtime error, not silent undefined behavior as in C.

`array.length` is a built-in field. Always use it instead of hardcoding the size:

```java
for (int i = 0; i < nums.length; i++) {
    nums[i] = i * i;   // 0, 1, 4, 9, 16, 25...
}
```

**Array initializer** — combine declaration and population:

```java
int nums[] = { 99, -10, 100123, 18, -978, 5623, 463, -9, 287, 49 };
```

Size is inferred from the number of values — no `new` needed.

**Finding min and max** — from the book directly:

```java
int min, max;
min = max = nums[0];
for (int i = 1; i < nums.length; i++) {
    if (nums[i] < min) min = nums[i];
    if (nums[i] > max) max = nums[i];
}
System.out.println("min and max: " + min + " " + max);
// Output: min and max: -978 100123
```

**For-each loop** — simplest form when you don't need the index:

```java
int sum = 0;
for (int x : nums) {    // "for each int x in nums"
    sum += x;
}
```

**Multidimensional arrays** — arrays of arrays, declared with multiple `[]`:

```java
int table[][] = new int[3][4];  // 3 rows, 4 columns
table[0][0] = 1;
table[2][3] = 99;

// Rows can be different lengths (jagged arrays):
int jagged[][] = new int[3][];
jagged[0] = new int[1];
jagged[1] = new int[4];
jagged[2] = new int[2];
```

### Strings — Objects, Not Primitives

`String` is a class. String variables hold references to `String` objects, not the characters themselves. This has a critical consequence for comparison:

```java
String s1 = "Hello";
String s2 = new String("Hello");

// == compares REFERENCES (memory addresses), not character content!
System.out.println(s1 == s2);        // false — different objects

// .equals() compares the actual character content
System.out.println(s1.equals(s2));   // true — same characters
```

**Always use `.equals()` to compare Strings, never `==`.** Using `==` is one of the most common bugs in Java.

Strings are **immutable** — once created, a `String` object cannot be changed. Every apparent modification creates a new `String`. `s = s + "!"` creates a new string; the old one becomes eligible for GC. This is why `StringBuilder` exists (for building strings in loops).

Key `String` methods from the book:

```java
String s = "Java";
int    len   = s.length();              // 4
char   c     = s.charAt(0);            // 'J'
String upper = s.toUpperCase();         // "JAVA"
boolean eq   = s.equals("Java");        // true
boolean eq2  = s.equalsIgnoreCase("java"); // true
int     pos  = s.indexOf("av");         // 1
String  sub  = s.substring(1, 3);      // "av"  (1 inclusive, 3 exclusive)
```

### Command-Line Arguments

`args[]` in `main(String args[])` holds everything typed after the program name. Parse them to use them:

```java
class CommandLine {
    public static void main(String args[]) {
        for (int i = 0; i < args.length; i++) {
            System.out.println("args[" + i + "] = " + args[i]);
        }
    }
}
```

`java CommandLine Hello 42 World` → `args[0]="Hello"`, `args[1]="42"`, `args[2]="World"`. Arguments arrive as Strings — to use `"42"` as a number, call `Integer.parseInt(args[1])`.

### Bitwise Operators

These operate directly on the individual bits of integer values:

| Operator | Operation | Example |
|----------|-----------|---------|
| `&` | AND | `0b1010 & 0b1100` = `0b1000` |
| `\|` | OR | `0b1010 \| 0b0101` = `0b1111` |
| `^` | XOR | `0b1010 ^ 0b1100` = `0b0110` |
| `~` | NOT (invert all bits) | `~0b1010` = `...10101` |
| `>>` | Signed right shift (divides by 2ⁿ) | `8 >> 1` = `4` |
| `>>>` | Unsigned right shift (fills 0s) | useful for sign-bit work |
| `<<` | Left shift (multiplies by 2ⁿ) | `1 << 3` = `8` |

These are critical in networking, compression, cryptography, graphics, and embedded systems. Example: extracting the second byte of a 32-bit integer: `(value >> 8) & 0xFF`.

---

## Chapter 6 — A Closer Look at Methods and Classes

### Access Control — Encapsulation in Practice

Access modifiers enforce encapsulation:

| Modifier | Accessible From |
|----------|----------------|
| `public` | Anywhere |
| `private` | Only within the same class |
| `protected` | Same class + subclasses + same package |
| (none) | Same package only |

The book demonstrates with `FailSoftArray` — an array wrapped in a class where the actual array `a[]` is `private` and access goes through `get()` and `put()` methods that check bounds before accessing:

```java
class FailSoftArray {
    private int a[];      // the actual array is hidden
    private int errval;   // returned when get() fails
    public  int length;

    public FailSoftArray(int size, int errv) {
        a      = new int[size];
        errval = errv;
        length = size;
    }

    public int get(int index) {
        if (indexOK(index)) return a[index];
        return errval;           // graceful failure, no exception
    }

    public boolean put(int index, int val) {
        if (indexOK(index)) {
            a[index] = val;
            return true;
        }
        return false;
    }

    private boolean indexOK(int index) {
        return (index >= 0 && index < length);
    }
}
```

The caller can never produce an `ArrayIndexOutOfBoundsException` because they can never touch `a[]` directly. This is what encapsulation buys you — the class guarantees its own invariants regardless of how it is used.

### Method Overloading — Compile-Time Polymorphism

Multiple methods can share the same name if their parameter lists differ (number, type, or order of parameters):

```java
class Overload {
    int test(int a) {
        return a * a;
    }
    int test(int a, int b) {
        return a * b;
    }
    double test(double a) {
        return a * a;
    }
}

Overload ob = new Overload();
ob.test(10);       // calls test(int) → 100
ob.test(4, 5);     // calls test(int, int) → 20
ob.test(3.14);     // calls test(double) → ~9.8596
```

The compiler selects the right method based on the argument types at compile time — this is called **compile-time polymorphism** (or static dispatch). Note: **the return type alone cannot distinguish overloaded methods**. If you had `int foo()` and `double foo()` with identical parameters, the compiler cannot tell which to call from `foo()` alone.

### `static` Members — Belonging to the Class Itself

A `static` field is shared by all instances. There is only one copy for the entire class, not one per object:

```java
class StaticDemo {
    int x;           // each object has its own x
    static int y;    // one y shared by ALL StaticDemo objects
}

StaticDemo ob1 = new StaticDemo();
StaticDemo ob2 = new StaticDemo();

ob1.x = 10;
ob2.x = 20;          // ob1.x and ob2.x are independent

StaticDemo.y = 19;   // accessed via class name — no object needed
System.out.println(ob1.x + ob2.x + StaticDemo.y);   // 10 + 20 + 19 = 49
```

A `static` method is also called on the class, not an instance. Its constraints: it can only call other `static` methods, only access `static` fields, and has no `this` reference (there is no "current object"). `Math.sqrt()`, `Math.abs()`, `Integer.parseInt()` are all static.

### Recursion — A Method Calling Itself

A method is **recursive** if it calls itself. Each call gets its own stack frame with its own local variables. The critical requirement: there must be a **base case** that stops the recursion:

```java
// n! = n × (n-1) × (n-2) × ... × 1
int factorial(int n) {
    if (n == 1) return 1;              // base case — stops here
    return n * factorial(n - 1);       // recursive step
}
```

Trace of `factorial(4)`:
```
factorial(4) → 4 × factorial(3)
                      → 3 × factorial(2)
                                 → 2 × factorial(1)
                                              → 1  (base case)
                                 → 2 × 1 = 2
                      → 3 × 2 = 6
              → 4 × 6 = 24
```

Without the base case, factorial would call itself forever until the call stack runs out of memory — a `StackOverflowError`.

### Varargs — Variable-Length Argument Lists

A method that must accept a flexible number of arguments uses `...`:

```java
static void printAll(String msg, int... v) {
    System.out.print(msg + ": ");
    for (int x : v)
        System.out.print(x + " ");
    System.out.println();
}

printAll("One",   10);           // v = {10}
printAll("Three", 1, 2, 3);     // v = {1, 2, 3}
printAll("None");                // v = {}
```

Inside the method, `v` is just a regular array. The `...` must be the last parameter. Only one vararg parameter is allowed per method.

---

## Chapter 7 — Inheritance

### The `extends` Keyword

A subclass inherits all non-private fields and methods of its superclass:

```java
class TwoDShape {
    double width;
    double height;

    void showDim() {
        System.out.println("Width and height are " + width + " and " + height);
    }
}

class Triangle extends TwoDShape {   // Triangle IS-A TwoDShape
    String style;

    double area() {
        return width * height / 2;   // accesses TwoDShape's fields directly
    }

    void showStyle() {
        System.out.println("Triangle is " + style);
    }
}
```

`Triangle` objects have access to `width`, `height`, `showDim()`, AND their own `style`, `area()`, `showStyle()`. The subclass adds to the superclass — it never takes away.

**Java allows only single inheritance** — one superclass per class. Unlike C++, you cannot extend multiple classes simultaneously. You can, however, build deep hierarchies: `A → B → C → D`.

### `super` — Two Distinct Uses

**1. Calling the superclass constructor** — must be the very first statement in the subclass constructor:

```java
class Triangle extends TwoDShape {
    String style;

    Triangle(String s, double w, double h) {
        super(w, h);     // calls TwoDShape(double, double) — MUST be first
        style = s;
    }
}
```

If you don't call `super(...)` explicitly, Java automatically calls the no-argument superclass constructor. If the superclass has no no-arg constructor, it is a compile error.

**2. Accessing a hidden superclass member** — when a subclass field or method has the same name as a superclass one:

```java
class A {
    int i = 10;
}
class B extends A {
    int i = 20;           // hides A's i

    void show() {
        System.out.println("B's i: " + i);       // 20
        System.out.println("A's i: " + super.i); // 10
    }
}
```

### Constructor Execution Order in a Hierarchy

Constructors execute **top-down**: the superclass constructor always completes before the subclass constructor runs. This ensures the superclass portion of the object is fully initialized before the subclass adds its own state. Given `A → B → C`, the execution order is `A()`, then `B()`, then `C()`.

### `private` Members Are Not Inherited

Inheritance means the subclass *contains* the private fields of its superclass (they exist inside every object), but cannot *access* them directly. This is enforced at compile time:

```java
class TwoDShape {
    private double width;   // private!
    private double height;
}

class Triangle extends TwoDShape {
    double area() {
        return width * height / 2;   // COMPILE ERROR — private fields
    }
}
```

The solution: provide `public` or `protected` accessor methods in the superclass:

```java
class TwoDShape {
    private double width;
    private double height;

    double getWidth()  { return width; }
    double getHeight() { return height; }
    void setWidth(double w)  { width = w; }
    void setHeight(double h) { height = h; }
}

class Triangle extends TwoDShape {
    double area() {
        return getWidth() * getHeight() / 2;   // uses accessor methods — works
    }
}
```

### Method Overriding — Runtime Polymorphism

When a subclass defines a method with the **same name and same parameter types** as a method in its superclass, it **overrides** it. When you call that method, the subclass version runs:

```java
class A {
    void show() {
        System.out.println("show() in A");
    }
}

class B extends A {
    void show() {    // overrides A's show()
        System.out.println("show() in B");
    }
}

B ob = new B();
ob.show();   // prints: show() in B
```

**This is not the same as overloading.** Overriding requires the same signature. If you change the parameters, you're overloading (creating a new method), not overriding.

### Dynamic Method Dispatch — The Engine of Runtime Polymorphism

Here is the most powerful concept in Java OOP: **a superclass reference can hold a reference to any subclass object.** When you call an overridden method through that superclass reference, Java determines *at runtime* which version to execute based on the *actual type of the object being referenced*, not the type of the reference variable.

From the book:

```java
class Sup {
    void who() { System.out.println("who() in Sup"); }
}
class Sub1 extends Sup {
    void who() { System.out.println("who() in Sub1"); }
}
class Sub2 extends Sup {
    void who() { System.out.println("who() in Sub2"); }
}

class DynDispDemo {
    public static void main(String args[]) {
        Sup superOb = new Sup();
        Sub1 subOb1 = new Sub1();
        Sub2 subOb2 = new Sub2();

        Sup supRef;

        supRef = superOb;
        supRef.who();       // who() in Sup

        supRef = subOb1;
        supRef.who();       // who() in Sub1  ← object type, not reference type

        supRef = subOb2;
        supRef.who();       // who() in Sub2  ← object type, not reference type
    }
}
```

`supRef` is declared as `Sup`. But what version of `who()` is called is determined by what `supRef` points to at that moment — not what type `supRef` is. This is **dynamic method dispatch**, and it is the mechanism by which Java implements runtime polymorphism.

Why does this matter? Because you can write a method that takes a `Sup` reference and handles *any* subclass correctly, without knowing in advance what subclasses will be created. You can add new subclasses and your existing code still works.

### `abstract` Classes

An `abstract` class is one that cannot be instantiated but can define methods that subclasses must implement:

```java
abstract class TwoDShape {
    private double width;
    private double height;

    // normal method — inherited as-is
    void showDim() {
        System.out.println("Width and height are " + width + " and " + height);
    }

    // abstract method — NO body, subclasses MUST provide one
    abstract double area();
}

class Triangle extends TwoDShape {
    // Must implement area() or be abstract itself
    double area() {
        return getWidth() * getHeight() / 2;
    }
}
```

`abstract` forces a contract: every concrete subclass must provide an `area()` method. You cannot do `new TwoDShape()` — it exists only as a base for other classes.

### `final` in Inheritance

`final` has three meanings related to inheritance:

- **`final` variable** — a constant. Must be initialized at declaration, cannot be changed. Convention: `ALL_UPPERCASE`. Think `Math.PI`.
- **`final` method** — cannot be overridden by any subclass. Used to lock down critical behavior.
- **`final` class** — cannot be subclassed at all. `String` is `final` — nobody can extend it and change how it behaves.

---

## Chapter 8 — Packages and Interfaces

### Packages — Organizing and Protecting Code

A package is a namespace and an access boundary. Declaration at the top of a source file:

```java
package mypack;
```

Every class in that file is in `mypack`. The package maps directly to a directory on disk — `mypack` classes must be in a `mypack/` directory. To find packages, the JVM looks at the current directory, the `CLASSPATH` environment variable, or the `-classpath` command-line option.

To use a class from another package:

```java
import mypack.MyClass;    // import a specific class
import mypack.*;           // import all classes in the package
```

`java.lang` is imported automatically — that's how `System`, `String`, `Math`, etc. are available without imports.

### Access Control With Packages — The Full Picture

| Modifier | Same Class | Same Package | Subclass | Other Package |
|----------|:---:|:---:|:---:|:---:|
| `public` | ✓ | ✓ | ✓ | ✓ |
| `protected` | ✓ | ✓ | ✓ | ✗ |
| (none) | ✓ | ✓ | ✗ | ✗ |
| `private` | ✓ | ✗ | ✗ | ✗ |

`protected` is the bridge between `private` (too restrictive for inheritance) and `public` (too open for everything).

### Interfaces — Contracts Without Implementation

An interface defines a set of methods that a class *must* implement. Before JDK 8, all interface methods were implicitly `public abstract` (no body):

```java
interface Series {
    int getNext();          // returns next number in series
    void reset();           // resets to start
    void setStart(int x);   // sets starting value
}
```

Any class that claims to implement `Series` must provide all three methods:

```java
class ByTwos implements Series {
    int start, val;

    ByTwos() { start = 0; val = 0; }

    public int getNext() { val += 2; return val; }
    public void reset()  { val = start; }
    public void setStart(int x) { start = x; val = x; }
}
```

**A class can implement multiple interfaces** — this is Java's answer to multiple inheritance:

```java
class MyClass implements Interface1, Interface2, Interface3 {
    // must implement all methods from all three interfaces
}
```

**Interfaces support polymorphism** — you can declare a reference of interface type and point it at any implementing class:

```java
Series ob;
ob = new ByTwos();
ob.getNext();   // works — ob implements Series

ob = new ByThrees();   // also implements Series
ob.getNext();   // calls ByThrees' version
```

**Default methods (JDK 8+)** — interfaces can now have methods with bodies using `default`. This allows adding methods to an interface without forcing every implementing class to change:

```java
interface MyIF {
    int getNumber();

    default String getString() {   // has a body — "default"
        return "Default String";
    }
}
```

The implementing class can override `getString()` or just inherit the default version.

---

## Chapter 9 — Exception Handling

### The Problem Exceptions Solve

Without exceptions, every operation that can fail must return an error code, and every caller must check it. This produces deeply nested if-chains, and programmers routinely skip the checks. Exceptions separate the normal logic from the error-handling logic into distinct code regions.

### The Five Exception Keywords

```java
try {
    // code you want to monitor for errors
} catch (ExceptionType1 exOb) {
    // handle ExceptionType1
} catch (ExceptionType2 exOb) {
    // handle ExceptionType2
} finally {
    // ALWAYS executes — cleanup code
}
```

Plus `throw` (manually throw an exception) and `throws` (declare what a method might throw).

### A Simple Exception Example — From the Book

```java
class ExcDemo1 {
    public static void main(String args[]) {
        int nums[] = new int[4];

        try {
            System.out.println("Before exception is generated.");
            nums[7] = 10;      // accessing index 7 of a 4-element array — BOOM
            System.out.println("this won't be displayed");
        } catch (ArrayIndexOutOfBoundsException exc) {
            System.out.println("Index out-of-bounds!");
        }
        System.out.println("After catch statement.");
    }
}
```

Output:
```
Before exception is generated.
Index out-of-bounds!
After catch statement.
```

When `nums[7]` is accessed, the JVM throws `ArrayIndexOutOfBoundsException`. Control jumps immediately to the matching `catch` block. Code after the throw inside `try` (the second `println`) is skipped. Execution resumes normally after the entire `try-catch` block.

### Multiple `catch` Blocks — Most Specific First

Each `catch` handles a specific exception type. Since Java exceptions form a class hierarchy, ordering matters:

```java
try {
    // some risky code
} catch (ArithmeticException exc) {
    System.out.println("Arithmetic error: " + exc);
} catch (ArrayIndexOutOfBoundsException exc) {
    System.out.println("Array error: " + exc);
} catch (Exception exc) {
    System.out.println("Some other error: " + exc);
}
```

Always put the most specific types first. `Exception` catches everything — if it were first, the specific handlers would never run. A common mistake is catching a superclass exception before its subclasses.

### `finally` — Code That Always Runs

```java
try {
    // code that may throw
} catch (Exception exc) {
    System.out.println("An exception occurred.");
} finally {
    System.out.println("This ALWAYS executes.");
}
```

`finally` runs whether an exception occurred or not, whether it was caught or not, whether the `try` returns normally or throws. This makes it ideal for cleanup — closing files, releasing locks, returning a database connection to a pool. The pattern:

```java
FileInputStream fis = null;
try {
    fis = new FileInputStream("file.txt");
    // read file...
} catch (IOException exc) {
    System.out.println("I/O error: " + exc);
} finally {
    if (fis != null)
        try { fis.close(); } catch (IOException e) {}  // close in finally
}
```

### `throw` — Manually Throwing an Exception

You can throw an exception yourself with `throw new ExceptionType(message)`:

```java
class ThrowDemo {
    static void demoproc() {
        try {
            throw new NullPointerException("demo");   // manually thrown
        } catch (NullPointerException e) {
            System.out.println("Caught inside demoproc.");
            throw e;   // re-throw it — pass it up the call stack
        }
    }

    public static void main(String args[]) {
        try {
            demoproc();
        } catch (NullPointerException e) {
            System.out.println("Recaught: " + e);
        }
    }
}
```

### Checked vs Unchecked Exceptions

**Checked exceptions** — subclasses of `Exception` (but not `RuntimeException`). The compiler forces you to either catch them or declare them with `throws`. Examples: `IOException`, `SQLException`. These are for conditions outside the programmer's control (file not found, network failure).

**Unchecked exceptions** — subclasses of `RuntimeException`. No catch required. Examples: `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ArithmeticException`. These indicate programming errors that should have been prevented with proper code.

**Declaring exceptions with `throws`:**

```java
void myMethod() throws IOException, SQLException {
    // this method might throw those exceptions
    // the caller is responsible for handling them
}
```

### Custom Exceptions

Extend `Exception` to create domain-specific exceptions:

```java
class NonIntResultException extends Exception {
    int n, d;

    NonIntResultException(int a, int b) {
        super("Result not an integer");   // message for getMessage()
        n = a;
        d = b;
    }

    public String toString() {
        return "Result of " + n + " / " + d + " is non-integer.";
    }
}
```

Custom exceptions let you communicate precise meaning instead of using generic exceptions for everything.

### try-with-resources (JDK 7+)

Any object implementing `AutoCloseable` can be opened in a `try` statement and will be automatically closed when the block exits — no `finally` needed:

```java
try (FileInputStream fin = new FileInputStream("test.txt")) {
    // use fin here
}   // fin.close() is called automatically here — even if an exception is thrown
```

This is the modern, correct way to work with streams, connections, and any resource that needs cleanup.

---

## Chapter 10 — Using I/O

### Java's Two Stream Systems

Java I/O uses the abstraction of a **stream** — a sequence of bytes flowing in or out. There are two parallel hierarchies:

**Byte streams** — handle raw 8-bit data. Root classes: `InputStream` and `OutputStream`. Use for binary files, images, compressed data, network protocols.

**Character streams** — handle 16-bit Unicode characters. Root classes: `Reader` and `Writer`. Use for text files, human-readable data. More efficient for character-by-character text I/O.

At the lowest level, all I/O is bytes. Character streams are a convenience layer on top.

### The Pre-Defined Streams

Three streams exist automatically (via `java.lang.System`):

- `System.out` — `PrintStream` connected to the console output (stdout)
- `System.in` — `InputStream` connected to keyboard input (stdin)
- `System.err` — `PrintStream` connected to console error output (stderr)

These are byte streams for historical reasons (they predate Java's character stream system).

### Reading Console Input

For production code, wrap `System.in` in a `BufferedReader` for efficient line reading:

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String str = br.readLine();   // reads a full line of text
```

`InputStreamReader` converts the byte stream (`System.in`) to a character stream. `BufferedReader` buffers the characters and provides `readLine()`.

### Reading and Writing Files — Byte Streams

```java
// Read a file byte by byte
try (FileInputStream fin = new FileInputStream("test.txt")) {
    int i;
    while ((i = fin.read()) != -1) {   // read() returns -1 at end of file
        System.out.print((char) i);
    }
}

// Write a file byte by byte
try (FileOutputStream fout = new FileOutputStream("output.txt")) {
    String str = "Hello, World!\n";
    byte buf[] = str.getBytes();
    fout.write(buf);
}
```

### Reading and Writing Files — Character Streams

```java
// Read text file line by line
try (BufferedReader br = new BufferedReader(new FileReader("test.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
}

// Write a text file
try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
    bw.write("First line");
    bw.newLine();
    bw.write("Second line");
}
```

`BufferedReader` and `BufferedWriter` are wrappers that add internal buffering and the newline-aware methods (`readLine()`, `newLine()`). Always wrap file streams in buffered streams for non-trivial I/O.

---

## Chapter 11 — Multithreaded Programming

### What Threads Are

A **thread** is an independent path of execution inside a program. All Java programs have at least one thread — the **main thread** that starts when `main()` is called. You create additional threads to do work concurrently.

Multithreading is for: UI responsiveness (one thread handles user input while another does computation), server scalability (one thread per client connection), parallelizing CPU work across multiple cores.

### Creating a Thread — The Runnable Approach

The recommended approach: implement `Runnable`, which has a single method `run()`:

```java
class MyThread implements Runnable {
    String thrdName;

    MyThread(String name) {
        thrdName = name;
    }

    public void run() {    // this is the thread's entry point
        System.out.println(thrdName + " starting.");
        try {
            for (int count = 0; count < 10; count++) {
                Thread.sleep(400);   // pause 400ms without burning CPU
                System.out.println("In " + thrdName + ", count is " + count);
            }
        } catch (InterruptedException exc) {
            System.out.println(thrdName + " interrupted.");
        }
        System.out.println(thrdName + " terminating.");
    }
}

class UseThreads {
    public static void main(String args[]) {
        System.out.println("Main thread starting.");

        MyThread mt = new MyThread("Child #1");    // create the Runnable
        Thread newThrd = new Thread(mt);           // wrap it in a Thread
        newThrd.start();                            // start() calls run() in a new thread

        for (int i = 0; i < 50; i++) {
            System.out.print(".");
            try { Thread.sleep(100); }
            catch (InterruptedException exc) {}
        }
        System.out.println("Main thread ending.");
    }
}
```

`start()` launches the thread and calls `run()` in the new thread. The main thread and the child thread now run concurrently — their output interleaves.

### Thread States and Key Methods

A thread moves through: New → Runnable → Running → Blocked/Waiting → Terminated.

| Method | Purpose |
|--------|---------|
| `start()` | Launch the thread (calls `run()`) |
| `sleep(ms)` | Pause this thread for `ms` milliseconds; another thread can run |
| `join()` | Wait for a specific thread to finish before continuing |
| `isAlive()` | Returns `true` if the thread has started and not yet terminated |
| `getName()` / `setName()` | Thread identifier for debugging |
| `getPriority()` / `setPriority()` | Priority 1–10; `Thread.NORM_PRIORITY` = 5 |

### Synchronization — Preventing Race Conditions

When two threads both access shared data, the results can be wrong if they interleave at the wrong moment. This is called a **race condition**. The `synchronized` keyword ensures only one thread executes a block at a time:

```java
class Callme {
    synchronized void call(String msg) {   // only one thread at a time
        System.out.print("[" + msg);
        try { Thread.sleep(1000); }
        catch (InterruptedException exc) {}
        System.out.println("]");
    }
}
```

Without `synchronized`, two threads calling `call()` simultaneously could interleave their output: `[Hello[World]]`. With `synchronized`, one call completes completely before the next starts.

You can also synchronize a block inside a method instead of the whole method:

```java
synchronized (object) {
    // only one thread at a time per object instance
}
```

### `wait()` and `notify()` — Thread Coordination

For producer-consumer patterns, threads need to communicate. `wait()` pauses a thread and releases its lock. `notify()` wakes one waiting thread. Both must be called from a `synchronized` context:

```java
synchronized void put(int val) {
    while (valueSet)           // if a value is waiting, pause
        wait();
    n = val;
    valueSet = true;
    notify();                  // wake up the consumer
}

synchronized int get() {
    while (!valueSet)          // if no value is ready, pause
        wait();
    valueSet = false;
    notify();                  // wake up the producer
    return n;
}
```

---

## Chapter 12 — Enumerations, Autoboxing, and Annotations

### Enumerations — Type-Safe Named Constants

Before enumerations, constants were just `static final int` values. The compiler could not prevent you from passing `5` where a valid transport mode was expected. Enumerations fix this:

```java
enum Transport {
    CAR, TRUCK, AIRPLANE, TRAIN, BOAT
}
```

`Transport` is now a type. Only the five named values are valid. The compiler rejects anything else:

```java
Transport tp = Transport.AIRPLANE;

if (tp == Transport.TRAIN)
    System.out.println("tp contains TRAIN.");

switch (tp) {
    case CAR:      System.out.println("A car carries people."); break;
    case TRUCK:    System.out.println("A truck carries freight."); break;
    case AIRPLANE: System.out.println("An airplane flies."); break;
    case TRAIN:    System.out.println("A train runs on rails."); break;
    case BOAT:     System.out.println("A boat sails on water."); break;
}
```

**Java enumerations are class types** — this makes them far more powerful than enums in C/C++. You can give them constructors, fields, and methods:

```java
enum Transport {
    CAR(65), TRUCK(55), AIRPLANE(600), TRAIN(70), BOAT(22);

    private int speed;

    Transport(int s) { speed = s; }

    int getSpeed() { return speed; }
}

System.out.println("Speed of AIRPLANE: " + Transport.AIRPLANE.getSpeed()); // 600
```

Built-in methods: `values()` returns all constants as an array; `ordinal()` returns the position (0-based); `valueOf(String)` converts a name string to the enum constant.

### Autoboxing and Unboxing — Primitives Meet Objects

Java collections (`ArrayList`, `HashMap`, etc.) can only hold objects — they cannot hold `int`, `double`, `boolean` directly. To bridge this, Java provides **wrapper classes**: `Integer`, `Double`, `Boolean`, `Character`, etc.

Before autoboxing, you had to convert manually:

```java
Integer iOb = Integer.valueOf(100);   // manually box the int
int i = iOb.intValue();               // manually unbox
```

**Autoboxing (JDK 5+)** makes this automatic:

```java
Integer iOb = 100;    // int 100 is automatically boxed into Integer
int i = iOb;          // Integer is automatically unboxed to int
```

This lets you use primitive values directly with collections and generic types that require objects:

```java
ArrayList<Integer> list = new ArrayList<>();
list.add(42);              // 42 autoboxed to Integer(42)
int v = list.get(0);       // Integer unboxed to int
```

Autoboxing also works in expressions — `Integer` objects can participate in arithmetic:

```java
Integer iOb = 10;
iOb++;          // unboxed, incremented, re-boxed — all automatic
```

---

## Chapter 13 — Generics

### The Problem Before Generics

Before generics (before JDK 5), to write a container that held any type, you used `Object` references. But taking a value back required a cast, and there was no guarantee you had the right type:

```java
class NonGen {
    Object ob;
    NonGen(Object o) { ob = o; }
    Object getob()   { return ob; }
}

NonGen iOb = new NonGen(88);
int v = (Integer) iOb.getob();   // cast required — type unsafe
```

Nothing stopped you from putting a `String` in and trying to cast it out as `Integer`. The bug would appear at runtime, not at compile time.

### Generic Classes — Type Parameters

A generic class parameterizes its type:

```java
class Gen<T> {    // T is a type parameter — placeholder for the real type
    T ob;

    Gen(T o) {
        ob = o;
    }

    T getob() {
        return ob;
    }

    void showType() {
        System.out.println("Type of T is " + ob.getClass().getName());
    }
}
```

When you instantiate, you supply the actual type:

```java
Gen<Integer> iOb = new Gen<Integer>(88);
iOb.showType();               // Type of T is java.lang.Integer
int v = iOb.getob();          // NO CAST NEEDED — compiler knows it's Integer
System.out.println(v);        // 88

Gen<String> strOb = new Gen<String>("Generics Test");
strOb.showType();             // Type of T is java.lang.String
String str = strOb.getob();   // NO CAST NEEDED
System.out.println(str);      // Generics Test
```

The compiler checks types at compile time. You cannot do `Gen<Integer> iOb = new Gen<Integer>("hello")` — it won't compile. The bug is caught before it can happen.

**Diamond operator `<>` (JDK 7+)** — type inference for the constructor:

```java
Gen<Integer> iOb = new Gen<>(88);   // type inferred from left side
```

### Bounded Type Parameters

Restrict which types can be used with a generic:

```java
class Stats<T extends Number> {   // T must be Number or a subclass of Number
    T[] nums;

    Stats(T[] o) { nums = o; }

    double average() {
        double sum = 0.0;
        for (T n : nums)
            sum += n.doubleValue();   // safe — Number has doubleValue()
        return sum / nums.length;
    }
}

Integer inums[] = {1, 2, 3, 4, 5};
Stats<Integer> iob = new Stats<>(inums);
System.out.println("Average: " + iob.average());   // 3.0

// Stats<String> strob = new Stats<>(new String[1]); // COMPILE ERROR — String is not Number
```

### Wildcards

A wildcard `?` represents an unknown type. It lets you write methods that work with generic types without knowing the exact type argument:

```java
static double absAverage(Stats<?> ob) {   // works with Stats<Integer>, Stats<Double>, etc.
    double sum = 0.0;
    for (int i = 0; i < ob.nums.length; i++)
        sum += Math.abs(ob.nums[i].doubleValue());
    return sum / ob.nums.length;
}
```

- `<?>` — any type
- `<? extends T>` — T or any subtype of T (upper bound)
- `<? super T>` — T or any supertype of T (lower bound)

### Generic Methods

A method can be generic independently of whether its class is generic:

```java
static <T extends Comparable<T>, V extends T> boolean isIn(T x, V[] y) {
    for (int i = 0; i < y.length; i++)
        if (x.compareTo(y[i]) == 0) return true;
    return false;
}
```

---

## Chapter 14 — Lambda Expressions and Method References

### Why Lambdas Exist

Before lambdas, passing behavior (a piece of code) to a method required creating a class that implements an interface, then instantiating it. For simple one-method callbacks, this was enormous boilerplate. Lambdas let you express behavior directly as a value.

### Functional Interfaces — The Target Type

A **functional interface** has exactly one abstract method. Lambdas implement functional interfaces:

```java
interface MyValue {
    double getValue();
}

interface MyParamValue {
    double getValue(double d);
}
```

### Lambda Syntax

```java
// No parameters, returns a constant
() -> 98.6

// One parameter, returns reciprocal
(n) -> 1.0 / n

// Boolean expression
(n) -> (n % 2) == 0

// Block lambda — multiple statements
(n) -> {
    int result = 1;
    for (int i = 2; i <= n; i++)
        result *= i;
    return result;
}
```

Assigning and calling:

```java
MyValue myVal = () -> 98.6;
System.out.println(myVal.getValue());   // 98.6

MyParamValue myPval = (d) -> 1.0 / d;
System.out.println(myPval.getValue(4.0));   // 0.25
```

The lambda becomes the implementation of the interface's abstract method. When you call `myVal.getValue()`, the lambda executes.

### Generic Functional Interfaces

```java
interface SomeTest<T> {
    boolean test(T n, T m);
}

SomeTest<Integer> isFactor = (n, d) -> (n % d) == 0;
System.out.println(isFactor.test(10, 2));   // true
System.out.println(isFactor.test(10, 3));   // false

SomeTest<Double> isFactorD = (n, d) -> (n % d) == 0;
System.out.println(isFactorD.test(212.0, 4.0));   // true
```

One functional interface, multiple types, zero code duplication.

### Variable Capture — Closures

A lambda can access local variables from the enclosing scope, but only if they are **effectively final** (never modified after the lambda is created):

```java
int n = 10;
MyValue myLambda = () -> n * 2;   // captures n — fine, n never changes
// n = 20;    // would make n NOT effectively final — compile error
```

Instance variables and static variables are accessible without restriction.

### Method References — Shorthand for Existing Methods

When a lambda just calls an existing method, you can replace it with a method reference:

```java
// Instead of:
(str) -> System.out.println(str)
// Write:
System.out::println

// Instead of:
(n) -> Math.abs(n)
// Write:
Math::abs
```

Forms:
- `ClassName::staticMethod` — static method reference
- `object::instanceMethod` — instance method on a specific object
- `ClassName::instanceMethod` — instance method, first argument becomes the receiver
- `ClassName::new` — constructor reference

---

## Chapters 15–17 — Applets, Swing, and JavaFX

### Chapter 15 — Applets and Event Handling

An **applet** runs inside a browser window (or applet viewer). It extends `JApplet` and overrides lifecycle methods: `init()` (once at creation), `start()` (each time it becomes visible), `stop()` (when hidden), `destroy()` (at removal), `paint(Graphics g)` (to draw content).

**Event Handling — the Delegation Model**: An event *source* (e.g., a button) generates an event object. An *event listener* (an object implementing a listener interface) receives and processes it. Connecting source to listener:

```java
button.addActionListener(new ActionListener() {
    public void actionPerformed(ActionEvent ae) {
        // handle click here
    }
});
```

With lambdas (JDK 8+), the anonymous class collapses to:

```java
button.addActionListener(ae -> handleClick(ae));
```

Common listener interfaces: `ActionListener` (button clicks), `MouseListener` (mouse clicks/enter/exit), `MouseMotionListener` (drag/move), `KeyListener` (keyboard).

### Chapter 16 — Swing

Swing is a full GUI toolkit built on top of AWT. It is **lightweight**: Swing components are drawn in Java rather than delegating to the OS. This gives consistent appearance across platforms and full programmatic control.

**Fundamental rules:**
1. All GUI creation and updates must happen on the **Event Dispatch Thread (EDT)**. Use `SwingUtilities.invokeLater()`.
2. Never do long computations on the EDT — it freezes the UI. Use worker threads and communicate back via `SwingUtilities.invokeLater()`.

Minimal Swing application:

```java
SwingUtilities.invokeLater(() -> {
    JFrame jfrm = new JFrame("My App");
    jfrm.setSize(300, 200);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    JLabel jlab = new JLabel("Hello, Swing!");
    jfrm.add(jlab);

    jfrm.setVisible(true);
});
```

**Key components**: `JButton`, `JLabel`, `JTextField`, `JCheckBox`, `JRadioButton`, `JList`, `JComboBox`, `JTable`.

**Layout managers** control how components are arranged: `FlowLayout` (left-to-right, wraps), `BorderLayout` (north/south/east/west/center), `GridLayout` (uniform grid).

**Handling button clicks:**

```java
JButton jbtn = new JButton("Click Me");
jbtn.addActionListener(ae -> jlab.setText("Button was pressed!"));
jfrm.add(jbtn);
```

### Chapter 17 — JavaFX

JavaFX is the modern successor to Swing, introduced in JDK 8. Architecture:

- **Stage** — the top-level window
- **Scene** — the content of the stage; holds a scene graph
- **Nodes** — all UI elements are nodes in a tree

Every JavaFX application extends `Application` and overrides `start(Stage stage)`:

```java
public class JavaFXDemo extends Application {
    public void start(Stage myStage) {
        myStage.setTitle("JavaFX Demo");

        FlowPane rootNode = new FlowPane(10, 10);
        Scene myScene = new Scene(rootNode, 300, 200);
        myStage.setScene(myScene);

        Label myLabel = new Label("JavaFX is the future.");
        rootNode.getChildren().add(myLabel);

        myStage.show();
    }

    public static void main(String args[]) {
        launch(args);
    }
}
```

JavaFX supports CSS styling, FXML (declarative UI in XML), 2D and 3D graphics, animation, media playback, and binding (automatically sync values between properties).

---

## Key Concepts Across All Chapters

### When to Use Each Loop
- Count known in advance → `for`
- Count unknown, might be zero iterations → `while`
- Always at least one iteration → `do-while`

### The OOP Decision Framework
- Repeated behavior across unrelated classes → **interface**
- Shared implementation among related classes → **abstract class**
- Complete implementation to inherit and extend → **concrete superclass**

### Exception Strategy
- Recoverable, external failure (file missing, network down) → **checked exception**, force the caller to handle it
- Programming error (null pointer, array bounds) → **unchecked exception**, fix the code
- Always use **try-with-resources** for anything that must be closed

### Generics vs Object
- `Object`-based collections — no type safety, requires casts, runtime bugs
- Generic collections — type safety at compile time, no casts, bugs caught before running

### Lambda Expression Use Cases
- Short callbacks (event handlers, comparators)
- Replacing single-method anonymous inner classes
- Functional-style processing with Streams API (`filter`, `map`, `reduce`)

### Thread Safety Checklist
- Shared mutable data → synchronize access
- One thread produces, another consumes → `wait()` / `notify()` in synchronized methods
- Read-only data shared across threads → no synchronization needed
- Independent tasks → no synchronization needed
