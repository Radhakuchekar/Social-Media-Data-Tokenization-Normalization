# Social-Media-Data-Tokenization-Normalization

## Problem Statement: 
The goal of the assignment is to write a social media data tokenizer. The input of the code will be a set of  posts/tweets and the output will be the tokens in each post/tweet.

## Data Scraping:

For the data scraping I have used Social Media Scrapper (Git directory:
https://github.com/the-javapocalypse/Social-Media-Scrapper/blob/master/README.md). In
order to get data from tweeter I have created app using tweeter development tools. Then I
tried different keywords like RamMandir, girl and the trending word Binod also. I did
analysis like repetition of tweets, content of tweets, satisfying maximum requirements from
assignment (clitics, time formats, special symbols etc) and then I finalized the tweets for
keyword girl.

## Data Cleaning:

In this part of coding. I have converted all the letters in lower case to simplify the further
processing. Then the double quotation marks in the input tweets was different from the double quotation marks 
typed by keyboard so I replaced all the opening and closing double quotation marks in the
program understanding for that is [ ” to the " and “ to the " ]

## Tokenizer and Normalizer:
#### Space tokenization:
I did tokenization on the space basis and got a list of tokens.

#### Time:
if the token is in the form of date eg. (2am) then It gets converted in the canonical
format and we continue the process with next token without applying other conditions like
URL, date, special characters etc.

#### URL checking: 
Tokenizer is able to differentiate any kind of URL. If the token is not URL and not even time then I have checked that token against further different cases.

#### Special characters, emojis and Special cases of # and @:
In this case I have done tokenization depending upon the special characters, emojis and the
special cases on the special characters regarding # and @.I got that list of emojis in the python package named emoji itself and the list has name “UNICODE_EMOJI”. I have demojize all emojis into the equivalent text format for that particular emoji for example 😍 becomes :smiling_face_with_heart-eyes and same for the punctuation marks python has module string
and in string string.punctuation gives the all punctuation marks including #@’. Then I was
supposed to handle them in separate. So each case for #@’ has the relevant piece of code.

#### Clitics into component words:
The tokenizer and normalizer I have designed is capable of handling all types of clitics and
convert them into the respective component words

#### Special cases R E T W E E T and U.S.A.:
These 2 cases are also handled as R E T W E E T becomes RERWEET one word 



