import sys

contents = ""
if(len(sys.argv) < 2):
    print("Please specify -l or -a")
else:
    command = sys.argv[1]
    if command == '-a':
        with open("log.txt", "a+") as f:
            f.write(sys.argv[2] + "\n")
            # f.close()
            print("The file should have been written to")
    elif command == '-l':
        with open("log.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                contents += line
            if contents == "":
                print("The file is empty")
            else:
                print(contents)
    else:
        print("Only -l and -a are valid in this case")