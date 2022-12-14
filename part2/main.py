import sys, os
from utils.commands import sort_cmd, search_cmd, list_all_tasks_cmd
sys.path.insert(1, os.getcwd())
from db.manager import create,remove_task, add_task, search, update_desc, sort #delete later for testing

args = sys.argv #is a list in Python that contains all the command-line arguements passed args[0] would be the script file,
# rest would be the commands passed in
create()

args.append('-l')
-print(parseArgs(args)) #calls the function
