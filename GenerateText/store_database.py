import pickle
import Generate_text as gt

path_to_wikipedia = r"wikipedia2text-extracted.txt"
with open(path_to_wikipedia, "rb") as f:
    string = f.read().decode().lower()[0:10000000]
lm_order = 11
lm = gt.train_lm(string, lm_order)

with open("alt_fact_lm.p", "wb") as f:
    pickle.dump(lm, f)