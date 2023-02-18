# Property Tag Creator

## Disclaimer

This project is only for study purposes only, all the code generate was basically provided by chatGPT. This repository is to share improvements as well as my experience using the tool of OpenAI.

## Approach

Based on a xlsx file, generate a patrimony tag to identify medical devices in a hospital or clinic. It takes the devices properties
and a institutional logo to create a tag with pre defined dimensions, and a QRcode that can be used as well. 

## Methodology

Using exclusivly chatGPT as a research method to develop a script based in python programming language, after a feel interaction 
with good results, small changes was made to improve layout and readability

### How to Use

1 - Download the python file and open in a interpreter (I used Spyder within Anaconda package)  
2 - Install requirements with `pip install -r requirements.txt`  
3 - Use your own data with the provided excel file, keeping the file name.  
4 - Use own logo to personalize the pag, keeping the file name  
5 - Run the script  

Feel free to modify the code as you need, you can also ask chatGPT for improvements. 

Some of the dialog that provided me this code. 

"I need to create a tag that has a qrcode and the proporties of a medical device, like manufacturer, model and serial number. "

"Ok, but i want the properties of the medical device to be defined in an external file and collected from the columns of a xls file, because there will be a lot of tags been generated"

"That great! But i want to provide the dimensions of the tag and a logo to personalize with"

"We are almost there, but
Its not working well, the QR code is out of the borders and the logo is to small You may consider that the xls file will have up to five properties, and if a property has more than 20 characters, you are not obligated to show the rest of characters in the tag. "
