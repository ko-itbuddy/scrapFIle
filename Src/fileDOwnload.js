'*ED*95*99*EC*82*AC*EA*B4*80*EB*A6*AC_15*EC*A3*BC_2018_*EB*AC*B8*EC*A0*9C.ppt',
'FILE_181211113257dbdc3113.ppt',
'/business/report/2018203070148723/'
function fileDownload(rfileName, sfileName, filePath) {
	var loc = "fileDownServlet?rFileName="+rfileName+"&sFileName="+sfileName+"&filePath="+filePath;
	hiddenFrame.location.href = loc;
}