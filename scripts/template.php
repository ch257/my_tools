<?php
$script_file_folder = __DIR__ . '\\';
echo $script_file_folder;


require_once($script_file_folder . 'modules\\php\\Template.php');

$template = new Template;
if ($template->main(null)) {
	print("\nOK\n");
} else {
	print("\nError\n");
}
