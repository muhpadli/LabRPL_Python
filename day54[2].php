<?php
/* ada seorang nasabah bank yang menabung di Bank X dengan saldo awal Rp. 1.000.000,-.
Bank X menerapkan kebijakan  bunga 3% perbulan dari saldo awal tabungan. hitunglah jumlah saldo akhir 
nasabah tersebut setelah 11 bulan.*/

$saldo_awal = 1000000;
$bunga = 0.03;
$banyak_bulan = 11;
$saldo_akhir = $saldo_awal + ($saldo_awal * $bunga * $banyak_bulan);

echo "Saldo akhir setelah $banyak_bulan bulan adalah : Rp. $saldo_akhir";
