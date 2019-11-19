// webServer.js
 
// node.js의 http모듈을 변수 http로 추출합니다.
var http = require('http');
var fs = require('fs');
var port = 80;
var hostName = '127.0.0.1';

var mimeTypes = {
    "html" : "text/html",
    "jpeg" : "image/jpeg",
    "jpg" : "image/jpeg",
    "png" : "image/png",
    "js" : "text/javascript",
    "css" : "text/css",
    "ttf" : "application/x-font-ttf"
}
// http모듈의 createServer 함수를 호출하여 서버를 생성합니다.
// req: request. 웹 요청 매개변수, res: response. 웹 응답 매개변수
var server = http.createServer((req, res) => {
    // writeHead: 응답 헤더를 작성합니다.
    // 200: 응답 성공, text/html: html문서
    var url = req.url;
    if(req.url == '/'){
        url = '/index.html';
    }
    if(req.url == '/favicon.ico'){
        return res.statusCode = 404;
    }
    res.statusCode = 200; // 통신 성공
    // res.setHeader("Content-Type", "text/html");
    var mimeType = mimeTypes[url.split('.').pop()];
    res.setHeader("Content-Type", mimeType);
    
    // end: 응답 본문을 작성합니다.
    res.end(fs.readFileSync(__dirname+url));
    // listen: 매개변수로 포트와 호스트를 지정합니다.
});
server.listen(port);
console.log(`Server running at http://${hostName}:${port}/`);