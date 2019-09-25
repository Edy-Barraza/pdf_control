from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        print("Merging:")
        print(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_name", type=str, required=True, help="(str) Name you want the output document to have")
    parser.add_argument("--files", required=True, type=str, nargs="+", help="(str) List all the files you want merged in the order you with to merge them ")
    args = parser.parse_args()

    if len(args.output_name) < 5 or args.output_name[-4:len(args.output_name)] != ".pdf":
        args.output_name += ".pdf"

    merge_pdfs(args.files, args.output_name)
    print(args.output_name)


if __name__ == '__main__':
    main()
