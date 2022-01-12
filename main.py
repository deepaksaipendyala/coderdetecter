from flask import Flask,render_template,request

d = Differ()
app = Flask('app')

def comparecode(code1,code2):
    text1 = code1
    text2 = code2
    lis=[]    
    print(type(text1))
    m = SequenceMatcher(None, text1, text2)
    a="The similarity between two python files is "+str(round(m.ratio() * 100, 2))+"%"
    # # print(a)
    lis.append(a)    
    b = list(
        d.compare(text1.splitlines(keepends=True),
                  text2.splitlines(keepends=True)))
    print(lis)
    b=""''.join(b)
    # # print(b)
    lis.append(b)
    return lis


@app.route('/')
def hello_world():
  return render_template('index.html')
@app.route('/submit_form',methods=['POST','GET'])
def Sumbit_form():
    if request.method=='POST':
        # try:
            data=request.form.to_dict()
            print(data)
            code1=data["code1"]
            code2=data["code2"]
            lis= comparecode(code1,code2)
            return render_template('index.html',r=lis[0],c=lis[1])
    #     except:
    #         return 'didnt save to database'
    else:
        return 'woops,Something went wrong'
        
app.run(host='0.0.0.0', port=8080)
