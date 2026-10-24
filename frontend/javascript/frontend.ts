export{}

async function post() {
    const output1 = document.getElementById("1") as HTMLInputElement || null
    const output2 = document.getElementById("2") as HTMLInputElement || null

    const id = parseInt(output1.value)
    const name = output2.value

    try {
        let config = await fetch("http://localhost/p",{
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name: name,id: id})
        })

        let answer = await config.json()
        console.log(answer)
    }catch(error){
        console.log('failed to fetch')
    }
}