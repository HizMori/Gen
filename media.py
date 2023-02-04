from telebot import *

hello = 'Добро пожаловать в бот Твой Сяо❤️! Со мной вы сможете легко найти необходимую информацию для спокойной ' \
        'прокачки персонажа и оружия! Так же он будет вас оповещать каждый день о походе в подземелья за расходниками. ' \
        'Этот бот также поддерживает групповые чаты, так что вы можете легко добавить меня к своим друзьям.' \
        'Если у вас появились вопросы по использованию бота, то вы можете воспользоваться командой /help'

media_perets1 = [types.InputMediaPhoto('https://i.postimg.cc/9fpVpxJK/image.jpg'),
                types.InputMediaPhoto('https://i.postimg.cc/857vgrJp/1.jpg'),
                types.InputMediaPhoto('https://i.postimg.cc/k51SHy5Y/2.jpg'),
                types.InputMediaPhoto('https://i.postimg.cc/8kryh7Kg/image.jpg')]
media_perets2 = [types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2023/01/11/248396142/8c3f502f2c63d0f5dc31e4cda76f5ec8_2709100773759874495.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
                types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2023/01/11/248396142/e7b9b2cb2c8d77e35816b5cb029d81e6_3029676775000092866.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
                types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2023/01/11/248396142/e6a67abf1f03f89c8473562147085ccd_4251702208743734820.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
                types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2023/01/11/248396142/841418f605a047c3e481bedd13509d23_7218972961873990210.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
                types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2023/01/11/248396142/c31ed424cd2ea0100bf704c239a4a988_7016942985186208232.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
                types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2023/01/11/248396142/dc648e38ea6351a5c28b4240967a436b_2154431125517450.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
                types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2023/01/11/248396142/3afe152ef70baa6a5c29ca2c22b3065d_1645498852111973490.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg')]

media_grib1 = [types.InputMediaPhoto('https://i.postimg.cc/52gsgqHs/1.jpg'), types.InputMediaPhoto('https://i.postimg.cc/QMM0y91h/image.jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/0774c0cb07bdc290ef8aec9ab77643b0_824445332174608328.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/f4049a4095092952ae99937871444665_860780274113981893.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/d685fbcb67847a8b47e84aedab591c1c_4928430254578402991.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/9e3cb92b1a18003413b5d928e70e61f7_8127078306206984234.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/d013cd20241dfaf54c9a10bee248410c_3113225055569351491.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/3ec9255f05918e7fce4d7ed4d6a1a048_5340257791702002469.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/2a206d14a338cf7268f1bf20bc1a1fb8_594343664241571873.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396142/4a4970394051cba872083339be850b46_5710666535058818217.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png')]

media_gard1 = [types.InputMediaPhoto('https://i.postimg.cc/gJx4Yxzd/1.jpg'), types.InputMediaPhoto('https://i.postimg.cc/LX4KvB3D/2.jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396142/c7b7957f28d8607fee449ea8bfaf7601_8725600783151493873.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/fcb2dd6fe72c9e3d6a49baa4527913c2_6005081774931836412.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/e1db609beac3776ade64e8176897c249_2071042209594616216.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/805282b38565a5f90faa67f75e7283ea_8966026364200074690.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/0f5068d86ef0d89a263f500c610b8c65_7239754817660320353.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/bd662b556b21234fd80bee4417721954_2951135537844622677.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/bd662b556b21234fd80bee4417721954_2951135537844622677.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/6a3fa072bfd91af3e850787898c67b4a_7115024813099086136.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg')]

media_gard2 = [types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/afc7a25357cfa0794889a352687a4938_3595763331863425451.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/8ab087b7372fb97153703f1c7be6db15_6600808333733065844.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/58d4b54df1f9c650325799fab2f78df5_3803862728893235024.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/cee2d79aefcc4e337dd3f2630ae98558_2551545361586437464.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/5034e1ead54b1ef82d30dab6a8b05ab8_366173961046055039.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/a056df4270a2246388992110a83a9efd_8714113453286878850.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/b81d66510e19280c7e812fad695d1c2b_4233477195938368725.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg'),
               types.InputMediaPhoto('https://upload-os-bbs.hoyolab.com/upload/2022/12/15/248396142/c8fdd1615ffe82836feaeb6a7d102e32_5573573155229905028.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg')]