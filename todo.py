import os
import sys
import time
from alive_progress import alive_bar

BLUE, RED, WHITE, YELLOW, GREEN, END = ['\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;32m', '\033[0m']

# Clear
def clear():
    os.system('clear')

# start greetings
def start_greeting():
    sys.stdout.write('\n\n' + GREEN + '''
    .########..#######..########...#######...........######..##.......####
    ....##....##.....##.##.....##.##.....##.........##....##.##........##.
    ....##....##.....##.##.....##.##.....##.........##.......##........##.
    ....##....##.....##.##.....##.##.....##.#######.##.......##........##.
    ....##....##.....##.##.....##.##.....##.........##.......##........##.
    ....##....##.....##.##.....##.##.....##.........##....##.##........##.
    ....##.....#######..########...#######...........######..########.####                                             
        ''' + '\n\n\n' + END)


# last greetings  
def pp():
    sys.stdout.write('\n\n' + GREEN + ''' Thank You for using Todo-CLI, KEEP CODING; & HACKING :D !!!''' + '\n\n\n' + END)

# option;s
def option():
     print('\n {0}[{1}1{0}]{1} Add Todos '.format(BLUE, WHITE) + '' + ' {0}[{1}2{0}]{1} Show All Todos'.format(BLUE, WHITE) + '' + ' {0}[{1}3{0}]{1} Delete Todos'.format(BLUE, WHITE) + '' + ' {0}[{1}4{0}]{1} Done Todos'.format(BLUE, WHITE) + '' + ' {0}[{1}5{0}]{1} Help'.format(BLUE, WHITE) + '' + ' {0}[{1}6{0}]{1} Report'.format(BLUE, WHITE) + '' + ' {0}[{1}Q{0}]{1} Quit'.format(BLUE, WHITE) + '\n')

# main funtion
def main():
    clear()
    start_greeting()
    try:
        # progress bar
        print('{0}'.format(GREEN))
        with alive_bar(100, bar='blocks') as bar:
            for i in range(100):       
                time.sleep(0.1)
                bar()
        clear()
        start_greeting()
        while True:
            header = ('{0}:todo{1}>>> {2}'.format(GREEN, YELLOW, WHITE))
            option()
            choise = input(header)

            if choise not in ['1','2','3','4','5','6','Q','q']:
                print('{0}Invalid Input... {1}[HELP]{2} for more info'.format(RED, YELLOW, WHITE))
                choise = 3
                time.sleep(1)
                raise SystemExit
                clear()
            else:
                # Add Todos
                if choise == '1':
                    new_todo = str(input('{0}Enter the todo here{1}...{2} '.format(BLUE, YELLOW, WHITE)))
                    todos.append(new_todo)
                    time.sleep(1)
                    print('{0} ToDo added successfully!!!'.format(GREEN))

                # Show All Todos
                if choise == '2':
                    print()
                    if len(todos) == 0:
                        print('{0}Out of ToDos'.format(RED))
                    else:
                        for index in range(len(todos)):
                            inc_index = index+1
                            print('\t{2}[{3}{0}{2}]{3} : {4}{1}\n'.format   (inc_index, todos[index], GREEN, WHITE, YELLOW))
                        # time.sleep(1)
                        print('{0} ToDo listed successfully!!!'.format(GREEN))

                # Delete Todos 
                if choise == '3':
                    if len(todos) == 0:
                        print('{0}Out of ToDos'.format(RED))
                    else:
                        todo_remove_index = int(input('{0}Enter the todo number for delete tood{1}...{2} '.format(BLUE, YELLOW, WHITE)))
                        if todo_remove_index == 0 or todo_remove_index > len    (todos):
                            print('{0}Out of Range'.format(RED))
                        else:
                            todos.pop(todo_remove_index-1)
                            time.sleep(1)
                            print('{0} ToDo deleted successfully!!!'.format (GREEN))

                # Done Todos
                if choise == '4':
                    if len(todos) == 0:
                        print('{0}Out of ToDos'.format(RED))
                    else:
                        todo_complete_index = int(input('{0}Enter the todo  number for complete the todo{1}...{2} '.format(BLUE,     YELLOW, WHITE)))
                        if todo_complete_index == 0 or todo_complete_index > len    (todos):
                            print('{0}Out of Range'.format(RED))
                        else:
                            complete_todo = todos.pop(todo_complete_index-1)
                            complete_todos.append(complete_todo)
                            time.sleep(1)
                            print('{0} ToDo completed successfully!!!'.format   (GREEN))

                # Help
                if choise == '5':
                    print('''
        {0}:todo> {3}1
        {1}$ ./todo add "todo item"  {2}# Add a new todo
        
        {0}:todo> {3}2
        {1}$ ./todo ls               {2}# Show remaining todos
        
        {0}:todo> {3}3
        {1}$ ./todo del NUMBER       {2}# Delete a todo
        
        {0}:todo> {3}4
        {1}$ ./todo done NUMBER      {2}# Complete a todo
        
        {0}:todo> {3}5
        {1}$ ./todo help             {2}# Show usage
        
        {0}:todo> {3}6
        {1}$ ./todo report           {2}# Statistics`;
        
        {0}:todo> {3}Q
        {1}$ ./todo QUIT   '''.format(GREEN, YELLOW, BLUE, WHITE))

                # Report
                if choise == '6':
                    print('''
        {2}Pending : $ {0}
        {3}Complete : $ {1}
                        '''.format(len(todos), len(complete_todos), YELLOW, GREEN))
                    time.sleep(1)
                    print('{0} ToDo report generated!!!'.format(GREEN))

                # Quit
                if choise.upper() == 'Q' or choise.upper() == 'QUIT':
                    clear()
                    pp()
                    time.sleep(1)
                    raise SystemExit
                    clear()

    # Exception occurs
    except KeyboardInterrupt:
        clear()
        print('{0}Invalid Input... {1}[HELP]{2} for more info'.format(RED, YELLOW, WHITE))
        time.sleep(1)
        raise SystemExit


# i like this function 
if __name__ == "__main__":

    # global todos list
    todos = []
    # global complete list
    complete_todos = []

    # execute the main()
    main()