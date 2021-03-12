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
* Deal with the creation (construction) of objects.

### Builder
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

Motivation:
* Some objects are simple and can be created in a single initializer call.
* Other objects require a lot of ceremony to create.
* Having an object with 10 initializer arguments is not productive.
* Instead, opt for piecewise construction.
* Builder is a component that provides an API for constructing and object step-by-step.

### Factory Method & Abstract Factory
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
A Factory is a component responsible solely for the wholesale (not piecewise) creation of objects.
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

Factories motivation:
* Object creation logic become too convoluted
* Initializer is not descriptive, name is always __init__. Cannot overload with same sets of arguments with different names, can turn into 'optional parameter hell'
* Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to:
  * A separate method (Factory Method)
  * That may exist in a separate class (Factory)
  * Can create hierarchy of factories with Abstract Factory

Summary:
* A Factory Method is a static method that creates Objects
* A Factory is any entity that can take care of object creation
* A Factory can be external or reside inside the object as an inner class
* Hierarchies of factories can be used to create related objects

### Prototype
Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.
A Prototype is a partially or fully initialized object that you copy (clone) and make use of it.

Motivation:
* Complicated objects (e.g. cars) are not designed from scratch. They reiterate existing designs
* An existing (partially or fully constructed) design is a Prototype
* We make a copy (clone) the prototype and customize it
* We make the cloning convenient (e.g. via a Factory)

Summary:
* To implement a prototype, partially construct an object and store it somewhere
* Deep copy the prototype
* Customize the resulting instance
* A factory provides a convenient API for using prototypes

### Singleton
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

Motivation:
* For some components it only makes sense to have one in the system
  * Database repository
  * Object factory
* E.g. the initializer call is expensive
  * We only do it once
  * We provide everyone with the same instance
* We want to prevent anyone creating additional copies
* Need to take care of lazy instantiation, you initialized it only when somebody ask for

Summary:
* Different realizations of Singleton:
  * Custom Allocator (was a nice idea but unfortunately still ended up calling the initializer more than once)
  * Decorator
  * Metaclass (This is probably the nicest implementation of Singleton)
  * Monostate variation
* Laziness is easy, just init the Singleton on first request (we check if it has been created before)


## Structural Patterns
* Concerned with the structure (e.g., class members).
* Many patterns are wrappers that mimic the underlying class' interface.
* Put extra weight on the importance of good API design.

### Adapter
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate. A construct which adapts an existing interface X to conform to the required interface Y.

Summary:
* Implementing and adapter is easy
* First determine the API you have and the API you need
* Then create a component which aggregates (has a reference to ...) the adaptee
* Intermediate representations can pile up: use caching and other optimizations

### Bridge
Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

Motivation:
* Bridge prevents a Cartesian product' complexity explosion
* Example:
  * Base class ThreadScheduler
  * Can be preemptive or cooperative
  * Can run on Windows or Unix
  * End up with a 2x2 scenario: WinPTS, UnixPTS, WinCTS, UnixCTS
* Bridge pattern avoids the entity explosion

### Composite
Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.

Motivation:
* Objects use other objects' properties/members through inheritance and composition
* Composition lets us make compound objects
  * E.g. a mathematical expression composed of simple expressions
  * E.g. a grouping of shapes that consists of several shapes
* Composite design pattern is used to treat both single (scalar) and composite objects uniformly
  * I.e. Foo and Sequence (yielding Foo's) have common APIs


## Behavioral Patterns
* They are all different; no central theme
