# for i in range(20):
#     print(i)
# ------------------------------
# for i in "Hello World!":
#     print(i)
# ------------------------------
# def print_list(lst):
#     for string in lst:
#         print(string)
        
# print_list(["a","b","c"])
# ------------------------------
# def print_gt3(lst):
#     for item in lst:
#         if item > 3:
#             print("😃 num is grater than 3")
#         else:
#             print("😒 num is less than 3")
# print_gt3([1,2,3,4])
# ------------------------------
def print_add3(lst=3):
    lsttype = type(lst)
    if lsttype is not list and lsttype is not int:
        return print("Please enter number or list of numbers only 🥹")
    if lsttype is list:
        for i in lst:
            print(i+3)
    elif lsttype is int:
        print(int(lst)+3)
print_add3(5)
print_add3([5,6])
print_add3()
print_add3("omkar")
print_add3({"k1":"omkar", "k2":"Sanskruti"})