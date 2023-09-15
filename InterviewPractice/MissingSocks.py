def count_missing_sock_pairs(socks):
    sock_count = {}
    missing_pairs = 0

    for sock in socks:
        key = (sock['size'], sock['color'])
        if key in sock_count:
            sock_count[key] += 1
        else:
            sock_count[key] = 1

    for count in sock_count.values():
        if count == 1:
            missing_pairs += 1

    print(sock_count)

# Example usage
socks = [
    {'size': 9, 'color': 'black'},
    {'size': 9, 'color': 'black'},
    {'size': 9, 'color': 'blue'},
    {'size': 9, 'color': 'blue'},
    {'size': 9, 'color': 'red'},
    {'size': 9, 'color': 'red'},
    {'size': 8, 'color': 'red'},
]

count_missing_sock_pairs(socks)
# print("Number of socks without a matching pair:", missing_pairs)
