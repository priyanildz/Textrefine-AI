from spellchecker import SpellChecker

spell_checker = SpellChecker()

def check_spelling_grammar(phrase):
    corrected_phrase = ' '.join([
        spell_checker.correction(word) for word in phrase.split()
    ])
    return corrected_phrase