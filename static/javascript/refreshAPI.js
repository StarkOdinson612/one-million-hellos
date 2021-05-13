setInterval(async function() {
    await fetch("http://localhost:5000/api")
    .then(response => response.json())
    .then(data => {
    //here you need to do the action to change the data on the page
        document.getElementById("list").innerHTML = data['text'];
        console.log("I HAVE ATTEMPTED TO REFRESH THE PAGE");
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}, 3);