import wikipedia
import random
import re
from pathlib import Path
from collections import Counter
from nltk.corpus import stopwords
import datetime

#auxiliar functions
def get_order(fil):
    original_pos=[i for i in range(0,len(fil))]
    order=[0 for i in fil]
    for i in range(len(fil)):
        max_index=i+fil[i:].index(max(fil[i:]))
        max_val=max(fil[i:])
        id=original_pos[max_index]
        original_pos[max_index]=original_pos[i]
        original_pos[i]=id
        fil[max_index]=fil[i]
        fil[i]=max_val
        order[id]=i+1
    return order


# Setup
output_folder = Path('./wiki_texts')
output_folder.mkdir(exist_ok=True)
stop_words = set(stopwords.words('english'))

# Step 1: Get 10 random Wikipedia pages
titles = wikipedia.random(10)

# Step 2: Fetch content and save it to temp .txt files
temp_files = []
size=[]
for i, title in enumerate(titles):
    try:
        content = wikipedia.page(title).content
        temp_filename = output_folder / f'temp_{i+1}.txt'
        temp_filename.write_text(content, encoding='utf-8')
        stats = temp_filename.stat()
        size.append(stats.st_size)  # in bytes
        created = datetime.datetime.fromtimestamp(stats.st_birthtime)
        formatted_created = created.strftime('%Y-%m-%d %H:%M:%S')  # This formats seconds as integers
        temp_filename.write_text(f'FILE CREATED ON: {formatted_created}\nSIZE:{size[-1]}\n'+content, encoding='utf-8')
        temp_files.append(temp_filename)
    except Exception as e:
        print(f"Failed to fetch '{title}': {e}")

order_sufix=get_order(size)

# Step 3: Read and analyze each file to rename it
for i,file_path in enumerate(temp_files):
    text = file_path.read_text(encoding='utf-8').lower()
    words = re.findall(r'\b[a-z]{3,}\b', text)  # only words with 3+ letters
    words = [word for word in words if word not in stop_words]
    
    if not words:
        print(f"No valid words found in {file_path.name}")
        continue

    most_common_word, _ = Counter(words).most_common(1)[0]
    new_filename = output_folder / f'{order_sufix[i]}_{most_common_word}.txt'

    # Avoid overwriting files
    suffix = 1
    while new_filename.exists():
        new_filename = output_folder / f'{order_sufix[i]}_{most_common_word}_{suffix}.txt'
        suffix += 1

    file_path.rename(new_filename)
    print(f'Renamed {file_path.name} -> {new_filename.name}')
