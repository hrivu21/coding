x, y, z = 0, 0, 0
for i in range(10):
    x = (72-15*y-2*z)/6
    y = 110-54*z-x
    z = 27*x+6*y-85

    # x = 110-y-54*z
    # y = (85+z-27*x)/6
    # z = (72-6*x-15*y)/2

    # x = (17-y+2*z)/20
    # y = (-18-3*x+z)/20
    # z = (25-2*x+3*y)/20

    print("ITERATION=", i)
    print(x, y, z)
    print("\n\n")
