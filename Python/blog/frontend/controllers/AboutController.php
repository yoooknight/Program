<?php
/**
 * Created by PhpStorm.
 * User: WangSong
 * Date: 2017/3/1 0001
 * Time: 13:57
 */
namespace frontend\controllers;
use Yii;
use yii\base\InvalidParamException;
use yii\web\BadRequestHttpException;
use yii\web\Controller;
use yii\filters\VerbFilter;
use yii\filters\AccessControl;
use common\models\LoginForm;
use frontend\models\PasswordResetRequestForm;
use frontend\models\ResetPasswordForm;
use frontend\models\SignupForm;
use frontend\models\ContactForm;

/**
 * Class AboutController
 * @package frontend\controllers
 * @description 关于页面控制器
 *
 */
Class AboutController extends Controller
{
    public function actionIndex()
    {
        return $this->render('index');
    }
}