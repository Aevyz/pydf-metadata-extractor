# Python PDF Metadata Extractor

Uses pikepdf to scan for PDF Metadata and outputs results to file

## Usage

`python pydf_metadata_extractor.py -i /mnt/hgfs/vmwareshare -o ./output.txt --force`

Options | Required | Explanation
---|---|---
Input | Required | Which file/folder do you wish to scan
Output | Optional | Do you want to optionally save the results to a file? (Default: only output to stdout)
Force | Optional | If an output file already exists, do you want to overwrite it?
