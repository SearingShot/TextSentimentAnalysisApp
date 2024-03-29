from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def roberta(Input):
  # Run for Roberta Model
  encoded_text = tokenizer(Input, return_tensors='pt')
  # This Will Convert our text into Encoded Text of 0 or 1, That our model will be Able to understand.
  output = model(**encoded_text) # we run our model on the encoded_text
  scores = output[0][0].detach().numpy()  # we take the output from tensor and store them in numpy.
  scores = softmax(scores)
  scores_dict = {
      'Negative' : scores[0],
      'Neutral' : scores[1],
      'Positive' : scores[2]
  }
  if scores[0]>0.5:
    return "Oops! That sounds pretty negative. 😢 Can't you be a bit more positive? 😤"
  elif scores[1]>0.5:
    return "Your sentiment are neutral. 🤷"
  elif scores[2]>0.5:
    return "Woah! That's super positive! 😃"

import streamlit as st

st.title('Sentiment Analysis App')
user_input = st.text_input("Enter a sentence:")
if user_input:
  # Process the input using roberta function
  result = roberta(user_input)
  # Display the result to the user
  st.success(f"Processed Output: {result}")

