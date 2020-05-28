
function introAnimation(){
	var oMove=document.getElementById('introduction');
	setTimeout(function(){
		startMove(oMove,{opacity:100},20);
	},200);
}
/***************************** Background Black  **************************************/ 
function controlBg(iSwitch){
	var oContactMePage=document.getElementById('ContactMePage');
	(iSwitch ? $("#oBlack").css('display','block') : $("#oBlack").css('display','none'));
		$("#oBlack").click(function(){
		controlBg(false);
		$("#ContactCV").css('display','none');
		$("#DownLoadMyCv").css('display','none');
		startMove(oContactMePage,{height:0},6);
		if($("#ContactMePage").height()==0){
			$("#ContactMePage").css('display','none');			
		}

	})
}
/***************************** Projects Lists  **************************************/ 
function fadeProjectsList(){
	for(var i=0;i<$(oProjectLists).length;i++){
		$(oProjectLists).eq(i).mouseover(function(){
			$(this).addClass('projectListActive');
			//$(this).find('.IntroProject').css('display','block');
		});
		$(oProjectLists).eq(i).mouseout(function(){
			$(this).removeClass('projectListActive');
			//$(this).find('.IntroProject').css('display','none');
		});	
	}		
}

/***************************** MenuTop  **************************************/ 
//调用方法
function displayMenuTop(oMenuMain){

	// oMenuMain[0].offset({left:oMenuMain[0].offset().left});
	// oMenuMain[1].offset({left:oMenuMain[1].offset().left+200});
	// oMenuMain[2].offset({left:oMenuMain[2].offset().left+400});
	//displayMenuTop(oMenuMain);
	for(var i=0;i<oMenuMain.length;i++){
		oMenuMain[i].index=i;
		oMenuMain[i].offset({left:(oMenuMain[i].offset().left+i*MenuTopDis)});
	}
}
//underLine animate Menu Top;
function underLineAnimate(mOver,mOut){
	for(var i=0;i<$(mOver).length;i++){
		//oMenuTop[i].index=i;
		$(mOver).eq(i).mouseover(function(){
			$(this).addClass(mOut);
		})
		$(mOver).eq(i).mouseout(function(){
			$(this).removeClass(mOut);
		})
	}		
}
/***************************** SocialMedia  **************************************/ 
function socialMedia(){
	for(var i=0;i<linkSocialNum;i++){
	clickToSocial(aClass,i,linkArray[i]);
	socialHover(aClass,i,adressArrayActive[i],adressArray[i]);
	}
}	
function socialHover(aClass,id,sLinkover,sLinkout){
	$(aClass).eq(id).mouseover(function(){
		$(aClass).eq(id).children("img").attr("src", sLinkover);
	});
	$(aClass).eq(id).mouseout(function(){
		$(aClass).eq(id).children("img").attr("src", sLinkout);
	});
}

// event to click social media
function clickToSocial(aClass,id,sLink){
		$(aClass).eq(id).click(function(){
		link(sLink);
	});
}

/***************************** Content Output Projects and Imgs  **************************************/ 
// output Content to Projects
function contentOutput(jsonContent){
	for(var key in jsonContent){
		$(key).html(jsonContent[key]);
	}
}

function ImgSrcOutput(jsonContent){
	for(var key in jsonContent){
		$(key).attr("src",jsonContent[key]);
		// $(key).html(jsonContent[key]);
	}
}
/***************************** Contact Js **************************************/ 
function MyResume(){
	var oContactMePage=document.getElementById('ContactMePage');
	var CVHeight=1400;
	$("#MyResume").click(function(){
		controlBg(true);
		$("#ContactMePage").css('display','block');
		$("#DownLoadMyCv").css('display','block');
		startMove(oContactMePage,{height:CVHeight},6);
		
		setTimeout(function(){
			$("#ContactCV").css('display','block');
			TransparentEffet("ContactCV",true);
		},400);	
	});
}
/***************************** Transparent DownloadCv **************************************/ 
function TransparentEffet(element,bool){
	var oElement=document.getElementById(element);
	//alert("1");
	//startMove(oElement,{opacity:100},20);
	( bool ? startMove(oElement,{opacity:100},30) : startMove(oElement,{opacity:0},30) );
}

/***************************** Click Projects **************************************/ 

function clickProjectsList(key){
	$(PagesJson[key].class).click(function(){
		window.location=PagesJson[key].link;
		
	})	
}

/***************************** Pages Contents**************************************/ 
function OutputPagesContents(key){
	//改变内容
	$(PageContentsDataTitles[key].className).html(PageContentsDataTitles[key].PagesContens);
	$(PageContentsDataSousTitles[key].className).html(PageContentsDataSousTitles[key].PagesContens);
	$(PageContentsDataIntroductions[key].className).html(PageContentsDataIntroductions[key].PagesContens);
	$(PageContentsDataTags[key].className).html(PageContentsDataTags[key].PagesContens);
}

/***************************** affiche touts project pages **************************************/ 
function imgContentsCreates(num,json,id){
	var arrayEle = new Array(num);
	
	for(var i=0;i<arrayEle.length;i++){
		//arrayEle[i].index=i;
		arrayEle[i]="<li class=\"Pcp ProjectsContentsPresents"+(i+1)+"\"><img class=\"imgPagesContents\"></li>";
		$(id).append(arrayEle[i]);
	}
	for(var key in json){
		$(key).children("img").attr("src", json[key]);
	}
	var lists=$('.imgPagesContents');
	for(var i=0;i<lists.length;i++){
		//$('.imgPagesContents').css('display','block');
		startMove(lists[i],{opacity:100},30)
	}		
}
/***************************** affiche touts project pages **************************************/ 
function backSpace(){
	// 	$(aClass).eq(id).mouseover(function(){
	// 	$(aClass).eq(id).children("img").attr("src", sLinkover);
	// });
	// $(aClass).eq(id).mouseout(function(){
	// 	$(aClass).eq(id).children("img").attr("src", sLinkout);
	// });
	$("#btnBackSpace").mouseover(function(){
		$(this).children("img").attr("src",link_BackSpaceActive);
	});
	$("#btnBackSpace").mouseout(function(){
		$(this).children("img").attr("src",link_BackSpace);
	});		
	$("#btnBackSpace").click(function(){
		window.location="../main.html";
	});		
}















/***************************** Create Node Elements on the main pages  **************************************/ 
// function CreateNodeOnMainPages(numProjects){
// 	for(var i=0;i<numProjects.length;i++){

// 	}
// }





















