import MeCab

tagger = MeCab.Tagger()
print(tagger.parse("私は私のことが好きなあなたが好きです"))
