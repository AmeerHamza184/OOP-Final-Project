import requests
import time

# Inheritance: Extending core Session class to inject custom behavior
class LoggedSession(requests.Session):
    """
    Custom wrapper around requests.Session to track request metrics.
    Demonstrates structural integration of all 4 core OOP principles.
    """

    def __init__(self):
        super().__init__()
        # Encapsulation: Restricting direct access to logs to preserve integrity
        self._log = []
        print("[INIT] LoggedSession ready.")

    # Polymorphism: Overriding core request method to capture all HTTP verbs
    def request(self, method, url, **kwargs):
        print(f"\n[LOG] {method.upper()} -> {url}")
        
        start = time.time()
        response = super().request(method, url, **kwargs)
        elapsed = time.time() - start

        # Internal state tracking
        self._log.append({
            "method"  : method.upper(),
            "url"     : url,
            "status"  : response.status_code,
            "time_sec": round(elapsed, 4),
            "ok"      : response.ok
        })
        
        print(f"[DONE] Status: {response.status_code} | Time: {elapsed:.4f}s")
        return response

    # Encapsulation: Getter method providing a safe boundary copy of internal data
    def get_log(self):
        return self._log.copy()

    # Abstraction: Exposing interface to user while hiding raw formatting logic
    def show_log(self):
        print("\n" + "="*60)
        print(f"{'#':<4}{'METHOD':<8}{'STATUS':<8}{'TIME(s)':<10}URL")
        print("="*60)
        for i, e in enumerate(self._log, 1):
            mark = "OK" if e["ok"] else "FAIL"
            print(f"{i:<4}{e['method']:<8}{str(e['status'])+' '+mark:<8}{e['time_sec']:<10}{e['url']}")
        print("="*60)

    def get_failed(self):
        return [e for e in self._log if not e["ok"]]

    def summary(self):
        total = len(self._log)
        ok    = sum(1 for e in self._log if e["ok"])
        print(f"\nSummary: {ok}/{total} successful | {total-ok} failed")

    def clear_log(self):
        self._log = []


if __name__ == "__main__":
    print("--- OOP Final Project -- Custom Extension Demo ---")

    with LoggedSession() as session:
        try:
            session.get("https://jsonplaceholder.typicode.com/todos/1")
            session.post("https://jsonplaceholder.typicode.com/posts")
            session.get("https://httpbin.org/status/404")

            session.show_log()

            print("\nFailed Requests:")
            for r in session.get_failed():
                print(f"  {r['method']} {r['url']} -> Status {r['status']}")

            session.summary()

        except Exception as e:
            print(f"[ERROR] Request failed: {e}")