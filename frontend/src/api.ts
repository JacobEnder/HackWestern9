const serverUrl = 'http://localhost:3001';

function getIdFromUrl(url: string) {
  const regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
  const match = url.match(regExp);
  return match && match[7].length == 11 ? match[7] : "";
}

export async function getToxicityFromUrl(url: string) {
  if (getIdFromUrl(url)) {
    const urlParams = new URLSearchParams({
      yt_code: getIdFromUrl(url),
    });

    const response = await fetch(`${serverUrl}?${urlParams.toString()}`)
    return await response.json()
  }
}
