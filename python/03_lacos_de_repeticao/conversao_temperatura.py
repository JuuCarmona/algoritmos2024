print("celsius\t\tfahrenheit")
print("-" * 24)

for celsius in range (0,101,10):

    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}\t\t{fahrenheit:.2f}")
