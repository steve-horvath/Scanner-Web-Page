<html>
  <head>
    <title>Today's Halton FD Calls</title>
    <meta http-equiv="refresh" content="5" >
  </head>
  <body>
    <h1>Live feeds</h1>
    <a href="http://192.168.1.18:5700">LOCAL</a>
    <a href="http://stevehorvath.ddns.net:5700">REMOTE</a>
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
