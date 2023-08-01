

var blocks = {};
var curr_supply = 0;
var init_supply = 0;

window.onload = function() { 
    $("#mine").on("click", function() { 
        $.ajax({ 
            type:"GET", 
            url:"http://127.0.0.1:5000/mine?miner_address=0x00", 
            success: function(data){ 
                console.log(data)
            },
            cache: false
        }); 
    });
}

$(document).ready( function () {

    $.getJSON('http://localhost:5000/blockchain', (returnData) => {
        dataSet = [];
        for (let i = 0; i < returnData.blocks.length; i++) {
            console.log("Working!")
            var block = returnData.blocks[i];
            var result = Object.keys(block).map((key) => [block[key]]);
            dataSet.push(result)
            console.log(result)
        }
        
        $('#table1').DataTable({
            data: dataSet,
            columns: [
                { title: 'Index' },
                { title: 'Miner Address' },
                { title: 'Previous Hash' },
                { title: 'Seed' },
                { title: 'Timestamp' },
                { title: 'Transaction Root' },
                { title: 'Transactions' }
            ]
        });
    });


} );