from flask import Flask,request

import json
import openai



##############################################

app = Flask(__name__)

@app.route("/")
def hello_world():
    parameter_dict = request.args.to_dict()

    if len(parameter_dict) == 0:
        return 'parameter_error'

    try:
        

        openai.api_key = "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"
        
        ##response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)
        
        from api import GPT, Example, set_openai_key
        
        gpt = GPT(engine="davinci-instruct-beta",
                temperature=0.25,
                max_tokens=100)

        print(request.args['a'])

        output = gpt.submit_request(request.args['a'])
        print("5")
        print(output.choices[0]['text'])
        print("6")
        return output.choices[0]['text']


    except:
        return 'try_error'
if __name__ == '__main__':
    app.run(host='10.138.40.210', port=8000, debug=True)