How to use this program

to run this app, you need to download virtualbox and vagrant and download this repo https://github.com/udacity/fullstack-nanodegree-vm

vagrant up 
vagrant ssh

load the sample data newsdata from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
by using this command

psql -d news -f newsdata.sql

now run:
python3 main.py


 
 