<?php
  $data = array();
  $data['EMAIL'] = $_GET['email'];

  // Add here the value of the input of type text with name like ="b_asdf123456789_1234567890c";
  $data['INPUT_TYPE_TEXT_NAME_VALUE'] = "";

  // Add here the form action url
  $url = 'MAILCHIMP_FORM_ACTION_URL';

  $params = array('http' => array('method' => 'POST', 'content' => http_build_query($data)));
  if (!is_null($headers)) {
    $params['http']['header'] = '';
    foreach ($headers as $k => $v) {
      $params['http']['header'] .= "$k: $v\n";
    }
  }
  $ctx = stream_context_create($params);
  $fp = @fopen($url, 'rb', false, $ctx);
  if ($fp) {
    echo @stream_get_contents($fp);
    die();
  } else {
    // Error
    throw new Exception("Error loading '$url', $php_errormsg");
  }

?>