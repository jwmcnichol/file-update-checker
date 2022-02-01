import datetime
from datetime import datetime
from datetime import timedelta
import os
import random



logfile = 'datetimetest.txt'
datafile = 'datafile.txt'

path = 'c:\\Users\jwmcn\Desktop\powerbi\successive file loads'  # note double slashes needed
path = os.path.abspath(path)
test_time_string = "1945-10-02 17:02:48.557508"


def list_items_in_path():
    items_in_path_list = []
    path_contents = os.listdir(path)
    print('Files in path:')
    list_counter = 0
    for name in path_contents:
        list_counter = list_counter + 1
        print(list_counter, ') ', name)
        items_in_path_list.append(name)
    return items_in_path_list


def check_time_manifest():
    files_in_path = list_items_in_path()
    test_list_set = set(files_in_path)
    if logfile in test_list_set:
        print("Element Exists")

    else:
        print('Time manifest not found')
        print('Creating time manifest')
        create_time_manifest()


def append_time_to_time_log():
    time_log_path = os.path.join(path, logfile)
    this_datetime = get_current_time()
    print(this_datetime, 'is returned from get current time')
    this_date = this_datetime[0]
    this_clock = this_datetime[1]
    write_string = ''
    time_list = [this_date, this_clock]
    for i in time_list:
        write_string = write_string + i + ' '
    print('write_string =', write_string)
    with open(time_log_path, 'a') as filehandle:
        filehandle.write('%s\n' % write_string)
        print('Appended %s\n' % write_string)


def create_time_manifest():
    try:
        name = logfile
        create_time_log_path = os.path.join(path, name)
        print(create_time_log_path)
        f = open(create_time_log_path, "x")
        f.close()
    except FileExistsError:
        print('File exists, returning')


# def write_time_to_log():

def print_time():
    now_time = get_current_time()
    print(now_time)
    print('format is', type(now_time))
    return


def get_current_time(currentTime=None):
    if currentTime:
        print(currentTime)
    else:
        print(datetime.now())
        found_time = datetime.now()
        date = found_time.strftime("%D")
        time_of_day = found_time.strftime("%H%M%S")
        print('got', date, time_of_day)
        return date, time_of_day


def get_time_from_log():
    filename = logfile
    os.chdir(path)
    wd = os.getcwd()
    print(wd, filename)
    with open(filename) as f:
        content = f.readlines()
        count = 1
    # Strips the newline character
    for line in content:
        print("Entry {}: {}".format(count, line.strip()))
        count = count + 1
        current_line = line
    last_line = current_line
    print('Last Entry:', last_line)
    converted_string = check_update_deadline(last_line)
    return last_line


def check_delta_against_increment(old_time, new_time):
    time_increment = 48
    print(old_time)
    print(type(old_time))
    print(new_time)
    print(type(new_time))
    print('****** check types inheritance')
    time_change = timedelta(hours=time_increment)
    print('old time plus increment = ', old_time + time_change)
    if new_time > old_time + time_change:
        print('greater than increment, passing move token')
        return 'move'
    else:
        print('not time to move yet, passing stay token.')
        return 'stay'


def check_update_deadline(retrieved_string):

    retrieved_string = (retrieved_string).rstrip()
    print('retrieved the string from file', retrieved_string)
    date = datetime.strptime(retrieved_string, "%x %H%M%S")
    now_time = datetime.now()
    sufficent_time_elapsed_value = check_delta_against_increment(date, now_time)

    return sufficent_time_elapsed_value

def update_routine():
    print('update routine running')
    last_time_string = get_time_from_log()
    print('The time stored in the log is', last_time_string)
    print('The stored value is of the type', type(last_time_string))
    converted_retrieved_string = check_update_deadline(last_time_string)
    print('The output of the deadline checker is', converted_retrieved_string)
    if converted_retrieved_string == 'move':
        move_file()
        print('moved file')
    else:
        print('did not move anything since it wasnt time yet')


def move_file():
    #move the file with this
    print('MOVED THE FILE!!')
    pass


    

def return_date_format(date_retrieved):
    date_format = type(date_retrieved)
    return date_format


def loop():
    while True:
        pressed = input("press 1")
        if pressed == '1':
            get_current_time()


class Menu:

    def menu_list(self):
        menu_items = [['append time to log', append_time_to_time_log],
                      ['create time manifest file', create_time_manifest],
                      ['Fraggle param', self.fraggle],
                      ['get time from log', get_time_from_log],
                      ['list items in path', list_items_in_path],
                      ['check time manifest', check_time_manifest],
                      # ['get time delta', get_time_delta()],
                      ['update', update_routine]
                      ]
        return menu_items

    def main_menu(self):
        while True:
            menu_items = Menu().menu_list()
            items_count = len(menu_items) + 1
            items_menu_numbers = []
            for x in range(1, items_count):
                items_menu_numbers.append(int(x))
            menu_dict = dict(zip(items_menu_numbers, menu_items))
            for x in menu_dict:
                print('-----------------------------')
                print(x, ')', menu_dict[x][0])
            menu_pick = int(input('pick a function to run'))

            menu_dict[menu_pick][1]()

    def fraggle(self):
        print('Im a fraggle')
        fparam = input('Enter a parameter')
        print('passed paramater', fparam)


Menu().main_menu()

# loop()
