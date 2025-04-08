async function runWasm() {
  try {
    const response = await fetch('output.wasm');
    const buffer = await response.arrayBuffer();
    const module = await WebAssembly.instantiate(buffer);
    const instance = module.instance;
    const result = instance.exports._start();
    document.getElementById('main').textContent = result;
  } catch (err) {
    console.error('Error:', err);
  }
}

runWasm();
