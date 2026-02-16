list1=[1,2,1]
list2=[1,2,3]
copy_list1=list.copy(list1)
copy_list1.reverse
if list1==copy_list1:
    print("palindrome")
else:
    print("not palindrome")