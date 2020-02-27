let sendButton = document.querySelector('#send');

sendButton.onclick = function(){
    let http = new XMLHttpRequest();
    let url = 'http://127.0.0.1:5000/createlink';
    let params = JSON.stringify({url: document.getElementById('inputlink').value});
    http.open('POST', url, true);

    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/json');

    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            outtext = document.getElementById('outlink');

            outtext.setAttribute('value', 'http://127.0.0.1:5000/' + JSON.parse(http.responseText)['result']);
        }
    };
    http.send(params);
};

let copyButton = document.getElementById('copy');

copyButton.onclick = function() {
  let outlink = document.getElementById('outlink');
  outlink.select();
  document.execCommand('copy');
};
