mapping_abc = "dictionary.txt"
print(mapping_abc)
lines = [l.strip() for l in open(mapping_abc, encoding='utf-8')] 
print(lines)
mapping = {k: v for k, v in (l.split() for l in lines[64:])}
print(mapping)