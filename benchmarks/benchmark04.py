def test_likitomi_130760006462(self):
    r = self.client.get('/likitomi/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["item_pic"]), u"""thumbs/mail.png""")
    self.assertEqual(unicode(r.context["subcontent_header"]), u"""Please scan or enter employee code""")
    self.assertEqual(unicode(r.context["is_enable_arrow"]), u"""False""")
    self.assertEqual(unicode(r.context["item_name"]), u"""Item name""")
    self.assertEqual(unicode(r.context["la_user_name"]), u"""USERNAME""")
    self.assertEqual(unicode(r.context["content_header"]), u"""Login""")
    self.assertEqual(unicode(r.context["is_enable_comment"]), u"""False""")
    self.assertEqual(unicode(r.context["is_enable_login"]), u"""True""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""False""")
    self.assertEqual(unicode(r.context["is_enable_tributton"]), u"""False""")
    self.assertEqual(unicode(r.context["is_enable_link"]), u"""False""")
    self.assertEqual(unicode(r.context["flashMessage"]), u"""""")
    self.assertEqual(unicode(r.context["title"]), u"""Welcome to Likitomi Status Tracking System""")
    self.assertEqual(unicode(r.context["page"]), u"""login""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Welcome""")


def test_likitomicssfal_stylecss_130760006487(self):
    r = self.client.get('/likitomi/css/fal_style.css', {})
    self.assertEqual(r.status_code, 200)


def test_likitomijavascriptflashjs_130760006494(self):
    r = self.client.get('/likitomi/javascript/flash.js', {})
    self.assertEqual(r.status_code, 200)


def test_likitomiimagesdjgpng_130760006526(self):
    r = self.client.get('/likitomi/images/djg.png', {})
    self.assertEqual(r.status_code, 200)


def test_faviconico_130760006536(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomihome_130760006883(self):
    r = self.client.get('/likitomi/home/', {'login': 'Login', 'user': 'workerATPC', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:29.081686""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitominormalplanrefresher_130760006998(self):
    r = self.client.get('/likitomi/normalPlanRefresher/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:29.986100""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitomilastupdate_130760007047(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:30.484825""")


def test_faviconico_130760007069(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_13076000727(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""CR""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:32.726486""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomipcdetailjavascriptflashjs_130760007302(self):
    r = self.client.get('/likitomi/pcdetail/javascript/flash.js', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailjavascriptjqueryjs_130760007306(self):
    r = self.client.get('/likitomi/pcdetail/javascript/jquery.js', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailjavascriptjquery_ui_1811customminjs_130760007314(self):
    r = self.client.get('/likitomi/pcdetail/javascript/jquery-ui-1.8.11.custom.min.js', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailcssfal_style2css_130760007323(self):
    r = self.client.get('/likitomi/pcdetail/css/fal_style2.css', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailcsssmoothnessjquery_ui_1810customcss_130760007328(self):
    r = self.client.get('/likitomi/pcdetail/css/smoothness/jquery-ui-1.8.10.custom.css', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailjavascriptjqueryquicksearchjs_130760007333(self):
    r = self.client.get('/likitomi/pcdetail/javascript/jquery.quicksearch.js', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailjavascriptjquerydatatablesjs_130760007339(self):
    r = self.client.get('/likitomi/pcdetail/javascript/jquery.dataTables.js', {})
    self.assertEqual(r.status_code, 200)


def test_likitomilastupdate_13076000737(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:33.710415""")


def test_likitomipcdetailcsssearch_iconpng_130760007377(self):
    r = self.client.get('/likitomi/pcdetail/css/search-icon.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailimagesquitpng_130760007386(self):
    r = self.client.get('/likitomi/pcdetail/images/quit.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailimagescv_normalpng_130760007391(self):
    r = self.client.get('/likitomi/pcdetail/images/CV_normal.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailimagespt_normalpng_130760007396(self):
    r = self.client.get('/likitomi/pcdetail/images/PT_normal.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailimageswh_normalpng_130760007401(self):
    r = self.client.get('/likitomi/pcdetail/images/WH_normal.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailcsssmoothnessimagesui_icons_888888_256x240png_130760007406(self):
    r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui-icons_888888_256x240.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailimagesdjgpng_130760007413(self):
    r = self.client.get('/likitomi/pcdetail/images/djg.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_130760007418(self):
    r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui-bg_flat_75_ffffff_40x100.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_130760007423(self):
    r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui-bg_highlight-soft_75_cccccc_1x100.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_130760007429(self):
    r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui-bg_glass_65_ffffff_1x400.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_75_e6e6e6_1x400png_130760007435(self):
    r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui-bg_glass_75_e6e6e6_1x400.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailimagescr_normalpng_13076000744(self):
    r = self.client.get('/likitomi/pcdetail/images/CR_normal.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetailimagespc_normalpng_130760007446(self):
    r = self.client.get('/likitomi/pcdetail/images/PC_normal.png', {})
    self.assertEqual(r.status_code, 200)


def test_faviconico_130760007453(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_75_dadada_1x400png_130760007458(self):
    r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui-bg_glass_75_dadada_1x400.png', {})
    self.assertEqual(r.status_code, 200)


def test_faviconico_130760007854(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomihomecsssmoothnessimagesui_bg_glass_75_dadada_1x400png_130760007859(self):
    r = self.client.get('/likitomi/home/css/smoothness/images/ui-bg_glass_75_dadada_1x400.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetail_130760009419(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:54.210875""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["page"]), u"""CV""")


def test_likitomilastupdate_130760009464(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:54.649419""")


def test_faviconico_130760009476(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_faviconico_130760009646(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760009762(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["page"]), u"""PT""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:57.647146""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760009804(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:58.046213""")


def test_likitomipcdetailimagescv_blackpng_130760009812(self):
    r = self.client.get('/likitomi/pcdetail/images/CV_black.png', {})
    self.assertEqual(r.status_code, 200)


def test_faviconico_130760009821(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_faviconico_130760010014(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760010124(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""WH""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:01.267739""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760010192(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:01.935450""")


def test_faviconico_130760010215(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_faviconico_130760010453(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760010568(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""CR""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:05.697315""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_13076001062(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:06.211677""")


def test_faviconico_130760010632(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetailimagescr_blackpng_130760010688(self):
    r = self.client.get('/likitomi/pcdetail/images/CR_black.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetail_130760010781(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""CR""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:07.830065""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760010827(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:08.284968""")


def test_faviconico_130760010846(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760011041(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:10.437439""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["page"]), u"""CV""")


def test_likitomilastupdate_130760011081(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:10.812250""")


def test_faviconico_13076001110(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetailimagespt_blackpng_130760011225(self):
    r = self.client.get('/likitomi/pcdetail/images/PT_black.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomipcdetail_13076001124(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["page"]), u"""PT""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:12.422798""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760011289(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:12.902492""")


def test_likitomipcdetailimageswh_blackpng_130760011299(self):
    r = self.client.get('/likitomi/pcdetail/images/WH_black.png', {})
    self.assertEqual(r.status_code, 200)


def test_faviconico_130760011303(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760011373(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""WH""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:13.753798""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760011406(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:14.069169""")


def test_faviconico_130760011421(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetailimagespc_blackpng_130760011428(self):
    r = self.client.get('/likitomi/pcdetail/images/PC_black.png', {})
    self.assertEqual(r.status_code, 200)


def test_likitomihome_130760011496(self):
    r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:15.081714""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitominormalplanrefresher_130760011576(self):
    r = self.client.get('/likitomi/normalPlanRefresher/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:15.768325""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitomilastupdate_130760011621(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:16.214159""")


def test_faviconico_130760011645(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760011961(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:19.634909""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["page"]), u"""CV""")


def test_likitomilastupdate_130760012014(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:20.148306""")


def test_faviconico_130760012022(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomihome_13076001216(self):
    r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:21.713089""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitominormalplanrefresher_130760012217(self):
    r = self.client.get('/likitomi/normalPlanRefresher/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:22.173076""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitomilastupdate_130760012261(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:22.622112""")


def test_faviconico_130760012283(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760012401(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:24.032179""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["page"]), u"""CV""")


def test_likitomilastupdate_130760012454(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:24.555077""")


def test_faviconico_130760012469(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760012535(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""CR""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:25.376307""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760012584(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:25.846340""")


def test_faviconico_130760012594(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760012721(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:27.233808""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["page"]), u"""CV""")


def test_likitomilastupdate_13076001276(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:27.611581""")


def test_faviconico_130760012769(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760012834(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["page"]), u"""PT""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:28.358351""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_13076001288(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:28.807214""")


def test_faviconico_130760012896(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760012944(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""WH""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:29.460604""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_13076001298(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:29.810382""")


def test_faviconico_130760012988(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomihome_130760013348(self):
    r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:33.603594""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitominormalplanrefresher_130760013434(self):
    r = self.client.get('/likitomi/normalPlanRefresher/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:34.349896""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitomilastupdate_13076001348(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:34.808124""")


def test_faviconico_130760013501(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760013626(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["page"]), u"""PT""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:36.275657""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760013673(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:36.742137""")


def test_faviconico_130760013683(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760013971(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""CR""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:39.734603""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760014019(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:40.198867""")


def test_faviconico_130760014031(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760014088(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:40.904628""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["page"]), u"""CV""")


def test_likitomilastupdate_13076001413(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:41.309265""")


def test_faviconico_130760014141(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760014179(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["page"]), u"""PT""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:41.811637""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_13076001423(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:42.310711""")


def test_faviconico_130760014242(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760014279(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""WH""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:42.807677""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760014317(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:43.174710""")


def test_faviconico_130760014325(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomihome_130760014469(self):
    r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:44.795591""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitominormalplanrefresher_130760014548(self):
    r = self.client.get('/likitomi/normalPlanRefresher/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:45.485300""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitomilastupdate_130760014594(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:45.945665""")


def test_faviconico_130760014625(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_13076001476(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""WH""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:47.628577""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760014816(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:48.165045""")


def test_faviconico_130760014823(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760014966(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""CR""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:49.683140""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760015012(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:50.123248""")


def test_faviconico_130760015026(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760015067(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:50.696872""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["page"]), u"""CV""")


def test_likitomilastupdate_13076001511(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:51.103919""")


def test_faviconico_13076001512(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760015157(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["page"]), u"""PT""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:51.594111""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760015205(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:52.061187""")


def test_faviconico_13076001522(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomipcdetail_130760015258(self):
    r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["page"]), u"""WH""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:52.615290""")
    self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


def test_likitomilastupdate_130760015297(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:52.979924""")


def test_faviconico_130760015309(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)


def test_likitomihome_130760015889(self):
    r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["thisMonth"]), u"""6""")
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
    self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-06-01 00:00:00""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["strThisMonth"]), u"""June""")
    self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["items"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:59.017152""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitominormalplanrefresher_130760015964(self):
    r = self.client.get('/likitomi/normalPlanRefresher/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["pos"]), u"""-2""")
    self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["startList"]), u"""-3""")
    self.assertEqual(unicode(r.context["cr"]), u"""idle""")
    self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
    self.assertEqual(unicode(r.context["cv"]), u"""idle""")
    self.assertEqual(unicode(r.context["size"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
    self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
    self.assertEqual(unicode(r.context["endList"]), u"""0""")
    self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
    self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
    self.assertEqual(unicode(r.context["wh"]), u"""idle""")
    self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
    self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
    self.assertEqual(unicode(r.context["pt"]), u"""idle""")
    self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
    self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
    self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:59.651206""")
    self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
    self.assertEqual(unicode(r.context["page"]), u"""PC""")


def test_likitomilastupdate_130760016007(self):
    r = self.client.get('/likitomi/lastUpdate/', {})
    self.assertEqual(r.status_code, 200)
    self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:16:00.081672""")


def test_faviconico_130760016028(self):
    r = self.client.get('/favicon.ico', {})
    self.assertEqual(r.status_code, 404)