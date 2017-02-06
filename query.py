"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
# object: <class 'flask_sqlalchemy.BaseQuery'>
        
# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# Association table manages many to many relationship
# Assotiation table for table1 and table2 contains own primary key and
# two foreign keys (foreign key table1 and foreign key table 2)
# to model many to many relatioship

# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries

# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter_by(brand_id='ram').first()
#print q1

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter(Model.name == 'Corvette',
                        Model.brand_id == 'che').all()
#print q2

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year > 1960).all()
#print q3

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()
#print q4

# Get all models with names that begin with "Cor."
q5 = Model.query.filter(Model.name.like('Cor%')).all()
#print q5

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903,
                        Brand.discontinued.is_(None)).all()
#print q6

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter(Brand.discontinued.isnot(None) |
                        (Brand.founded < 1950)).all()
print q7

# Get any model whose brand_id is not "for."
q8 = Model.query.filter(Model.brand_id != 'for').all()
#print q8


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_info = db.session.query(Model.name, Brand.name, Brand.headquarters).\
                            join(Brand).filter(Model.year == year).all()

    for model in model_info:
        name, brand_name, headquarters = model
        print name, brand_name, headquarters

    print 'Total: ', len(model_info)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    brands_info = db.session.query(Brand.name, Model.name, Model.year).\
                            outerjoin(Model).order_by(Brand.name, Model.year).all()

    for brand in brands_info:
        brand_name, model_name, year = brand
        print brand_name, model_name, year

    print 'Total: ', len(brands_info)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    mystr = '%' + mystr + '%'
    return Brand.query.filter(Brand.name.like(mystr)).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()



#get_model_info(1964)
#get_brands_summary()
#print search_brands_by_name('ler')
#print get_models_between(1960, 1970)
