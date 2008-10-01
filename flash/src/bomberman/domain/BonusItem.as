package game {
	
	public class BonusItem {
		
		public static const EXTRA_BOMB:int = 1;
		public static const EXTRA_FLAME:int = 2;
		public static const KICK:int = 3;
		public static const TRIPLE_BOMB:int = 4;
		
		public var position:Position = new Position(0, 0);
		public var type:int = 1;
	}
	
}
