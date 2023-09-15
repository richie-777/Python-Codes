import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
new_dict = {val.letter: val.code for (index, val) in df.iterrows()}
print(new_dict)


def generate_phonetic():
    n = str(input()).upper()
    try:
        words = [new_dict[letter] for letter in n]
    except KeyError:
        print("Sorry, only Alphabets are allowed here.")
        generate_phonetic()
    else:
        print(words)


generate_phonetic()
