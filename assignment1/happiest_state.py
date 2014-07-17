
import sys
import json
import types

def main():

    tweet_file = open(sys.argv[2])
    sent_file = open(sys.argv[1])
    sent_scores={} # Initilize dict for maintaining sent scores
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    state_count={}
    state_scores={}


    for sent_line in sent_file:
	sent_line.rstrip("\n")
	sent_line.rstrip("\r")
	term,score=sent_line.split("\t")
	sent_scores[term]=int(score)

    twitter_dict={}
    for twt_line in tweet_file:
	twt_data=json.loads(twt_line)
	total_per_line=0
	for key,val in twt_data.items():
		if(key.encode('utf-8') == "text"):
		#	print "*",key.encode('utf-8'),"\t",val.encode('utf-8'),"*"
			text_str=val.encode('utf-8').lower()
			text_str=text_str.replace('\n','')
			text_str=text_str.replace('\.','')
			text_str=text_str.replace(',','')
			text_str=text_str.replace(';','')
			text_arr=text_str.split()
			for item in text_arr:
				if(item in sent_scores.keys()):
		#			print item," ",sent_scores[item]," _ "
					total_per_line+=sent_scores[item]
	if ("place" in twt_data.keys() and type(twt_data["place"]) is not types.NoneType):
                 if twt_data["place"]["country_code"] == 'US':
			#print twt_data["place"]["full_name"].encode('utf-8')
			city_state=twt_data["place"]["full_name"].encode('utf-8').split(', ')
			if city_state[1] in states.keys():
		    	   if city_state[1] in state_count.keys():				
			      state_count[city_state[1]]+=1
			      state_scores[city_state[1]]+=total_per_line
			   else:
			      state_count[city_state[1]]=1
                              state_scores[city_state[1]]=total_per_line   
    max_state=""
    max_key=0
    for skey in state_count.keys():
	temp_val=float(state_scores[skey])/float(state_count[skey])
	if temp_val > max_key:
	   max_key=temp_val
	   max_state=skey
	  # print skey,"\t",temp_val
	elif temp_val == max_key:
	   max_state+=skey

    print max_state

'''	  hashtags = twt_data["entities"]["hashtags"] 
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

	for key,val in twt_data.items():
		
		if(key.encode('utf-8') == "entities"):
			
			for hkeys in twt_data[key].keys():
				if (hkeys.encode('utf-8')=="hashtags"):
				  print twt_data[key][hkeys]	
				
'''

if __name__ == '__main__':
    main()
