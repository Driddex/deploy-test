async function post() {
    const idPuter = document.getElementById('1');
    const CreateBtn = document.getElementById('2');
    if (!idPuter || !CreateBtn) {
        console.log('failed to find elements');
        alert('...');
        return;
    }
    const val = Number(idPuter.value);
    try {
        const Post = await fetch('/api/p', {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id: val })
        });
        console.log('posted');
        let response = await Post.json();
        console.log(response);
    }
    catch (error) {
        console.log('error');
    }
}
async function del() {
    const idPuter = document.getElementById('3');
    const CreateBtn = document.getElementById('4');
    if (!idPuter || !CreateBtn) {
        console.log('failed to find elements');
        alert('...');
        return;
    }
    const val = Number(idPuter.value);
    try {
        const Post = await fetch('/api/d', {
            method: 'DELETE',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id: val })
        });
        console.log('deleted');
        let response = await Post.json();
        console.log(response);
    }
    catch (error) {
        console.log('error');
    }
}
