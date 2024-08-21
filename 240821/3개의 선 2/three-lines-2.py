def verify_dots(dots):
    xs = list(set(dot[0] for dot in dots))
    ys = list(set(dot[1] for dot in dots))
    len_xs, len_ys = len(xs), len(ys)

    # x >= 3
    if len_xs >= 3:
        for i in range(len_xs):
            for j in range(i+1, len_xs):
                for k in range(j+1, len_xs):
                    lines_x = [xs[i], xs[j], xs[k]]

                    if all(dot[0] in lines_x for dot in dots):
                        return 1

    # x >= 2 and y >= 1
    if len_xs >= 2 and len_ys >= 1:
        for i in range(len_xs):
            for j in range(i+1, len_xs):
                for k in range(len_ys):
                    lines_x = [xs[i], xs[j]]
                    lines_y = [ys[k]]

                    if all(dot[0] in lines_x or dot[1] in lines_y for dot in dots):
                        return 1

    # x >= 1 and y >= 2
    if len_xs >= 1 and len_ys >= 2:
        for i in range(len_xs):
            for j in range(len_ys):
                for k in range(j+1, len_ys):
                    lines_x = [xs[i]]
                    lines_y = [ys[j], ys[k]]

                    if all(dot[0] in lines_x or dot[1] in lines_y for dot in dots):
                        return 1

    # y >= 3
    if len_ys >= 3:
        for i in range(len_ys):
            for j in range(i+1, len_ys):
                for k in range(j+1, len_ys):
                    lines_y = [ys[i], ys[j], xs[k]]

                    if all(dot[1] in lines_y for dot in dots):
                        return 1

    return 0


N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

print(verify_dots(dots))