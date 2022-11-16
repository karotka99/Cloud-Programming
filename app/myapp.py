from flask import Flask, request, escape
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from flask import Flask
import numpy as np

plt.rcParams["figure.figsize"] = [10.50, 8.50]
plt.rcParams["figure.autolayout"] = True
app = Flask(__name__)

@app.route("/")
def function():
    xmin= int(request.args.get('xmin',-5))
    a=int(request.args.get('a',1))
    b=int(request.args.get('b',0))
    c=int(request.args.get('c',0))
    xmax=int(request.args.get('xmax',5))
    ymin=int(request.args.get('ymin',-5))
    ymax=int(request.args.get('ymax',5))
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = np.arange(xmin,xmax,0.1)
    ys = [a*x**2+b*x+c for x in xs]
    axis.plot(xs, ys)
    axis.set_xlim((xmin,xmax))
    axis.set_ylim((ymin,ymax))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')




