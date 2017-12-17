import sys


# class TodoUsage():
#     usage_text = 

# INT APP WITH PRINTING USAGE TO THE USER
def usage():
    print('\n\nCommand Line Todo application\n=============================\n \n Command line arguments:\n -l   Lists all the tasks\n -a   Adds a new task\n -r   Removes an task\n -c   Completes an task\n\n')


# LISTS TASKS FROM THE TXT FILE
# def listreader():
#     lista = open('todolist.txt', 'r')
#     lines = lista.readlines()    
#     # EMPTY LIST
#     if lines == []:
#         print('No todos for today! :)')
#         lista.close()
#     else:
#         print('\n\nTodos for today:\n')
#         for i in range(len(lines)):
#             print(str(i+1) + ' ' + '-' + ' ' + '[ ]' + ' ' + lines[i].strip())
#         print('\n')
#         lista.close()

def listreader():
    lista = open('todolist.txt', 'r')
    lines = lista.readlines()    
    # EMPTY LIST
    if lines == []:
        print('No todos for today! :)')
        lista.close()
    else:
        print('\n\nTodos for today:\n')
        for i in range(len(lines)):
            if lines[i][-1] == 'x':
                print(str(i+1) + ' ' + '-' + ' ' + '[x]' + ' ' + lines[i].strip())
            else:
                print(str(i+1) + ' ' + '-' + ' ' + '[ ]' + ' ' + lines[i].strip())
        print('\n')
        lista.close()
    

# ADD NEW TASK
def add_task(task):
    lista = open('todolist.txt', 'a')
    lista.write(task)
    print(task + ' added to todo list.\n')
    lista.close()


# DELETE TASK
def delete_task(task):
    lista = open('todolist.txt', 'r')
    lines = lista.readlines() 
    lista.close()
    lista = open('todolist.txt', 'w')  
    if int(sys.argv[2]) == 1:
        lines.pop(0)
    else:
        i = int(sys.argv[2]) - 1
        lines.pop(i)
    for line in lines:
        lista.write(line)


# CHECK TASK
def check_task(task):
    lista = open('todolist.txt', 'r')
    lines = lista.readlines() 
    lista.close()
    lista = open('todolist.txt', 'w')  
    if int(sys.argv[2]) == 1:    
        lines[0] = (line + ' x')
    else:
        i = int(sys.argv[2]) - 1
        lines.pop(i)
    for line in lines:
        lista.write(line)


# CHECKING WHAT THE USER WANTS
# for argument in sys.argv:
if len(sys.argv) == 1:
    usage()
elif len(sys.argv) > 1:
    # Argument error handling - check if arguemnt[1] is supported   
    # if sys.argv[1] == '-l' or '-a' or '-r' or '-c':
    if sys.argv[1] == '-l':
        listreader()
    elif sys.argv[1] == '-a':
        if len(sys.argv) == 2:
            print('\nUnable to add: no task provided\n')
        else:
            add_task('\n' + sys.argv[2])
    elif sys.argv[1] == '-r':
        if len(sys.argv) == 2:
            print('\nUnable to remove: no index provided\n')
        else:
            delete_task(sys.argv[2])
    elif sys.argv[1] == '-c':
        if len(sys.argv) == 2:
            print('\nUnable to check: no index provided\n')
        else:
            check_task(sys.argv[2])
    else: # sys.argv[1] != '-l' or '-a' or '-r' or '-c':        
        print('\nUnsupported argument!')
        usage()
elif len(sys.argv) == 3:
    # check if there is 
    print('ERROR: Gimmi an index PLS!')
