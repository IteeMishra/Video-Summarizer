import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
import re
from nltk.corpus import stopwords
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.tokenize import sent_tokenize
import transformers
from transformers import BartTokenizer, BartForConditionalGeneration
from transformers import pipeline

def summarize_youtube_model(youtubeLink):
    nltk.download('punkt')
    link = youtubeLink
    unique_id = link.split("=")[-1]
    sub = YouTubeTranscriptApi.get_transcript(unique_id)  
    subtitle = " ".join([x['text'] for x in sub])

    summarizer = pipeline(
        'summarization',
        model='facebook/bart-large-cnn',
        tokenizer='facebook/bart-large-cnn'
    )

    n = 1000
    splitSummary = []

    for i in range(0, len(subtitle), n):
        split = subtitle[i:i + n]
        summary = summarizer(split, max_length=180, min_length=30, truncation=True)
        splitSummary.append(summary)

    summaryText = "".join([s[0]['summary_text'] for s in splitSummary])

    print("Summarizing Text:")
    print("Before Summarization Length:", len(subtitle))
    print("After Summarization Length:", len(summaryText))
    print(f"Summarized text : {summaryText}")
    return summaryText
