import functools

# Logging-Dekorator
def log_method_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Aufruf der Methode: {func.__name__}, args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
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
