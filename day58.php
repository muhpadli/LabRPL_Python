<?php
//belajar array pada php

$buah = array('pisang', 'jambu', 'mangga', 'pepaya', 'semangka');

//mengakses array dengan looping for()
for ($i = 0; $i < 3; $i++) {
    echo "\n$buah[$i]";
}

//mengakses array dengan looping while()
$j = 0;
while ($j <= 4) {
    echo "\n$buah[$j]";
    $j++;
}
