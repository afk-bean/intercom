var url = "ws://127.0.0.1:8080"

const WebSocket = require("ws");

const wss = new WebSocket.Server({port: 812});

wss.on("connection", ws =>{
    console.log("new client connected")

    ws.on("close", () => {
        console.log("client died")

    });

});