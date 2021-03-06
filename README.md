# Design Patterns in Python

Design Patterns are reusable solutions to common programming problems. They were popularized with the 1994 book Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma, John Vlissides, Ralph Johnson and Richard Helm (who are commonly known as a Gang of Four, hence the GoF acronym).
The original book was written using C++ and Smalltalk as examples, but since then, design patterns have been adapted to every programming language imaginable: C#, Java, Python and even programming languages that aren't strictly object-oriented, such as JavaScript.
The appeal of design patterns is immortal: we see them in libraries, some of them are intrinsic in programming languages, and you probably use them on a daily basis even if you don't realize they are there.


## The SOLID Design Principles
In object-oriented computer programming, SOLID is a mnemonic acronym for five design principles intended to make software designs more understandable, flexible, and maintainable.
The principles are a subset of many principles promoted by American software engineer and instructor Robert C. Martin, first introduced in his 2000 paper Design Principles and Design Patterns.

### Single Responsability Principle
A class should only have a single responsibility, that is, only changes to one part of the software's specification should be able to affect the specification of the class.
* A class should only have one reason to change
* Separation of concerns - different classes handling different, independent tasks/problems

### Open-Closed Principle
* Classes should be open for extension but close for modification

### Liskow Substitution Principle
"Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program."
* You should be able to substitute a base type for a subtype
* Any function that use a class should also work for any derived classes

### Interface Segregation Principle
"Many client-specific interfaces are better than one general-purpose interface."[
* Don't put too much into an interface, split into separate interfaces
* YAGNI - You Ain't Going to Need It

### Dependency Inversion Principle
"Depend upon abstractions, [not] concretions."
* High-level modules should not depend upon low-level ones; use abstractions


## Creational Patterns

### Builder
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.



## Structural Patterns


## Behavioral Patterns
