// app
window.onload = async function() {
    // refrest: slow
    await hndl_btn_frsh(false);
    // initiate: coin & tab
    await hndl_btn_coin('BTC', 'USDT', glb_Tibtc, false);
    await slct_tab('hltd');
    // loop: prl
    //while (true) { 
        // call: loops (sort & tick)
        //await updateSrtr(); await updateData(false); } 
};