import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = '../Batting/t20.csv'

df2 = pd.read_csv(FILE_PATH)



while(True):

	choice = int(input(("Enter choices : 0)Exit 1)Show player with max runs 2)Delete player 3)Plot Graph Runs vs player name\n")))
	if choice == 0 :
		break

	if choice == 1:
		ans=df2[df2.Runs==df2.Runs.max()]
		print(ans)
	
	if choice == 2:
		print(df2.Player)
		ind=int(input("Enter player index : "))

		player = df2.Player[ind]
		
		print("Dropping player :"+player)
		df2=df2.drop(ind)
		
		print("After dropping :")
		print(df2)
	if(choice==3):
		plt.bar(df2.Player,df2.Runs)
		plt.show()

#print(df2.head)


