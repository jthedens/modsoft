document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
        window.location.href = 'abstimmungen.html';
    } else {
        alert('Login fehlgeschlagen');
    }
});

async function loadAbstimmungen() {
    const response = await fetch('http://localhost:5000/api/abstimmungen');
    const abstimmungen = await response.json();

    const list = document.getElementById('abstimmungenList');
    list.innerHTML = abstimmungen.map(a => `
        <li>
            <a href="abstimmung.html?id=${a.abstimmungs_id}">${a.titel}</a>
        </li>
    `).join('');
}

if (window.location.pathname.endsWith('abstimmungen.html')) {
    loadAbstimmungen();
}

async function loadAbstimmung() {
    const urlParams = new URLSearchParams(window.location.search);
    const abstimmungsId = urlParams.get('id');

    const response = await fetch(`http://localhost:5000/api/abstimmungen/${abstimmungsId}`);
    const abstimmung = await response.json();

    document.getElementById('abstimmungDetails').innerText = abstimmung.beschreibung;
}

async function submitVote(option) {
    const urlParams = new URLSearchParams(window.location.search);
    const abstimmungsId = urlParams.get('id');

    const response = await fetch(`http://localhost:5000/api/vote`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ abstimmungs_id: abstimmungsId, wahloption: option }),
    });

    if (response.ok) {
        window.location.href = `ergebnisse.html?id=${abstimmungsId}`;
    } else {
        alert('Abstimmung fehlgeschlagen');
    }
}

if (window.location.pathname.endsWith('abstimmung.html')) {
    loadAbstimmung();
}

async function loadResults() {
    const urlParams = new URLSearchParams(window.location.search);
    const abstimmungsId = urlParams.get('id');

    const response = await fetch(`http://localhost:5000/api/results/${abstimmungsId}`);
    const results = await response.json();

    const list = document.getElementById('resultsList');
    list.innerHTML = Object.entries(results).map(([option, votes]) => `
        <li>${option}: ${votes} Stimmen</li>
    `).join('');
}

if (window.location.pathname.endsWith('ergebnisse.html')) {
    loadResults();
}
