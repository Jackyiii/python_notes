function controlPosition(){
	$(oBg).height($(document).height());
}
function offsetValue(oDiv){
	var offLeft=oDiv.offset().left;
	var offTop=oDiv.offset().top;
	var info={"left":offLeft,"top":offTop};
	return info;
}

