import string
import emoji
import re 
from emoji import UNICODE_EMOJI
punch = string.punctuation
times = ['1am', '1pm', '2am', '2pm', '3am', '3pm', '4am', '4pm', '5am', '5pm', '6am', '6pm', '7am', '7pm', '8am', '8pm', '9am', '9pm', '10am', '10pm', '11am', '11pm', '12am', '12pm']
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
case_tweet = ""
emojis = UNICODE_EMOJI
def token_space(text):
	tokenz  = text.split(" ")
	return(tokenz)
def token_punctuation(tokenz, punch) :
	i = 0
	case_tweet = ""
	while(i < len(tokenz)):

		#if its time only integers with am or pn are allowed 
		if (tokenz[i] in times):
			t = int(tokenz[i][0:-2])
			print	(t)
			if t in [1,2,3,4,5,6,7,8,9]:
				t = "0"+str(t)+"00"
			else:
				t = str(t)+"00"
			if tokenz[i][-2:] == "pm":
				t = int(tokenz[i][0:-2])
				t +=12
				t = t%24
				if t == 0:
					t = "0000"
				else:
					t = str(t)+"00"
			t = "CF:T:" +t
			tokenz[i] = t
			i +=1
			break	
		###Checking for URL NOTE: I am using regex from the GFG referance
		if len(tokenz[i]) == 1 and tokenz[i] in alphabet_list : 
			if len(case_tweet) == 0:
				flag = i
			case_tweet += tokenz[i]
			tokenz[i] = ""
		else:
			if len(case_tweet) > 0:
				tokenz[flag] = case_tweet
				case_tweet = ""
			r = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
			u = re.findall(r,tokenz[i])
			if (len(u)):
				i +=1
				continue	
			#separating tokens using special characters # tags @
			ll = list(tokenz[i])
			c = 0
			s = ""
			flag = 0
			for s in range(0, len(ll)):
				if(ll[s] == "."):
					c +=1
				if ll[s] in emojis:
					flag = 1
					break
			if(flag ==0 and c > 1 ):
				i+=1
				continue
			for j in range(0, len(ll)):
				
				if ll[j] in punch or ll[j] in emojis:
					if (ll[j] != "@" and ll[j] != "#" and ll[j] != "'"):
						a = "".join(ll[0:j])
						b = "".join(ll[j])
						c = "".join(ll[j+1:])
						tokenz[i] = a
						if b in emojis:
							b = emoji.demojize(b) 
						tokenz.insert(i+1, b)
						tokenz.insert(i+2, c)
						i = i + 1
						break
					else:
						if ll[j] != punch[6]:
							a = "".join(ll[0:j])
							a = "".join(ll[0:j])
							b = "".join(ll[j:])
							tokenz[i] = a
							temp = punch
							temp = temp.replace("_", "")
							temp = token_punctuation(["".join(b[1:])], temp)
							tokenz.insert(i+1, ll[j]+temp[0])
							for k in range(1, len(temp)):
								tokenz.insert(i+k +1, temp[k])
							i += len(temp)
							break
						else:
							####handling ' Clitics 
							test = "".join(ll[j:])
							if len(test) >1:
								a = "".join(ll[0:j])
								b = ""
								if test in ["'s","'m","'d","'t","'ve","'ll","'re"]:
									if test == "'s":
										b = "is"
									if test == "'m":
										b = "am"
									if test == "'d":
										b = "would"
									if test == "'t":
										a = "".join(ll[0:j-1])
										b = "not"
									if test == "'ll":
										b = "will"
									if test == "'ve":
										b = "have"
									if test == "'re":
										b = "are"
									tokenz[i] = a
									tokenz.insert(i+1, b)
									i = i + 1
									break
								else:
									if test[0:2] in ["'s","'m","'d", "'t"]:
										a = "".join(ll[0:j+2])
										b = "".join(ll[j+2:])
										tokenz[i] = a
										tokenz.insert(i+1, b)
										i -=1
										break
									else:
										a = "".join(ll[0:j+3])
										b = "".join(ll[j+3:])
										tokenz[i] = a
										tokenz.insert(i+1, b)
										i -=1
										break
							else:			
								
								tokenz[i] = "".join(ll[0:len(ll)-1])
								tokenz.insert(i+1,"'s")
								i+=2
								break
		i += 1
	##removing empty tokens 
	while "" in tokenz:
		tokenz.remove("")
	while "\n" in tokenz:
		tokenz.remove("\n")
	return(tokenz)


def my_tokenizer(tweet):
	tweet = tweet.lower()
	tweet = tweet.replace('“', ' " ')
	tweet=  tweet.replace('”', ' " ')
	tweet=  tweet.replace('\n', '')
	tokens_space = token_space(tweet)
	#without USA RETWEET TIME DATE
	tokenz = token_punctuation(tokens_space, punch)
	#print(tokenz)
	return(tokenz)

###################################################Data reading and writing############################################
###################################################************************############################################
fr = open("inputfile.txt", "r", encoding = "utf-8")
fw = open("output.txt", "w")
tweet = fr.readline()
while len(tweet) > 1:
	tokenz = my_tokenizer(tweet)
	tweet = " ".join(tokenz)
	tweet += "\n"+str(len(tokenz))+"\n"
	for i in range(len(tokenz)):
		if tokenz[i] == "\n":
			continue
		if i != (len(tokenz) -1):
			tweet += tokenz[i]+"\n"
		else:
			tweet += tokenz[i]
	fw.write(tweet)
	tweet = fr.readline()
	if len(tweet) > 1:
		fw.write("\n")

fw.close()
fr.close()
print("done")
