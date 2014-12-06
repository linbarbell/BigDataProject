fout=open("out.csv","a")
for line in open("data1.csv"):
    fout.write(line)
for line in open('data2.csv'):	
    fout.write(line)
fout.close()