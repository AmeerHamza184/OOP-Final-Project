# Architectural Analysis & Custom Extension of Python 'requests' Library

## 👥 Group Members & Project Details
* **Ameer Hamza** (Lead)         -- F25BDATS1M02077
* **Humayon Zahid** -- F25BDATS1M02064
* **Fahad Iqbal** -- S25BDATS1E01001
* **Rehman Ali Chattha** -- F25BDATS1M02068

### 📚 Academic Context
* **Academic Program:** BS Data Science (Semester 2)
* **Course:** Object-Oriented Programming (OOP) Final Term Project
* **Instructor:** Dr. Akmal Khan

---

## 1. Library Overview (Rubric Component - 10 Marks)
The Python `requests` library is an elegant, user-friendly HTTP client built on top of `urllib3`. While it simplifies networking for developers, its underlying architecture relies heavily on solid Object-Oriented design patterns. 

Our project focuses on dissecting the design patterns of `requests`, specifically analyzing how it manages connection pooling, session states, and abstracting network complexities away from the end user.

---

## 2. Class Hierarchy & Architectural Diagram (Rubric Component - 15 Marks)
To understand the structural composition of the library and our extension, we have mapped out the core class relationships. Below is the verified architectural UML class diagram demonstrating inheritance boundaries and method overriding points:

![UML Class Diagram](diagrams/uml_diagram.png)

*Note: In case the image doesn't render natively, the physical hand-drawn diagram is securely hosted inside the `/diagrams` directory of this repository.*

---

## 3. Core OOP Principles Analyzed (Rubric Component - 15 Marks)
Our custom implementation bridges the gap between raw library behaviors and custom business logic by successfully leveraging all four core pillars of Object-Oriented Programming:

1. **Inheritance:** Our custom class `LoggedSession` extends the core `requests.Session` class, instantly gaining full access to connection pooling, cookies, and HTTP verb methods.
2. **Polymorphism:** We override the standard central `.request()` method. Since high-level methods like `.get()` and `.post()` internally route through `.request()`, our logging logic intercepts all types of HTTP traffic seamlessly.
3. **Encapsulation:** The request history is safely stored within a private internal array `self._log`. Direct mutation from the outside runtime environment is restricted, exposing only a secure copy via the `get_log()` getter method.
4. **Abstraction:** Complex table formatting and metrics evaluation logic are encapsulated cleanly inside `show_log()` and `summary()` interfaces, letting the user manage session logs with minimal cognitive load.

---

## 4. Custom Extension Implementation (Rubric Component - 20 Marks)
The source code located inside the `/code/main.py` directory serves as a production-grade wrapper for automated API monitoring.

### Key Features Implemented:
* **Performance Tracking:** Measures real-time connection latency and execution timers for every request.
* **Failure Analytics:** Dedicated error isolation through custom status monitoring (`get_failed()`).
* **Clean Interface:** Human-readable terminal reporting engine for rapid API debugging.

### Quick Start / Demo Execution
To execute the working demonstration and verify the custom extension logic locally, run:
```bash
python code/main.py