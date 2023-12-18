import csv

data = []
counters = dict()
counters['TIGER'] = 0
counters['LEOPARD'] = 0


def get_next_item_path(item_class):
    """func that gets path to the next item according to its class

    Args:
        item_class (_type_): accepts class

    Returns:
        item : returns string item
    """
    item_class = item_class.upper()
    counter = 0
    for item in data:
        if item[3].upper() == item_class:
            if counter == counters[item_class]:
                counters[item_class] += 1
                return item[1]
            else:
                counter += 1
    


with open('annotation.csv', 'r', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filereader.__next__()
    for row in filereader:
        data.append(row)

print(get_next_item_path("TIGER"))
print(get_next_item_path("LEOPARD"))
print(get_next_item_path("LEOPARD"))