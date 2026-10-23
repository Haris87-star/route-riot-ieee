const { spawn } = require('child_process');

const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless=new',
  '--remote-debugging-port=9225',
  '--disable-gpu',
  'file:///C:/Users/Harish/OneDrive/Desktop/IEEE/index.html'
]);

setTimeout(async () => {
  try {
    const list = await (await fetch('http://127.0.0.1:9225/json')).json();
    const ws = new WebSocket(list[0].webSocketDebuggerUrl);
    ws.addEventListener('open', () => {
      ws.send(JSON.stringify({
        id: 1,
        method: 'Runtime.evaluate',
        params: {
          expression: 'JSON.stringify({ gridH: document.querySelector(".main-grid").offsetHeight, colH: document.querySelector(".column").offsetHeight, cardHs: Array.from(document.querySelectorAll(".poster-card")).map(c => ({ title: c.querySelector(".card-title") ? c.querySelector(".card-title").innerText : "unknown", h: c.offsetHeight, flex: window.getComputedStyle(c).flex })) })',
          returnByValue: true
        }
      }));
    });
    ws.addEventListener('message', (e) => {
      console.log(e.data);
      chrome.kill();
      process.exit(0);
    });
  } catch(err) {
    console.error(err);
    chrome.kill();
  }
}, 1500);
