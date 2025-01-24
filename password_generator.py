details = [('banana', 'yellow', 14) , ('peach', 'pink', 10) , ('cherry', 'red', 20) , ('watermelon', 'green', 7)]

def sort_based_on_index(list):
    return list[2]

details.sort(reverse=True, key=sort_based_on_index)

print(details)
