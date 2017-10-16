import webbrowser
import json
import platform
import sys

def find_system_platform():
    return platform.system()

def set_chrome_path(platform):
    if platform == "Darwin":
        return 'open -a /Applications/Google\ Chrome.app %s'
    elif platform == "Linux":
        return '/usr/bin/google-chrome %s'
    elif platform == "Windows":
        return 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'    
    sys.exit("Operating System not supported")

def parse_bookmarks():
    with open('start-browser/bookmarks.json') as links_file:
        return json.load(links_file)

def open_browser():
    links = parse_bookmarks()
    platform = find_system_platform()
    chrome_path = set_chrome_path(platform)

    for url in links["links"].values():
        webbrowser.get(chrome_path).open(url)

