def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    new_lst = lst[1:len(lst)-1]
    print (new_lst)

middle([1, 2, 3, 4, 5])