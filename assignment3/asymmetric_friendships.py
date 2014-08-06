import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(key, w)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    tables={}

    for v in list_of_values:
    #  total += v
     #print key,"\t",v
     if((key+v) not in tables.keys() and (v+key) not in tables.keys()):
       tables[key+v]=" "
       mr.emit((key, v))
       mr.emit((v,key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
