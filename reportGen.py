# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:30:07 2020

@author: Abhijith
"""

from string import Template
from xhtml2pdf import pisa  



# Utility function
def convertHtmlToPdf(Udata):
    
    sourceHtml = """<html>
                    <head>
                    <style>
                        table {
                                font-family: arial, sans-serif;
                                border-collapse: collapse;
  
                              }
                        th,td {
                        
                                border: 1px solid #dddddd;
                                text-align: left;
                                padding: 2px;
                             }
                        h1{
                                font-size: 25px;
                         }
                        tr:nth-child(even) {
                                background-color: #dddddd;
                        }
                            
                    </style>
                    </head>
                    <body><h1 align="center">Test Report</h1> 
                        <h3 align="right">Date: $date<br>Report ID: $ReportNo </h3>
                        
                        <table>
                            <tr>
                                <th>Name:</th>
                                <td>$name</td>
                                <th>Email:</th>
                                <td>$email</td>
                            </tr>
                            <tr>
                                <th>Age:</th>
                                <td>$age</td>
                                <th>Phone:</th>
                                <td>$phone</td>
                            </tr>
                            <tr>
                                <th>DocName:</th>
                                <td>$DocName</td>
                            </tr>
                            <tr>
                                <th>HospName:</th>
                                <td>
                                <div style=" max-width:1px; width: 442px; word-wrap: break-word; overflow-wrap:break-word;">
                                    $HospName
                                </div></td>
                            </tr>
                            <tr>
                                <th>TestType:</th>
                                <td>$TestType</td>
                            </tr>
                            <tr>
                                <th>Problem:</th>
                                <td>$problem</td>
                            </tr>
                            <tr>
                                <th>Description:</th>
                                <td>$description</td>
                            </tr>
                            
                            </tr>
                            </table>
                            <div>
                                <h2>Results:</h2>"""

    if(Udata['TestType'] =='0'):
        st=  """ <h2>Vein Detection Test Report</h2><br/>
                <img src="Final.jpg" alt="report" style="width:100%;height:100%;"></img><br/> """
    elif(Udata['TestType'] =='1'):
        st= """<h2>Heart Rate Test Report:</h2><br/>"""
    else:
        st=  """<h2>Vein Detection Test Report</h2>
        <img src="Final.jpg" alt="report" style="width:100%;height:1000px;"></img><br/> 
        <h2>Heart Rate Test Report:</h2>
        <img src="Final.jpg" alt="report" style="width:100%;height:1000px;"></img><br/>
        """
    sourceHtml=sourceHtml+st+""" <h2> Download Report:</h2>
        <a href=$downloadLink >Click here to download</a></div></body></html>"""
                    
    s=Template(sourceHtml).safe_substitute(name=Udata['Name'],
                                       age=23,#Udata['age'],
                                       DocName=Udata['DoctorName'],
                                       HospName=Udata['HospName'],
                                       TestType=Udata['TestType'],
                                       email=Udata['email'],
                                       phone=Udata['phone'],
                                       date=Udata['date'],
                                       ReportNo=Udata['ReportID'],
                                       problem=Udata['problem'],
                                       description=Udata['description'],
                                       downloadLink=Udata['DownloadLink'])
                                       
    outputFilename = "1231233123123.pdf"
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")
    # convert HTML to PDF
    pisaStatus = pisa.pisaDocument(s, dest=resultFile) 
    # close output file
    resultFile.close()                 # close output file
    # return True on success and False on errors
    return pisaStatus.err

