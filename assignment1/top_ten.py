
import sys
import json


def main():

    tweet_file = open(sys.argv[1])
    twitter_dict={}
    for twt_line in tweet_file:
	twt_data=json.loads(twt_line)
	if "entities" in twt_data.keys():
	  hashtags = twt_data["entities"]["hashtags"] 
	  for htKeys in hashtags:
		if(htKeys != "None"):
         	    #print htKeys["text"].encode("utf-8")
		    if(htKeys["text"].encode("utf-8") in twitter_dict.keys()):
			twitter_dict[htKeys["text"].encode("utf-8")]+=1
		    else:
			twitter_dict[htKeys["text"].encode("utf-8")]=1 
    #print twitter_dict.items()
    
    from operator import itemgetter
   # print sorted(twitter_dict.items(), key=itemgetter(1), reverse=True)[:10]
    sr_twitter_dict=dict(sorted(twitter_dict.items(), key=itemgetter(1), reverse=True)[:10])
    for srkey in sr_twitter_dict:
	print srkey,"\t",twitter_dict[srkey] 

'''	for key,val in twt_data.items():
		
		if(key.encode('utf-8') == "entities"):
			
			for hkeys in twt_data[key].keys():
				if (hkeys.encode('utf-8')=="hashtags"):
				  print twt_data[key][hkeys]	
				
'''

if __name__ == '__main__':
    main()
