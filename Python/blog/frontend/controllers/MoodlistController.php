<?php
/**
 * Created by PhpStorm.
 * User: WangSong
 * Date: 2017/3/1 0001
 * Time: 14:44
 */

namespace frontend\controllers;

use yii;
use yii\web\Controller;

Class MoodlistController extends Controller
{
    public function actionIndex()
    {
        return $this->render("index");
    }
}