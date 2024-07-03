#install packages pymupdf and pil
#pip install pymupdf pil

#import libraries
import fitz
import io
from PIL import Image

#open pdf file
file_list=["C:/Users/HP-PC/OneDrive/Documents/git_projects_Repo\Data-Extraction-/imageExtraction/Include/pdf/PrinceCatalogue.pdf","C:/Users/HP-PC/OneDrive/Documents/git_projects_Repo\Data-Extraction-/imageExtraction/Include/pdf/invoicesample.pdf","C:/Users/HP-PC/OneDrive/Documents/git_projects_Repo\Data-Extraction-/imageExtraction/Include/pdf/flyer.pdf"]
for fileorder in range(len(file_list)):
    file=file_list[fileorder]
    print('##'+file)
    pdfFile=fitz.open(file)
    print(pdfFile)
    #get each pages and images from each page
    for pageNumber in range(len(pdfFile)):
        page=pdfFile[pageNumber]
        image_list=page.get_images()
        print(image_list)

        for image_index,img in enumerate(page.get_images(),start=1):
            print(image_index)
            xref=img[0]
            baseImage=pdfFile.extract_image(xref)
            image_bytes=baseImage["image"]
            image_ext=baseImage["ext"]
            print(image_ext)
            # Create a PIL Image object from the image bytes
            pil_image = Image.open(io.BytesIO(image_bytes))
            # Save the image to disk
        # file="C:/Users/HP-PC/OneDrive/Documents/git_projects_Repo/Data-Extraction-/imageExtraction/Include/pdf/ExtractedImages"
            image_path = f"C:/Users/HP-PC/OneDrive/Documents/git_projects_Repo/Data-Extraction-/imageExtraction/Include/pdf/ExtractedImages/image_{pageNumber}_{image_index}.{image_ext}"
           #image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))
            pil_image.save(image_path)

