ciphertext = "16 12 8 4 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
cipherlist = list(ciphertext.split())

#initialize variables
COLS = 4
ROWS = 5
key = '-1 2 -3 4'
translation_matrix = [None]*COLS
plaintext = ''
start = 0
stop = ROWS

key_init = [int(i) for i in key.split()]
for k in key_init:
    if k > 0:
        col_items = cipherlist[start:stop]
    elif k < 0 :
        col_items = cipherlist[stop:start]
    else:
        print('keys cannot be zero')
    translation_matrix[(abs(k))-1] = col_items
    start += ROWS
    stop += ROWS

print('\nciphertext = {}'.format(ciphertext))
print('\ntranslation matrix = ', *translation_matrix, sep='\n')
print('\nkey length = {}'.format(len(key_int)))

for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + " "

print('\nplaintext = {}'.format(plaintext))
