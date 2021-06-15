import json
import logging
import sys
from scrappers.vultr import extract_vultr
from scrappers.digital_ocean import extract_digital_ocean

logging.basicConfig(filename="scrappers.log", level=logging.ERROR)

def main(argv):
    if argv:

        response_vultr, row_count_vultr = extract_vultr()
        response_digital_ocean, row_count_digital_ocean = extract_digital_ocean()

        for option in argv:
            if "--help" in option:
                show_options()

            elif "--print" in option:
                print(response_vultr)
                print("\n")
                print(response_digital_ocean)

            elif "--save_json" in option:
                if not row_count_vultr > 0 or not row_count_digital_ocean > 0:
                    print(response_vultr)
                    print("\n")
                    print(response_digital_ocean)
                    return
                generate_file(response_vultr, "vultr.json", "json")
                generate_file(response_digital_ocean, "digital_ocean.json", "json")

            elif "--save_csv" in option:
                if not row_count_vultr > 0 or not row_count_digital_ocean > 0:
                    print(response_vultr)
                    print("\n")
                    print(response_digital_ocean)
                    return
                generate_file(response_vultr, "vultr.csv", "csv")
                generate_file(response_digital_ocean, "digital_ocean.csv", "csv")

            else:
                show_options()
    else:
        show_options()

def generate_file(response, filename, extension):
    """
    Funtion to generate the json or csv file
    """
    file = open(filename, "w")
    if extension == "json":
        file.write(response.to_json())
    else:
        file.write(response.to_csv())
    file.close()


def show_options():
    print("\n")
    print("Required flags")
    print("#" * 45)
    print("--help - Show how to use the flags")
    print("--print -  Print result in the screen")
    print("--save_json - Save the result in .json file")
    print("--save_csv - Save the result in .csv file")
    print("#" * 45)


if __name__ == "__main__":
    main(sys.argv[1:])
