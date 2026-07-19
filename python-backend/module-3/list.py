# In python Array , Linklist , Stack , Queue  All are represented as List 

#  =================================== Stack ===============================================================

#  FILO => First In Last Out

# arr = [1,2,3,4]

# arr.append(5)

# print(arr)

# arr.pop()

# print(arr[len(arr) - 1])
# print(arr[-1])
# print(arr[-2])


# ========================================= Queue ==========================================================

# FIFO

# First IN First Out

# arr = [1,2,3,4]

# # arr.pop(0)
# arr.insert(1,10)
# print(arr)


#  ========================================== Set ===========================================================
# Set is like list but it can't contain duplicate

# How computer which is duplicate in set

# example 

#  my_tuple = (1) => this is init class
# my_tuple = (1,) => This is tuple class

my_tuple = tuple()
my_tuple = (1,2,3,[4,5,6,7])

print(my_tuple[3].extend([10,11])) # we can add data to list not at tuple (here inside tuple we add the data)

print(my_tuple)



#  ======================= How to define list ====================================== 

# my_list = list([1,2,3]) # one way

#  Another way  to define my list
# my_list = [1,2,3,4]
# my_list2 = [7,8,9,10]

# # my_list.append(my_list2)  # output will be [1,2,3,4,[7,8,9,10]]

# my_list.extend(my_list2) # output will be [1,2,3,4,7,8,9,10]

# print(my_list)


# ======================== Slice =============================================
# It create sallow copy don't change the original array
# my_list = [1,2,3,4,5]
# List[start:stop:step]
# print(my_list[::-1]) # reverse arrray

# my_list = [10, 20, 30, 40]
# chunk = my_list[1:3]

# print(chunk)   # Output: [20, 30]
# print(my_list) # Output: [10, 20, 30, 40] (Unchanged)


# ====================== Splice ===============================================

# It modify the original array

# my_list = [1,2,3,4,5,6]

# chunk = my_list[1:4]= [23,56]
# print(chunk)
# print(my_list)


