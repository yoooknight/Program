var WINDOW_WIDTH=1300;
var WINDOW_HEIGHT=600;
var r=8;
var MARGIN_TOP=60;
var MARGIN_LEFT=175;

const endTime=new Date(2015,10,15,21,08,0);
var showCurrentTimeSeconds=0;

var balls=[];
const colors=["#E4F910","#F61229","#E916AF","#695DEC","#02B1FA","#139423","#ED700C","#12F1CF","#171110","#D16060"];
window.onload=function()
{
	var canvas=document.getElementById("canvas");
	var context=canvas.getContext("2d");
	showCurrentTimeSeconds=getShowCurrentTimeSeconds();
	canvas.width=WINDOW_WIDTH;
	canvas.height=WINDOW_HEIGHT;
	
	setInterval(function()
	{
		render(context);
		update();
				
	},50)


}
function getShowCurrentTimeSeconds()
	{
		var currentTime=new Date();
		var ret=endTime.getTime()-currentTime.getTime();
		ret=Math.round(ret/1000);
		return ret>0?ret:0;	
	}
function update()
{
	var nextShow=getShowCurrentTimeSeconds();
	var nextHours=parseInt(nextShow/3600);
	var nextMintes=parseInt(nextShow/60-nextHours*60);
	var nextSeconds=nextShow%60;

	var curHours=parseInt(showCurrentTimeSeconds/3600);
	var curMintes=parseInt(showCurrentTimeSeconds/60-curHours*60);
	var curSeconds=showCurrentTimeSeconds%60;

	if(curSeconds!=nextSeconds)
	{

		if(parseInt(nextHours/10)!=parseInt(curHours/10)){addBalls(MARGIN_LEFT,MARGIN_TOP,parseInt(curHours/10));}
		if(parseInt(nextHours%10)!=parseInt(curHours%10)){addBalls(MARGIN_LEFT+15*(r+1),MARGIN_TOP,parseInt(curHours%10));}
		if(parseInt(nextMintes/10)!=parseInt(curMintes/10)){addBalls(MARGIN_LEFT+38*(r+1),MARGIN_TOP,parseInt(curMintes/10));}
		if(parseInt(nextMintes%10)!=parseInt(curMintes%10)){addBalls(MARGIN_LEFT+53*(r+1),MARGIN_TOP,parseInt(curMintes%10));}
		if(parseInt(nextSeconds/10)!=parseInt(curSeconds/10)){addBalls(MARGIN_LEFT+76*(r+1),MARGIN_TOP,parseInt(curSeconds/10));}
		if(parseInt(nextSeconds%10)!=parseInt(curSeconds%10)){addBalls(MARGIN_LEFT+91*(r+1),MARGIN_TOP,parseInt(curSeconds%10));}
		showCurrentTimeSeconds=nextShow;
	}
	updateBalls();
}
function updateBalls()
	{
		for(var i=0;i<balls.length;i++)
		{
			balls[i].x+=balls[i].vx;
			balls[i].y+=balls[i].vy;
			balls[i].vy+=balls[i].g;
			if(balls[i].y>=WINDOW_HEIGHT-r)
			{
				balls[i].y=WINDOW_HEIGHT-r;
				balls[i].vy=-0.75*balls[i].vy;
			}
		}
	}
function addBalls(x,y,num)
{
	for(var i=0;i<digit[num].length;i++)
		for(var j=0;j<digit[num][i].length;j++)
		{
			if(digit[num][i][j]==1)
			{
				var aBall=
				{
					x:x+2*j*(r+1)+(r+1),
					y:y+2*i*(r+1)+(r+1),
					g:1.5+Math.random(),
					vx:Math.pow(-1,Math.ceil(Math.random()*1000))*4,
					vy:-5,
					color:colors[Math.floor(Math.random()*colors.length)]
				}	
				balls.push(aBall);
			}
		}
}
function render(cxt) 
{
	cxt.clearRect(0,0,WINDOW_WIDTH,WINDOW_HEIGHT);
	var hours=parseInt(showCurrentTimeSeconds/3600);
	var mintes=parseInt(showCurrentTimeSeconds/60-hours*60);
	var seconds=showCurrentTimeSeconds%60;
	
	readerDigit(MARGIN_LEFT,MARGIN_TOP,parseInt(hours/10),cxt);					
	readerDigit(MARGIN_LEFT+15*(r+1),MARGIN_TOP,parseInt(hours%10),cxt);					
	readerDigit(MARGIN_LEFT+30*(r+1),MARGIN_TOP,10,cxt);					
	readerDigit(MARGIN_LEFT+38*(r+1),MARGIN_TOP,parseInt(mintes/10),cxt);					
	readerDigit(MARGIN_LEFT+53*(r+1),MARGIN_TOP,parseInt(mintes%10),cxt);
	readerDigit(MARGIN_LEFT+68*(r+1),MARGIN_TOP,10,cxt);	
	readerDigit(MARGIN_LEFT+76*(r+1),MARGIN_TOP,parseInt(seconds/10),cxt);				
	readerDigit(MARGIN_LEFT+91*(r+1),MARGIN_TOP,parseInt(seconds%10),cxt);	

	cxt.font="bolder 60px Courier New";
	cxt.fillStyle="black";
	cxt.fillText("-BY Darker W",175,400);

	for(var i=0;i<balls.length;i++)
	{
		cxt.fillStyle=balls[i].color;
		cxt.beginPath();
		cxt.arc(balls[i].x,balls[i].y,r,0,2*Math.PI);
		cxt.closePath();

		cxt.fill();
	}

	
		
}
function readerDigit(x,y,num,cxt)
{
	cxt.fillStyle="#0FC4F5";
	for(var i=0;i<digit[num].length;i++)
		for(var j=0;j<digit[num][i].length;j++)
		{
			if(digit[num][i][j]==1)
			{

				cxt.beginPath();
				cxt.arc(x+2*j*(r+1)+(r+1),y+2*i*(r+1)+(r+1),r,0,2*Math.PI);
				cxt.closePath();
				cxt.fill();
			}
		}
}
