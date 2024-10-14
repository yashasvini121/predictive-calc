from page_handler import PageHandler

# Initialize the PageHandler with the path to your pages.json file
page_handler = PageHandler("pages/pages.json")

# Render the Car Price Estimator page
page_handler.render_page("Car Price Estimator")
