def word_freq(fname):
    fp = open(fname)
    counts = {}
    for line in fp:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    fp.close()
    return counts


def morse():
    to_convert = input('Enter a message: ')
    to_convert = to_convert.upper()
    morse_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}
    morse_string = ''
    for char in to_convert:
        morse_string = morse_string + morse_dictionary.get(char) + ' '
    return morse_string

costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}

total = costs['Chicago']['Las Vegas'] + costs['Las Vegas']['Dallas']
print(total)
print(type(total))
#This is the end of part 1

def cheapest(costs, origin, destination):
    options = []
    for path in costs[origin]:
        if path == destination:
            options.append(costs[origin][path])
        else:
            for sub_path in costs[path]:
                if sub_path == destination:
                    options.append(costs[origin][path] + costs[path][sub_path])
    if len(options) == 0:
        return float('inf')
    return min(options)

print(cheapest(costs, 'San Francisco', 'Philadelphia'))
print(cheapest(costs, 'Chicago', 'Dallas'))
print(cheapest(costs, 'Las Vegas', 'Los Angeles'))
print(cheapest(costs, 'Philadelphia', 'Las Vegas'))



        


        