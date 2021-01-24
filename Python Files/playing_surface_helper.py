"""
@author: Ross Drucker
"""
import numpy as np
import pandas as pd

from util import get_soup

def create_circle(center = (0, 0), npoints = 500, d = 2, start = 0, end = 2):
    """
    Create a set of x and y coordinates that form a circle (or the arc of a
    circle)
    
    Parameters
    ----------
    center: The (x, y) coordinates of the center of the circle. Default: (0, 0)
    npoints: The number of points with which to create the circle. This will
        also be the length of the resulting data frame. Default: 500
    d: Diameter of the circle IN THE UNITS OF THE PLOT. This default unit will
        be feet. Default: 2 (unit circle)
    start: The angle (in radians) at which to start drawing the circle, where
        zero runs along the +x axis. Default: 0
    end: The angle (in radians) at which to stop drawing the circle, where zero
        runs along the +x axis. Default: 0

    Returns
    -------
    circle_df: A pandas dataframe that contains the circle's coordinate points
    """
    # Create a vector of numbers that are evenly spaced apart between the
    # starting and ending angles. They should be multiplied by pi to be in
    # radians. This vector represents the angle through which the circle is
    # traced
    pts = np.linspace(start * np.pi, end * np.pi, npoints)
    
    # Create the vectors x and y that represent the circle (or arc of a circle)
    # to be created. This is a translation away from the center across (d/2),
    # then rotated by cos(angle) and sin(angle) for x and y respectively. 
    x = center[0] + ((d / 2) * np.cos(pts))
    y = center[1] + ((d / 2) * np.sin(pts))
    
    # Combine points into data frame for output
    circle_df = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    return circle_df

def get_teams_info(league):
    """
    Get the cursory information on teams, their leagues, and what division or
    conference or league they play in. This information comes from ESPN
    
    Parameters
    ----------
    league: The league of which to scrape the information
    """
    # Clean input to make it case-insensitive
    league = league.upper()
    
    # Match with the ESPN string for the link
    league_links = {
        'NCAAM': 'mens-college-basketball',
        'NCAAF': 'college-football',
        'MLB': 'mlb',
        'NFL': 'nfl',
        'NBA': 'nba',
        'NHL': 'nhl',
        'EPL': 'football',
        'WNBA': 'wnba'
    }
    
    if league == 'MLS':
        url = ('https://www.espn.com/soccer/teams/_/league/'
               'USA.1/major-league-soccer')
        
    elif league == 'UEFA CHAMPIONS LEAGUE':
        url = ('https://www.espn.com/soccer/teams/_/league/'
               'UEFA.CHAMPIONS/uefa-champions-league')
        
    elif league == 'UEFA EUROPA LEAGUE':
        url = ('https://www.espn.com/soccer/teams/_/league/'
               'UEFA.EUROPA/uefa-europa-league')
        
    elif league == 'SPANISH PRIMERA DIVISION':
        url = ('https://www.espn.com/soccer/teams/_/league/'
               'ESP.1/spanish-primera-división')
        
    elif league == 'ITALIAN SERIE A':
        url = ('https://www.espn.com/soccer/teams/_/league/'
               'ITA.1/italian-serie-a')
        
    elif league == 'BUNDESLIGA':
        url = ('https://www.espn.com/soccer/teams/_/league/'
               'GER.1/german-bundesliga')
        
    elif league == 'NWSL':
        url = ("https://www.espn.com/soccer/teams/_/league/"
               "USA.NWSL/united-states-nwsl-women's-league")
        
    else:
        url = f'https://www.espn.com/{league_links[league]}/teams'
        
    # Get the raw page source
    soup = get_soup(url)
    
    # Find the divisional breakdown if applicable
    divisions = soup.find_all('div', attrs = {'class': 'mt7'})
    
    # Container for the team information
    team_info = pd.DataFrame()
    
    # Iterate through the divisions/conferences
    for division in divisions:
        # Get the division's name
        division_name = division.find('div', attrs = {'class': 'headline'})
        division_name = division_name.contents[0]
        
        # Get the teams
        team_links = division.find_all(
            'section',
            attrs = {'class': 'TeamLinks'}
        )
        
        # Containers for the division's team's information
        team_ids = []
        team_names_hyphenated = []
        team_full_names = []
        logo_links = []
        
        # Base of logo link
        base_link = 'https://a.espncdn.com/combiner/i?img=/i/teamlogos'
        
        # Iterate through teams
        for item in team_links:
            # Find split point to get relevant information
            if league == 'NCAAF' or league == 'NCAAM':
                temp_league = 'ncaa'
                splitter = 'id/'
                
            elif league in ['epl', 'mls', 'uefa champions league',
                            'uefa europa league', 'spanish primera division',
                            'italian serie a', 'bundesliga', 'nwsl']:
                temp_league = 'soccer'
                splitter = 'id/'
                
            else:
                temp_league = league_links[league]
                splitter = 'name/'
    
            try:
                # Get the team's name, ID, and logo link if the ID is an int
                # (for college teams)
                temp = item.a.get('href')
                split_1 = temp.split(splitter)[1]
                split_2 = split_1.split('/')
                team_id = int(split_2[0])
                team_name_hyphenated = split_2[1]
                team_full_name = item.find('h2').contents[0]
                team_ids.append(team_id)
                team_names_hyphenated.append(team_name_hyphenated)
                team_full_names.append(team_full_name)
                logo_links.append(
                    f'{base_link}/{temp_league}/500/{team_id}.png'
                )
                
            except:
                # Get the team's name, ID, and logo if the ID cannot be
                # converted to an int
                temp = item.a.get('href')
                split_1 = temp.split(splitter)[1]
                split_2 = split_1.split('/')
                team_id = split_2[0]
                team_name_hyphenated = split_2[1]
                team_full_name = item.find('h2').contents[0]
                team_ids.append(team_id)
                team_names_hyphenated.append(team_name_hyphenated)
                team_full_names.append(team_full_name)
                logo_links.append(
                    f'{base_link}/{temp_league}/500/{team_id}.png'
                )
            
            # Combine results into dataframe
            division_teams_info = pd.DataFrame({
                'team_id': team_ids,
                'league': league,
                'division': division_name,
                'team_full_name': team_full_names,
                'team_name_hyphenated': team_names_hyphenated,
                'logo_link': logo_links,
            })
        
        # Combine divisions into main container
        team_info = pd.concat([team_info, division_teams_info])
    
    return team_info

def make_teams_info():
    """
    Call the get_teams_info() function from above and aggregate several
    leagues, then save output
    
    Returns
    -------
    Nothing, but saves the info. This gets cleaned by hand
    """
    # List leagues for which to get information. Note: NCAAM and NCAAW are
    # equivalent, but only listing one reduces redundancy
    leagues = ['NCAAM', 'NCAAF', 'MLB', 'NFL', 'NBA', 'NHL', 'WNBA']
    
    # Container for scraped information
    overall_teams_info = pd.DataFrame()
    
    # Iterate through leagues
    for league in leagues:
        print(f'Now pulling information for {league}')
        # Get the information
        league_teams_info = get_teams_info(league)
        
        # Order by the team's ID
        league_teams_info = league_teams_info.sort_values(by = 'team_id')
        
        # Combine to container
        overall_teams_info = pd.concat([
            overall_teams_info,
            league_teams_info
        ])
        
        
        print(f'Done with {league}')
    
    # Save the results
    overall_teams_info.to_csv('team_info.csv', index = False)
    
    return None

if __name__ == '__main__':
    make_teams_info()