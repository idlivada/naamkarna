""" Generates list of boy or girl names from indianhindunames.com """
import string
import urllib
import sys
import BeautifulSoup

def main():
    if len(sys.argv) < 3:
        print "Usage python retrieve.py boy|girl include_meanings(yes/no)"
        return

    gender = sys.argv[1]
    include_meanings = sys.argv[2]
    for alpha in string.lowercase:
        get_names(alpha, gender, include_meanings=='yes')

def get_names(alpha, gender, include_meanings):
    f = urllib.urlopen('http://www.indianhindunames.com/indian-hindu-%s-name-%s.htm' % (gender, alpha))
    soup = BeautifulSoup.BeautifulSoup(f.read())
    f.close()

    [tag.extract() for tag in soup.findAll('script')]

    for p in soup.findAll('p'):
        for line in p.prettify().split('\n'):
            if not ' = ' in line:
                continue

            if include_meanings:
                print line
            else:
                print line.split(' = ')[0]


if __name__ == "__main__":
    main()
