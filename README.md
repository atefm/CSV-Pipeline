# CSV-Pipeline
===================
DESCRIPTION
===================
This project allows data in CSV to be coneverted to various formats. Currently, only Json and Html is supported but the project can easily be extended to support more formats. A sample CSV data file is provided with customised validation rules for a particular (hotels) case. Ouput in HTML and JSON format is also provided.


===================
REQUIREMENTS
===================
python 2.7


===================
INSTRUCTIONS
===================

To run the program:

python pipeline.py -i "input file" -f "output format" 

example:

python pipeline.py -i hotels.csv -f json 
