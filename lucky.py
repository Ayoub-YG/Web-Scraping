import webbrowser, sys, requests, bs4

print('Googling ...')

res = requests.get('https://www.bing.com/search?q='+' '.join(sys.argv[1:]))
#for testing connexion

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

all_a_tags = soup.select('a[h]')
# print(type(all_a_tags[0]))
# print(all_a_tags[0].get('h'))
# for tag in all_a_tags:
#     if tag.get('h').endswith('2'):
#         print('est la')
#     else:
#         print('nooo la')
#         print(tag.get('h'))
LinkElems = [a for a in all_a_tags if a.get('h') and a.get('h').endswith('2')]
print(LinkElems)


numberOFOpen = min(5, len(LinkElems))
for i in range(numberOFOpen):
    webbrowser.open(LinkElems[i].get('href'))
