from flask import Flask,render_template_string,request

app=Flask(__name__)
 
indexhtml="""
<html>
<title>just a test</title>
<body><h1>
why not come <a href="ssti">here </a>to have a look</h1>
</h1></body>
</html>
"""
 
whoareuhtml="""
<html>
<title>here s ssti</title>
<body>
<h3>you should tell me who you are then i can say hello to u!(use ?name= in url)</h3>
</body>
</html>
"""
 
tinyhtml="""
<html>
<title>here s ssti</title>
<body>
<h1>hello %s</h1>
</body>
</html>
"""
 
@app.route("/index")
@app.route("/")
def index():
    return indexhtml
 
@app.route("/ssti")
def ssti():
    name=request.args.get("name")
    if not name:
        return render_template_string(whoareuhtml)
    else:
        return render_template_string(tinyhtml%name)
 
if __name__=="__main__":
    app.run(debug=True)