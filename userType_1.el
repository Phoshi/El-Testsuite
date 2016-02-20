record Foo = (fooX: Integer, fooY: Integer)
{
val foo = Foo(1, 5);
val x = fooX(foo);
val y = fooY(foo);
print(x);
print(" ");
print(y);
}