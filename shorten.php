<?php

$long_url = $_POST['long_url'];
$short_code = substr(md5(uniqid(rand(), true)), 0, 6);

// Save the short code and long URL in a file
file_put_contents('urls.txt', $short_code . ':' . $long_url . PHP_EOL, FILE_APPEND);

$base_url = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? "https" : "http") . "://" . $_SERVER['HTTP_HOST'];
echo "Your short URL is: <a href='{$base_url}/{$short_code}'>{$base_url}/{$short_code}</a>";

?>