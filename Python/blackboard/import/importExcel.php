<?php
error_reporting(E_ALL);

function excelToArray(){
    require_once dirname(__FILE__) . '/Classes/PHPExcel/IOFactory.php';

    $filename = dirname(__FILE__).'/../productList.xlsx';
    $objPHPExcelReader = PHPExcel_IOFactory::load($filename);

    $sheet = $objPHPExcelReader->getSheet(0);
    $highestRow = $sheet->getHighestRow();
    $highestColumn = $sheet->getHighestColumn();

//    $arr = array('A','B','C','D','E','F','G','H','I','J','K','L','M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z');
    $arr = ['C', 'D', 'E'];
    $res_arr = array();
    $sql = 'INSERT INTO bb_product (`name`,bar_code,left_num,borrow_num,total_num) Values ';

    for ($row = 3; $row <= 773; $row++) {
        $sql .= ' (';
        $row_arr = array();
//        for ($column = 0; $arr[$column] != 'F'; $column++) {
            $val1 = $sheet->getCellByColumnAndRow(2, $row)->getValue();
            $val2 = $sheet->getCellByColumnAndRow(3, $row)->getValue();
            $val3 = $sheet->getCellByColumnAndRow(4, $row)->getValue();
//            $row_arr[] = $val;
//        }

        $val1 = $val1 ? $val1 : '暂无';
        $val1 = iconv('UTF-8', 'GBK', $val1);

        $val2 = $val2 ? $val2 : '暂无';
        $val2 = iconv('UTF-8', 'GBK', $val2);


        $val3 = iconv('UTF-8', 'GBK', $val3);
        $val3 = $val3 ? $val3 : 1;
//        try {
            preg_match_all('/\d+/', $val3, $match);
            $val3 = $match[0][0];
//            if (!isset($match[0][0])) {
//                var_dump($row);
//            }
//        }catch (Exception $exception) {
//            var_dump($row);
//            exit();
//        }

        $sql .= "\"{$val2}\", \"{$val1}\", {$val3}, 0, {$val3}),";


//        var_dump(substr($val3, 0, -1));

//        var_dump(PHP_EOL);

        $res_arr[] = $row_arr;
    }


    $sql = substr($sql,0 ,-1);
    file_put_contents('insert.sql', $sql);

    return $res_arr;
}

excelToArray();