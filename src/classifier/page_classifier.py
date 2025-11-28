import re
from src.classifier.rules import(
    PHARMACY_KEYWORDS,FINAL_BILL_KEYWORDS, BILL_DETAIL_KEYWORDS
)

def count_matches(text,keywords):
    text=text.lower()
    return sum(1 for kw in keywords if kw in text)

def table_density(ocr_boxes):
    numeric_count=0
    for box in ocr_boxes:
        text=box[1][0] if isinstance(box,list) else box
        if re.search(r"\d{1,}\.?\d{0,2}",text):
            numeric_count+=1
        return numeric_count


def classify_page(text,ocr_boxes):
    text_lower=text.lower()

    pharmacy_score=count_matches(text,PHARMACY_KEYWORDS)
    final_bill_score = count_matches(text, FINAL_BILL_KEYWORDS)
    bill_detail_score = count_matches(text, BILL_DETAIL_KEYWORDS)

    density=table_density(ocr_boxes)

    if final_bill_score >= 1:
        return "FINAL_BILL"

    if pharmacy_score >= 1:
        return "PHARMACY"

    if density > 10:  # If density is high → must be BILL DETAIL
        return "BILL_DETAIL"

    if bill_detail_score >= 1:
        return "BILL_DETAIL"

    return "BILL_DETAIL"