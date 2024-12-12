def solve(x: int, t: int, dp: dict = None) -> int:
    """Calculate how many stones result from stone x after t steps"""
    if dp is None:
        dp = {}
    
    if (x, t) in dp:
        return dp[(x, t)]
        
    if t == 0:
        return 1
    
    if x == 0:
        result = solve(1, t-1, dp)
    elif len(str(x)) % 2 == 0:
        num_str = str(x)
        mid = len(num_str) // 2
        left = int(num_str[:mid] or '0')
        right = int(num_str[mid:] or '0')
        result = solve(left, t-1, dp) + solve(right, t-1, dp)
    else:
        result = solve(x * 2024, t-1, dp)
    
    dp[(x, t)] = result
    return result

def solve_all(stones: list[str], blinks: int) -> int:
    return sum(solve(int(x), blinks, {}) for x in stones)

def main():
    input_data = "965842 9159 3372473 311 0 6 86213 48"
    stones = input_data.strip().split()
    print(f"Solution: {solve_all(stones, 75)}")

if __name__ == "__main__":
    main()
