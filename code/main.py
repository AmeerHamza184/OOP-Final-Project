# OOP Final Project: requests Library Analysis
# Course: BS Data Science (Semester 2) | Submitted to: Dr Akmal Khan 
# Group Members: Ameer Hamza, Humayon Zahid, Fahad Iqbal, Rehman Ali Chattha

import requests
import time

class CustomLoggingSession(requests.Session):
    """
    A custom subclass of requests.Session that automatically 
    calculates and prints the execution time of every HTTP request.
    """

    def __init__(self, *args, **kwargs):
        # INHERITANCE: Calling the parent constructor so that all default session 
        # features (cookies, headers, connection pooling) are initialized correctly.
        super().__init__(*args, **kwargs)
        print("[INIT] CustomLoggingSession initialized successfully.")

    def send(self, request, **kwargs):
        """
        POLYMORPHISM: Overriding the core send() method to inject our own logic 
        before and after the request goes out to the network.
        """
        # ENCAPSULATION: Printing basic request info directly inside the method 
        # without changing or exposing any internal session attributes.
        print(f"\n[SENDING] Request to URL: {request.url} | Method: {request.method}")

        # Save the timestamp right before sending the request
        start_time = time.time()

        # Forward the request to the parent class using super().send() 
        # so the built-in networking logic works normally.
        response = super().send(request, **kwargs)

        # Calculate the time difference after receiving the response (Latency check)
        elapsed_time = time.time() - start_time

        print(f"[RESPONSE] Status Code: {response.status_code} | Taken: {elapsed_time:.4f} seconds")

        # Return the original, unmodified response object back to the caller
        return response


if __name__ == "__main__":
    print("=" * 60)
    print("  OOP Final Project — Custom Extension Demonstration")
    print("  Library: requests | Class: CustomLoggingSession")
    print("=" * 60)

    # Using a context manager ('with') to make sure the session closes automatically
    with CustomLoggingSession() as session:
        try:
            # Using a free public API endpoint to test the session
            url = "https://jsonplaceholder.typicode.com/todos/1"
            
            # session.get internally triggers our overridden send() method
            response = session.get(url)
            todo_data = response.json()

            print("\n" + "─" * 60)
            print("  Fetched Real-World API Response")
            print("─" * 60)
            print(f"  Todo Title   : {todo_data.get('title')}")
            print(f"  Completed    : {todo_data.get('completed')}")
            print(f"  User ID      : {todo_data.get('userId')}")
            print("─" * 60)

        except requests.exceptions.ConnectionError:
            # Handles network failure gracefully instead of letting the script crash
            print("[ERROR] Network unreachable. Please check your connection.")

        except requests.exceptions.Timeout:
            # Handles cases where the server takes too long to respond
            print("[ERROR] Request timed out. The server did not respond.")

        except Exception as e:
            # Catch-all block for any other unexpected error to avoid hard crashes
            print(f"[ERROR] An unexpected error occurred: {e}")