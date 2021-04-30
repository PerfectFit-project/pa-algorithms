def weekly_kilometers(age):
    '''
    Mock algorithm that returns a weekly training schema given age of user 
    as weekly running kilometers = 40 - (age/2)
    
    Args:
        age (int): Age of the user

    Returns:
        kilometers (float): number of kilometer the user should run this week
    '''
    
    kilometers = (40 - (age)/2)
    return kilometers