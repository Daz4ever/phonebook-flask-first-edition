from flask import Flask, render_template

app = Flask('MyApp')

@app.route('/')

def helloworld():

    return render_template(
        'helloworld.html',
        title = 'Hello World'
        )

if __name__ == '__main__':
    app.run(debug=True)
