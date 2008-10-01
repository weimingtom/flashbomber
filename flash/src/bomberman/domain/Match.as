package game {
	
	public class Match {
		
		private var date:Date = new Date();
		private var arena:Arena = new Arena();		
		private var neededWins:int = 4;
		private var duration:int = 2;
		private var players:Array = new Array();		
		private var winner:Player = new Player();
		
		public function addPlayer(player:Player):void {
			players.push(player);
		}
		
	}
}
