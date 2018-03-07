import os.path
endofprogram = False
try:
  infile=open(input("Enter name of input file: "),"r")
  filename=input("Enter name of output file: ")
  while os.path.isfile(filename):
    filename=input("File Exists. Enter name again:  ")
  outfile=open(filename,"w") 
except IOError:
  print("Error opening file - End of program")
  endofprogram = True
if endofprogram == False:
  a_list=[]
  b_list=[]
  for line in infile:
    line=line.strip()
    if len(line)==0:
      continue
    if line[0]!="#":
      a_list.append(line)    
  i=len(a_list)-1
  while i>=0:
    b_list.append(a_list[i])
    i=i-1
  outfile.writelines("\n".join(b_list))
  outfile.close()

