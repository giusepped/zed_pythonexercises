from sys import argv

script, input_file = argv

def print_all():
    print f.read()
    
def rewind(f):
    f.seek(0)
