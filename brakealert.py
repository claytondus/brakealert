import obd

port = sys.argv[1]
baud = sys.argv[2]

conn = obd.OBD(port, baud)

speedcmd = obd.commands.SPEED;
tpscmd = obd.command.TPS;

while 1
	speedres = conn.query(speedcmd)
	print(speedres.value.to("mph")	
	tpsres = conn.query(tpsres)
	print(tpsres.value)

