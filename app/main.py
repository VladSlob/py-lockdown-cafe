import datetime
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"

    masks_needed = sum(1 for friend in friends if not friend.get('wearing_a_mask', False))
    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    
    return f"Friends can go to {cafe.name}"
