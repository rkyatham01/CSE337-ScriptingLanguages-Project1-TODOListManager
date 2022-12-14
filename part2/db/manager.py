import os

tasks_file = os.path.join(os.getcwd(), 'part2','db', 'tasks.csv')

# creates tasks file is none exists
def create():
    if is_tasks_file_exists() == False:
        file = open(tasks_file, "w")
        file.write("ID,DESCRIPTION,PRIORITY,STATUS\n")
        file.close()
        return True
    else:
        return False #if file already exists

# check if tasks file exists
def is_tasks_file_exists():
    return os.path.exists(tasks_file)

# adds a task to the task file and returns the task id.
def add_task(desc, priority):
    file = open(tasks_file, "r")
    currentLine = len(file.readlines())
    file.close()
    file = open(tasks_file, "a")
    file.write(str(currentLine) + ',' + desc + ',' + str(priority) + ',' + "Incomplete\n")
    file.close()

    return currentLine

# returns list of tasks in the task file.
def get_all_tasks():
    res = []
    if not is_tasks_file_exists():
        return res #returns empty array

    with open(tasks_file) as file:
        next(file)
        for line in file:
            res.append(line)
    if len(res) == 1:
        res.append("ID,DESCRIPTION,PRIORITY,STATUS\n")
        return res
    return res

# remove a task from the task file.
def remove_task(id):
    res = []

    flag = 0 #if this is 0 then theirs nothin to delete
    with open(tasks_file) as file:
        next(file)
        for line in file:
            print(line)
            arr = line.split(',')
            if int(arr[0]) == id:
                flag = 1
                continue
            if flag == 1: #from here subtract the rest of the ids
                #reconstruct the line
                arr[0] = int(arr[0]) - 1
                line = str(arr[0]) + ',' + arr[1] + ',' + arr[2] + ',' + arr[3] #all strings
            res.append(line)
    #now res has all the lines from task
    file = open(tasks_file, "w")
    file.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
    for line in res:
        file.write(line)
    file.close()
    
    if flag == 0:
        return False
    else:
        return True

# complete a task in the task file.
def complete_task(id):
    file = open(tasks_file, "r")
    fileread = file.readlines()
    if id > len(fileread):
        file.close()
        return False #impossible to update

    editarr = fileread[id]
    arr = editarr.split(',')
    line = str(arr[0]) + ',' + arr[1] + ',' + str(arr[2]) + ',' + "Complete\n" #add all strings
    fileread[id] = line #setting to this line now

    file = open(tasks_file, "w")
    file.writelines(fileread)
    file.close()
    return True

# change the priority of a task in the task file.
def change_priority(id, priority):
    file = open(tasks_file, "r")
    fileread = file.readlines()
    if id > len(fileread):
        file.close()
        return False #impossible to update

    editarr = fileread[id]
    arr = editarr.split(',')
    arr[2] = priority #updating priority
    line = str(arr[0]) + ',' + arr[1] + ',' + str(arr[2]) + ',' + arr[3] #add all strings
    fileread[id] = line #setting to this line now

    file = open(tasks_file, "w")
    file.writelines(fileread)
    file.close()
    return True

# update the task description of a task in the task file.
def update_desc(id, desc):
    file = open(tasks_file, "r")
    fileread = file.readlines()
    if id > len(fileread):
        file.close()
        return False #impossible to update
    editarr = fileread[id]
    arr = editarr.split(',')
    arr[1] = desc #updating description
    line = str(arr[0]) + ',' + arr[1] + ',' + arr[2] + ',' + arr[3] #add all strings
    fileread[id] = line #setting to this line now

    file = open(tasks_file, "w")
    file.writelines(fileread)
    file.close()
    return True

# search for a task in the task file.
def search(id, desc, priority):
    res = ""
    flag = 0
    with open(tasks_file) as file:
        next(file) #skips first line
        for line in file:
            arr = line.split(',')
            temp = []
            for i in arr:
                temp.append(i) #copy array

            if id == None:
                temp[0] = str(None) #set the variable
            if desc == None:
                temp[1] = None #set the variable
            else:
                temp[1] = temp[1].lower()
            if priority == None:
                temp[2] = str(None) #set the variable
            if desc != None:
                desc = desc.lower()

            if str(id) == temp[0] and desc == temp[1] and str(priority) == temp[2]:
                #construct the line back here to return
                flag = 1 #means it added atleast one
                line = str(arr[0]) + ',' + arr[1] + ',' + arr[2] + ',' + arr[3] #add all strings
                res += line #adds the line to the end
    
    if flag == 1:
        return res
    else:
        return "" #If it doesn't find
# sort the tasks in the task file. Default order is 1.
def sort(order=None):
    if order == None: #add in increased priority queue
       file = open(tasks_file, "r")
       fileread = file.readlines()
       fileread = fileread[1:]
       res = []
       for line in fileread:
            arr = line.split(',')
            res.append(arr)
        #now res has a list of list of arrays
        #now we use lambda to sort this list by 3rd index
       res.sort(key = lambda res: res[2])
       resString = ""
       for i in res:
            c = 0 #then it resets
            for w in i:
                resString += w
                if c == 3:
                    break
                resString += ','
                c += 1
       return resString
    else: #add in decreased priority queue
       file = open(tasks_file, "r")
       fileread = file.readlines()
       fileread = fileread[1:]
       res = []
       for line in fileread:
            arr = line.split(',')
            res.append(arr)
        #now res has a list of list of arrays
        #now we use lambda to sort this list by 3rd index
       res.sort(key = lambda res: res[2], reverse=True)
       resString = ""
       for i in res:
            c = 0 #then it resets
            for w in i:
                resString += w
                if c == 3:
                    break
                resString += ','
                c += 1
       return resString