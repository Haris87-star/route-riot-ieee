const { spawn } = require('child_process');

const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless=new',
  '--remote-debugging-port=9228',
  '--disable-gpu',
  'file:///C:/Users/Harish/OneDrive/Desktop/IEEE/index.html'
]);

setTimeout(async () => {
  try {
    const list = await (await fetch('http://127.0.0.1:9228/json')).json();
    const page = list.find(x => x.type === 'page');
    
    const ws = new WebSocket(page.webSocketDebuggerUrl);
    ws.addEventListener('open', () => {
      ws.send(JSON.stringify({
        id: 1,
        method: 'Runtime.evaluate',
        params: {
          expression: 'JSON.stringify({ gridH: document.querySelector(".main-grid").offsetHeight, cols: Array.from(document.querySelectorAll(".column")).map(c => ({ h: c.offsetHeight, cardHs: Array.from(c.querySelectorAll(".poster-card")).map(k => ({ title: k.querySelector(".card-title").innerText.substring(0, 15), h: k.offsetHeight, flex: window.getComputedStyle(k).flex })) })) })',
          returnByValue: true
        }
      }));
    });
    ws.addEventListener('message', (e) => {
      console.log(JSON.parse(e.data).result.result.value);
      chrome.kill();
      process.exit(0);
    });
  } catch(err) {
    console.error(err);
    chrome.kill();
  }
}, 1500);
