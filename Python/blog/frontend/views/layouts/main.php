<?php

/* @var $this \yii\web\View */
/* @var $content string */

use yii\helpers\Html;
use yii\helpers\Url;

use yii\bootstrap\Nav;
use yii\bootstrap\NavBar;
use yii\widgets\Breadcrumbs;
use frontend\assets\AppAsset;
use common\widgets\Alert;
AppAsset::register($this);

$about_url = Url::to(['about/index']);
$site_url = Url::to(['site/index']);
$newlist_url = Url::to(['newlist/index']);
$share_url = Url::to(['share/index']);
$moodlist_url = Url::to(['moodlist/index']);
$knowledge_url = Url::to(['knowledge/index']);
?>

<?php $this->beginPage() ?>
<!DOCTYPE html>
<html lang="<?= Yii::$app->language ?>">
<head>
    <meta charset="<?= Yii::$app->charset ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?= Html::csrfMetaTags() ?>
    <title><?= Html::encode($this->title) ?></title>
    <?php $this->head() ?>
    <header>
        <div id="logo"><a href="<?php echo $site_url?>"></a></div>
        <nav class="topnav" id="topnav">
            <a href="<?php echo $site_url?>"><span>首页</span><span class="en">Protal</span></a>
            <a href="<?php echo $newlist_url?>"><span>慢生活</span><span class="en">Life</span></a>
            <a href="<?php echo $moodlist_url?>"><span>碎言碎语</span><span class="en">Doing</span></a>
            <a href="<?php echo $share_url?>"><span>模板分享</span><span class="en">Share</span></a>
            <a href="<?php echo $knowledge_url?>"><span>学无止境</span><span class="en">Learn</span></a>
            <a href="<?php echo $about_url?>"><span>关于我</span><span class="en">About</span></a>
        </nav>
    </header>
</head>
<body>
<?php $this->beginBody() ?>

<div class="wrap">
    <div class="container">
        <?= Breadcrumbs::widget([
            'links' => isset($this->params['breadcrumbs']) ? $this->params['breadcrumbs'] : [],
        ]) ?>
        <?= Alert::widget() ?>
        <?= $content ?>
    </div>
</div>

<footer class="footer">
    <div class="container">
        <p class="pull-left">&copy; My Company <?= date('Y') ?></p>

        <p class="pull-right"><?= Yii::powered() ?></p>
    </div>
</footer>

<?php $this->endBody() ?>
</body>
</html>
<?php $this->endPage() ?>
