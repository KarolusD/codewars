def flip(d,a):
    #1.if statement for direction
#2.sort array from left to right or rightto left
#3. return array
    if d=='R':
        return a.sort(reverse=True)
    elif d=='L':
            return a.sort()





print(flip('R', [3, 2, 1, 2]), [1, 2, 2, 3]);
print(flip('L', [1, 4, 5, 3, 5]), [5, 5, 4, 3, 1]);