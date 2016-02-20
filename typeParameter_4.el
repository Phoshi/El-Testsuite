record Tuple2 T K = (Item1: T, Item2: K)
def print(t2: Tuple2 Integer, String){
print(Item1(t2));
print(Item2(t2));
}
val myTuple: Tuple2 Integer, String = Tuple2(2, "Hello, world!")
print(myTuple)