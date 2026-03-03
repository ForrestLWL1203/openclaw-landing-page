BOARD_SIZE = 15
EMPTY = '·'
BLACK = '●'
WHITE = '○'

board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board():
    print('  ' + ' '.join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(f'{i} ' + ' '.join(row))
    print()

def place_piece(row, col, piece):
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY:
        board[row][col] = piece
        return True
    return False

def check_win(row, col, piece):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        for d in [1, -1]:
            r, c = row + dr * d, col + dc * d
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == piece:
                count += 1
                r += dr * d
                c += dc * d
        if count >= 5:
            return True
    return False

def parse_input(s):
    try:
        parts = s.split()
        if len(parts) != 2:
            return None
        return int(parts[0]), int(parts[1])
    except:
        return None

def main():
    print('五子棋游戏 - 输入坐标(行 列)下棋，例如: 7 7')
    print('退出: q\n')
    print_board()
    
    current = BLACK
    moves = 0
    
    while moves < BOARD_SIZE * BOARD_SIZE:
        player = '黑棋' if current == BLACK else '白棋'
        s = input(f'{player}落子: ').strip()
        
        if s.lower() == 'q':
            print('游戏结束')
            break
        
        pos = parse_input(s)
        if pos is None:
            print('输入无效，格式: 行 列 (如 7 7)')
            continue
        
        row, col = pos
        if not place_piece(row, col, current):
            print('位置无效或已有棋子')
            continue
        
        print_board()
        
        if check_win(row, col, current):
            print(f'{player}获胜!')
            break
        
        current = WHITE if current == BLACK else BLACK
        moves += 1
    
    if moves == BOARD_SIZE * BOARD_SIZE:
        print('平局!')

if __name__ == '__main__':
    main()
