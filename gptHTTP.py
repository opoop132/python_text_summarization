from flask import Flask,request

import json
import openai



##############################################

app = Flask(__name__)

@app.route("/")
def hello_world():
    parameter_dict = request.args.to_dict()

    if len(parameter_dict) <= 1:
        return 'parameter_error'

    try:
        

        openai.api_key = "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"
        print("1")
        ##response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)
        print("2")
        from api import GPT, Example, set_openai_key
        print("3")
        gpt = GPT(engine="davinci-instruct-beta",
                temperature=0.5,
                max_tokens=int(request.args['b']))
        print("4")
        print(request.args['a'])
        print("5")
        output = gpt.submit_request(request.args['a'])
        print("6")
        print(output.choices[0]['text'])
        print("7")
        return output.choices[0]['text']


    except:
        return 'try_error'
if __name__ == '__main__':
    ##app.run(host='0.0.0.0:4999:5000', debug=True)
    app.run(host='10.138.41.170', port=5000, debug=True)