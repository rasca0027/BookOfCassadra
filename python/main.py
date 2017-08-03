import random


monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
character = "{0} is both {1} and {2}. {3} is sometimes {4} and never {5}."

def generate_story(name, pronoun):
    with open('trivial.txt') as t:
        a = t.readlines()
    with open('surreal.txt') as t:
        b = t.readlines()
    d = a + b

    print '\n\nThe life story of %s\n------\n' % name
    
    # characteristic
    with open('character.txt') as t:
        c = t.readlines()
    cs = []
    for i in xrange(4):
        trait = c[random.randint(1, len(c) - 1)]
        cs.append(trait.replace('\r', '').replace('\n', '').lower())
    traits = character.format(name, cs[0], cs[1], pronoun.capitalize(), cs[2], cs[3]) 
    print traits
    
    # story
    for i in xrange(5):
        s = random.randint(1, len(d) - 1)
        story = d[s]
        del d[s]
        story = story.replace("{I}", pronoun).replace('\r', '').replace('\n', '')
        story = story.capitalize()
        year = random.randint(1, 39) + 2017
        month = random.randint(1, 11)
        month = monthes[month]
        print 'In %s %s, %s' % (month, year, story)


name = raw_input()
pronoun = raw_input()
generate_story(name, pronoun.lower())
