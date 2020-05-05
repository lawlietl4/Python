import sys

if(len(sys.argv) < 2):
    print("Please specify -l or -a")
else:
    command = sys.argv[1]
    if command == '-a':
        message = sys.argv[2]
        print(message)
    elif command == '-l':
        print("this prints the contents of a file")
    else:
        print("Only -l and -a are valid in this case")
