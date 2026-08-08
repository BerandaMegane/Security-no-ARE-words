Residential Proxy
=====================================================
.. glossary::
  Residential Proxy : R

.. glossary::
  RESIP : R

.. glossary::
  レジデンシャルプロキシー : れ

.. glossary::
  おまえんち踏み台サービス : お

* 住宅用ネットワーク（Residential）のホストを利用したトラフィックの中継を行うプロキシーサービスの一種
* 自宅にあるようなコンピュータ上でプロキシーサーバー（プロキシーウェア）が動作しており、見ず知らずの人のコンピュータを中継点として利用できる
* 家庭や個人で利用している IP アドレスで接続元を隠蔽できるため、サイバー犯罪を支えるサービスとしても普及が進むと推測されている

  * ただ、名前が `Residential Proxy` や `住宅用プロキシー` だと、危険性が一般人には伝わりにくいため、辻氏は「おまえんち踏み台サービス」と呼ぶことを提唱している

* 利用例

  * GeoIP など IP アドレスをもとに `おま国 <https://dic.nicovideo.jp/a/%E3%81%8A%E3%81%BE%E5%9B%BD>`_ されているようなコンテンツにアクセスするとき

    * Netflix などの動画視聴サービスにおいて、日本国内からは視聴できないジブリ作品を視聴したいときに利用できるとされる
  
  * サイバー犯罪者っぽい人が、アクセス元を偽装するとき

    * IP アドレスに紐づく地理情報 (GeoIP 的情報) 上では、家庭からアクセスしているように偽装できるとされる

.. tip:: 
  * 根岸氏が `S3#143`_ および `S3#215`_ で取り上げている

    * `S3#143 11:27~ <https://listen.style/p/sec_are/0decerns?t=687.3>`_
    * `S3#215 42:04~ <https://listen.style/p/sec_are/0dgjxceo?t=2524.02>`_

  * プロキシーサーバーの増やし方

    * 「自宅で余っている回線帯域を有効活用しませんか？」といった宣伝文句で参加者を募集し、回線提供に対してペイが発生するパターン
    * プロキシーウェアが組み込まれたソフトウェアを知らずにインストールしてしまうパターン（利用規約にちょろっと書いてある）
    * 攻撃されて実行してしまうパターン

.. tip::
  辻氏が `S3#310`_ で「おまえんち踏み台サービス」と呼ぶことを提唱している (`S3#310 16:27~ <https://listen.style/p/sec_are/jy4hvbsj?t=987.02>`_)

  経緯

  * 根岸氏と piyokango 氏が `S3#309`_ で `Residential Proxy` について取り上げたことがきっかけ (辻氏はお休みの回)
    
    * 危機感が一般人には伝わりにくいので「良い名前をつけてくれないかな」と話題にする
    * 例として「犯罪用プロキシー」という直球ネーミングも提案される
  
  * 辻氏によると、「一般人でも、自分ごととして捉えてもらえること」がポイントとのこと
  
    * `お前んちって言われたら、俺かってなるじゃないですか。` とのこと
    * 最初は「ひとんち踏み台サービス」も候補にあったが、自分ごととして考えてほしかったとのこと
  
  * `一応、母さん助けて詐欺よりはいいネーミングなんちゃうかなと思ってるんですよ。` とのこと
  
    * 「母さん助けて詐欺」とは、もともと「オレオレ詐欺」「振り込め詐欺」と呼ばれた手口について、警視庁が2013年に公募で採用した愛称のこと
    * しかし「母さん助けて」以外にも様々な手口があるため実態にそぐわないことなども背景にあったのか、実際に使用されることは少なく、現在は総称として「特殊詐欺」が定着している
    * ちなみに、このまとめを作成している著者は「母さん助けて詐欺」を聞いたこともなかった

.. rubric:: 関連リンク

* `Unveiling the depths of Residential Proxies providers - Sekoia.io Blog <https://blog.sekoia.io/unveiling-the-depths-of-residential-proxies-providers/>`_
* `Residential IP Proxy サービスに悪用される住宅用ホストの調査 <https://www.kikn.fms.meiji.ac.jp/paper/2020/master/hanzawa/CSS_2019_hanzawa.pdf>`_
* `SOMPO CYBER SECURITY 用語集 <https://www.sompocybersecurity.com/column/glossary/residential-proxy>`_
* `特殊詐欺 - Wikipedia <https://ja.wikipedia.org/wiki/%E7%89%B9%E6%AE%8A%E8%A9%90%E6%AC%BA>`_
* `警察庁 特殊詐欺対策ページ <https://www.npa.go.jp/bureau/safetylife/sos47/>`_

.. rubric:: 関連放送回

* `第143回 勝手に中継点！新たなバラマキと止まったランサム！スペシャル`_
* `第215回 いわば！まさに！もはや！むしろ！スペシャル！`_
* `第310回 おまえんち踏み台サービスで！スペシャル！`_
* `第309回 これはボクも聴くのが楽しみだ！スペシャル！`_

.. _第143回 勝手に中継点！新たなバラマキと止まったランサム！スペシャル: https://www.tsujileaks.com/?p=1265
.. _S3#143: https://www.tsujileaks.com/?p=1265
.. _第215回 いわば！まさに！もはや！むしろ！スペシャル！: https://www.tsujileaks.com/?p=1727
.. _S3#215: https://www.tsujileaks.com/?p=1727
.. _第310回 おまえんち踏み台サービスで！スペシャル！: https://www.tsujileaks.com/?p=2331
.. _S3#310: https://www.tsujileaks.com/?p=2331
.. _第309回 これはボクも聴くのが楽しみだ！スペシャル！: https://www.tsujileaks.com/?p=2323
.. _S3#309: https://www.tsujileaks.com/?p=2323
