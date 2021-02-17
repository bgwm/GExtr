import seaborn as sns
import matplotlib.pyplot  as plt
import numpy as np

f, ax = plt.subplots()
sns.set_theme()

#sns.set_style("ticks")

tips = sns.load_dataset("tips")

vivo_c = ["#d0cdff", "#415fff", "#FF4d9b", "#FF8769", "#ffc452", "#f9f871"]
sns.set_palette(vivo_c)

sns.histplot(data=tips, x="total_bill", hue="sex", bins=35, multiple="stack",
        )
ax.legend(ncol=2, loc='lower right', frameon=True)
ax.set_xticks([])
ax.axes.get_yaxis().set_visible(False)
ax.patch.set_facecolor('#ff4d9b')
sns.despine(right=True)
#g.set(yticks=[])
plt.show()
f.savefig("out.png")

