const BASE_URL = "http://127.0.0.1:5000/api"

$(document).ready(getData);


async function getData() {
    // write axios to get listing of cupcakes
    try {
        const response = await axios({
            url: `${BASE_URL}/cupcakes`,
            method: "GET"
        });
        console.log(response.data.cupcakes)
        displayData(response.data.cupcakes)
    }
    catch (e) {
        console.log('something happened in getting data')
        console.log(e)
    }
}

function displayData(data) {
    data.forEach(d => {
        console.log(d)
        $("#cupcakeList").append(`<li><img src="${d.image}">`)
        $("#cupcakeList").append(`${d.flavor}, ${d.rating}, ${d.size}</li>`)
    })

}



// get form data and send it over to 
$("#cupcake").submit(async function (e) {
    e.preventDefault()
    // get data from the form
    const cupcake = {
        "flavor": $('#flavor').val(),
        "size": $('#size').val(),
        "rating": parseFloat($('#rating').val()),
        "image": $('#cupcake_image').val()
    }
    console.log(cupcake)
    try {
        const response = await axios({
            url: `${BASE_URL}/cupcakes`,
            method: "POST",
            data: cupcake
        });
        console.log(response)
        await getData()
    } catch (e) {
        console.log(e)
        console.log('failed at adding new cupcake')
    }



})
