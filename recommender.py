import os from data_utils import get_data, load_ratings_data_with_sparkfrom pyspark.sql import SparkSession from pyspark.sql.functions import *spark = SparkSession.builder \    .master('local[*]') \    .config("spark.driver.memory", "15g") \    .appName('MovieRecommender') \    .getOrCreate()size = '25m'get_data(size) #  data is '25M' or '100k'  use argparse# ds = load_ratings_data(size)ratings_df = load_ratings_data_with_spark(size, spark)ratings_df = ratings_df.drop('timestamp')train,test = ratings_df.randomSplit([0.75,0.25])ratings_df.unpersist()from pyspark.ml.recommendation import ALSmodel = ALS(maxIter=10,regParam=0.01,userCol='userId',itemCol='movieId',ratingCol='rating',nonnegative=True,coldStartStrategy="drop")print('Training Model')trained_model = model.fit(train)test_predictions= trained_model.transform(test)predictions_with_error = test_predictions.withColumn('abs error',abs(test_predictions.prediction - test_predictions.rating))predictions_with_error.show()predictions_with_error.groupBy('rating').agg({'abs error':'mean'}).orderBy('rating',ascending=True).show()import numpy as npnew_user = []for i in range(5):    running = [100000000]    running.append( int(np.random.randint(1,55900)) )    running.append(float(np.random.randint(1,10)/2))    new_user.append(running)    new_user_df = spark.createDataFrame(new_user, train.schema)new_predictions = trained_model.transform(new_user_df)"""For later - when finished training and want predictions - need to translate movieId to movie title."""#movies_df = load_movies_data_with_spark(size, spark)