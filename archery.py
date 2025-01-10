"""
This program accepts three sets of coordinates on an archery target, converts it to a ring location
on the target and computes and outputs the total score. This is the solution file.

J. Cihlar - January 2025
"""

import math

def compute_distance(x: float, y: float) -> float:
    """
    Computes the distance from a coordinate to the origin.

    Parameters:
        x(float): The x-coordinate
        y(float): The y-coordinate
    
    Returns: 
        float: The distance from the x,y coordinate to the origin.
    """
    return math.sqrt(x**2 + y**2)

def get_score(distance: float) -> int:
    """
    Converts a distance from the origin to a score on an olympic archery target. It assumes
    the target is composed of 10 concentric circles with 6.1cm as the radius. The inner-most circle scores 10
    and decreases as you go further out.

    Parameters:
        distance(float): The distance from the x,y coordinate to the origin.
    Returns:
        int: The score the particular coordinate earns.
    """
    WIDTH: float = 6.1
    if distance <= WIDTH:
        return 10
    
    if distance <= 2 * WIDTH:
        return 9
    
    if distance <= 3 * WIDTH:
        return 8
    
    if distance <= 4 * WIDTH:
        return 7
    
    if distance <= 5 * WIDTH:
        return 6
    
    if distance <= 6 * WIDTH:
        return 5
    
    if distance <= 7 * WIDTH:
        return 4
    
    if distance <= 8 * WIDTH:
        return 3
    
    if distance <= 9 * WIDTH:
        return 2
    
    return 1

def main() -> None:
    total_score: int = 0 
    # process three inputs
    for _ in range(3):
        line: str = input()
        x,y = line.split()
        x = float(x)
        y = float(y)
            # compute the distance and conver to a score
        distance: float = compute_distance(x, y)
        score: int = get_score(distance)
            # add the score to the total
        total_score += score
    
    print(total_score)

if __name__ == "__main__":
    main()