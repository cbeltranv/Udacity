###
### crawler.py
###

from getpage import get_page
from bs4 import BeautifulSoup
from webcorpus import WebCorpus

def get_all_links(page):
    soup = BeautifulSoup(page)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def add_page_to_index(corpus, url, content):
    words = content.split()
    for word in words:
        corpus.add_word_occurrence(url, word)

def crawl_web(seed): # returns webcorpus (includes index, graph)
    tocrawl = set([seed])
    crawled = []
    corpus = WebCorpus()

    while tocrawl: 
        url = tocrawl.pop()
        if url not in crawled:
            content = get_page(url)
            add_page_to_index(corpus, url, content)
            
            outlinks = get_all_links(content)
            for outlink in outlinks:
                corpus.add_link(url, outlink)

            tocrawl.update(outlinks)
            crawled.append(url)
    
    return corpus

if __name__ == '__main__':
    import pickle

    corpus = crawl_web('http://udacity.com/cs101x/urank/index.html')
    # write corpus to file
    fname = 'corpus.pkl'
    try:
        with open(fname, 'w') as fout:
            pickle.dump(corpus, fout)
            print "Succesfully wrote corpus to " + fname
    except IOError, e:
        print "Cannot write out corpus: " + str(e)