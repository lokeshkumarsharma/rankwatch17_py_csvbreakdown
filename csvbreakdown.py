

"""read a csv file from one directory and
write the text to anther csv file in another directory"""

import csv
import glob								
import os

write_directory_path = os.getcwd() + '/processed/'			#return current working directory
def main():
  """Main function to read all csv files from directory """
  files = glob.glob('raw/*.csv')							#look for a list of csv file for given path
  for file in files:						
    read_csv(file)											#read each csv file one by one


def read_csv(file_name):									#function for reading a file
  """"Reads csv file.

  Args:
      file_name: Name of csv file.
  """
  created_files = []										#creates an array 
  try:
    with open(file_name, 'rb') as csvfile:					#open to file to read in binary format
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:									#iterate each line of csv file
        create_csv(row,row[0] in created_files)						#call to create_csv function and checks whether same date is present or not
        created_files.append(row[0])						
  except Exception as e:									#catch an exception
    print 'Facing error while reading this %s csv file ' % file_name
    print 'Error:', e
    pass

def create_csv(data, is_created):			#declaration of function
  """"Reads csv file.

  
      data: Details to be add in csv file.
      is_created: Return true if file already created.
  """
  try:
    new_file_path = write_directory_path + data[0] + '-processed.csv'			#store the path of csv file		
    with open(new_file_path, is_created and 'a' or 'wb') as csv_file:			#open to created csv file
      writer = csv.writer(csv_file)												#write the data 				
      writer.writerows([data])											
  except Exception as e:														#catch an exception	
    print 'Facing error while writing file on this path %s' % new_file_path
    print 'Error:', e
    pass																	    #do not execute any command or code

if __name__ == '__main__':
  main()																	    #call to function
