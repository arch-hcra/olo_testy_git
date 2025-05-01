def compare_numbers(nu1, nu2):
    if nu1[0] == nu2[0]:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    print("checks nums")
    nu1 = input("in nums №1: ")
    nu2 = input("in nums №2: ")
    result = compare_numbers(nu1, nu2)
    print(result)
