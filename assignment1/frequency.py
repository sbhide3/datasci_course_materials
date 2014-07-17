
import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    all_counts=0
    tweet_counts={} # Initilize dict for maintaining sent scores
    for twt_line in tweet_file:
	twt_data=json.loads(twt_line)
	for key,val in twt_data.items():
		if(key.encode('utf-8') == "text"):
			text_str=val.encode('utf-8')
			text_str=text_str.replace('\n','')
			text_str=text_str.replace('\.','')
			text_str=text_str.replace(',','')
			text_str=text_str.replace(';','')
			text_arr=text_str.split()
			for item in text_arr:
				if item in tweet_counts.keys():
				   tweet_counts[item]+=1
				   all_counts+=1
				else:
				   tweet_counts[item]=1                                                                            
                                   all_counts+=1

#    print tweet_counts.items()
#    print all_counts
    for key in tweet_counts.keys():
       temp_freq=float(tweet_counts[key])/float(all_counts)
       print key,"\t",temp_freq


if __name__ == '__main__':
    main()
