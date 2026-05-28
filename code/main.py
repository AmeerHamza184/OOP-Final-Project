"""
working.py -- OOP Final Term Project
Custom Extension of the requests library

Group Members:
  Ameer Hamza        -- F25BDATS1M02077
  Humayon Zahid      -- F25BDATS1M02064
  Fahad Iqbal        -- S25BDATS1E01001
  Rehman Ali Chattha -- F25BDATS1M02068
"""

import requests
import time

# 1. INHERITANCE -- LoggedSession extends requests.Session
class LoggedSession(requests.Session):
    """
    Custom extension of requests.Session.
    Adds automatic logging AND execution time tracking.
    Demonstrates all 4 OOP principles.
    """

    def __init__(self):
        super().__init__()           # Inheritance -- parent init
        self._log = []               # Encapsulation -- private attribute
        print("[INIT] LoggedSession ready.")

    # 2. POLYMORPHISM -- override request() method
    def request(self, method, url, **kwargs):
        """Override to add logging + execution time tracking."""
        print(f"\n[LOG] {method.upper()} -> {url}")
        start = time.time()
        response = super().request(method, url, **kwargs)
        elapsed = time.time() - start

        # 3. ENCAPSULATION -- stored privately in _log
        self._log.append({
            "method"  : method.upper(),
            "url"     : url,
            "status"  : response.status_code,
            "time_sec": round(elapsed, 4),
            "ok"      : response.ok
        })
        print(f"[DONE] Status: {response.status_code} | Time: {elapsed:.4f}s")
        return response

    def get_log(self):              # Getter -- Encapsulation
        """Return a copy of the private log."""
        return self._log.copy()

    def show_log(self):             # 4. ABSTRACTION -- hides internal detail
        """Print all requests in a readable table format."""
        print("\n" + "="*60)
        print(f"{'#':<4}{'METHOD':<8}{'STATUS':<8}{'TIME(s)':<10}URL")
        print("="*60)
        for i, e in enumerate(self._log, 1):
            mark = "OK" if e["ok"] else "FAIL"
            print(f"{i:<4}{e['method']:<8}{str(e['status'])+' '+mark:<8}{e['time_sec']:<10}{e['url']}")
        print("="*60)

    def get_failed(self):           # Extra meaningful method
        """Return only the failed requests (status >= 400)."""
        return [e for e in self._log if not e["ok"]]

    def summary(self):              # Extra meaningful method
        """Print a quick summary of total, success, and failed."""
        total = len(self._log)
        ok    = sum(1 for e in self._log if e["ok"])
        print(f"\nSummary: {ok}/{total} successful | {total-ok} failed")

    def clear_log(self):
        """Clear all stored log entries."""
        self._log = []


# DEMO BLOCK -- Required by Rubric
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