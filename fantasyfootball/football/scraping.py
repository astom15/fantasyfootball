import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

from football.models import Players, Teams, Positions, Quarterbacks

URL = 'https://www.pro-football-reference.com/years/2022/passing.htm'


def scrape_pfr_qbs():
  try:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    qbs = soup.find('table', id='passing')

    df = pd.read_html(str(qbs))[0]
    df.drop_duplicates(subset=['Player'], inplace=True, keep=False)
    df.drop(['Rk', 'QBrec', 'QBR', 'NY/A', 'ANY/A'], axis=1, inplace=True)
    df = df.rename(columns={'Yds.1': 'SkYds'})
    df = df.fillna(0)
    df = df.reset_index()
    for idx in range(len(df)):
      first, last = format_names(df.loc[idx, 'Player'])
      player = Players(first_name=first, last_name=last,
                       age=df.loc[idx, 'Age'], games_played=df.loc[idx, 'G'], games_started=df.loc[idx, 'GS'])
      team = Teams(team=df.loc[idx, 'Tm'])
      position = Positions(position=df.loc[idx, 'Pos'])
      quarterback = Quarterbacks(yards=df.loc[idx, 'Yds'],
                                 completions=df.loc[idx, 'Cmp'],
                                 attempts=df.loc[idx, 'Att'],
                                 completion_percentage=df.loc[idx, 'Cmp%'],
                                 touchdowns=df.loc[idx, 'TD'],
                                 touchdown_percentage=df.loc[idx, 'TD%'],
                                 interceptions=df.loc[idx, 'Int'],
                                 interception_percentage=df.loc[idx, 'Int%'],
                                 first_downs_passing=df.loc[idx, '1D'],
                                 longest_completed_pass=df.loc[idx, 'Lng'],
                                 average_yards_per_attempt=df.loc[idx, 'Y/A'],
                                 adjusted_average_yards_per_attempt=df.loc[idx, 'AY/A'],
                                 yards_per_completion=df.loc[idx, 'Y/C'],
                                 yards_per_game=df.loc[idx, 'Y/G'],
                                 rating=df.loc[idx, 'Rate'],
                                 times_sacked=df.loc[idx, 'Sk'],
                                 yards_lost_to_sacks=df.loc[idx, 'SkYds'],
                                 sack_percentage=df.loc[idx, 'Sk%'],
                                 comebacks=df.loc[idx, '4QC'],
                                 game_winning_drives=df.loc[idx, 'GWD'])
      player.save()
      team.save()
      position.save()
      quarterback.save()
  except Exception as e:
    print('Scraping job failed', e)


def format_names(name: str):
  player = name.split(" ")
  return player[0], player[1].split('*')[0]


scrape_pfr_qbs()
