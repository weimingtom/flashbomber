package bomberman {
	
import mx.core.UIComponent;
import flash.geom.Point;
import flash.display.Bitmap;
import flash.display.Sprite;

public class Field extends Sprite {
	
    private static const _:int = 0;
    private static const W:int = 1;
    private static const B:int = 2;

    [Embed(source="tile_desert_solid.png")]
    [Bindable]
    private var wall:Class;

    [Embed(source="tile_desert_empty.png")]
    [Bindable]
    private var empty:Class;

    [Embed(source="tile_desert_breakable.png")]
    [Bindable]
    private var breakable:Class;
	
	
    private var tilesX:int = 13;
    private var tilesY:int = 12;
    private var tileW:int = 32;
    private var tileH:int = 32;

    private var fieldTiles:Array = [
                                   [W,W,W,W,W,W,W,W,W,W,W,W,W],
                                   [W,B,B,B,_,_,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,_,_,_,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,B,B,B,B,B,_,_,_,_,W],
                                   [W,_,W,_,W,B,W,B,W,_,W,_,W],
                                   [W,_,_,B,_,B,_,B,B,B,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,_,_,B,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,B,W,_,W],
                                   [W,_,_,_,B,B,B,B,_,_,_,_,W],
                                   [W,W,W,W,W,W,W,W,W,W,W,W,W]
                                   ];


    public function Field() {
        super();
        for(var i:int = 0; i < fieldTiles.length; i++) {
            for(var j:int = 0; j < fieldTiles[i].length; j++) {
                var tile:Bitmap;

                if (fieldTiles[i][j] == W) {
                    tile = new wall() as Bitmap;
                } else if (fieldTiles[i][j] == _) {
                    tile = new empty() as Bitmap;
                } else if (fieldTiles[i][j] == B) {
                    tile = new breakable() as Bitmap;
				}
				tile.y = i * tileH;
				tile.x = j * tileW;
				tile.width = tileW;
				tile.height = tileH;
				addChild(tile);				
            }
        }
    }

    public function canMove(x:int, y:int):Boolean {
        var tilex:int = x / 32;
        var tiley:int = y / 32;

        if (fieldTiles[tiley][tilex] == W)
            return false;

        return true;
    }
}
}