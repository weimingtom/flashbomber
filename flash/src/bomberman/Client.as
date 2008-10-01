package bomberman {
import flash.utils.getTimer;

import flash.net.Socket;
import flash.events.*;

public class Client extends Socket {
    private var gameId:String;
    private var playerId:String;
    private var recievedActions:Array = [];
    private var lastSend:int;
    private var lag:int;

    public function Client(host:String, port:Number, gameId:String, playerId:String) {
        super(host, port);

        this.gameId = gameId;
        this.playerId = playerId;

        addEventListener(Event.CLOSE, closeHandler);
        addEventListener(Event.CONNECT, connectHandler);
        addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
        addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);
        addEventListener(ProgressEvent.SOCKET_DATA, socketDataHandler);
    }

    public function position(x:int, y:int):void {
        writeUTF("ACT:" + gameId + ":" + playerId + ":" + x + "," + y);
        lastSend = getTimer();
        flush();
    }

    public function readActions():Array {
        return recievedActions;
    }

    public function clear():void {
        recievedActions = [];
    }

    public function getLag():int {
        return lag;
    }


    private function closeHandler(e:Event):void {
        //what here?
    }

    private function connectHandler(e:Event):void {
        
    }

    private function ioErrorHandler(e:Event):void {

    }

    private function securityErrorHandler(e:Event):void {

    }

    private function socketDataHandler(e:Event):void {
        recievedActions[recievedActions.length] = readUTF();

        if (recievedActions[recievedActions.length -1].indexOf(playerId) != -1)
            lag = getTimer() - lastSend;
    }
}
}