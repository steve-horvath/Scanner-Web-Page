<html>
  <head>
  <body>
    <h1>Today's archived calls</h1>
	<a href="/today_no-refresh.php">NO REFRESH</a><p>
	<?php 
	$command = 'ls';
	exec($command, $out, $status);
	
	$command = escapeshellcmd('/var/www/html/recordings.py today 800 109 4');
	$output = shell_exec($command);
	echo $output;

	?>

  </body>
</html>
