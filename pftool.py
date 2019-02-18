#!/bin/paython3

import argparse

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
        self.name = "PFTool"
        self.version = "0.01"
        self.about = ""
        print("init")
    
    def get_version(self):
        """バージョン表示
        """
        dict = {
            "name":self.name,
            "version":self.version,
            "about":self.about
        }
        return "{0[name]} {0[version]}\n{0[about]}".format(dict)
        

# メイン起動
if __name__ == '__main__':

    obj = pftool()
    print(obj.get_version())

