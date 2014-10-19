""" Generates list of boy or girl names from indianhindunames.com """
import string
import urllib
import sys
import re
import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print "Usage python retrieve.py boy|girl"
        return

    gender = sys.argv[1]
    for alpha in string.lowercase:
        get_names(alpha, gender)

def get_names(alpha, gender):
    f = urllib.urlopen('http://www.indianhindunames.com/indian-hindu-%s-name-%s.htm' % (gender, alpha))
    soup = BeautifulSoup.BeautifulSoup(f.read())
    f.close()

    [tag.extract() for tag in soup.findAll('script')]

    for p in soup.findAll('p'):
        for line in p.prettify().split('\n'):
            if not ' = ' in line:
                continue
            
            name = line.split(' = ')[0]
            for n in re.split('\,|\/', name):
                print n.strip()


if __name__ == "__main__":
    main()
