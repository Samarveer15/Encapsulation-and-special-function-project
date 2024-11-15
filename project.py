class Reverse:
    def __init__(self, string=""):
        self.string = string

    def reverse_string(self):
        return self.string[::-1]


user_input = input("Enter a string: ")


reverse_obj = Reverse(user_input)


print(f'The reversed string is: {reverse_obj.reverse_string()}')

