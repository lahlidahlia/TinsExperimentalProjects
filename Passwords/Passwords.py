import os, sys, random, string


#This program will make a separate folder to contain all the passwords generated

####### FUNCTION DEFINITION ########
def get_pass_key():
    """Prompt and return a pass_key"""
    pass_key = raw_input("Enter the name of the name of the password you are making/changing/looking up IN ALL CAPS:\n")
    return pass_key + ".txt"

def get_password():
    """Prompt and return a password"""
    password = raw_input("Enter your password, either writing it or copy and pasting: \n")
    return password

def path_join(file_name):
    """Navigates the path to the correct locations"""
    main_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
    file_path = os.path.join(main_dir, "data")
    file_path = os.path.join(file_path, file_name)
    return file_path

def check_file_exist(pass_key):
    """Check if a file already exists by trying to read it and look for errors"""
    try:
        path = path_join(pass_key)
        file = open(path, "r")
        file.close()
        return True
    except IOError: #Error means file doesn't exist
        return False
    
def write_password(pass_key, password):
    """Overwrite password into a file"""
    path = path_join(pass_key)
    file = open(path, "w")
    file.write(password)
    file.close()

def read_password(pass_key):
    """Open and read a password"""
    path = path_join(pass_key)
    file = open(path, "r")
    password = file.read()
    file.close()
    return password

def generate_password(length):
    """Generate a random password using randomized digits of all english ascii and number digits"""
    ascii_and_digits = string.ascii_letters + string.digits
    password = '' #Initializing the password
    for i in range(length):
        password += ascii_and_digits[random.randrange(1, len(ascii_and_digits))] #Concatenate the random digits into pass_key
    return password

def check_existing_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

####### MAIN #######
def main():
    check_existing_dir("data")
    while True: #Not an infinite loop, used for error checking
        print("\"gn\" to Generate New (random) passwords, \"n\" to make a New (non-random) password, \"l\" to Lookup password, \"c\" to Change password:")
        command = raw_input("Options: gn, n, l, c \n")
        
        if command == "n":
            pass_key = get_pass_key()
            while check_file_exist(pass_key):
                print("ERROR: File already exist, please enter a new name")
                pass_key = get_pass_key()
            password = get_password()
            write_password(pass_key, password)
            break
            
        elif command == "c":
            pass_key = get_pass_key()
            while not check_file_exist(pass_key):
                print("ERROR: File does not exist, please retry")
                pass_key = get_pass_key()
            password = get_password()
            write_password(pass_key, password)
            break
        
        elif command == "l":
            pass_key = get_pass_key()
            while not check_file_exist(pass_key):
                print("ERROR: File does not exist, please retry")
                pass_key= get_pass_key()
            print(read_password(pass_key))
            break
        
        elif command == "gn":
            pass_key = get_pass_key()
            while check_file_exist(pass_key):
                print("ERROR: File already exist, please enter a new name")
                pass_key = get_pass_key()
            while True:
                try:
                    length = int(raw_input("How long do you want your password to be? (Input a number)\n"))
                    break
                except ValueError:
                    print("Invalid input, please try again")
            password = generate_password(length)
            write_password(pass_key, password)
            break
            
        print("Not a valid selection, please try again.")
        
if __name__ == "__main__":
    main()

