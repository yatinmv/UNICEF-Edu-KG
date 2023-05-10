import fetch from "node-fetch";

let url = "http://192.168.0.17:5001/query/1";

let options = {
  method: "GET",
  headers: { Accept: "application/json" },
};

const createHtmlTablefromData = (data) => {
  let htmlString = ``;

  if (data.length < 0) throw new Error("No data found");

  const tableHeads = Object.keys(data[0]);

  const tableRows = [];
  for (const obj of data) {
    const objValues = Object.values(obj);
    tableRows.push(objValues);
  }

  htmlString += `<table><tr>`;
  for (let i = 0; i < tableHeads.length; i++) {
    htmlString += `<th>${tableHeads[i]}</th>`;
  }
  htmlString += `</tr>`;
  for (let i = 0; i < tableRows.length; i++) {
    htmlString += `<tr>`;
    for (let j = 0; j < tableRows[i].length; j++) {
      htmlString += `<td>${tableRows[i][j]}</td>`;
    }
    htmlString += `</tr>`;
  }
  htmlString += `</table>`;
  return htmlString;
};

(async () => {
  let response = await fetch(url, options);
  let data = await response.json();
    let htmlString = createHtmlTablefromData(data);
    console.log(htmlString);
    
})();
