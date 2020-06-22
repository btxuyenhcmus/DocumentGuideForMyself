# Django
## Create a debugger launch profile #
You're probably already wondering if there's an easier way to run the server and test the app without typing `python manage.py runserver` each time. Fortunately, there is! You can create a customized launch profile in VS Code, which is also used for the inevitable exercise of debugging.

1. Switch to **Run** view in VS Code (using the left-side activity bar). Along the top of the Run view, you may see "No Configurations" and a warning dot on the gear icon. Both indicators mean that you don't yet have a `launch.json` file containing debug configurations:
![vscode-debugger](./src/static/vscode-debugger.png)

2. Select the gear icon and wait for a few seconds for VS Code to create and open a `launch.json` file. (If you're using an older version of VS Code, you may be prompted with a list of debugger targets, in which case select **Python** from the list.) The `launch.json` file contains a number of debugging configurations, each of which is a separate JSON object within the `configuration` array.

3. Scroll down to and examine the configuration with the name "Python: Django":
    ```
    {
        "name": "Python: Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/manage.py",
        "console": "integratedTerminal",
        "args": [
            "runserver",
        ],
        "django": true
    },
    ```
    This configuration tells VS Code to run `"${workspaceFolder}/manage.py"` using the selected Python interpreter and the arguments in the `args` list. Launching the VS Code debugger with this configuration, then, is the same as running `python manage.py runserver` in the VS Code Terminal with your activated virtual environment. (You can add a port number like `"5000"` to `args` if desired.) The `"django": true` entry also tells VS Code to enable debugging of Django page templates, which you see later in this tutorial.

4. Save `launch.json` *(Ctrl+S)*. In the debug configuration drop-down list (which reads **Python: Current File**) select the **Python: Django** configuration:

    ![vscode-debugger-select](./src/static/vscode-debugger-select.png)

5. Test the configuration by selecting the **Run > Start Debugging** menu command, or selecting the green **Start Debugging** arrow next to the list (*F5*):

    ![vscode-run](./src/static/vscode-run.png)

6. **Ctrl+click** the `http://127.0.0.1:8000/` URL in the terminal output window to open the browser and see that the app is running properly.

7. Close the browser and stop the debugger when you're finished. To stop the debugger, use the Stop toolbar button (the red square) or the **Run > Stop Debugging** command (*Shift+F5*).

8. You can now use the **Run > Start Debugging** at any time to test the app, which also has the benefit of automatically saving all modified files.