#!/bin/sh


#Update repository list
sudo apt-get update

#Install python
sudo apt-get -y install python

#Install pip3
sudo apt-get -y install python3-pip

#Use input of where the requirements.txt is to use that
pip3 install -r requirements.txt
