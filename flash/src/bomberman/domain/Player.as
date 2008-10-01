package game {
	
	import flash.display.Sprite;
	
	public class Player extends Sprite {
		
		private static const RED:int = 1;
		private static const BLUE:int = 2;
		private static const WHITE:int = 3;
		private static const BLACK:int = 4;
		private static const GREEN:int = 5;

		private static const NORMAL_STATE:int = 1;
		private static const SKULL_STATE:int = 2;
		
		private var playerName:String;
		private var color:int;
		private var startPosition:Position = new Position(0, 0);
		private var currentPosition:Position = new Position(0, 0);
		private var state:int = NORMAL_STATE;
		private var amountOfBombs:int = 1;
		private var lenghtOfFlames:int = 2;
		private var hasKick:Boolean = false;
		private var hasMulti:Boolean = false;

		public function moveLeft():void {} 
		public function moveRight():void {} 
		public function moveUp():void {} 
		public function moveDown():void {}
		public function dropBomb():void {}
		public function stopBomb():void {}
		public function draw():void {}
		
	}
}

