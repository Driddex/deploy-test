async function post() {
    const output1 = document.getElementById("1") || null;
    const output2 = document.getElementById("2") || null;
    const id = parseInt(output1.value);
    const name = output2.value;
    let config = await fetch("http://localhost/p", {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, id: id })
    });
    let answer = await config.json();
    console.log(answer);
}
