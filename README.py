Shopping-List
=============
# create a shared list
theList = []
# open and or creat list file
STLIST = open('slist.txt', 'r')

# function to print out the command instructions
def printMenu():
    print("""Here are the list of commands:
  -p : Print the List
  -e : Empty the List
  -r : Remove item 
  -x : Exit
  -h : Print this command list""")

# function to screen items for duplicates and badapples, if the items passes these tests it will be added to the list.
def addToList(item):
    if item in theList:
        print(item, ' already in list')
    elif item == 'badapple':
        print('unrecognized command')
    else:
        theList.append(item)
    return theList

# function that let's the user know how many items are in the list and asks them to add an item.  It tests to see if it is blank or not and if so reports that and asks them again.
def getInput():
    print('You have', len(theList), ' items on your list.')
    item = input('Enter an item or command: ')
    if item.isspace():
        print(item, 'Shopping list items cannot be blank.')
        item
    elif item == None:
        print('shopping list items cannot blank.')
    elif item =='':
        print('Shopping list items cannot be blank.')
    else:
        return item

# Prints out the running list items formated and numbered.
def printList():
    print('Your shopping list:')
    count = 0
    for item in theList:
        count += 1
        print('  ',str(count)+'.', item)

#uses a loop to clear the contents of the list.
def emptyList():
    while len(theList) > 0:
        del theList[0]
    print('Shopping list is empty')

# removes specif items from list.  Checks to see if the item was mentioned or if its number was mentioned and removes just that item.
def removeFromList(item):
    if item in theList:
        theList.remove(item)
        print(item, ' has been removed from list.')
    else:
        if item.isdigit():
            n = int(item) 
            del theList[n-1]
            print('item ', item, ' has been removed from list.')

#function to print welcome message and start program and open and read file then close file.
def startProgram():
    print('Welcome to the XYZ Shopping List Program')
    readme = STLIST.readlines()
    readme += theList
    STLIST.close

# function to end program.  Prints end message and opens, writes and closes shopping list to a file.
def endProgram():
    print('Thank you for using the XYZ Shoppling List Program.')
    STLIST = open('slist.txt', 'w')
    STLIST.write(str(theList))
    STLIST.close()

#Main function calls the start function, the menu function, the getinput function, tests input for commands then if so runs commands, the runs exit function.
def main():
    startProgram()
    printMenu()
    item = getInput()
    while item != '-x':
        if item == None:
            item = getInput()
        elif item[0] == '-' and item[1] not in ['p', 'h', 'e', 'r']:
            item = 'badapple'
        elif item == '-p':
            printList()
        elif item == '-h':
            printMenu()
        elif item == '-e':
            emptyList()
        elif '-r' in item:
            removeFromList(item[3:])
        else:
            addToList(item)
        item = getInput()
    endProgram()

# calls main function!
main()
