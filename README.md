# PDF_Control

Split and Merge PDF Files for whatever reason! 

<h3>Requires: </h3>
<ul>
  <li>Python3 </li>
  <li>PyPDF2</li>
</ul>

<h3>Split </h3>

Split a PDF into many other smaller PDF files by inputting the maximum number of pages you wish each resultant file to have.
For example, you could run:
```
python split_pdf.py --split_file path/to/file/strength_to_love_mlk.pdf --max_pages 40 
```

split_pdf.py has the following arguments:
```
Args:
        split_file (str) - path to pdf file you wish to split
        max_pages (int) - maximum number of pages you wish each resultant file to have
        split_name (str) - base name of resultant split files. can include path
```

<h3> Merge </h3>

Merge many PDF files into one big PDF! 
For example, you could run:
```
python merge_pdfs.py --output_name path/to/outputdir/strength_to_love_mlk_merged.pdf --files mlk_1.pdf mlk_2.pdf mlk_2.pdf
```
merge_pdfs.py has the following arguments:
```
Args:
        output_name (str) - Name you want the output document to have
        files (str) - List all the files you want merged in the order you with to merge them
```
