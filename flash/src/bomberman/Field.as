package bomberman {
import mx.core.UIComponent;
import flash.geom.Point;
import flash.display.Bitmap;
import flash.display.Sprite;

public class Field extends Sprite {
    private static const _:int = 0;
    private static const W:int = 1;

    [Embed(source="tile2.gif")]
    [Bindable]
    private var wall:Class;

    private var tilesX:int = 13;
    private var tilesY:int = 12;
    private var tileW:int = 40;
    private var tileH:int = 40;

    private var fieldTiles:Array = [
                                   [W,W,W,W,W,W,W,W,W,W,W,W,W],
                                   [W,_,_,_,_,_,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,_,_,_,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,_,_,_,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,_,_,_,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,_,_,_,_,_,_,_,_,_,W],
                                   [W,_,W,_,W,_,W,_,W,_,W,_,W],
                                   [W,_,_,_,_,_,_,_,_,_,_,_,W],
                                   [W,W,W,W,W,W,W,W,W,W,W,W,W]
                                   ];


    public function Field() {
        super();
        for(var i:int = 0; i < fieldTiles.length; i++) {
            for(var j:int = 0; j < fieldTiles[i].length; j++) {
                var tile:Bitmap;

                if (fieldTiles[i][j] == W) {
                    tile = new wall() as Bitmap;
                    tile.y = i * tileH;
                    tile.x = j * tileW;
                    tile.width = 40;
                    tile.height = 40;
                    addChild(tile);
                }
            }
        }
    }

    public function canMove(x:int, y:int):Boolean {
        var tilex:int = x / 40;
        var tiley:int = y / 40;

        if (fieldTiles[tiley][tilex] == W)
            return false;

        return true;
    }
}
}