from paddleocr import PaddleOCR

ocr=PaddleOCR(use_angle_cls=True,lang='en',use_structure=True)

def run_ocr(img_path):
    result=ocr.ocr(img_path,cls=True)
    return result