import os
import requests
from urllib.parse import urlparse
import sys
import time
import random
from colorama import Fore, Style
"""
Yet another manager - yay improved

Usage: ➜ yam [options]
"""



orange = Style.BRIGHT + Fore.YELLOW + "\n➜ " + Style.RESET_ALL
orange_ = Style.BRIGHT + Fore.YELLOW + "➜ " + Style.RESET_ALL
aur_mode = 0
def get_repo_url(repo_name):

    github_url = ""

    # Validate the provided name format (username/repo-name.git)
    if not repo_name.endswith(".git") not in repo_name[:-5]:
        raise ValueError(orange +"Invalid repository name. Please use the format 'username/repo-name.git', or use AUR repos 'AUR-repo.git'(no username nessesary).")

    # Extract username and repo name
    if aur_mode ==0:
        username, repo = repo_name.split("/")[:2]
        url = github_url + username + "/" + repo
    elif aur_mode == 1:
        url = "https://aur.archlinux.org/"+ repo
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        return data["clone_url"]  # Extract clone URL from response
    else:
        raise ValueError(f"{orange} error: Failed to retrieve repository URL: {response.status_code}")

def clone_repo(repo_name, target_dir="."):
    yorn = input(Fore.LIGHTCYAN_EX + ":. "+ Fore.RESET +"Proceed with installation? [Y/n] ")
    if yorn == "Y" or yorn == "y":
        # Retrieve the valid repository URL
        repo_url = get_repo_url(repo_name)

        # Construct the cloning command using `urlparse` for proper URL formatting
        parsed_url = urlparse(repo_url)
        if aur_mode == 0:
            command = f"git clone {parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        elif aur_mode == 1:
            command = f"git clone https://aur.archlinux.org/{pkg}"
    # 
        # Clone the repository using os.system
        if os.system(command, cwd=target_dir) != 0:
            raise RuntimeError(orange +"error: A failure occurred in cloning the (AUR/github) repo")
    elif yorn == "n" or yorn == "N":
        print(orange +"User aborted (exit)")
        exit(0)


if __name__ == "__main__":    # <- main script
    if sys.argv[1] == "-S":
        if len(sys.argv[1]) > 1:
            if aur_mode == 1:
                print(orange +"Installing AUR package...")
            elif aur_mode == 0:
                print(Fore.LIGHTCYAN_EX + ":. "+ Fore.RESET +"Synchronizing package databases...")
                time.sleep(random.randint(1,5))
                print("\n")
                print(Fore.LIGHTCYAN_EX + ":. "+ Fore.RESET +"resolving dependencies...")
            time.sleep(random.randint(1,5))
            pkg = sys.argv[2]
            repo_name = pkg
            
            get_repo_url()
            try:
                clone_repo(repo_name)
                print(Fore.LIGHTCYAN_EX+ ":. " + Fore.RESET Successfully cloned repository + "'"+repo_name+"'" ")
            except (ValueError, RuntimeError) as e:
                print(f"{orange}error: A installation failure occurred: {e}")
    elif sys.argv[1] == "":
        print("\nUsage: "+ orange_ +"yam [options]")
    
    if sys.argv[1] == "-R":
        if len(sys.argv[1]) > 1:
            if aur_mode == 1:
                print(orange +"removing specified AUR package...")
            elif aur_mode == 0:
                print(Fore.LIGHTCYAN_EX + ":. "+ Fore.RESET +"removing specified git packages...")
            rmpkg = sys.argv[2]
            os.system("rm -rf "+ rmpkg)
    if sys.argv[1] == "--version":
        print(orange +"yam version 1.2")
        
    
    else:
        print("\nUsage:"+ orange_ +"yam [options]")
        

    while True: # <- find if AUR is package instead of git.
        if ("/" in pkg) == False:
            aur_mode = 1
        else:
            aur_mode = 0
            
        
