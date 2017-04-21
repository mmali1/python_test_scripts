#!/usr/bin/python
import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  name_rank = {}
  year = "not found"

  with open(filename,"r") as f:
	  for line in f:
#		  print line
		  match = re.search('Popularity\sin\s\d+'  ,line)
		  if match:
			  #Extract year
			  year = filter(lambda x:x.isdigit(),match.group())
			  print year
			  break

  if year == "not found":
	  print "unable to find year, returning"


  with open(filename,"r") as f:
	  for line in f:
		  # Extract names lines
		  match = re.search(r'<tr.*?><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',line)
		  if match:
			  # Extract rank, boy name, girl name
			  rank,boy_name,girl_name = match.groups(0)
			  # If boy name already exists update rank, if current rank is less than old rank
			  if boy_name in name_rank:
				  old_rank = name_rank[boy_name]
				  if rank < old_rank:
					  name_rank[boy_name] = rank
			  else:
				  # add boy name and rank in name rank list
				  name_rank[boy_name] = rank

			# If girl name already exists update rank, if current rank is less than old rank
			  if girl_name in name_rank:
				  old_rank = name_rank[girl_name]
				  if rank < old_rank:
					  name_rank[girl_name] = rank
			  else:
				  name_rank[girl_name] = rank


  final_list = [year]

  for key,value in name_rank.items():
	  namerank = key + " " + str(value)
	  #print namerank
	  final_list.append(namerank)

  # print list of names sorted in alphabetical order
  print sorted(final_list)

  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  print args[0]

  extract_names(args[0])

if __name__ == '__main__':
  main()
