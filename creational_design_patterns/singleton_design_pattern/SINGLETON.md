# Design Pattern
In software engineering, a design pattern is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations

# Uses of Design Patterns
Design patterns can speed up the development process by providing tested, proven development paradigms. Effective software design requires considering issues that may not become visible until later in the implementation. Reusing design patterns helps to prevent subtle issues that can cause major problems and improves code readability for coders and architects familiar with the patterns.

# Types of Design Pattern
1. Creational design patterns
2. Structural design patterns
3. Behavioral design patterns

# Creational Design Pattern
In software engineering, creational design patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by somehow controlling this object creation.

## Forms of Creational Pattern
1. Abstract Factory
2. Builder
3. Factory Method
4. Object Pool
5. Prototype
6. Singleton


here today we talk about `Singleton Design pattern`

## Singleton Design Pattern
The singleton design pattern restricts the instantiation of a class to a single instance. This is done in order to provide coordinated access to a certain resource, throughout an entire software system. Through this design pattern, the singleton class ensures that it’s only instantiated once, and can provide easy access to the single instance.

* Common use-cases for the singleton design pattern include factories, builders, and objects that hold program state. 
* Ensure a class has only one instance, and provide a global point of access to it.
* Encapsulated "just-in-time initialization" or "initialization on first use".

### Usage
* Singletons are sometimes considered to be an alternative to global variables or static classes.
* Common use-cases for the singleton design pattern include factories, builders, and objects that hold program state.

Compared to global variables, singletons have the following benefits:

* Singleton instance fields don’t take up space in the global namespace
* Singletons may be lazily initialized (to be discussed further)

#### Examples
1. Redux
2. Cache
3. Constant
4. Setting Config
5. Loging

