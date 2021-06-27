def chuck_push_ups(st):
    if st == '' or type(st) != str:
        return 'FAIL!!'

    arr = st.split()
    highest = 0
    is_num = False

    for item in arr:
        nums_only = ''.join(c for c in list(item) if c == '0' or c == '1')
        print(nums_only)
        if nums_only != '':
            is_num = True
            if highest < int(nums_only):
              highest = int(nums_only)
        else:
            continue

    return int(str(highest), 2) if is_num else 'CHUCK SMASH!!'


print(chuck_push_ups(
    'p^KZe"F, 270496 &'), 3244)
# print(chuck_push_ups('1000 "Did you kick someone in the face today?" 1001 1010 "Will I be making dinner then?!" 1011 110') == 11)
# print(chuck_push_ups(
#     '10000 "Nice Beard" 1111 "Are you wearing denim shorts?" 1110 1101') == 16)
# print(chuck_push_ups('') == 'FAIL!!')
# print(chuck_push_ups([]) == 'FAIL!!')
# print(chuck_push_ups(1) == 'FAIL!!')
