# WeVo Platform

## We build more inclusive cities with data and analytics.

### Summary

WeVo is a civic engagement platform designed to help land development and building project stakeholders incorporate community feedback into their projects, reduce paper consumption, conserve resources by managing project risk, analyze public sentiment and predict community response.

### Objectives

The project objectives are as follows:

1. Reduce project risk by minimizing project delays and lawsuits
2. Allow constituents to vote on projects and initiatives
3. Allow project owners to track voting and sentiment

### Background

This project started at [Startup Weekend Sacramento](http://communities.techstars.com/usa/sacramento/startup-weekend/14400) in June 2019 with the goal of increasing civic engagement, reducing project risk and helping build more inclusive cities.

### Methodology

This project was developed based on coach feedback and custom development during the event; it pivoted into this concept for the following reasons:

1. Customers have a pain point with costly project delays and lawsuits
2. Constituents may not be involved with the civic engagement process
3. Project owners are required by law to hold public comment periods
4. Project satisfies multiple portions of the sustainability model
5. This project was developed based on the tutorial listed below

### Tutorial Example - DonorsChoose_Visualization

* Based on this [tutorial blog post](http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/)
* [Author Blog - Adil Moujahid](http://adilmoujahid.com)

### Getting Started

The dependencies for the project can be installed using

    $ pip install -r requirements.txt

You can use ``Vagrant`` to start a machine with a MongoDB instance running

    $ vagrant up

To initialize the database you need to download the data

    $ wget https://s3.amazonaws.com/open_data/csv/opendata_projects.zip && unzip opendata_projects.zip

and import it

    $ mongoimport -d donorschoose -c projects --type csv --file /vagrant/opendata_projects.csv -headerline
