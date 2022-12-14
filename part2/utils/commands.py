# import db/manager here.
import dbm

from db.manager import get_all_tasks, create, is_tasks_file_exists, add_task, get_all_tasks, remove_task, complete_task, update_desc, search, sort, change_priority

def showhelp():
    print('usage: python main.py <options>')
    print('===== options =====')
    print('-h or --help to print this menu.')
    print('-l or --list to list all tasks.')
    print('-a or --add <DESCRIPTION> to add a new task')
    print('-p or --priority <NUMBER> to assign a priority to a new task. Must use with -a or -s.')
    print('-r or --remove <ID> remove a task.')
    print('-c or --complete <ID> mark a task as complete.')
    print('-cp or --changepriority <ID> <NUMBER> change an existing task\'s priority.')
    print('-u or --update <ID> <DESCRIPTION> update an existing task\'s description.')
    print('-s or --search <OPTIONS> search a task by options.')
    print('-t or --sort show sorted list of tasks by increasing order of priority.')
    print('-d or --desc decreasing order of priority. Must use with -t.')
    print('-i or --id <ID> task ID. Must use with -s for search task with ID.')
    print('-dp or --description <TEXT> task description. Must use with -s for search task with description.')

# command to list all tasks
def list_all_tasks_cmd():
    arr = get_all_tasks()
    if len(arr) == 0:
        string = 'TODO List empty. Add some tasks.'
        return string
    else:
        #gotta get the format he wants it in
        string = ""
        for line in arr:
            newString = ""
            arr2 = line.split(',') #now u got the properties again
            #arr3 = arr2[3].split('\n')
            newString = 'ID: ' + str(arr2[0]) + ' ' + 'DESC: ' + arr2[1] + ' ' + 'PRIORITY: ' + str(arr2[2]) + ' ' + 'STATUS: ' + arr2[3]
            string += (newString)
        return string

# command to add a task
def add_task_cmd(task, priority):
    string = 'Failed to add task'
    if task == '' or priority <= 0:
        return string

    currentLinesRead = add_task(task, priority)
    string = 'Task added and assigned ID ' + str(currentLinesRead)
    return string

# command to delete a task
def remove_task_cmd(id):
    RemovedCheck = remove_task(id) #is true if removed
    #else returns False
    if RemovedCheck == True:
        string = "Removed task ID " + str(id)
    else:
        string = 'Failed to remove task ID ' + str(id)
    return string

# command to complete a task
def complete_task_cmd(id):
    if complete_task(id):
        string = "Task " + str(id) + " completed"
        return string
    else:
        string = "Task " + str(id) + " could not be completed"
        return string

# command to edit task priority
def change_priority_cmd(id, priority):
    if id <= 0 or priority <= 0:
        string = 'Priority of task ' + str(id) + ' could not be changed'
        return string

    if change_priority(id,priority):
        string = 'Changed priority of task ' + str(id) + ' to ' + str(priority)
        return string
    else:
        string = 'Priority of task ' + str(id) + ' could not be changed'
        return string

# command to edit task description
def update_cmd(id, desc):

    if desc == '': #if its empty, you shouldn't update
        string = 'Failed to update task ' + str(id)
        return string
    if id <= 0: #gotta be higher
        string = 'Failed to update task ' + str(id)
        return string

    if update_desc(id, desc):
        string = 'Task ' + str(id) + ' updated'
        return string
    else:
        string = 'Failed to update task ' + str(id)
        return string

# command to search a task by id, description, or priority
def search_cmd(id, desc, priority):
    notFound = 'Task not found'

    if id != None and id <= 0:
        return notFound
    if priority != None and priority <= 0:
        return notFound
    
    res = search(id,desc,priority)
    
    if res == "":
        return notFound
    else:
        return res
         
# command to sort the tasks in specified order
def sort_cmd(order):
    if order == '':
        string = sort() #don't pass in anythin default
        return string
    #then its not empty so any number
    string = sort(order)
    return string
