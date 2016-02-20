def sanitise(unsafe: Integer): Integer?#Safe{
return unsafe;
}
var x: Integer#Safe = 5
var y: Integer = sanitise(x)
print(y)