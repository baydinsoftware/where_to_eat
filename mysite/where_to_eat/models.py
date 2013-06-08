from django.db import models

class Ballot(models.Model):
    date = models.DateTimeField('date')
    voting_method = models.CharField(max_length=200, default='plurality_voting')
    winner = models.CharField(max_length=200, default='')
    
    def __unicode__(self):
        return str(self.date)
    
class Restaurant(models.Model):
    ballot = models.ForeignKey(Ballot)
    name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
        
class Voter(models.Model):
    ballot = models.ForeignKey(Ballot)
    name = models.CharField(max_length=200)
    votes_submitted = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
