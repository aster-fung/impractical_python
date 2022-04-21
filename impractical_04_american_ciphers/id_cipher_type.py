import collections
import pandas as pd
import matplotlib.pyplot as plt


def load_cipher(filename):
    """
    load cipher text
    remove whitespace 
    return the cipher as a list of letters
    """
    with open(filename) as f:
        cipher_string = f.read().strip()
        cipher_list = list(cipher_string)
        # print('trying to decrypt {}'.format(filename))
    # print (cipher_list)
    return cipher_list


def count_letters(cipher_list):
    """
    count the letters in the cipher
    sort the letters by count
    remove \n
    """
    letter_count = collections.Counter(cipher_list)
    letter_count_sorted = letter_count.most_common()
    pointer = 0
    for (letter,count) in letter_count_sorted:
        if '\n' in letter:
            letter_count_sorted.pop(pointer)
        pointer += 1
    print(letter_count_sorted)
    return letter_count_sorted


def plot(count_list, provided_title):
    df = pd.DataFrame(count_list)
    x_label = [letter for (letter, count) in count_list]
    ax = df.plot.bar(title = provided_title,  legend = False)
    ax.set_xticklabels(x_label)
    plt.show()
    return None

def main():
    # import and load cipher texts
    cipher_a = load_cipher('cipher_a.txt')
    cipher_b = load_cipher('cipher_b.txt')
    # count the most common letters in the cipher texts
    a_count = count_letters(cipher_a)
    b_count = count_letters(cipher_b)
    # display the most common letters as a bar chart 
    # let user decide based on the chart display
    plot(a_count, 'cipher a')
    plot(b_count, 'cipher b')

    

if __name__ == "__main__":
    main()
