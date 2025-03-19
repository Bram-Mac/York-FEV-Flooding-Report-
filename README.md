# How to Reproduce the Findings in this Report
After reading the full Report, the reader might want to use the Data provided to reproduce the findings made or expand on them. This will give a quick explanation on the code attached and how to use it.

# Data 
In the Data folder, you will find three csv files which is the file type needed when using data in Python. There are the two datasets, one for the flood in 2000 and one for the flood in 2015. The other file was only used to compare the two datasets to produce the linear regression model and hence the dataset for the year 2000. 

# Code
All the code given has specific titles so should be reasonably easy to find the code that you want to use.<br/>
To use the code, you will need to download the datasets as csv files. You will notice at the top of most of the python files there is a line which gives access to the data, for example: <br/>
**Data = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2015 Stage and Flow Data.csv')**. <br/> The reader will need to edit this line and change it so that it finds the file (that you have downloaded) in your computer. <br/> 
<br/>
The FEV for 2015 (Original, Rising Limb and Falling Limb) all have a threshold height $h_T$
