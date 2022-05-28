import requests, json, os, time
from colorama import *
yes = "yes"
retry_ask = "y"
init()
print(Fore.BLUE + "Some COVID thing v1.0")

def clearConsole(): #function to clear console
    os.system("cls" if os.name == "nt" else "clear")

while yes == "yes":
    yes == "no"
    response = requests.get("https://api.covid19api.com/summary").text
    response_info = json.loads(response)

    print(Fore.CYAN + "")
    print("New COVID cases [1]\nTotal COVID cases [2]\nTotal COVID deaths [3]\nNew COVID deaths[4]")
    choice = str(input(">>> "))

    if choice == "1":
        print(Fore.GREEN + "\n")
        for i in range(len(response_info["Countries"])):
            print(response_info["Countries"][i]["Country"] + Fore.YELLOW + ": " + str(response_info["Countries"][i]["NewConfirmed"]) + Fore.GREEN)
        print(Fore.GREEN + "Global: " + Fore.YELLOW + str(response_info["Global"]["NewConfirmed"]))

    elif choice == "2":
        print(Fore.GREEN + "\n")
        for i in range(len(response_info["Countries"])):
            print(response_info["Countries"][i]["Country"] + Fore.YELLOW + ": " + str(response_info["Countries"][i]["TotalConfirmed"]) + Fore.GREEN)
        print(Fore.GREEN + "Global: " + Fore.YELLOW + str(response_info["Global"]["TotalConfirmed"]))

    elif choice == "3":
        print(Fore.GREEN + "\n")
        for i in range(len(response_info["Countries"])):
            print(response_info["Countries"][i]["Country"] + Fore.YELLOW + ": " + str(response_info["Countries"][i]["TotalDeaths"]) + Fore.GREEN)
        print(Fore.GREEN + "Global: " + Fore.YELLOW + str(response_info["Global"]["TotalDeaths"]))

    elif choice == "4":
        print(Fore.GREEN + "\n")
        for i in range(len(response_info["Countries"])):
            print(response_info["Countries"][i]["Country"] + Fore.YELLOW + ": " + str(response_info["Countries"][i]["NewDeaths"]) + Fore.GREEN)
        print(Fore.GREEN + "Global: " + Fore.YELLOW + str(response_info["Global"]["NewDeaths"]))

    else:
        print("Invalid input, retry")
        time.sleep(1)
        clearConsole()
        retry_ask = "n"
        yes = "yes"

    if retry_ask == "y":
        print(Fore.RED + "\n")
        xd = input("Hit ENTER to exit or SPACE + ENTER to refresh")
        exit() if xd == "" else clearConsole() and yes == "yes"
