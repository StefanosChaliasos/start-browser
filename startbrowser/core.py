import webbrowser
import json
import sys
import argparse
import platform
from collections import OrderedDict
import os


browsers = { "chrome":{"Darwin":"open -a /Applications/Google\ Chrome.app %s",
                       "Linux":"/usr/bin/google-chrome %s",
                       "Windows":"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"},
             "firefox":{"Darwin":"",
                        "Linux":"",
                        "Windows":""}
           }


def parse_arguments():
    if not len(sys.argv) > 1:  # Check if an argument had given
        return False
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', choices=[
                        'chrome', 'firefox', 'safari',
                        'opera', 'chromium', 'windows-default'])

    args = parser.parse_args()
    return args.browser


def find_bookmarks_absolute_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path + "/bookmarks.json" 


def parse_bookmarks():
    bookmarks = find_bookmarks_absolute_path()
    with open(bookmarks) as links_file:
        links = json.load(links_file, object_pairs_hook=OrderedDict)
        return links
        

def find_platform():
    return platform.system()


def browser_not_open(url, browser):
    platform = find_platform()
    try:
        path = browsers[browser][platform]
        webbrowser.get(path).open(url)
    except Exception as e:
        print("Browser not found")
        sys.exit()


def open_browser():
    links = parse_bookmarks()
    browser_selection = parse_arguments()
    
    for url in links["links"].values():
        if browser_selection:
            try:
                #webbrowser.get(browser_selection).open(url)
                browser_not_open(url)
            except:
                browser_not_open(url, browser_selection)
        else:
            webbrowser.get().open(url)
