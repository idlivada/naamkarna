import sys
import utils.countsyl

swears = ['shit', 'dik', ]

def main(gender):
    names = [name.strip() for name in iter_names(gender)]  
    print 'Loaded %d %s names.' % (len(names), gender)

    min_syll = 2
    max_syll = 4

    names = batch_filter_syllables(names, min_syll, max_syll)
    print 'Filtered to %d %s names between %d and %d syllables.' % \
        (len(names), gender, min_syll, max_syll)

    names = batch_filter(names, filter_prefixes)
    print 'Filtered to %d %s names.' % \
        (len(names), gender)

    names = batch_filter(names, filter_swears)
    print 'Filtered to %d %s names.' % \
        (len(names), gender)

    for name in names:
        print name

def batch_filter_syllables(names, min_count, max_count):
    filtered_names = []
    for name in names:
        if filter_syllables(name, min_count, max_count):
            filtered_names.append(name)
        else:
            print 'Filtered out %s' % name
        
    return filtered_names

def batch_filter(names, function):
    filtered_names = []
    for name in names:
        if function(name):
            filtered_names.append(name)
        else:
            print 'Filtered out %s' % name
        
    return filtered_names

def filter_syllables(name, min_count, max_count):
    syllables = utils.countsyl.count_syllables(name)
    return syllables[0] >= min_count and syllables[1] <= max_count

def filter_swears(name):
    for swear in swears:
        if swear in name.lower():
            return False
    return True

def filter_prefixes(name):
    prefixes = ['Vr', 'Mr', 'O', 'Z', 'Madhu', 'Hr', 'Hy', 'Dr', 'Dy', 'Dhr']
    for prefix in prefixes:
        if name.startswith(prefix):
            return False
    return True

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
