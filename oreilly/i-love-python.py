def i_love_python():
    """
    I'm not sure why I love Python, but I do.
    1. Zen of Python
        I've never seen a language that encouraged coding best practices. In
        other languages, it seems like line count and performance are more
        important, not readability or ease of debugging. This gives me hope
        that the entry point is not nearly as high.
    2. I love that there is a defined style guide for Python code.
    3. It runs practically everywhere!
    4. Python code just makes sense to me.
    5. Python is accessable.
    """
    return "I love Python!"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
