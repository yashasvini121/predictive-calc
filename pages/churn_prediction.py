from page_handler import PageHandler

# Initialize PageHandler with the path to the pages configuration file
page_handler = PageHandler("pages/pages.json")

# Render the page for Churn Prediction (update the page name to match `pages.json` configuration)
page_handler.render_page("Churn Prediction")
