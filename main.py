import json
import sys
from scrappers.vultr import extract_vultr

def main(argv):
    if argv:

        response, row_count = extract_vultr()

        for option in argv:
            if "--help" in option:
                show_options()
            elif "--print" in option:
                print(response)
            elif "--save_json" in option:
                if not row_count > 0:
                    print(response)
                    return

                file = open("vultr.json", "w")
                file.write(response.to_json())
                file.close()

            else:
                show_options()
    else:
        show_options()

def show_options():
    print('\n')
    print("Required flags")
    print('#' * 45)
    print('--help - Show how to use the flags')
    print('--print -  Print result in the screen')
    print('--save_json - Save the result in .json file')
    print('#' * 45)
        

if __name__ == "__main__":
    main(sys.argv[1:])
    
