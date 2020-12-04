from _datetime import datetime
log_file = 'imageFilter.log'

def log(msg):
    """
    logs all the actions in the file 'imageFilter.log'
    :param msg: the message we want to log in our file

    """
    now = datetime.now()
    timestamp= now.strftime('%d/%m/%Y %H:%M:%S')
    formatted = f'{timestamp}-{msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')



def dump_log():
    """
    Opens our file 'imageFilter.log' for reading and prints it in the console.

    """
    with open(log_file,'r') as f :
        print(f.read())