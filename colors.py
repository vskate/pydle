# colors controlled by ANSI escape codes

def green():
    print("\033[32m", end="")

def yellow():
    print("\033[93m", end="")

def red():
    print("\033[31m", end="")

def clear_screen():
    print("\033[H\033[J", end="")

def reset():
    print("\033[0m", end="")
