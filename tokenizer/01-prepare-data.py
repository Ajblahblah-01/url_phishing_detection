import pandas as pd
from tqdm.auto import tqdm
from nltk.tokenize import RegexpTokenizer  
import os

# load the dataset
df = pd.read_csv('/Users/arpit/Downloads/python_nb/url_phishing_detection/dataset/phishing_site_urls.csv')

# generate samples for tokenizer
PATH = '/Users/arpit/Downloads/python_nb/url_phishing_detection/tokenizer/content'
paths = []
tokenizer = RegexpTokenizer(r'[A-Za-z]+')

text_data = []
file_count = 0

for sample in tqdm(df['URL'].values):
    words = tokenizer.tokenize(sample)
    for word in words:
        if len(word) > 1:
            text_data.append(sample)
    if len(text_data) >= 10000:
        with open(os.path.join(PATH, f'text_data_{file_count}.txt'), 'w') as f:
            f.write('/n'.join(text_data))
        file_count += 1
        text_data = []


with open(os.path.join(PATH, f'text_data_{file_count}.txt'), 'w') as f:
    f.write('/n'.join(text_data))