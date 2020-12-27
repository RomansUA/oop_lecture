TestClass = type('TestClass', (), {'test1': True})

MetaClass = type('MetaClass', (TestClass,),{'test2': False})

meta = MetaClass()


print(meta)
print(meta.test1)
print(meta.test2)