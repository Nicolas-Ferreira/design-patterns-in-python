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
* Initializer is not descriptive, name is always `__init__`. Cannot overload with same sets of arguments with different names, can turn into 'optional parameter hell'
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

### Decorator
Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.
This means you can add additional behaviors to a particular classes without either modifying the class or indeed inheriting from them.

 Motivation:
 * Want to augment an object with additional functionality
 * Do not want to rewrite or alter existing object (not break the OCP)
 * Want to keep new functionality separate (not break SRP)
 * Need to be able to interact with existing structures
 * Two options:
  * Inherit from required object (if possible) and add new functionality
  * Build a decorator, which simply references the decorated objects(s)

Summary:
* A decorator keeps the reference to the decorated Objects
* Adds utility attributes and methods to augment the object's features
* May or may not forward calls to the underlying object
* Proxying of underlying calls can be done dynamically
* Python's functional decorators wrap functions; no direct relation to the GoF Decorator pattern

### Facade
Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.
Facade provides a simple, easy to understand/use interface over a large and sophisticated body of code.

Motivation:
* Balancing complexity and presentation/usability
* Typical home
  * Many subsystems (electrical, sanitation)
  * Complex internal structure (floor layers)
  * End user is not exposed to internals
* Same with software!
  * Many systems working provide flexibility, but..
  * API consumers want it to just work

Summary:
* Build a Facade to provide a simplified API over a set of Classes
* May wish to (optionally) expose internals through the facade
* May allow users to escalate to use more complex APIs if the need to

### Flyweight
Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.
It is a space optimization technique that lets us use less memory by storing externally the data associated with similar objects.

Motivation:
* Avoid redundancy when storing data
* E.g. MMORPG
  * Plenty of users with identical first/last names
  * No sense in storing same first/last names over and over again
  * Store a list of names and references to them
* E.g. bold or italic text formatting
  * Do not want each character to have a formatting character
  * Operate on ranges (e.g. line number, start/end positions)

Summary:
* Store common data externally
* Specify an index or a reference into the external data store
* Define the idea of 'ranges' on homogeneous collections and store data related to those ranges

### Proxy
Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.
It is basically a class that functions as an interface to a particular resource. That resource may be remote, expensive to construct, or may require logging or some other added functionality.

Motivation:
* You are calling foo.Bar()
* This assumes that foo is in the same process as Bar()
* What if, later on, you want to put all Foo-related operations into a separate process
  * Can you avoid changing your code?
* Proxy to the rescue!
  * Same interface, entirely different behaviour
* This is called a communication Proxy
  * Other types: logging, virtual, guarding, ...

Summary:
* A proxy has the same interface as the underlying object
* To create a proxy, simply replicate the existing interface of an object
* Add relevant functionality to the redefined member functions
* Different proxies (communication, logging, caching, etc.) have completely different behaviours


## Behavioral Patterns
* They are all different; no central theme

### Chain of Responsibility
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.
It is all about chaining several components who all get a chance to process a command or a query, optionally having default processing implementation and an ability to terminate the processing chain.

Motivation:
* Unethical behavior by an employee; who takes the blame?
  * Employee
  * Manager
  * CEO
* You click a graphical element on a form
  * Button handles it, stops further processing
  * Underlying group box
  * Underlying window
* CCG computer game
  * Creature has attack and defense values
  * Those can be boosted by others

Summary:
* CoR can be implemented as a chain of references or a centralized construct
* Enlist objects in the chain, possible controlling their order
* Object removal from chain (e.g. in `__exit__`)

### Command
Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations.
A command is simple an object which represents an instruction to perform a particular action. Contains all the information necessary for the action to be taken.

Motivation:
* Ordinary statements are perishable
  * Cannot undo member assignment
  * Cannot directly serialize a sequence of actions (calls)
* Want an object that represents and operation
  * person should change its age to value 22
  * car should do explode()
* Uses: GUI commands, multi-level undo/redo, macro recording and more!

Summary:
* Encapsulate all details of an operation in a separate object
* Define instruction for applying the command (either in the command itself or elsewhere)
* Optionally define instructions for undoing the command
* Can create composite commands (a.k.a. macros)

### Interpreter
The interpreter is a component that processes structured text data. Does so by turning it into separate lexical tokens (lexing) and the interpreting sequences of said tokens (parsing).

Motivation:
* Textual input needs to be processed
  * E.g. turned into OOP structures 
* Some examples
  * Programming language compilers
  * HTML, XML and similar
  * Numeric expressions (3+4/5)
  * Regular expressions
* Turning strings into OOP based structures in a complicated object

Summary:
* Barring simple cases, an interpreter acts in two stages
* Lexing turns text into a set of tokens, e.g. 3*(4+5) -> Lit[3] Star Lparen Lit[4] Plus Lit[5] Rparen
* Parsing tokens into meaningful constructs
* Parsed data can then be traversed

### Iterator
Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

Motivation:
* Iteration (traversal) is a core functionality of various data structures
* An iterator is a class that facilitates the traversal
  * Keeps a reference to the current element
  * Knows how to move to a different element
* The iterator protocol requires
  * `__iter__()` to expose the iterator, which uses
  * `__next__()` to return each of the iterated elements or
  * raise StopIteration when it's done

Summary:
* An iterator specify how you can traverse an object
* Stateful iterators cannot be recursive
* yield allows for much more succinct iteration

### Mediator
Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

Motivation:
* Components may go in and out of a system at any time
  * Chat room participants
  * Players in a MMORPG
* It makes no sense for them to have direct references to one another
  * Those references may go dead
* Solution: have them all refer to some central component that facilitates communication

Summary:
* Create the mediator and have each object in the system to refer to it
  * E.g. in a property
* Mediator engages the bidirectional communication with tis connected components
* Mediator has functions the components can call
* Components have functions the mediator can call
* Event processing libraries make communication easier to implement

### Memento
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.
A token/handle representing the system state. Let us roll back to the state when the token was generated. May or may not directly expose state information.

Motivation:
* An object or system goes through changes
  * E.g. a bank account get deposits and withdrawals
* There are different ways of navigating those changes
* One way is to record every change (Command) and teach a command to undo itself
* Another is to simply save snapshots of the system (Memento)

Summary:
* Mementos are use to roll back states arbitrarily
* A memento is simply a token/handle class with (typically) no functions of its own
* A memento is not required to expose directly the state(s) to which it reverts the system
* Can be used to implement undo/redo

### Observer
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
