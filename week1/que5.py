#Q5: Find the closest points

import math
def clst_pts(S, P):
    clst_pts = []
    final_list = []

    for point in S:
        dnmntr = math.sqrt((point[0] ** 2) + (point[1] ** 2)) * math.sqrt((P[0] ** 2) + (P[1] ** 2))
        nmrtr = point[0] * P[0] + point[1] * P[1]

        if dnmntr != 0:
            cosine_distance_for_this_point = math.acos(nmrtr / dnmntr)
            clst_pts.append((cosine_distance_for_this_point, point))

    for item in sorted(clst_pts, key=lambda x: x[0])[:5]:
        final_list.append(item[1])

    return final_list

S = [(1, 2), (3, 4), (-1, 1), (6, -7), (0, 6), (-5, -8), (-1, -1), (6, 0), (1, -1)]
P = (3, -4)

clst_pts = clst_pts(S, P)
print("Closest point-cosine-distance - top 5:", *[point for point in clst_pts], sep="\n")