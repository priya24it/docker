# example.py

def add(a, b):
    print(a + b)
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print(f"3 + 2 = {add(3, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
