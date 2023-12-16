//variables
const homeBtn = document.getElementById("home");
const fangraphBtn = document.getElementById("fangraph");
const theathleticBtn = document.getElementById("theathletic");
const fantasyprosBtn = document.getElementById("fantasypros");
const rotoballerBtn = document.getElementById("rotoballer");
const searchBtn = document.getElementById("search");

const newsQuery = document.getElementById("newsQuery");

const newsType = document.getElementById("newsType");
const newsDetails = document.getElementById("newsDetails");


//array
let newsDataArr = [];
//apis

homeBtn.addEventListener("click", function(){
    fetchHomeNews()
});

fangraphBtn.addEventListener("click", function(){

});

theathleticBtn.addEventListener("click", function(){

});

fantasyprosBtn.addEventListener("click", function(){

});

rotoballerBtn.addEventListener("click", function(){

});

searchBtn.addEventListener("click", function(){

});

function myFunc(vars) {
    console.log("here")
    console.log(vars)
    document.getElementById("myText").innerHTML = vars;
    const number = "123";
    document.getElementById("myText").innerHTML = number;
    return vars
}

function displayNews() {

    newsDetails.innerHTML = "";

    // if(newsDataArr.length == 0) {
    //     newsdetails.innerHTML = "<h5>No data found.</h5>"
    //     return;
    // }

    newsDataArr.forEach(news => {

        
        var col = document.createElement('div');
        col.className="col-sm-12 col-md-4 col-lg-3 p-2 card";

        var card = document.createElement('div');
        card.className = "p-2";

        var image = document.createElement('img');
        image.setAttribute("height","matchparent");
        image.setAttribute("width","100%");
        image.src=news.urlToImage;

        var cardBody = document.createElement('div');
        
        var newsHeading = document.createElement('h5');
        newsHeading.className = "card-title";
        newsHeading.innerHTML = news.headline;


        var description = document.createElement('p');
        description.className="text-muted";
        description.innerHTML = news.description;

        var link = document.createElement('a');
        link.className="btn btn-dark";
        link.setAttribute("target", "_blank");
        link.href = news.url;
        link.innerHTML="Read more";

        cardBody.appendChild(newsHeading);
        cardBody.appendChild(description);
        cardBody.appendChild(link);

        card.appendChild(image);
        card.appendChild(cardBody);

        col.appendChild(card);

        newsDetails.appendChild(col);
    });
}