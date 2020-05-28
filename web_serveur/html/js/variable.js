//variable string 
var aClass=".socialMedials";
var oMenu=".menuHeaderTitle";
var oNoActiveMenuTop=".noActiveMenuTop";
var oActiveMenuTop="activeMenuTop";
var oProjects=".projectList";
var linkSocialNum=5;
var MenuTopDis=120;
var oProjectLists='.projectList';
var oBg="#oBlack";

//Projects Content
var IP01="This project is about network management and the demand of supply chain automation in Shandong area. The content is mainly to provide mobile network services for Shandong users."
var IP02="This project is a graduate project for undergraduates. This project is to help foreigners better understand foreign exhibitions. The audio guide is usually not particularly easy to use. It does not have Chinese and the content of the machine is not rich enough. I hope that by establishing a platform, The combination of people who can do the tour, the platform and the user, the idea is similar to the Uber platform"
var IP03="The Ali-baba project is a collaborating project among READi, University Paris 7 and Mobidys. It is aimed to provide an interactive and comprehensive way to help children’s reading and improve the reading skills";
var IP04="This is a business to business (B2B) e-commerce platform project. The main content of the project is to study UX and simplify the interface of the App, so that wholesalers can quickly use the commercial version of the App to place orders on the PFS platform, and better manage logistics as well. My job is mainly responsible for researching user experience and prototype through JavaScript and Java technology";
var IP05="Smart homes can build efficient management systems for residential facilities andfamily schedules, enhance home safety, convenience and artistry, and achieve an environmentally friendly and energy-efficient living environment. Complete enterprise-level requirements through design systems and design principles";
var IP06="We created a start-up Cuillere in France with the project - The Internet Exhibition,an O2O platform for sharing works of users from different regions and cultures. Iworked for this project as a UX designer, and I've been making effort to do the right thing for our users.";
var IP07="1111";
var IP08="1111";
var IP09="This project mainly implements 3D and unity. This is the school's personal project. What I want to do is to re-review the movie《Spirited Away》. The main object of the project is the mask. The scene uses shader, special effects, and postprocessing to set off the atmosphere.";

var CP01="Internship in Alcatel-Lucent Technology";
var CP02="Graduate project for Ecole de design Nantes Atlantique";
var CP03="Internship in Lab IHM & Mobidys";
var CP04="Internship in PFS,Paris";
var CP05="Internship in Hisense R&D";
var CP06="Created a Start-up Cuillère in France";
var CP07="11";
var CP08="11";
var CP09="Work in Arts et Metiers Paris Tech";

var TP01="Project Call";
var TP02="App Panoguider guide for exhibition";
var TP03="Mobidys Epubs Alibaba";
var TP04="E-commerce PFS B2B";
var TP05="Home automation SMART SOLUTION";
var TP06="Panoguider O2O Network Exhibition";
var TP07="11";
var TP08="11";
var TP09="M3D and VR with Unity";

var ZP01="Work on: C++, C, Java,  user exprience, Application systems <br> Dates: 01/07/2015-01/09/2015";
var ZP02="User exprience / JavaScript / AndroidStudio / arduino / Java";
var ZP03="/ JavaScript / Java / User exprience / Prototypes";
var ZP04="/ JavaScript / Sketch / User exprience / Java / Prototypes";
var ZP05="/ C++ / C / user exprience /";
var ZP06="/ C++ / C / user exprience /";
var ZP07="/ C++ / C / user exprience /";
var ZP08="/ C++ / C / user exprience /";
var ZP09="/ C# / 3ds Max / blender / Substance Painter / Unity / PostProcessing / shader / VR";

var CpJson={
	".CP01" :CP01,
	".CP02": CP02,
	".CP03": CP03,
	".CP04": CP04,
	".CP05": CP05,
	".CP06": CP06,
	".CP07": CP07,
	".CP08": CP08,
	".CP09": CP09
}
var TpJson={
	".TP01" :TP01,
	".TP02": TP02,
	".TP03": TP03,
	".TP04": TP04,
	".TP05": TP05,
	".TP06": TP06,
	".TP07": TP07,
	".TP08": TP08,
	".TP09": TP09
}

var PageContentsDataTitles=[
	{ "className" : ".PagesProjectsNames1" , "PagesContens" : TP01 },
	{ "className" : ".PagesProjectsNames2" , "PagesContens" : TP02 },
	{ "className" : ".PagesProjectsNames3" , "PagesContens" : TP03 },
	{ "className" : ".PagesProjectsNames4" , "PagesContens" : TP04 },
	{ "className" : ".PagesProjectsNames5" , "PagesContens" : TP05 },
	{ "className" : ".PagesProjectsNames6" , "PagesContens" : TP06 },
	{ "className" : ".PagesProjectsNames7" , "PagesContens" : TP07 },
	{ "className" : ".PagesProjectsNames8" , "PagesContens" : TP08 },
	{ "className" : ".PagesProjectsNames9" , "PagesContens" : TP09 }
]
var PageContentsDataSousTitles=[
	{ "className" : ".PagesProjectsUnTitles1" , "PagesContens" : CP01 },
	{ "className" : ".PagesProjectsUnTitles2" , "PagesContens" : CP02 },
	{ "className" : ".PagesProjectsUnTitles3" , "PagesContens" : CP03 },
	{ "className" : ".PagesProjectsUnTitles4" , "PagesContens" : CP04 },
	{ "className" : ".PagesProjectsUnTitles5" , "PagesContens" : CP05 },
	{ "className" : ".PagesProjectsUnTitles6" , "PagesContens" : CP06 },
	{ "className" : ".PagesProjectsUnTitles7" , "PagesContens" : CP07 },
	{ "className" : ".PagesProjectsUnTitles8" , "PagesContens" : CP08 },
	{ "className" : ".PagesProjectsUnTitles9" , "PagesContens" : CP09 }
]
var PageContentsDataIntroductions=[
	{ "className" : ".PagesProjectsIntroductions1" , "PagesContens" : IP01 },
	{ "className" : ".PagesProjectsIntroductions2" , "PagesContens" : IP02 },
	{ "className" : ".PagesProjectsIntroductions3" , "PagesContens" : IP03 },
	{ "className" : ".PagesProjectsIntroductions4" , "PagesContens" : IP04 },
	{ "className" : ".PagesProjectsIntroductions5" , "PagesContens" : IP05 },
	{ "className" : ".PagesProjectsIntroductions6" , "PagesContens" : IP06 },
	{ "className" : ".PagesProjectsIntroductions7" , "PagesContens" : IP07 },
	{ "className" : ".PagesProjectsIntroductions8" , "PagesContens" : IP08 },
	{ "className" : ".PagesProjectsIntroductions9" , "PagesContens" : IP09 }
]
var PageContentsDataTags=[
	{ "className" : ".PagesProjectsTags1" , "PagesContens" : ZP01 },
	{ "className" : ".PagesProjectsTags2" , "PagesContens" : ZP02 },
	{ "className" : ".PagesProjectsTags3" , "PagesContens" : ZP03 },
	{ "className" : ".PagesProjectsTags4" , "PagesContens" : ZP04 },
	{ "className" : ".PagesProjectsTags5" , "PagesContens" : ZP05 },
	{ "className" : ".PagesProjectsTags6" , "PagesContens" : ZP06 },
	{ "className" : ".PagesProjectsTags7" , "PagesContens" : ZP07 },
	{ "className" : ".PagesProjectsTags8" , "PagesContens" : ZP08 },
	{ "className" : ".PagesProjectsTags9" , "PagesContens" : ZP09 }
]

