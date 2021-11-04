from flask import Flask, render_template, session, redirect, request
from friends import Friend


app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    print("**** in index ****")
    all_friends = Friend.get_all()
    print(all_friends)

    for idx in range(len(all_friends)):
        print(all_friends[idx].first_name,all_friends[idx].last_name, all_friends[idx].occupation)

    return render_template("index.html")


    # if request.form['number_guess'] != "":
    #     session['number_guess'] = int(request.form['number_guess'])
    #     session['input_error'] = 0
    # else:
    #     session['number_guess'] = 50
    #     session['input_error'] = 1
    print("Got number guess of:", session['number_guess'], "from form post :: Message:", session['message'])
    return redirect("/")

# @app.route('/increment_by', methods=['POST'])
# def increment_by():

#     return redirect("/")

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)    