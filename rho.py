import math
xy = [[i, j, (2 * i - j) / (2 * i + j)] for i in range(3, 10) for j in range(3, 10)]
# xy = [[3,3], [4,3], [4,4], [5,3], [5,4], [5,5], [6,5], [6,6], [7,6], []]
x = [i[0] for i in xy]
y = [i[1] for i in xy]
for i in range(len(xy)):
    VSR = 12.31222661 * x[i] * y[i] + 2.243627412 * pow(y[i], 2)
    VSM = 13.08877324 * pow(x[i], 2) + 6.691121744 * x[i] * y[i] - 0.1058927222 * pow(y[i], 2)
    VS =  13.08877324 * pow(x[i], 2) + 19.00334836 * x[i] * y[i] + 2.137734690 * pow(y[i], 2)
    # print('x = ', x[i], ' y = ', y[i], ' w = ', round((2 * x[i] - y[i]) / (2 * x[i] + y[i]), 2), ' VSR = ', round(VSR, 2), ' VSM = ', round(VSM, 2), ' VS = ', round(VS, 2))
    VNM = 4.031496871 * pow(x[i], 2) + 11.00797448 * x[i] * y[i]
    VNR = 7.914230020 * x[i] * y[i] + 5.607445650 * pow(y[i], 2)
    VN = 4.031496871 * pow(x[i], 2) + 18.92220450 * x[i] * y[i] + 5.607445650 * pow(y[i], 2)

    VC = 9.638942521 * pow(x[i], 2) + 19.27788504 * x[i] * y[i] + 9.638942521 * pow(y[i], 2)
    # print(x[i])
    # print(y[i])
    # print(round((2 * x[i] - y[i]) / (2 * x[i] + y[i]), 2))
    # print(round(VSR, 2))
    # print(round(VSM, 2))
    # print(round(VS, 2))

    # print(round(VNM, 2))
    # print(round(VNR, 2))
    # print(round(VN, 2))
    print("%.2f" % round(VC, 2))

