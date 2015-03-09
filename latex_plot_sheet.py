#!/usr/bin/env python

""" File: latex_plot_sheet.py
	Author: Sarah Lindner
	Date of last change: 03.03.2015

	Takes figure files (pdf, png) in a directory as input and creates a latex file with rows of 3 figures which can be input to a latex file.
"""

from sys import argv 

out_filename = argv[1]
in_filenames = argv[2:]

out_file = open(out_filename, 'w')

# empty file
out_file.truncate()

index = 0

for index in range(0, len(in_filenames), 3):
	out_file.write("\\begin{figure}[!ht]\n")

	for i in range(0,3):
		out_file.write("\\begin{subfigure}[t]{0.29\linewidth}\n")
		out_file.write("\\begin{center}\n")
		out_file.write("\\testbox{\includegraphics[width= \\textwidth, clip=true, trim = 0 0 0 0]{" + in_filenames[index + i] + "}}\n")
		out_file.write("\end{center}\n")
		out_file.write("\end{subfigure}\n")
		out_file.write("\hfill\n")


	out_file.write("\end{figure}\n")



out_file.close()
