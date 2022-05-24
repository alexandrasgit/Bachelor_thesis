setBatchMode(true) ;
count = 1;
fileIn= getDirectory("Choose a Directory");
listIn= getFileList(fileIn); 
nIn =lengthOf(listIn);

fileOut= getDirectory("Choose a Directory");


for (i=0; i < listIn.length; i++) {
	green = listIn[i];
	print(green);
	if (startsWith(green, "GFP") && endsWith(green, ".tif")) {
		  name = substring(green,3,green.length - 4);
		  print(name);
		  red = "red"+name+".tif";
		  open(fileIn+green);
		  open(fileIn + red);
		  run("Merge Channels...", "c2="+green+ " c1="+red+ " keep");
		  out = name+".png";
		  
		  run("Set Scale...", "distance=483.3887 known=100 unit=um global");
		  // run("Scale Bar...", "width=10 height=4 font=12 color=Black background=None location=[Lower Right] bold overlay");
		  run("Scale Bar...", "width=100 height=16 font=56 bold overlay");
		  
		  saveAs("png", fileOut+out);
		  close("*");
	}
} 
setBatchMode(false) ;
