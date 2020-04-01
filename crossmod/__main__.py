from crossmod.ml.subreddit_monitor import CrossmodSubredditMonitor
from crossmod.ml.classifiers import CrossmodClassifiers
from crossmod.crossmod_gunicorn import CrossmodGunicorn
import click
import crossmod
from pyfiglet import Figlet

@click.command()
@click.argument('mode')
def main(mode):
  crossmod_ascii_banner = Figlet(font='graffiti')
  print(crossmod_ascii_banner.renderText('crossmod'))

  if mode == "api":
    crossmod.clf_ensemble = CrossmodClassifiers()
    print("API\n")
    options = {
      'bind': '0.0.0.0:8000',
      'preload_app': True,
      'workers': 3
    }
    CrossmodGunicorn(crossmod.app, options).run()

  elif mode == "monitor":
    print("Monitor\n")
    subreddit_monitor = CrossmodSubredditMonitor()
    subreddit_monitor.monitor()

if __name__=="__main__":
  main()
