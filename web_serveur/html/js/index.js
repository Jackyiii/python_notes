window.onresize=function(){
  OWidth=parseInt($(window).width()*0.14);
  OHeight1=parseInt($(window).height()*0.40);//0.48
  OHeight2=parseInt($(window).height()*0.56);
  $("#lineAnimationIndex1").width()==OWidth;
  $("#lineAnimationIndex2").width()==OWidth;
}
window.onload=function(){
	/* ---- particles.js config ---- */
// 目标元素、配置参数对象、回调函数
  ParticleJs_index();
  var OMove1=document.getElementById("lineAnimationIndex1");
  var OMove2=document.getElementById("lineAnimationIndex2");
  var OWidth=parseInt($(window).width()*0.14);
  var OHeight1=parseInt($(window).height()*0.40);//0.48
  var OHeight2=parseInt($(window).height()*0.56);
  var timer1=null;

  setTimeout(function(){
    startMove(OMove1,{width:OWidth},4,function(){
        if($("#lineAnimationIndex1").width()==OWidth){
          setTimeout(function(){
            startMove(OMove1,{top:OHeight1},4,function(){
              if($("#lineAnimationIndex1").offset().top==OHeight1){
                setTimeout(function(){
                  $("#MyNamePortIndex").css('display','block');
                  $("#MyNamePortIndex2").css('display','block');
                },500);
              }
            });
          },500);
        }
    });
  },8000);
  setTimeout(function(){
    startMove(OMove2,{width:OWidth},4,function(){
        if($("#lineAnimationIndex2").width()==OWidth){
          setTimeout(function(){
            startMove(OMove2,{top:OHeight2},4);
          },500);
        }
    });
  },8000);


  setTimeout(function(){
    window.location="main.html";
  },12000);
}
function ParticleJs_index(){
  particlesJS("contarner", {
    
    "particles": {
      "number": {                   
        "value": 100, // 粒子数量
        "density": {
          "enable": true, // 启用粒子密度
          "value_area": 800 // 每一个粒子占据的空间（启用粒子密度，才可用）
        }
      },
      
      "color": {
        "value": "07BBF3" // 粒子颜色
      },
      
      "shape": {
        "type": "circle", // 粒子形状
        "stroke": {
          "width": 0, // 粒子边框宽度
          "color": "#55EDED" // 粒子边框颜色
        },
        "polygon": {
          "nb_sides": 5 // 多边形粒子的边数
        },
        // "image": {
        //   "src": "img/github.svg", // 自定义粒子(图片替代)
        //   "width": 100, // 自定义粒子图片宽度
        //   "height": 100 // 自定义粒子图片高度
        // }
      },
      
      "opacity": {
        "value": 0.5, // 不透明度
        "random": false,// 随机不透明度
        "anim": {
          "enable": false, // 开启渐变动画
          "speed": 1, // 渐变动画速度
          "opacity_min": 0.1, // 渐变动画不透明度
          "sync": false
        }
      },
      
      "size": {
        "value": 2, // 粒子大小
        "random": true, // 粒子大小随机
        "anim": {
          "enable": true, // 粒子渐变(闪烁)
          "speed": 10, // 粒子渐变速度
          "size_min": .5, // 渐变最小粒子
          "sync": false
        }
      },
      
      "line_linked": {
        "enable": true, // 开启连接线
        "distance": 150, // 连接线有效距离
        "color": "#07BBF3", // 连接线颜色
        "opacity": 0.4, // 连接线不透明度
        "width": 1 // 连接线的宽度
      },
      
      "move": {
        "enable": true, // 开启粒子移动
        "speed": 1, // 移动速度
        "direction": "none", // 移动方向
        "random": false, // 移动方向随机
        "straight": false, // 直接移动
        "out_mode": "out", // 是否移出画布
        "bounce": true, // 是否跳动移动
        "attract": {
          "enable": false, // 粒子之间吸引
          "rotateX": 600, // X 水平距离
          "rotateY": 1200 // Y 水平距离
        }
      }
    },
    "interactivity": {
      "detect_on": "canvas", // 粒子之间互动检测
      "events": {
        "onhover": {
          "enable": false, // 开启悬停
          "mode": "grab" // 悬停模式
        },
        "onclick": {
          "enable": false, // 鼠标单击效果
          "mode": "push" // 效果模式
        },
        "resize": false //  互动事件调整
      },
      "modes": {
        "grab": {
          "distance": 140, // 粒子互动抓取距离
          "line_linked": {
            "opacity": 1 // 粒子互动抓取距离连线不透明度
          }
        },
        "bubble": {
          "distance": 400, // 粒子抓取泡沫效果之间的距离
          "size": 40, // 粒子抓取泡沫效果之间的大小
          "duration": 2, // 粒子抓取泡沫效果之间的持续时间
          "opacity": 8, // 不透明度
          "speed": 3 // 速度
        },
        "repulse": {
          "distance": 200, // 击退效果距离
          "duration": 0.4 // 击退效果持续时间
        },
        "push": {
          "particles_nb": 4 // 粒子推出的数量
        },
        "remove": {
          "particles_nb": 2 // 粒子移除的数量
        }
      }
    },
    "retina_detect": true // 视图检测
  });
}