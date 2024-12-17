# Shape Adapter System

This Python project demonstrates the Adapter design pattern, enabling an existing, incompatible `XXCircle` class to work within a standard `Shape` interface. The adapter allows `XXCircle` to integrate seamlessly with other shapes like `Point` and `Line`, which already follow the `Shape` interface.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Overview](#project-overview)
4. [Key Features](#key-features)
5. [Purpose and Lessons Learned](#purpose-and-lessons-learned)

## Installation

To set up and run this project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alex-nin/adapter-design-pattern.git
   cd adapter-design-pattern
   ```
2. **Install Dependencies:** Ensure you have Python 3.x installed.

## Usage

To run the program, execute the following command in your terminal in the program directory, depending on your Python environment:

```bash
python adapter.py
```
or
```bash
python3 adapter.py
```

This will demonstrate the CircleAdapter enabling XXCircle to work with the standard Shape interface, along with Point and Line objects.

## Project Overview

The main components include:
- **XXCircle**: An external or legacy circle class that has unique methods for operations like setting location, displaying, and filling. It does not follow the standard `Shape` interface.
- **Shape Interface**: The target interface which defines standardized methods for shapes (`setLocation`, `getLocation`, `display`, `fill`, `setColor`, and `undisplay`).
- **CircleAdapter**: An adapter class that wraps `XXCircle`, translating its unique methods to match the `Shape` interface. This enables `XXCircle` to be used interchangeably with `Shape`-compatible classes.
- **Additional Shapes (Point, Line)**: These classes implement the `Shape` interface, providing standard methods for graphical operations. 

## Key Features

- **Interface Compatibility**: The `CircleAdapter` bridges `XXCircle` with the standard `Shape` interface, enabling compatibility with other shapes without modifying the original `XXCircle` class.
- **Unified Operations**: By adhering to the `Shape` interface, operations like `display`, `fill`, and `undisplay` are consistent across all shape types, simplifying the code.
- **Extensibility**: The Adapter pattern allows for future integration of additional legacy or third-party shapes with unique interfaces, simply by adding new adapters.
- **Encapsulation of Legacy Code**: `CircleAdapter` encapsulates the original `XXCircle` functionality, minimizing dependencies on the legacy interface while preserving its behavior.

## Purpose and Lessons Learned

Through this project, I learned how the Adapter pattern enables compatibility between incompatible interfaces, particularly when integrating legacy or third-party code into new systems. By creating the `CircleAdapter`, I saw how the Adapter pattern acts as a bridge, allowing `XXCircle` to be used alongside other shapes without modifying its code. This approach enhanced my understanding of flexible software design, especially when dealing with legacy systems.
