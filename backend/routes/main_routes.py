from flask import Blueprint, render_template, request

from backend.services.paraphraser import generate_paraphrases
from backend.services.grammar import check_spelling_grammar
from backend.services.sentiment import analyze_sentiment

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        phrase = request.form['phrase']

        paraphrases = generate_paraphrases(phrase)
        corrected_phrase = check_spelling_grammar(phrase)
        sentiment_label, polarity, subjectivity = analyze_sentiment(phrase)

        return render_template(
            'index.html',
            paraphrases=paraphrases,
            input_phrase=phrase,
            corrected_phrase=corrected_phrase,
            sentiment_label=sentiment_label,
            polarity=polarity,
            subjectivity=subjectivity
        )

    return render_template('index.html')

@main.route('/analyze')
def analyze():
    return render_template('analyze.html')

@main.route('/casual')
def casual():
    return render_template('casual.html')

@main.route('/interview')
def interview():
    return render_template('interview.html')

@main.route('/presentation')
def presentation():
    return render_template('presentation.html')