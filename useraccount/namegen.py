import random
items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def _rnf(length):
    name = ""
    for i in range(length):
        name += items[random.randrange(0,len(items))]
    return name
def random_name_file(length=9,count=1,filetype=""):
    names_file = []
    for _ in range(count):
        names_file.append(_rnf(length=length))
    return names_file

if __name__ == "__main__":
    print(random_name_file(12,1))