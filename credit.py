from cs50 import get_string
def main():
    card_number = get_string("What the credit card number? ")
    print_card_flag(card_number)


def print_card_flag(card_number):
    if checksum(card_number) == False:
        print('INVALID')
    elif checkamex(card_number) == True:
        print("AMEX")
    elif checkmaster(card_number) == True:
        print("MASTERCARD")
    elif checkvisa(card_number) == True:
        print("VISA")
    else:
        print("INVALID")

def checkamex(card_number):
    if len(card_number) == 15 and card_number[:2] in ['34', '37']:
        return True
    else:
        return False

def checkmaster(card_number):
    if len(card_number) == 16 and card_number[:2] in ['51', '52', '53', '54', '55']:
        return True
    else:
        return False

def checkvisa(card_number):
    if len(card_number) in [13, 16] and card_number[0] == '4':
        return True
    else:
        return False

def checksum(card_number):
    not_mult_two_sequence = 0
    mult_two_sequence = 0

    mult_two_digits_array = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    for i in range(len(card_number)):
        curr_num = int(card_number[len(card_number) - 1 - i])
        if i % 2 == 0:
            not_mult_two_sequence += curr_num
        else:
            mult_two_sequence += mult_two_digits_array[curr_num]

    total_sum = not_mult_two_sequence + mult_two_sequence
    return ((total_sum % 10) == 0)


main()

