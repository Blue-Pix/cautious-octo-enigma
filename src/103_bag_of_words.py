from tokenizer import tokenize

def calc_bow(tokenized_texts):
  vocabulary = {}
  for tokenized_text in tokenized_texts:
    for token in tokenized_text:
      if token not in vocabulary:
        vocabulary[token] = len(vocabulary)

  n_vocab = len(vocabulary)
  
  bow = [[0] * n_vocab for i in range(len(tokenized_texts))]
  for i, tokenized_text in enumerate(tokenized_texts):
    for token in tokenized_text:
      index = vocabulary[token]
      bow[i][index] += 1

  return vocabulary, bow

texts = [
  '私は私のことが好きなあなたが好きです',
  '私はラーメンが好きです',
  '富士山は日本一高い山です'
]

tokenized_texts = [tokenize(text) for text in texts]
vocabulary, bow = calc_bow(tokenized_texts)
print(vocabulary)
print(bow)
