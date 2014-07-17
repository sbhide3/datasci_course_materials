
import sys
import json

#def hw():
 #   print 'Hello, world!'

#def lines(fp):
 #   print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores={} # Initilize dict for maintaining sent scores
    for sent_line in sent_file:
	sent_line.rstrip("\n")
	sent_line.rstrip("\r")
	term,score=sent_line.split("\t")
	sent_scores[term]=int(score)
    #print sent_scores.items()
    for twt_line in tweet_file:
    #	print twt_line;
	twt_data=json.loads(twt_line)
	total_per_line=0
	for key,val in twt_data.items():
		if(key.encode('utf-8') == "text"):
		#	print "*",key.encode('utf-8'),"\t",val.encode('utf-8'),"*"
			text_str=val.encode('utf-8')
			text_str=text_str.replace('\n','')
			text_str=text_str.replace('\.','')
			text_str=text_str.replace(',','')
			text_str=text_str.replace(';','')
			text_arr=text_str.split()
			for item in text_arr:
				if(item in sent_scores.keys()):
		#			print item," ",sent_scores[item]," _ "
					total_per_line+=sent_scores[item]
	#print "Total is :",total_per_line
	print total_per_line


if __name__ == '__main__':
    main()
