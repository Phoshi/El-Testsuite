record Foo T = (fooX: T)
def fooble(x: Foo Integer){
print(1);
}
def fooble(x: Foo String){
print(2);
}
fooble(Foo("Hi"))
fooble(Foo(0))