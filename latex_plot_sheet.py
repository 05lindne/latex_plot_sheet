#!/usr/bin/env python

""" File: latex_plot_sheet.py
	Author: Sarah Lindner
	Date of last change: 09.03.2015

	Takes figure files (pdf, png) in a directory as input and creates a latex file with rows of 3 figures which can be input to a latex file.
"""

from sys import argv 

out_filename = argv[1]
in_filenames = argv[2:]

out_file = open(out_filename, 'w')

# empty file
out_file.truncate()


out_file.write("\\begin{figure}[!t]\n")


for index, filename in enumerate(in_filenames):
	out_file.write("\\begin{subfigure}[t]{0.29\linewidth}\n")
	out_file.write("\\begin{center}\n")
	out_file.write("\\testbox{\includegraphics[width= \\textwidth, trim = 0 0 0 0]{" + filename + "}}\n")
	out_file.write("\end{center}\n")
	out_file.write("\end{subfigure}\n")
	out_file.write("\hfill\n")


	# stop subfigure after every 3rd file or after last file in list
	if ((index+1) - len(in_filenames) == 0):
		out_file.write("\end{figure}\n")
	elif (index != 0 ) and ( (index+1)%3 == 0):
		out_file.write("\end{figure}\n")
		out_file.write("\\begin{figure}[!t]\n")



out_file.close()
