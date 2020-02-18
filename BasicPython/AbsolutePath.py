def absolutefilepath(pathfname):
    import os
    return os.path.abspath("pathfname")
print("Absolute file path:",absolutefilepath("primeFactorization.py"))