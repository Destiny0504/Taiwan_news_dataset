import re
import textwrap

import news.crawlers.db.schema
import news.crawlers.util.normalize
import news.crawlers.util.request_url
import news.parse.db.schema
import news.parse.epochtimes


def test_parsing_result() -> None:
    r"""Ensure parsing result consistency."""
    company_id = news.crawlers.util.normalize.get_company_id(company='大紀元')
    url = r'https://www.epochtimes.com/b5/13/7/21/n3922412.htm'
    response = news.crawlers.util.request_url.get(url=url)

    raw_news = news.crawlers.db.schema.RawNews(
        company_id=company_id,
        raw_xml=news.crawlers.util.normalize.compress_raw_xml(
            raw_xml=response.text,
        ),
        url_pattern=news.crawlers.util.normalize.compress_url(
            company_id=company_id,
            url=url,
        )
    )

    parsed_news = news.parse.epochtimes.parser(raw_news=raw_news)

    assert parsed_news.article == re.sub(
        r'\n',
        '',
        textwrap.dedent(
            '''\
            一架美國無人機在土耳其-伊拉克邊界墜毀。去年9月18日,潛伏在那裏的庫爾德工人黨武裝
            分子拍攝了燒燬的無人機殘骸,並把短片發佈在Youtube上。沒有人相信解說者的吹噓,稱
            他們打下了這架無人機。但對於懷疑此無人機國別的人來說,該短片中卻帶有英語的部件
            以及製造商的銘牌:美國通用原子公司(General Atomics)。 《華盛頓郵報》報導,這次
            墜機事件揭開了美軍秘密監控計劃「遊牧影子行動」(Operation Nomad Shadow)的
            面紗。2011年11月以來,美國空軍一直在土耳其東南部印吉利克空軍基地
            (Incirlik Air Base)試飛不帶武器的無人機,試圖壓制當地的地區衝突。「捕食者」
            (Predator)無人機帶有相機,能在土耳其-伊拉克邊界飛行時拍攝高解析度照片。這些照片
            幫助土耳其軍隊追蹤庫爾德工人黨武裝分子。 奧巴馬政府正在縮小無人機在阿富汗、
            巴基斯坦和也門的作戰範圍。不過,美軍把這些無人機用於世界其它的熱點地區。無人機
            戰爭的下一階段不在於消滅而是情報蒐集。這將會把五角大樓發達的監控網絡延伸到傳統的
            戰區以外。 美國無人機部署全球 過去十年中,美國國防部建成了一隻擁有400架飛機的
            無人機部隊,機型包括捕食者、死神(Reaper)、獵人(Hunter)、灰鷹(Gray Eagles)
            以及其它高空機種,給反恐行動帶來了一次革命。美軍離開阿富汗時,一部份無人機也回到
            美國。他們隨即又被部署到新的前線,用以監視武裝團體、販毒集團、海盜以及其它美國人
            關心的目標。 在中東,美軍在卡塔爾和阿拉伯聯合酋長國設立了無人機中樞,實施對波斯灣的
            偵察。去年11月,伊朗戰機兩次飛臨或向接近伊朗邊境的美國無人機開火。 在非洲,美國空軍
            無人機曾在5個月之前飛躍撒哈拉沙漠以追蹤馬里北部的基地組織叛亂分子。美國國防部在
            埃塞俄比亞、吉布提和塞舌爾建立了無人機基地。今年2月,美國空軍司令告訴國會,美國在
            非洲的監控、偵察和情報蒐集工作需要擴大15倍。 今年4月,美國副防長卡特
            (Ashton B. Carter)說,國防部將首次把死神無人機派遣到除阿富汗以外的其它亞洲
            地區。一名國防部發言人稱,美軍致力於增加其在亞太地區的監控能力。 在中南美洲,美軍
            一直希望使用無人機來協助反毒品行動。美軍南方司令部司令凱利
            (Marine Gen. John F. Kelly)今年3月表示,無人機能夠幫助減輕其航空兵的負擔。
            南方司令部發言人說,去年美軍航空兵在確定了一些販毒分子的精確地點後,哥倫比亞政府軍
            一舉消滅了32名重要武裝分子。如果配備捕食者和死神無人機,美軍追蹤販毒分子的區域和
            時間都可以得到大幅擴充。 出擊土耳其 2011年秋,四架被肢解的捕食者無人機被運送到
            土耳其印吉利克空軍基地。這些飛機來自伊拉克。它們同美軍航空兵協力配合,追蹤庫爾德
            工人黨武裝,並向土耳其軍隊提供錄像源。 庫爾德工人黨長久以來想在土耳其建立一個
            自治區,並從伊拉克北部的藏身之處頻頻發動襲擊。美國和土耳其當局都把該黨當作恐怖
            組織。土耳其則以空襲和炮擊還擊,並曾派遣地面部隊進入伊拉克。這給本來就不穩定的當地
            局勢火上澆油。 土耳其領導人擔心美軍撤離伊拉克之後,美國在打擊庫爾德工人黨上的合作
            也會消亡。因此他們邀請美軍在土耳其部署無人機,繼續執行偵察活動。 兩方都不願意透露
            這一協定。奧巴馬政府對其世界範圍內的無人機計劃三緘其口。國防部官員拒絕談論遊牧
            影子行動。土耳其政府僅表示該國部署有捕食者無人機,但這在該國是一個敏感話題。7月
            18日,皮尤中心發佈的一項調查表明,82%的土耳其人反對奧巴馬政府使用無人機獵殺國際
            極端分子。 9600公里外遙控 已發表的文件顯示,在龐大的印吉利克空軍基地,無人機僅佔了
            一個小小的角落。操作人員有30多名,來自美國空軍414遠征偵察中隊和承包商空戰飛行服務
            公司(Battlespace Flight Services)。 在絕大部份飛行時間中,捕食者受到9600公里
            外技師的遙控,通過衛星連接飛行。414遠征偵察中隊位於密蘇里州的惠特曼空軍基地。根據
            土耳其政府的規定,一旦進入土耳其領空,無人機必須關閉其照相機和感應器。從印吉利克
            空軍基地,航速為每小時220公里的捕食者將飛行約5個小時方能到達伊拉克邊境。 伊拉克
            政府允許這一行動。進入伊拉克之後,捕食者將按照一個長方形路線飛行,執行任務長達12
            小時。過程中它們將把錄像和其它情報傳迴密蘇里。美軍分析人士評估情報後,把情報發送到
            位於土耳其安卡拉的美土聯合情報辦公室。一名前美國空軍軍官稱,這一過程只有15-20分鐘
            的延遲。如果土耳其軍方想發動空襲或炮擊,無人機會有足夠時間離開該地區。 從這一計劃
            開始,某些美國官員就擔心出事故。2011年12月,土耳其戰機襲擊了一個從伊拉克進入土耳其
            的可疑商隊,34人死亡。後來證實這些人是走私犯,而不是恐怖份子。這在土耳其境內引發了
            抗議浪潮。 《華爾街日報》曾報導,去年美國無人機操作員通知土耳其軍方捕食者發現了
            可疑車隊。在未經詳查的情況下,土耳其官員命令無人機撤離,並迅速發動了襲擊。這一
            事件加劇了美軍官員的不滿。土耳其政府一直想要更長的飛行時間,甚至想要購買載有武器的
            死神無人機編隊。但是美國官員和國會一直不願批准。 美國前空軍官員表示,遊牧影子行動
            整體上很成功。他說,監控錄像防止了庫爾德工人黨的襲擊,並使土耳其軍隊發動更有限度、
            更精確的反恐行動成為可能。 失事報告中的線索 去年9月17日,美國參謀長聯席會議主席
            鄧普西(Martin Dempsey)在安卡拉會見了土耳其軍隊總參謀長奧澤兒(Necdet Özel)。
            土耳其媒體報導說,後者一如既往的敦促鄧普西在打擊庫爾德工人黨上提供更多幫助。 然而
            第二天,就傳來了捕食者無人機在伊拉克因突然斷電而墜毀的報告。美國空軍事故調查報告稱,
            該機在4分鐘內俯衝了3300米,最後在一個無人區墜毀。雖然該報告中所有的地理位置信息
            均被塗黑,但是報告中卻包含有一些清楚的線索,證明該機隸屬於遊牧影子行動。 該機地勤
            人員在報告中說,該無人機從印吉利克空軍基地出發,並受命於414遠征偵察中隊。另外一份
            文件中把該機稱為「遊牧01」。 但是該報告的附件裏提供了更強大的證據:失事地點的照片,
            來自庫爾德工人黨發佈在YouTube上的錄像。
            '''
        ),
    )
    assert parsed_news.category == '國際要聞'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1374336000
    assert parsed_news.reporter == '海寧'
    assert parsed_news.title == '美國無人機部署全球 不僅只限於戰區'
    assert parsed_news.url_pattern == '13-7-21-3922412'
