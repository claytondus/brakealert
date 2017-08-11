#!/usr/bin/env python

from datetime import datetime
import obd, sys, time

brake_delta = 0.3
accel_delta = 0.3

port = sys.argv[1]
baud = sys.argv[2]

#obd.logger.setLevel(obd.logging.DEBUG)
conn = obd.OBD(port, baud)

print(conn.status())

if(conn.status() != obd.OBDStatus.CAR_CONNECTED):
	print("Vehicle not connected")
	exit

speedcmd = obd.commands.SPEED;
tpscmd = obd.commands.THROTTLE_POS;

speed = 1
tps = 1

while 1:
	speedres = conn.query(speedcmd)
	speednow = speedres.value.to("mph").magnitude
	if(speed > 15):
		if(((speed - speednow) / speed) > brake_delta):
			print("BRAKE ALERT!!!!\a\a\a")
	speed = speednow
	print '{0}: Speed {1}'.format(str(datetime.utcnow()), speednow)	
	tpsres = conn.query(tpscmd)
	tps = tpsres.value.magnitude
	if(tps > 50):
		print("HARD ACCELERATION\a\a\a")
	print '{0}: Throttle {1}'.format(str(datetime.utcnow()), tps)

	

	time.sleep(0.3)

