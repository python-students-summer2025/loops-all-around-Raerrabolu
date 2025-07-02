def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            else:
                print("Please enter a number greater than or equal to 1.")
        except ValueError:
            print("That's not a valid number. Try again.")

def sing(start_bottles):
    bottles = start_bottles
    while bottles > 0:
        if bottles == 1:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        else:
            next_bottles = bottles - 1
            bottle_word = "bottles" if next_bottles != 1 else "bottle"
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {next_bottles} {bottle_word} of beer on the wall!\n")
        bottles -= 1
