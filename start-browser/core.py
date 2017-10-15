import webbrowser
import json

def parse_bookmarks():
    with open('start-browser/bookmarks.json') as links_file:
        return json.load(links_file)

def open_browser():
    
    links = parse_bookmarks()
    
    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    for url in links["links"].values():
        webbrowser.get(chrome_path).open(url)

