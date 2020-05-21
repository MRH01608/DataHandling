import csv 

FileIn = "Finishing_R2.csv"
#These are the field names applied to your csv. Make sure to structure it in this way. Script is set up to not look at first line of csv for headers
fnames = ['InputPath', 'Experiment', 'Genotype', 'Chamber_n', 'X_coord', 'Y_coord', 'Start', 'Stop', 'OutputPath']
# EXAMPLE csv layout
# X:\lossless\Matthew\20200403_BACKUP_W4_F02Ctrl1_lossless.avi, W4, Exp1, 1, 167, 109, 17, 1788, D:\MH_DLC_CutVids\W4

#A function for ultimately populating a .bat script
def PrintToFile(Input_, Exp_, Geno_, Chamber_, X_, Y_, Start_, Stop_, Output_):
	f = open('DLC_Cropping.bat', 'a')
	f.write(f"ffmpeg -i \"{Input_}\" -vf crop=616:616:{X_}:{Y_} -ss {Start_} -to {Stop_} -c:v libx264 -crf 10 \"{Output_}\{Exp_}_{Geno_}_Chamber{Chamber_}.avi\"\n\n")


#The business end - reads a csv and loads each row into a dictionary for easy indexing
with open (FileIn, 'r') as csv_file:
	csv_dict = csv.DictReader(csv_file, delimiter =',', fieldnames=fnames)
	count = 0
	for row in csv_dict:
		Input_ = row['InputPath']
		Exp_ = row['Experiment']
		Geno_ = row['Genotype']
		Chamber_ = row['Chamber_n']
		X_ = row['X_coord']
		Y_ = row['Y_coord']
		Start_ = row['Start']
		Stop_ = row['Stop']
		Output_ = row['OutputPath']
		PrintToFile(Input_, Exp_, Geno_, Chamber_, X_, Y_, Start_, Stop_, Output_)
		count += 1
	print(f"\nyou have {count} rows in your table")

