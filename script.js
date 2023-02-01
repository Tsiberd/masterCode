function replace(){
  var myLoc = window.prompt('Please enter a web site address', 'http://');
getHttp =   myLoc.substring(0, 7);
 
if ( getHttp == "http://")
{
finalUrl = myLoc;
} else {
finalUrl = 'http://' + myLoc;
}
 
window.location = 'view-source:' + finalUrl;
};

function urls(){
 var los = ["http://w3.org/WAI/WCAG21/understanding/resize-test",
 "http://w3.org/WAI/WCAG21/Understanding/images-of-text",
 "http://w3.org/WAI/WCAG21/Understanding/visual-presentation",
 "http://w3.org/WAI/WCAG21/Understanding/images-of-text-no-exception"]

for (let i=0; i<los.length; i++){
 window.open(los[i])}
};
function urls1(){
  var los = ["http://w3.org/WAI/WCAG21/Tequiques/general/G4.html",
  "http://w3.org/WAI/WCAG21/Tequiques/general/G4.html"]
  
 for (let i=0; i<los.length; i++){
  window.open(los[i])}
};


function urls2(){
  var los = ["http://w3.org/WAI/WCAG21/Techniques/general/G57.html",
  "http://w3.org/WAI/WCAG21/Techniques/general/G14.html",
  "http://w3.org/WAI/WCAG21/Techniques/general/G17.html",
  "http://w3.org/WAI/WCAG21/Techniques/css/C22.html",
  "http://w3.org/WAI/WCAG21/Techniques/css/C32.html",
  "http://w3.org/WAI/WCAG21/Techniques/general/G195.html",
  "http://w3.org/WAI/WCAG21/Techniques/css/C8.html",
  "http://w3.org/WAI/WCAG21/Techniques/css/C39.html",
  "http://w3.org/WAI/WCAG21/Techniques/general/G213.html",
  "http://w3.org/WAI/WCAG21/Techniques/css/C15.html"
]
  
 for (let i=0; i<los.length; i++){
  window.open(los[i])}
};


function urls3(){
  var los = ["http://w3.org/WAI/WCAG21/Techniques/html/H91.html",
  "http://w3.org/WAI/WCAG21/Techniques/General/G91.html"
]
  
 for (let i=0; i<los.length; i++){
  window.open(los[i])}
};


function refresh(){
  setTimeout(function(){
    location.replace("http://localhost/codeMcs/index.html")
  },100);
};








