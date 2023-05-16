import numpy as np
from PIL import Image

def create_card_array(grid_size):
    symbol_grid = []
    symbol_inf_line = []

    symbol_grid = np.arange(grid_size**2).reshape(grid_size, grid_size)

    symbol = symbol_grid[-1][-1]
    for i in range(grid_size+1):
        symbol += 1
        symbol_inf_line.append(symbol)

    card_array = []
    inf_counter = 0
    card_array.append(symbol_inf_line)

    #all diagonals - n for offsetting the starting i, m for offsetting the "along" count
    for m in range(grid_size - 1):
        for n in range(grid_size):
            card = []
            i = n
            j = 0
            for x in range(grid_size):
                symbol = symbol_grid[i][j]
                card.append(symbol)
                i += 1 + m
                j += 1
                if i >= grid_size:
                    i = i - grid_size
            card.append(symbol_inf_line[inf_counter])
            card.sort()
            card_array.append(card)
        inf_counter += 1

    #horizontal lines - i for going along columns, n for moving to next row
    for n in range(grid_size):
        card = []
        for j in range(grid_size):
            symbol = symbol_grid[n][j]
            card.append(symbol)
        card.append(symbol_inf_line[inf_counter])
        card.sort()
        card_array.append(card)

    inf_counter += 1

    #vertical lines - i for going along rows, n for moving to next column
    for n in range(grid_size):
        card = []
        for i in range(grid_size):
            symbol = symbol_grid[i][n]
            card.append(symbol)
        card.append(symbol_inf_line[inf_counter])
        card.sort()
        card_array.append(card)

    return card_array


def create_card_image(columns, space, symbols, card_number):
    rows = len(symbols)//columns

    if len(symbols)%columns:
        rows += 1
    
    width_max = max([Image.open(image).width for image in symbols])
    height_max = max([Image.open(image).height for image in symbols])
    background_width = width_max*columns + (space*columns)-space
    background_height = height_max*rows + (space*rows)-space
    background = Image.new('RGBA', (background_width, background_height), "WHITE")
    x = 0
    y = 0
    for i, image in enumerate(symbols):
        img = Image.open(image)
        x_offset = int((width_max-img.width)/2)
        y_offset = int((height_max-img.height)/2)
        background.paste(img, (x+x_offset, y+y_offset))
        x += width_max + space
        if (i+1) % columns == 0:
            y += height_max + space
            x = 0
    card = Image.new("RGBA", (background_width, background_height), "WHITE")
    card.paste(background, (0,0), background)
    card_name = "Cards/card_" + str(card_number) + ".jpg"
    card.convert("RGB").save(card_name)