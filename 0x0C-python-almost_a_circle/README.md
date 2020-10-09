# 0x0C. - Python - Almost a Circle

### About
Project to review all concepts learned sofar in Holberton School's Python curriculum

### Files Used in this Project

FILE | DESCRIPTION
----|----
[0. If it's not tested it doesn't work](./tests) | Unittests for all files
[1. Base Class](./models/base.py) | Base class with private class attribute and class constructor
[1. Base init](./models/__init__.py) | empty init file
[2. First Rectangle](./models/rectangle.py) | Class 'Rectangle' that inherits from Base
[3. Validate Attributes](./models/rectangle.py) | Validation of all setter methods and instantiation
[4. Area First](./models/rectangle.py) | Adds public method that returns area value of 'Rectangle' instance
[5. Display #0](./models/rectangle.py) | Adds public method that prints the instance of 'Rectangle' with the character '#'
[6. \_\_str\_\_](./models/rectangle.py) | Override \_\_str\_\_ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
[7. Display #1](./models/rectangle.py) | Improves display method by taking care of x and y
[8. Update #0](./models/rectangle.py) | Adds public method that assigns an argument to each attribute
[9. Update #1](./models/rectangle.py) | Assigns key/value agrument to attributes
[10. And now, the Square!](./models/square.py) | Class 'Square' inherits from Rectangle
[11. Square size](./models/square.py) | Adds public getter and setter width and height
[12. Square Update](./models/square.py) | Adds public method to assign attributes
[13. Rectangle Instance to Dictionary Representation](./models/rectangle.py) | Adds public method that returns the dictionary representation of 'Rectangle'
[14. Square Instance to Dictionary Representation](./models/square.py) | Adds public method that returns the dictionary representation of 'Square'
[15. Dictionary to JSON string](./models/base.py) | Adds static method that returns the JSON string representation
[16. JSON string to file](./models/base.py) | Adds class method that writes the JSON string representation of list_objs to a file
[17. JSON string to Dictionary](./models/base.py) | Adds static method that returns the list of the JSON string representation
[18. Dictionary to Instance](./models/base.py) | Adds class method that returns an instance with all attributes already set
[19. File to Instances](./models/base.py) | Adds class method that returns list of instances
[20. JSON ok, but CSV?](./models/) | Adds class methods to serialize and deserialize in CSV
[21. Let's Draw It](./models/base.py) | Adds static method that opens a window and draws all 'Rectangles' and 'Squares' with Turtle graphics module

### Author
Deyber Castañeda
