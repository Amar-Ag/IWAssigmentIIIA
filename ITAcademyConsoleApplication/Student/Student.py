import csv

import pandas as pan


class Student:
    def __init__(self,
                 fullName,
                 emailAddress,
                 phoneNumber,
                 collegeName,
                 course,
                 depositAmount,
                 ):
        self.fullName = fullName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.collegeName = collegeName
        self.course = course
        self.depositAmount = depositAmount
        self.remainingAmount = 20000 - self.depositAmount

    def save_record(self):
        with open('./student.csv', 'a+', newline='') as file:
            # df = pan.read_csv('./student.csv')
            fileTitles = ['name', 'emailAddress', 'phoneNumber', 'collegeName',
                          'course', 'depositAmount', 'remainingAmount']
            writer = csv.DictWriter(file, fieldnames=fileTitles)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(
                {'name': f'{self.fullName}',
                 'emailAddress': f'{self.emailAddress}',
                 'phoneNumber': f'{self.phoneNumber}',
                 'collegeName': f'{self.collegeName}',
                 'course': f'{self.course}',
                 'depositAmount': f'{self.depositAmount}',
                 'remainingAmount': f'{self.remainingAmount}'})
