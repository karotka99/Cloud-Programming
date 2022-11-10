# Cloud-Programming

Here you can find prepared endpoint in Flask, which display plot of the quadratic function.\
The endpoint gets in URL parameters: a, b, c and limits of the plot. 

# How to view it?

Firstly, you have to clone this repository. Next, run it using Docker.

 -docker image rm task3_app:v1.0\
 -docker run --rm -it -p 5000:5000 task3_app:v1.0

To view the plot you have to display site in such way:
http://localhost:5000/?xmin=-5&xmax=10&ymin=0&ymax=10&a=1&b=-4&c=4

Don't worry if you forgot about some of the parameters :) \
Site will work, but with predetermined numbers.
