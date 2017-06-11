# Description of homework 2
行列積を求めるプログラムを書いて、行列のサイズNと実行時間関係を調べてみよう  
- 仕様：
- プログラムの入力はサイズN
- N×Nの列AとBを用意する(行列の中身は適当でOK)
- C=ABを計算する(この部分の実行時間を測定する)
- Nと実行時間の関係をグラフにする（計算量との関係は？）

Write code to calculate C = A * B, where A, B and C are matrices of size N * N.
Measure the execution time of your code for various Ns, and plot the relationship between N and the execution time.

***
The two java programs using different algorithms both compute __matrix__ __multiplication__.  
  [MatrixNaive.java](https://github.com/LingyingWu/STEP2017/blob/master/week2/MatrixNaive.java) uses the naive algorithm, 
whose time complexity is O(n^3).  
[MatrixStrassen.java](https://github.com/LingyingWu/STEP2017/blob/master/week2/MatrixStrassen.java) implements the Strassen algorithm,
which has a time complexity of around O(n^2.807).
