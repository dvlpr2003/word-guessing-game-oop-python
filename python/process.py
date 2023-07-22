import random


class function:
    def __init__(self, data):
        self.exit_list = data

        self.dash = 0
        self.empty_list = []
        self.empty_list2 = []
        self.string_convert = ""
        self.index_numbers = []
        self.final_string = []

    def word_guessing(self):
        option = True
        choose_word = random.choice(self.exit_list)
        # self.empty_list2.append(choose_word)
        choose_mode = int(input("Select mode:\n1.Easy\n2.Intermediate\n3.Hard\n"))
        if choose_mode == 1:
            print("You are in Easy mode: ")
            self.dash = 1
        elif choose_mode == 2:
            print("You are in Intermediate mode: ")
            self.dash = 2

        elif choose_mode == 3:
            print("You are in Hard mode: ")
            self.dash = 3

        else:
            print("Please select valid mode: ")
        for letters in choose_word:
            self.empty_list.append(letters)
            self.empty_list2.append(letters)

        for i in range(0, self.dash):
            length = len(self.empty_list)
            self.empty_list[random.randint(0, length - 1)] = "_"
        # print(self.empty_list)
        for convert in self.empty_list:
            self.string_convert += convert
        for finding_index in range(0, self.dash):
            j = self.empty_list.index("_")

            self.empty_list[j] = "x"

            self.index_numbers.append(j)

        # print(self.index_numbers)

    def user_operation(self):
        print(self.string_convert)
        final_string = ""

        for i in range(0, self.dash):
            if self.dash == 1:
                user_input_index = int(
                    input("choose index, you want to insert element : ")
                )
            elif self.dash == 2:
                user_input_index = int(
                    input("choose index, you want to insert element (1)(2): ")
                )

            elif self.dash == 3:
                user_input_index = int(
                    input("choose index, you want to insert element (1)(2)(3): ")
                )
            user_letter = input("Enter your letter :").casefold()
            n_number = self.index_numbers[user_input_index - 1]
            # print(n_number)

            if user_letter == self.empty_list2[n_number]:
                self.empty_list[n_number] = user_letter

            elif user_letter != self.empty_list2[n_number]:
                self.empty_list[n_number] = user_letter
                print("Invalid letter! ")
        for final in self.empty_list:
            final_string += final
        print(final_string)

        if self.empty_list == self.empty_list2:
            print("Hey! you win the game.")
        else:
            print("You loose, Please try again later.")
