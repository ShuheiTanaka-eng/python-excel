# python-excel

<h2>PythonでExcelを操作</h2>
このリポジトリはPythonを使ったExcel操作の基本的なコードをアップロードしています。
<h2>各ファイルの説明</h2>
<h3>agelist.py</h3>
生まれ年と現在の年齢の一覧表を表示します。
for文の中の、age_cellでセルを選択して、そのセルに対して、.valueとすることで値（age変数i）をいれています。
同様の原理で、year_cellでセルを選択して、.valueでyearを指定して格納しています。
forを抜けたら、saveする。

<h3>cell_write.py</h3>
このコードでは様々なセルの指定の仕方があることを示しています。

<h3>hello_excel.py</h3>
同上

<h3>kuku_excel.py</h3>
forの二重ループを使って、九九の表を作成しています。

<h3>make_cellname100.py</h3>
セルの名前（A1とかC4とか）をセルに書き込むコードです。

<h3>read_excel.py</h3>
cellのvalueを取得して表示しています。

h3>read_range1.py</h3>
任意のセルの範囲をforの二重表記を使って表現して、その値を順にdata配列に格納して最後に表示しています。

<h3>read_range2.py</h3>
任意のセルの範囲を[]を使って表現しています。
valuesへの値の入れ方は少し特殊なのでこの書き方ごと暗記するといいでしょう。

<h3>read_range3.py</h3>
任意のセルの範囲を、イテレータを使って表現しています。
.iter_rowsとその後の、forの書き方は暗記しましょう。

<h3>renzoku.py</h3>
n行m列にnのn乗をを表記しています。

<h3>uriage_get.py</h3>
xlsxを読み込んでセルに任意の範囲の値を書き込んでいます。

