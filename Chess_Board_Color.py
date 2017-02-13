"""This problem asked for a function to tell if two given cells on a chessboard were the same color and return True or False"""

def chess_board_cell_color(cell1, cell2):
    celllst = [list(cell1),list(cell2)]
    dark = []
    light = []
    dark1 = ('A','C','E','G')
    for x in celllst:
    	if x[0] in dark1 and int(x[1]) % 2 != 0:
      		dark.append(x)
      	elif x[0] not in dark1 and int(x[1]) %2 == 0:
        	dark.append(x)
        else:
            light.append(x)
    if len(dark) > 1 or len(light) > 1:
    	return True
    else:
    	return False
