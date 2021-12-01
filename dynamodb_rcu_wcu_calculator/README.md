This script will calculate Read Capacity Units and Write Capacity Units for a DynamoDB table based on given item size and read/writes per second parameters.

Example for an item size of 6 KB with 100 Item read/second and 40 Item write/second:
```
$ python capacity_calculator.py 6 100 40

Output:

Calculating RCU and WCU for an item size of 6 KB and 100 Item read/second and 40 Item write/second 

Read capacity units (Strongly Consistent) : 200
Read capacity units (Eventually Consistent) : 100
Read capacity units (Transactional) : 400
Write capacity units (Standard) : 240
Write capacity units (Transactional) : 480
```