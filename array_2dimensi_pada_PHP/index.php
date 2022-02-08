<?php

//belajar array 2 dimensi
$negara_id = array(
    array('Indonesia', 'Bahasa Indonesia', 'rupiah'),
    array('Malaysia', 'Melayu', 'Ringgit'),
    array('Thailand', 'Thai', 'Bath Thailand')
);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>array php</title>
</head>

<body>
    <?php
    //menampilkan array 2 dimensi
    echo "menampilkan array 2 dimensi <br>";
    echo '| ' . $negara_id[0][0] . ' => ' . $negara_id[0][1] . ' => ' . $negara_id[0][2] . ' | <br>';
    echo '| ' . $negara_id[1][0] . ' => ' . $negara_id[1][1] . ' => ' . $negara_id[1][2] . ' | <br>';
    echo '| ' . $negara_id[2][0] . ' => ' . $negara_id[2][1] . ' => ' . $negara_id[2][2] . ' | <br>';
    echo '<br>';

    echo "menampilkan array 2 dimensi dengan looping <br>";
    for ($baris = 0; $baris < 3; $baris++) {
        for ($kolom = 0; $kolom < 3; $kolom++) {
            echo ' | ' . $negara_id[$baris][$kolom];
        }
        echo ' | <br>';
    }
    ?>

</body>

</html>