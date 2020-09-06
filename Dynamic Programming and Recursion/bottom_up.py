# top-down, recursive approach of factorial
def product_1_to_n(n):
    # We assume n >= 1
    return n * product_1_to_n(n - 1) if n > 1 else 1
    
# bottom-up approach
def product_1_to_n(n):
    # We assume n >= 1
    result = 1
    for num in range(1, n + 1):
        result *= num

    return result
