#!/usr/bin/env python

""" File: latex_plot_sheet_half.py
	Author: Sarah Lindner
	Date of last change: 09.03.2015

	Takes figure files (pdf, png) in a directory as input and creates a latex file with rows of 3 figures which can be input to a latex file.
"""

from sys import argv 
import os

def main():
	out_filename = argv[1]
	in_filenames = argv[2:]

	# don't overwrite existing file
	if os.stat(path_filename(out_filename)).st_size > 0:
		response = raw_input("Overwrite " + out_filename + " ? - y/n\n")
		if response.lower().startswith("n"):
			print("Sayoonara")
			exit()

	out_file = open(out_filename, 'w')

	# empty file
	out_file.truncate()

	out_file.write("\\begin{figure}[!t]\n")


	for index, item in enumerate(in_filenames):

		filename = path_filename(item)

		out_file.write("\\begin{subfigure}[t]{0.49\linewidth}\n")
		out_file.write("\\begin{center}\n")
		out_file.write("\\testbox{\includegraphics[width= \\textwidth, trim = 0 0 0 0]{" + file_directory + "/" + filename + "}}\n")
		out_file.write("\end{center}\n")
		out_file.write("\end{subfigure}\n")


		# stop subfigure after every 2nd file or after last file in list
		if ((index+1) - len(in_filenames) == 0):
			out_file.write("\end{figure}\n")
			out_file.write("\hfill\n")
		elif (index != 0 ) and ( (index+1)%2 == 0):
			out_file.write("\end{figure}\n")
			out_file.write("\hfill\n")
			out_file.write("\\begin{figure}[!t]\n")

	out_file.write("\\hfill\n")
	out_file.write("\\vfill\n")

	out_file.close()

def path_filename( file ):
   return os.path.dirname( os.path.realpath( file ) ) + "/" + os.path.basename( file )


if __name__ == '__main__':
    main()