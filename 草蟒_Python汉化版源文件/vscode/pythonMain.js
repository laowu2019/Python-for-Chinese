"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const vscode_1 = require("vscode");
function activate(_context) {
    vscode_1.languages.setLanguageConfiguration('python', {
        onEnterRules: [
            {
                beforeText: /^\s*(?:def|class|for|if|elif|else|while|try|with|finally|except|async|定义|类|取|如果|不然|否则|只要|尝试|用|最后|捕获|异步).*?:\s*$/,
                action: { indentAction: vscode_1.IndentAction.Indent }
            }
        ]
    });
}
exports.activate = activate;

//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/a622c65b2c713c890fcf4fbf07cf34049d5fe758/extensions\python\out/pythonMain.js.map
