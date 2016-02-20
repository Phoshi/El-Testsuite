typeclass Showable T = {show(instance: T): String};
instance Showable Integer = {
def show(instance: Integer): String {
return "Integer";
}
}
instance Showable String = {
def show(instance: String): String){
return "String";
}
}
val int = show(1)
val str = show("hi")
print(int)
print(str)