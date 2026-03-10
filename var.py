# Global variable
x = 100

def outer_function():
    # Enclosing variable (local to outer_function, but enclosing for inner_function)
    y = 50

    def inner_function():
        # Local variable (local to inner_function)
        z = 25

        # Accessing enclosing variable using nonlocal
        nonlocal y
        y = y + 10  # modifies enclosing variable

        # Accessing global variable
        global x
        x = x + 5   # modifies global variable

        # Built-in variable (using len, a built-in function)
        name = "Guru"
        print("Length of name (builtin function):", len(name))

        print("Local z:", z)
        print("Enclosed y (after change):", y)
        print("Global x (after change):", x)

    inner_function()
    print("Outer function y:", y)

outer_function()
print("Outside all functions, global x:", x)
