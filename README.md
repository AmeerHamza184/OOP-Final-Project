# Architectural Analysis & Custom Extension of Python 'requests' Library

## 👥 Group Members & Project Details
* **Ameer Hamza (Lead)** — F25BDATS1M02077
* **Humayon Zahid** — F25BDATS1M02064
* **Fahad Iqbal** — S25BDATS1E01001
* **Rehman Ali Chattha** — F25BDATS1M02068

## 📚 Academic Context
* **Academic Program:** BS Data Science (Semester 2)
* **Course:** Object-Oriented Programming (OOP) Final Term Project
* **Instructor:** Dr. Akmal Khan
* **Date:** 30 May 2026

---

## 1. Library Overview
The Python `requests` library is an elegant, user-friendly HTTP client built on top of `urllib3`. While it simplifies networking for developers, its underlying architecture relies heavily on solid Object-Oriented design patterns. Our project focuses on dissecting the design patterns of `requests`, specifically analyzing how it manages connection pooling, session states, and abstracting network complexities away from the end user.

---

## 2. Class Hierarchy & Architectural Diagram
To understand the structural composition of the library and our extension, we have mapped out the core class relationships. Our hand-drawn UML class diagram demonstrating inheritance boundaries and method overriding points is embedded directly inside our comprehensive final report document.

### 📄 Final Project Deliverable
Our complete 15-page final project report, architectural analysis, and diagrams have been successfully compiled into a professional PDF. You can view or download the final document here:
* 📁 **[Final Project Report (PDF)](report/Requests_OOP_Analysis_Final.pdf)**

---

## 3. Core OOP Principles Analyzed
Our custom implementation bridges the gap between raw library behaviors and custom metrics by successfully leveraging the core pillars of Object-Oriented Programming:

* **Inheritance:** Our custom class `CustomLoggingSession` extends the core `requests.Session` class, instantly gaining full access to connection pooling, cookies, and HTTP verb methods without rewriting any code.
* **Polymorphism:** We override the standard central `send()` method. By utilizing method overriding, our custom session intercepts network requests transparently to inject our timing wrappers while keeping the original method contract intact.
* **Encapsulation:** The latency and execution logging operations are entirely enclosed within the overridden method scope. The application handles complex calculations internally without exposing internal state attributes to outside callers.
* **Abstraction:** The underlying structural complexity—such as creating a `PreparedRequest`, socket connections, and managing stream timeouts—is hidden behind simple interfaces like `session.get()`, reducing cognitive load for the developer.

---

## 4. Custom Extension Implementation
The source code located in the main directory serves as a practical demonstration of automated API latency monitoring.

### Key Features Implemented:
* **Performance Tracking:** Measures real-time connection latency and execution timers for every request.
* **Transparent Wrappers:** Works as a drop-in replacement for standard sessions without modifying client-side HTTP call methods.
* **Clean Interface:** Human-readable terminal reporting engine for rapid API tracking and monitoring.

### Quick Start / Demo Execution
To execute the working demonstration and verify the custom extension execution logs locally, run the main script:
```bash
python main.py