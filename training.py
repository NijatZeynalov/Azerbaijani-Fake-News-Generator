#import libraries
import re
import string
import tensorflow as tf
from numpy import array
from pickle import dump
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.layers import LSTM
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
from tensorflow.keras.layers import Activation
from tensorflow.keras.callbacks import EarlyStopping

#load document
def load_doc(filename):
        file = open(filename, 'r',encoding="utf-8")
        text = file.read()
        file.close()
        return text

in_filename = 'news.txt'
doc = load_doc(in_filename)

#clean text
def clean_doc(doc):
    doc = doc.replace('-','')
    tokens = doc.split()
    # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # make lower case
    tokens = [word.lower() for word in tokens]
    return tokens
tokens = clean_doc(doc)
#print(tokens)
#print(len(set(tokens)))

#save clean text
length = 50+1
sequences = list()
for i in range(length, len(tokens)):
    seq = tokens[i-length:i]
    line = ' '.join(seq)
    # store
    sequences.append(line)
#print('Total Sequences: %d' % len(sequences))

#save tokens to file
def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w',encoding="utf-8")
    file.write(data)
    file.close()

out_filename = 'news_sequences.txt'
save_doc(sequences, out_filename)


#train a model
def load_doc(filename):
# open the file as read only
    file = open(filename, 'r',encoding="utf-8")
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text
# load
in_filename = 'news_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')

# integer encode sequences of words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)

vocab_size = len(tokenizer.word_index) + 1
sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]

model = Sequential()
model.add(Embedding(vocab_size, seq_length, input_length=seq_length))
model.add(LSTM(seq_length * 2, return_sequences=True))
model.add(LSTM(50))
model.add(Dense(50, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

earlystop = EarlyStopping(monitor='loss', min_delta=0, patience=5, verbose=0, mode='auto')
model.fit(X, y, epochs=50, verbose = 2, callbacks=[earlystop])

# save the model to file
model.save('model.h5')
# save the tokenizer
dump(tokenizer, open('tokenizer.pkl', 'wb'))
