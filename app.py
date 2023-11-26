from flask import Flask, render_template, request

app = Flask(__name__)

def flames(n1, n2):
    s1 = list(str(n1))
    s2 = list(str(n2))
    
    if len(n1) == 0 or len(n2) == 0:
        return 'Dont you have a crush or Have you forgot your name..?'

    for i in range(len(n1)):
        if n1[i] in s2:
            s2.remove(n1[i])
            s1.remove(n1[i])

    c = len(s1) + len(s2)
    s = 'flames' * c * c
    a = []
    t = 1

    for i in s:
        if len(a) == 5:
            break
        if t == c and i not in a:
            a.append(i)
            t = 1
            continue
        if i in a:
            continue
        else:
            t += 1

    p = set('flames') - set(a)

    for x in p:
        if x == "f":
            return n1 + " and " + n2 + " are friends"
        elif x == "l":
            return n1 + " and " + n2 + " are in LOVE :)"
        elif x == "a":
            return n1 + " " + n2 + " are in the attraction phase"
        elif x == "m":
            return n1 + " and " + n2 + " will get married :)"
        elif x == "e":
            return n1 + " and " + n2 + " are enemies"
        elif x == "s":
            return "bruhh..ig you both are siblings"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']

        result = flames(input1, input2)

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
