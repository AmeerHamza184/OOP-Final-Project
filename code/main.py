import requests
import time

# 1. INHERITANCE: We are inheriting from the core 'Session' class of requests library
class CustomLoggingSession(requests.Session):
    """
    A custom extension of requests.Session that automatically logs 
    the execution time and status code of every HTTP request.
    This demonstrates the OOP principles of Inheritance and Method Overriding.
    """
    
    def __init__(self, *args, **kwargs):
        # Calling the parent class constructor using super()
        super().__init__(*args, **kwargs)
        print("[INIT] CustomLoggingSession initialized successfully.")

    # 2. METHOD OVERRIDING: Overriding the parent class 'send' method
    def send(self, request, **kwargs):
        """
        Overrides the standard send() method to inject custom logging functionality.
        """
        print(f"\n[SENDING] Request to URL: {request.url} | Method: {request.method}")
        
        # Recording start time to measure performance
        start_time = time.time()
        
        # Calling the original send method of the parent class (Polymorphism & Reusability)
        response = super().send(request, **kwargs)
        
        # Calculating total elapsed time
        elapsed_time = time.time() - start_time
        
        print(f"[RESPONSE] Status Code: {response.status_code} | Taken: {elapsed_time:.4f} seconds")
        return response

# 3. DEMO BLOCK: Showing the custom extension in action (Required by Rubric)
if __name__ == "__main__":
    print("--- Testing Custom Extension for OOP Final Project ---")
    
    # Instantiating the custom subclass object
    with CustomLoggingSession() as session:
        try:
            # Using a real-world public mock API that returns sample user/todo data
            # This simulates fetching real data from a production server
            url = "https://jsonplaceholder.typicode.com/todos/1"
            response = session.get(url)
            
            # Checking JSON decoding to prove the session works normally
            todo_data = response.json()
            print("\n--- Fetched Real-World API Response Data ---")
            print(f"Todo Title: {todo_data.get('title')}")
            print(f"Completed Status: {todo_data.get('completed')}")
            print("--------------------------------------------")
            
        except Exception as e:
            print(f"[ERROR] Request failed: {e}")