
print("please type in your bank USSD.")
option=input("")

print("welcome to UBA.\n1.Checkbalance\n2.Transfer\n3.Airtime\n4.Loans\n5.Other Services")
option=input("")
if (option=="1"):
	print("Enter Pin")
	pin=input("")
	print("Your Balance is N34000")
	print("Enter 1 To go back to menu")
	print("Enter # to exit")
	option=input("")
	if (option=="1"):
		print("1Checkbalance\n2Transfer")
		option=input("")
		if option=="2":
			print("Enter amount")
			amount=input("")
			print("Enter Account number")
			number=input("")
			print("1.Access\n2.UBA\n3.First Bank\n4.FCMB\n5.Union bank")
			option=input("")
			if (option=="1"):
				print("Usman Bello")
				print("Enter 1 to confrim")
				print("Enter 2 to go bank")
				option=input("")
				if option=="1":
					print("Enter pin")
					pin=input("")
				print("Transaction Successful")
				print("Enter * to go to menu")
				print("Enter ** to exit")
				option=input("")
				while option != "**":
					if option == "*":
						print("1Checkbalance\n2Transfer")
					else:
							print("invalid option")
							print("Enter * to go to menu")
							print("Enter ** to exit")
							break
				if (option=="2"):
					print("Usman Bello")
					print("Enter 1 to confrim")
					print("Enter 2 to go bank")
					print("Enter * to exit")
					option=input("")
					while option!="*":
						if option=="1":
							print("Enter pin")
						pin=input("")
						print("Transaction successful")
						if option == "2":
							print("1.Access\n2.UBA\n3.First Bank\n4.FCMB\n5.Union bank")
						else:
								print("invalid Option")
								print("Enter * to go to menu")
								print("Enter ** to exit")
								option=input("")
								while option != "**":
									if option == "*":
										print("1Checkbalance\n2Transfer")
									else:
											print("invalid option")
											print("Enter * to go to menu")
											print("Enter ** to exit")
											break
						if (option=="3"):
							print("Usman Bello")
							print("Enter 1 to confrim")
							print("Enter 2 to go bank")
							print("Enter * to exit")
							option=input("")
							if option=="1":
								print("Enter pin")
								pin=input("")
								print("Transaction Successful")
								if option == "2":
									print("1.Access\n2.UBA\n3.First Bank\n4.FCMB\n5.Union bank")
								else:
										print("invalid Option")
										print("Enter * to go to menu")
										print("Enter ** to exit")
										option=input("")
										while option != "**":
											if option == "*":
												print("1Checkbalance\n2Transfer\n3Airtime\n4Xtracashloan")
												if option == "*":
													exit
												else:
													print("invalid option")
													print("Enter * to go to menu")
													print("Enter ** to exit")
													break
								if (option=="4"):
									print("Usman Bello")
									print("Enter 1 to confrim")
									print("Enter 2 to go bank")
									option=input("")
									if option=="1":
										print("Enter pin")
										pin=input("")
										print("Transaction Successful")
										if option == "2":
											print("1.Access\n2.UBA\n3.First Bank\n4.FCMB\n5.Union bank")
										else:
												print("invalid Option")
												print("Enter * to go to menu")
												print("Enter ** to exit")
												break
												option=input("")
												while option != "**":
													if option == "*":
														print("1Checkbalance\n2Transfer\n3Airtime\n4Xtracashloan")
														if option == "*":
															exit
														else:
															print("invalid option")
															print("Enter * to go to menu")
															print("Enter ** to exit")
															break
										if (option=="5"):
											print("Usman Bello")
											print("Enter 1 to confrim")
											print("Enter 2 to go bank")
											option=input("")
											if option=="1":
												print("Enter pin")
												pin=input("")
												print("Transaction Successful")
												if option == "2":
													print("1.Access\n2.UBA\n3.First Bank\n4.FCMB\n5.Union bank")
												else:
														print("invalid Option")
														print("Enter * to go to menu")
														print("Enter ** to exit")
														option=input("")
														break
														while option != "**":
															if option == "*":
																print("1Checkbalance\n2Transfer\n3Airtime\n4Xtracashloan")
																if option == "*":
																	exit
																else:
																	print("invalid option")
																	print("Enter * to go to menu")
																	print("Enter ** to exit")
																	break
																	if option=="#":
																		exit												