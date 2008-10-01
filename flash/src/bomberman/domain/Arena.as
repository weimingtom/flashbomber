package game {

	import flash.display.Loader;	
	import flash.display.Sprite;
	
	public class Arena extends Sprite {
		
		public var arenaName:String = "The Grid";

		private var sizeX:int = 20;
		private var sizeY:int = 10;
		
		private var amountOfExtraBombs:int = 20;
		private var amountOfExtraFlames:int = 10;
		private var amountOfKicks:int = 4;
		
		private var tiles:Array = new Array();

		public function initBasicArena():void {
			var x:int, y:int;
			solidLine(0);
			for (y = 0; y < sizeY - 2; y++) {
				if (y % 2 == 0) {
					oddLine(y);	
				} else {
					evenLine(y);
				}
			}
			solidLine(sizeY);
			addBonusItems();			
		}
			
		private	function oddLine(line:int):void {				
			var x:int, y:int;
			tiles[line][0] = new Tile(Tile.SOLID);
			for (x = 1; x < sizeX - 1; x++) {
				tiles[line][x] = new Tile(Tile.BREAKABLE);
			}				
			tiles[line][sizeX] = new Tile(Tile.SOLID);
		}
			
		private function evenLine(line:int):void {
			var x:int, y:int;
			tiles[line][0] = new Tile(Tile.SOLID);
			for (x = 0; x < sizeX; x++) {
				if (x % 2 == 0) {
					tiles[line][x] = new Tile(Tile.BREAKABLE);
				} else {
					tiles[line][x] = new Tile(Tile.SOLID);
				}
			}				
			tiles[line][sizeX] = new Tile(Tile.SOLID);
		}
		
		private function solidLine(line:int):void {
			var x:int, y:int;
			for (x = 0; x < sizeX; x++) {
				tiles[line][x] = new Tile(Tile.SOLID);
			}				
		}

		private function addBonusItems():void {
			var x:int, y:int;
			for (y = 0; y < sizeY; y++) {
				for (x = 0; x < sizeX; x++) {
					var tile:Tile = tiles[y][x];
					if (tile.type == Tile.BREAKABLE) {
						// randomize some bonus items	
					}
				}
			}
		}				
		
		internal function loadTiles():void {
			// use Loader class to load the bitmap image containing tiles
		}

		public function draw():void {
			this.graphics.beginFill(0xFFCC00);
			this.graphics.drawCircle(130, 130, 30);
		}
	}
		
}

