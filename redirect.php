<?php

$short_code = $_GET['short_code'];

$long_url = false;
$urls = explode(PHP_EOL, file_get_contents('urls.txt'));
foreach ($urls as $url) {
  $url_data = explode(':', $url);
  if ($url_data[0] === $short_code) {
    $long_url = $url_data[1];
    break;
  }
}

if ($long_url) {
  header("HTTP/1.1 301 Moved Permanently");
  header("Location: " . $long_url);
} else {
  header("HTTP/1.1 404 Not Found");
  echo "Short URL not found.";
}

?>