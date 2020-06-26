Project Name: Vein Detector and Heart rate monitor
Team Members:
Abhijith Purohit (1BM17CS400)
Jayalakshmi J (1BM17CS409)
Fahad Mohammed Tahasildar (1BM15CS130)
Mohammed Fardeen Saqlain (1BM15CS155)

Project Guide: Selva Kumar S, Assistant Professor, Dept. of CSE, BMSCE.

Repository for System Code: https://github.com/abhi-1203/VDHRM_SystemCode

Repository for App: https://github.com/abhi-1203/VDHRM

Description:

This project contains implemented code to detect Vein Patterns and heart rate Monitor of the patients. this project helps doctors, radiologists, Hospital Nurses who perform venipuncture on patients to draw blood or to give IV drips. the Code captures the image, processes it, and projects the result back to the patient's skin.

Hardware Requirements to execute the project:

1. Raspberry Pi 3 is recommended but you can use Raspberry Pi 4 or newer. link to Buy -> (https://www.thingbits.in/products/raspberry-pi-4-model-b-2-gb-ram)
2. IR Camera- 5MP or more. link to Buy ->  (https://robu.in/product/ir-cut-camera-5-mp-ov5647-manually-switch-day-and-night-mode-module-raspberry-pi-3-camera-with-light/)
3. DLP2000 EVM Pico Projector. link to Buy -> (https://www.digikey.com/products/en?mpart=DLPDLCR2000EVM&v=296)
4. Pulse Sensor link to Buy -> (https://www.amazon.in/REES52-PULSESENSOR-Pulse-Sensor-Heart/dp/B01L19X7B2)

Tools/ Software Required to Execute the code:

Required Python tools: 

1. xhtml2pdf 
2. boto3
3. matplotlib
4. numpy
5. pandas
6. python Bluetooth Library
7. OpenCV
8. aws cli

Before Moving to the next steps, Please Create an AWS Account and generate the ACCESS KEY and SECRET KEY, and a S3 Bucket.


Steps to Run the code:
1. Clone or download the repository from the link (https://github.com/abhi-1203/VDHRM_SystemCode)
2. Make sure Python 3 is installed.
3. Install the above specified tools.
4. Extract the Cloned Repository to a folder
5. Configure AWS Account with your own ACCESS KEY, SECRET KEY, SERVER ZONE 
6. Execute the mainCode.py
7. Turn on Bluetooth Manually if it doesn't.
8. To initiate the process, the patient's data must be generated from the Android App.
9. Once the Patient data is generated through the app, the raspberry pi system code will receive the data via bluetooth and the process will be initiated.



Steps to Install the Android Application:

1. Download Android Studio
2. Download or clone the Android App from the repository- (https://github.com/abhi-1203/VDHRM)
3. Build the App.
4. After build is complete, Go to the project folder, open ReportTask.java file and replace the “aws-secret-key” with your AWS SECRET KEY, 
    and “aws-access-key with your AWS ACCESS KEY.
5. Click on Build and Run to install the app onto your Android Device.
6. Once installed, Login or signup, and click on Generate Report and follow the steps in the app.
7. The Generated Reports can be downloaded from the Read/ Access Report tab in the app.


Thank You! 
If any of the code or snippet does not work, please send a mail to abhijith1203@gmail.com




