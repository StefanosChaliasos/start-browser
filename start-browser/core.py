import webbrowser
import json
import sys
import argparse


def parse_arguments():
    if not len(sys.argv) > 1:               # check if an argument had given
        return False
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', choices=[
                        'chrome', 'firefox', 'safari',
                        'opera', 'chromium', 'windows-default'])

    args = parser.parse_args()
    return args.browser


def parse_bookmarks():
    with open('start-browser/bookmarks.json') as links_file:
        return json.load(links_file)


def open_browser():
    links = parse_bookmarks()

    browser_selection = parse_arguments()

    for url in links["links"].values():
        if browser_selection:
            try:
                webbrowser.get(browser_selection).open(url)
            except Exception as e:
                print("Browser not found")
                sys.exit()
        else:
            webbrowser.get().open(url)
