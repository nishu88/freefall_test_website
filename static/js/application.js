
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received 1" + msg.a);
        console.log("Received 2" + msg.b);
        console.log("Received 3" + msg.c);
        
        console.log("Received 3" + msg.l);
        console.log("Received 3" + msg.m);
        console.log("Received 3" + msg.n);
        
        //maintain a list of ten numbers
        
        
        a1 = '<center><p>' + msg.a + '</p></center>';
        b1 = '<center><p>' + msg.b + '</p></center>';
        c1 = '<center><p>' + msg.c + '</p></center>';
        
        l1 = '1<center><p>' + msg.l + '</p></center>';
        m1 = '2<center><p>' + msg.m + '</p></center>';
        n1 = '3<center><p>' + msg.n + '</p></center>';
        
        $('#log1').html(a1);
        $('#log2').html(b1);
        $('#log3').html(c1);
        
        $('#name1').html(l1);
        $('#name2').html(m1);        
        $('#name3').html(n1);
        
        
    });

});