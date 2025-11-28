from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path,output_folder,dpi=400):
    os.makedirs(output_folder,exist_ok=True)
    pages=convert_from_path(pdf_path,dpi=dpi)
    for i,page in enumerate(pages):
        page_path=os.path.join(output_folder,f"page_{i+1}.png")
        page.save(page_path,"PNG")

    return [os.path.join(output_folder,f"page_{i+1}.png") for i in range(len(pages))]