package bomberman.domain {
	
	public class Bomb {
		
		public var position:Position = new Position(0, 0);
		public var owner:Player = new Player();
		public var secondsToGo:int = 5;
		public var exploding:Boolean = false;
		
		public Bomb(position:Position, owner:Player, secondsToGo:int) {
			this.position = position;
			this.owner = owner;
			this.secondsToGo = secondsToGo;
		}
			
		public function burnFuse():void {
			this.secondsToGo--;
			if(this.secondsToGo == 0) {
				explode();
			}
		}

		public function explode():void {
		}
	}
	
}
