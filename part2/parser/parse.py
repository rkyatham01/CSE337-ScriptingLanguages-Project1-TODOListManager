# import utils.commands here

# parse the command line arguments and execute the appropriate commands.
from db.manager import get_all_tasks
from utils.commands import showhelp, list_all_tasks_cmd, add_task_cmd, remove_task_cmd, complete_task_cmd, change_priority_cmd, update_cmd, search_cmd, sort_cmd

def parseArgs(args):
    if len(args) < 2:
        string = 'Missing Required argument. Type -h to seek help'
        return string

    filename = args[0] #just for storage incase we need it
    args = args[1:] #bc we dont need the rest

    indx = 0

    while indx != len(args): #for each arguement in the array now check whats what
        if args[indx] in ("-h", "--help"):
            showhelp() #calls this function if these arguements were found
            break #breaks out of the for loop we done going through the arguements here
        if args[indx] in ("-l", "--list"):
            arr = get_all_tasks()
            res = ''
            for line in arr:
                res += line
            return res

        if args[indx] in ("-a", "--add"):
           if args[indx+1] == '-p':
               string = "Error: Incorrect priority option"
               return string

           if len(args) <= 3:
                string = 'Error: Cannot add a task with empty priority'
                return string

           if len(args) >= 5:
                string = 'Error: Found extraneous options'
                return string

           else:
                if args[indx+2] in ("-p", "--priority"):
                    if type(args[indx+3]) == type(5):
                        return add_task_cmd(args[indx+1], args[indx+3])
                    else:
                        string = 'Priority must be integer'
                        return string

        if args[indx] in ("-r", "--remove"):
            if len(args) > 2:
                string = 'Error: Found extraneous options'
                return string

            if len(args) == 1:
                string = 'Task ID missing'
                return string
            else:
                if type(args[indx + 1]) != type(5):
                    string = 'Task ID must be a number'
                    return string
                else:
                     return remove_task_cmd(args[1])

        if args[indx] in ("-c", "--complete"):
            if len(args) > 2:
                string = 'Error: Found extraneous options'
                return string

            if len(args) == 1:
                string = 'Task ID missing'
                return string
            else:       
                if type(args[indx+1]) != type(5):
                    string = 'Task ID must be a number'
                    return string
                else:
                    return complete_task_cmd(args[indx + 1])
            
        if args[indx] in ('-cp', '--changepriority'):
            if len(args) > 3:
                string = 'Error: Found extraneous options'
                return string

            if len(args) == 1:
                string = 'Task ID or priority missing'
                return string

            if type(args[indx+1]) != type(5):
                string = 'Task ID must be a number'
                return string
            else:
                return change_priority_cmd(args[indx + 1], args[indx + 2])
        
        if args[indx] in ('-u', '--update'):
            if len(args) > 3:
                string = 'Error: Found extraneous options'
                return string

            if len(args) == 1:
                string = 'Task ID or description missing'
                return string

            if type(args[indx+1]) != type(5):
                string = 'Task ID must be a number'
                return string
            else:
                return update_cmd(args[indx + 1], args[indx + 2])
        
        if args[indx] in ('-s', '--search'):
            if len(args) == 1:
                string = 'Search Criteria Missing'
                return string
            if len(args) > 7:
                string = 'Error: Found extraneous options'
                return string #too many arguements
            ###########################################
            if args[indx+1] in ("-p", "--priority"):
                if type(args[indx+2]) != type(5):
                    string = 'search ID and priority must be integer.'
                    return string
                if len(args) == 3:
                    string = search_cmd(None, None, args[indx+2]) 
                    return string
                #now more arguements should be perceived
                if args[indx+3] in ("-dp", "--description"):
                    if len(args) == 5:
                        string = search_cmd(None, args[indx+4], args[indx+2])
                        return string
                    if args[indx+5] in ("--id", "-i"):
                        if type(args[indx+6]) != type(5):
                            string = 'search ID and priority must be integer.'
                            return string
                        else:
                            string = search_cmd(args[indx+6], args[indx+4], args[indx+2])
                            return string
                if args[indx+3] in ("--id", "-i"):
                    if type(args[indx+4]) != type(5):
                        string = 'search ID and priority must be integer.'
                        return string
                    if len(args) == 5:
                        string = search_cmd(args[indx+4], None, args[indx+2])
                        return string
                    else: #pass the description in as last
                        string = search_cmd(args[indx+4], args[indx+6], args[indx+2])
                        return string
                string = search_cmd(None, None, args[indx+2])
                return string
            #1/3rd done
            ###################################################
            ###################################################
            if args[indx+1] in ("--id", "-i"):
                if type(args[indx+2]) != type(5):
                    string = 'search ID and priority must be integer.'
                    return string
                if len(args) == 3:
                    string = search_cmd(args[indx+2], None, None) 
                    return string
                #now more arguements should be perceived
                if args[indx+3] in ("-dp", "--description"):
                    if len(args) == 5:
                        string = search_cmd(args[indx+2], args[indx+4], None)
                        return string
                    if args[indx+5] in ("-p", "--priority"):
                        if type(args[indx+6]) != type(5):
                            string = 'search ID and priority must be integer.'
                            return string
                        else:
                            string = search_cmd(args[indx+2], args[indx+4], args[indx+6])
                            return string
                if args[indx+3] in ("-p", "--priority"):
                    if type(args[indx+4]) != type(5):
                        string = 'search ID and priority must be integer.'
                        return string
                    if len(args) == 5:
                        string = search_cmd(args[indx+2], None, args[indx+4])
                        return string
                    else: #pass the description in as last
                        string = search_cmd(args[indx+2], args[indx+6], args[indx+4])
                        return string
                string = search_cmd(args[indx+2], None, None)
                return string

            #2/3rd done
            ###################################################
            ###################################################
            if args[indx+1] in ("-dp", "--description"):
                    if len(args) == 3:
                        string = search_cmd(None, args[indx+2], None) 
                        return string
                    #now more arguements should be perceived
                    if args[indx+3] in ("-i", "--id"):
                        if type(args[indx+4]) != type(5):
                            string = 'search ID and priority must be integer.'
                            return string

                        if len(args) == 5:
                            string = search_cmd(args[indx+4], args[indx+2], None)
                            return string

                        if args[indx+5] in ("-p", "--priority"):
                            if type(args[indx+6]) != type(5):
                                string = 'search ID and priority must be integer.'
                                return string
                            else:
                                string = search_cmd(args[indx+4], args[indx+2], args[indx+6])
                                return string
                    if args[indx+3] in ("-p", "--priority"):
                        if type(args[indx+4]) != type(5):
                            string = 'search ID and priority must be integer.'
                            return string
                        if len(args) == 5:
                            string = search_cmd(None, args[indx+2], args[indx+4])
                            return string
                        else: #pass the description in as last
                            if type(args[indx+6]) != type(5):
                                string = 'search ID and priority must be integer.'
                                return string
                            string = search_cmd(args[indx+6], args[indx+2], args[indx+4])
                            return string
                    string = search_cmd(None, args[indx+2],None)
                    return string
            #3/3 done
            ###################################################
            #else you pass in None, None, None
            string = search_cmd(None, None, None)
            return string

        if args[indx] in ('-t', '--sort'):
            if len(args) > 2:
                string = 'Error: Found extraneous options'
                return string
            if len(args) == 1: #sorts normally pass empty string
                passString = ''
                string = sort_cmd(passString)
                return string
            if len(args) == 2:
                if args[indx+1] == '-d': #then reverse is true
                    passString = 'something'
                    string = sort_cmd(passString)
                    return string
                else:
                    passStrin = ''
                    string = sort_cmd(passStrin)
                    return string