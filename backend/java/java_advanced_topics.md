# Ultimate Java Advanced Topics: Complete Guide

## For Alexandro Disla — A Python Developer Learning Java

---

# Table of Contents

1. [Exceptions](#1-exceptions)
2. [Generics](#2-generics)
3. [Collections Framework](#3-collections-framework)
4. [Lambda Expressions & Functional Interfaces](#4-lambda-expressions--functional-interfaces)
5. [Streams API](#5-streams-api)
6. [Concurrency & Multi-threading](#6-concurrency--multi-threading)
7. [The Executor Framework](#7-the-executor-framework)

---

# 1. Exceptions

## What Are Exceptions?

Exceptions are **events that disrupt the normal flow of a program**. In Java, exceptions are objects that represent errors or unexpected conditions. Unlike Python where you have `try/except`, Java uses `try/catch` with a more rigid type system.

## The Exception Hierarchy

```
Throwable (root class)
├── Error (serious problems - don't catch these)
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── VirtualMachineError
│
└── Exception (recoverable problems)
    ├── RuntimeException (unchecked - don't need to declare)
    │   ├── NullPointerException
    │   ├── IndexOutOfBoundsException
    │   ├── IllegalArgumentException
    │   └── ArithmeticException
    │
    └── Checked Exceptions (MUST be handled or declared)
        ├── IOException
        ├── SQLException
        └── FileNotFoundException
```

## Checked vs Unchecked Exceptions

This is **the biggest difference from Python**. Java has two categories:

### Checked Exceptions (Compile-time)
- The compiler **forces** you to handle them
- Must use `try/catch` OR declare with `throws`
- Examples: `IOException`, `SQLException`, `FileNotFoundException`

### Unchecked Exceptions (Runtime)
- Extend `RuntimeException`
- Compiler doesn't force handling
- Examples: `NullPointerException`, `ArrayIndexOutOfBoundsException`

## Basic Exception Handling

```java
public class ExceptionDemo {
    
    public static void main(String[] args) {
        // Basic try-catch
        try {
            int result = 10 / 0;  // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero!");
            System.out.println("Message: " + e.getMessage());
            e.printStackTrace();  // Print full stack trace
        }
    }
}
```

## Multiple Catch Blocks

```java
public class MultipleCatchDemo {
    
    public static void readFile(String path) {
        try {
            FileReader file = new FileReader(path);
            int data = file.read();
            int[] arr = new int[5];
            arr[10] = data;  // IndexOutOfBoundsException
            
        } catch (FileNotFoundException e) {
            // Most specific exception first
            System.out.println("File not found: " + path);
            
        } catch (IOException e) {
            // More general IO exception
            System.out.println("Error reading file: " + e.getMessage());
            
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Array index error!");
            
        } catch (Exception e) {
            // Catch-all (put last)
            System.out.println("Something went wrong: " + e.getMessage());
        }
    }
}
```

## Multi-Catch (Java 7+)

When you want to handle multiple exceptions the same way:

```java
public class MultiCatchDemo {
    
    public static void process(String data) {
        try {
            int number = Integer.parseInt(data);
            int[] arr = new int[5];
            arr[number] = 100;
            
        } catch (NumberFormatException | IndexOutOfBoundsException e) {
            // Handle both the same way
            System.out.println("Invalid input: " + e.getMessage());
        }
    }
}
```

## The `finally` Block

The `finally` block **always executes**, whether an exception occurred or not. It's used for cleanup (closing files, connections, etc.).

```java
public class FinallyDemo {
    
    public static void readFile(String path) {
        FileReader reader = null;
        
        try {
            reader = new FileReader(path);
            int data = reader.read();
            System.out.println("Read: " + (char) data);
            
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
            
        } finally {
            // This ALWAYS runs
            System.out.println("Cleanup starting...");
            
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.out.println("Error closing file");
                }
            }
            
            System.out.println("Cleanup complete");
        }
    }
}
```

## Try-With-Resources (Java 7+) — THE MODERN WAY

This is like Python's `with` statement. Resources are automatically closed!

```java
public class TryWithResourcesDemo {
    
    // OLD WAY - verbose and error-prone
    public static void oldWay(String path) {
        FileReader reader = null;
        try {
            reader = new FileReader(path);
            // use reader...
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    
    // NEW WAY - clean and automatic
    public static void newWay(String path) {
        // Resource declared in parentheses is auto-closed
        try (FileReader reader = new FileReader(path);
             BufferedReader buffered = new BufferedReader(reader)) {
            
            String line;
            while ((line = buffered.readLine()) != null) {
                System.out.println(line);
            }
            
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        // No finally needed! Both readers are automatically closed
    }
}
```

**Note:** Any class implementing `AutoCloseable` or `Closeable` can be used with try-with-resources.

## Throwing Exceptions

```java
public class ThrowingExceptions {
    
    // Throwing unchecked exception (no declaration needed)
    public static void validateAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative: " + age);
        }
        if (age > 150) {
            throw new IllegalArgumentException("Age seems unrealistic: " + age);
        }
    }
    
    // Throwing checked exception (MUST declare with 'throws')
    public static void loadConfig(String path) throws IOException {
        if (!new File(path).exists()) {
            throw new FileNotFoundException("Config file not found: " + path);
        }
        // Load file...
    }
    
    // Declaring multiple checked exceptions
    public static void connectDatabase(String url) 
            throws SQLException, ClassNotFoundException {
        Class.forName("com.mysql.jdbc.Driver");
        Connection conn = DriverManager.getConnection(url);
    }
}
```

## Creating Custom Exceptions

```java
// Custom unchecked exception
public class InsufficientFundsException extends RuntimeException {
    
    private final double amount;
    private final double balance;
    
    public InsufficientFundsException(double amount, double balance) {
        super(String.format(
            "Cannot withdraw %.2f. Current balance: %.2f", 
            amount, balance
        ));
        this.amount = amount;
        this.balance = balance;
    }
    
    public double getAmount() {
        return amount;
    }
    
    public double getBalance() {
        return balance;
    }
}

// Custom checked exception
public class UserNotFoundException extends Exception {
    
    private final String userId;
    
    public UserNotFoundException(String userId) {
        super("User not found: " + userId);
        this.userId = userId;
    }
    
    public String getUserId() {
        return userId;
    }
}

// Using custom exceptions
public class BankAccount {
    private double balance;
    
    public void withdraw(double amount) {
        if (amount > balance) {
            throw new InsufficientFundsException(amount, balance);
        }
        balance -= amount;
    }
}
```

## Exception Chaining

Wrap lower-level exceptions in higher-level ones while preserving the original cause:

```java
public class ExceptionChaining {
    
    public static User loadUser(String id) throws ServiceException {
        try {
            // Low-level database call
            return database.findUser(id);
            
        } catch (SQLException e) {
            // Wrap in higher-level exception, preserving original
            throw new ServiceException("Failed to load user: " + id, e);
        }
    }
}

// The custom exception with cause
public class ServiceException extends Exception {
    
    public ServiceException(String message, Throwable cause) {
        super(message, cause);  // Pass cause to parent
    }
}

// Accessing the chain
try {
    loadUser("123");
} catch (ServiceException e) {
    System.out.println("Service error: " + e.getMessage());
    System.out.println("Caused by: " + e.getCause().getMessage());
}
```

## Best Practices for Exceptions

```java
public class ExceptionBestPractices {
    
    // 1. Be specific - catch the most specific exception possible
    // BAD:
    public void bad1() {
        try {
            // code
        } catch (Exception e) {  // Too broad!
            e.printStackTrace();
        }
    }
    
    // GOOD:
    public void good1() {
        try {
            // code
        } catch (FileNotFoundException e) {
            // Handle specifically
        } catch (IOException e) {
            // Handle other IO issues
        }
    }
    
    // 2. Don't catch and ignore
    // BAD:
    public void bad2() {
        try {
            // code
        } catch (Exception e) {
            // Empty catch block - silent failure!
        }
    }
    
    // GOOD:
    public void good2() {
        try {
            // code
        } catch (Exception e) {
            logger.error("Operation failed", e);
            throw new RuntimeException("Could not complete operation", e);
        }
    }
    
    // 3. Use exceptions for exceptional cases, not control flow
    // BAD:
    public void bad3(String[] arr) {
        try {
            int i = 0;
            while (true) {
                System.out.println(arr[i++]);
            }
        } catch (IndexOutOfBoundsException e) {
            // Using exception for normal termination
        }
    }
    
    // GOOD:
    public void good3(String[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
    
    // 4. Clean up resources with try-with-resources
    // GOOD:
    public void good4(String path) {
        try (var reader = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = reader.readLine()) != null) {
                process(line);
            }
        } catch (IOException e) {
            logger.error("Failed to read file", e);
        }
    }
}
```

---

# 2. Generics

## What Are Generics?

Generics allow you to write **type-safe, reusable code**. They're similar to Python's type hints, but in Java they're **enforced at compile time**.

**Python equivalent concept:**
```python
from typing import List, TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item
```

## The Problem Generics Solve

```java
// WITHOUT Generics (the old way)
public class OldWay {
    public static void main(String[] args) {
        List list = new ArrayList();  // Raw type
        list.add("Hello");
        list.add(123);  // No error at compile time!
        
        // Dangerous - might fail at runtime
        for (Object item : list) {
            String s = (String) item;  // ClassCastException on 123!
        }
    }
}

// WITH Generics (the modern way)
public class NewWay {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();  // Type-safe
        list.add("Hello");
        // list.add(123);  // COMPILE ERROR! Type safety enforced
        
        for (String item : list) {
            System.out.println(item);  // No casting needed
        }
    }
}
```

## Generic Classes

```java
// A generic Box that can hold any type
public class Box<T> {
    
    private T content;
    
    public Box(T content) {
        this.content = content;
    }
    
    public T getContent() {
        return content;
    }
    
    public void setContent(T content) {
        this.content = content;
    }
    
    public boolean isEmpty() {
        return content == null;
    }
}

// Usage
public class BoxDemo {
    public static void main(String[] args) {
        // Box of Strings
        Box<String> stringBox = new Box<>("Hello");
        String s = stringBox.getContent();  // No casting!
        
        // Box of Integers
        Box<Integer> intBox = new Box<>(42);
        int num = intBox.getContent();  // Auto-unboxing
        
        // Box of custom objects
        Box<User> userBox = new Box<>(new User("Alex"));
        User user = userBox.getContent();
    }
}
```

## Multiple Type Parameters

```java
// A Pair with two different types
public class Pair<K, V> {
    
    private K key;
    private V value;
    
    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }
    
    public K getKey() { return key; }
    public V getValue() { return value; }
    
    public void setKey(K key) { this.key = key; }
    public void setValue(V value) { this.value = value; }
    
    @Override
    public String toString() {
        return "Pair{" + key + " = " + value + "}";
    }
}

// Usage
public class PairDemo {
    public static void main(String[] args) {
        Pair<String, Integer> score = new Pair<>("Alex", 100);
        System.out.println(score.getKey());   // "Alex"
        System.out.println(score.getValue()); // 100
        
        Pair<Integer, List<String>> complex = new Pair<>(
            1, 
            Arrays.asList("a", "b", "c")
        );
    }
}
```

## Generic Methods

You can make individual methods generic, even in non-generic classes:

```java
public class GenericMethods {
    
    // Generic method - type parameter <T> before return type
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }
    
    // Generic method that returns the type
    public static <T> T getFirst(List<T> list) {
        if (list.isEmpty()) {
            return null;
        }
        return list.get(0);
    }
    
    // Multiple type parameters
    public static <K, V> Map<K, V> createMap(K key, V value) {
        Map<K, V> map = new HashMap<>();
        map.put(key, value);
        return map;
    }
    
    // Generic method with relationship between parameters
    public static <T> void copy(List<T> source, List<T> destination) {
        for (T item : source) {
            destination.add(item);
        }
    }
    
    public static void main(String[] args) {
        // Type inference - compiler figures out the type
        Integer[] numbers = {1, 2, 3};
        printArray(numbers);  // T is inferred as Integer
        
        String[] words = {"hello", "world"};
        printArray(words);    // T is inferred as String
        
        List<String> names = Arrays.asList("Alex", "Maria");
        String first = getFirst(names);  // Returns "Alex"
    }
}
```

## Bounded Type Parameters

Sometimes you want to restrict what types can be used:

```java
// Upper bound: T must be Number or its subclass
public class Calculator<T extends Number> {
    
    private T value;
    
    public Calculator(T value) {
        this.value = value;
    }
    
    // We can call Number methods because T is guaranteed to be a Number
    public double doubleValue() {
        return value.doubleValue();
    }
    
    public double add(T other) {
        return value.doubleValue() + other.doubleValue();
    }
}

// Usage
public class BoundedDemo {
    public static void main(String[] args) {
        Calculator<Integer> intCalc = new Calculator<>(10);
        Calculator<Double> doubleCalc = new Calculator<>(3.14);
        
        // Calculator<String> stringCalc = new Calculator<>("hello");
        // COMPILE ERROR! String doesn't extend Number
        
        System.out.println(intCalc.doubleValue());  // 10.0
        System.out.println(doubleCalc.add(2.0));    // 5.14
    }
}
```

## Multiple Bounds

```java
// T must extend Number AND implement Comparable
public class SortableCalculator<T extends Number & Comparable<T>> {
    
    private List<T> values = new ArrayList<>();
    
    public void add(T value) {
        values.add(value);
    }
    
    public T getMax() {
        if (values.isEmpty()) return null;
        
        T max = values.get(0);
        for (T value : values) {
            if (value.compareTo(max) > 0) {
                max = value;
            }
        }
        return max;
    }
    
    public double sum() {
        double total = 0;
        for (T value : values) {
            total += value.doubleValue();
        }
        return total;
    }
}
```

## Wildcards

Wildcards (`?`) provide flexibility when you don't know or don't care about the exact type:

### Unbounded Wildcard `<?>`

```java
public class WildcardDemo {
    
    // Accepts any List, regardless of type
    public static void printList(List<?> list) {
        for (Object item : list) {
            System.out.println(item);
        }
    }
    
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "b");
        List<Integer> numbers = Arrays.asList(1, 2);
        
        printList(strings);  // Works
        printList(numbers);  // Works
    }
}
```

### Upper-Bounded Wildcard `<? extends Type>`

"Accept Type or any subclass" - useful for **reading** from a collection:

```java
public class UpperBoundDemo {
    
    // Accepts List of Number or any subclass (Integer, Double, etc.)
    public static double sumNumbers(List<? extends Number> numbers) {
        double sum = 0;
        for (Number num : numbers) {
            sum += num.doubleValue();
        }
        return sum;
    }
    
    public static void main(String[] args) {
        List<Integer> integers = Arrays.asList(1, 2, 3);
        List<Double> doubles = Arrays.asList(1.5, 2.5, 3.5);
        List<Number> numbers = Arrays.asList(1, 2.5, 3);
        
        System.out.println(sumNumbers(integers)); // 6.0
        System.out.println(sumNumbers(doubles));  // 7.5
        System.out.println(sumNumbers(numbers));  // 6.5
    }
}
```

### Lower-Bounded Wildcard `<? super Type>`

"Accept Type or any superclass" - useful for **writing** to a collection:

```java
public class LowerBoundDemo {
    
    // Can add Integers to any list that accepts Integer or its superclass
    public static void addNumbers(List<? super Integer> list) {
        list.add(1);
        list.add(2);
        list.add(3);
    }
    
    public static void main(String[] args) {
        List<Integer> integers = new ArrayList<>();
        List<Number> numbers = new ArrayList<>();
        List<Object> objects = new ArrayList<>();
        
        addNumbers(integers);  // Works
        addNumbers(numbers);   // Works
        addNumbers(objects);   // Works
        
        // List<Double> doubles = new ArrayList<>();
        // addNumbers(doubles);  // COMPILE ERROR!
    }
}
```

### PECS Principle

**P**roducer **E**xtends, **C**onsumer **S**uper

```java
public class PECSDemo {
    
    // Producer (we READ from it) - use extends
    public static <T> void copyTo(
            List<? extends T> source,      // Producer - we read from this
            List<? super T> destination) { // Consumer - we write to this
        
        for (T item : source) {
            destination.add(item);
        }
    }
    
    public static void main(String[] args) {
        List<Integer> source = Arrays.asList(1, 2, 3);
        List<Number> destination = new ArrayList<>();
        
        copyTo(source, destination);  // Copy Integers to Number list
        System.out.println(destination);  // [1, 2, 3]
    }
}
```

## Type Erasure

**Important concept:** Generics in Java are a compile-time feature. At runtime, type information is "erased":

```java
public class TypeErasureDemo {
    
    public static void main(String[] args) {
        List<String> strings = new ArrayList<>();
        List<Integer> integers = new ArrayList<>();
        
        // At runtime, both are just ArrayList!
        System.out.println(strings.getClass() == integers.getClass());  // true!
        
        // This is why you can't do this:
        // if (obj instanceof List<String>) { }  // Compile error
        
        // Or this:
        // T[] array = new T[10];  // Can't create generic array
    }
}
```

## Practical Generic Examples

```java
// Generic Repository pattern (like your Python repositories!)
public interface Repository<T, ID> {
    T findById(ID id);
    List<T> findAll();
    T save(T entity);
    void delete(T entity);
    boolean exists(ID id);
}

// Implementation for User
public class UserRepository implements Repository<User, Long> {
    
    private Map<Long, User> storage = new HashMap<>();
    
    @Override
    public User findById(Long id) {
        return storage.get(id);
    }
    
    @Override
    public List<User> findAll() {
        return new ArrayList<>(storage.values());
    }
    
    @Override
    public User save(User user) {
        storage.put(user.getId(), user);
        return user;
    }
    
    @Override
    public void delete(User user) {
        storage.remove(user.getId());
    }
    
    @Override
    public boolean exists(Long id) {
        return storage.containsKey(id);
    }
}

// Generic Response wrapper (like FastAPI responses!)
public class ApiResponse<T> {
    
    private boolean success;
    private T data;
    private String message;
    private List<String> errors;
    
    public static <T> ApiResponse<T> success(T data) {
        ApiResponse<T> response = new ApiResponse<>();
        response.success = true;
        response.data = data;
        return response;
    }
    
    public static <T> ApiResponse<T> error(String message, List<String> errors) {
        ApiResponse<T> response = new ApiResponse<>();
        response.success = false;
        response.message = message;
        response.errors = errors;
        return response;
    }
    
    // Getters...
}

// Usage
ApiResponse<User> userResponse = ApiResponse.success(new User("Alex"));
ApiResponse<List<Product>> productsResponse = ApiResponse.success(products);
```

---

# 3. Collections Framework

## Overview

The Java Collections Framework is a unified architecture for representing and manipulating collections. Think of it as Java's equivalent to Python's `list`, `dict`, `set`, but with more structure and type safety.

```
Collection (interface)
├── List (interface) - ordered, allows duplicates
│   ├── ArrayList - dynamic array (like Python list)
│   ├── LinkedList - doubly-linked list
│   └── Vector - synchronized (legacy, avoid)
│
├── Set (interface) - no duplicates
│   ├── HashSet - unordered, fastest
│   ├── LinkedHashSet - insertion order preserved
│   └── TreeSet - sorted order
│
└── Queue (interface) - FIFO
    ├── LinkedList - also implements Queue
    ├── PriorityQueue - priority-based ordering
    └── ArrayDeque - double-ended queue

Map (interface) - key-value pairs (NOT a Collection!)
├── HashMap - unordered, fastest (like Python dict)
├── LinkedHashMap - insertion order preserved
├── TreeMap - sorted by keys
└── Hashtable - synchronized (legacy, avoid)
```

## The Collection Interface

```java
public interface Collection<E> extends Iterable<E> {
    int size();
    boolean isEmpty();
    boolean contains(Object o);
    boolean add(E e);
    boolean remove(Object o);
    void clear();
    Iterator<E> iterator();
    Object[] toArray();
    // ... and more
}
```

## List Interface and Implementations

### ArrayList — Your Go-To List

```java
import java.util.*;

public class ArrayListDemo {
    
    public static void main(String[] args) {
        // Creating lists
        List<String> list1 = new ArrayList<>();  // Empty
        List<String> list2 = new ArrayList<>(100);  // Initial capacity
        List<String> list3 = new ArrayList<>(Arrays.asList("a", "b", "c"));
        List<String> list4 = List.of("x", "y", "z");  // Immutable! (Java 9+)
        
        // Adding elements
        List<String> names = new ArrayList<>();
        names.add("Alex");           // Add to end
        names.add(0, "Maria");       // Add at index
        names.addAll(Arrays.asList("Bob", "Carol"));  // Add multiple
        
        // Accessing elements
        String first = names.get(0);           // "Maria"
        int index = names.indexOf("Alex");     // 1
        int lastIndex = names.lastIndexOf("Alex");
        
        // Modifying
        names.set(0, "Marie");  // Replace at index
        
        // Removing
        names.remove("Bob");      // Remove by object
        names.remove(0);          // Remove by index
        names.removeIf(n -> n.startsWith("C"));  // Remove with predicate
        
        // Checking
        boolean hasAlex = names.contains("Alex");
        boolean isEmpty = names.isEmpty();
        int size = names.size();
        
        // Iterating (multiple ways)
        // 1. Enhanced for loop
        for (String name : names) {
            System.out.println(name);
        }
        
        // 2. Index-based (when you need the index)
        for (int i = 0; i < names.size(); i++) {
            System.out.println(i + ": " + names.get(i));
        }
        
        // 3. forEach with lambda
        names.forEach(name -> System.out.println(name));
        
        // 4. Iterator (for safe removal during iteration)
        Iterator<String> iter = names.iterator();
        while (iter.hasNext()) {
            String name = iter.next();
            if (name.startsWith("A")) {
                iter.remove();  // Safe removal
            }
        }
        
        // Sorting
        Collections.sort(names);  // Natural order
        Collections.sort(names, Collections.reverseOrder());
        names.sort(Comparator.comparing(String::length));  // By length
        
        // Converting
        String[] array = names.toArray(new String[0]);
        List<String> fromArray = Arrays.asList(array);  // Fixed-size!
        List<String> mutableFromArray = new ArrayList<>(Arrays.asList(array));
    }
}
```

### LinkedList — When You Need Fast Insert/Remove

```java
public class LinkedListDemo {
    
    public static void main(String[] args) {
        // LinkedList implements both List AND Deque
        LinkedList<String> list = new LinkedList<>();
        
        // List operations (same as ArrayList)
        list.add("middle");
        
        // Deque operations (double-ended queue)
        list.addFirst("start");   // Add to beginning
        list.addLast("end");      // Add to end
        
        String first = list.getFirst();  // Peek at first
        String last = list.getLast();    // Peek at last
        
        String removed1 = list.removeFirst();  // Remove and return first
        String removed2 = list.removeLast();   // Remove and return last
        
        // Stack operations (LIFO)
        list.push("new");   // Add to front
        String popped = list.pop();  // Remove from front
        
        // Queue operations (FIFO)
        list.offer("new");  // Add to end
        String polled = list.poll();  // Remove from front
    }
}
```

### When to Use Which?

| Operation | ArrayList | LinkedList |
|-----------|-----------|------------|
| Access by index | O(1) ✓ | O(n) |
| Add/remove at end | O(1)* | O(1) |
| Add/remove at beginning | O(n) | O(1) ✓ |
| Add/remove in middle | O(n) | O(1)** |
| Memory overhead | Low | Higher |

*Amortized, due to resizing
**After you have a reference to the node

**Rule of thumb:** Use `ArrayList` unless you need frequent insertions/deletions at the beginning.

## Set Interface and Implementations

Sets store **unique elements only** (no duplicates).

### HashSet — Fastest, Unordered

```java
public class HashSetDemo {
    
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();
        
        // Adding elements
        set.add("Apple");
        set.add("Banana");
        set.add("Apple");  // Duplicate - ignored!
        
        System.out.println(set.size());  // 2, not 3
        
        // Checking membership (O(1) average)
        boolean hasApple = set.contains("Apple");  // true
        
        // Removing
        set.remove("Apple");
        
        // Iterating (order is unpredictable!)
        for (String item : set) {
            System.out.println(item);
        }
        
        // Set operations
        Set<Integer> set1 = new HashSet<>(Arrays.asList(1, 2, 3, 4));
        Set<Integer> set2 = new HashSet<>(Arrays.asList(3, 4, 5, 6));
        
        // Union
        Set<Integer> union = new HashSet<>(set1);
        union.addAll(set2);  // {1, 2, 3, 4, 5, 6}
        
        // Intersection
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);  // {3, 4}
        
        // Difference
        Set<Integer> difference = new HashSet<>(set1);
        difference.removeAll(set2);  // {1, 2}
    }
}
```

### LinkedHashSet — Maintains Insertion Order

```java
public class LinkedHashSetDemo {
    
    public static void main(String[] args) {
        Set<String> set = new LinkedHashSet<>();
        
        set.add("First");
        set.add("Second");
        set.add("Third");
        
        // Iteration order = insertion order
        for (String item : set) {
            System.out.println(item);  // First, Second, Third
        }
    }
}
```

### TreeSet — Sorted Order

```java
public class TreeSetDemo {
    
    public static void main(String[] args) {
        // Natural ordering (alphabetical for strings)
        Set<String> set = new TreeSet<>();
        set.add("Banana");
        set.add("Apple");
        set.add("Cherry");
        
        for (String item : set) {
            System.out.println(item);  // Apple, Banana, Cherry
        }
        
        // Custom ordering
        Set<String> byLength = new TreeSet<>(
            Comparator.comparing(String::length)
                      .thenComparing(Comparator.naturalOrder())
        );
        byLength.addAll(Arrays.asList("bb", "aaa", "c"));
        // Order: c, bb, aaa (by length, then alphabetically)
        
        // TreeSet extra methods
        TreeSet<Integer> numbers = new TreeSet<>(Arrays.asList(1, 3, 5, 7, 9));
        
        System.out.println(numbers.first());      // 1
        System.out.println(numbers.last());       // 9
        System.out.println(numbers.lower(5));     // 3 (strictly less than)
        System.out.println(numbers.higher(5));    // 7 (strictly greater than)
        System.out.println(numbers.floor(6));     // 5 (less than or equal)
        System.out.println(numbers.ceiling(6));   // 7 (greater than or equal)
        
        // Subsets
        SortedSet<Integer> subset = numbers.subSet(3, 7);  // [3, 5]
        SortedSet<Integer> head = numbers.headSet(5);      // [1, 3]
        SortedSet<Integer> tail = numbers.tailSet(5);      // [5, 7, 9]
    }
}
```

## Map Interface and Implementations

Maps store **key-value pairs**. Keys must be unique.

### HashMap — Your Go-To Map

```java
public class HashMapDemo {
    
    public static void main(String[] args) {
        // Creating maps
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> map2 = Map.of("a", 1, "b", 2);  // Immutable
        Map<String, Integer> map3 = new HashMap<>(Map.of("a", 1, "b", 2));
        
        // Adding/updating entries
        map.put("Alex", 100);
        map.put("Maria", 95);
        map.put("Alex", 105);  // Updates existing key
        
        // Safe adding (only if key doesn't exist)
        map.putIfAbsent("Bob", 80);
        
        // Getting values
        Integer score = map.get("Alex");        // 105
        Integer missing = map.get("Unknown");   // null
        Integer safe = map.getOrDefault("Unknown", 0);  // 0
        
        // Checking
        boolean hasKey = map.containsKey("Alex");
        boolean hasValue = map.containsValue(100);
        
        // Removing
        map.remove("Bob");
        map.remove("Alex", 100);  // Only removes if value matches
        
        // Iterating
        // 1. Over entries (most common)
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        // 2. Over keys
        for (String key : map.keySet()) {
            System.out.println(key);
        }
        
        // 3. Over values
        for (Integer value : map.values()) {
            System.out.println(value);
        }
        
        // 4. forEach with lambda
        map.forEach((key, value) -> {
            System.out.println(key + " -> " + value);
        });
        
        // Compute methods (powerful!)
        // Update value based on current value
        map.compute("Alex", (key, val) -> val == null ? 1 : val + 1);
        
        // Only if key is absent
        map.computeIfAbsent("New", key -> key.length());
        
        // Only if key is present
        map.computeIfPresent("Alex", (key, val) -> val * 2);
        
        // Merge - combine existing with new
        map.merge("Alex", 10, Integer::sum);  // Add 10 to existing
    }
}
```

### LinkedHashMap — Maintains Insertion Order

```java
public class LinkedHashMapDemo {
    
    public static void main(String[] args) {
        Map<String, Integer> map = new LinkedHashMap<>();
        
        map.put("First", 1);
        map.put("Second", 2);
        map.put("Third", 3);
        
        // Iteration preserves insertion order
        map.forEach((k, v) -> System.out.println(k));
        // Output: First, Second, Third
        
        // Access-order mode (for LRU cache)
        Map<String, Integer> accessOrder = new LinkedHashMap<>(16, 0.75f, true);
        accessOrder.put("A", 1);
        accessOrder.put("B", 2);
        accessOrder.put("C", 3);
        
        accessOrder.get("A");  // Access A
        
        accessOrder.forEach((k, v) -> System.out.println(k));
        // Output: B, C, A (A moved to end because it was accessed)
    }
}
```

### TreeMap — Sorted by Keys

```java
public class TreeMapDemo {
    
    public static void main(String[] args) {
        // Natural ordering
        Map<String, Integer> map = new TreeMap<>();
        map.put("Banana", 2);
        map.put("Apple", 1);
        map.put("Cherry", 3);
        
        map.forEach((k, v) -> System.out.println(k));
        // Output: Apple, Banana, Cherry (alphabetically sorted)
        
        // Custom ordering
        Map<String, Integer> byLength = new TreeMap<>(
            Comparator.comparing(String::length).reversed()
        );
        
        // TreeMap extra methods
        TreeMap<Integer, String> scores = new TreeMap<>();
        scores.put(90, "A");
        scores.put(80, "B");
        scores.put(70, "C");
        
        System.out.println(scores.firstKey());     // 70
        System.out.println(scores.lastKey());      // 90
        System.out.println(scores.lowerKey(80));   // 70
        System.out.println(scores.higherKey(80));  // 90
        
        // Range operations
        SortedMap<Integer, String> above75 = scores.tailMap(75);
    }
}
```

## Queue and Deque

### Queue — FIFO (First In, First Out)

```java
public class QueueDemo {
    
    public static void main(String[] args) {
        // LinkedList as Queue
        Queue<String> queue = new LinkedList<>();
        
        // Adding (to back of queue)
        queue.offer("First");   // Returns false if full
        queue.add("Second");    // Throws exception if full
        
        // Peek (look without removing)
        String front = queue.peek();  // null if empty
        String frontOrThrow = queue.element();  // Throws if empty
        
        // Remove (from front)
        String removed = queue.poll();  // null if empty
        String removedOrThrow = queue.remove();  // Throws if empty
        
        // PriorityQueue - elements ordered by priority
        Queue<Integer> pq = new PriorityQueue<>();  // Min-heap by default
        pq.offer(3);
        pq.offer(1);
        pq.offer(2);
        
        while (!pq.isEmpty()) {
            System.out.println(pq.poll());  // 1, 2, 3 (smallest first)
        }
        
        // Max-heap
        Queue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
    }
}
```

### Deque — Double-Ended Queue

```java
public class DequeDemo {
    
    public static void main(String[] args) {
        Deque<String> deque = new ArrayDeque<>();
        
        // Add to front or back
        deque.addFirst("A");
        deque.addLast("B");
        deque.offerFirst("0");
        deque.offerLast("C");
        
        // Remove from front or back
        String first = deque.pollFirst();
        String last = deque.pollLast();
        
        // Peek at front or back
        String peekFirst = deque.peekFirst();
        String peekLast = deque.peekLast();
        
        // Use as Stack (LIFO)
        deque.push("X");  // Add to front
        String popped = deque.pop();  // Remove from front
    }
}
```

## Collections Utility Class

```java
public class CollectionsUtilityDemo {
    
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5, 9));
        
        // Sorting
        Collections.sort(numbers);  // [1, 1, 3, 4, 5, 9]
        Collections.sort(numbers, Collections.reverseOrder());
        
        // Searching (list must be sorted!)
        Collections.sort(numbers);
        int index = Collections.binarySearch(numbers, 4);
        
        // Min/Max
        int min = Collections.min(numbers);
        int max = Collections.max(numbers);
        
        // Shuffling
        Collections.shuffle(numbers);
        
        // Reversing
        Collections.reverse(numbers);
        
        // Filling
        Collections.fill(numbers, 0);  // All elements become 0
        
        // Copying
        List<Integer> dest = new ArrayList<>(Collections.nCopies(numbers.size(), 0));
        Collections.copy(dest, numbers);
        
        // Replacing
        Collections.replaceAll(numbers, 0, 100);
        
        // Frequency
        int count = Collections.frequency(numbers, 1);
        
        // Immutable wrappers
        List<Integer> unmodifiable = Collections.unmodifiableList(numbers);
        // unmodifiable.add(10);  // Throws UnsupportedOperationException
        
        // Synchronized wrappers (for thread safety)
        List<Integer> syncList = Collections.synchronizedList(numbers);
        
        // Empty collections
        List<String> emptyList = Collections.emptyList();
        Set<String> emptySet = Collections.emptySet();
        Map<String, Integer> emptyMap = Collections.emptyMap();
        
        // Singleton collections
        List<String> singletonList = Collections.singletonList("only");
        Set<String> singletonSet = Collections.singleton("only");
    }
}
```

## Comparable vs Comparator

```java
// Comparable - natural ordering (built into the class)
public class Person implements Comparable<Person> {
    private String name;
    private int age;
    
    @Override
    public int compareTo(Person other) {
        // Natural ordering by name
        return this.name.compareTo(other.name);
    }
}

// Comparator - external ordering (can have multiple)
public class PersonComparators {
    
    // By age
    public static Comparator<Person> byAge() {
        return Comparator.comparingInt(Person::getAge);
    }
    
    // By name length
    public static Comparator<Person> byNameLength() {
        return Comparator.comparingInt(p -> p.getName().length());
    }
    
    // Complex: by age descending, then name ascending
    public static Comparator<Person> byAgeDescThenName() {
        return Comparator.comparingInt(Person::getAge).reversed()
                         .thenComparing(Person::getName);
    }
}

// Usage
List<Person> people = ...;
Collections.sort(people);  // Uses Comparable (natural order)
Collections.sort(people, PersonComparators.byAge());  // Uses Comparator
people.sort(PersonComparators.byAgeDescThenName());
```

---

# 4. Lambda Expressions & Functional Interfaces

## What Are Lambda Expressions?

Lambdas are **anonymous functions** — they're Java's way of treating functions as values. Very similar to Python's lambda, but more powerful.

```python
# Python lambda
square = lambda x: x ** 2
```

```java
// Java lambda
Function<Integer, Integer> square = x -> x * x;
```

## Lambda Syntax

```java
public class LambdaSyntax {
    
    public static void main(String[] args) {
        // Full syntax
        Comparator<String> c1 = (String a, String b) -> {
            return a.compareTo(b);
        };
        
        // Type inference (types can be omitted)
        Comparator<String> c2 = (a, b) -> {
            return a.compareTo(b);
        };
        
        // Single expression (no braces, implicit return)
        Comparator<String> c3 = (a, b) -> a.compareTo(b);
        
        // Single parameter (no parentheses needed)
        Consumer<String> printer = s -> System.out.println(s);
        
        // No parameters
        Runnable r = () -> System.out.println("Hello!");
        
        // Multiple statements (need braces and explicit return)
        Function<String, Integer> parser = s -> {
            System.out.println("Parsing: " + s);
            return Integer.parseInt(s);
        };
    }
}
```

## Functional Interfaces

A **functional interface** is an interface with exactly ONE abstract method. Lambdas can be used wherever a functional interface is expected.

```java
// This is a functional interface
@FunctionalInterface
public interface Greeting {
    String greet(String name);
}

// Usage with lambda
Greeting hello = name -> "Hello, " + name + "!";
System.out.println(hello.greet("Alex"));  // "Hello, Alex!"
```

## Built-in Functional Interfaces

Java provides many functional interfaces in `java.util.function`:

### Function<T, R> — Takes T, returns R

```java
import java.util.function.Function;

public class FunctionDemo {
    
    public static void main(String[] args) {
        // String -> Integer
        Function<String, Integer> length = s -> s.length();
        System.out.println(length.apply("Hello"));  // 5
        
        // Chaining functions
        Function<Integer, Integer> doubleIt = x -> x * 2;
        Function<Integer, String> toString = x -> "Value: " + x;
        
        // Compose: first length, then doubleIt, then toString
        Function<String, String> combined = length
            .andThen(doubleIt)
            .andThen(toString);
        
        System.out.println(combined.apply("Hello"));  // "Value: 10"
        
        // BiFunction<T, U, R> - takes two arguments
        BiFunction<String, String, String> concat = (a, b) -> a + b;
        System.out.println(concat.apply("Hello, ", "World!"));
    }
}
```

### Predicate<T> — Takes T, returns boolean

```java
import java.util.function.Predicate;

public class PredicateDemo {
    
    public static void main(String[] args) {
        Predicate<String> isEmpty = s -> s.isEmpty();
        Predicate<String> isLong = s -> s.length() > 10;
        
        System.out.println(isEmpty.test(""));      // true
        System.out.println(isLong.test("Hello"));  // false
        
        // Combining predicates
        Predicate<String> notEmpty = isEmpty.negate();
        Predicate<String> notEmptyAndLong = notEmpty.and(isLong);
        Predicate<String> emptyOrLong = isEmpty.or(isLong);
        
        // Filtering a list
        List<String> words = Arrays.asList("", "hi", "hello world!");
        words.stream()
             .filter(notEmpty.and(isLong))
             .forEach(System.out::println);  // "hello world!"
        
        // BiPredicate
        BiPredicate<String, Integer> hasMinLength = (s, len) -> s.length() >= len;
        System.out.println(hasMinLength.test("Hello", 3));  // true
    }
}
```

### Consumer<T> — Takes T, returns nothing

```java
import java.util.function.Consumer;

public class ConsumerDemo {
    
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello!");  // Prints: Hello!
        
        // Chaining consumers
        Consumer<String> logger = s -> System.out.println("[LOG] " + s);
        Consumer<String> both = printer.andThen(logger);
        
        both.accept("Test");
        // Prints:
        // Test
        // [LOG] Test
        
        // BiConsumer
        BiConsumer<String, Integer> printWithCount = (s, n) -> {
            for (int i = 0; i < n; i++) {
                System.out.println(s);
            }
        };
        printWithCount.accept("Hello", 3);
    }
}
```

### Supplier<T> — Takes nothing, returns T

```java
import java.util.function.Supplier;

public class SupplierDemo {
    
    public static void main(String[] args) {
        Supplier<Double> random = () -> Math.random();
        System.out.println(random.get());
        System.out.println(random.get());
        
        // Lazy initialization
        Supplier<ExpensiveObject> lazyObject = () -> new ExpensiveObject();
        
        // Object is only created when we call get()
        if (needObject) {
            ExpensiveObject obj = lazyObject.get();
        }
        
        // Useful for default values
        public static <T> T getOrDefault(T value, Supplier<T> defaultSupplier) {
            return value != null ? value : defaultSupplier.get();
        }
    }
}
```

### UnaryOperator<T> and BinaryOperator<T>

```java
import java.util.function.UnaryOperator;
import java.util.function.BinaryOperator;

public class OperatorDemo {
    
    public static void main(String[] args) {
        // UnaryOperator<T> is Function<T, T> (same input/output type)
        UnaryOperator<Integer> square = x -> x * x;
        System.out.println(square.apply(5));  // 25
        
        // BinaryOperator<T> is BiFunction<T, T, T>
        BinaryOperator<Integer> sum = (a, b) -> a + b;
        System.out.println(sum.apply(3, 4));  // 7
        
        // Useful in reduce operations
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        int total = numbers.stream()
                           .reduce(0, sum);  // 15
    }
}
```

### Primitive Specializations

To avoid boxing/unboxing overhead:

```java
import java.util.function.*;

public class PrimitiveDemo {
    
    public static void main(String[] args) {
        // Instead of Function<Integer, Integer>
        IntUnaryOperator square = x -> x * x;
        System.out.println(square.applyAsInt(5));
        
        // Instead of Predicate<Integer>
        IntPredicate isEven = x -> x % 2 == 0;
        System.out.println(isEven.test(4));
        
        // Instead of Consumer<Double>
        DoubleConsumer printer = d -> System.out.println(d);
        
        // Instead of Supplier<Long>
        LongSupplier timer = () -> System.currentTimeMillis();
        
        // Conversion functions
        IntFunction<String> intToString = i -> String.valueOf(i);
        ToIntFunction<String> stringToInt = s -> Integer.parseInt(s);
    }
}
```

## Method References

Method references are a shorthand for lambdas that just call an existing method:

```java
public class MethodReferenceDemo {
    
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alex", "Maria", "Bob");
        
        // Lambda
        names.forEach(name -> System.out.println(name));
        
        // Method reference (equivalent)
        names.forEach(System.out::println);
        
        // Four types of method references:
        
        // 1. Static method reference: ClassName::staticMethod
        Function<String, Integer> parser = Integer::parseInt;
        // Equivalent to: s -> Integer.parseInt(s)
        
        // 2. Instance method on a specific object: object::instanceMethod
        String prefix = "Hello, ";
        Function<String, String> greeter = prefix::concat;
        // Equivalent to: s -> prefix.concat(s)
        
        // 3. Instance method on an arbitrary object: ClassName::instanceMethod
        Function<String, String> upper = String::toUpperCase;
        // Equivalent to: s -> s.toUpperCase()
        
        // 4. Constructor reference: ClassName::new
        Supplier<List<String>> listFactory = ArrayList::new;
        // Equivalent to: () -> new ArrayList<>()
        
        Function<Integer, List<String>> sizedListFactory = ArrayList::new;
        // Equivalent to: size -> new ArrayList<>(size)
    }
}
```

## Practical Examples

```java
public class LambdaPractical {
    
    public static void main(String[] args) {
        // Sorting with lambda
        List<String> names = Arrays.asList("Bob", "Alice", "Charlie");
        names.sort((a, b) -> a.compareTo(b));
        names.sort(Comparator.naturalOrder());  // Even simpler
        
        // Custom comparator
        List<Person> people = getPeople();
        people.sort(Comparator
            .comparing(Person::getLastName)
            .thenComparing(Person::getFirstName)
            .reversed());
        
        // Event handling (GUI)
        button.setOnAction(event -> handleClick(event));
        button.setOnAction(this::handleClick);
        
        // Filtering collections
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        numbers.removeIf(n -> n % 2 == 0);  // Remove evens
        
        // Map operations
        Map<String, Integer> scores = new HashMap<>();
        scores.computeIfAbsent("Alex", k -> 0);
        scores.merge("Alex", 10, Integer::sum);
        
        // Optional
        Optional<String> name = getName();
        String result = name
            .filter(n -> n.length() > 3)
            .map(String::toUpperCase)
            .orElse("Unknown");
    }
}
```

## Creating Your Own Functional Interfaces

```java
@FunctionalInterface
public interface TriFunction<T, U, V, R> {
    R apply(T t, U u, V v);
}

// Usage
TriFunction<Integer, Integer, Integer, Integer> sumThree = (a, b, c) -> a + b + c;
System.out.println(sumThree.apply(1, 2, 3));  // 6

// With default methods
@FunctionalInterface
public interface Transformer<T> {
    T transform(T input);
    
    // Default method (doesn't count as abstract)
    default Transformer<T> andThen(Transformer<T> after) {
        return input -> after.transform(this.transform(input));
    }
    
    // Static factory method
    static <T> Transformer<T> identity() {
        return input -> input;
    }
}
```

---

# 5. Streams API

## What Are Streams?

Streams provide a **declarative way to process collections**. Think of them like Python's list comprehensions and `map`/`filter`/`reduce`, but more powerful.

```python
# Python
numbers = [1, 2, 3, 4, 5]
result = [x * 2 for x in numbers if x % 2 == 0]
# or
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
```

```java
// Java Streams
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> result = numbers.stream()
    .filter(x -> x % 2 == 0)
    .map(x -> x * 2)
    .collect(Collectors.toList());
```

## Key Characteristics

1. **Not a data structure** — Streams don't store data; they carry values from a source
2. **Lazy evaluation** — Operations aren't performed until a terminal operation is called
3. **Possibly unbounded** — Can be infinite (with short-circuit operations)
4. **Consumable** — Can only be traversed once

## Creating Streams

```java
public class CreatingStreams {
    
    public static void main(String[] args) {
        // From collections
        List<String> list = Arrays.asList("a", "b", "c");
        Stream<String> stream1 = list.stream();
        Stream<String> parallelStream = list.parallelStream();
        
        // From arrays
        String[] array = {"a", "b", "c"};
        Stream<String> stream2 = Arrays.stream(array);
        
        // Using Stream.of()
        Stream<String> stream3 = Stream.of("a", "b", "c");
        
        // Using Stream.builder()
        Stream<String> stream4 = Stream.<String>builder()
            .add("a")
            .add("b")
            .add("c")
            .build();
        
        // Empty stream
        Stream<String> empty = Stream.empty();
        
        // Infinite streams
        Stream<Double> randoms = Stream.generate(Math::random);
        Stream<Integer> evenNumbers = Stream.iterate(0, n -> n + 2);
        
        // With limit (Java 9+)
        Stream<Integer> limited = Stream.iterate(0, n -> n < 100, n -> n + 2);
        
        // Primitive streams (avoid boxing)
        IntStream ints = IntStream.range(0, 10);       // 0 to 9
        IntStream ints2 = IntStream.rangeClosed(1, 10); // 1 to 10
        LongStream longs = LongStream.of(1L, 2L, 3L);
        DoubleStream doubles = DoubleStream.of(1.0, 2.0, 3.0);
        
        // From other sources
        Stream<String> lines = Files.lines(Path.of("file.txt"));  // File lines
        Stream<String> tokens = Pattern.compile(",").splitAsStream("a,b,c");
    }
}
```

## Stream Operations

### Intermediate Operations (Lazy, Return Stream)

```java
public class IntermediateOperations {
    
    public static void main(String[] args) {
        List<String> words = Arrays.asList("hello", "world", "java", "streams");
        
        // filter() - keep elements matching predicate
        words.stream()
            .filter(w -> w.length() > 4)
            .forEach(System.out::println);  // hello, world, streams
        
        // map() - transform elements
        words.stream()
            .map(String::toUpperCase)
            .forEach(System.out::println);  // HELLO, WORLD, JAVA, STREAMS
        
        // flatMap() - flatten nested structures
        List<List<Integer>> nested = Arrays.asList(
            Arrays.asList(1, 2),
            Arrays.asList(3, 4),
            Arrays.asList(5, 6)
        );
        nested.stream()
            .flatMap(List::stream)  // Flatten to single stream
            .forEach(System.out::println);  // 1, 2, 3, 4, 5, 6
        
        // distinct() - remove duplicates
        Stream.of(1, 2, 2, 3, 3, 3)
            .distinct()
            .forEach(System.out::println);  // 1, 2, 3
        
        // sorted() - sort elements
        words.stream()
            .sorted()
            .forEach(System.out::println);  // hello, java, streams, world
        
        words.stream()
            .sorted(Comparator.comparing(String::length).reversed())
            .forEach(System.out::println);  // streams, hello, world, java
        
        // peek() - perform action without modifying (for debugging)
        words.stream()
            .peek(w -> System.out.println("Processing: " + w))
            .map(String::toUpperCase)
            .forEach(System.out::println);
        
        // limit() - take first n elements
        Stream.iterate(1, n -> n + 1)
            .limit(5)
            .forEach(System.out::println);  // 1, 2, 3, 4, 5
        
        // skip() - skip first n elements
        words.stream()
            .skip(2)
            .forEach(System.out::println);  // java, streams
        
        // takeWhile() and dropWhile() (Java 9+)
        Stream.of(2, 4, 6, 7, 8, 10)
            .takeWhile(n -> n % 2 == 0)
            .forEach(System.out::println);  // 2, 4, 6
        
        Stream.of(2, 4, 6, 7, 8, 10)
            .dropWhile(n -> n % 2 == 0)
            .forEach(System.out::println);  // 7, 8, 10
    }
}
```

### Terminal Operations (Trigger Processing, Return Result)

```java
public class TerminalOperations {
    
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        
        // forEach() - perform action on each element
        numbers.stream().forEach(System.out::println);
        numbers.forEach(System.out::println);  // Shortcut for lists
        
        // collect() - gather results into a collection
        List<Integer> doubled = numbers.stream()
            .map(n -> n * 2)
            .collect(Collectors.toList());
        
        Set<Integer> uniqueDoubled = numbers.stream()
            .map(n -> n * 2)
            .collect(Collectors.toSet());
        
        // toArray() - convert to array
        Integer[] array = numbers.stream()
            .map(n -> n * 2)
            .toArray(Integer[]::new);
        
        // count() - count elements
        long count = numbers.stream()
            .filter(n -> n > 2)
            .count();  // 3
        
        // min() and max() - find minimum/maximum
        Optional<Integer> min = numbers.stream().min(Integer::compareTo);
        Optional<Integer> max = numbers.stream().max(Integer::compareTo);
        
        // findFirst() and findAny() - find an element
        Optional<Integer> first = numbers.stream()
            .filter(n -> n > 2)
            .findFirst();  // 3
        
        Optional<Integer> any = numbers.parallelStream()
            .filter(n -> n > 2)
            .findAny();  // Could be 3, 4, or 5
        
        // anyMatch(), allMatch(), noneMatch() - test conditions
        boolean anyEven = numbers.stream().anyMatch(n -> n % 2 == 0);     // true
        boolean allPositive = numbers.stream().allMatch(n -> n > 0);      // true
        boolean noneNegative = numbers.stream().noneMatch(n -> n < 0);    // true
        
        // reduce() - combine elements into single result
        int sum = numbers.stream()
            .reduce(0, Integer::sum);  // 15
        
        Optional<Integer> product = numbers.stream()
            .reduce((a, b) -> a * b);  // 120
        
        // More complex reduce
        String joined = numbers.stream()
            .map(String::valueOf)
            .reduce("", (a, b) -> a + (a.isEmpty() ? "" : ", ") + b);
        // "1, 2, 3, 4, 5"
    }
}
```

## Collectors

```java
import java.util.stream.Collectors;

public class CollectorsDemo {
    
    public static void main(String[] args) {
        List<Person> people = Arrays.asList(
            new Person("Alex", 30, "Engineering"),
            new Person("Maria", 25, "Marketing"),
            new Person("Bob", 35, "Engineering"),
            new Person("Carol", 28, "Marketing")
        );
        
        // toList(), toSet(), toCollection()
        List<String> names = people.stream()
            .map(Person::getName)
            .collect(Collectors.toList());
        
        Set<String> departments = people.stream()
            .map(Person::getDepartment)
            .collect(Collectors.toSet());
        
        TreeSet<String> sortedNames = people.stream()
            .map(Person::getName)
            .collect(Collectors.toCollection(TreeSet::new));
        
        // toMap()
        Map<String, Integer> nameToAge = people.stream()
            .collect(Collectors.toMap(
                Person::getName,      // Key mapper
                Person::getAge        // Value mapper
            ));
        
        // toMap with merge function (for duplicate keys)
        Map<String, Integer> deptToCount = people.stream()
            .collect(Collectors.toMap(
                Person::getDepartment,
                p -> 1,
                Integer::sum  // Merge function
            ));
        
        // joining() - concatenate strings
        String allNames = people.stream()
            .map(Person::getName)
            .collect(Collectors.joining());  // "AlexMariaBobCarol"
        
        String withDelimiter = people.stream()
            .map(Person::getName)
            .collect(Collectors.joining(", "));  // "Alex, Maria, Bob, Carol"
        
        String withPrefixSuffix = people.stream()
            .map(Person::getName)
            .collect(Collectors.joining(", ", "[", "]"));  // "[Alex, Maria, Bob, Carol]"
        
        // groupingBy() - group by property
        Map<String, List<Person>> byDepartment = people.stream()
            .collect(Collectors.groupingBy(Person::getDepartment));
        // {Engineering=[Alex, Bob], Marketing=[Maria, Carol]}
        
        // groupingBy with downstream collector
        Map<String, Long> countByDept = people.stream()
            .collect(Collectors.groupingBy(
                Person::getDepartment,
                Collectors.counting()
            ));
        // {Engineering=2, Marketing=2}
        
        Map<String, Double> avgAgeByDept = people.stream()
            .collect(Collectors.groupingBy(
                Person::getDepartment,
                Collectors.averagingInt(Person::getAge)
            ));
        // {Engineering=32.5, Marketing=26.5}
        
        Map<String, List<String>> namesByDept = people.stream()
            .collect(Collectors.groupingBy(
                Person::getDepartment,
                Collectors.mapping(Person::getName, Collectors.toList())
            ));
        // {Engineering=[Alex, Bob], Marketing=[Maria, Carol]}
        
        // partitioningBy() - split into two groups
        Map<Boolean, List<Person>> adultsAndYouth = people.stream()
            .collect(Collectors.partitioningBy(p -> p.getAge() >= 30));
        // {false=[Maria, Carol], true=[Alex, Bob]}
        
        // Summarizing
        IntSummaryStatistics ageStats = people.stream()
            .collect(Collectors.summarizingInt(Person::getAge));
        System.out.println("Count: " + ageStats.getCount());
        System.out.println("Sum: " + ageStats.getSum());
        System.out.println("Min: " + ageStats.getMin());
        System.out.println("Max: " + ageStats.getMax());
        System.out.println("Avg: " + ageStats.getAverage());
        
        // Reducing
        Optional<Person> oldest = people.stream()
            .collect(Collectors.maxBy(Comparator.comparing(Person::getAge)));
    }
}
```

## Primitive Streams

More efficient for primitive operations:

```java
public class PrimitiveStreams {
    
    public static void main(String[] args) {
        // IntStream, LongStream, DoubleStream
        
        IntStream ints = IntStream.range(1, 6);  // 1, 2, 3, 4, 5
        
        // Aggregate operations
        int sum = IntStream.range(1, 6).sum();           // 15
        double avg = IntStream.range(1, 6).average().getAsDouble();  // 3.0
        int max = IntStream.range(1, 6).max().getAsInt();  // 5
        
        // Convert between object and primitive streams
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        
        // Stream<Integer> -> IntStream
        IntStream intStream = list.stream().mapToInt(Integer::intValue);
        
        // IntStream -> Stream<Integer>
        Stream<Integer> boxed = IntStream.range(1, 6).boxed();
        
        // Useful methods
        int[] array = IntStream.range(1, 6).toArray();
        
        IntSummaryStatistics stats = IntStream.range(1, 6).summaryStatistics();
    }
}
```

## Parallel Streams

Easily parallelize operations:

```java
public class ParallelStreams {
    
    public static void main(String[] args) {
        List<Integer> numbers = IntStream.range(1, 1_000_000)
            .boxed()
            .collect(Collectors.toList());
        
        // Sequential
        long sequentialSum = numbers.stream()
            .reduce(0, Integer::sum);
        
        // Parallel (uses multiple threads)
        long parallelSum = numbers.parallelStream()
            .reduce(0, Integer::sum);
        
        // Or convert existing stream
        long parallelSum2 = numbers.stream()
            .parallel()
            .reduce(0, Integer::sum);
        
        // Back to sequential
        numbers.stream()
            .parallel()
            .filter(n -> n > 500_000)
            .sequential()  // Continue sequentially
            .forEach(System.out::println);
        
        // CAUTION: Not always faster!
        // Good for:
        // - Large datasets
        // - Independent operations
        // - CPU-intensive transformations
        
        // Bad for:
        // - Small datasets (overhead > benefit)
        // - Order-dependent operations
        // - I/O-bound operations
        // - Shared mutable state
    }
}
```

## Real-World Examples

```java
public class StreamExamples {
    
    // 1. Process a CSV file
    public static List<User> loadUsers(Path path) throws IOException {
        try (Stream<String> lines = Files.lines(path)) {
            return lines
                .skip(1)  // Skip header
                .map(line -> line.split(","))
                .filter(parts -> parts.length >= 3)
                .map(parts -> new User(
                    parts[0].trim(),
                    parts[1].trim(),
                    Integer.parseInt(parts[2].trim())
                ))
                .collect(Collectors.toList());
        }
    }
    
    // 2. Find top N elements
    public static List<Product> getTopProducts(List<Product> products, int n) {
        return products.stream()
            .sorted(Comparator.comparing(Product::getRating).reversed())
            .limit(n)
            .collect(Collectors.toList());
    }
    
    // 3. Word frequency count
    public static Map<String, Long> wordFrequency(String text) {
        return Arrays.stream(text.toLowerCase().split("\\W+"))
            .filter(word -> !word.isEmpty())
            .collect(Collectors.groupingBy(
                Function.identity(),
                Collectors.counting()
            ));
    }
    
    // 4. Flatten and deduplicate
    public static List<String> getAllUniqueTags(List<Article> articles) {
        return articles.stream()
            .flatMap(article -> article.getTags().stream())
            .distinct()
            .sorted()
            .collect(Collectors.toList());
    }
    
    // 5. Complex transformation
    public static Map<String, List<String>> getEmailsByDomain(List<User> users) {
        return users.stream()
            .filter(u -> u.getEmail() != null)
            .collect(Collectors.groupingBy(
                u -> u.getEmail().substring(u.getEmail().indexOf("@") + 1),
                Collectors.mapping(User::getEmail, Collectors.toList())
            ));
    }
    
    // 6. Pagination
    public static <T> List<T> paginate(List<T> items, int page, int pageSize) {
        return items.stream()
            .skip((long) page * pageSize)
            .limit(pageSize)
            .collect(Collectors.toList());
    }
}
```

---

# 6. Concurrency & Multi-threading

## What Is Concurrency?

Concurrency allows multiple tasks to make progress simultaneously. In Java, this is achieved through threads.

**Python comparison:** Similar to Python's `threading` module, but Java threads are actual OS threads (Python has the GIL limitation).

## Creating Threads

### Method 1: Extending Thread

```java
public class MyThread extends Thread {
    
    private String name;
    
    public MyThread(String name) {
        this.name = name;
    }
    
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(name + ": " + i);
            try {
                Thread.sleep(100);  // Pause for 100ms
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    
    public static void main(String[] args) {
        MyThread t1 = new MyThread("Thread-1");
        MyThread t2 = new MyThread("Thread-2");
        
        t1.start();  // Start thread (calls run() in new thread)
        t2.start();
        
        // Note: start(), not run()!
        // t1.run() would run in the current thread
    }
}
```

### Method 2: Implementing Runnable (Preferred)

```java
public class MyRunnable implements Runnable {
    
    private String name;
    
    public MyRunnable(String name) {
        this.name = name;
    }
    
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(name + ": " + i);
        }
    }
    
    public static void main(String[] args) {
        Thread t1 = new Thread(new MyRunnable("Task-1"));
        Thread t2 = new Thread(new MyRunnable("Task-2"));
        
        t1.start();
        t2.start();
    }
}
```

### Method 3: Lambda (Most Concise)

```java
public class LambdaThread {
    
    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Lambda thread: " + i);
            }
        });
        
        t1.start();
    }
}
```

## Thread Lifecycle

```
NEW → (start()) → RUNNABLE → (scheduler) → RUNNING → TERMINATED
                      ↑                        ↓
                      ← ← ← ← ← ← ← ← ← ← ← ← ←
                    BLOCKED/WAITING/TIMED_WAITING
```

## Thread Methods

```java
public class ThreadMethodsDemo {
    
    public static void main(String[] args) throws InterruptedException {
        Thread worker = new Thread(() -> {
            System.out.println("Worker starting");
            try {
                Thread.sleep(2000);  // Sleep for 2 seconds
            } catch (InterruptedException e) {
                System.out.println("Worker was interrupted!");
                return;
            }
            System.out.println("Worker done");
        });
        
        // Thread information
        System.out.println("Name: " + worker.getName());
        System.out.println("State: " + worker.getState());  // NEW
        System.out.println("Priority: " + worker.getPriority());
        System.out.println("Is alive: " + worker.isAlive());  // false
        
        worker.start();
        System.out.println("State after start: " + worker.getState());  // RUNNABLE
        System.out.println("Is alive: " + worker.isAlive());  // true
        
        // Wait for thread to complete
        worker.join();  // Block until worker finishes
        System.out.println("Worker finished");
        
        // Join with timeout
        Thread longTask = new Thread(() -> {
            try { Thread.sleep(10000); } catch (InterruptedException e) {}
        });
        longTask.start();
        longTask.join(1000);  // Wait max 1 second
        if (longTask.isAlive()) {
            System.out.println("Task still running, interrupting...");
            longTask.interrupt();
        }
        
        // Current thread
        Thread current = Thread.currentThread();
        System.out.println("Current thread: " + current.getName());
    }
}
```

## Thread Synchronization

When multiple threads access shared data, you need synchronization to prevent race conditions.

### The Problem: Race Condition

```java
public class RaceConditionDemo {
    
    private int counter = 0;
    
    public void increment() {
        counter++;  // NOT atomic! (read, increment, write)
    }
    
    public static void main(String[] args) throws InterruptedException {
        RaceConditionDemo demo = new RaceConditionDemo();
        
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) demo.increment();
        });
        
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) demo.increment();
        });
        
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        
        // Expected: 20000
        // Actual: Unpredictable! (could be 15000, 18000, etc.)
        System.out.println("Counter: " + demo.counter);
    }
}
```

### Solution 1: synchronized Keyword

```java
public class SynchronizedDemo {
    
    private int counter = 0;
    
    // Synchronized method - only one thread can execute at a time
    public synchronized void increment() {
        counter++;
    }
    
    // Synchronized block - more fine-grained control
    public void incrementWithBlock() {
        // Other code can run concurrently...
        
        synchronized (this) {  // Lock on 'this' object
            counter++;
        }
        
        // Other code can run concurrently...
    }
    
    // Using a separate lock object
    private final Object lock = new Object();
    
    public void incrementWithLock() {
        synchronized (lock) {
            counter++;
        }
    }
    
    public static void main(String[] args) throws InterruptedException {
        SynchronizedDemo demo = new SynchronizedDemo();
        
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) demo.increment();
        });
        
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) demo.increment();
        });
        
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        
        System.out.println("Counter: " + demo.counter);  // Always 20000
    }
}
```

### Solution 2: Atomic Classes

```java
import java.util.concurrent.atomic.*;

public class AtomicDemo {
    
    // Thread-safe counter
    private AtomicInteger counter = new AtomicInteger(0);
    
    public void increment() {
        counter.incrementAndGet();  // Atomic operation
    }
    
    public int getCounter() {
        return counter.get();
    }
    
    public static void main(String[] args) throws InterruptedException {
        AtomicDemo demo = new AtomicDemo();
        
        // Multiple threads incrementing
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) demo.increment();
        });
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) demo.increment();
        });
        
        t1.start(); t2.start();
        t1.join(); t2.join();
        
        System.out.println("Counter: " + demo.getCounter());  // Always 20000
        
        // Other atomic classes
        AtomicLong atomicLong = new AtomicLong(0);
        AtomicBoolean atomicBoolean = new AtomicBoolean(false);
        AtomicReference<String> atomicRef = new AtomicReference<>("initial");
        
        // Atomic operations
        int oldValue = demo.counter.getAndIncrement();  // Returns old, then increments
        int newValue = demo.counter.incrementAndGet();  // Increments, then returns new
        boolean updated = demo.counter.compareAndSet(5, 10);  // CAS operation
        demo.counter.addAndGet(5);  // Add and get result
    }
}
```

### Solution 3: Locks (java.util.concurrent.locks)

```java
import java.util.concurrent.locks.*;

public class LockDemo {
    
    private int counter = 0;
    private final Lock lock = new ReentrantLock();
    
    public void increment() {
        lock.lock();  // Acquire lock
        try {
            counter++;
        } finally {
            lock.unlock();  // ALWAYS unlock in finally!
        }
    }
    
    // Try to acquire lock with timeout
    public boolean tryIncrement() {
        try {
            if (lock.tryLock(1, TimeUnit.SECONDS)) {
                try {
                    counter++;
                    return true;
                } finally {
                    lock.unlock();
                }
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return false;
    }
    
    // ReadWriteLock - multiple readers OR one writer
    private final ReadWriteLock rwLock = new ReentrantReadWriteLock();
    private List<String> data = new ArrayList<>();
    
    public String read(int index) {
        rwLock.readLock().lock();
        try {
            return data.get(index);
        } finally {
            rwLock.readLock().unlock();
        }
    }
    
    public void write(String value) {
        rwLock.writeLock().lock();
        try {
            data.add(value);
        } finally {
            rwLock.writeLock().unlock();
        }
    }
}
```

## Thread Communication

### wait() and notify()

```java
public class ProducerConsumer {
    
    private final Queue<Integer> queue = new LinkedList<>();
    private final int capacity = 10;
    
    public synchronized void produce(int item) throws InterruptedException {
        while (queue.size() == capacity) {
            wait();  // Wait until space available
        }
        queue.offer(item);
        System.out.println("Produced: " + item);
        notifyAll();  // Notify waiting consumers
    }
    
    public synchronized int consume() throws InterruptedException {
        while (queue.isEmpty()) {
            wait();  // Wait until item available
        }
        int item = queue.poll();
        System.out.println("Consumed: " + item);
        notifyAll();  // Notify waiting producers
        return item;
    }
    
    public static void main(String[] args) {
        ProducerConsumer pc = new ProducerConsumer();
        
        Thread producer = new Thread(() -> {
            for (int i = 0; i < 20; i++) {
                try {
                    pc.produce(i);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });
        
        Thread consumer = new Thread(() -> {
            for (int i = 0; i < 20; i++) {
                try {
                    pc.consume();
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });
        
        producer.start();
        consumer.start();
    }
}
```

### BlockingQueue (Preferred)

```java
import java.util.concurrent.*;

public class BlockingQueueDemo {
    
    public static void main(String[] args) {
        // Handles synchronization automatically!
        BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(10);
        
        Thread producer = new Thread(() -> {
            try {
                for (int i = 0; i < 20; i++) {
                    queue.put(i);  // Blocks if full
                    System.out.println("Produced: " + i);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        Thread consumer = new Thread(() -> {
            try {
                for (int i = 0; i < 20; i++) {
                    int item = queue.take();  // Blocks if empty
                    System.out.println("Consumed: " + item);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        producer.start();
        consumer.start();
    }
}
```

## Thread-Safe Collections

```java
import java.util.concurrent.*;

public class ConcurrentCollectionsDemo {
    
    public static void main(String[] args) {
        // ConcurrentHashMap - thread-safe HashMap
        ConcurrentMap<String, Integer> map = new ConcurrentHashMap<>();
        map.put("key1", 1);
        map.putIfAbsent("key2", 2);
        map.computeIfAbsent("key3", k -> 3);
        
        // CopyOnWriteArrayList - thread-safe ArrayList (for read-heavy workloads)
        List<String> list = new CopyOnWriteArrayList<>();
        list.add("item");
        
        // CopyOnWriteArraySet - thread-safe Set
        Set<String> set = new CopyOnWriteArraySet<>();
        
        // ConcurrentLinkedQueue - non-blocking queue
        Queue<String> queue = new ConcurrentLinkedQueue<>();
        queue.offer("item");
        String item = queue.poll();
        
        // BlockingQueue implementations
        BlockingQueue<String> arrayQueue = new ArrayBlockingQueue<>(100);
        BlockingQueue<String> linkedQueue = new LinkedBlockingQueue<>();
        BlockingQueue<String> priorityQueue = new PriorityBlockingQueue<>();
    }
}
```

## Common Concurrency Patterns

### CountDownLatch - Wait for N events

```java
public class CountDownLatchDemo {
    
    public static void main(String[] args) throws InterruptedException {
        int numWorkers = 3;
        CountDownLatch latch = new CountDownLatch(numWorkers);
        
        for (int i = 0; i < numWorkers; i++) {
            final int workerId = i;
            new Thread(() -> {
                System.out.println("Worker " + workerId + " starting");
                try {
                    Thread.sleep(1000 * (workerId + 1));
                } catch (InterruptedException e) {}
                System.out.println("Worker " + workerId + " done");
                latch.countDown();  // Signal completion
            }).start();
        }
        
        System.out.println("Waiting for workers...");
        latch.await();  // Block until count reaches 0
        System.out.println("All workers finished!");
    }
}
```

### Semaphore - Limit concurrent access

```java
public class SemaphoreDemo {
    
    public static void main(String[] args) {
        // Only 3 threads can access the resource at a time
        Semaphore semaphore = new Semaphore(3);
        
        for (int i = 0; i < 10; i++) {
            final int id = i;
            new Thread(() -> {
                try {
                    semaphore.acquire();  // Wait for permit
                    System.out.println("Thread " + id + " acquired permit");
                    Thread.sleep(2000);  // Use resource
                    System.out.println("Thread " + id + " releasing permit");
                } catch (InterruptedException e) {
                } finally {
                    semaphore.release();  // Return permit
                }
            }).start();
        }
    }
}
```

### CyclicBarrier - Synchronize threads at a barrier

```java
public class CyclicBarrierDemo {
    
    public static void main(String[] args) {
        int numThreads = 3;
        
        CyclicBarrier barrier = new CyclicBarrier(numThreads, () -> {
            System.out.println("All threads reached barrier!");
        });
        
        for (int i = 0; i < numThreads; i++) {
            final int id = i;
            new Thread(() -> {
                try {
                    System.out.println("Thread " + id + " working...");
                    Thread.sleep(1000 * (id + 1));
                    System.out.println("Thread " + id + " waiting at barrier");
                    barrier.await();  // Wait for others
                    System.out.println("Thread " + id + " continuing");
                } catch (Exception e) {}
            }).start();
        }
    }
}
```

---

# 7. The Executor Framework

## Why Executors?

Creating threads directly has problems:
1. Thread creation is expensive
2. Hard to manage many threads
3. No built-in task queuing
4. Difficult to handle results

The Executor framework solves all of these!

## Basic Executor Interface

```java
public interface Executor {
    void execute(Runnable command);
}
```

## ExecutorService

```java
import java.util.concurrent.*;

public class ExecutorServiceDemo {
    
    public static void main(String[] args) throws Exception {
        // Create a thread pool with 4 threads
        ExecutorService executor = Executors.newFixedThreadPool(4);
        
        // Submit tasks
        executor.execute(() -> System.out.println("Task 1"));
        executor.execute(() -> System.out.println("Task 2"));
        executor.execute(() -> System.out.println("Task 3"));
        
        // Submit Callable (returns a result)
        Future<String> future = executor.submit(() -> {
            Thread.sleep(1000);
            return "Hello from task!";
        });
        
        // Get result (blocks until ready)
        String result = future.get();  // "Hello from task!"
        
        // Get with timeout
        try {
            String result2 = future.get(500, TimeUnit.MILLISECONDS);
        } catch (TimeoutException e) {
            System.out.println("Task took too long!");
        }
        
        // Check status
        boolean isDone = future.isDone();
        boolean isCancelled = future.isCancelled();
        
        // Cancel task
        boolean cancelled = future.cancel(true);  // true = interrupt if running
        
        // Shutdown executor (important!)
        executor.shutdown();  // No new tasks, wait for existing
        
        // Wait for termination
        if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
            executor.shutdownNow();  // Force shutdown
        }
    }
}
```

## Types of Thread Pools

```java
public class ThreadPoolTypes {
    
    public static void main(String[] args) {
        // 1. Fixed Thread Pool - fixed number of threads
        ExecutorService fixed = Executors.newFixedThreadPool(4);
        // Good for: CPU-intensive tasks, known workload
        
        // 2. Cached Thread Pool - creates threads as needed, reuses idle threads
        ExecutorService cached = Executors.newCachedThreadPool();
        // Good for: Many short-lived tasks, variable load
        // Caution: Can create too many threads!
        
        // 3. Single Thread Executor - one thread, tasks run sequentially
        ExecutorService single = Executors.newSingleThreadExecutor();
        // Good for: Tasks that must run sequentially
        
        // 4. Scheduled Thread Pool - run tasks after delay or periodically
        ScheduledExecutorService scheduled = Executors.newScheduledThreadPool(2);
        // Good for: Scheduled/periodic tasks
        
        // 5. Work-Stealing Pool (Java 8+) - uses ForkJoinPool
        ExecutorService workStealing = Executors.newWorkStealingPool();
        // Good for: Recursive/divide-and-conquer tasks
        
        // Remember to shutdown!
        fixed.shutdown();
        cached.shutdown();
        single.shutdown();
        scheduled.shutdown();
        workStealing.shutdown();
    }
}
```

## Scheduled Executor

```java
public class ScheduledExecutorDemo {
    
    public static void main(String[] args) {
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
        
        // Run once after delay
        scheduler.schedule(() -> {
            System.out.println("Delayed task");
        }, 3, TimeUnit.SECONDS);
        
        // Run periodically (fixed rate)
        // Runs every 2 seconds, regardless of task duration
        ScheduledFuture<?> fixedRate = scheduler.scheduleAtFixedRate(() -> {
            System.out.println("Fixed rate task: " + System.currentTimeMillis());
        }, 0, 2, TimeUnit.SECONDS);
        
        // Run periodically (fixed delay)
        // Waits 2 seconds AFTER previous task completes
        ScheduledFuture<?> fixedDelay = scheduler.scheduleWithFixedDelay(() -> {
            System.out.println("Fixed delay task");
            try { Thread.sleep(1000); } catch (InterruptedException e) {}
        }, 0, 2, TimeUnit.SECONDS);
        
        // Cancel scheduled task after 10 seconds
        scheduler.schedule(() -> {
            fixedRate.cancel(false);
            fixedDelay.cancel(false);
            scheduler.shutdown();
        }, 10, TimeUnit.SECONDS);
    }
}
```

## Callable and Future

```java
public class CallableFutureDemo {
    
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        // Callable returns a result
        Callable<Integer> task = () -> {
            Thread.sleep(1000);
            return 42;
        };
        
        // Submit returns a Future
        Future<Integer> future = executor.submit(task);
        
        // Do other work while task runs...
        System.out.println("Doing other work...");
        
        // Get result (blocks if not ready)
        Integer result = future.get();
        System.out.println("Result: " + result);
        
        // Submit multiple tasks
        List<Callable<String>> tasks = Arrays.asList(
            () -> { Thread.sleep(1000); return "Task 1"; },
            () -> { Thread.sleep(2000); return "Task 2"; },
            () -> { Thread.sleep(1500); return "Task 3"; }
        );
        
        // invokeAll - wait for all to complete
        List<Future<String>> futures = executor.invokeAll(tasks);
        for (Future<String> f : futures) {
            System.out.println(f.get());
        }
        
        // invokeAny - return first completed result
        String firstResult = executor.invokeAny(tasks);
        System.out.println("First result: " + firstResult);
        
        executor.shutdown();
    }
}
```

## CompletableFuture (Java 8+)

This is the **modern way** to handle asynchronous programming:

```java
import java.util.concurrent.CompletableFuture;

public class CompletableFutureDemo {
    
    public static void main(String[] args) throws Exception {
        
        // Create and complete manually
        CompletableFuture<String> future1 = new CompletableFuture<>();
        new Thread(() -> {
            try { Thread.sleep(1000); } catch (InterruptedException e) {}
            future1.complete("Done!");
        }).start();
        
        // Run async (uses ForkJoinPool by default)
        CompletableFuture<Void> future2 = CompletableFuture.runAsync(() -> {
            System.out.println("Running async");
        });
        
        // Supply async (returns a result)
        CompletableFuture<String> future3 = CompletableFuture.supplyAsync(() -> {
            return "Hello";
        });
        
        // Chaining transformations
        CompletableFuture<String> chained = CompletableFuture
            .supplyAsync(() -> "hello")
            .thenApply(s -> s + " world")      // Transform result
            .thenApply(String::toUpperCase);   // Chain another transformation
        
        System.out.println(chained.get());  // "HELLO WORLD"
        
        // thenAccept - consume result (no return)
        CompletableFuture.supplyAsync(() -> "Hello")
            .thenAccept(s -> System.out.println("Received: " + s));
        
        // thenRun - run action after completion (ignores result)
        CompletableFuture.supplyAsync(() -> "Hello")
            .thenRun(() -> System.out.println("Task finished"));
        
        // thenCompose - flatten nested futures
        CompletableFuture<String> composed = CompletableFuture
            .supplyAsync(() -> "User123")
            .thenCompose(userId -> fetchUserData(userId));  // Returns CompletableFuture
        
        // thenCombine - combine two futures
        CompletableFuture<String> combined = CompletableFuture
            .supplyAsync(() -> "Hello")
            .thenCombine(
                CompletableFuture.supplyAsync(() -> "World"),
                (s1, s2) -> s1 + " " + s2
            );
        System.out.println(combined.get());  // "Hello World"
        
        // Error handling
        CompletableFuture<String> withError = CompletableFuture
            .supplyAsync(() -> {
                if (true) throw new RuntimeException("Oops!");
                return "Success";
            })
            .exceptionally(ex -> "Error: " + ex.getMessage());
        
        System.out.println(withError.get());  // "Error: Oops!"
        
        // Handle both success and error
        CompletableFuture<String> handled = CompletableFuture
            .supplyAsync(() -> "Success")
            .handle((result, ex) -> {
                if (ex != null) return "Error: " + ex.getMessage();
                return "Result: " + result;
            });
        
        // Wait for all
        CompletableFuture<Void> all = CompletableFuture.allOf(
            CompletableFuture.supplyAsync(() -> task1()),
            CompletableFuture.supplyAsync(() -> task2()),
            CompletableFuture.supplyAsync(() -> task3())
        );
        all.join();  // Wait for all to complete
        
        // Wait for any (first to complete)
        CompletableFuture<Object> any = CompletableFuture.anyOf(
            CompletableFuture.supplyAsync(() -> slowTask()),
            CompletableFuture.supplyAsync(() -> fastTask())
        );
        System.out.println("First result: " + any.get());
    }
    
    static CompletableFuture<String> fetchUserData(String userId) {
        return CompletableFuture.supplyAsync(() -> "Data for " + userId);
    }
    
    static String task1() { return "Task 1"; }
    static String task2() { return "Task 2"; }
    static String task3() { return "Task 3"; }
    static String slowTask() { 
        try { Thread.sleep(2000); } catch (InterruptedException e) {}
        return "Slow"; 
    }
    static String fastTask() { return "Fast"; }
}
```

## Real-World Async Example

```java
public class AsyncServiceExample {
    
    private final ExecutorService executor = Executors.newFixedThreadPool(10);
    
    // Simulate fetching user from database
    public CompletableFuture<User> fetchUser(String userId) {
        return CompletableFuture.supplyAsync(() -> {
            // Simulate DB call
            try { Thread.sleep(500); } catch (InterruptedException e) {}
            return new User(userId, "Alex");
        }, executor);
    }
    
    // Simulate fetching orders
    public CompletableFuture<List<Order>> fetchOrders(String userId) {
        return CompletableFuture.supplyAsync(() -> {
            try { Thread.sleep(800); } catch (InterruptedException e) {}
            return Arrays.asList(new Order("O1"), new Order("O2"));
        }, executor);
    }
    
    // Simulate sending notification
    public CompletableFuture<Void> sendNotification(User user, String message) {
        return CompletableFuture.runAsync(() -> {
            System.out.println("Sending to " + user.getName() + ": " + message);
        }, executor);
    }
    
    // Combine multiple async operations
    public CompletableFuture<UserDashboard> getUserDashboard(String userId) {
        CompletableFuture<User> userFuture = fetchUser(userId);
        CompletableFuture<List<Order>> ordersFuture = fetchOrders(userId);
        
        return userFuture.thenCombine(ordersFuture, (user, orders) -> {
            return new UserDashboard(user, orders);
        });
    }
    
    // Complex workflow
    public CompletableFuture<Void> processOrder(String userId, Order order) {
        return fetchUser(userId)
            .thenCompose(user -> validateUser(user))
            .thenCompose(user -> saveOrder(user, order))
            .thenCompose(savedOrder -> sendNotification(
                savedOrder.getUser(), 
                "Order " + savedOrder.getId() + " confirmed!"
            ))
            .exceptionally(ex -> {
                System.err.println("Order failed: " + ex.getMessage());
                return null;
            });
    }
    
    public void shutdown() {
        executor.shutdown();
    }
}
```

## Best Practices Summary

```java
public class BestPractices {
    
    // 1. Always shutdown executors
    public void example1() {
        ExecutorService executor = Executors.newFixedThreadPool(4);
        try {
            // Submit tasks...
        } finally {
            executor.shutdown();
            try {
                if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
                    executor.shutdownNow();
                }
            } catch (InterruptedException e) {
                executor.shutdownNow();
            }
        }
    }
    
    // 2. Handle InterruptedException properly
    public void example2() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();  // Restore interrupt flag
            return;
        }
    }
    
    // 3. Prefer higher-level constructs
    // BAD: manual thread creation
    // GOOD: ExecutorService, CompletableFuture
    
    // 4. Size thread pools appropriately
    // CPU-intensive: number of CPUs
    int cpuPool = Runtime.getRuntime().availableProcessors();
    
    // IO-intensive: more threads (waiting on IO)
    int ioPool = Runtime.getRuntime().availableProcessors() * 2;
    
    // 5. Use concurrent collections, not synchronized wrappers
    // BAD: Collections.synchronizedMap(new HashMap<>())
    // GOOD: new ConcurrentHashMap<>()
    
    // 6. Prefer immutable objects in concurrent code
    // Immutable objects are inherently thread-safe
}
```

---

# Summary

You've now covered all the advanced Java topics from the course:

| Topic | Key Takeaways |
|-------|---------------|
| **Exceptions** | Checked vs unchecked, try-with-resources, custom exceptions |
| **Generics** | Type safety, wildcards, PECS principle |
| **Collections** | List, Set, Map implementations, when to use which |
| **Lambdas** | Functional interfaces, method references, built-in interfaces |
| **Streams** | Declarative data processing, collectors, parallel streams |
| **Concurrency** | Synchronization, locks, thread-safe collections |
| **Executors** | Thread pools, CompletableFuture, async programming |

## Quick Reference for Your Python Background

| Python | Java |
|--------|------|
| `try/except/finally` | `try/catch/finally` |
| `with open()` | `try (resource)` |
| `typing.Generic[T]` | `class Name<T>` |
| `list` | `ArrayList<T>` |
| `dict` | `HashMap<K,V>` |
| `set` | `HashSet<T>` |
| `lambda x: x*2` | `x -> x*2` |
| `[x*2 for x in lst if x>0]` | `lst.stream().filter(x->x>0).map(x->x*2).collect(...)` |
| `threading.Thread` | `Thread` / `ExecutorService` |
| `asyncio` | `CompletableFuture` |

Good luck with your Java learning journey, Alex! 🚀
