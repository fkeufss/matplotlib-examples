import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'serif';
mpl.rcParams['font.size'] = 16;


score_compare = {
	'subject': [22, 28, 8],
	'mark': [11, 8, 1],
	'face': [30, 40, 14],
	'deal': [37, 46, 18],
	# 'word5': [30, 20, 10]
}

words = sorted(score_compare.keys())
labels = [r"$O>B$", r"$O=B$", r"$O<B$"]
methods = ['Baseline', 'Ours']
colors = ['#31a354', '#6baed6', '#de2d26']
graylevels = ['#f0f0f0', '#bdbdbd', '#636363']
hatches = ['*'*2, 'o'*2, 'x'*2]

###### Plot score distributions ######
def norm(data):
	for w in data:
		data[w] = np.array(data[w])/float(np.sum(data[w]))

def plot_stacked_bar_dist(data, filename):

	norm(data)

	# Create the general blog and the "subplots" i.e. the bars
	fig, ax = plt.subplots(1, 1, figsize=(4,4))

	# Number of bars
	n_bars = len(words)

	# Set the bar width
	bar_width = 0.5

	# positions of the center bar-boundaries
	bar_l = np.arange(n_bars) + 1

	# positions of the x-axis ticks (center of the bars as bar labels)
	tick_pos = np.arange(n_bars) + 1

	# Initial bottom position of each bar
	bottoms = np.ones( n_bars )

	for id in xrange(len(labels)):

		# data of the current row of the bar
		data_row = [data[w][id] for w in words]

		# bottom position of the current bar
		bottoms -= data_row

		# plot bar for data1
		ax.bar(
			bar_l,
			data_row,
			width=bar_width,
			alpha=1,
			bottom=bottoms,
			edgecolor="k",
			color=graylevels[id],
			label=labels[id])
			# hatch=hatches[id])

	# set the x ticks and labels names
	ax.set_xticks(tick_pos)
	ax.set_xticklabels([r'\textit{%s}' % i for i in words ], ha='center')

	# set the y label and legends
	ax.set_ylabel("Proportion")
	ax.set_xlabel("Candidate")

	# set legends
	ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0., fontsize=11)

	# set axis limits
	ax.set_xlim([0.5, n_bars+0.5])
	ax.set_ylim([0, 1])

	ax.grid(linestyle='dotted', alpha=0.4, color='black')
	# set title
	# ax.set_title(word)

	# save and close fig

	fig.savefig(filename, format='pdf', bbox_inches='tight', pad_inches=0.05)
	plt.close(fig)


plot_stacked_bar_dist(score_compare, "bar_plots_compare.pdf")


