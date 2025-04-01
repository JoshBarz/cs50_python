def main():
    mass = int(input("mass: "))
    energy(mass)


def energy(mass):
    c = 300000000 * 300000000
    energy = c * mass
    print(f"energy {energy}")

main()

