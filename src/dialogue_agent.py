from os.path import dirname, join, normpath
import MeCab
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import neologdn
import unicodedata

class DialogueAgent:

  def __init__(self):
    DIC_DIR = "/usr/lib/mecab/dic/mecab-ipadic-neologd"
    self.tagger = MeCab.Tagger('-d {}'.format(DIC_DIR))

  def _tokenize(self, text):
    text = unicodedata.normalize('NFKC', text)
    text = neologdn.normalize(text)
    text = text.lower()

    node = self.tagger.parseToNode(text)
    tokens = []
    while node:
      features = node.feature.split(',')
      if features[0] != 'BOS/EOS':
        if features[0] not in ['助詞', '助動詞']:
          token = features[6] if features[6] != '*' else node.surface
          tokens.append(token)
      node = node.next
    return tokens

  def train(self, texts, labels):
    pipeline = Pipeline([
      ('vectorizer', TfidfVectorizer(tokenizer=self._tokenize, ngram_range=(1,3))),
      ('classifier', SVC())
    ])
    pipeline.fit(texts, labels)
    self.pipeline = pipeline

  def predict(self, texts):
    return self.pipeline.predict(texts)

if __name__ == '__main__':
  BASE_DIR = normpath(dirname(__file__))
  training_data = pd.read_csv(join(BASE_DIR, './training_data.csv'))
  
  dialogue_agent = DialogueAgent()
  dialogue_agent.train(training_data['text'], training_data['label'])

  with open(join(BASE_DIR, './replies.csv')) as f:
    replies = f.read().split('\n')

  input_text = '名前を教えてよ'
  predictions = dialogue_agent.predict([input_text])
  predicted_class_id = predictions[0]

  print(replies[predicted_class_id])

