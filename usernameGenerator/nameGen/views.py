from django.shortcuts import render
from django.http import HttpResponse

import random
from nltk.corpus import wordnet

# Create your views here.
def index(response):
    return render(response, "nameGen/base.html", {})

def home(response):
    return render(response, "nameGen/home.html", {})

isListGenerated = False
nouns = list(wordnet.all_synsets(wordnet.NOUN))
adjectives = list(wordnet.all_synsets(wordnet.ADJ))

def generate_word(response):
    global nouns
    global adjectives

    noun = random.choice(nouns).lemmas()[0].name()
    adjective = random.choice(adjectives).lemmas()[0].name()

    context = {'noun': noun, 'adjective': adjective}
    return render(response, "nameGen/generate_word.html", context)