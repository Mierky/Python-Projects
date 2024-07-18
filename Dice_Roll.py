import random

def draw_die_face(number, width):
    border = '-' * (width + 2)
    padding = ' ' * (width - len(str(number)))
    middle_line = f"|{padding}{number}{padding}|"

    print(border)
    print(middle_line)
    print(border)
def roll_dice(faces,nr):
    dice = [random.randint(1,faces) for _ in range(nr)]

    print("Dice rolled: ")

    for nr,die in enumerate(dice):
        print(f"## Dice {nr+1} ##")
        draw_die_face(die, len(str(die)))


if __name__ == '__main__':
    roll = input("Roll the dice? (Yes/No)")
    while roll.lower().strip() == 'Yes'.lower().strip():
        faces = int(input("How many faces should the die have?"))
        nr = int(input("How many dice?"))
        roll_dice(faces,nr)

        roll = input("Roll again? (Yes/No)")