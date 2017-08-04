import pickle

path_to_wikipedia = r"wikipedia2text-extracted.txt"
with open(path_to_wikipedia, "rb") as f:
    string = f.read().decode().lower()[0:10000000]

pickle.dump(string, open("wiki_data.p", "wb"))