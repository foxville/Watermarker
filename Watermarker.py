import PyPDF2, sys, os

try:
	path = sys.argv[1]
	directory = sys.argv[2]
except IndexError:
	print("Please add the input and output folders\' names: \"python watermark.py INPUT_FOLDER OUTPUT_FOLDER\"")
	exit()

if not os.path.exists(path):
	print('You need to create the input folder first and put there the pdf file')
	exit()

try:
	watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
except FileNotFoundError:
	while True:
		print(f'Please add a watermark pdf file to the \"{os.getcwd()}\" folder and name it \"watermark.pdf\"')
		break

if not os.listdir(path):
	print(f'Put a pdf file into the \"{sys.argv[1]}\" folder!')
else:
	output = PyPDF2.PdfFileWriter()

	if not os.path.exists(directory):
		os.makedirs(directory)

	for pdfs in os.listdir(path):
		temps = PyPDF2.PdfFileReader(open(f'{path}/{pdfs}', 'rb'))
		for i in range(temps.getNumPages()):
			page = temps.getPage(i)
			page.mergePage(watermark.getPage(0))
			output.addPage(page)

			with open(f'{directory}/watermarked_output.pdf','wb') as file:
				output.write(file)
	print ("Task is finished!")