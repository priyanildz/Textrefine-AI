from parrot import Parrot

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

def generate_paraphrases(phrase):
    para_phrases = parrot.augment(input_phrase=phrase)
    return para_phrases