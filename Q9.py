n = int(input())
reviews = []
filler_words = {"very", "really", "quite", "extremely", "actually"}

for i in range(n):
    reviews.append(input())
    
text = " ".join(reviews)

words = text.split()
filtered_words = []


for w in words:
    if w.lower().strip("!()-[]{};:'\",<>./?@#$%^&*_~") not in filler_words:
        filtered_words.append(w)
        
if filtered_words:
    final_txt = " ".join(filtered_words)
    final_txt = final_txt[0].upper() + final_txt[1:]
else:
    final_txt = ""

punctuations = '''!@#$%^&*()_+-=?/>.<,:;"'{[}\]|'''
clean_for_count = ""
for ch in final_txt:
    if ch not in punctuations:
        clean_for_count += ch
        
count_words = clean_for_count.split()

total_words = len(count_words)


unique_words = set(w.lower() for w in count_words)
unique_count = len(unique_words)


print(final_txt)
print(total_words)
print(unique_count)
            
            
            