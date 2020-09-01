<?php
$password = "marlaspassword";
$enc_line = md5(crypt($password, 'fa'));
echo $enc_line . "\r\n";
echo date("Y-m-d_H:i:s") . "\r\n";
?>
