package game {
	
	public class Skull {
		
		public static const SLOW_MOTION:int = 1;
		public static const FAST_MOTION:int = 2;
		public static const SLOW_BOMBS:int = 3;
		public static const FAST_BOMBS:int = 4;
		public static const MIRROR_MOVEMENT:int = 5;
		public static const TELEPORT:int = 6;
		public static const FORCED_BOMB_DROPPING:int = 7;
		public static const NO_BOMB_DROPPING:int = 8;
		
		public var position:Position = new Position(0, 0);
		public var type:int = 0;
	}
	
}
