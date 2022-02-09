<?php

//array 3 dimensi pada php 

$barang = array(
    array(
        array('Tas', 5, 65000),
        array('sepatu', 3, 135000),
        array('buku', 12, 3000)
    ),
    array(
        array('masker', 12, 22000),
        array('Hand Sanitizer', 6, 15000),
        array('Baygon', 4, 40000)
    ),
    array(
        array('songkok', 3, 50000),
        array('sarung', 5, 65000),
        array('sajadah', 3, 65000)
    )
);
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>belajar array</title>
</head>

<body>

    <?php

    echo "array  dimensi pada php<br>";
    //mengakses array 3 dimensi dengan forloopoing

    for ($daftar_barang = 0; $daftar_barang < 3; $daftar_barang++) {
        echo "<< Daftar Barang $daftar_barang. >><br>";
        for ($baris = 0; $baris < 3; $baris++) {
            for ($kolom = 0; $kolom < 3; $kolom++) {
                echo ' | ' . $barang[$daftar_barang][$baris][$kolom];
            }
            echo " |<br>";
        }
        echo '<br>';
    }
    ?>

</body>

</html>