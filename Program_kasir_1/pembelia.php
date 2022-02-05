<?php
$jumlah_tas = $_POST["jtas"];
$jumlah_baju = $_POST["jbaju"];
$jumlah_sepatu = $_POST["jsepatu"];

define('HARGA_TAS', 55000);
define('HARGA_BAJU', 50000);
define('HARGA_SEPATU', 150000);

$hrg_ttltas = $jumlah_tas * HARGA_TAS;
$hrg_ttlbaju = $jumlah_tas * HARGA_BAJU;
$hrg_ttlsepatu = $jumlah_tas * HARGA_SEPATU;
$total = $hrg_ttltas + $hrg_ttlbaju + $hrg_ttlsepatu;

if ($total < 500000) {
    $diskon = 0;
} else {
    $diskon = 0.15;
}
$total_bayar = $total - ($total * $diskon);

?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Program kasir</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>

<body>
    <?php
    echo '<div class="container-fluid pt-5 pb-5">';
    echo '<div class="container text-center">';
    echo '<h3 class="mb-5">Struk Pembayaran</h3>';
    echo '<div class=" row col-md-4">';

    echo '<table class="table mb-5">';
    echo '<thead>';
    echo '<tr>';
    echo '<th scope="col">No</th>';
    echo '<th scope="col">Barang</th>';
    echo '<th scope="col">Harga</th>';
    echo '<th scope="col">Jumlah</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';
    echo '<tr>';
    echo '<th scope="row">1</th>';
    echo '<td>Tas</td>';
    echo '<td>55.000</td>';
    echo '<td>' . $jumlah_tas . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<th scope="row">2</th>';
    echo '<td>Baju</td>';
    echo '<td>50.000</td>';
    echo '<td>' . $jumlah_baju . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<th scope="row">3</th>';
    echo '<td>sepatu</td>';
    echo '<td>150.000</td>';
    echo '<td>' . $jumlah_sepatu . '</td>';
    echo '</tr>';
    echo '</tbody>';
    echo '</table>';
    echo "<p><b>TOTAL HARGA : Rp. $total </b><br>";
    echo "<b>Diskon: Rp. $diskon </b><br>";
    echo "<b>Total Bayar: Rp. $total_bayar </b></p>";

    echo '</div>';
    echo '</div>';
    echo '</div>';
    ?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
    </script>
</body>

</html>