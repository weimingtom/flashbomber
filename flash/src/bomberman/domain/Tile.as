package bomberman.domain {

	import flash.display.*;

	public class Tile extends Sprite {
		
		public static const EMPTY:int = 1;
		public static const SOLID:int = 2;
		public static const BREAKABLE:int = 3;
		
		private var gfx:BitmapData;
		public var type:int = 0;
		public var item:Object = null;		
		
		public function Tile(type:int):void {
			this.type = type;	
		}
		
		public function draw():void {}
		
		public function hasItem():Boolean {
			return item != null ? true : false;
		}
	}
}
