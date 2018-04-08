import numpy as np 
import scipy as sp
import pandas as pd
import sys


#   |---------------|
#   |               |
#   |     EVENT     |  has a priority (translates to where exactly it will be placed, visually on the screen)
#   |               |  has a name (very simple) 
#   |---------------|  has tags (that can determine its priority)

#  -----------------------------------------------------------------------------------------------------------------------------------   
#  Each event is an object with crucial variables such as blurb (description), tags, time, and location
#
#  Created a class for the database, to simulate firebase, so that accessing it is done through class member functions
#
#  The simple terminal UI asks people to choose a selection from the list of events, then give it an interest value. 
#
#  The interest value is appended to the tags that the event contains in its tag section
#
#  Then, using a function (which iterates across the objects) the score of each event is updated using the complete tag-score database
#  (score = sigma(relevant_tag score)) 
#  -----------------------------------------------------------------------------------------------------------------------------------

class event_entry(object):
	def __init__(self, event_blurb, event_tags, event_time, event_location):
		self.tags = event_tags # tags are in array format, as they have non value associated with them
		self.blurb = event_blurb
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
		for tag in self.tags:
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
	def update_tag_score_dictionary(self, tags, interest_value):
		for tag_to_append in tags:
			self.tag_dictionary[tag_to_append] = self.tag_dictionary[tag_to_append] + interest_value
	def output_score_dictionary(self):
		''' No inputs, essentially outputs
		a score vector for all the relevant tags in the 
		app database. Will be used to update the 
		rankings of each event '''
		return self.tag_dictionary

def show_event_and_ranks(event_dictionary):
	print("These are the events and their rankings and scores:   ")
	for event in event_dictionary.keys():
		print(str(event) + "   Rank: " + str(event_dictionary[event].rank) + "    Score: " + str(event_dictionary[event].score))

def update_event_scores(event_dictionary, tag_score_dictionary):
	for event in event_dictionary.keys():
		event_dictionary[event].update_score(tag_score_dictionary)

# def update_event_ranks(event_dictionary, scores):
# 	for event in event_dictionary.keys():
# 		event_dictionary[event].update_rank(tag_score_dictionary)

if __name__ == "__main__":
	ranking_system = tag_ranking_system()
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

	with open('tag_scores.txt', 'a') as tag_scores:
		CONTINUE = 1
		while(CONTINUE == 1):
			show_event_and_ranks(app_events)
			CONTINUE = int(input("Would you like to continue? (1/0):\t\t"))
			if(CONTINUE == 0):
				show_event_and_ranks(app_events)
				sys.exit() # Exit the program
			else:
				print("Please pick one of the following: \n")
				print(app_events.keys())
				event_selection = str(input("Exact string selection please! NO GUI IS PROVIDED!\t\t"))
				print("\n" + app_events[event_selection].blurb)
				print(str(app_events[event_selection].time) + "\t" + str(app_events[event_selection].location) + "\n")
				event_interest = int(input("How interested are you in this even [0, 5]?\t\t"))
				ranking_system.update_tag_score_dictionary(app_events[event_selection].tags, event_interest) # update score for each TAG in the entire tag dictionary
				update_event_scores(app_events, ranking_system.tag_dictionary) # update the score for each event
				# See tag scores in the background, written to a file
				tag_scores.write("Chose " + str(event_selection) + " with interest of " + str(event_interest) + "\n")
				tag_scores.write(str(ranking_system.tag_dictionary))
				tag_scores.write("\n\n")