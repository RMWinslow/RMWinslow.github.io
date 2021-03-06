
import yed

y = yed.Graph()

n1 = y.node(text="1", fill_color="#aaaaaa")
n2 = y.node(text="2", fill_color="#aaaaaa")
n3 = y.node(text="3", fill_color="#aaaaaa")
n4 = y.node(text="4", fill_color="#aaaaaa")
n5 = y.node(text="5", fill_color="#aaaaaa")

for n in [n2, n3, n4, n5]:
    y.edge(n1, n, target_arrow="none")
for n in [n3, n4, n5]:
    y.edge(n2, n, target_arrow="none")
for n in [n4, n5]:
    y.edge(n3, n, target_arrow="none")
for n in [n5]:
    y.edge(n4, n, target_arrow="none")

y.save("k5.graphml")