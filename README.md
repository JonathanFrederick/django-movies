## Set-up

- Download all files in this repository to your desired directory
- In Terminal, run:
  - ```echo layout python3 >> .envrc```
  - ```direnv allow```
  - ```pip install -r requirements.txt```
  - ```cd movieratings```
  - ```mkdir /ratings/fixtures```
  - ```mkdir data```
- Download the [MovieLens 1M Dataset](http://files.grouplens.org/datasets/movielens/ml-1m.zip)
- Unzip MovieLens data to the data directory we just created
- In Terminal, run:
  - ```python manage.py migrate```
  - ```python manage.py shell```
- While in the Python environment, run:
  - ```from ratings import *```
  - ```models.load_initial_data()```
  - ```exit()```
- Back in Terminal, run:
  - ```python manage.py loaddata movies```
  - ```python manage.py loaddata raters```
  - ```python manage.py loaddata ratings```
  - ```python manage.py runserver```

## To use

To view the top 20 movies by average rating, open ```127.0.0.1:8000/db/movies/top``` in your browser
