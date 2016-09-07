# Diary

- Recently, I did buy some boards and sensors from [Adafruit](http://www.adafruit.com). The parts were here. But I didn't have an soldering iron and solder to assemble them. Sean borrowed me his soldering iron. Thank you very much. 
- After soldering, I had to do some setup: The board required the newest Arduino IDE with a new board definition and a driver. I did sucessfully install it. 
- I adapted an [example script](http://cactus.io/hookups/sensors/temperature-humidity/sht31/hookup-arduino-to-sensirion-sht31-temp-humidity-sensor) for the temperature and humidity reading.
- [Infos how to set up the RTC](https://bitbucket.org/orbitalair/arduino_rtc_pcf8563/downloads).
- First in the serial console appeared only strange letters. It took me a while to find out: I had to set the Baud rate to 57600. Then this problem was fixed. 
- I put together two working sketches: One to write to the SD card and one to read out the sensor. Unfortunately, I couldn't get the new script to work again. As soon as the SD card is activated, the sensor just delivers NaNs. I was working for hours on this issue. Even Soma didn't find a solution. After an afternoon of fiddling around with it, I [asked for help on the forum](https://forums.adafruit.com/viewtopic.php?f=22&t=101717) of the seller of the products. 
- Since nobody seems to be able to solve the problem with this board, I decided to move on. I asked Soma if he could bring me one of his Arduinos with logger shield. Unfortunately, he forgot it before the weekend. 
- Why not sending the values directly to a web server? I am trying to set up the Arduino to use the internet connection of my smartphone.
- I was using a PHP script to receive the data on my webserver -- until the provider blocked me. I was then trying to switch to Digital Ocean. Following a tutorial to set up Nginx and PHP that suggested to use a firewall, I locked myself out of Digital Ocean. It took me two hours to recapture my baby server. The PHP part didn't work. So I decided to switch back to my other provider. 
- I had a hard time to send the exact date to the server. The Arduino did send just one digit for some month and days while the server expected two digits. Solution: "sprintf" and a "%02d" combination. 
- The server script did also break when I was using a whitespace between date and time. "&nbsp;" didn't work either. Finally, I had to put an underline between the two fields.
- Since there is no Wifi on the way, I am setting up my cell phone as access point. The sensor Arduino connects to it. 
- I put project v.0.8 in a empty hummus case, go out and stroll around the campus. It's late at night. I hope that I am not looking suspicious to the guard man on the campus with my case with the electronics and the burning leds. To track my stroll, I am using the app OSMAnd on an iPhone. 
- Now, I am importing the GPX file from my smartphone. First, I tried to convert it in Bash with "GPSBabel". I didn't figure out the right parameters, though: The timestamp gets lost. Therefore, I switched over to the python library "gpxpy".
- The system now works. Or better: It worked -- until the second provider blocked me, too. Are two Get-Requests per minute too much? 
- Soma bought Arduinos with logging shields today. I might try to set up the system on these...
- An engineer answered on my second question on the Adafruit forum. He doesn't think that it is a power issue. He suggested to use a different library. Unfortunately, that didn't work either. 
- I tried Soma's board. Since it is a Ardunio clone it needs a own driver. I couldn't get it to work yet. I'll probably stay with the over the air solution. 
- I tried to add the second network that I am regulary using. Unfortunately, the Arduino compiler doesn't allow try -- catch. I'll select the network manually. 
- Autoupload GPS data. https://github.com/ToeBee/OsmAnd-Tracker
- I create a subset of the data containing the hottest spots. These "hotspots" should be put on the map. Since I don't want to have more than one value from one location, we have to filter them depending on the coordinates. The TAs and I spent a long time trying to calculate the distance. The problem: I needed to apply a function pulling values from the row above. 
- Trying to put all together, I experienced another problem: The RTC probably has lost its time. That makes it impossible to match the times from the GPX file and from the sensor readings. I will have to look into this problem later. For now, I am adapting the PHP script. It will take the timestamp from the server, not from the device. I will have to take care of the timezone, though.
- Everything is working -- everything besides of the import of the Trackpoints. I get just five points. There are many more in the file, though. 
 

