import numpy as np 
import scipy as sp
import pandas as pd

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
	def __init__(self, event_name, event_tags, event_time, event_location):
		self.tags = event_tags # tags are in array format, as they have non value associated with them
		self.name = event_name
		# other relevent details that will be used to rank events
		self.time = event_time
		self.location = event_location # this will be used to prioritize entries if there are conflicts (the 
		# tag-based rankings are the same for two different events)

		# member variables for ranking purposes:
		self.score = 0 # scoring determined by sigma tag * score of particular tag 
		self.rank = 0 # the final output for the object, determining the positioning of the event
	def update_score(self, tag_score_dictionary):
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
		self.tag_dictionary = {
			"gun control" : 0,			"tax" : 0,
			"women" : 0,			"finance" : 0,
			"first amendment" : 0,			"second amendment" : 0,
			"pro-life" : 0,			"pro-choice" : 0,
			"bullying" : 0,			"corruption" : 0,
			"political instability" : 0,			"climate change" : 0,
			"planned parenthood" : 0,			"medical" : 0,
			"health/obesity" : 0,			"animal rights/issues" : 0,
			"lgbtq" : 0,			"education" : 0,
			"poverty" : 0,			"antisemitism" : 0,
			"environment" : 0,			"food" : 0,
			"water security" : 0,			"racism" : 0,
			"working conditions" : 0, 			"minimum wage" : 0, 
			"pay issues" : 0,			"crime and justice system" : 0,
			"alcohol" : 0,			"drugs" : 0,
			"substance issues" : 0,			"terrorism" : 0,
			"large scale conflict" : 0,			"war" : 0
		}
	def update_score_dictionary(self, tags, interest_value):
		for tag_to_append in tags:
			self.tag_dictionary[tag_to_append] = self.tag_dictionary[tag_to_append] + interest_value
	def output_score_dictionary(self):
		''' No inputs, essentially outputs
		a score vector for all the relevant tags in the 
		app database. Will be used to update the 
		rankings of each event '''
		return self.tag_dictionary

def show_event_and_ranks(event_dictionary):
	print("These are the events and their rankings:   ")
	for event in event_dictionary.keys():
		print(str(event) + "   Rank: " + str(event_dictionary[event].rank))


if __name__ == "__main__":
	# Defining the blurbs for each event associated with this back-end demonstration
	parkland_blurb = """This event is made for people who are outraged on the Parkland Shooting.
	Attendees will primarily be focussing on gun laws, including the second amendment."""
	hackny_blurb = """Attend the HackNY 2018. This event is made for students who are interested in 
	applying this computer science skills"""
	occupy_wall_street_blurb = """Event for those who feel anger regarding the current wall street affairs"""
	planned_parenthood_march_blurb = """Pro-choice? Attend this rally!"""
	womens_march_blurb = """Women should get paid the same as men! Women should be treated the same as men in the 
	workplace! Come join the fight!"""
	# END OF BLURBS

	parkland = event_entry(parkland_blurb, ['gun control', 'second amendment', 
							'crime and justice system', 'political instability'], 
							pd.Timestamp('20180707 12:00:00'), 'New York City')
	hackny = event_entry(hackny_blurb, ['women', 'education', 'food'], 
						pd.Timestamp('20180704 12:00:00'), 'New York City')
	occupy_wall_street = event_entry(occupy_wall_street_blurb, ['first amendment', 'political instability'],
									pd.Timestamp('20180708 12:00:00'), 'New York City')
	planned_parenthood_march = event_entry(planned_parenthood_march_blurb, ['planned parenthood', 'health/obesity', 
											'pro-choice', 'crime and justice system'], pd.Timestamp('20180709 11:00:00'), 
											'New York City')
	womens_march = event_entry(womens_march_blurb, ['women', 'first amendment'], pd.Timestamp('20180710 10:00:00'), 
								'Philadelphia')

	app_events = {
		"Parkland March" : parkland,
		"HackNY 2018" : hackny,
		"Occupy Wall Street" : occupy_wall_street,
		"Planned Parenthood March" : planned_parenthood_march,
		'Women March' : womens_march
	}

	
	show_event_and_ranks(app_events)


	





	# new_object = tag_ranking_system()
	# print(new_object.tag_dictionary.keys())




# class event_entry(object):
# 	def __init__(self, event_name, event_priority, event_tags, event_time, event_location):
# 		self.tags = tags # tags are in array format, as they have non value associated with them
# 		self.priority = event_priority # a simple int or double format value
# 		self.name = event_name
# 		# other relevent details that will be used to rank events
# 		self.time = event_time
# 		self.location = event_location # this will be used to prioritize entries if there are conflicts (the 
# 		# tag-based rankings are the same for two different events)	

	# def __init__(self):
	# 	self.tag_dictionary = {
	# 		"gun control" : 0,
	# 		"tax" : 0,
	# 		"women" : 0,
	# 		"finance" : 0,
	# 		"first amendment" : 0,
	# 		"second amendment" : 0,
	# 		"pro-life" : 0,
	# 		"pro-choice" : 0,
	# 		"bullying" : 0,
	# 		"corruption" : 0,
	# 		"political instability" : 0,
	# 		"climate change" : 0,
	# 		"planned parenthood" : 0,
	# 		"medical" : 0,
	# 		"health/obesity" : 0,
	# 		"animal rights/issues" : 0,
	# 		"lgbtq" : 0,
	# 		"education" : 0,
	# 		"poverty" : 0,
	# 		"antisemitism" : 0,
	# 		"environment" : 0,
	# 		"food" : 0,
	# 		"water security" : 0,
	# 		"racism" : 0,
	# 		"working conditions" : 0, 
	# 		"minimum wage" : 0, 
	# 		"pay issues" : 0,
	# 		"crime and justice system" : 0,
	# 		"alcohol" : 0,
	# 		"drugs" : 0,
	# 		"substance issues" : 0,
	# 		"terrorism" : 0,
	# 		"large scale conflict" : 0,
	# 		"war" : 0
	# 	}