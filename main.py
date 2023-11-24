import streamlit as st
import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Initialize NLTK tools
nltk.download('punkt')

def generate_ngrams(text, n_gram_size):
    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Generate n-grams
    ngrams = []
    for i in range(len(tokens) - n_gram_size + 1):
        ngrams.append(' '.join(tokens[i:i+n_gram_size]))

    return ngrams

def plot_ngram_frequency(ngrams):
    # Calculate frequency distribution of n-grams
    freq_dist = FreqDist(ngrams)

    # Plot bar chart
    plt.bar(freq_dist.keys(), freq_dist.values())
    plt.xlabel('N-grams')
    plt.ylabel('Frequency')
    plt.title('N-Gram Frequency')
    plt.xticks(rotation=45, ha="right")
    st.pyplot(plt)

# Create a Streamlit app
st.title("N-Gram Generator with Frequency Chart")
st.markdown("Enter a text passage and select the n-gram size to generate n-grams from the text.")
# Unique and attractive interface element (replace with your own image URL)
st.image("8ARA1.png", caption="Abstract Image")
# Get user input
text_input = st.text_input("Enter text passage:")
n_gram_size = st.selectbox("N-gram size:", [1, 2, 3, 4, 5])

# Generate n-grams if the user has provided input and selected n-gram size
if st.button("Submit") and text_input and n_gram_size:
    ngrams = generate_ngrams(text_input, n_gram_size)
    st.markdown("Generated n-grams:")
    for ngram in ngrams:
        st.write(ngram)

    # Display the unique visual element (frequency chart)
    st.markdown("### N-Gram Frequency Chart")
    plot_ngram_frequency(ngrams)

elif not text_input or not n_gram_size:
    st.info("Please enter text passage and select n-gram size to generate n-grams.")
