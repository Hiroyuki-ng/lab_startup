with open("compare.dat", "w") as f:
    for i in range(20):
        x = i/20.0
        y1 = 1.8+0.2*(x*10)
        y2 = 1.8+0.2*(x*10)**1.1
        f.write(f"{x} {y1} {y2}\n")
