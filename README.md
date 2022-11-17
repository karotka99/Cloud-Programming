# Cloud-Programming

Here you can find prepared endpoint in Flask, which display plot of the quadratic function.\
The endpoint gets in URL parameters of the quadratic function and limits of the plot. 

# How to view it?

Firstly, you have to clone this repository. To do this you have to open Git Bash. Write:
```
git clone https://github.com/karotka99/Cloud-Programming.git
```
Please put the cloned file to the Desktop.
Nextly, you have to open Anaconda Powershell Prompt and there you have to get to the file by writing:
```
cd Desktop\Cloud-Programming
```
Now, don't close Anaconda Powershell Prompt and open Docker Desktop. Coming back to the Anaconda Powershell Prompt write the following commands to build an image:

```
docker build -t function_app:v1.0 . 
 ```
 Wait until it will be ready and write the following comment to run the container:
 ```
 docker run --rm -it -p 5000:5000 function_app:v1.0
 ```
 
Now you have to display site in such way:
http://localhost:5000/?a=1&b=-4&c=4&xmin=-5&xmax=10&ymin=0&ymax=10


Parameters $a$, $b$ and $c$ means parameters for quadratic function: 
$$f(x)=ax^2+bx+c$$

Parameters $x_{min}$, $x_{max}$, $y_{min}$ and $y_{max}$ means domain and the set of values:
$$x \in (x_{min},x_{max}) ~~~~~~~~~~y \in (y_{min},y_{max})$$

You can enter your own values to see function with chosen parameters, domain and the set of values.\
However you have to remember that following conditions have to be met:
$$x_{max} > x_{min},~~~~~~ y_{max} > y_{min}.$$
Don't worry if you forgot about some of the parameters :) \
Site will work, but with predetermined numbers $a=1$, $b=0$, $c=0$, $x_{min}=-5$, $x_{max}=5$, $y_{min}=-5$, $y_{max}=5$.\
If you run http://localhost:5000/ you will see plot of predefined function:
$$f(x)=x^2, ~~ x\in (-5,5), ~~ y \in (-5,5).$$
\
\
But please, don't go crazy with parameters. Application is not prepared for problems like: what if $x_{min}> x_{max}$. So you have to write good numbers.
\
\
At the end you can remove the image by wirting following command:
```
docker image rm function_app:v1.0
```
