# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:23:42 2020

@author: Abhijith
"""

import boto3
#import os
#import sys
import logging
import pandas as pd
import matplotlib.pyplot as plt
#import datetime
from botocore.exceptions import ClientError

#function to upload files to s3 bucket.
def upload_file(filename, key):
    
    #d = datetime.datetime.now()
    #Extract timestamp, for unique identification to name the files/ objects
    #timestamp ="{}-{}-{}-{}-{}-{}".format(d.year,d.month,d.day,d.hour,d.minute,d.second)
    #s3 client object
    s3obj = boto3.client('s3')
    #Bucket Name
    s3bucketName= 's3veinbucket145218-dev'
    # Read a file in binary
    data = open("1231233123123.pdf", 'rb')
    #s3 Folder Name
    foldername = key#Udata['UserId']
    #try uploading a file to the specified foldername and bucket name
    try:
        print("Inside try")
        res = s3obj.put_object(ACL='public-read',Bucket=s3bucketName,
                            Key=foldername+'/'+filename, Body=data)
        #if HTTP request is 200, upload is success. returns true
        if res['ResponseMetadata']['HTTPStatusCode'] == 200 :
            print("Uploaded file successfully")
            return True
    except ClientError as e:
        logging.error(e)
        return False


#function to download files from s3 bucket.
def download_files():
    #write download code here.
    
    return True
    
#function to list files from s3 bucket.
def list_files():
    #s3 client object
    s3obj = boto3.client('s3')
   
    #s3 Folder Name
    foldername = "jayatest"
    #Bucket Name
    s3bucketName= 's3veinbucket145218-dev'
    
    #try uploading a file to the specified foldername and bucket name
    try:
        response = s3obj.list_objects(Bucket=s3bucketName,Prefix=foldername)
        for x in response.get("Contents"):
            res= str(x.get("Key"))
            fileName = res.replace(foldername+'/','')
            print('FileName: '+fileName)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    

#list_files()
#print(rs)


