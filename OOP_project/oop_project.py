from bankaccount import *

dave=bankaccount(10000,"dave")
sara=bankaccount(5000,"sara")

dave.getbalance()
sara.getbalance()

dave.deposit(2000)

sara.withdraw(20000)
dave.withdraw(20)

sara.transfer(200,dave)
dave.withdraw(20000)

jim=intrestrewardacc(1000,"jim")
jim.getbalance()
jim.deposit(2000)
jim.transfer(4000,dave)

blaze=savingaccount(1000,"blaze")
blaze.getbalance()
blaze.transfer(4000,"jim")