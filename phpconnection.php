<?php
$serverName = "SABARMATI\SQLEXPRESS";
$connectionOptions = array(
    "Database" => "sreyas_prod",
    "Uid" => "sa",
    "PWD" => "sadguru"
);

$conn = sqlsrv_connect($serverName, $connectionOptions);

if (!$conn) {
    die("Connection failed: " . sqlsrv_errors());
}

echo "Connected successfully!";

sqlsrv_close($conn);
?>
