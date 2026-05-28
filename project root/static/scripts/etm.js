// tab
async function slct_tab(tab) {
    let response1 = {}; let response2 = {}; let response3 = {};
    // get: tab
    while (!response1.ok) { response1 = await fetch(`http://${glb_Thost}:${glb_Tport}/tab-w/?tab=${tab}`); }
    // get: master
    while (!response2.ok) { response2 = await fetch(`http://${glb_Thost}:${glb_Tport}/master/`); } const jsonRes2 = await response2.json(); const tcoin = jsonRes2.tcoin; const tcola = jsonRes2.tcola;
    // get: UHVR
    while (!response3.ok) { response3 = await fetch(`http://${glb_Thost}:${glb_Tport}/uhvr/?tcoin=${tcoin}`); } const jsonRes3 = await response3.json();
    const ULTD = jsonRes3.ULTD; const HLTD = jsonRes3.HLTD; const VLTD = jsonRes3.VLTD; const RLTD = jsonRes3.RLTD;
    // tab: show selected
    const buttons = document.querySelectorAll('.btn_tab'); buttons.forEach(button => { button.classList.remove('active'); if (button.id === tab) { button.classList.add('active');}});
    switch (tab) { case 'ultd': await thst(ULTD); break; case 'hltd': await thst(HLTD); break; case 'vltd': await thst(VLTD); break; case 'rltd': await thst(RLTD); break; default: break; }
};
// tbl
async function thst(data_hist) {
    // rows
    const uhvrBOX = document.getElementById('tbl_hist'); const table = document.createElement('table'); const thead = document.createElement('thead'); const headerRow = document.createElement('tr'); 
    // columns
    const headers = ['tcoin', 'tside', 'drisk', 'drwrd', 'ntent', 'ntext', 'sprm', 'sext', 'dbpur', 'dbdec', 'rx', 'rz']; // 'tsdmc' 'sent''savg' 'nrent', 'nstep' 'tctc'
    // pop: history table
    uhvrBOX.innerHTML = ""; headers.forEach(header => { const th = document.createElement('th'); th.classList.add('UHVR_hed'); th.textContent = header; headerRow.appendChild(th); });
    thead.appendChild(headerRow); table.appendChild(thead); const tbody = document.createElement('tbody'); data_hist.forEach(item => {
        const row = document.createElement('tr'); row.classList.add('UHVR_row'); headers.forEach(column => { 
            const td = document.createElement('td'); td.textContent = item[column]; row.appendChild(td); }); tbody.appendChild(row); });
    table.appendChild(tbody); uhvrBOX.appendChild(table);
};
// trd
async function ftrd(vrlsf) {
    // solo: vsf
    if (vrlsf == 'vls') { bsolo = true; } if (vrlsf == 'vlf') { bsolo = false; }
    let response1 = {}; while (!response1.ok) { response1 = await fetch(`http://${glb_Thost}:${glb_Tport}/vrtrd/?vrlsf=${vrlsf}`); }
};
// mng
async function fmng(vrlsf) { 
    // mngr: vsf
    // if (vrlsf == 'vls_mng') { bmngr = true; localStorage.setItem('bmngr', JSON.stringify(true));} if (vrlsf == 'vlf_mng') { bmngr = false; localStorage.setItem('bmngr', JSON.stringify(false));}
    bmngr = vrlsf; localStorage.setItem('bmngr', vrlsf);
    let response1 = {}; while (!response1.ok) { response1 = await fetch(`http://${glb_Thost}:${glb_Tport}/vrmng/?vrlsf=${vrlsf}`); }
};