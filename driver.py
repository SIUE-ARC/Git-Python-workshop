__author__ = 'ryanvade'

import base
import fromBase

myBase = base.base()
myBase.printValue()
myBase.printWhoAmI()
myBase.value = "newValue"
myBase.printValue()
myBase.newValue = "A new Value"
print(myBase.newValue)

myFromBase = fromBase.fromBase()
myFromBase.printValue()
myFromBase.printWhoAmI()

print(isinstance(myBase, base.base))
print(isinstance(myBase, fromBase.fromBase))
print(issubclass(base.base, fromBase.fromBase))
print(issubclass(fromBase.fromBase, base.base))
x = myBase.printValue()
x()