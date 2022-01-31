
def cheat(exercise):
    """
    This definition gives answers to first four questions of the 
    Assignment 1.2P. Input is the exercise number (1,2,3,or 4) and output
    is the solution to that exercise.
    """
    if exercise < 1 or exercise > 4 or exercise%1 > 0:
        print("Enter 1,2,3 or 4")
    elif exercise == 1:
        print("import numpy as np")
    elif exercise == 2:
        print("pickElement = another_array[0, 3, -1]  # 1st of 1st dimension, 4th of 2nd dimension, last of 3rd dimension "
              "firstFirst = another_array[0, 0, 0]  # first element, first dimension "
              "fourthSecond = another_array[0, 3, 0]  # fourth element, second dimension "
              "lastThird = another_array[0, 0, -1]  # last element, third dimension")
    elif exercise == 3:
        print("another_array = np.zeros((2, 4, 6)) "
              "new_array = another_array  # instead, use another_array.copy()"
              "new_array[1, 2, 2] = 1"
              "print(another_array[1, 2, 2])")
    else:
        print("%paste does not work in script since it's a Magic command specific to and provided by the IPython kernel.")

