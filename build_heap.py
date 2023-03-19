# python3


def build_heap(data):
    swaps = []
    for i in range(len(data)):
        siftdown(i, data, swaps)
    return swaps
def siftdown(i, data, swaps):
    node = i
    left_child = 2*i+1
    right_child = 2*i+2
    if left_child < len(data) and data[left_child] < data[node]:
        node = left_child
    if right_child < len(data) and data[right_child] < data[node]:
        node = right_child
    if i != node:
        data[i], data[node] = data[node], data[i]
        swaps.append((i, node))
        siftdown(node, data, swaps)
def main():
    input_type = input()
    if "I" in input_type:
        nav = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_type:
        filename = input()
        if "a" not in filename:
            with open("./tests/" + filename, mode='r') as f:
                nav = int(f.readline())
                data = list(map(int, f.readline().split()))
    else:
        print("error")
        return
    assert len(data) == nav
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
if __name__ == "__main__":
    main()
