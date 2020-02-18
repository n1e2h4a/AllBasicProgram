import os
print("\nEffective group id: ",os.getegid())
print(" Effective group id: ",os.geteuid())
print("\nEffective group id: ",os.getgid())
print("group of supplemental group ids: ",os.getgroups())
print()