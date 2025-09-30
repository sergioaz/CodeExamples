def solution(Number_of_keys: int, Start_position_of_gold_key: int, Length_of_seq: int, Winning_Position: int) -> str:
    """
    Determine the winner of the key reversal game.
    
    Args:
        Number_of_keys: Total number of keys (1 gold + n-1 silver)
        Start_position_of_gold_key: Initial position of gold key (1-indexed)
        Length_of_seq: Number of consecutive keys that can be reversed (K)
        Winning_Position: Target position for the gold key (1-indexed)
    
    Returns:
        "player_one", "player_two", or "Draw" indicating the winner or draw
    """
    
    # Convert to 0-indexed for easier calculation
    gold_pos = Start_position_of_gold_key - 1
    target_pos = Winning_Position - 1
    n = Number_of_keys
    k = Length_of_seq
    
    # If gold key is already at winning position, player one wins immediately
    if gold_pos == target_pos:
        return "player_one"
    
    # Use BFS to find the minimum number of moves to reach target
    from collections import deque
    
    visited = set()
    queue = deque([(gold_pos, 0)])  # (position, moves)
    visited.add(gold_pos)
    
    # Maximum possible moves to prevent infinite search
    # If we can't reach target in n*2 moves, it's likely impossible
    max_moves = n * 2
    
    while queue:
        pos, moves = queue.popleft()
        
        # If we've exceeded reasonable number of moves, consider it a draw
        if moves > max_moves:
            return "Draw"
        
        if pos == target_pos:
            # If minimum moves is odd, player one wins (they make the final move)
            # If minimum moves is even, player two wins (they make the final move)
            if moves % 2 == 1:
                return "player_one"
            else:
                return "player_two"
        
        # Try all possible sequences of length k that include current position
        for start in range(max(0, pos - k + 1), min(n - k + 1, pos + 1)):
            # After reversing sequence [start, start+k), 
            # element at pos will move to position: start + (start + k - 1 - pos)
            new_pos = start + (start + k - 1 - pos)
            
            if 0 <= new_pos < n and new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, moves + 1))
    
    # If we've exhausted all possibilities and haven't reached the target, it's a draw
    return "Draw"


def solution_with_game_theory(Number_of_keys: int, Start_position_of_gold_key: int, Length_of_seq: int, Winning_Position: int) -> str:
    """
    Alternative solution using game theory - determines winner/draw by analyzing all reachable positions
    and their winning/losing states.
    """
    
    # Convert to 0-indexed
    start_pos = Start_position_of_gold_key - 1
    target_pos = Winning_Position - 1
    n = Number_of_keys
    k = Length_of_seq
    
    if start_pos == target_pos:
        return "player_one"
    
    # Find all reachable positions from start
    def get_reachable_positions():
        visited = set()
        queue = [start_pos]
        visited.add(start_pos)
        reachable = {start_pos}
        
        while queue:
            pos = queue.pop(0)
            
            # Try all possible sequences of length k that include current position
            for seq_start in range(max(0, pos - k + 1), min(n - k + 1, pos + 1)):
                # After reversing sequence [seq_start, seq_start+k), 
                # element at pos will move to position: seq_start + (seq_start + k - 1 - pos)
                new_pos = seq_start + (seq_start + k - 1 - pos)
                
                if 0 <= new_pos < n and new_pos not in visited:
                    visited.add(new_pos)
                    reachable.add(new_pos)
                    queue.append(new_pos)
        
        return reachable
    
    reachable = get_reachable_positions()
    
    # If target is not reachable, it's a draw
    if target_pos not in reachable:
        return "Draw"
    
    # Build transition graph
    transitions = {}
    for pos in reachable:
        transitions[pos] = set()
        for seq_start in range(max(0, pos - k + 1), min(n - k + 1, pos + 1)):
            new_pos = seq_start + (seq_start + k - 1 - pos)
            if 0 <= new_pos < n and new_pos in reachable:
                transitions[pos].add(new_pos)
    
    # Use dynamic programming to determine winning/losing positions
    # winning[pos] = True if current player can force a win from position pos
    winning = {}
    
    def can_win(pos, memo=None):
        if memo is None:
            memo = {}
        
        if pos in memo:
            return memo[pos]
        
        if pos == target_pos:
            memo[pos] = True
            return True
        
        # If any move leads to a losing position for opponent, current player wins
        for next_pos in transitions[pos]:
            if not can_win(next_pos, memo):
                memo[pos] = True
                return True
        
        # If all moves lead to winning positions for opponent, current player loses
        memo[pos] = False
        return False
    
    # Check if player one can win from start position
    if can_win(start_pos):
        return "player_one"
    else:
        # Check if the game can reach a cycle without reaching target
        # If so, it might be a draw
        
        # Simple check: if we can't win but target is reachable, 
        # player two has advantage
        return "player_two"


# Test the function with some examples
if __name__ == "__main__":

    # Test case 0: Gold key at position 1, need to get to position 4, can reverse 2 keys
    result0 = solution(4, 1, 2, 4)
    print(f"Test 0 - Keys: 4, Gold at: 1, Sequence length: 2, Target: 4 -> Winner: {result0}")

    result0 = solution_with_game_theory(4, 1, 2, 4)
    print(f"Test 0 - Keys: 4, Gold at: 1, Sequence length: 2, Target: 4 -> Winner: {result0}")

    exit (0)

    # Test case 1: Gold key at position 1, need to get to position 5, can reverse 3 keys
    result1 = solution(10, 1, 3, 5)
    print(f"Test 1 - Keys: 10, Gold at: 1, Sequence length: 3, Target: 5 -> Winner: {result1}")
    
    # Test case 2: Gold key at position 5, need to get to position 1, can reverse 4 keys  
    result2 = solution(8, 5, 4, 1)
    print(f"Test 2 - Keys: 8, Gold at: 5, Sequence length: 4, Target: 1 -> Winner: {result2}")
    
    # Test case 3: Gold key already at target
    result3 = solution(6, 3, 2, 3)
    print(f"Test 3 - Keys: 6, Gold at: 3, Sequence length: 2, Target: 3 -> Winner: {result3}")
    
    # Test case 4: Simple case
    result4 = solution(5, 2, 3, 4)
    print(f"Test 4 - Keys: 5, Gold at: 2, Sequence length: 3, Target: 4 -> Winner: {result4}")
    
    # Test case 5: Potential draw scenario - target unreachable
    result5 = solution(4, 1, 2, 4)
    print(f"Test 5 - Keys: 4, Gold at: 1, Sequence length: 2, Target: 4 -> Winner: {result5}")
    
    # Test case 6: Another potential draw scenario
    result6 = solution(3, 1, 1, 3)  # Can only reverse 1 key at a time
    print(f"Test 6 - Keys: 3, Gold at: 1, Sequence length: 1, Target: 3 -> Winner: {result6}")