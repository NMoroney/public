# python process_log.py > cleaned.csv
#
import re  # regular expressions

# print "process log : [1704]"

log_name = "UnderPP05162017.log"
# log_name = "primaryPP04272017_2.log"
# print "log name : " + log_name

with open (log_name, "r") as myfile:
  data = myfile.read()
# print data
# print "log file read in as data"

# 17.05
txt = re.sub('_predict#\\|\r\n\s+', '_predict#', data)
data = re.sub('#\\|\r\n', '#', txt)
# print data

# start of table tag is: _predict#
# end of table tage is: -----------
# to specify everything between: .*?
# the flags of re.DOTALL is required to search across newlines in data
#
tables = re.findall('_predict#.*?----------', data, flags=re.DOTALL)
number_tables = len(tables)
# print "found " + str(number_tables) + " tables in the log"

# print "first table "
# print tables[0]

labels = []
for table in tables :
  # label = re.findall('_predict#(.*) \\|', table)
  label = re.findall('_predict#(.*) \\|', table)
  # print label
  labels.append(label)
# print "first and last table labels : "
# print labels[0]
# print labels[number_tables-1]

j = 0
cleaned = []
for table in tables :
  rows = table.splitlines()
  number_rows = len(rows) - 1
  i = 0
  label = ''.join(labels[j])
  for row in rows :
    if (i > 0) and (i < number_rows) :
      out = ""
      halves = row.split('|')
      if '#' in halves[0] :
        text = halves[0].split('#')
      else :
        text = halves[0]
        text = halves[0].split()
      out += label + ", " + text[0].strip() + ", " 
      out += text[1].replace(",",";").strip() + ", "
      values = halves[1].split()
      for value in values :
        out += value + ", "
      print out[:-2]
    i += 1
  j += 1

