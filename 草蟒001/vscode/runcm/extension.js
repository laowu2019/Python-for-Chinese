// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');
const entryPoint = vscode.workspace.getConfiguration('运行草蟒程序').get('entryPath');
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	//console.log('Congratulations, your extension "run-caomang" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json
	
	let disposable = vscode.commands.registerCommand('extension.runcm', () => {
		// The code you place here will be executed every time your command is executed

		// Display a message box to the user
		//vscode.window.showInformationMessage('Hello World!');

		//vscode.window.showInformationMessage(entryPoint)
		//vscode.window.showInformationMessage(vscode.WorkspaceConfiguration.get<string>("code-runner.customCommand"))
		//var fn = editor.document.fullFileName;
		//console.log(vscode.WorkspaceConfiguration.get<string>("entryPath"));
		//vscode.window.activeTerminal.sendText('python e:\\草蟒工作室\\运行草蟒程序.py ' + vscode.window.activeTextEditor.document.fileName)
		vscode.window.activeTerminal.sendText('python ' + entryPoint + ' ' + vscode.window.activeTextEditor.document.fileName)
		//vscode.commands.executeCommand('')
	});

	context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
function deactivate() {}

module.exports = {
	activate,
	deactivate
}
