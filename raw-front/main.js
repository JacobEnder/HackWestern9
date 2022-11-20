const main = (event) => {
  const url = undefined;
  console.log("hello world")

  chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    console.log(url)
    // use `url` here inside the callback because it's asynchronous!

    getToxicityFromUrl(url)
      .then((data) => {
        console.log(data);
      }
    );
  });
}

window.onload = main