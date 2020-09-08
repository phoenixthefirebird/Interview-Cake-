# has a small probability of never returning 
# in fact, no solution exists that would guarantee returning
# give rand7() random integer generator between 1 and 7

def rand5():
    result = 7  # arbitrarily large
    while result > 5:
        result = rand7()
    return result
