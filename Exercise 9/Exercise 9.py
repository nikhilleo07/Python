import datetime
x = datetime.datetime.now()
d=x.strftime("%B")
m=x.strftime("%d")
y=x.strftime("%A")
w=x.strftime("%I")
t=x.strftime("%M")
s=x.strftime("%p")
print(f"Its {y} {w}:{t} {s} of {m}rd {d}")
