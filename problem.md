Welcome! Your mission, should you chose to accept it, is to
build a basic REST/JSON API around Yelp's Academic Dataset.

First step, download the dataset (http://www.yelp.com/academic_dataset).

Second step, build a REST API that can serve up the following views into
the dataset:
 * List all colleges
 * List all of the businesses associated with a given college
 * List all of the reviews for a given business
 * List all of the reviews for a given user

You will be juged on:
 * Quality of your code. Is this something you would want to run in production?
 * Conformance to the API
 * How good are your unit tests

If you're having fun with the project, adding a couple extra entrypoints
to the API that give interesting views into the data.

## Ok, how bout this for idea:

### Unneeded, but convenient

 * /business/all
 * /school/all
 * /user/all

### Required views

 * /business/reviews?id=<xxx>
 * /business/users?id=<xxx>
 * /user/reviews?id=<xxx>
 * /school/businesses?id=<xxx>

Could potentially give a js fronend that they can plug into... App should be interactive
through that js frontend.... I kinda like that idea.
