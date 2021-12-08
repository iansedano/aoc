from debug import p

solution = ["d", "e", "a", "f", "g", "b", "c"]

a = set(["a", "b", "c", "d"])
b = set(["b", "c"])

p(a.symmetric_difference(b))
p(b.symmetric_difference(a))


a = {"c", "d", "a", "b", "e", "f"}
b = {"c", "d", "g", "b", "e", "f"}
c = {"c", "d", "g", "a", "b", "e"}

p(a)
p(b)
p(c)
p(a.symmetric_difference(b))
p(b.symmetric_difference(c))
p(a.symmetric_difference(c))



a = set(["c", "b"])
b = set(["b", "c"])
p(a ==  b)