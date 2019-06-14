@echo off
@title minecraft server

echo starting minecraft server
cd server
java -Xms1024M -Xmx1024M -jar -DIReallyKnowWhatIAmDoingISwear ../jars/spigot-1.14.2.jar -o true

PAUSE