#!/bin/paython3

import argparse
from pathlib import Path

class pftool:
    """PFTool
    コマンドラインから各種便利なCUIベースのツール郡です。
    これはそのランチャーとしての役割を持ちます。
    
    """

    def __init__(self, args=None):
        """コンストラクタ
        
        Keyword Arguments:
            args {ArgumentParser} -- コマンドラインパラメータ用のパーサ (default: {None})
        """
        # バージョン情報とか
        self.name = "PFTool"
        self.version = "0.01"
        self.about = ""

        # パラメータ用パーサ
        self.argparser = argparse.ArgumentParser(
            prog=Path(__file__).name,
            usage="コマンドラインから各種便利なCUIベースのツール郡です。\nこれはそのランチャーとしての役割を持ちます。",
            description="test",
            epilog='end',
            add_help=True,
        )
        # TODO:descriptionの詳細な実装を


    def get_version(self):
        """バージョン情報表示
        """
        dict = {
            "name":self.name,
            "version":self.version,
            "about":self.about
        }
        return "{0[name]} {0[version]}\n{0[about]}".format(dict)

    def get_help(self):
        """ヘルプ情報取得
        """
        # TODO: ヘルプ実装
        return "help"

    def get_modules(self):
        """利用可能モジュール取得
        """
        # TODO: モジュール一覧実装
        return "get_modules"
        
# メイン起動
if __name__ == '__main__':

    """
    obj = pftool()
    print(obj.get_version())

    print(Path(__file__).name)
    """

    obj = pftool()
    args = obj.argparser.parse_args()


