from page_handler import PageHandler

# Initialize the page handler with the path to the pages configuration file
page_handler = PageHandler("pages/pages.json")

# Render the page for Insurance Cost Predictor
page_handler.render_page("Insurance Cost Predictor")
