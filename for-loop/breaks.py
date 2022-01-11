# for i in range(5):
#     for o in range(5):
#         if o % 2 == 0:
#             print("Continue in the loop since ", o, " is even")
#             continue
#         print("i=", i, " o=", o)
#
# print(" --- ")
#
# for i in range(5):
#     for o in range(1,5):
#         if o % 2 == 0:
#             print("Break the loop")
#             break
#         print("i=", i, " o=", o)
#
for i in range(5):
    print("i is now ", i)
    if i == 6:
        print("Break the loop")
        break
else:
    print("We did not break the loop!!!")
