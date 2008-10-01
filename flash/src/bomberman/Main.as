package bomberman  {


import mx.core.UIComponent;
import mx.core.BitmapAsset;
import mx.core.Application;
import flash.display.Loader;
import flash.display.Bitmap;
import flash.events.Event;
import flash.events.KeyboardEvent;
import flash.net.URLRequest;
import flash.utils.Timer;
import flash.events.TimerEvent;
import mx.controls.Label;

public class Main extends UIComponent {
    [Embed(source="tile1.gif")]
    [Bindable]
    private var imageCls:Class;


    private var player1:Bitmap;
    private var player2:Bitmap;
    private var gameTimer:Timer;
    private var aKeyPress:Array = [];
    private var keyPressN:int = 1;
    private var client:Client;
    private var field:Field;
    private var speed:int = 10;
    private var lagLabel:Label;

    public function createGame():void {
        trace("Alku");

        this.width = 520;
        this.height = 520;
        this.x = 0;
        this.y = 0;

        field = new Field();
        field.x = 0;
        field.y = 0;

        addChild(field);

        player1 = new imageCls() as Bitmap;
        player1.width = 40;
        player1.height = 40;
        player1.x = 40;
        player1.y = 40;

        player2 = new imageCls() as Bitmap;
        player2.x = 0;
        player2.y = 0;

        addChild(player1);
        //addChild(player2);

        lagLabel = Application.application.lagLabel as Label;

        stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
        stage.addEventListener(KeyboardEvent.KEY_UP, onKeyUp);

        gameTimer = new Timer(30);
        gameTimer.addEventListener(TimerEvent.TIMER, runGame);
        gameTimer.start();

        client = new Client("localhost", 5555, "peli", "player1");

    }

    private function runGame(event:TimerEvent):void {
        checkKeys();
        moveOtherPlayers();
        lagLabel.text = "lag: " + client.getLag() + "ms";
    }

    private function onKeyDown(event:KeyboardEvent):void {
        aKeyPress[event.keyCode] = keyPressN++;
    }

    private function onKeyUp(event:KeyboardEvent):void {
        aKeyPress[event.keyCode] = 0;
    }

    private function checkKeys():void {
        var n:int;
        var key:int;
        var posChanged:Boolean;

        if (aKeyPress[38] > 0) {
            n = aKeyPress[38];
            key = 38;

        }
        if (aKeyPress[40] > 0) {
            if (aKeyPress[40] > n) {
                n = aKeyPress[40];
                key = 40;
            }
        }
        if (aKeyPress[37] > 0) {
            if (aKeyPress[37] > n) {
                n = aKeyPress[37];
                key = 37;
            }
        }

        if (aKeyPress[39] && field.canMove(player1.x + 47, player1.y)) {
            if (aKeyPress[39] > n) {
                key = 39;
            }
            player1.x += speed;
            posChanged = true;
        }

        if (key == 38  && field.canMove(player1.x, player1.y - speed)) {
            player1.y -= speed;
            posChanged = true;
        }

        else if (key == 40 && field.canMove(player1.x, player1.y + 47)) {
            player1.y += speed;
            posChanged = true;
        }

        else if (key == 37 && field.canMove(player1.x -speed, player1.y)) {
            player1.x -= speed;
            posChanged = true;
        }


        if (posChanged)
            client.position(player1.x, player1.y);
    }

    private function moveOtherPlayers():void {
        var movements:Array = client.readActions();

        for(var i:int; i < movements.length; i++) {
            var action:String = movements[i];

            if(action.indexOf("UP") != -1)
                player2.y -= 5;
            else if (action.indexOf("DOWN") != -1)
                player2.y += 5;
            else if (action.indexOf("LEFT") != -1)
                player2.x -= 5;
            else if (action.indexOf("RIGHT") != -1)
                player2.x += 5;
        }

        client.clear();
    }
}
}