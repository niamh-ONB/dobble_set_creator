import random, os, time, math
from dobble_functions import create_card_array, create_card_image

start_time = time.time()

grid_size = 3

num_of_symbols = grid_size**2 + grid_size + 1
symbols_on_card = grid_size + 1
card_array = create_card_array(grid_size)

symbols_path = r'Symbols'
count = 0

for path in os.listdir(symbols_path):
    if os.path.isfile(os.path.join(symbols_path, path)):
        count += 1

if count < num_of_symbols:
    print("Error: not enough symbols.")
    missing = num_of_symbols - count
    print("Missing " + str(missing) + " image files. Printing card array: \n")
    print(card_array)

    quit()

card_number = 1
for card in card_array:
    random.shuffle(card)
    card_strings = []
    for symbol in card:
        symbol_png = "Symbols/" + str(symbol) + ".png"
        card_strings.append(symbol_png)

    columns = math.ceil(math.sqrt(symbols_on_card))
    create_card_image(columns, 20, card_strings, card_number)
    card_number += 1

print(str(num_of_symbols) + " cards have been generated and saved.")
print("Time taken: " + str(time.time() - start_time) + " seconds.")
