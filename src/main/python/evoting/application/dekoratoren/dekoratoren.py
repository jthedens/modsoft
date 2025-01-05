import functools

# Logging-Dekorator
def log_method_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Aufruf der Methode: {func.__name__}, args: {args[1:]}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Ergebnis der Methode: {result}")
        return result
    return wrapper

# Fehlerbehandlungs-Dekorator
def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Ausnahme in Methode {func.__name__}: {e}")
            return {"error": str(e)}
    return wrapper
