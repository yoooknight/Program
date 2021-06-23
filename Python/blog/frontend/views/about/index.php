<?php
use yii\helpers\Url;
/* @var $this yii\web\View */
$this->title = "YoooKnight's Blog";
$index_url = Url::to(["site/index"]);
$local_url = Url::to(["about/index"]);
?>
<link href="css/about.css" rel="stylesheet">
<link href='http://fonts.googleapis.com/css?family=Architects+Daughter' rel='stylesheet' type='text/css'>

<article class="aboutcon">
    <h1 class="t_nav"><span>For you，thousand times！</span><a href="<?php echo $index_url?>" class="n1">网站首页</a><a href="<?php echo $local_url?>" class="n2">关于我</a></h1>
    <div class="about left">
        <h2>Just about me</h2>
        <ul>
            <p>YoooKnight，男，90后技术狂</p>
        </ul>
        <h2>About my blog</h2>
        <p>域  名：www.yoooknight.ml 创建于2016年01月12日</p>
        <p>服务器：搬瓦工</p>
    </div>
    <aside class="right">
        <div class="about_c">
            <p>网名：<span>YoooKnight</span> | 即步非烟</p>
            <p>生日：1993-10-23</p>
            <p>现居：四川省—成都市</p>
            <p>职业：码农~</p>
            <p>喜欢的书：《追风筝的人》《黑客与画家》</p>
        </div>
    </aside>
</article>
<script src="js/silder.js"></script>