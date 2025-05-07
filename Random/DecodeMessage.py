import pandas as panda

# Returns a decoded message from a list of unicode characters
def decodeMessage(link):

    # Grabs the table from the file, and ensures correct encoding
    tables = panda.read_html(link, encoding='utf-8')
    
    # Checks if table was found successfully
    if not tables:
        print("Error finding a table")
        return

    # Grabs table 1 and finds the max value of x-coordinates and y-coordinates
    table = tables[0]
    xMax = int(table.iloc[1:][0].max()) + 1
    yMax = int(table.iloc[1:][2].max()) + 1

    # Creates a 2d array to hold values and collects values from the table
    messageGrid = [[" " for _ in range(xMax)] for _ in range(yMax)]
    for index, row in table.iloc[1:].iterrows(): messageGrid[yMax - int(row[2]) - 1][int(row[0])] = row[1]

    # Prints message
    for r in range(yMax):
        for c in range(xMax): print(f"{messageGrid[r][c]:<2}", end='')
        print()

# Calls function
decodeMessage("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")