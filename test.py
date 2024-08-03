vstup = "10.5"

try:
    vstup = int(vstup) * -1
except ValueError:
    vstup = float(vstup) * -1

print(vstup)
