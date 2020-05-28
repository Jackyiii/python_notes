window.onload=function(){
	var oMenuMain=new Array($(oMenu).eq(0),$(oMenu).eq(1),$(oMenu).eq(2));
	underLineAnimate(oNoActiveMenuTop,oActiveMenuTop);
	socialMedia();
	displayMenuTop(oMenuMain);
	fadeProjectsList();
	controlPosition();
	controlBg(false);
	introAnimation();
    contentOutput(CpJson);
    contentOutput(TpJson);
    ImgSrcOutput(ImgSrcJson);
    MyResume();
   	for(var i=0;i<PagesJson.length;i++){
   		clickProjectsList(i);
   	}
   	



















	//ParticleJs_index();
	// new Typed('#typed3', {
 //    	strings: [
 //    	  '',
 //    	  '',
 //    	  // 'I am ...',
 //    	  'who am I?',
 //    	  '',
 //    	  '',

 //    	  // 'I am a passionate about Design UX, Java, Innovation, AI(Artificial Intelligence) and VR(Virtual Reality).',
 //    	  'I am a passionate about Design UX, Java, Innovation, AI(Artificial Intelligence) and VR(Virtual Reality). And I\'m work specialising in Interaction Design, User Experience, Innovation, VR and Technology.'
 //    	],
 //    	typeSpeed: 15,
 //    	backSpeed: 5,
 //    	smartBackspace: true,
 //    	loop: false
 //  	});

}


