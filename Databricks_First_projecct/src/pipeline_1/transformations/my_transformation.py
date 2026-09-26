import dlt

print(range(1,10))

@dlt.table
def demo_table():
  return spark.range(10)
  
