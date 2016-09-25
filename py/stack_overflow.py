#!/usr/bin/python3

from lxml import html
import requests
import time
from helper_fns import testPythonCode
import signal

def linksForNPagesOf50(n):
    # http://stackoverflow.com/questions/tagged/python?page=2&sort=votes&pagesize=50
    urls = []
    for i in range(1, n+1):
        page = requests.get('http://stackoverflow.com/questions/tagged/python?page='+str(i)+'&sort=votes&pagesize=50')
        tree=html.fromstring(page.text)
        urls += tree.xpath('//div[@class="summary"]/h3/a/@href')
    return ["http://stackoverflow.com" + x for x in urls]


def getCodeFromPage(url):
        # First one is OPs code
        desc = ""
        mini_programs = []

        page = requests.get(url)
        tree=html.fromstring(page.text)
        answers=tree.xpath('//div[@class="post-text"]')
        if len(answers) == 0:
            return []

        for a in answers:
            s = ""
            for line in a.xpath('pre/code/text()'):
                s += line
            mini_programs.append(s)

        for s in answers[0].xpath('p/text()'):
            desc += s

        return mini_programs

# WARNING!!! THIS FUNCTION EXECUTES ARBITRARY PYTHON CODE FROM STACKOVERFLOW
def do_routine(pages):
    valid = []
    for url in linksForNPagesOf50(1):
        snippets = getCodeFromPage(url)
        if len(snippets) == 1:
            continue
        for snippet in snippets[1:]:
            print ("running: \n" + snippet + "\n\n")
            try:
                with timeout(seconds=3):
                    output = testPythonCode(snippet)
            except TimeoutError:
                pass
            if output != None:
                valid.append((snippets[0], output))
    return valid

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

