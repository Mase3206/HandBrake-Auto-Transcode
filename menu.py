import getCommands, settings, csv, subprocess
from time import sleep




def sendCommands():
	for i in range(episodeQty):
		if episodes[i] != ['case', 'disk', 'title']:
			cmd = getCommands.allEpisodes(episodeQty, i + 1)

			"""if environment == 'Unix':
				logFileName = ''.join(['logs/', '-'.join(episodes[i]), '.log'])
			elif environment == 'Windows':
				logFileName = ''.join(['logs\\', '-'.join(episodes[i]), '.log'])
			else:
				raise ValueError('Environment variable set to illegal value in `settings.yml`. Only "Windows" and "Unix" are accepted values.')"""
			
			

			if cmd != False:
				print('\nLog: Running "' + ' '.join(cmd) + '"')
				#output = Popen(["mycmd", "myarg"], stdout=PIPE).communicate()[0]
				log = subprocess.run(cmd, stdout=subprocess.PIPE)#.communicate()[0]
				print('Log:', episodes[i], 'is finished.\n')
			else:
				print('\nLog:', episodes[i], 'was set to not rip. If you would like to rip it, set "Rip: " to "True" in its associated .yml file.\n')


				


def main():

	print('\n1. Begin automated transcode')
	print('2. Enter Settings Manager to show or edit settings')
	print('3. Exit')
	choice = int(input(' : '))

	if choice == 1:
		sendCommands()
	elif choice == 2:
		settings.main()
		start()
	elif choice == 3:
		exit()
	else:
		print('Unknown option "' + choice + '".')


def start():
	print("\n\n *** HandBrake TV Show Transcode Automator *** ")
	
	global rawSettings, prettySettings, episodeQty, episodes, environment
	# get current settings
	rawSettings, prettySettings = settings.getSettings(False)
	environment = rawSettings['Environment']

	with open(rawSettings['Episode List Location'], 'r') as csvfile1:
		episodeList = csv.reader(csvfile1, delimiter=',')
		episodes = []

		for row in episodeList:
			episodes.append(row)

		episodeQty = len(episodes) - 1

	main()

start()