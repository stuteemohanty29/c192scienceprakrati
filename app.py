from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

answer_dict = {
                "1": ["solid", "liquid", "gas", "small", "cooling", "Evaporation", "K", "Pa"],
                "2": ["fundamental", "leucoplasts ", "Robert Hooke", "1665", "latin", "Leeuwenhoek", "Robert Brown","Purkinje","Schleiden and Schwann","Virchow"],
                "3": ["v = u + at","s = ut +1/2a(t x t)","2as = (v x v)-(u x u)","t","s","v","u","a"]
        }

stories = [
    {
        "inputs": 8,
        "title": "Chemistry time",
        "story": 'There are 3 states of matter <span class="rep_input">_____</span>,<span class="rep_input">_____</span>,<span class="rep_input">_____</span>.Matter is made up of <span class="rep_input">_____</span>particles.Evaporation causes<span class="rep_input">_____</span>. <span class="rep_input">_____</span> is a surface phenomenon.Kelvin is denoted with letter<span class="rep_input">_____</span>,and Pascal is donated by letters<span class="rep_input">_____</span>.',
        "words": ["cooling", "K", "Evaporation", "gas", "Pa", "liquid", "small", "solid"],
        "story_id": "1"
    },
    {
        "inputs": 7,
        "title": "Lets Revise Biology",
        "story": 'The<span class="rep_input">_____</span>organisational unit of life is the cell.The primary function of<span class="rep_input">_____</span>is storage.<span class="rep_input">_____</span>discovered dead cell in <span class="rep_input">_____</span>.Cell is a <span class="rep_input">_____</span>word which means a little room.<span class="rep_input">_____</span>discovered first living cell in 1674 in pond water.<span class="rep_input">_____</span>discovered nucles in 1831.<span class="rep_input">_____</span>discovered protoplasm in 1839.<span class="rep_input">_____</span>presented the old cell theory in 1839, then in 1855<span class="rep_input">_____</span>presented the new cell thoery',
        "words": ["Robert Hooke", "Robert Brown", "leucoplasts ", "Purkinje", "latin", "fundamental", "1665","Virchow","Leeuwenhoek ","Schleiden and Schwann"],
        "story_id": "2"
    },
    {
        "inputs": 8,
        "title": "Lets Test Your Physics",
        "story": 'Mention 3 equations for uniform accleration<span class="rep_input">_____</span>,<span class="rep_input">_____</span>,<span class="rep_input">_____</span>.Time is donated with letter<span class="rep_input">_____</span>.Distance/Displacement is donated by letter<span class="rep_input">_____</span>.Speed is donated by letter<span class="rep_input">_____</span>.Inecial Vilocity is donate with letter<span class="rep_input">_____</span>.Accleration is donted by letter<span class="rep_input">_____</span>.',
        "words": ["s", "a", "v = u + at","v", "2as = (v x v)-(u x u)", "u", "s = ut +1/2a(t x t)", "t"],
        "story_id": "3"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-story")
def get_story():
    return jsonify({
        "status": "success",
        "story": random.choice(stories)
    })

@app.route("/post-answers", methods=["POST"])
def post_answers():
    story_id = request.json.get("story_id")
    values = request.json.get("values")
    answers = answer_dict.get(story_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)