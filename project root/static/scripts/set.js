// set
async function hndl_btn_set(b) {
    // post: SETUP
    let response1 = {}; 
    while (!response1.ok) { response1 = await fetch(`http://${glb_Thost}:${glb_Tport}/setup-w/`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ b: b,
        set_Nperps: document.getElementById('set_Nperps').value, set_Rassets_oto: document.getElementById('set_Rassets_oto').value,
        set_Ndeals: document.getElementById('set_Ndeals').value, set_Nserial: document.getElementById('set_Nserial').value,
        set_Tsort: document.getElementById('set_Tsort').value, set_Tdscnd: document.getElementById('set_Tdscnd').value,
        set_Ntimer: document.getElementById('set_Ntimer').value, set_Nturn: document.getElementById('set_Nturn').value,
        set_Ntfrm: document.getElementById('set_Ntfrm').value, set_Troll: document.getElementById('set_Troll').value,
        set_Tback: document.getElementById('set_Tback').value, set_Ncook_dyn_oto: document.getElementById('set_Ncook_dyn_oto').value,
        set_Dsglm: document.getElementById('set_Dsglm').value, set_Dfltr: document.getElementById('set_Dfltr').value, set_Nwhale: document.getElementById('set_Nwhale').value,
        set_Nzrrr_0: document.getElementById('set_Nzrrr_0').value, set_Nzrrr_1: document.getElementById('set_Nzrrr_1').value, set_Tzrrr: document.getElementById('set_Tzrrr').value, set_Rzrrr: document.getElementById('set_Rzrrr').value,
        set_Nzrrd: document.getElementById('set_Nzrrd').value, set_Nzrlm: document.getElementById('set_Nzrlm').value, set_Nzliq: document.getElementById('set_Nzliq').value,
        set_Nstep_dyn_oto: document.getElementById('set_Nstep_dyn_oto').value, set_Dstep_dyn_oto: document.getElementById('set_Dstep_dyn_oto').value,
        set_Nxbeg_dyn_oto: document.getElementById('set_Nxbeg_dyn_oto').value, set_Dcbeg: document.getElementById('set_Dcbeg').value,
        set_Dcfin: document.getElementById('set_Dcfin').value }) }); }
    // if user clicked
    if (b === 'setup') { await updateData(true); }
};