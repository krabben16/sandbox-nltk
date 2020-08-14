FROM python:3.7.5-alpine

# https://www.nltk.org/data.html
# > The downloader will search for an existing nltk_data directory to install NLTK data.
RUN mkdir /usr/share/nltk_data

RUN pip3 install nltk==3.4.5 && python3 -m nltk.downloader all
