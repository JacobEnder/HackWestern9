const serverUrl = "http://localhost:5000/s";

function getIdFromUrl(url) {
  const regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
  const match = url.match(regExp);
  return match && match[7].length == 11 ? match[7] : "";
}

function reqListener() {
  console.log(this.responseText);
}



chrome.tabs.onUpdated.addListener(async function (tabId, changeInfo, tab) {

  // const url = tab.url;
  // const urlParams = new URLSearchParams({
  //   yt_code: getIdFromUrl(url),
  // });
  // // const response = await fetch(`${serverUrl}?${urlParams.toString()}`, {});
  // // console.log(response);
  // const req = new XMLHttpRequest();
  // req.addEventListener("load", reqListener);
  // req.open("GET", "http://www.example.org/example.txt");
  // req.send();
  
  console.log("Executing in a separate script");
  chrome.tabs.executeScript(null, {file: "apiCall.js"});

  if (changeInfo.status == "complete") {
    // Pass data from to the contentScript
    if (tab.url && tab.url.includes("youtube")) {
      chrome.tabs.sendMessage(tabId, {
        value: tab.url
      });
    }
    // console.log(tab.url);
  }
});
