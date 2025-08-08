# Thoth

このリポジトリには、Python プログラミング学習用のチュートリアルが含まれています。

## Python と VS Code のセットアップ

1. **Python 3.10.10 Windows embeddable package (64-bit)** を公式サイトから [ダウンロード](https://www.python.org/ftp/python/3.10.10/python-3.10.10-embed-amd64.zip) します
2. このリポジトリのルート（`README.md` と同じ階層）に `bin` フォルダを作成します。
3. ダウンロードした `python-3.10.10-embed-amd64.zip` を `bin` フォルダに展開します。
4. **Visual Studio Code の ZIP（ポータブル）版** を以下から [ダウンロード](https://code.visualstudio.com/download) します：  
5. ダウンロードした `VSCode-win32-x64-<version>.zip` を `bin` フォルダに展開します。
6. `setup.bat` を実行して環境を初期化します（ローカル設定を作成／更新します）。

## 起動方法

1. `launch_vscode.bat` を実行します。

このスクリプトは、`bin` フォルダ内で最も新しい `VSCode-win32-x64-<version>` を自動的に検出して起動します。
