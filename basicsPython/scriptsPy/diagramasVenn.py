from matplotlib import pyplot as plt
from matplotlib_venn import venn2

diagram = venn2((1, 1, 1))
diagram.get_label_by_id("11").set_text("A ∪ B")
diagram.get_label_by_id("10").set_text("A")
diagram.get_label_by_id("01").set_text("B")

diagram = venn2((1, 1, 1))
diagram.get_label_by_id("11").set_text("A ∪ B")
diagram.get_label_by_id("10").set_text("A")
diagram.get_label_by_id("01").set_text("B")

plt.title("(A ∪ B)'")
plt.show()

