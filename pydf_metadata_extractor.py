import argparse
import pikepdf
import os
import sys
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True,dest="input",help="Input Folder / File",type=str)
parser.add_argument("-o", "--output", required=False,default=None, dest="output",help="Output File",type=str)
parser.add_argument("-f", "--force", required=False,default=False, action='store_true', dest="force",help="Overwrite Output File if Exists")
args = parser.parse_args()

files = []

# Inspired by https://stackoverflow.com/a/120948
def lsdir_full(dir):
    return [os.path.join(dir, f) for f in os.listdir(dir)]


if not os.path.exists(args.input):
    print('Exiting: Input Dir not Found')
    sys.exit(1)

if args.output is not None:
    if not os.path.exists(os.path.dirname(args.output)):
        print('Exiting: Directory of Output File does not exist')
        sys.exit(1)
    if not args.force and os.path.exists(args.output):
        print('Exiting: Output path exists')
        sys.exit(1)

    outputFile = open(args.output, "w")

if os.path.isfile(args.input):
    files = [args.input]
else: 
    files = lsdir_full(args.input)

if len(files) == 0:
    print("No files found in folder")
for pdf_path in files:
    print(pdf_path)
    if args.output is not None:
        outputFile.write(pdf_path+'\n')
    if not pdf_path.endswith('.pdf'):
        print('\t-File is not a pdf!')
        if args.output is not None:
            outputFile.write('\t-File is not a pdf!\n')
        continue
    try:
        pdf = pikepdf.Pdf.open(pdf_path)
        docinfo = pdf.docinfo
        for key, value in docinfo.items():
            print('\t-', key, ":", value)
            if args.output is not None:
                outputFile.write('\t-'+ str(key)+ ":"+str(value)+'\n')
    except Exception as e:
        print('\t-[Error]'+ str(e))
        outputFile.write('\t-[Error]'+ str(e)+'\n')