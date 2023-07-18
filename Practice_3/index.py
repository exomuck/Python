# Hàm kiểm tra nếu 2 quân hậu có thể tấn công nhau
def is_attacking(x1, y1, x2, y2):
    # Kiểm tra cùng hàng hoặc cùng cột
    if x1 == x2 or y1 == y2:
        return True
    # Kiểm tra đường chéo chính
    if x1 + y1 == x2 + y2:
        return True
    # Kiểm tra đường chéo phụ
    if x1 - y1 == x2 - y2:
        return True
    return False


# Hàm kiểm tra bàn cờ có hợp lệ hay không
def is_valid_board(board):
    # Kiểm tra từng cặp quân hậu
    for i in range(8):
        for j in range(i + 1, 8):
            # Nếu 2 quân hậu có thể tấn công nhau
            if is_attacking(i, board[i], j, board[j]):
                return False
    return True


# Nhập số lượng test case
T = int(input())

# Duyệt qua từng test case
for t in range(T):
    # Nhập bàn cờ
    board = []
    for i in range(8):
        row = list(map(int, input().split()))
        board.extend(row)

    # Kiểm tra bàn cờ có hợp lệ hay không
    if is_valid_board(board):
        print("NO")
    else:
        print("YES")