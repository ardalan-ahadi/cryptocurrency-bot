// loading start
async function load_hide() {
    const load = document.getElementById('load'); load.style.display = 'block'; 
    const box_coin = document.getElementById('box_coin'); // const btn_frsh = document.getElementById('btn_frsh'); 
    const box_dcsn = document.getElementById('box_dcsn'); const box_anlz = document.getElementById('box_anlz'); 
    const box_prop = document.getElementById('box_prop'); const box_perd = document.getElementById('box_perd'); 
    const box_chrt = document.getElementById('box_chrt'); const box_step = document.getElementById('box_step'); 
    const box_uhvr = document.getElementById('box_uhvr'); const form = document.getElementById('form');
    box_coin.style.display = box_anlz.style.display = box_dcsn.style.display = form.style.display = // btn_frsh.style.display = 
    box_perd.style.display = box_prop.style.display = box_chrt.style.display = box_step.style.display = box_uhvr.style.display = 'none';
};

// loading finish
async function load_show() {
    const load = document.getElementById('load'); load.style.display = 'none';
    const box_coin = document.getElementById('box_coin'); // const btn_frsh = document.getElementById('btn_frsh'); 
    const box_dcsn = document.getElementById('box_dcsn'); const box_anlz = document.getElementById('box_anlz'); 
    const box_prop = document.getElementById('box_prop'); const box_perd = document.getElementById('box_perd'); 
    const box_chrt = document.getElementById('box_chrt'); const box_step = document.getElementById('box_step'); 
    const box_uhvr = document.getElementById('box_uhvr'); const form = document.getElementById('form');
    box_coin.style.display = box_anlz.style.display = box_dcsn.style.display = form.style.display = // = btn_frsh.style.display
    box_perd.style.display = box_prop.style.display = box_chrt.style.display = box_step.style.display = box_uhvr.style.display = 'block';
};
