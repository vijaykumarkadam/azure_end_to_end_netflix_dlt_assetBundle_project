from pyspark import pipelines as dp
from pyspark.sql.functions  import *


netflix_cast_rule = {"rule1" : "show_id is NOT NULL"}
@dp.temporary_view
@dp.expect_all(netflix_cast_rule)
def netflix_cast_view():
    df = spark.readStream.table("netflix_cata.silver.netflix_cast")
    return df

@dp.table
def gold_netflix_cast():
    df = spark.readStream.table("netflix_cast_view")
    return df


@dp.temporary_view
@dp.expect_all(netflix_cast_rule)
def netflix_category_view():
    df = spark.readStream.table("netflix_cata.silver.netflix_category")
    return df

@dp.table
def gold_netflix_category():
    df = spark.readStream.table("netflix_category_view")
    return df

@dp.temporary_view
@dp.expect_all(netflix_cast_rule)
def netflix_countries_view():
    df = spark.readStream.table("netflix_cata.silver.netflix_countries")
    return df

@dp.table
def gold_netflix_countries():
    df = spark.readStream.table("netflix_countries_view")
    return df

@dp.temporary_view
@dp.expect_all(netflix_cast_rule)
def netflix_directors_view():
    df = spark.readStream.table("netflix_cata.silver.netflix_directors")
    return df

@dp.table
def gold_netflix_directors():
    df = spark.readStream.table("netflix_directors_view")
    return df


@dp.table
def gold_netflix_titles_stag():
    df = spark.readStream.table("netflix_cata.silver.netflix_titles")
    return df

@dp.materialized_view
def gold_netflix_titles_trans():
    df = spark.read.table("gold_netflix_titles_stag")
    return df

netflix_titles_rule = {
    "rule1" : "show_id is NOT NULL",
    "rule2" : "title is NOT NULL",
    "rule3" : "type is NOT NULL"}
    
@dp.table
@dp.expect_all_or_drop(netflix_titles_rule)
def gold_netflix_titles():
    df = spark.readStream.table("gold_netflix_titles_trans")
    return df















