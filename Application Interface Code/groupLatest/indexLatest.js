const faqs = document.querySelectorAll('.faq');
const questions = document.querySelectorAll('.question');
const submit = document.querySelectorAll('.submit');

questions.forEach(question => {
    question.addEventListener('click', () => {
        question.parentElement.classList.toggle('active');
    })
})

function displayHome() {
    document.getElementsByClassName('homePage')[0].classList.remove('hide-content');
    document.getElementsByClassName('sparqlPage')[0].classList.add('hide-content');
    document.getElementsByClassName('overlay')[0].classList.add('hide-content');
}

function displayQueries() {
    document.getElementsByClassName('sparqlPage')[0].classList.remove('hide-content');
    document.getElementsByClassName('homePage')[0].classList.add('hide-content');
    document.getElementsByClassName('overlay')[0].classList.add('hide-content');
}

function openPopup() {
    document.getElementsByClassName('overlay')[0].classList.remove('hide-content');
    document.getElementsByClassName('homePage')[0].classList.add('hide-content');
    document.getElementsByClassName('sparqlPage')[0].classList.add('hide-content');
    document.addEventListener('click', (e) => {
        var ele = e.target.parentElement.parentElement;
        console.log('This is event: ' + ele.classList);
        if (ele.classList.contains('answer')) {
            var text = ele.getElementsByTagName('p')[0].innerText;
            fetchData(text);
            document.getElementsByClassName('overlayText')[0].innerHTML = text;
        }
    })
}

function closeOverlay() {
    document.getElementsByClassName('sparqlPage')[0].classList.remove('hide-content');
    document.getElementsByClassName('homePage')[0].classList.add('hide-content');
    document.getElementsByClassName('overlay')[0].classList.add('hide-content');
}


let url = "http://172.17.16.159:5001/query/1";
let baseurl = "http://172.17.16.159:5001/query/";

submit.forEach(sub => {
    sub.addEventListener('click', () => {
        if (sub.classList.contains('sub1')) {
            url = baseurl + '1';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub2')) {
            url = baseurl + '2';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub3')) {
            url = baseurl + '3';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub4')) {
            url = baseurl + '4';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub5')) {
            url = baseurl + '5';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub6')) {
            url = baseurl + '6';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub7')) {
            url = baseurl + '7';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub8')) {
            url = baseurl + '8';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub9')) {
            url = baseurl + '9';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else if (sub.classList.contains('sub10')) {
            url = baseurl + '10';
            document.getElementsByClassName('overlayText')[0].innerHTML = "";
            getData();
        }
        else {
            console.log("Error");
        }
    })
})

function getData() {
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
        console.log('This is htmlString'+htmlString);
        document.getElementsByClassName('overlayText')[0].innerHTML = "";
        document.getElementsByClassName('overlayText')[0].insertAdjacentHTML('afterbegin', htmlString);
    })();
}
