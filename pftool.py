#!/bin/paython3

import argparse

class pftool(object):
    """PFTool
    コマンドラインから各種便利なCUIベースのツール郡です。
    これはそのランチャーとしての役割を持ちます。
    
    Arguments:
        object {object} -- 規定クラス
    """

    name = "PFTool"
    version = "0.01"
    about = ""

    def __init__(self, args=None):
        """コンストラクタ
        
        Keyword Arguments:
            args {ArgumentParser} -- コマンドラインパラメータ用のパーサ (default: {None})
        """
        print("init!")

    def version(self):
        dic = {
            "name":self.name,
            "version":self.version,
            "about":self.about
        }
        print("{name} {version}\n{about}".format(dic))

# メイン起動
if __name__ == '__main__':



    obj = pftool()
    obj.version()
