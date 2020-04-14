class Directory:

    def __init__(self, string):
        array = string.split(" ")
        self.name = array[0]
        self.number = array[1]


# dictioary forming code
def directory_forming():
    phoneDirectory = {}
    n = int(input())
    for x in range(n):
        string_name_number = input()
        p = Directory(string_name_number)
        phoneDirectory[p.name] = p.number
    return(phoneDirectory)
# querryArray finding


def querryList(phoneDirectory):
    check = False
    to_print = []
    check = True
    while(check):
        try:
            check = input()
            if (check in phoneDirectory):
                to_print.append(check + "=" + phoneDirectory[check])
            elif(check != ""):
                to_print.append("Not found")

        except EOFError:
            break
    return to_print

#printing in order


def printAll(to_print):
    for elements in to_print:
        print(elements)


# checking value
Directory = directory_forming()
querryArray = querryList(Directory)
printAll(querryArray)
