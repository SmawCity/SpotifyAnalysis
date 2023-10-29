# Overview

In writing this program, I wished to do some data analysis in order to gain some experience with the field. I have been interested in data analysis for a while, but I've never properly tried to do some data analysis programming. Additionally, the Pandas library is something new that I wanted to explore. 


[Software Demo Video](https://youtu.be/ob5iq_i-cq0)

# Data Analysis Results

Q1: Does the BPM (beats per minute) have an effect on the streams that a song receives?
A: The data collected shows that there is a positive correlation between slower bpm and streams, indicating that the slowest songs are generally more preferred than the fastest ones. However, this does not account for the songs in the middle, so the larger correlation cannot be fully confirmed. 

Q2: Are certain keys more popular than other ones? 
A: Certain keys enjoy much more popularity than others. Songs written in the key of A received an average of roughly 408 million streams, while songs written in the key of C# received an average of 604 million, whichis around 48% more. Other popular keys were E and D#, with averages of 577 million and 553 million respectively. 

# Development Environment

I wrote this program in the Visual Studio Code IDE in Python. In order to do that, I utilized tools from the Python pandas library as well as a free dataset from Kaggle.

# Useful Websites

* [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)
* [Kaggle (Pandas: Zero to Hero)](https://www.kaggle.com/code/kuchhbhi/pandas-zero-to-hero)

# Future Work

* Examine the correlation between bpm and streams to see if there is a specific range of bpm that results in more streams