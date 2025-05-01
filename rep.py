def compare_numbers(nu1, nu2):
    if not isinstance(nu1, int) or not isinstance(nu2, int):
        raise ValueError("Inputs must be integers")
    
    return "Yes" if nu1 == nu2 else "No"

if __name__ == "__main__":
    print("checks nums")
    try:
        nu1 = int(input("in nums №1: "))
        nu2 = int(input("in nums №2: "))
        result = compare_numbers(nu1, nu2)
        print(result)
    except ValueError:
        print("Error: Please enter valid integers.")
