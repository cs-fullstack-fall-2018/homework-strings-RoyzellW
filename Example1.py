# 1. What is the error message returned when you improperly use quotes inside of strings?

#SyntaxError: EOL while scanning string literal

# 2. Provide an example and explain the error message.

    print("I like pie.')
        # EOL stands for end of the line when going through a string.
        # It's because you forgot ending quotes, mismatched quotes, or because you tried to make a string extend past one line.

