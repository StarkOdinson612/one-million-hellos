setInterval(async function() {
    await fetch("https://one-million-hellos.herokuapp.com/api")
    .then(response => response.json())
    .then(data => {
    //here you need to do the action to change the data on the page
        document.getElementById("list").innerHTML = data['text'];
        console.log("I HAVE ATTEMPTED TO REFRESH THE PAGE!");
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}, 300);