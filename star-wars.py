'''Star Wars mad-libs'''

noun = input('Give me a noun: ')
verb = input('Give me a verb: ')
noun2 = input('Give me another noun: ')
adjective = input('Give me an adjective: ')

print("*" * 40)

print('"Look at him. He\'s heading for that small %s," said Luke.' %noun)
print('"I think I can %s him before he gets there... he\'s almost in range," said Han.' %verb)
print('"That\'s not a %s! It\'s a %s," said Obi-Wan.' %(noun, noun2))
print('"It\'s too big to be a %s," said Han.' %noun2)
print('"I have a very %s feeling about this," said Luke.' %adjective)
