from page_handler import PageHandler 
from models.Breast_Cancer_Detector.predict import model_details

page_handler = PageHandler("pages/pages.json")
page_handler.render_page("Breast Tumor Classifier Form")

# Add a new tab for model details
page_handler.add_tab("Model Details", model_details)