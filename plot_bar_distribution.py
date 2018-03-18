import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'serif';
mpl.rcParams['font.size'] = 18;

print "Hello"
print "Lalala"

# data1 = {"word":[# of score 2, # of score 1, # of score 0]}
score_dist_data1 = {
	'subject': [27, 18, 13],
	'mark': [3, 6, 11],
	'face': [46, 10, 28],
	'deal': [51, 21, 29],
	# 'word5': [22, 22, 26]
}

score_dist_data2 = {
	'subject': [41, 11, 6],
	'mark': [12, 3, 5],
	'face': [57, 14, 13],
	'deal': [67, 20, 14],
	# 'word5': [30, 20, 10]
}


words = sorted(score_dist_data1.keys())
scores = ["2 - Good", "1 - Acceptable", "0 - Wrong"]
methods = ['Baseline', 'Ours']
colors1 = ['#bdd7e7', '#3182bd', '#08519c']
colors2 = ['#fee5d9', '#de2d26', '#a50f15']
graylevels = ['#f0f0f0', '#bdbdbd', '#636363']
hatches = ['*'*2, 'o'*2, 'x'*2]
bar_linewidth = 1

# color_base = '#377eb8'
# color_ours = '#e41a1c'
color_base = 'black'
color_ours = 'black'

###### Plot score distributions ######
def norm(data):
	for w in data:
		data[w] = np.array(data[w])/float(np.sum(data[w]))

def plot_stacked_bar_dist(data1, data2, filename):

	norm(data1)
	norm(data2)

	# Create the general blog and the "subplots" i.e. the bars
	fig, ax = plt.subplots(1, 1, figsize=(4, 4))

	# Number of bars
	n_bars = len(words)

	# Set the bar width
	bar_width = 0.3

	# positions of the center bar-boundaries
	bar_l_1 = np.arange(n_bars) + 1 - bar_width/2 - 0.05
	bar_l_2 = np.arange(n_bars) + 1 + bar_width/2 + 0.05

	# positions of the x-axis ticks (center of the bars as bar labels)
	tick_pos = np.arange(n_bars) + 1

	# Initial bottom position of each bar
	bottoms1 = np.ones( n_bars )
	bottoms2 = np.ones( n_bars )

	legend_patches = []

	for id in xrange(len(scores)):

		# data of the current row of the bar
		data1_row = [data1[w][id] for w in words]
		data2_row = [data2[w][id] for w in words]

		# bottom position of the current bar
		bottoms1 -= data1_row
		bottoms2 -= data2_row

		# plot bar for data1
		ax.bar(
			bar_l_1,
			data1_row,
			width=bar_width,
			alpha=1,
			bottom=bottoms1,
			edgecolor=color_base,
			lw=bar_linewidth,
			linestyle="--",
			color=graylevels[id])
			# hatch=hatches[id])

		ax.bar(
			bar_l_2,
			data2_row,
			width=bar_width,
			label=scores[id],
			alpha=1,
			bottom=bottoms2,
			edgecolor=color_ours,
			lw=bar_linewidth,
			color=graylevels[id])
			# hatch=hatches[id])

		legend_patches.append(
			mpatches.Patch(facecolor=graylevels[id], edgecolor='black', lw=0.5, label=scores[id])
			)

	# set the x ticks and labels names
	ax.set_xticks(tick_pos)
	ax.set_xticklabels([r'\textit{%s}' % i for i in words ], ha='center')

	# set the y label and legends
	ax.set_ylabel("Proportion")
	ax.set_xlabel("Candidate")

	# set legends
	legend_patches += [
		mpatches.Patch(facecolor='white', edgecolor='white', alpha=0, label=''),
		mpatches.Patch(facecolor='white', edgecolor=color_base, lw=bar_linewidth, linestyle="--", label='Baseline'),
		mpatches.Patch(facecolor='white', edgecolor=color_ours, lw=bar_linewidth, label='Our method')
	]

	# first_legend = plt.legend(handles=legend_patches_2, loc='upper center', bbox_to_anchor=(0.5, 1.11), borderaxespad=0., ncol=2)
	# plt.gca().add_artist(first_legend)

	plt.legend(handles=legend_patches, bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0., fontsize=11)

	# set axis limits
	ax.set_xlim([1-0.6, n_bars+0.6])
	ax.set_ylim([0, 1])

	ax.grid(linestyle='dotted', alpha=0.4, color='black')
	# set title
	# ax.set_title(word)

	# save and close fig

	fig.savefig(filename, format='pdf', bbox_inches='tight', pad_inches=0.05)
	plt.close(fig)


plot_stacked_bar_dist(score_dist_data1, score_dist_data2, "bar_plots.pdf")


