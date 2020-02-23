# AWSLambdaPacker

Usage Information: 

Have you ever tried using a Library like Pandas which is not available on AWS Lambda and felt frustrated? This python script takes care of your dependencies and packages them along with your Lambda Handler script so that you can directly upload the package to AWS Lambda.

Version:
	- 1.0.0 (Beta)

Requirements:
	- Works with Python3 (DOES NOT WORK WITH PYTHON2)
	- Works in Linux Box (Linux Environment)
	- requires curl (Please install curl if you don't have it already!)
	- permission to create file/directories in working directory
	

Instructions:
	- Edit the dependencies.json and fill the packages/modules you want installed
	- Optionally you can also edit the "scripts" tag if the 
	  Lambda Handler script is already available in your linux environment
	- Please use full path for Available scripts (Please see example dependency.json)
  	- Please keep dependencies.json in the same directory as packager.py
	- Run the script using "python packager.py" (Where your default python is Python3, else use "python3 packager.py")
	- This script will give you an output with the name of function.zip
	- You can directly attach this zip to your Lambda Function (if you have already passed on
	  your Lambda Handler Scripts)
	- Else copy your Lambda Handler scripts into function.zip and attach
	- You're free to rename function.zip with any name you want before attaching to Lambda
	- You will receive colourful warning messages if something goes wrong


Ongoing Developmennt:
	- Working on a way to configure AWS and directly attach it to Lambda (Please provide feedback if you want this to be enabled)
	
