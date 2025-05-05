def search(P, T):
    # Constants
    d = 256  # Number of characters in the input alphabet (ASCII)
    q = 101  # A prime number for the modulus
    
    m = len(P)
    n = len(T)
    p_hash = 0  # Hash value for the pattern
    t_hash = 0  # Hash value for the text
    h = 1
    
    # The value of h would be "pow(d, m-1)%q"
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of the pattern and the first window of the text
    for i in range(m):
        p_hash = (d * p_hash + ord(P[i])) % q
        t_hash = (d * t_hash + ord(T[i])) % q
    
    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # If hash values match, then only check the characters one by one
        if p_hash == t_hash:
            # Check the characters one by one
            if T[i:i + m] == P:
                print(f"Pattern found at index {i}")

        # Calculate hash value for the next window of text
        if i < n - m:
            t_hash = (d * (t_hash - ord(T[i]) * h) + ord(T[i + m])) % q

            # We might get negative value of t_hash, so we convert it to positive
            if t_hash < 0:
                t_hash = t_hash + q

# Test the function with examples
T1 = "THIS IS A TEST TEXT"
P1 = "TEST"
search(P1, T1)

print()  # For separating different test case outputs

T2 = "AABAACAADAABAABA"
P2 = "AABA"
search(P2, T2)
