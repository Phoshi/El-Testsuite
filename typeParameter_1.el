record Foo T = (fooX: T)
val foo: Foo Integer = Foo(1)
val x = fooX(foo)
print(x)