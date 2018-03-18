import pandas as pd
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'serif';
mpl.rcParams['font.size'] = 12;

import shutil

def plotStackedBar( data, scores, labels, labelsTicks, xlabel, ylabel, legend,  colors, filename):

	# Create the general blog and the "subplots" i.e. the bars
	f, ax1 = plt.subplots(1, figsize=(5,3))

	# Set the bar width
	bar_width = 0.75

	# positions of the left bar-boundaries
	bar_l = range(len(labels))

	# positions of the x-axis ticks (center of the bars as bar labels)
	tick_pos = [i+(bar_width) for i in bar_l]

	bottoms = 100*np.ones( len(labels) )

	for idx, factor in enumerate(scores):
		data_row = []
		for label in labels:
			# Each row corresponds to a score of every labels.
			data_row.append( data[label][idx] )

		bottoms -= np.array( data_row ) 

		# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
		ax1.bar(bar_l, 
	        # using the pre_score data
	        data_row,
	        # emotion_factor_impact_of_each_method[factor],
	        # set the width
	        width=bar_width,
	        # with the label pre score
	        label=factor, 
	        # with alpha 0.5
	        alpha=1, 
	        # with color
	        bottom=bottoms,
	        edgecolor="k",
	        color=colors[factor])

	# set the x ticks with names
	plt.xticks(tick_pos, labelsTicks, rotation=45, ha='right' )

	# Set the label and legends
	if ylabel: 
		ax1.set_ylabel(ylabel)
	ax1.set_xlabel(xlabel)
	ax1.xaxis.set_ticks_position('none')
	plt.grid(True)
	plt.ylim([0,100])
	if legend:
		plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=14)

	# Set a buffer around the edge
	plt.xlim([min(bar_l)-(1-bar_width), max(bar_l)+1])

	# filename = "emotion_factor_dist_stacked_bar.eps"
	plt.savefig(filename, format='pdf', bbox_inches='tight', pad_inches=0.05)



df = pd.read_csv("data-all.csv")
scores = ["Do NOT Share", "Partially Share", "Entirely Share"]
scores_colors = dict(zip(scores,["#d7191c", "#ffffbf", "#1a9641"]))

annotation_y_position = -53

# Create the general blog and the "subplots" i.e. the bars
# f, ax1 = plt.subplots(figsize=(10,3))
# f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(16,4), gridspec_kw = {'width_ratios':[12, 6, 1]})
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(16,3), gridspec_kw = {'width_ratios':[12, 6]})

# Set the bar width
bar_width = 1


# Image Type
imageTypes = ["Friends", "Activity", "Selfie", "Food", "Pet", "Gadget", "Fashion", "Caption"]
imageTypesTicks = ["Friends", "Activity", "Selfie", "Food", "Pet", "Gadget", "Fashion", "Caption Photo"]
imageTypesArray = dict(zip(imageTypes,[[],[],[],[],[],[],[],[]]))
imageTypesDist = dict(zip(imageTypes,[[],[],[],[],[],[],[],[]]))
for i in range(df.shape[0]):
	imagetype = df["I.categoryName"][i]
	decision  = df["A.answer"][i]
	imageTypesArray[imagetype].append(decision)

for key in imageTypesDist:
	for answer in [1,2,5]:
		proportion = 100 * imageTypesArray[key].count(answer) / float(len(imageTypesArray[key])) # proportion of the answer
		imageTypesDist[key].append(proportion)

# plotStackedBar( imageTypesDist, scores, imageTypes, imageTypesTicks, "Image Type", "Proportion (\%)", True, scores_colors, "dist_decisions_imagetype.pdf" )

labels = imageTypes
# positions of the left bar-boundaries
bar_l = range(len(imageTypes))

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = imageTypesDist
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax1.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # with the label pre score
        label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])
ax1.annotate('Image Type', xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)


# No. of people in image
numPeople = ['0', '1', '2', '3', '4', '5', '6']
numPeopleTicks = ['0', '1', '2', '3', '4', '5', '6 or more']
numPeopleArray = dict(zip(numPeople,[[],[],[],[],[],[],[]]))
numPeopleDist = dict(zip(numPeople,[[],[],[],[],[],[],[]]))
for i in range(df.shape[0]):
	numpeople = df["I.nb_person"][i]
	decision  = df["A.answer"][i]
	numPeopleArray[str(numpeople)].append(decision)

for key in numPeople:
	for answer in [1,2,5]:
		proportion = 100 * numPeopleArray[key].count(answer) / float(len(numPeopleArray[key])) # proportion of the answer
		numPeopleDist[key].append(proportion)

# plotStackedBar( numPeopleDist, scores, numPeople, numPeopleTicks, "Number of people in image", None, False, scores_colors, "dist_decisions_numpeople.pdf" )


# positions of the left bar-boundaries
offset = 0
offset += len(bar_l)+1
bar_l = range(offset, offset+len(numPeople))

labels = numPeople

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos += [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = numPeopleDist
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax1.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # # with the label pre score
        # label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])
ax1.annotate('\# of People', xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)

# identities in picture
identities = ["I.family", "I.friends", "I.boy_girlfriend", "I.school_work", "I.myself", "I.acquaintance", "I.stranger", "I.celebrity"]
identitiesTicks = ["Family", "Close friends", "Girl/Boyfriend", "School/Colleague", "Myself", "Acquaintance", "Stranger", "Celebrity"]
identitiesArray = dict(zip(identities,[[],[],[],[],[],[],[],[]]))
identitiesDist = dict(zip(identities,[[],[],[],[],[],[],[],[]]))
for i in range(df.shape[0]):
	for id in identities:
		if df[id][i] == 1:
			identitiesArray[id].append( df["A.answer"][i] )

for key in identities:
	for answer in [1,2,5]:
		proportion = 100 * identitiesArray[key].count(answer) / float(len(identitiesArray[key])) # proportion of the answer
		identitiesDist[key].append(proportion)
# plotStackedBar( identitiesDist, scores, identities, identitiesTicks, "Identity in picture", None, False, scores_colors, "dist_decisions_ids_picture.pdf" )

# positions of the left bar-boundaries
labels = identities
offset += len(bar_l)+1
bar_l = range(offset, offset+len(labels))

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos += [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = identitiesDist
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax1.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # # with the label pre score
        # label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])
ax1.annotate('Identity in Picture', xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)


# Picture Location
picLocation = ['ArtsEntertainment', 'School', 'Event', 'Food', 'Nightlife', 'Outdoors', 'Professionals', 'OwnHome', 'OtherHome', 'ShopService', 'TravelTransport', 'Undefined']
picLocationTicks = ['Entertainment', 'School', 'Event', 'Restaurant/Bar', 'Nightlife', 'Outdoors/Recreation', 'Professionals', 'Home', 'Others Home', 'Shop/Service', 'Travel/Transport', 'Undefined']
picLocationArray = dict(zip(picLocation,[[],[],[],[],[],[],[],[],[],[],[],[]]))
picLocationDist = dict(zip(picLocation,[[],[],[],[],[],[],[],[],[],[],[],[]]))
for i in range(df.shape[0]):
	location = df["I.placeName"][i]
	decision  = df["A.answer"][i]
	picLocationArray[location].append(decision)

for key in picLocation:
	for answer in [1,2,5]:
		proportion = 100 * picLocationArray[key].count(answer) / float(len(picLocationArray[key])) # proportion of the answer
		picLocationDist[key].append(proportion)

# plotStackedBar( picLocationDist, scores, picLocation, picLocationTicks, "Location of the picture", None, False, scores_colors, "dist_decisions_pic_location.pdf" )

# positions of the left bar-boundaries
labels = picLocation
offset += len(bar_l)+1
bar_l = range(offset, offset+len(labels))

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos += [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = picLocationDist
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax1.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # # with the label pre score
        # label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])

ax1.annotate('Location of Picture', xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)

# set the x ticks with names
labelsTicks = imageTypesTicks + numPeopleTicks + identitiesTicks + picLocationTicks
ax1.set_xticks(tick_pos)
ax1.set_xticklabels(labelsTicks, rotation=45, ha='right' )


# # Set the label and legends
# if ylabel: 
# 	ax1.set_ylabel(ylabel)
# ax1.set_xlabel(xlabel)
# ax1.xaxis.set_ticks_position('none')
ax1.grid(True)
ax1.set_ylim([0,100])
# if legend:
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=8)

# Set a buffer around the edge
ax1.set_xlim([0-(2-bar_width), max(bar_l)+2])

ax1.set_ylabel("Proportion (\%)")
ax1.set_title(r"Image Semantic Features (partial)")
# filename = "emotion_factor_dist_stacked_bar.eps"
# filename = "decision_dist_image_info.pdf"
# plt.savefig(filename, format='pdf', bbox_inches='tight', pad_inches=0.05)
# shutil.copy(filename, "/Users/yuanlin/PhD/Conference/2017_IFIP_SEC/paper/images/"+filename)









########### Plot requesters ##########
# Identities of requester
requesters = ['a family member', 'a close friend', 'a school mate or work colleague', 'a boyfriend or girlfriend', 'an acquaintance', 'a stranger']
requestersTicks = ['Family', 'Close friend', 'School/Colleague', 'Girl/Boyfriend', 'Acquaintance', 'Stranger']
requestersArray = dict(zip(requesters,[[],[],[],[],[],[]]))
requestersDist = dict(zip(requesters,[[],[],[],[],[],[]]))
for i in range(df.shape[0]):
	requester = df["Q.identity"][i]
	decision  = df["A.answer"][i]
	requestersArray[requester].append(decision)

for key in requesters:
	for answer in [1,2,5]:
		proportion = 100 * requestersArray[key].count(answer) / float(len(requestersArray[key])) # proportion of the answer
		requestersDist[key].append(proportion)

# plotStackedBar( requestersDist, scores, requesters, requestersTicks, "Identitiy of requester", None, False, scores_colors, "dist_decisions_requesters.pdf" )

# Create the general blog and the "subplots" i.e. the bars
# f, ax1 = plt.subplots(1, figsize=(6,3))
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(7,3), gridspec_kw = {'width_ratios':[6, 1]})
# Set the bar width
bar_width = 1
labels = requesters
# positions of the left bar-boundaries
bar_l = range(len(requesters))

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = requestersDist
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax2.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # with the label pre score
        # label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])
ax2.annotate("Identity", xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)

labelsTicks = []
labelsTicks += requestersTicks


# Gender of requester
requesters = ['she', 'he']
requestersTicks = ['Female', 'Male']
requestersArray = dict(zip(requesters,[[],[]]))
requestersDist = dict(zip(requesters,[[],[]]))
for i in range(df.shape[0]):
	requester = df["Q.gender"][i]
	decision  = df["A.answer"][i]
	requestersArray[requester].append(decision)

for key in requesters:
	for answer in [1,2,5]:
		proportion = 100 * requestersArray[key].count(answer) / float(len(requestersArray[key])) # proportion of the answer
		requestersDist[key].append(proportion)

# plotStackedBar( requestersDist, scores, requesters, requestersTicks, "Gender of requester", None, False, scores_colors, "dist_decisions_gender.pdf" )

# positions of the left bar-boundaries
offset = 0
labels = requesters
offset += len(bar_l)+1
bar_l = range(offset, offset+len(labels))

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos += [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = requestersDist
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax2.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # # with the label pre score
        # label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])
ax2.annotate('Gender', xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)
labelsTicks += requestersTicks


# Location of requester
requesters = ['in an unknown place', 'at home', "at friend's home", "in a public place", "at work place"]
requestersTicks = ['Unknown', 'Home', 'Other home', 'Public', 'Work']
requestersArray = dict(zip(requesters,[[],[],[],[],[]]))
requestersDist = dict(zip(requesters,[[],[],[],[],[]]))
for i in range(df.shape[0]):
	requester = df["Q.location"][i]
	decision  = df["A.answer"][i]
	requestersArray[requester].append(decision)

for key in requesters:
	for answer in [1,2,5]:
		proportion = 100 * requestersArray[key].count(answer) / float(len(requestersArray[key])) # proportion of the answer
		requestersDist[key].append(proportion)

# plotStackedBar( requestersDist, scores, requesters, requestersTicks, "Location of requester", None, False, scores_colors, "dist_decisions_req_location.pdf" )

# positions of the left bar-boundaries
labels = requesters
offset += len(bar_l)+1
bar_l = range(offset, offset+len(labels))

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos += [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = requestersDist
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax2.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # # with the label pre score
        # label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])
ax2.annotate('Location', xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)
labelsTicks += requestersTicks


# Nearby of requester
requesters = ['alone', 'with other people']
requestersTicks = ['Alone', 'With people']
requestersArray = dict(zip(requesters,[[],[]]))
requestersDist = dict(zip(requesters,[[],[]]))
for i in range(df.shape[0]):
	requester = df["Q.nearby"][i]
	decision  = df["A.answer"][i]
	requestersArray[requester].append(decision)

for key in requesters:
	for answer in [1,2,5]:
		proportion = 100 * requestersArray[key].count(answer) / float(len(requestersArray[key])) # proportion of the answer
		requestersDist[key].append(proportion)

# plotStackedBar( requestersDist, scores, requesters, requestersTicks, "Nearby of requester", None, False, scores_colors, "dist_decisions_req_nearby.pdf" )


# positions of the left bar-boundaries
labels = requesters
offset += len(bar_l)+1
bar_l = range(offset, offset+len(labels))

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos += [i+(bar_width) for i in bar_l]
bottoms = 100*np.ones( len(labels) )
data = requestersDist
# bars = [None, None, None]
for idx, factor in enumerate(scores):
	data_row = []
	for label in labels:
		# Each row corresponds to a score of every labels.
		data_row.append( data[label][idx] )

	bottoms -= np.array( data_row ) 

	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
	ax2.bar(bar_l, 
        # using the pre_score data
        data_row,
        # emotion_factor_impact_of_each_method[factor],
        # set the width
        width=bar_width,
        # with the label pre score
        label=factor, 
        # with alpha 0.5
        alpha=1, 
        # with color
        bottom=bottoms,
        edgecolor="k",
        color=scores_colors[factor])
ax2.annotate('Nearby', xy=(0,0), xytext=((bar_l[0]+bar_l[-1]+bar_width)/2.0, annotation_y_position), 
			horizontalalignment='center', verticalalignment='bottom', fontsize=12)

labelsTicks += requestersTicks

# set the x ticks with names
# labelsTicks = imageTypesTicks + numPeopleTicks + identitiesTicks + picLocationTicks
ax2.set_xticks( tick_pos )
ax2.set_xticklabels( labelsTicks, rotation=45, ha='right'  )
# # Set the label and legends
# if ylabel: 
# 	ax1.set_ylabel(ylabel)
# ax1.set_xlabel(xlabel)
# ax1.xaxis.set_ticks_position('none')
ax2.grid(True)
ax2.set_ylim([0,100])
# Set a buffer around the edge
ax2.set_xlim([0-(2-bar_width), max(bar_l)+2])
ax2.set_title(r"Requester Contextual Features")
ax2.legend(loc="lower right", fontsize=12)



# ########## Overall distribution of decisions ###########
# # requesters = ['alone', 'with other people']
# # requestersTicks = ['Alone', 'With people']
# # requestersArray = dict(zip(requesters,[[],[]]))
# # requestersDist = dict(zip(requesters,[[],[]]))
# results = []
# decisions = list(df["A.answer"])
# # for i in range(df.shape[0]):
# # 	decision  = df["A.answer"][i]
# # 	requestersArray[requester].append(decision)

# for answer in [1,2,5]:
# 	proportion = 100 * decisions.count(answer) / float(len(decisions)) # proportion of the answer
# 	results.append(proportion)

# # f, ax2 = plt.subplots(1, figsize=(2,3))
# bar_l = 1
# # positions of the x-axis ticks (center of the bars as bar labels)
# bottoms = 100
# data = requestersDist
# for idx, factor in enumerate(scores):

# 	bottoms -= results[idx]

# 	# bottoms -= np.array( emotion_factor_impact_of_each_method[factor] )
# 	ax3.bar(bar_l, 
#         # using the pre_score data
#         results[idx],
#         # emotion_factor_impact_of_each_method[factor],
#         # set the width
#         width=1,
#         # with the label pre score
#         label=factor, 
#         # with alpha 0.5
#         alpha=1, 
#         # with color
#         bottom=bottoms,
#         edgecolor="k",
#         color=scores_colors[factor])
# # ax3.annotate('Overall', xy=(0,0), xytext=(1, annotation_y_position), 
# 			# horizontalalignment='center', verticalalignment='bottom', fontsize=12)
# ax3.grid(True)
# ax3.set_ylim([0,100])
# # Set a buffer around the edge
# ax3.set_xlim(0, 3)
# ax3.set_xticks([])
# ax3.set_title("Overall")

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.05)
# f.legend(bars, scores, "upper right")
# bbox_to_anchor=(1.05, 1.03), 
# ax3.legend(loc="lower left", fontsize=10)
plt.subplots_adjust(wspace=0.03, hspace=0)
filename = "decision_dist_requester_info.pdf"
filename = "decision_hist.pdf"
plt.savefig(filename, format='pdf', bbox_inches='tight', pad_inches=0.05)
shutil.copy(filename, "/Users/yuanlin/PhD/Conference/2017_IFIP_SEC/paper/images/"+filename)
# /Users/yuanlin/PhD/Conference/2017_IFIP_SEC/paper


