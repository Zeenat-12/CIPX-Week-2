from random import randint

def main():
    print("Khansole Academy")

    correct_in_a_row = 0
    num_problems = 0
    num_correct = 0

    while correct_in_a_row < 3:
        # Generate two random numbers
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        # Prompt the user with the problem
        print(f"What is {num1} + {num2}?")
        user_ans = int(input("Your answer: "))
        true_ans = num1 + num2
        num_problems += 1

        if user_ans == true_ans:
            print("Correct!")
            correct_in_a_row += 1
            num_correct += 1
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            print("Incorrect.")
            correct_in_a_row = 0
            print(f"The expected answer is {true_ans}")
        print()

    print("Congratulations! You mastered addition.")

    # Show how the whole practice went
    print(f"You tried {num_problems} problems and got {num_correct} right.")

if __name__ == '__main__':
    main()
