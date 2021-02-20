from django.db import models
import json
import csv

class Book(models.Model):
    book_title = models.CharField (max_length = 250)
    author = models.CharField (max_length = 250)
    publication_date = models.CharField (max_length = 25)
    plot_summary  = models.TextField ()
  

def __str__ (self):
    return self.book_title

objects = models.Manager()


class Autocomplete(models.TextField):

    def __init__(self, sentences, times):
        self.search = ''
        self.history = defaultdict(int)
        for i in range (len(sentences)):
            self.history[sentences[i]] = times [i]
        self.matches = []

    def input (self,C):
        if C == '#':
            self.history [self.search] +=1 
            self.search = ''
            self.matches = []
            return

        if not self.search:
            for sentence in self.history:
                if sentence [0] == C:
                    self.matches.append([sentence, self.history[sentence]])

            self.matches.sort(key=lambda x: (-x[1], x[0]))
            self.matches = [x[0] for x in self.matches]

            if self.search:
                
                i = len (self.search)
                self.matches = [match for match in self.matches if len(match)> i and match[i] == C ]

            self.search += C
            return self.matches[:3]

  