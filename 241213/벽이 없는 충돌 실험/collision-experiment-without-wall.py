import sys
from typing import List, Tuple

def solve_bead_simulation(n: int, beads: List[List[float | int | str]]) -> int:
    # Directions: x and y movement
    directions = {
        "L": (-0.5, 0), 
        "R": (0.5, 0), 
        "U": (0, 0.5), 
        "D": (0, -0.5)
    }
    
    def in_range(x: float, y: float) -> bool:
        return -1000 <= x <= 1000 and -1000 <= y <= 1000
    
    latest_collision = -1
    time = 1
    
    # Deep copy to avoid modifying original
    current_beads = [bead.copy() for bead in beads]
    
    while True:
        # Track bead positions after movement
        positions: dict[Tuple[float, float], List[List]] = {}
        stuck_count = 0
        collision_occurred = False
        
        # Move each active bead
        for bead in current_beads:
            # Unpack bead details
            x, y, w, d, i, active = bead
            
            # Skip inactive beads
            if not active:
                stuck_count += 1
                continue
            
            # Calculate new position
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            
            # Check boundary
            if not in_range(nx, ny):
                bead[5] = False  # Mark as stuck
                stuck_count += 1
                continue
            
            # Update bead position
            bead[0], bead[1] = nx, ny
            
            # Track positions
            pos_key = (nx, ny)
            if pos_key not in positions:
                positions[pos_key] = []
            positions[pos_key].append(bead)
        
        # Handle collisions
        for pos_beads in positions.values():
            if len(pos_beads) > 1:
                # Sort by weight (descending), then by index (descending)
                pos_beads.sort(key=lambda x: (-x[2], -x[4]))
                
                # Keep only the first (most influential) bead
                for collision_bead in pos_beads[1:]:
                    if collision_bead[5]:
                        collision_bead[5] = False
                        collision_occurred = True
        
        # Update latest collision time
        if collision_occurred:
            latest_collision = time
        
        # Check termination conditions
        if stuck_count == n:
            break
        
        time += 1
    
    return latest_collision

def main():
    # Read number of test cases
    t = int(sys.stdin.readline().strip())
    
    # Process each test case
    for _ in range(t):
        # Read number of beads
        n = int(sys.stdin.readline().strip())
        
        # Read bead information
        beads = []
        for i in range(n):
            x, y, w, d = sys.stdin.readline().split()
            # [x, y, weight, direction, original_index, active]
            beads.append([float(x), float(y), int(w), d, i, True])
        
        # Solve and print result
        result = solve_bead_simulation(n, beads)
        print(result)

if __name__ == "__main__":
    main()