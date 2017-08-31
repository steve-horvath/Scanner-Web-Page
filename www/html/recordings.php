<html>
  <head>
    <title>Today's Halton FD Calls</title>
    <meta http-equiv="refresh" content="5" >
  </head>
  <body>
    <h1>Today's archived calls</h1>
	<a href="/today_no-refresh.php">NO REFRESH</a><p>
	<?php 
	$command = escapeshellcmd('/var/www/html/recordings.py' . " " . $_GET["date"] . " " . $_GET["tgid"] . " " . $_GET["rid"] . " " . $_GET["len"]);
	$output = shell_exec($command);
	echo $output;

	?>

  </body>
</html>
