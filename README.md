# Azerbaijani Fake News Generator
A language model can predict the probability of the next word in the sequence, based on the words already observed in the sequence. Neural network models are a preferred method for developing statistical language models because they can use a distributed representation where
different words with similar meanings have similar representation and because they can use a large context of recently observed words when making predictions. The aim of this project is to generate fake news in the Azerbaijani language using LSTM Recurrent Neural Networks. LSTM Recurrent Neural Networks are powerful Deep Learning models which are used for learning sequenced data. 


In this project a LSTM model is used and trained on 100 thousand samples, and it should be able to generate text. Data for the training has been scraped from the most popular news website of Azerbaijan. 

Model accuracy is about 70% over the 50 epochs. I have used all possible methods to avoid overfitting.

__NB! I have shared only a small piece of sample data.__

Plot of the defined word-based language model.

![a257122b-e168-4045-9eb1-7e8d11b81712](https://user-images.githubusercontent.com/31247506/83392283-80baca80-a3fd-11ea-8441-10c339f6d0f3.png)


The learned embedding needs to know the size of the vocabulary and the length of input sequences as previously discussed. It also has a parameter to specify how many dimensions will be used to represent each word. That is, the size of the embedding vector space. Common values are 50, 100, and 300. We will use sequence length size here, but consider testing smaller or larger values. We will use a two LSTM hidden layers with 100 memory cells each. More memory cells and a deeper network may achieve better results. 

Two dense fully connected layer with 50 and 100 neurons connects to the LSTM hidden layers to interpret the features extracted from the sequence. We then add Dropout in order to avoid overfitting. The output layer predicts the next word as a single vector the size of the vocabulary with a probability for each word in the vocabulary. A softmax activation function is used to ensure the outputs have the characteristics of normalized probabilities.

The model is compiled specifying the categorical cross entropy loss needed to fit the model. Technically, the model is learning a multiclass classification and this is the suitable loss function for this type of problem. The efficient Adam implementation to mini-batch gradient descent is used and accuracy is evaluated of the model.


Some sample outputs:
```
müraciətdə qeyd edilib ki müvafiq addımlar atmışıq həmin səlahiyyətlər cənab dövlət başçısının etimadını doğrultmalıdırlar bu barədə iqtisadiyyat nazirliyinin açıqlamasında bildirilir

millət vəkili kimi bütün vədlərə dərhal reaksiya verilir digər tərəfdən mübarizə mexanizmləri ardıcıl olaraq təkmilləşdirilib mübarizə aparılmasında uğurlar qazanacağına inandığını

```



The project is under developing and if you want to be a part of this amazing work, feel free to contact me! :)
