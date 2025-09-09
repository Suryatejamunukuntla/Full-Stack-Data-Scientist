import statistics
scores=eval(input("enter the scores : "))
print(f"mean =  {statistics.mean(scores):.2f}")
print("median = " ,statistics.median(scores))
print(f"varience = {statistics.variance(scores):.2f}")
