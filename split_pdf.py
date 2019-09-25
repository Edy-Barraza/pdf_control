from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse


def split_pdf(file, max_pages, split_name):
    pdf = PdfFileReader(file)
    pdf_writer = PdfFileWriter()
    for page_numb in range(pdf.getNumPages()):
        if page_numb % max_pages == 0:
            if page_numb > 0:
                output_name = f'{split_name}{"_"}{page_numb//max_pages}.pdf'
                with open(output_name, 'wb') as output_pdf:
                    print("Creating File:")
                    print(output_name)
                    pdf_writer.write(output_pdf)
            pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page_numb))
    if page_numb%max_pages != 0:
        output_name = f'{split_name}{"_"}{(page_numb // max_pages)+1}.pdf'
        with open(output_name, 'wb') as output_pdf:
            print("Creating File:")
            print(output_name)
            pdf_writer.write(output_pdf)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--split_file", type=str, required=True, help="(str) file you with to split")
    parser.add_argument("--max_pages", type=int, required=True, help="(int) max number of pages in resultant pdf files")
    parser.add_argument("--split_name", type=str, required=False, help='(str) base name of resultant split files')
    args = parser.parse_args()

    if args.split_name is None:
        split_pdf(args.split_file, args.max_pages, args.split_file)
    else:
        split_pdf(args.split_file, args.max_pages, args.split_name)


if __name__ == '__main__':
    main()
