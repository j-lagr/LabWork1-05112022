random_list = [3, 1, 15, 19, 7, 25, 1, 3, 1, 99]


def menu():
    print("\n     List/Array: ", random_list,"       \n"
          "__________________________________________________________")
    print("|                  List / Array Modifier                 |")
    print("----------------------------------------------------------")
    print("|   1  -> Print the list elements per line               |"
          "\n|   2  -> Add an element                                 |"
          "\n|   3  -> Insert an element                              |"
          "\n|   4  -> Modify an element                              |"
          "\n|   5  -> Delete an element                              |"
          "\n|   6  -> Arrange in ascending order                     |"
          "\n|   7  -> Arrange in descending order                    |"
          "\n|   8  -> Identify the smallest element                  |"
          "\n|   9  -> Identify the largest element                   |"
          "\n|   10 -> Get the sum of all the elements                |"
          "\n|   11 -> Determine the number of elements in the array  |"
          "\n|   12 -> Get the number of times an element appeared    |"
          "\n|   13 -> Exit                                           |"
          "\n__________________________________________________________")

def yesno():
    while True:
        decide= input("Do you want to go back to the menu? ( Y / N ): ")
        if decide == "Y":
            menu()
            break
        elif decide == "N":
            print("Thank you for using the List/Array Modifier!")
            exit()
        else:
            print("WRONG INPUT! The program is case sensitive.")

def printlist():
    for x in range(len(random_list)):
        print (random_list[x])
    yesno()



def append():
    append_list = int(input("Enter the element you want to add: "))
    random_list.append(append_list)
    print("The element has been added.")
    print("This is the new array: ", random_list)
    yesno()


def insert():
    insert_list = int(input("Enter the index you want to insert: "))
    ins_num = int(input("Enter the element you want to insert: "))
    random_list.insert(insert_list, ins_num)
    print("The element has been inserted.")
    print("This is the new array: ", random_list)
    yesno()


def modify():
    modify_element = int(input("Enter the index you want to modify: "))
    mod_num = int(input("Enter the element you want to modify: "))
    random_list[modify_element] = mod_num
    print("The element has been modified.")
    print("This is the new array: ", random_list)
    yesno()


def delete():
    delete_element = int(input("Enter the index you want to delete: "))
    random_list.pop(delete_element)
    print("The element has been deleted.")
    print("This is the new array: ", random_list)
    yesno()

def ascend_list():
    random_list.sort()
    print("This is the new array: ", random_list)
    yesno()

def descend_list():
    random_list.sort()
    random_list.reverse()
    print("This is the new array: ", random_list)
    yesno()

def minimum_element():
    smallest = min(random_list)
    print("The smallest element in the list/array is: ", smallest)
    yesno()

def maximum_element():
    largest = max(random_list)
    print("The smallest element in the list/array is: ", largest)
    yesno()

def sum_elements():
    total = sum(random_list)
    print("This is the sum of all the elements in the array: ", total)
    yesno()

def length_list():
    length = len(random_list)
    print("This is the length of the array: ", length)
    yesno()

def count_element():
    element = int(input("Enter the element you want to count: "))
    counted = random_list.count(element)
    print("This is the number of times the element "f"{element} appeared: ", counted)
    yesno()

def close():
    print("Thank you for using the List/Array Modifier!")
    exit()
    yesno()

while True:
    menu()
    option = int(input("\nEnter the option you want to choose from the menu (1-13): "))
    if option == 1:
        printlist()
    elif option == 2:
        append()
    elif option == 3:
        insert()
    elif option == 4:
        modify()
    elif option == 5:
        delete()
    elif option == 6:
        ascend_list()
    elif option == 7:
        descend_list()
    elif option == 8:
        minimum_element()
    elif option == 9:
        maximum_element()
    elif option == 10:
        sum_elements()
    elif option == 11:
        length_list()
    elif option == 12:
        count_element()
    elif option == 13:
        close()
    else:
        print("WRONG INPUT! There are only 13 options.")
