import numpy as np 
import scipy as sp

# object for the score aggregator and sorter
# injector method to supply data into the array 
# method to sort entries of the data structure at every calling


#   |---------------|
#   |               |
#   |     EVENT     |  has a priority (translates to where exactly it will be placed, visually on the screen)
#   |               |  has a name (very simple) 
#   |---------------|  has tags (that can determine its priority)
#
#

class event_entry(object):
	def __init__(self, event_name, event_priority, event_tags, event_time, event_location):
		self.tags = tags # tags are in array format, as they have non value associated with them
		self.priority = event_priority # a simple int or double format value
		self.name = event_name
		# other relevent details that will be used to rank events
		self.time = event_time
		self.location = event_location # this will be used to prioritize entries if there are conflicts (the 
		# tag-based rankings are the same for two different events)

		# member variables for ranking purposes:
		self.score = 0 # scoring determined by sigma tag * score of particular tag 
		self.rank = 0 # the final output for the object, determining the positioning of the event
	def update_score(self, tag_score_dictionary):
		''' Tag score vector is a datastructure 
		outputed by the tag_ranking_system function 
		named output_score_vector '''
		updated_score = 0
		for tag in tags:
			# tags is an array containing strings of tag names
			updated_score = updated_score + tag_score_dictionary[tag]
		self.score = updated_score
	def assign_rank(self, updated_rank):
		# new rank is injected by the sorting algorithm according to event scores
		self.rank = updated_rank

class tag_ranking_system(object):
	def __init__(self):
		tag_dictionary = { 
			
		}
	def output_score_dictionary(self):
		''' No inputs, essentially outputs
		a score vector for all the relevant tags in the 
		app database. Will be used to update the 
		rankings of each event '''

if __name__ == "__main__":
	new_object = tag_ranking_system()