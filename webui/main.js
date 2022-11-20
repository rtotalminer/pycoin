

var blocks = {};
var curr_supply = 0;
var init_supply = 0;

function covertBlocksTable(blocks) {
    dataSet = []
    for (let i = 0; i < blocks.length; i++) {
        block_ = [];
        var block = blocks[i];

        var result = Object.keys(block).map((key) => [block[key]]);
        for (let k in result) {
            // Pull out the transactions
            if (k == 6) {
                block_.push("Transaction Hash")
            }
            else {
                block_.push(result[k])
            }
        }

        dataSet.push(block_)
    }
    return dataSet;
}

function mine() {
    var miner_addr = document.getElementById('miner_address_input').value;
    console.log(miner_addr)
    $.getJSON(`http://localhost:5000/mine?miner_address=${miner_addr}`, (returnData) => {
        console.log(returnData)
    });
    
}

function getBlockchain() {

}


$(document).ready( function () {

    $.getJSON('http://localhost:5000/blockchain', (returnData) => {
        dataSet = covertBlocksTable(returnData.blocks);
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