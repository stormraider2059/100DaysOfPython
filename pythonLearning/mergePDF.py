#Python program that merges pdf files in the mergePDF folder.
import PyPDF2 as p2
merger=p2.PdfWriter()
def mergePDF():
    for pdf in ['./mergePDF/a.pdf','./mergePDF/b.pdf','./mergePDF/c.pdf']:
        merger.append(pdf)
    merger.write('./mergePDF/mergedFinal.pdf')
    merger.close()      
mergePDF()