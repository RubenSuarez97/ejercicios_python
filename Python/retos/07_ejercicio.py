def check(palabra1: str, palabra2: str):
    # Palindromes
    print(f"{palabra1} es un palindrome ? {palabra1 == palabra1[::-1]}")
    print(f"{palabra2} es un palindrome ? {palabra2 == palabra2[::-1]}")

    # Anagramas
    print(f"{palabra1} en anagrama de {palabra2} ?: {sorted(palabra1) == sorted(palabra2)}")

    # Isogramas

    print(f"{palabra1} es un isograma?: {len(palabra1) == len(set(palabra1))}")
    print(f"{palabra2} es un isograma?: {len(palabra2) == len(set(palabra2))}")



check('radar', 'python')
check('amor', 'roma')


