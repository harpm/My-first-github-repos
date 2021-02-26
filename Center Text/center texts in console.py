

def center_expression(*args, sep=" "):
    text = ""

    for arg in args:
        text += arg + sep
        pass

    for temp in text.split(" "):
        if len(temp) > 80:
            print("-" * 40)
            print("\nYou piece of shit what kind of word have you entered!\n"
                  "Really a word with more than 80 chars 😐\n"
                  "I'm sure you are a jerk, mother fucker\n")
            print("-" * 40)
            return

    for t in text.splitlines():
        exp_list = [t]
        if len(t) >= 80:
            exp_list = list()

            while len(t) > 80:
                new_item = split_by_n(t)
                exp_list.append(new_item)

                t = clear_first_n(t, len(new_item))

                pass

            exp_list.append(t)
            pass

        for item in exp_list:
            space_no = (85 - len(item)) // 2
            print(" " * space_no + item, end="\n")
            pass

        pass

    pass


def clear_first_n(text, limit):
    temp_text = ""

    for i in range(0, len(text) + 1):
        if i <= limit:
            continue

        temp_text += text[i - 1]
        pass

    return temp_text


def split_by_n(exp, limit=80):
    exp = str(exp)

    if len(exp) < limit:
        return

    returning_text = ""

    for t in exp.split(" "):
        returning_text += " " + t

        if len(returning_text) >= limit:
            break

    return returning_text


expression = input("Please enter a valid expression so I'll center it and print it for you(note: type '\"' to end the "
                   "expression): \n\"") + "\n"

while expression[len(expression) - 2] != '"':
    expression += input() + "\n"

print("\nThe Result is: \n")
expression = expression[0:-2:1]
center_expression(expression)
