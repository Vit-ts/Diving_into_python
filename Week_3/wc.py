# this program counts lines in a file

import sys

def wc(filename):
    count = 0 
    with open(filename) as f:
        for _ in f:
            count += 1
    return count

def process_file(filename):
    count = wc(filename)
    print("file: {0} has {1} lines".format(filename, count))

# sys.argv[1] - первый аргумент командной строки
# For example: sudo python3 wc.py /etc/shadow
def _main():
    process_file(sys.argv[1])
    
if __name__ == "__main__":
    _main()
