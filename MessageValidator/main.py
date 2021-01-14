def is_a_valid_message(message):
    # split message for single char
    # check if first char is number (marked as n)
    # then check n-times if next chars are not the numbers
    # if any codition is false I return False
    # if every condition will be true I returned True
    spl_message = list(message)
    jump = 1
    i = 0
    while i < len(spl_message):
        i += 1
        print('letter', spl_message[i])
        if spl_message[i].isdigit():
            print('jump', jump)
            jump = int(spl_message[i])
            for k in range(i+1, int(spl_message[i])):
                if spl_message[k].isdigit():
                    print('1:')
                    return False
        else:
            print('2:')
            return False
    return True

    # your code
    # pass


print(is_a_valid_message("3pey5kello2ki"), True)
#print(is_a_valid_message("4code13hellocodewars"), True)
#print(is_a_valid_message("code4hello5"), False)
#print(is_a_valid_message("1a2bb3ccc4dddd5eeeee"), True)
#print(is_a_valid_message(""), True)
# print(type(int('n')))
#print(isinstance('n', 3), 'siema')
# print(int('n'))
