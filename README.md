# Sweater Customization Dashboard
 
Welcome to the repository for the sweater customization dashboard. This project creates a knitting pattern for a drop shoulder sweater with the user's inputted customizations. Prior knitting knowledge is needed to understand the pattern and dashboard details. This pattern will not teach you how to knit but will instead give you instructions to follow. A more detailed understanding of the project is in a pdf called writeup.pdf is the writeup folder.

### Launching the Dashboard
To launch the dashboard, clone the repository and ensure that the following libraries are installed in your environment:
- Pandas
- Dash
- Pillow
- Flask
- FPDF
- PathLib
- re

Then run `main.py` in the terminal. A link to a website will return. Copy the link and paste it into a browser.

### Using the Dashboard
The dashboard takes many inputs to meet the user's customization needs. The following selections and inputs must be chosen and entered for the program to create the pattern.
- Sweater name
- Neckline type
- Sleeve type
- Embellishment type
- Size
- Gauge details

The sweater name can be any string the user wishes to enter. The image displaying the sweater changes with each neckline, sleeve, and embellishment dropdown option to show the user a preview of their sweater. If any option besides 'No embellishment' is chosen for the embellishment dropdown, the user must enter their desired rib type and rib height. If a collar option is chosen, the user must enter their desired collar height. If the user wishes to insert their own sweater measurements, they may do so by choosing "Insert own measurements" in the size dropdown.

To accurately calculate the pattern details, users must enter their gauge. The gauge is found by knitting a small square with the needle size, yarn, and tension they intend to use for the pattern. Then, measure the length of the square, count the number of stitches in that length, measure the height, and count the number of rows in that height. If this step is not completed and users guess at their gauge, the pattern calculations will not be correct.

When all customizations are selected and entered, hit "Generate Pattern." A link to trigger the download will appear to the right of the button. If you have forgotten to select or enter one of the required inputs, the link will not appear. You will find your sweater pattern in the patterns folder called (the name the entered)_sweater_pattern.pdf.