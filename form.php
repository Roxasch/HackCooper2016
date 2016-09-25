<?php

//initially
$comment = null;

//if the form is submitted
if($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($_POST['preview-form-comment'])) {
	$comment = $_POST['preview-form-comment'];
}

?>

<!DOCTYPE html>
<html>
	<head>
		<title>CodeMirror - Form</title>
		<link rel="stylesheet" type="text/css" href="plugin/codemirror/lib/codemirror.css">
	</head>
	<body>
		<form id="preview-form" method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
			<textarea class="codemirror-textarea" name="preview-form-comment" id="preview-form-comment"><?php echo $comment; ?></textarea>
			<br>
			<input type="submit" name="preview-form-submit" id="preview-form-submit" value="Submit">
		</form>
		<div id="preview-comment"><?php echo $comment; ?></div>

		<!-- javascript -->
		<script type="text/javascript" src="js/jquery.min.js"></script>
		<script type="text/javascript" src="plugin/codemirror/lib/codemirror.js"></script>
		<script type="text/javascript" src="js/default.js"></script>
	</body>
</html>