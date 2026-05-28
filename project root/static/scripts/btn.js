// btn
async function hndl_btn_coin(tcoin, tcola, ticon, srtr) {
    // update: slave
    // if (srtr) { await fetch(`http://${glb_Thost}:${glb_Tport}/cpad/?tcoin=${tcoin}&tsorc=srtr`); } // const check =
    // update: master
    if (!srtr) { 
        // get: cpad (PERD, PROP, CHRT, ANLZ, DCSN, STEP, ttfrm, dbxyuhv)
        // let response1 = {}; while (!response1.ok) { response1 = await fetch(`http://${glb_Thost}:${glb_Tport}/cpad/?tcoin=${tcoin}&tsorc=btn`); }
        // const jsonRes1 = await response1.json(); if (jsonRes1.message === 'cancelled!') { return; }
        let PERD = null, PROP = null, CHRT = null, ANLZ = null, DCSN = null, STEP = null, ttfrm = null;
        let dbtxtul = null, dbtxtuy = null, dbtxthl = null, dbtxthy = null, dbtxtvl = null, dbtxtvy = null, dbtxtrl = null, dbtxtry = null;
        let response1 = {}; while (!response1.ok) { response1 = await fetch(`http://${glb_Thost}:${glb_Tport}/vbsy/`); }
        let response2 = {}; while (!response2.ok) { response2 = await fetch(`http://${glb_Thost}:${glb_Tport}/rbsy/`); }
        const jsonRes1 = await response1.json(); const VBSY = jsonRes1.VBSY; const jsonRes2 = await response2.json(); const RBSY = jsonRes2.RBSY;
        if (0<VBSY.length) { 
            for (const cpar of VBSY) { 
                if ((new Date().getSeconds())<30) { // && (new Date().getMinutes())!==30) { // [4].includes %n // 30<
                    let response3 = {}; let jsonRes3 = null;
                    while (!response3.ok) { response3 = await fetch(`http://${glb_Thost}:${glb_Tport}/cpad/?tcoin=${cpar.tcoin}&tcola=${tcola}&tsorc=btn`); }
                    jsonRes3 = await response3.json(); if (jsonRes3.message === 'cancelled!') { return; } 
                    PERD = jsonRes3.PERD; PROP = jsonRes3.PROP[jsonRes3.PROP.length - 1]; CHRT = jsonRes3.CHRT;
                    ANLZ = jsonRes3.ANLZ[jsonRes3.ANLZ.length - 1]; DCSN = jsonRes3.DCSN[jsonRes3.DCSN.length - 1]; 
                    STEP = jsonRes3.STEP[jsonRes3.STEP.length - 1]; ttfrm = jsonRes3.ttfrm;
                    dbtxtul = jsonRes3.dbtxtul;  dbtxtuy = jsonRes3.dbtxtuy; dbtxthl = jsonRes3.dbtxthl;  dbtxthy = jsonRes3.dbtxthy;
                    dbtxtvl = jsonRes3.dbtxtvl;  dbtxtvy = jsonRes3.dbtxtvy; dbtxtrl = jsonRes3.dbtxtrl;  dbtxtry = jsonRes3.dbtxtry; 
                } else { break; } }}
        if (0<RBSY.length) { 
            for (const cpar of RBSY) { 
                if ((new Date().getSeconds())<30) { //  && (new Date().getMinutes())!==30) { // [4].includes %n // 30<
                    let response4 = {}; let jsonRes4 = null;
                    while (!response4.ok) { response4 = await fetch(`http://${glb_Thost}:${glb_Tport}/cpad/?tcoin=${cpar.tcoin}&tcola=${tcola}&tsorc=btn`); }
                    jsonRes4 = await response4.json(); if (jsonRes4.message === 'cancelled!') { return; } 
                    PERD = jsonRes4.PERD; PROP = jsonRes4.PROP[jsonRes4.PROP.length - 1]; CHRT = jsonRes4.CHRT;
                    ANLZ = jsonRes4.ANLZ[jsonRes4.ANLZ.length - 1]; DCSN = jsonRes4.DCSN[jsonRes4.DCSN.length - 1]; 
                    STEP = jsonRes4.STEP[jsonRes4.STEP.length - 1]; ttfrm = jsonRes4.ttfrm;
                    dbtxtul = jsonRes4.dbtxtul;  dbtxtuy = jsonRes4.dbtxtuy; dbtxthl = jsonRes4.dbtxthl;  dbtxthy = jsonRes4.dbtxthy;
                    dbtxtvl = jsonRes4.dbtxtvl;  dbtxtvy = jsonRes4.dbtxtvy; dbtxtrl = jsonRes4.dbtxtrl;  dbtxtry = jsonRes4.dbtxtry; 
                } else { break; } }}
        let response5 = {}; let jsonRes5 = null;
        while (!response5.ok) { response5 = await fetch(`http://${glb_Thost}:${glb_Tport}/cpad/?tcoin=${tcoin}&tcola=${tcola}&tsorc=btn`); }
        jsonRes5 = await response5.json(); if (jsonRes5.message === 'cancelled!') { return; } 
        PERD = jsonRes5.PERD;  PROP = jsonRes5.PROP[jsonRes5.PROP.length - 1];  CHRT = jsonRes5.CHRT;
        ANLZ = jsonRes5.ANLZ[jsonRes5.ANLZ.length - 1];  DCSN = jsonRes5.DCSN[jsonRes5.DCSN.length - 1];
        STEP = jsonRes5.STEP[jsonRes5.STEP.length - 1];  ttfrm = jsonRes5.ttfrm;
        dmaxd = jsonRes5.dmaxd; dtotd = jsonRes5.dtotd; dmaxdacc = jsonRes5.dmaxdacc; dtotdacc = jsonRes5.dtotdacc;
        dbtxtul = jsonRes5.dbtxtul;  dbtxtuy = jsonRes5.dbtxtuy; dbtxthl = jsonRes5.dbtxthl;  dbtxthy = jsonRes5.dbtxthy;
        dbtxtvl = jsonRes5.dbtxtvl;  dbtxtvy = jsonRes5.dbtxtvy; dbtxtrl = jsonRes5.dbtxtrl;  dbtxtry = jsonRes5.dbtxtry;
        // const ULTD = jsonRes5.ULTD; const HLTD = jsonRes5.HLTD; const VLTD = jsonRes5.VLTD; const RLTD = jsonRes5.RLTD;
        // plot: CHRT
        plotPriceChart(CHRT, tcoin);
        // call: tout & tbox , update table uhvr
        await tout(ttfrm, dbtxtul, dbtxtuy, dbtxthl, dbtxthy, dbtxtvl, dbtxtvy, dbtxtrl, dbtxtry, dmaxd, dmaxdacc, dtotd, dtotdacc); await tbox(tcoin, tcola, ticon, PERD, PROP, ANLZ, DCSN, STEP);
        const response6 = await fetch(`http://${glb_Thost}:${glb_Tport}/tab-r/`); const jsonRes6 = await response6.json(); const tab = jsonRes6.tab; await slct_tab(tab); }
};