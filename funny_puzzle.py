import heapq
import math


def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0

    for i in range(len(from_state)):
        x1 = math.floor(i / 3)
        y1 = i % 3
        if from_state[i] == 0:
            continue
        for j in range(len(to_state)):
            if from_state[i] == to_state[j]:
                x2 = math.floor(j / 3)
                y2 = j % 3
                distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """

    result = []

    weizhi0 = []

    for i in range(len(state)):
        if state[i] == 0:
            x1 = math.floor(i / 3)
            y1 = i % 3
            weizhi0.append(x1)
            weizhi0.append(y1)

    left = weizhi0[1] - 1
    upper = weizhi0[0] - 1

    low = weizhi0[0] + 1
    right = weizhi0[1] + 1

    left1 = weizhi0[3] - 1
    upper1 = weizhi0[2] - 1

    low1 = weizhi0[2] + 1
    right1 = weizhi0[3] + 1

    if left == -1 and upper == -1 and right == 1 and low == 1:
        statenew1 = state.copy()
        statenew1[0] = state[1]
        statenew1[1] = state[0]
        result.append(statenew1)

        statenew2 = state.copy()
        statenew2[0] = state[3]
        statenew2[3] = state[0]
        result.append(statenew2)

    if left == 0 and upper == -1 and right == 2 and low == 1:
        statenew3 = state.copy()
        statenew3[1] = state[0]
        statenew3[0] = state[1]
        result.append(statenew3)

        statenew4 = state.copy()
        statenew4[1] = state[4]
        statenew4[4] = state[1]
        result.append(statenew4)

        statenew5 = state.copy()
        statenew5[1] = state[2]
        statenew5[2] = state[1]
        result.append(statenew5)

    if left == 1 and upper == -1 and right == 3 and low == 1:
        statenew6 = state.copy()
        statenew6[2] = state[1]
        statenew6[1] = state[2]
        result.append(statenew6)

        statenew7 = state.copy()
        statenew7[2] = state[5]
        statenew7[5] = state[2]
        result.append(statenew7)

    if left == -1 and upper == 0 and right == 1 and low == 2:
        statenew8 = state.copy()
        statenew8[3] = state[0]
        statenew8[0] = state[3]
        result.append(statenew8)

        statenew9 = state.copy()
        statenew9[3] = state[4]
        statenew9[4] = state[3]
        result.append(statenew9)

        statenew10 = state.copy()
        statenew10[3] = state[6]
        statenew10[6] = state[3]
        result.append(statenew10)

    if left == 0 and upper == 0 and right == 2 and low == 2:
        statenew11 = state.copy()
        statenew11[4] = state[1]
        statenew11[1] = state[4]
        result.append(statenew11)

        statenew12 = state.copy()
        statenew12[4] = state[3]
        statenew12[3] = state[4]
        result.append(statenew12)

        statenew13 = state.copy()
        statenew13[4] = state[5]
        statenew13[5] = state[4]
        result.append(statenew13)

        statenew14 = state.copy()
        statenew14[4] = state[7]
        statenew14[7] = state[4]
        result.append(statenew14)

    if left == 1 and upper == 0 and right == 3 and low == 2:
        statenew15 = state.copy()
        statenew15[5] = state[2]
        statenew15[2] = state[5]
        result.append(statenew15)

        statenew16 = state.copy()
        statenew16[5] = state[4]
        statenew16[4] = state[5]
        result.append(statenew16)

        statenew17 = state.copy()
        statenew17[5] = state[8]
        statenew17[8] = state[5]
        result.append(statenew17)

    if left == -1 and upper == 1 and right == 1 and low == 3:
        statenew18 = state.copy()
        statenew18[6] = state[3]
        statenew18[3] = state[6]
        result.append(statenew18)

        statenew19 = state.copy()
        statenew19[6] = state[7]
        statenew19[7] = state[6]
        result.append(statenew19)

    if left == 0 and upper == 1 and right == 2 and low == 3:
        statenew20 = state.copy()
        statenew20[7] = state[6]
        statenew20[6] = state[7]
        result.append(statenew20)

        statenew21 = state.copy()
        statenew21[7] = state[4]
        statenew21[4] = state[7]
        result.append(statenew21)

        statenew22 = state.copy()
        statenew22[7] = state[8]
        statenew22[8] = state[7]
        result.append(statenew22)

    if left == 1 and upper == 1 and right == 3 and low == 3:
        statenew23 = state.copy()
        statenew23[8] = state[5]
        statenew23[5] = state[8]
        result.append(statenew23)

        statenew24 = state.copy()
        statenew24[8] = state[7]
        statenew24[7] = state[8]
        result.append(statenew24)

    if left1 == -1 and upper1 == -1 and right1 == 1 and low1 == 1:
        statenew1 = state.copy()
        statenew1[0] = state[1]
        statenew1[1] = state[0]
        result.append(statenew1)

        statenew2 = state.copy()
        statenew2[0] = state[3]
        statenew2[3] = state[0]
        result.append(statenew2)

    if left1 == 0 and upper1 == -1 and right1 == 2 and low1 == 1:
        statenew3 = state.copy()
        statenew3[1] = state[0]
        statenew3[0] = state[1]
        result.append(statenew3)

        statenew4 = state.copy()
        statenew4[1] = state[4]
        statenew4[4] = state[1]
        result.append(statenew4)

        statenew5 = state.copy()
        statenew5[1] = state[2]
        statenew5[2] = state[1]
        result.append(statenew5)

    if left1 == 1 and upper1 == -1 and right1 == 3 and low1 == 1:
        statenew6 = state.copy()
        statenew6[2] = state[1]
        statenew6[1] = state[2]
        result.append(statenew6)

        statenew7 = state.copy()
        statenew7[2] = state[5]
        statenew7[5] = state[2]
        result.append(statenew7)

    if left1 == -1 and upper1 == 0 and right1 == 1 and low1 == 2:
        statenew8 = state.copy()
        statenew8[3] = state[0]
        statenew8[0] = state[3]
        result.append(statenew8)

        statenew9 = state.copy()
        statenew9[3] = state[4]
        statenew9[4] = state[3]
        result.append(statenew9)

        statenew10 = state.copy()
        statenew10[3] = state[6]
        statenew10[6] = state[3]
        result.append(statenew10)

    if left1 == 0 and upper1 == 0 and right1 == 2 and low1 == 2:
        statenew11 = state.copy()
        statenew11[4] = state[1]
        statenew11[1] = state[4]
        result.append(statenew11)

        statenew12 = state.copy()
        statenew12[4] = state[3]
        statenew12[3] = state[4]
        result.append(statenew12)

        statenew13 = state.copy()
        statenew13[4] = state[5]
        statenew13[5] = state[4]
        result.append(statenew13)

        statenew14 = state.copy()
        statenew14[4] = state[7]
        statenew14[7] = state[4]
        result.append(statenew14)

    if left1 == 1 and upper1 == 0 and right1 == 3 and low1 == 2:
        statenew15 = state.copy()
        statenew15[5] = state[2]
        statenew15[2] = state[5]
        result.append(statenew15)

        statenew16 = state.copy()
        statenew16[5] = state[4]
        statenew16[4] = state[5]
        result.append(statenew16)

        statenew17 = state.copy()
        statenew17[5] = state[8]
        statenew17[8] = state[5]
        result.append(statenew17)

    if left1 == -1 and upper1 == 1 and right1 == 1 and low1 == 3:
        statenew18 = state.copy()
        statenew18[6] = state[3]
        statenew18[3] = state[6]
        result.append(statenew18)

        statenew19 = state.copy()
        statenew19[6] = state[7]
        statenew19[7] = state[6]
        result.append(statenew19)

    if left1 == 0 and upper1 == 1 and right1 == 2 and low1 == 3:
        statenew20 = state.copy()
        statenew20[7] = state[6]
        statenew20[6] = state[7]
        result.append(statenew20)

        statenew21 = state.copy()
        statenew21[7] = state[4]
        statenew21[4] = state[7]
        result.append(statenew21)

        statenew22 = state.copy()
        statenew22[7] = state[8]
        statenew22[8] = state[7]
        result.append(statenew22)

    if left1 == 1 and upper1 == 1 and right1 == 3 and low1 == 3:
        statenew23 = state.copy()
        statenew23[8] = state[5]
        statenew23[5] = state[8]
        result.append(statenew23)

        statenew24 = state.copy()
        statenew24[8] = state[7]
        statenew24[7] = state[8]
        result.append(statenew24)

    # print(result)
    # print(result[len(result)])

    for i in range(len(result)):
        for j in range(len(result)):
            # if result[i] == result[j] and i != j:
            # print(j)
            if result[i] == result[j] and i != j:
                # print(len(result))
                result.pop(i)
                j = j - 1

                result.pop(j)
                # j = j-1
                i = i - 1
                result = sorted(result)

                return result

    return result

    # return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    OPEN = []
    CLOSED = []
    PARENT_index = 0
    A = {}
    MAX = 1
    H = get_manhattan_distance(state, goal_state)
    heapq.heappush(OPEN, (H, state, (0, H, -1)))
    while len(OPEN) > 0:
            n = heapq.heappop(OPEN)
            CLOSED.append(n[1])
            A[PARENT_index]=n
            PARENT_index+=1
            # if n[1] == goal_state:
            #     A = n[2][2]
            #     j = CLOSED[-1]
            #     while j[2][2] != -1:
            #         j = CLOSED[j[2][2]]
            #         PARENT_LIST.append(j[2][2])
            #         PARENT_LIST.reverse()
            if n[2][1]==0:
                Parent_list = [n]
                while Parent_list[-1][2][2] != 0:
                    N = A[Parent_list[-1][2][2]]
                    Parent_list.append(N)

                Parent_list.append(A[0])
                Parent_list = Parent_list[::-1]
                for state in Parent_list:
                    print(f"{state[1]} h={state[2][1]} moves: {state[2][0]}")
                print("Max queue length: "+str(MAX))
                break
            else:
                B = get_succ(n[1])
                g0 = n[2][0]
                for k in B:
                    if k not in CLOSED:
                        g1 = g0 + 1
                        new_H = get_manhattan_distance(k, goal_state)
                        f = g1 + new_H
                        heapq.heappush(OPEN, (f, k, (n[2][0] + 1, new_H, PARENT_index-1)))
                        heapq.heapify(OPEN)
                        MAX = len(OPEN)
                    # else:
                    #     if k in CLOSED:
                    #         for m in CLOSED:
                    #             if k[2][0] < m[2][0]:
                    #                 g1 = g0 + 1
                    #                 new_H = get_manhattan_distance(k, goal_state)
                    #                 f = g1 + new_H
                    #                 heapq.heappush(OPEN, (f,k, (n[2][0]+1, new_H, PARENT_index)))
                    #                 heapq.heapify(OPEN)
                    #     if k in OPEN:
                    #         for m in OPEN:
                    #             if k[2][0] < m[2][0]:
                    #                 g1 = g0 + 1
                    #                 new_H = get_manhattan_distance(k, goal_state)
                    #                 f = g1 + new_H
                    #                 heapq.heappush(OPEN, (f, k, (g1, new_H, PARENT_index)))
                    #                 heapq.heapify(OPEN)

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    # print_succ([0, 4, 7, 1, 3, 0, 6, 2, 5])
    # print()
    #
    #
    # print(get_manhattan_distance([4, 3,0,5,1,6,7,2,0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    # print()
    #
    # solve([1, 7, 0, 6, 3, 2, 0, 4, 5])
    # print()
