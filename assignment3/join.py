import MapReduce
import sys
from pprint import pprint

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    records=[]

    for ords in list_of_values:
#        print ords[0]
	for lst in list_of_values:
#		print lst[0]
		if ords[0]=="order":
			if ords[0]!=lst[0]:
#				print ords+lst
				mr.emit(ords+lst)
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
