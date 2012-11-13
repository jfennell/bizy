## NOTE

This is currently in draft form. `problem.txt` is probably out of date and everything
should be taken with a grain of salt. I also have no automated testing at this point,
which is also kinda bad.

## Getting started

Pull the repo. Run

	python main.py

Then hit [localhost:8888](http://localhost:8888) to see the running app. This is very exciting, but you will
not have any data to run with. You can download the full [dataset](http://www.yelp.com/academic_dataset)
or you can run

	python load_dataset.py --path data/small_dataset.json

to get a *very* tiny sample set.

### What to look at once you have data

Some things to look at are:

 * [/business/all](http://localhost:8888/business/all)
 * [/school/all](http://localhost:8888/school/all)
 * [/user/all](http://localhost:8888/user/all)

Based on the ids that you get clicking through those different spots you can look at 

 * [/business/revews](http://localhost:8888/business/reviews)
 * [/business/users](http://localhost:8888/business/users)
 * [/user/reviews](http://localhost:8888/user/reviews)
 * [/school/businesses](http://localhost:8888/school/businesses)
