from bs4 import BeautifulSoup
import requests


# This is Graph Search Problem
# I'll use Depth First Search

def is_valid_link(link, context=0):
    return ((link != None) and (len(link) > 6) and (link[0] != "#") and (link[:6] == "/wiki/"))


starting_page_title = "/wiki/Dolph_Lundgren"
page_title = starting_page_title
visited = {}

while (page_title.lower() != "/wiki/philosophy"):
    page_url = "https://en.wikipedia.org" + page_title

    html_page = None
    response = requests.get(page_url)
    if ( response.status_code == 200 ):
        html_page = response.content

    soup = BeautifulSoup(html_page, 'html.parser')
    out_links = [link.get('href') for link in soup.find_all('a') if \
                 (is_valid_link(link.get('href'), context=0)) and \
                 (link.get('href') not in visited) \
                 ]
    if (len(out_links) == 0):
        break
    else:
        page_title = out_links[0]
        visited[page_title] = True

        if (len(visited) % 50 == 0):
            print("Number of pages visited: {}".format(len(visited)))

if ("philosophy" in str.lower(page_title)):
    print("Traversed from page '{}' to Philosophy after taking {} links.".format(starting_page_title, len(visited) + 1))
else:
    print("We reached a dead end page, congratulations. You proved the hypothesis false!")