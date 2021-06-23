<?php
use yii\helpers\Url;
/* @var $this yii\web\View */
$this->title = "YoooKnight's Blog";
$index_url = Url::to(["site/index"]);
$local_url = Url::to(["moodlist/index"]);
?>

<link href="css/mood.css" rel="stylesheet">

<div class="moodlist">
    <h1 class="t_nav"><span>删删写写，回回忆忆，虽无法行云流水，却也可碎言碎语。</span><a href="<?php echo $index_url?>" class="n1">网站首页</a><a href="<?php echo $local_url?>" class="n2">碎言碎语</a></h1>
    <div class="bloglist">
        <ul class="arrow_box">
            <div class="sy">
                <img src="images/001.png">
                <p> 我希望我的爱情是这样的，相濡以沫，举案齐眉，平淡如水。</p>
            </div>
            <span class="dateview">2014-1-1</span>
        </ul>
        <ul class="arrow_box">
            <div class="sy">
                <p> 我希望我的爱情是这样的，相濡以沫，举案齐眉，平淡如水。我在岁月中找到他，依靠他，将一生交付给他。做他的妻子，他孩子的母亲，为他做饭，洗衣服，缝一颗掉了的纽扣。然后，我们一起在时光中变老。</p>
            </div>
            <span class="dateview">2014-1-1</span>
        </ul>
        <ul class="arrow_box">
            <div class="sy">
                <img src="images/001.png">
                <p> 我希望我的爱情是这样的，相濡以沫，举案齐眉，平淡如水。我在岁月中找到他，依靠他，将一生交付给他。做他的妻子，他孩子的母亲，为他做饭，洗衣服，缝一颗掉了的纽扣。然后，我们一起在时光中变老。</p>
                <span class="dateview">2014-1-1</span>
            </div>
        </ul>
    </div>
    <div class="page"><a title="Total record"><b>41</b></a><b>1</b><a href="/news/s/index_2.html">2</a><a href="/news/s/index_2.html">&gt;</a><a href="/news/s/index_2.html">&gt;&gt;</a></div>
</div>
<script src="js/silder.js"></script>