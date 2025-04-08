# Running the Generated WAT Code in the Browser

Assuming the Delta compiler generates correct WAT code, call the `realize` method with the `Phase.CODE_GENERATION` argument. For example:

```python
from delta import Compiler, Phase

source_code = '42'
c = Compiler('program')
c.realize(source_code, Phase.CODE_GENERATION)
```

Running the preceding code creates an `output.wat` file within the `web` folder. To execute this file in a browser, we first need to translate it into a WASM binary file. This can be done by following these steps:

- Copy the entire contents of the `web/ouput.wat` file and paste them into the WAT pane on the [wat2wasm demo](https://webassembly.github.io/wabt/demo/wat2wasm/) page. Ensure you remove any existing content in the pane beforehand.
- Click the `Download` button and save the resulting file as `output.wasm` inside the `web` folder.

Now, we can execute the WASM code within a browser. At the terminal, navigate to the `web` folder and run the following command to start a simple web server:

    python -m http.server

Open a web browser (Google Chrome is recommended due to its fine WebAssembly debugging tools) and enter the following in the address bar:

    localhost:8000

The numeric result of the execution should then be displayed as part of the `index.html` web page.

You can open the developer tools on Chrome (`Ctrl+Shift+I` on Windows and Linux, or `Option-Command-I` on macOS) to utilize the debugger. Navigate to the `Sources` tab and locate the WebAssembly code under the `wasm` node. You can then place a code breakpoint and reload the page to start single-stepping through the WASM code.
