words = input().split()

print("\n".join(el for el in words if len(el) % 2 == 0))
