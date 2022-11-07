const BASE_URL = "http://127.0.0.1:5000/api"

$(document).ready(function () {
    console.log('testing')
});


async function getData() {
    alert('gotdata')
    // write axios to get listing of cupcakes
    const response = await axios({
        url: `${BASE_URL}/cupcakes`,
        method: "GET"
    });
    console.log(response)

    $("#cupcake_list").append("<li></li>")
}



// get form data and send it over to 
$("#cupcake").submit(function (e) {
    e.preventDefault()
    alert('submitting but not haha')
})

