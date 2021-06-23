
var num=document.getElementsByTagName("li").length,
    _this=$(this),
    _index=_this.index(),
    li=$("ul li").eq(_index),
    max=1178;
   


 
 $("ul").each(
 function(){
 	for(var i=0;i<=19;i++)
 {  var x=62*(i);
    $(this).find("li").eq(i).find("a").css("background-position","0px -"+x+"px");
 }
 }
)

$("#content_l").kxbdSuperMarquee({ isMarquee:true,direction:"up",scrollAmount:1,scrollDelay:30,time:10});

$("#content_r").kxbdSuperMarquee({ isMarquee:true,direction:"down",scrollAmount:1,scrollDelay:30,time:10});






/*
$(".ad").mouseover(function(){
	$("#logo").stop();
	$("#logo").animate({bottom:"0px",opacity:"0.9"},200); 
});
$(".ad").mouseleave(function(){
$("#logo").stop();
	$("#logo").animate({bottom:"-50px",opacity:"0"},200);
});*/
$(" li").mouseover(function(){
	$(this).find("img").attr("src","./img/border_02.png");

});
$("li").mouseleave(function(){
	$(this).find("img").attr("src","./img/border_01.png");
});


		