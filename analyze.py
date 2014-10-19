import sys
import utils.countsyl

def main(gender):
    names = [name.strip() for name in iter_names(gender)]  
    print 'Loaded %d %s names.' % (len(names), gender)

    min_syll = 2
    max_syll = 4

    filtered_names = []
    for name in names:
        if filter_syllables(name, min_syll, max_syll):
            filtered_names.append(name)
        else:
            print 'Filtered out %s' % name
        
    names = filtered_names
    print 'Filtered to %d %s names between %d and %d syllables.' % \
        (len(names), gender, min_syll, max_syll)

    #for name in names:
    #    print name

def filter_syllables(name, min_count, max_count):
    syllables = utils.countsyl.count_syllables(name)
    return syllables[0] >= min_count and syllables[1] <= max_count

def iter_names(gender):
    if gender not in ['boy', 'girl']:
        raise ValueError

    f = open('%s.txt' % gender)
    return f.xreadlines()
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Specify gender: boy/girl"
    else:
        main(sys.argv[1])
