const serverUrl = "http://localhost:5000/s";

export default async function getToxicityFromUrl(url) {
  if (getIdFromUrl(url)) {
    const urlParams = new URLSearchParams({
      yt_code: getIdFromUrl(url),
    });

    const response = await fetch(`${serverUrl}?${urlParams.toString()}`);

    return await response.json()
  }
}

