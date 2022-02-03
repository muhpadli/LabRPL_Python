<?php

$nama = "RUDIANTO";

//mengecek apakah variabel $nama bertipe string atau bukan
//jika $nama bernilai string,  maka akan tampil '$nama bertipe string'
//jika bukan, maka akan tampil '@nama bukan tipe string

if (is_string($nama)) {
    echo "$nama bertipe string";
} else {
    echo "$nama buka tipe string";
}
