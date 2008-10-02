package bomberman.domain {
	
	import mx.controls.Alert;
	import flash.display.*;
	import flash.text.*;
	import flash.events.KeyboardEvent;
	import flash.events.DataEvent;
	import flash.ui.Keyboard;
	import flash.net.XMLSocket;
	
	public class Game extends Sprite {
		
		private var serverHostName:String = "localhost";			// address for socket connection
		private var serverPort:int = 8080;							// address for socket connection
		private var serverConnectionReady:Boolean = false;
		private var xmlsock:XMLSocket = new XMLSocket();
		
		private var myPlayer:Player = new Player();
		private var otherPlayers:Player = new Player();					// players currently on the game server
	
		public function Game(stage:Stage) {
			stage.addEventListener(KeyboardEvent.KEY_DOWN, keyPressed);
			var arena:Arena = new Arena();
			arena.initBasicArena();
			stage.addChild(arena);	
			arena.draw();
		}
		
		public function setFullScreenMode():void {
			//set Stage displayState to StageDisplayState.FULL_SCREEN	
		}		
		
		private function keyPressed(event:KeyboardEvent):void {
			trace("User pressed key: " + event.keyCode);
			var flags:uint = Alert.OK;
			var alert:Alert = Alert.show("keyCode=" + event.keyCode, "", flags);
			
			if (event.keyCode == Keyboard.ENTER) {
				//dropBomb
			}
			
			switch(event.keyCode) {
				case Keyboard.ENTER:
					myPlayer.dropBomb();
					break;
				case Keyboard.SPACE:
					myPlayer.stopBomb();
					break;
			}
			
			switch (String.fromCharCode(event.keyCode)) {
				case 'A':
					myPlayer.moveLeft();
					break;
				case 'S':
					myPlayer.moveDown();
					break;
				case 'D:':
					myPlayer.moveRight();
					break;
				case 'W':
					myPlayer.moveUp();
					break;
				
			}
			
			//move left, right, up, down, stop bomb
			
		}
		
		private function initBitmapGraphics():void {
			// load stuff and create objects
		}
		
		private function initServerConnection():void {
			try {
				xmlsock.connect(serverHostName, serverPort);
			} catch (e:SecurityError) {
				// TODO: handle error condition
			}
			serverConnectionReady = true;
			xmlsock.addEventListener(DataEvent.DATA, receivedDataFromServer);
		}

		private function closeServerConnection():void {
			// release resources			
			xmlsock.close();
			serverConnectionReady = false;
		}
		
		private function stillConnectedToServer():Boolean {
			return xmlsock.connected;
		}
		
		private function receivedDataFromServer(event:DataEvent):void {
			trace("[" + event.type + "] " + event.data);
			
			// parse XML and update game objects accordingly
		}
		
		private function sendDataToServer(xmlData:String):void {
			xmlsock.send(xmlData);
		}
		
		private function playerJoins():void {
			//
		}
		
		private function playerLeaves():void {
			//
		}
		
	}
		
}
