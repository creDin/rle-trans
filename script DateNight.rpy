label Date_Ask(Girl=0): #rkeljsvgb
        #From the chat menu, you ask Rogue to meet you
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)
        if "yesdate" in Girl.DailyActions:
                $ Girl.FaceChange("bemused")
                if Girl is RogueX:
                        ch_r "Да ладно, Я же уже сказала тебе \"да.\""
                elif Girl is KittyX:
                        ch_k "Лол, я же уже сказала тебе \"да.\""
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Ты забыла? Я уже сказала тебе \"да\", [Girl.Petname]."
                        else:
                            ch_e "Ты забыл? Я уже сказала тебе \"да\", [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Я же уже сказала тебе \"ладно.\""
                elif Girl is JeanX:
                        ch_j "Ты все еще здесь?"
                elif Girl is StormX:
                        ch_s "Я уже согласилась, [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "Ага, мы уже об этом договорились..."
                elif Girl is GwenX:
                        ch_g "Ты хочешь... чтобы я еще раз сказала тебе \"да\"?"
                elif Girl is BetsyX:
                        ch_b "Кажется, я уже приняла твое приглашение..."
                elif Girl is DoreenX:
                        ch_d "Я уже согласилась."
                elif Girl is WandaX:
                        ch_w "Можешь перестать спрашивать, я приду."
                return
        if "askeddate" in Girl.DailyActions:
                $ Girl.FaceChange("angry")
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Думаю, ты уже получила ответ."
                        else:
                            ch_r "Думаю, ты уже получил ответ."
                elif Girl is KittyX:
                        ch_k "Боже, хватит уже меня доставать!"
                elif Girl is EmmaX:
                        ch_e "Настойчивость останется без награды, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Отвали."
                elif Girl is JeanX:
                        ch_j "Ты все еще здесь?"
                elif Girl is StormX:
                        ch_s "Я уже сказала \"нет,\" [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "Ага, в смысле я уже сказал \"нет\"..."
                elif Girl is GwenX:
                        ch_g "\"Принцесса в другом замке\"..."
                elif Girl is BetsyX:
                        ch_b "Я уже отклонила твое приглашение..."
                elif Girl is DoreenX:
                        ch_d "Перестань приставать ко мне."
                elif Girl is WandaX:
                        ch_w "Можешь перестать спрашивать, я не приду."
                return
        if "stoodup" in Girl.Traits:
                call Date_Stood_Up(Girl)
                #$ Girl.AddWord(1,"askeddate","askeddate")#recent and daily
                return
        $ Girl.AddWord(1,"askeddate","askeddate")  #recent and daily

        if Girl is EmmaX:
                if "classcaught" not in EmmaX.History:
                        #if you haven't caught her yet
                        ch_e "Не думаю, что нас должны видеть вместе."
                        return
                if "taboo" not in EmmaX.History:
                        #if she hasn't agreed to go public yet
                        call Emma_Taboo_Talk
                        if "taboo" not in EmmaX.History:
                            return
        if Girl.Break[0] and "ex" in Girl.Traits:
                $ Girl.FaceChange("angry")
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Серьезно? Ты просишь меня об этом после того, что ты недавно сделала?"
                        else:
                            ch_r "Серьезно? Ты просишь меня об этом после того, что ты недавно сделал?"
                elif Girl is KittyX:
                        ch_k "Ты не можешь просто притворяться, что ничего не произошло!"
                elif Girl is EmmaX:
                        ch_e "Прежде чем задавать такой вопрос, разберись в себе."
                elif Girl is LauraX:
                        ch_l "Лучше бы тебе сейчас меня не доставать."
                elif Girl is JeanX:
                        if not Player.Male:
                            ch_j "Если бы не твоя способность, ты бы даже не вспомнила, что ты сделала."
                        else:
                            ch_j "Если бы не твоя способность, ты бы даже не вспомнил, что ты сделал."
                        ch_j "Но я  бы -помнила-."
                elif Girl is StormX:
                        ch_s "Боюсь, что нет. Возможность утеряна."
                elif Girl is JubesX:
                        ch_v "Я вроде как все еще зла на тебя?"
                elif Girl is GwenX:
                        ch_g "У меня нет на это времени."
                elif Girl is BetsyX:
                        ch_b "Мне кажется, наше свидание не пройдет хорошо..."
                elif Girl is DoreenX:
                        ch_d "Я совсем не хочу сейчас никуда с тобой идти."
                elif Girl is WandaX:
                        ch_w "Я даже думать об этом сейчас не хочу."
                return
        if "ex" in Girl.Traits:
            if ApprovalCheck(Girl, 1200):
                    $ Girl.FaceChange("bemused",Brows = "sad" )
                    if Girl is RogueX:
                            ch_r "Раньше мы неплохо веселились, думаю, мы можем сходить куда-нибудь, как друзья."
                    elif Girl is KittyX:
                            ch_k "Не знаю, раньше нам было весело. Наверное, я не против..."
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Раньше ты была интересной собеседницей. Полагаю, можно попробовать еще раз."
                            else:
                                ch_e "Раньше ты был интересным собеседником. Полагаю, можно попробовать еще раз."
                    elif Girl is LauraX:
                            ch_l "Ну, раньше мы неплохо проводили время..."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Напомни, кто ты такая?"
                            else:
                                ch_j "Напомни, кто ты такой?"
                    elif Girl is StormX:
                            ch_s "Пожалуй, мы могли бы прогуляться как друзья, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Ага, ну, мы могли бы пойти как друзья или типа того..."
                    elif Girl is GwenX:
                            ch_g "Эм, конечно, как скажешь, я всегда рада бесплатной еде."
                            ch_g "Лучше бы, чтобы она была."
                    elif Girl is BetsyX:
                            ch_b "Раньше мы неплохо проводили время вместе, думаю, не повредит провести еще один вечер в твоей компании..."
                    elif Girl is DoreenX:
                            ch_d "Ну, конечно, я думаю это может быть весело."
                    elif Girl is WandaX:
                            ch_w "Конечно..."
            else:
                    $ Girl.FaceChange("angry",Eyes = "side")
                    if Girl is RogueX:
                            ch_r "Не думаю, что хочу идти куда-либо с тобой, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "Я[Girl.like]так не думаю."
                    elif Girl is EmmaX:
                            ch_e "Я не думаю, что хочу идти куда-либо с тобой, [Girl.Petname]."
                    elif Girl is LauraX:
                            ch_l "Нет, лучше я откажусь."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Напомни, кто ты такая?"
                            else:
                                ch_j "Напомни, кто ты такой?"
                    elif Girl is StormX:
                            ch_s "Мы были плохой парой, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Не думаю, что в этом есть хоть какой-то смысл..."
                    elif Girl is GwenX:
                            ch_g "Неа."
                    elif Girl is BetsyX:
                            ch_b "Я не вижу в этом никакого смысла..."
                    elif Girl is DoreenX:
                            ch_d "У меня сейчас много дел."
                    elif Girl is WandaX:
                            ch_w "Думаю, я не хочу с тобой связываться."
                    return

        call FriendlyDate #checks to see if this is more than just friends...

        if "stoodup" in Girl.History or "deadbeat" in Girl.History:
            if "stoodup" in Girl.History:
                    $ Girl.FaceChange("angry",Eyes = "side")
                    if Girl is RogueX:
                            ch_r "На этот раз не заставляй меня ждать."
                    elif Girl is KittyX:
                            ch_k "Я не хочу снова ждать тебя пол вечера на площади."
                    elif Girl is EmmaX:
                            ch_e "Уверена, ты знаешь, что лучше не заставлять меня снова ждать."
                    elif Girl is LauraX:
                            ch_l "Только не заставляй меня снова ждать."
                    elif Girl is JeanX:
                            ch_j "Я редко даю вторые шансы."
                    elif Girl is StormX:
                            ch_s "На этот раз обязательно сдержи свое обещание, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "В этот раз действительно приходи..."
                    elif Girl is GwenX:
                            ch_g "Только не бросай меня одну... снова."
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Пожалуйста, на этот раз будь пунктуальна..."
                            else:
                                ch_b "Пожалуйста, на этот раз будь пунктуален..."
                    elif Girl is DoreenX:
                            ch_d "В этот раз ты планируешь прийти?"
                    elif Girl is WandaX:
                            ch_w "Я не хочу снова ждать тебя непонятно сколько."
            if "deadbeat" in Girl.History:
                    $ Girl.FaceChange("angry")
                    if Girl is RogueX:
                            if "stoodup" in Girl.History:
                                if not Player.Male:
                                    ch_r "Помнишь, что в прошлый раз ты даже заставила меня заплатить за тебя, нищебродку?"
                                else:
                                    ch_r "Помнишь, что в прошлый раз ты даже заставил меня заплатить за тебя, нищеброда?"
                            else:
                                if not Player.Male:
                                    ch_r "Помнишь прошлый раз, когда ты заставила меня платить за тебя, нищебродку?"
                                else:
                                    ch_r "Помнишь прошлый раз, когда ты заставил меня платить за тебя, нищеброда?"
                    elif Girl is KittyX:
                            if "stoodup" in Girl.History:
                                if not Player.Male:
                                    ch_k "Да и на нашем прошлом свидание, ты[Girl.like]оставила счет на меня!"
                                else:
                                    ch_k "Да и на нашем прошлом свидание, ты[Girl.like]оставил счет на меня!"
                            else:
                                if not Player.Male:
                                    ch_k "На нашем прошлом свидание, ты[Girl.like]оставила счет на меня!"
                                else:
                                    ch_k "На нашем прошлом свидание, ты[Girl.like]оставил счет на меня!"
                    elif Girl is EmmaX:
                            if "stoodup" in Girl.History:
                                ch_e "И я больше не хочу оплачивать счет."
                            else:
                                ch_e "Я больше не хочу оплачивать счет."
                    elif Girl is LauraX:
                            if "stoodup" in Girl.History:
                                if not Player.Male:
                                    ch_l "И в прошлый раз ты просто оставила счет на меня."
                                else:
                                    ch_l "И в прошлый раз ты просто оставил счет на меня."
                            else:
                                if not Player.Male:
                                    ch_l "В прошлый раз ты просто оставила счет на меня."
                                else:
                                    ch_l "В прошлый раз ты просто оставил счет на меня."
                    elif Girl is JeanX:
                            if "stoodup" in Girl.History:
                                if not Player.Male:
                                    ch_j "и -в особенности- бездельницам вроде тебя."
                                else:
                                    ch_j "и -в особенности- бездельникам вроде тебя."
                            else:
                                if not Player.Male:
                                    ch_j "Ты забыла, как в прошлый раз просила \"заплатить за тебя\"..."
                                else:
                                    ch_j "Ты забыл, как в прошлый раз просил \"заплатить за тебя\"..."
                    elif Girl is StormX:
                            if "stoodup" in Girl.History:
                                ch_s "И на этот раз я не буду оплачивать счет."
                            else:
                                ch_s "И на этот раз я не буду оплачивать счет."
                    elif Girl is JubesX:
                            if "stoodup" in Girl.History:
                                if not Player.Male:
                                    ch_v "-а еще в прошлый раз ты просто оставила счет на меня!"
                                else:
                                    ch_v "-а еще в прошлый раз ты просто оставил счет на меня!"
                            else:
                                if not Player.Male:
                                    ch_v "В прошлый раз ты просто оставила счет на меня!"
                                else:
                                    ch_v "В прошлый раз ты просто оставил счет на меня!"
                    elif Girl is GwenX:
                            if "stoodup" in Girl.History:
                                if not Player.Male:
                                    ch_g "И убедись, что в этот раз ты взяла с собой кошелек!"
                                else:
                                    ch_g "И убедись, что в этот раз ты взял с собой кошелек!"
                            else:
                                if not Player.Male:
                                    ch_g "Убедись, что в этот раз ты взяла с собой кошелек!"
                                else:
                                    ch_g "Убедись, что в этот раз ты взял с собой кошелек!"
                    elif Girl is BetsyX:
                            if "stoodup" in Girl.History:
                                ch_b "И не забудь взять с собой бумажник..."
                            else:
                                ch_b "В этот раз у меня нет желания платить за тебя..."
                    elif Girl is DoreenX:
                            if "stoodup" in Girl.History:
                                ch_d "-и на этот раз я не буду платить за тебя."
                            else:
                                ch_d "В этот раз я не буду платить за тебя."
                    elif Girl is WandaX:
                            if "stoodup" in Girl.History:
                                ch_w "-ия не собираюсь платить за тебя."
                            else:
                                ch_w "Но я не собираюсь платить за тебя."
            menu:
                extend ""
                "Извини, на этот раз все будет по-другому.":
                        if ApprovalCheck(Girl, 650):
                                $ Girl.FaceChange("sad")
                                if Girl is RogueX:
                                        ch_r "Ладно, [Girl.Petname], тебе лучше сдержать слово."
                                elif Girl is KittyX:
                                        ch_k "Ну, думаю, я могу дать тебе еще один шанс, только не разочаровывай меня снова."
                                elif Girl is EmmaX:
                                        ch_e "Ловлю тебя на слове, [Girl.Petname]."
                                elif Girl is LauraX:
                                        ch_l "Хорошо, у тебя появился еще один шанс, не облажайся."
                                elif Girl is JeanX:
                                        if not Player.Male:
                                            ch_j "Ох, уверена? Тебе лучше сдержать слово."
                                        else:
                                            ch_j "Ох, уверен? Тебе лучше сдержать слово."
                                elif Girl is StormX:
                                        ch_s "Ты должен сдержать свое слово, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "Очень на это надеюсь..."
                                elif Girl is GwenX:
                                        ch_g "О да, надеюсь."
                                elif Girl is BetsyX:
                                        ch_b "Посмотрим..."
                                elif Girl is DoreenX:
                                        ch_d "Ладно, надеюсь на это."
                                elif Girl is WandaX:
                                        ch_w "Что ж, ладно."
                        else:
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        ch_r "Ага, конечно. Я не куплюсь на эту чушь, [Girl.Petname]."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Ага[Girl.like]нашла дурочку... нет, спасибо, [Girl.Petname]."
                                        else:
                                            ch_k "Ага[Girl.like]нашел дурочку... нет, спасибо, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        ch_e "Да-да, так я тебе и поверила."
                                elif Girl is LauraX:
                                        if not Player.Male:
                                            ch_l "У тебя был шанс, но ты его упустила."
                                        else:
                                            ch_l "У тебя был шанс, но ты его упустил."
                                elif Girl is JeanX:
                                        ch_j "Я на это не куплюсь."
                                elif Girl is StormX:
                                        ch_s "Что ж, пожалуй, хватит с тебя обещаний."
                                elif Girl is JubesX:
                                        ch_v "Ну-ну..."
                                elif Girl is GwenX:
                                        ch_g "Попробуй придумать что-нибудь получше."
                                elif Girl is BetsyX:
                                        ch_b "Это лишь слова..."
                                elif Girl is DoreenX:
                                        ch_d "Я в этом сомневаюсь."
                                elif Girl is WandaX:
                                        ch_w "Ага, где-то я это уже слышала."
                                return
                "Ага, и что?":
                        if ApprovalCheck(Girl, 1400,Alt=[[EmmaX],1500]):
                                $ Girl.FaceChange("angry", Mouth = "grimace")
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Тебе повезло, что ты такая красивая."
                                        else:
                                            ch_r "Тебе повезло, что ты такой красивый."
                                elif Girl is KittyX:
                                        ch_k "Почему я[Girl.like]вообще терплю тебя?"
                                elif Girl is EmmaX:
                                        ch_e "Ценю твою уверенность."
                                        $ EmmaX.FaceChange("bemused")
                                        if not Player.Male:
                                            ch_e "Только не становись {i}слишком{/i} самоуверенной."
                                        else:
                                            ch_e "Только не становись {i}слишком{/i} самоуверенным."
                                elif Girl is LauraX:
                                        ch_l "Хмм, ладно."
                                elif Girl is JeanX:
                                        ch_j "Смело."
                                        ch_j "Ты заслуживаешь уважения."
                                elif Girl is StormX:
                                        ch_s "Смелости тебе не занимать, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "И что?! Нуу... значит..."
                                        ch_v "А, да пофиг."
                                elif Girl is GwenX:
                                        ch_g "Ага, ладно, все равно это деньги монополистов..."
                                elif Girl is BetsyX:
                                        ch_b "Ох, надеюсь, наше свидание не обойдется мне в кругленькую сумму..."
                                elif Girl is DoreenX:
                                        ch_d "Ох, ладно, расходы на мне..."
                                elif Girl is WandaX:
                                        ch_w "... Думаю, я могу заплатить еще один раз."
                                $ Girl.FaceChange("bemused")
                        elif ApprovalCheck(Girl, 500, "O",Alt=[[EmmaX],700]):
                                $ Girl.FaceChange("surprised")
                                call AnyLine(Girl,"...")
                                $ Girl.FaceChange("sad")
                                $ Girl.Statup("Obed", 80, 3)
                                if Girl is RogueX:
                                        ch_r "Я... думаю, я могу дать тебе еще один шанс..."
                                elif Girl is KittyX:
                                        ch_k "Хорошо, думаю, мы все еще можем повеселиться..."
                                elif Girl is EmmaX:
                                        ch_e "Хорошо, полагаю, я могу составить тебе компанию ненадолго..."
                                elif Girl is LauraX:
                                        ch_l "Если ты настаиваешь..."
                                elif Girl is JeanX:
                                        ch_j "Хмм... Ладно..."
                                elif Girl is StormX:
                                        ch_s "... Я дам тебе еще один шанс."
                                elif Girl is JubesX:
                                        ch_v "Думаю, можно попробовать снова..."
                                elif Girl is GwenX:
                                        ch_g "Будто у меня есть другие варианты."
                                elif Girl is BetsyX:
                                        ch_b "Ох, надеюсь, наше свидание не обойдется мне в кругленькую сумму..."
                                elif Girl is DoreenX:
                                        ch_d "Нууу... ладно."
                                elif Girl is WandaX:
                                        ch_w "... Думаю, я могу заплатить еще раз."
                        elif ApprovalCheck(Girl, 650):
                                $ Girl.FaceChange("angry")
                                $ Girl.Statup("Love", 80, -5)
                                $ Girl.Statup("Inbt", 60, 2)
                                if Girl is RogueX:
                                        ch_r "\"И что\"? Похоже, мы с тобой никуда не пойдем."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Ну ты и стерва, а я[Girl.like]еще собиралась на свидание с {i}тобой{/i}."
                                        else:
                                            ch_k "Ну да[Girl.like]и я собиралась на свидание с {i}тобой{/i}, гондон."
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Уверена, ты и сама знаешь мой ответ."
                                        else:
                                            ch_e "Уверена, ты и сам знаешь мой ответ."
                                elif Girl is LauraX:
                                        ch_l "И то, я больше никуда с тобой не пойду."
                                elif Girl is JeanX:
                                        ch_j "\"И что\"? Я найду кого-нибудь другого, кто заплатит за ужин."
                                elif Girl is StormX:
                                        ch_s "Что ж, в таком случае, тебе точно не придется платить за меня."
                                elif Girl is JubesX:
                                        ch_v "И что... становись лучше..."
                                elif Girl is GwenX:
                                        ch_g "И что... думаю, я лучше поем в одиночестве..."
                                elif Girl is BetsyX:
                                        ch_b "Твоя компания не стоит таких затрат..."
                                elif Girl is DoreenX:
                                        ch_d "Тогда, пожалуй, иди без меня."
                                elif Girl is WandaX:
                                        ch_w "... Тогда я могу сходить и одна."
                                return
                        else:
                                $ Girl.FaceChange("angry")
                                $ Girl.Statup("Love", 80, -10)
                                $ Girl.Statup("Obed", 80, -3)
                                $ Girl.Statup("Inbt", 60, 2)
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Да пошла ты."
                                        else:
                                            ch_r "Да пошел ты."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Сучка."
                                        else:
                                            ch_k "Мудак."
                                elif Girl is EmmaX:
                                        ch_e "Тебе лучше уйти."
                                elif Girl is LauraX:
                                        if not Player.Male:
                                            ch_l "Блядь."
                                        else:
                                            ch_l "Чмо."
                                elif Girl is JeanX:
                                        $ Girl.FaceChange("angry",1,Eyes="psychic")
                                        ch_j "..."
                                        $ Girl.FaceChange("angry",1)
                                elif Girl is StormX:
                                        ch_s "Поэтому, [Girl.Petname], ты будешь ужинать в одиночестве."
                                elif Girl is JubesX:
                                        ch_v "Неа..."
                                elif Girl is GwenX:
                                        if not Player.Male:
                                            ch_g "Ты получишь то, что заслужила!"
                                        else:
                                            ch_g "Ты получишь то, что заслужил!"
                                elif Girl is BetsyX:
                                        ch_b "Проваливай."
                                elif Girl is DoreenX:
                                        ch_d "Знаешь что? Я -не пойду- на свидание с тобой!"
                                elif Girl is WandaX:
                                        ch_w "Да иди ты..."
                                return
            $ Girl.Statup("Obed", 30, 3)
            $ Girl.Statup("Obed", 80, 2)
        #end "if stoodup or deadbeat"...
        elif ApprovalCheck(Girl, 650) or (ApprovalCheck(Girl, 400) and "friendly" in Girl.DailyActions):
                $ Girl.FaceChange("smile")
                if Girl is RogueX:
                        ch_r "Да, звучит неплохо. Скоро увидимся, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Конечно, скоро увидимся."
                elif Girl is EmmaX:
                        ch_e "Звучит заманчиво, увидимся, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Конечно, увидимся."
                elif Girl is JeanX:
                        ch_j "Ладно, не опаздывай."
                elif Girl is StormX:
                        ch_s "Тогда скоро увидимся, [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "Хорошо, тогда до встречи..."
                elif Girl is GwenX:
                        ch_g "Конечно."
                elif Girl is BetsyX:
                        ch_b "Хорошо, до скорой встречи."
                elif Girl is DoreenX:
                        ch_d "Хорошо, звучит весело!"
                elif Girl is WandaX:
                        ch_w "Конечно, звучит заманчиво."
        elif ApprovalCheck(Girl, 400):
                $ Girl.FaceChange("angry",Eyes = "side")
                if Girl is RogueX:
                        ch_r "У меня в планах на вечер помыть голову..."
                elif Girl is KittyX:
                        ch_k "У меня[Girl.like]есть дела поважнее..."
                elif Girl is EmmaX:
                        ch_e "Сегодня вечером мне нужно заняться кое-какой бумажной работой..."
                elif Girl is LauraX:
                        ch_l "У меня есть кое-какие дела..."
                elif Girl is JeanX:
                        ch_j "У меня есть планы на вечер и ты в них не входишь."
                elif Girl is StormX:
                        ch_s "Боюсь, я буду занята."
                elif Girl is JubesX:
                        ch_v "Думаю, у меня будут в это время кое-какие дела?"
                elif Girl is GwenX:
                        ch_g "Эм, я немного занята."
                elif Girl is BetsyX:
                        ch_b "Я буду занята..."
                elif Girl is DoreenX:
                        ch_d "У меня много дел."
                elif Girl is WandaX:
                        ch_w "Я так не думаю."
                return
        else:
                $ Girl.FaceChange("angry")
                if Girl is RogueX:
                        ch_r "Ага, ты этого хочешь, не я."
                elif Girl is KittyX:
                        ch_k "[Girl.Like]ни за что."
                elif Girl is EmmaX:
                        ch_e "Не представляю, зачем мне это."
                elif Girl is LauraX:
                        ch_l "Неа."
                elif Girl is JeanX:
                        ch_j "Ха! Ага, конечно."
                elif Girl is StormX:
                        ch_s "Я так не думаю."
                elif Girl is JubesX:
                        ch_v "Ни за что."
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "Ха, ладно, чувиха, это не по мне."
                        else:
                            ch_g "Ха, ладно, чувак, это не по мне."
                elif Girl is BetsyX:
                        ch_b "Я вынуждена отказаться."
                elif Girl is DoreenX:
                        ch_d "Эм, нет."
                elif Girl is WandaX:
                        ch_w "Ха! Нет."
                return

        $ Count = 0
        #She mostly agreed, do you ask for a double date?
        menu:
            "Хорошо, тогда встретимся на площади кампуса." if bg_current != "bg campus" or Time_Count < 2: #pre-evening time
                            $ Girl.FaceChange("smile")
            "Хорошо, тогда пошли." if bg_current == "bg campus" and Time_Count == 2: #evening time
                            $ Girl.FaceChange("smile")
            "И давай позовем...":
                        menu:
                            ch_p "И давай позовем..."
                            "[RogueX.Name_vin]." if Girl is not RogueX:
                                        $ Count = Girl.LikeRogue
                            "[KittyX.Name_vin]." if Girl is not KittyX and "met" in KittyX.History:
                                        $ Count = Girl.LikeKitty
                            "[EmmaX.Name_vin]." if Girl is not EmmaX and "met" in EmmaX.History:
                                        $ Count = Girl.LikeEmma
                            "[LauraX.Name_vin]." if Girl is not LauraX and "met" in LauraX.History:
                                        $ Count = Girl.LikeLaura
                            "[JeanX.Name_vin]." if Girl is not JeanX and "met" in JeanX.History:
                                        $ Count = Girl.LikeJean
                            "[StormX.Name_vin]." if Girl is not StormX and "met" in StormX.History:
                                        $ Count = Girl.LikeStorm
                            "[JubesX.Name_vin]." if Girl is not JubesX and "met" in JubesX.History:
                                        $ Count = Girl.LikeJubes
                            "[GwenX.Name_vin]." if Girl is not GwenX and "met" in GwenX.History:
                                        $ Count = Girl.LikeGwen
                            "[BetsyX.Name_vin]." if Girl is not BetsyX and "met" in BetsyX.History:
                                        $ Count = Girl.LikeBetsy
                            "[DoreenX.Name_vin]." if Girl is not DoreenX and DoreenX in ActiveGirls:
                                        $ Count = Girl.LikeDoreen
                            "[WandaX.Name_vin]." if Girl is not WandaX and WandaX in ActiveGirls:
                                        $ Count = Girl.LikeWanda
                            "Не обращай внимание, это была плохая идея.":
                                        $ Girl.FaceChange("confused")
                                        if Girl is RogueX:
                                                ch_r "Ладно..."
                                        elif Girl is KittyX:
                                                ch_k "Эм..."
                                        elif Girl is EmmaX:
                                                ch_e "Ясно..."
                                        elif Girl is LauraX:
                                                ch_l "Эм..."
                                        elif Girl is JeanX:
                                                ch_j "Эм... хм..."
                                        elif Girl is StormX:
                                                ch_s "Ох, хорошо."
                                        elif Girl is JubesX:
                                                ch_v "... ладно..."
                                        elif Girl is GwenX:
                                                ch_g "Пожалуй, можно..."
                                        elif Girl is BetsyX:
                                                ch_b "Конечно..."
                                        elif Girl is DoreenX:
                                                ch_d "Эм, ага."
                                        elif Girl is WandaX:
                                                ch_w "Не пугай меня приятным времяпрепровождением..."

                                        if bg_current != "bg campus":
                                                ch_p "Тогда встречаемся на площади кампуса."
        if Count:
            #If you asked about another girl...
            if Girl is WandaX and Count >= 500 and ApprovalCheck(Girl, 400, "I"):
                            $ Girl.FaceChange("sly")
                            ch_w "Конечно, звучит заманчиво..."
            elif (Count >= 600 and ApprovalCheck(Girl, 800, "OI")) or "friendly" in Girl.DailyActions: #Count is "Girl.LikeX"
                    $ Girl.FaceChange("smile")
                    if Girl is RogueX:
                            ch_r "Ох, ага, звучит неплохо."
                    elif Girl is KittyX:
                            ch_k "Конечно, будет весело."
                    elif Girl is EmmaX:
                            ch_e "Она была бы чудесной компанией."
                    elif Girl is LauraX:
                            ch_l "Конечно, чем больше, тем веселее... наверное."
                    elif Girl is JeanX:
                            ch_j "Наверное можно? Как хочешь."
                    elif Girl is StormX:
                            ch_s "Это может быть забавно."
                    elif Girl is JubesX:
                            ch_v "Ладно, звучит весело."
                    elif Girl is GwenX:
                            ch_g "Ха, ага."
                    elif Girl is BetsyX:
                            ch_b "Ох, она составит нам прекрасную компанию..."
                    elif Girl is DoreenX:
                            ch_d "О, ага, она веселая."
                    elif Girl is WandaX:
                            ch_w "Конечно, звучит заманчиво..."
            elif Count >= 750:
                    $ Girl.FaceChange("bemused")
                    if Girl is RogueX:
                            ch_r "Ох, классно..."
                    elif Girl is KittyX:
                            ch_k "Хм, ага..."
                    elif Girl is EmmaX:
                            ch_e "Мммм, у тебя хороший вкус..."
                    elif Girl is LauraX:
                            ch_l "Ладно..."
                    elif Girl is JeanX:
                            ch_j "Ох, хочешь удвоить удовольсвие?"
                    elif Girl is StormX:
                            ch_s "Она может... отвлекать."
                    elif Girl is JubesX:
                            ch_v "Нууу, ладно..."
                    elif Girl is GwenX:
                            ch_g "О, ради меня? Спасибо!"
                    elif Girl is BetsyX:
                            ch_b "Ох, она составит нам прекрасную компанию..."
                    elif Girl is DoreenX:
                            ch_d "Ох, ага, она очень веселая."
                    elif Girl is WandaX:
                            ch_w "Эм, думаю, я не против..."
            elif ApprovalCheck(Girl, 1300, "LO"):
                    $ Girl.FaceChange("sad")
                    if Girl is RogueX:
                            ch_r "Если тебе так хочется..."
                    elif Girl is KittyX:
                            ch_k "Думаю, можно, если тебе так этого хочется..."
                    elif Girl is EmmaX:
                            ch_e "Ох, если ты этого так хочешь..."
                    elif Girl is LauraX:
                            ch_l "Если ты настаиваешь..."
                    elif Girl is JeanX:
                            ch_j "Почему бы и нет?"
                    elif Girl is StormX:
                            ch_s "Не вижу причин отказать."
                    elif Girl is JubesX:
                            ch_v "... Наверное, можно?"
                    elif Girl is GwenX:
                            ch_g "Конечно... ладно."
                    elif Girl is BetsyX:
                            ch_b "Пожалуй, можно..."
                    elif Girl is DoreenX:
                            ch_d "Думаю, я не против... она веселая."
                    elif Girl is WandaX:
                            ch_w "Конечно, звучит заманчиво..."
            else:
                    $ Girl.FaceChange("angry")
                    if Girl is RogueX:
                            ch_r "Можешь не пытаться, я пас."
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Ну да, не сомневаюсь, что ты бы этого хотела!"
                            else:
                                ch_k "Ну да, не сомневаюсь, что ты бы этого хотел!"
                    elif Girl is EmmaX:
                            ch_e "Нет, не думаю, что готова к этому."
                    elif Girl is LauraX:
                            ch_l "Я в этом не учавствую."
                    elif Girl is JeanX:
                            ch_j "Уверена, ты этого не хочешь."
                            $ Girl.DailyActions.append("yesdate")
                    elif Girl is StormX:
                            ch_s "Меня это не устраивает."
                    elif Girl is JubesX:
                            ch_v "... меня это не устраивает."
                    elif Girl is GwenX:
                            ch_g "Ага, но я не готова."
                    elif Girl is BetsyX:
                            ch_b "Я бы предпочла, чтобы ее не было..."
                    elif Girl is DoreenX:
                            ch_d "Может, лучше не будем звать ее?"
                    elif Girl is WandaX:
                            $ Girl.FaceChange("sly")
                            ch_w "Ха, нет, спасибо..."
                    $ Count = 0
                    return
            $ Girl.DailyActions.append("yesdouble")
            if bg_current != "bg campus":
                    ch_p "Тогда встречаемся на площади кампуса."
            $ Count = 0

        if bg_current != "bg campus" or Time_Count < 2: #evening time
                if Girl is RogueX:
                        ch_r "Ага, увидимся!"
                elif Girl is KittyX:
                        ch_k "Ладно, увидимся!"
                elif Girl is EmmaX:
                        ch_e "Да, увидимся."
                elif Girl is LauraX:
                        ch_l "Ага."
                elif Girl is JeanX:
                        ch_j "Конечно."
                elif Girl is StormX:
                        ch_s "Увидимся."
                elif Girl is JubesX:
                        ch_v "Тогда до встречи!"
                elif Girl is GwenX:
                        ch_g "Ладно, увидимся!"
                elif Girl is BetsyX:
                        ch_b "До встречи..."
                elif Girl is DoreenX:
                        ch_d "Хорошо, увидимся!"
                elif Girl is WandaX:
                        ch_w "Ладно, увидимся на месте..."
        $ Girl.DailyActions.append("yesdate")
        $ Player.DailyActions.append("yesdate")
        return
#end AskDate / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Date_Stood_Up(Girl=0): #rkeljsvgb
    # if "stoodup" in Girl.Traits
    $ Event_Queue = [0,0]
    if Girl.Loc != bg_current:
            "[Girl.Name] врывается в комнату."
            $ Girl.Loc = bg_current
            call Display_Girl(Girl)
    else:
            "[Girl.Name] поворачивается к вам."
    $ Girl.FaceChange("confused")
    $ Girl.Statup("Love", 80, -10)
    if Girl is RogueX:
            if not Player.Male:
                ch_r "Почему ты не пришла на наше свидание?"
            else:
                ch_r "Почему ты не пришел на наше свидание?"
    elif Girl is KittyX:
            if not Player.Male:
                ch_k "Эй, ты не пришла на наше свидание! Ты можешь это как-то объяснить?!"
            else:
                ch_k "Эй, ты не пришел на наше свидание! Ты можешь это как-то объяснить?!"
    elif Girl is EmmaX:
            if not Player.Male:
                ch_e "Не могла бы ты объяснить, где ты была прошлым вечером?"
            else:
                ch_e "Не мог бы ты объяснить, где ты был прошлым вечером?"
    elif Girl is LauraX:
            if not Player.Male:
                ch_l "У нас были планы, но ты не пришла."
            else:
                ch_l "У нас были планы, но ты не пришел."
    elif Girl is JeanX:
            if not Player.Male:
                ch_j "Ты забыла прийти."
            else:
                ch_j "Ты забыл прийти."
    elif Girl is StormX:
            if not Player.Male:
                ch_s "Ты не явилась на нашу встречу."
            else:
                ch_s "Ты не явился на нашу встречу."
    elif Girl is JubesX:
            if not Player.Male:
                ch_v "Ты забыла о нашем свидании?"
            else:
                ch_v "Ты забыл о нашем свидании?"
    elif Girl is GwenX:
            if not Player.Male:
                ch_g "Забыла о нашем свидании?"
            else:
                ch_g "Забыл о нашем свидании?"
    elif Girl is BetsyX:
            if not Player.Male:
                ch_b "Ты что, забыла о нашей встрече?"
            else:
                ch_b "Ты что, забыл о нашей встрече?"
    elif Girl is DoreenX:
            if not Player.Male:
                ch_d "Ты что, забыла, что у нас было назначено свидание?"
            else:
                ch_d "Ты что, забыл, что у нас было назначено свидание?"
    elif Girl is WandaX:
            if not Player.Male:
                ch_w "Ты что, забыла? Ты так и не пришла..."
            else:
                ch_w "Ты что, забыл? Ты так и не пришел..."
    if "stoodup" in Girl.History:
            $ Girl.FaceChange("angry")
            $ Girl.Statup("Love", 80, -5)
            if Girl is RogueX:
                    ch_r "Снова!"
            elif Girl is KittyX:
                    ch_k "Снова!"
            elif Girl is EmmaX:
                    ch_e "И не в первый раз!"
            elif Girl is LauraX:
                    ch_l "Снова!"
            elif Girl is JeanX:
                    ch_j "Думаю, я вижу здесь какую-то закономерность."
            elif Girl is StormX:
                    ch_s "И это уже не в первый раз."
            elif Girl is JubesX:
                    ch_v "Это уже не в первый раз!"
            elif Girl is GwenX:
                    ch_g "Ты часто так делаешь!"
            elif Girl is BetsyX:
                    ch_b "Думаю, это уже можно назвать твоей привычкой..."
            elif Girl is DoreenX:
                    if not Player.Male:
                        ch_d "Ты прямо -очень- забывчивая..."
                    else:
                        ch_d "Ты прямо -очень- забывчивый..."
            elif Girl is WandaX:
                    ch_w "-это уже не в первый раз..."
    menu:
            extend ""
            "Ох, прости, как-то вылетело из головы.":
                if ApprovalCheck(Girl, 800, "LO") or ApprovalCheck(Girl, 1200):
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 80, 5)
                        if Girl is RogueX:
                                ch_r "Ну, по крайней мере, ты признаешь свои ошибки."
                        elif Girl is KittyX:
                                ch_k "Думаю, всякое может случиться, но не привыкай."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Хмм. Что ж, по крайней мере ты ответила честно."
                                else:
                                    ch_e "Хмм. Что ж, по крайней мере ты ответил честно."
                        elif Girl is LauraX:
                                ch_l "Пфф, ладно, я уж чуть было не порезала тебя."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Ты должна радоваться, что я не могу заставить тебя забыть свое имя."
                                else:
                                    ch_j "Ты должен радоваться, что я не могу заставить тебя забыть свое имя."
                        elif Girl is StormX:
                                ch_s "Извинение - хорошее начало."
                        elif Girl is JubesX:
                                ch_v "Ну... ладно..."
                        elif Girl is GwenX:
                                ch_g "Да, и?"
                        elif Girl is BetsyX:
                                ch_b "Ну, это едва ли все объясняет."
                        elif Girl is DoreenX:
                                ch_d "Ну, неплохое начало."
                        elif Girl is WandaX:
                                ch_w "Вижу, что ты очень переживаешь из-за этого..."
                        if "stoodup" in Girl.History:
                                $ Girl.FaceChange("sad",Eyes="side")
                                $ Girl.Statup("Obed", 80, 5)
                                if Girl is RogueX:
                                        ch_r "Тебе нужно привести свои мысли в порядок."
                                elif Girl is KittyX:
                                        ch_k "Тебе нужно правильно расставлять приорететы."
                                elif Girl is EmmaX:
                                        ch_e "Однако, тебе стоило придумать что-нибудь получше."
                                elif Girl is LauraX:
                                        ch_l "Разберись со своими планами."
                                elif Girl is StormX:
                                        ch_s "Придумал бы что-нибудь получше."
                                elif Girl is JubesX:
                                        ch_v "Просто перестань так делать."
                                elif Girl is GwenX:
                                        ch_g "Извинения лишь все усугубляют."
                                elif Girl is BetsyX:
                                        ch_b "Тебе нужно стараться стать лучше..."
                                elif Girl is DoreenX:
                                        ch_d "-но ты не можешь продолжать пропускать такие важные встречи, как наша."
                                elif Girl is WandaX:
                                        ch_w "Это не может продолжаться и дальше..."
                elif "stoodup" in Girl.History:
                        $ Girl.FaceChange("sad",Eyes="side")
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.Statup("Obed", 80, 5)
                        if Girl is RogueX:
                                ch_r "Тебе нужно разобраться в себе!"
                        elif Girl is KittyX:
                                ch_k "Тебе нужно правильно расставлять приорететы."
                        elif Girl is EmmaX:
                                ch_e "Что ж, тебе нужно перестать юлить."
                        elif Girl is LauraX:
                                ch_l "Разберись со своими планами."
                        elif Girl is JeanX:
                                ch_j "Похоже, у тебя это вошло в привычку..."
                        elif Girl is StormX:
                                ch_s "Тебе следует изменить свои привычки"
                        elif Girl is JubesX:
                                ch_v "Тебе нужно перестать так делать."
                        elif Girl is GwenX:
                                $ GwenX.ArmPose = 1
                                ch_g "У тебя есть вся информация на экране!"
                                $ GwenX.ArmPose = 2
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ты заставила меня долго ждать, и все в пустую..."
                                else:
                                    ch_b "Ты заставил меня долго ждать, и все в пустую..."
                        elif Girl is DoreenX:
                                ch_d "Я так долго ждала тебя..."
                        elif Girl is WandaX:
                                ch_w "Это не может продолжаться и дальше..."
                else:
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Obed", 80, -2)
                        $ Girl.Statup("Inbt", 60, 2)
                        if Girl is RogueX:
                                ch_r "Одного \"прости\" в следующий раз будет мало."
                        elif Girl is KittyX:
                                ch_k "В следующий раз тебе придётся хорошо постараться, чтобы загладить свою вину."
                        elif Girl is EmmaX:
                                ch_e "В следующий раз простых извинений может быть недостаточно."
                                ch_e "Если вообще будет следующий раз."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "На этот раз ты встряла."
                                else:
                                    ch_l "На этот раз ты встрял."
                        elif Girl is JeanX:
                                ch_j "Со мной это не пройдет!"
                        elif Girl is StormX:
                                ch_s "Ты будешь у меня в долгу, если будет следующий раз."
                        elif Girl is JubesX:
                                ch_v "В следующий раз исправляйся."
                        elif Girl is GwenX:
                                ch_g "Серьезно, разберись уже с собой!"
                        elif Girl is BetsyX:
                                ch_b "Я не буду долго этого терпеть..."
                        elif Girl is DoreenX:
                                ch_d "Я так долго ждала тебя!"
                        elif Girl is WandaX:
                                ch_w "Это не может продолжаться и дальше..."
            # end "sorry"

            "Это невозможно! Может ты что-то перепутала?":
                if Girl is GwenX:
                        ch_g "Секундочку..."
                        hide Gwen_Sprite  with easeoutright
                        "..."
                        $ Girl.Statup("Inbt", 70, 10)
                        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) with easeinleft
                        ch_g "Нет, я точно не ошиблась."
                        if ApprovalCheck(Girl, 700, "L"):
                                ch_g "Хотя меня развеселила твоя попытка выкрутиться..."
                        elif ApprovalCheck(Girl, 700, "O"):
                                ch_g "Десять очков тебе за попытку..."
                        else:
                                $ Girl.FaceChange("angry")
                                $ Girl.RecentActions.append("angry")
                                $ Girl.DailyActions.append("angry")
                                $ Girl.Statup("Love", 80, -10)
                                $ Girl.Statup("Obed", 80, -5)
                                ch_g "Это не прикольно..."
                elif "stoodup" in Girl.History and ApprovalCheck(Girl, 800, "O",Alt=[[EmmaX],900]):
                        $ Girl.FaceChange("confused")
                        $ Girl.Statup("Obed", 90, 15)
                        if Girl is RogueX:
                                ch_r "Что?... Нет, я уверена..."
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_r "Хм."
                        elif Girl is KittyX:
                                ch_k "Ты... я была уверена, что я..."
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_k "Хм."
                        elif Girl is EmmaX:
                                ch_e "Что?... Нет, мы определенно..."
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_e "Хм."
                        elif Girl is LauraX:
                                ch_l "Я не думаю... я почти уверена..."
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_l "Хм."
                        elif Girl is JeanX:
                                $ Girl.FaceChange("confused")
                                ch_j "Хмм..."
                                $ Girl.FaceChange("sly")
                                ch_j "Нет, это невозможно."
                                ch_j "Если я так считаю, то так оно и есть."
                        elif Girl is StormX:
                                ch_s "Что?.. это... маловероятно..."
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_s "Хм."
                        elif Girl is JubesX:
                                ch_v "Хм?... ну..."
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_v "... возможно..."
                        elif Girl is BetsyX:
                                ch_b "Что?"
                                ch_b "..."
                                ch_b "Я была абсолютно уверена, что мы планировали сходить куда-нибудь..."
                        elif Girl is DoreenX:
                                if not Player.Male:
                                    ch_d "Что? Ты уверена?"
                                else:
                                    ch_d "Что? Ты уверен?"
                                ch_d "Пожалуй, это возможно."
                                ch_d "Наверное..."
                        elif Girl is WandaX:
                                ch_w "Я..."
                                ch_w "Этого не может быть..."
                elif ApprovalCheck(Girl, 700, "O",Alt=[[EmmaX],800]):
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Obed", 80, 5)
                        $ Girl.Statup("Obed", 90, 10)
                        if Girl is RogueX:
                                ch_r "Нет... мы определенно..."
                        elif Girl is KittyX:
                                ch_k "Эм... я так не думаю, но это возможно..."
                        elif Girl is EmmaX:
                                ch_e "Нет... мы определенно..."
                        elif Girl is LauraX:
                                ch_l "... Я так не думаю, но это возможно..."
                        elif Girl is JeanX:
                                ch_j "Хорошая попытка!"
                        elif Girl is StormX:
                                ch_s "Не пытайся сбить меня с толку."
                        elif Girl is JubesX:
                                ch_v "Со мной это не сработает!"
                        elif Girl is BetsyX:
                                ch_b "У меня нет никакого желание играть в такие игры..."
                        elif Girl is DoreenX:
                                ch_d "Я... так не думаю..."
                        elif Girl is WandaX:
                                if not Player.Male:
                                    ch_w "... Я почти уверена, что забыла тут именно ты..."
                                else:
                                    ch_w "... Я почти уверена, что забыл тут именно ты..."
                elif Girl is WandaX:
                        $ Girl.FaceChange("sad")
                        $ Girl.Statup("Obed", 80, 5)
                        if not Player.Male:
                            ch_w "... Я почти уверена, что забыла тут именно ты..."
                        else:
                            ch_w "... Я почти уверена, что забыл тут именно ты..."
                elif Girl is EmmaX and not ApprovalCheck(Girl, 700, "L"):
                        $ Girl.FaceChange("angry")
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                        $ Girl.Statup("Love", 80, -10)
                        $ Girl.Statup("Obed", 80, -5)
                        $ Girl.Statup("Inbt", 70, 10)
                        ch_e "Не пытайся провернуть такое со мной, [Girl.Petname]!"
                        ch_e "Я всю жизнь МАНИПУЛИРУЮ чужими сознаниями."
                elif Girl is not EmmaX and ApprovalCheck(Girl, 500, "I"):
                        $ Girl.FaceChange("angry")
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                        $ Girl.Statup("Love", 80, -10)
                        $ Girl.Statup("Inbt", 70, 10)
                        if Girl is RogueX:
                                ch_r "Не пытайся провернуть это со мной!"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Попробуй придумать что-нибудь получше, дура."
                                else:
                                    ch_k "Попробуй придумать что-нибудь получше, придурок."
                        elif Girl is LauraX:
                                ch_l "Ага, конечно."
                        elif Girl is JeanX:
                                ch_j "Хорошая попытка!"
                        elif Girl is StormX:
                                ch_s "Мог бы придумать что-нибудь получше."
                        elif Girl is JubesX:
                                ch_v "Не может такого быть."
                        elif Girl is BetsyX:
                                ch_b "Не стоит играть со мной в такие игры..."
                        elif Girl is DoreenX:
                                ch_d "Я... так не думаю!"
                else:
                        $ Girl.FaceChange("sad",Eyes="side")
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.Statup("Obed", 80, -5)
                        $ Girl.Statup("Inbt", 60, 5)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Я сомневаюсь, лучше подумала бы как получше извиниться."
                                else:
                                    ch_r "Я сомневаюсь, лучше подумал бы как получше извиниться."
                        elif Girl is KittyX:
                                ch_k "Ну... Я так не думаю, перестань меня беспокоить."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Ох, [Girl.Petname], ты могла бы придумать что-нибудь получше."
                                else:
                                    ch_e "Ох, [Girl.Petname], ты мог бы придумать что-нибудь получше."
                        elif Girl is LauraX:
                                ch_l "Нет, я на это не куплюсь."
                        elif Girl is JeanX:
                                ch_j "Неееет."
                        elif Girl is StormX:
                                ch_s "Это не так."
                        elif Girl is JubesX:
                                ch_v "Неа."
                        elif Girl is BetsyX:
                                ch_b "Я абсолюно уверена, что мы договаривались встретиться..."
                        elif Girl is DoreenX:
                                ch_d "У меня свидание даже записано в моем ежедневнике!"
            #end "gaslight"

            "У меня были занятия получше.":
                if ApprovalCheck(Girl, 1200, "LO"):
                        $ Girl.FaceChange("sad",Eyes="side")
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.Statup("Obed", 80, 5)
                        if Girl is RogueX:
                                if "stoodup" in Girl.History:
                                        ch_r "Ох... "
                                        ch_r "Ну, это твой выбор..."
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_r "Ох... "
                                        ch_r "только не делай так снова."
                        elif Girl is KittyX:
                                if "stoodup" in Girl.History:
                                        ch_k "Ага... "
                                        if not Player.Male:
                                            ch_k "Ты всегда такая..."
                                        else:
                                            ch_k "Ты всегда такой..."
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_k "Хорошо... "
                                        ch_k "не дай этому повториться."
                        elif Girl is EmmaX:
                                if "stoodup" in Girl.History:
                                        ch_e "Ох... "
                                        ch_e "Эта твоя своевольность начинает утомлять..."
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_e "Ох... "
                                        ch_e "не искушай судьбу."
                        elif Girl is LauraX:
                                if "stoodup" in Girl.History:
                                        ch_l "Ага... "
                                        ch_l "Так похоже на тебя..."
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_l "Хм... "
                                        ch_l "Ну, не делай так больше."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Мы обе знаем, что это невозможно."
                                else:
                                    ch_j "Мы оба знаем, что это невозможно."
                                if "stoodup" not in Girl.History:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_j "Больше так не делай."
                        elif Girl is StormX:
                                if "stoodup" in Girl.History:
                                        ch_s "Похоже, это вошло у тебя в привычку..."
                                else:
                                        ch_s "Я и представить не могла, что такое возможно."
                        elif Girl is JubesX:
                                if "stoodup" in Girl.History:
                                        ch_v "Ага, нууу..."
                                        ch_v "У меня тоже есть дела поважнее..."
                                else:
                                        ch_v "Ага, нууу..."
                                        ch_v "... не делай так снова!"
                        elif Girl is GwenX:
                                if "stoodup" in Girl.History:
                                        ch_g "Такое часто случается, да?"
                                else:
                                        ch_g "Ну... перестань."
                        elif Girl is BetsyX:
                                if "stoodup" in Girl.History:
                                        ch_b "По-видимому, это часто бывает..."
                                else:
                                        ch_b "Я не уверена, как к этому отнестись..."
                        elif Girl is DoreenX:
                                if "stoodup" in Girl.History:
                                        ch_d "Это... не лучший ответ!"
                                else:
                                        ch_d "Я... вроде бы, понимаю?.."
                        elif Girl is WandaX:
                                if "stoodup" in Girl.History:
                                        ch_w "Это стало последней каплей!"
                                else:
                                        ch_w "Ну-ну.."
                elif ApprovalCheck(Girl, 800, "LO"):
                        $ Girl.FaceChange("angry",Eyes="side")
                        $ Girl.Statup("Love", 80, -10)
                        $ Girl.Statup("Obed", 80, 20)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Могла бы придумать что-нибудь помягче."
                                else:
                                    ch_r "Мог бы придумать что-нибудь помягче."
                        elif Girl is KittyX:
                                ch_k "Так грубо."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Полагаю, лучше бы ты что-нибудь придумала."
                                else:
                                    ch_e "Полагаю, лучше бы ты что-нибудь придумал."
                        elif Girl is LauraX:
                                ch_l "Эм."
                        elif Girl is JeanX:
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_j "Этого не может быть..."
                                ch_j "Или может?.."
                                $ Girl.FaceChange("sly",Eyes="side")
                                ch_j "Да, наверное, все таки может."
                        elif Girl is StormX:
                                ch_s "Это не оправдание."
                        elif Girl is JubesX:
                                ch_v "Да кого это волнует?!"
                        elif Girl is GwenX:
                                ch_g "Ауч."
                        elif Girl is BetsyX:
                                ch_b "Что ж, это было довольно грубо с твоей стороны..."
                        elif Girl is DoreenX:
                                ch_d "Это... было грубо..."
                        elif Girl is WandaX:
                                ch_w "Что ж, я это запомню!"
                else:
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 80, -15)
                        $ Girl.Statup("Inbt", 60, 5)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ох, да пошла ты."
                                else:
                                    ch_r "Ох, да пошел ты."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Стерва."
                                else:
                                    ch_k "Мудак."
                        elif Girl is EmmaX:
                                ch_e "Что ж, полагаю, тогда и у меня нет времени на тебя."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Пизда."
                                else:
                                    ch_l "Уебок."
                        elif Girl is JeanX:
                                ch_j "Невозможно."
                        elif Girl is StormX:
                                ch_s "Не пытайся повторить."
                        elif Girl is JubesX:
                                ch_v "Не может такого быть."
                        elif Girl is GwenX:
                                ch_g "Как и у меня!"
                        elif Girl is BetsyX:
                                ch_b "Тогда мне придется сделать то же самое!"
                        elif Girl is DoreenX:
                                ch_d "Как грубо!"
                        elif Girl is WandaX:
                                if not Player.Male:
                                    ch_w "Ну и пошла ты тогда!"
                                else:
                                    ch_w "Ну и пошел ты тогда!"
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
            #end "something better to do"

    $ Girl.Traits.remove("stoodup")
    if "stoodup" not in Girl.History:
            $ Girl.History.append("stoodup")

    return

# End Ask Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Readytogo(Girl=0,R=0,BO=[]):  #rkeljsvgb
    #checks to see if you want to go on a date
    if Girl in TotalGirls and "yesdate" in Girl.DailyActions:
            #if a girl was sent and she has a date
            $ R = Girl
    else:
            $ BO = TotalGirls[:]
            python:
                for BX in BO:
                    if BX.Loc == bg_current and "yesdate" in BX.DailyActions:
                            R = BX
                            break
    if R not in TotalGirls:
            #if nobody was found...
            return

    if R.Loc != bg_current:
            # if the girl you have a date with isn't the one you're talking to...
            "Вам, наверное, стоит отправиться на это свидание."
    elif R is RogueX:
            if not Player.Male:
                ch_r "Готова идти?"
            else:
                ch_r "Готов идти?"
    elif R is KittyX:
            ch_k "Идем?"
    elif R is EmmaX:
            ch_e "Нам пора идти."
    elif R is LauraX:
            if not Player.Male:
                ch_l "Готова?"
            else:
                ch_l "Готов?"
    elif R is JeanX:
            ch_j "Пошли."
    elif R is StormX:
            ch_s "Тогда идем?"
    elif R is JubesX:
            if not Player.Male:
                ch_v "Готова идти?"
            else:
                ch_v "Готов идти?"
    elif R is GwenX:
            if not Player.Male:
                ch_g "Ладно, готова?"
            else:
                ch_g "Ладно, готов?"
    elif R is BetsyX:
            ch_b "Мы идем?"
    elif R is DoreenX:
            if not Player.Male:
                ch_d "Готова идти?"
            else:
                ch_d "Готов идти?"
    elif R is WandaX:
            if not Player.Male:
                ch_w "Готова идти?"
            else:
                ch_w "Готов идти?"
    else:
            "Отправиться на свидание?"
    menu:
        extend ""
        "Да":
                $ renpy.pop_call() #removes call to ReadytoGo
                $ renpy.pop_call() #removes call to Chat
                jump Campus_Entry
        "Позже":
                if R is RogueX:
                        ch_r "Ладно, хотя уже довольно поздно."
                elif R is KittyX:
                        ch_k "Ладно."
                elif R is EmmaX:
                        ch_e "Хорошо, но нам не стоит опаздывать."
                elif R is LauraX:
                        ch_l "Хорошо, но поторопись."
                elif R is JeanX:
                        ch_j "Я дам тебе минутку."
                elif R is StormX:
                        ch_s "Сильно не задерживайся."
                elif R is JubesX:
                        ch_v "Ладно, просто дай мне знать, когда будешь готов."
                elif R is GwenX:
                        ch_g "Лаааадно... Я могу немного подождать."
                elif R is BetsyX:
                        ch_b "Хорошо, но не задерживайся."
                elif R is DoreenX:
                        if not Player.Male:
                            ch_d "Хорошо, скажи, когда будешь готова..."
                        else:
                            ch_d "Хорошо, скажи, когда будешь готов..."
                elif R is WandaX:
                        ch_w "Хорошо, я могу подождать несколько минут."
                else:
                        "Как пожелаете."
        "Давай отменим наше свидание и просто проведем время вместе в кампусе. [[Местность переполнена] (locked)" if R and R.Loc != bg_current and Room_Full():
                pass
        "Давай отменим наше свидание и просто проведем время вместе в кампусе." if R and not Room_Full():
                #won't work if the room is full.
                if R is RogueX:  #Checks if Rogue is in
                        ch_r "Ага, хорошо, все в порядке."
                elif R is KittyX:
                        ch_k "Ага, ладно."
                elif R is EmmaX:
                        ch_e "Как хочешь."
                elif R is LauraX:
                        ch_l "Ладно, как скажешь."
                elif R is JeanX:
                        ch_j "Что?"
                        ch_j "Ладно?"
                elif R is StormX:
                        ch_s "... Хорошо."
                elif R is JubesX:
                        ch_v "Нууу... ладно?"
                elif R is GwenX:
                        ch_g "Ладно, как скажешь."
                elif R is BetsyX:
                        ch_b "Что ж... Думаю, можно."
                elif R is DoreenX:
                        ch_d "Ох, эм, ладно..."
                elif R is WandaX:
                        ch_w "Эм?..  Если это необходимо..."
                $ R.DailyActions.remove("yesdate")

                if R.Loc != bg_current:
                        # brings her if she wasn't already there
                        $ R.RecentActions.append("summoned")
                        $ Line = 0
                        if "locked" in Player.Traits:
                                call Locked_Door(R)
                                return
                        $ R.Loc = bg_current
                        call Taboo_Level(0)
                        $ R.OutfitChange()
                        call Set_The_Scene
    return


# Date Night //////////////////////////////////////////////////////////////////////
# Gets called from the Events whenever "yesdate" in Player.DailyActions
# Checks to see which girls show up, if more than one, they decide whether they are cool with that.
# If they are, you choose location. можешь идти to dinner first, or skip to movies.
# During dinner there is a check to menu, then a check to whether sexy stuff occurs
# During sexy stuff, the other girl can join in, ignore it, to cockblock it.
# Then you pay, during which you can cause offense by being cheap.
# Then you can pick a movie, and pay for that too, similar to dinner.
# Then you watch the movie and potentially have sex, and again the other girl can object.
# Then you return to campus, and can pick a girl to take home first, the other will follow.

label DateNight(Date_Bonus=[0,0],Play_Cost=0,Date_Cost=[0,0],BO=[]):  #rkeljsvgb
    #(nee Prime_Bonus=0,Second_Bonus=0,Play_Cost=0,Prime_Cost=0,Second_Cost=0,BO=[]):
    # Called from the event menu
    # Party[0] is the lead girl Party[1] the other.
    # Primary_Bonus and Secondary_Bonus track the girl's love bonuses, Cost is cost of the date

    $ Party = [] #clears Party if there is one

    $ BO = ActiveGirls[:]
    python:
        for BX in BO:
            if "yesdate" in BX.DailyActions:  #Checks if which girls are in
                Party.append(BX)
                BX.DailyActions.remove("yesdate")

    if not Party:
            "Никто не появился, странно."
            return

    $ renpy.random.shuffle(Party)

    while len(Party) > 2:
            # If two or more members in the party
            #Culls down party size to two
            $ Party.remove(Party[2])


    # This portion sets the girls' clothing and mood for the date

    $ BO = Party[:]
    python:
        for BX in BO:
            if "stoodup" in BX.History:
                        BX.History.remove("stoodup")
            #This gets the girl Dressed and ready for Dinner, called by Date_Night
            BX.Taboo = 40
            if BX.Clothing[7]:
                    # if she has a date outfit set
                    if BX.Clothing[7] == 2:
                            BX.Outfit = "casual2"
                    elif BX.Clothing[7] == 3:
                            BX.Outfit = "custom1"
                    elif BX.Clothing[7] == 4:
                            BX.Outfit = "gym"
                    elif BX.Clothing[7] == 5:
                            BX.Outfit = "custom2"
                    elif BX.Clothing[7] == 6:
                            BX.Outfit = "custom3"
                    else:
                            BX.Outfit = "casual1"
            else:
                    Options = ["casual2", "casual1"]
                    Options.append("custom1") if BX.Custom1[0] == 2 else Options
                    Options.append("custom2") if BX.Custom2[0] == 2 else Options
                    Options.append("custom3") if BX.Custom3[0] == 2 else Options
                    renpy.random.shuffle(Options)
                    BX.Outfit = Options[0]
                    del Options[:]
            BX.Loc = "date"
            BX.OutfitChange(Changed=1)
            BX.FaceChange("smile")
    #end Date prep loop
    $ Taboo = 40

    $ bg_current = "date"
    $ Player.AddWord(1,"date") #recent
    call Shift_Focus(Party[0])
    call Set_The_Scene

    if len(Party) >= 2:
        "По прибытии, вы видите, что [Party[0].Name] и [Party[1].Name_tvo] ожидают вас."
        call Date_Crossed
        if not Party:
                # both left
                return
        elif len(Party) < 2:
                # One stayed, but not both
                ch_p "Ладно, думаю, нам пора идти..."
    else:
                "По прибытии, вы видите, что [Party[0].Name] ожидает вас."
    if Round <= 60:
            #kept waiting
            $ Party[0].Statup("Love", 90, -3)
            $ Party[0].Statup("Obed", 50, 2)
            $ Party[0].Statup("Obed", 70, 1)
            $ Party[0].FaceChange("angry")
            if len(Party) >= 2:
                    $ Party[1].Statup("Love", 90, -3)
                    $ Party[1].Statup("Obed", 50, 2)
                    $ Party[1].Statup("Obed", 70, 1)
                    $ Party[1].FaceChange("angry")
            if Party[0] is RogueX:
                    if not Player.Male:
                        ch_r "Ты заставила меня ждать, [Party[0].Petname]!"
                    else:
                        ch_r "Ты заставил меня ждать, [Party[0].Petname]!"
            elif Party[0] is KittyX:
                    if not Player.Male:
                        ch_k "Так вот, ты[KittyX.like]заставила меня ждать..."
                    else:
                        ch_k "Так вот, ты[KittyX.like]заставил меня ждать..."
            elif Party[0] is EmmaX:
                    ch_e "Ты не думаешь, что у меня есть дела поважнее, чем ждать тебя?"
            elif Party[0] is LauraX:
                    ch_l "Почему ты так долго?"
            elif Party[0] is JeanX:
                    $ Party[0].Statup("Obed", 70, 2)
                    if not Player.Male:
                        ch_j "Ты должна была быть здесь несколько часов назад!"
                    else:
                        ch_j "Ты должен был быть здесь несколько часов назад!"
            elif Party[0] is StormX:
                    if not Player.Male:
                        ch_s "Если ты собиралась опоздать, тебе следовало предупредить меня."
                    else:
                        ch_s "Если ты собирался опоздать, тебе следовало предупредить меня."
            elif Party[0] is JubesX:
                    ch_v "Эй, что за задержка?"
            elif Party[0] is GwenX:
                    if not Player.Male:
                        ch_g "Ты опоздала, опоздала на очень важное свидание!"
                    else:
                        ch_g "Ты опоздал, опоздал на очень важное свидание!"
            elif Party[0] is BetsyX:
                    if not Player.Male:
                        ch_b "Ты заставила меня ждать..."
                    else:
                        ch_b "Ты заставил меня ждать..."
            elif Party[0] is DoreenX:
                    if not Player.Male:
                        ch_d "Ого, ты опоздала, у тебя все хорошо?"
                    else:
                        ch_d "Ого, ты опоздал, у тебя все хорошо?"
            elif Party[0] is WandaX:
                    if not Player.Male:
                        ch_w "Ты опоздала."
                    else:
                        ch_w "Ты опоздал."
            menu:
                "Извини, так получилось!":
                        $ Party[0].Statup("Love", 70, 1)
                        $ Party[0].Statup("Love", 90, 1)
                        $ Party[0].FaceChange("normal")
                        if len(Party) >= 2:
                                $ Party[1].Statup("Love", 70, 1)
                                $ Party[1].Statup("Love", 90, 1)
                                $ Party[1].FaceChange("normal")
                        call AnyLine(Party[0],"Не дай этому повториться.")
                "Я потеряла счет времени." if not Player.Male:
                        $ Party[0].Statup("Love", 70, -1)
                        $ Party[0].Statup("Love", 90, -1)
                        $ Party[0].Statup("Obed", 50, 1)
                        if len(Party) >= 2:
                                $ Party[1].Statup("Love", 70, -1)
                                $ Party[1].Statup("Love", 90, -1)
                                $ Party[1].Statup("Obed", 50, 1)
                        call AnyLine(Party[0],"Ну, тогда и не приходила!")
                "Я потерял счет времени." if Player.Male:
                        $ Party[0].Statup("Love", 70, -1)
                        $ Party[0].Statup("Love", 90, -1)
                        $ Party[0].Statup("Obed", 50, 1)
                        if len(Party) >= 2:
                                $ Party[1].Statup("Love", 70, -1)
                                $ Party[1].Statup("Love", 90, -1)
                                $ Party[1].Statup("Obed", 50, 1)
                        call AnyLine(Party[0],"Ну, тогда и не приходил!")
                "Мне нужно было кое с чем разобраться.":
                        $ Party[0].Statup("Love", 70, -1)
                        $ Party[0].Statup("Love", 90, -2)
                        $ Party[0].Statup("Obed", 50, 1)
                        $ Party[0].Statup("Obed", 70, 1)
                        if len(Party) >= 2:
                                $ Party[1].Statup("Love", 70, -1)
                                $ Party[1].Statup("Love", 90, -2)
                                $ Party[1].Statup("Obed", 50, 1)
                                $ Party[1].Statup("Obed", 70, 1)
                        call AnyLine(Party[0],"Это не оправдание!")
    # end if Round <= 60:

    if Round <= 25:
            #no time
            $ Party[0].Statup("Love", 90, -3)
            $ Party[0].Statup("Obed", 50, 1)
            $ Party[0].FaceChange("angry")
            if len(Party) >= 2:
                    $ Party[1].Statup("Love", 90, -3)
                    $ Party[1].Statup("Obed", 50, 1)
                    $ Party[1].FaceChange("angry")
            call AnyLine(Party[0],"Похоже, сегодня у нас уже нет времени ни на что!")
            if Party[0] is RogueX:
                    ch_r "Ну и зачем я вообще прихорашивалась?"
            elif Party[0] is KittyX:
                    ch_k "[KittyX.Like]у тебя обычно так проходят свидания?"
            elif Party[0] is EmmaX:
                    ch_e "Зря только потратила свое время."
            elif Party[0] is LauraX:
                    ch_l "М-да."
            elif Party[0] is JeanX:
                    $ Party[0].Statup("Obed", 70, 2)
                    if not Player.Male:
                        ch_j "Ты что, просто так потратила мое время?"
                    else:
                        ch_j "Ты что, просто так потратил мое время?"
            elif Party[0] is StormX:
                    ch_s "Терпеть не могу, когда тратят мое время впустую."
            elif Party[0] is JubesX:
                    ch_v "Бессмысленная потеря времени..."
            elif Party[0] is GwenX:
                    ch_g "М-да. Как будто и не было причин прихорашиваться..."
            elif Party[0] is BetsyX:
                    ch_b "Вечер потрачен впустую, [Party[0].Petname]..."
            elif Party[0] is DoreenX:
                    $ Party[0].FaceChange("sad")
                    ch_d "Уже так поздно, даже не успеть сделать ничего полезного..."
            elif Party[0] is WandaX:
                    ch_w "Мы не успеем даже ничем заняться до закрытия торгового центра."
            if len(Party) >= 2:
                    "Девушки уходят."
            else:
                    "[Party[0].Tag] уходит."
            call Remove_Girl("All")
            $ bg_current = "bg campus"
            $ Player.DrainWord("date") #recent
            $ Player.DrainWord("yesdate") #recent
            return
    #end if Round <= 25:

    $ Line = 0
    if JeanX in Party and "dinner" not in Player.RecentActions:
        ch_j "Мы идем ужинать."
        menu:
            "Хорошо.":
                    $ Line = "dinner"

            "А потом в кино?":
                    $ Line = "dinner"
                    if ApprovalCheck(JeanX, 500, "LO"):
                            ch_j "Конечно, если ты хочешь, потом пойдем в кино."
                    else:
                            ch_j "Я не хочу тратить весь вечер на тебя."

            "Нет, мы идем за покупками." if "mall" in Player.History:
                    if ApprovalCheck(JeanX, 700, "LO"):
                            ch_j "Ладно, хорошо, за покупками так за покупками."
                            $ Line = "shopping"
                    else:
                            ch_j "Что ж, это было короткое свидание."
                            call Girl_Date_Over(JeanX)
                            #if only girl, quit?

            "Нет, мы идем только в кино.":
                    if ApprovalCheck(JeanX, 700, "LO"):
                            ch_j "Ладно-ладно, кино так кино."
                            $ Line = "movie"
                    else:
                            ch_j "Что ж, это было короткое свидание."
                            call Girl_Date_Over(JeanX)
                            #if only girl, quit?

    if Line:
            #if Jean picked
            pass
    else:
            #if Jean didn't pick
            if Party[0] is RogueX:
                    ch_r "Куда мы идем?"
            elif Party[0] is KittyX:
                    ch_k "Так что[KittyX.like]куда пойдем?"
            elif Party[0] is EmmaX:
                    ch_e "У тебя есть местечко на примете?"
            elif Party[0] is LauraX:
                    ch_l "Куда мы направляемся?"
            elif Party[0] is JeanX:
                    ch_j "Так что, куда идем?"
            elif Party[0] is StormX:
                    ch_s "Куда тогда пойдем?"
            elif Party[0] is JubesX:
                    ch_v "Ладно, куда идем?"
            elif Party[0] is GwenX:
                    ch_g "Ну и чем у вас здесь можно заняться?"
            elif Party[0] is BetsyX:
                    ch_b "Куда собираешься сводить меня?"
            elif Party[0] is DoreenX:
                    ch_d "Куда пойдем?"
            elif Party[0] is WandaX:
                    ch_w "Веди..."

            menu Date_Location:
                extend ""
                "В ресторан." if "dinner" not in Player.RecentActions and Round >= 20:
                        $ Line = "dinner"
                "В ресторан. (locked)" if "dinner" in Player.RecentActions or Round <=20:
                        $ Line = "dinner"

                "Пройдемся по магазинам." if "shopping" not in Player.RecentActions and Round >= 20 and "mall" in Player.History:
                        $ Line = "shopping"
                "Пройдемся по магазинам. (locked)" if ("shopping" in Player.RecentActions or Round < 20) and "mall" in Player.History:
                        $ Line = "shopping"

                "В кино." if "movie" not in Player.RecentActions and Round >= 60:
                        $ Line = "movie"
                "В кино [[No time]. (locked)" if "movie" in Player.RecentActions or Round < 60:
                        $ Line = "movie"

                "Давай вернемся.":
                        if "movie" in Player.RecentActions or "dinner" in Player.RecentActions or "shopping" in Player.RecentActions:
                                #if you did anything at all...
                                show blackscreen onlayer black with dissolve
                                "Уже поздно, вы возвращаетесь в общежитие..."
                        else:
                                $ Party[0].Statup("Love", 90, -3)
                                $ Party[0].Statup("Obed", 50, 1)
                                if len(Party) >= 2:
                                        $ Party[1].Statup("Love", 90, -3)
                                        $ Party[1].Statup("Obed", 50, 1)
                                if Party[0] is RogueX:
                                        ch_r "Ну и зачем я вообще прихорашивалась?"
                                elif Party[0] is KittyX:
                                        ch_k "[KittyX.Like]у тебя обычно так проходят свидания?"
                                elif Party[0] is EmmaX:
                                        ch_e "Зря только потратила свое время."
                                elif Party[0] is LauraX:
                                        ch_l "М-да."
                                elif Party[0] is JeanX:
                                        $ Party[0].Statup("Obed", 70, 2)
                                        if not Player.Male:
                                            ch_j "Ты что, просто так потратила мое время?"
                                        else:
                                            ch_j "Ты что, просто так потратил мое время?"
                                elif Party[0] is StormX:
                                        ch_s "Терпеть не могу, когда тратят мое время впустую."
                                elif Party[0] is JubesX:
                                        ch_v "Бессмысленная потеря времени..."
                                elif Party[0] is GwenX:
                                        ch_g "Знаааачит... \"никуда мы не идем.\""
                                elif Party[0] is BetsyX:
                                        ch_b "Только впустую потратила свое время..."
                                elif Party[0] is DoreenX:
                                        ch_d "Ох... ладно..."
                                elif Party[0] is WandaX:
                                        ch_w "Мы же только начали!"
                                show blackscreen onlayer black with dissolve
                        $ Line = 0
                        jump Date_End


    if len(Party) >= 2 and JeanX not in Party:
            if Party[1] is RogueX:
                    ch_r "Звучит заманчиво."
            elif Party[1] is KittyX:
                    ch_k "Ладно, тогда пошли."
            elif Party[1] is EmmaX:
                    ch_e "Ох, чудесно, пойдем?"
            elif Party[1] is LauraX:
                    ch_l "Клево."
            elif Party[1] is StormX:
                    ch_s "Прекрасно."
            elif Party[1] is JubesX:
                    ch_v "Ладно, круто."
            elif Party[1] is GwenX:
                    ch_g "Здорово."
            elif Party[1] is BetsyX:
                    ch_b "Очень хорошо."
            elif Party[1] is DoreenX:
                    ch_d "Ох, здорово!"
            elif Party[1] is WandaX:
                    ch_w "Ладно, отлично."
    else:
            if RogueX in Party:
                    ch_r "Звучит заманчиво."
            elif KittyX in Party:
                    ch_k "Ладно, тогда пошли."
            elif EmmaX in Party:
                    ch_e "Ох, чудесно, пойдем?"
            elif LauraX in Party:
                    ch_l "Клево."
            elif StormX in Party:
                    ch_s "Прекрасно."
            elif JubesX in Party:
                    ch_v "Ладно, круто."
            elif GwenX in Party:
                    ch_g "Здорово."
            elif BetsyX in Party:
                    ch_b "Очень хорошо."
            elif DoreenX in Party:
                    ch_d "Ох, здорово!"
            elif WandaX in Party:
                    ch_w "Ладно, отлично."

    show blackscreen onlayer black with dissolve

    $ Nearby = []
    $ Present = Party[:]

    if Line == "dinner":
            "Вы идете в один из лучших ресторанов города. Еда качественная, но вполне доступная."
            jump Date_Dinner
    elif Line == "movie":
            "Вы направляетесь в местный кинотеатр и просматриваете список фильмов."
            jump Date_Movies
    elif Line == "shopping":
            "Вы гуляете по торговому центру, заглядывая в самые лучшие бутики."
            call Shopping_Mall
            jump Misplaced
    else:
            #somehow didn't pick a location?
            $ bg_current = "bg campus"
            jump Misplaced

#End Date Start   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Crossed Wires Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Date_Crossed(Girls=[],Check=0,Count=0,Cnt=0): #rkeljsvgb
    #this checks to make sure both girls are on the same page.
    #"girls" is the girls that are not cool with a double date.

    if Party[0] is RogueX and "yesdouble" not in RogueX.DailyActions:
            ch_r "А [Party[1].Name] что здесь делает?"
            $ Girls.append(RogueX)
    elif Party[0] is KittyX and "yesdouble" not in KittyX.DailyActions:
            ch_k "А? Что здесь делает [Party[1].Name]?"
            $ Girls.append(KittyX)
    elif Party[0] is EmmaX and "yesdouble" not in EmmaX.DailyActions:
            ch_e "Ох, послушай, почему [Party[1].Name] здесь?"
            $ Girls.append(EmmaX)
    elif Party[0] is LauraX and "yesdouble" not in LauraX.DailyActions:
            ch_l "Слушай."
            ch_l "Почему [Party[1].Name] здесь?"
            $ Girls.append(LauraX)
    elif Party[0] is JeanX and "yesdouble" not in JeanX.DailyActions:
            ch_j "[Party[1].Name]? Я не помню, чтобы приглашала ее."
            $ Girls.append(JeanX)
    elif Party[0] is StormX and "yesdouble" not in StormX.DailyActions:
            ch_s "Послушай, что [Party[1].Name] здесь делает?"
            $ Girls.append(StormX)
    elif Party[0] is JubesX and "yesdouble" not in JubesX.DailyActions:
            ch_v "Что? Почему [Party[1].Name] здесь?"
            $ Girls.append(JubesX)
    elif Party[0] is GwenX and "yesdouble" not in GwenX.DailyActions:
            ch_g "А почему [Party[1].Name] здесь?"
            $ Girls.append(GwenX)
    elif Party[0] is BetsyX and "yesdouble" not in BetsyX.DailyActions:
            ch_b "Могу я спросить, почему [Party[1].Name] здесь?"
            $ Girls.append(BetsyX)
    elif Party[0] is DoreenX and "yesdouble" not in DoreenX.DailyActions:
            ch_d "Слушай, [DoreenX.Petname], почему [Party[1].Name] здесь?"
            $ Girls.append(DoreenX)
    elif Party[0] is WandaX and "yesdouble" not in WandaX.DailyActions:
            ch_w "Послушай, что здесь делает [Party[1].Name]?"
            $ Girls.append(WandaX)

    if Party[1] is RogueX and "yesdouble" not in RogueX.DailyActions:
            if Girls:
                ch_r "Да, почему [Party[0].Name] здесь?"
            else:
                ch_r "Что [Party[0].Name] здесь делает?"
            $ Girls.append(RogueX)
    elif Party[1] is KittyX and "yesdouble" not in KittyX.DailyActions:
            if Girls:
                ch_k "Ага, что нибудь мне объяснишь?"
            else:
                ch_k "А? [Party[0].Name] что здесь делает?"
            $ Girls.append(KittyX)
    elif Party[1] is EmmaX and "yesdouble" not in EmmaX.DailyActions:
            if Girls:
                ch_e "Да, постараешься объяснить?"
            else:
                ch_e "Ох, послушай, почему [Party[0].Name] здесь?"
            $ Girls.append(EmmaX)
    elif Party[1] is LauraX and "yesdouble" not in LauraX.DailyActions:
            if Girls:
                ch_l "Да, в чем дело?"
            else:
                ch_l "Слушай."
                ch_l "Почему [Party[0].Name] здесь?"
            $ Girls.append(LauraX)
    elif Party[1] is JeanX and "yesdouble" not in JeanX.DailyActions:
            if Girls:
                ch_j "Да, [Party[0].Name]? Я не помню чтобы приглашала ее."
            else:
                ch_j "[Party[0].Name]? Я не помню чтобы приглашала ее."
            $ Girls.append(JeanX)
    elif Party[1] is StormX and "yesdouble" not in StormX.DailyActions:
            if Girls:
                ch_s "Да, я тоже хотела бы это знать."
            else:
                ch_s "Послушай, что [Party[0].Name] здесь делает?"
            $ Girls.append(StormX)
    elif Party[1] is JubesX and "yesdouble" not in JubesX.DailyActions:
            if Girls:
                ch_v "Да, в чем дело?"
            else:
                ch_v "Слушай, почему [Party[0].Name] здесь?"
            $ Girls.append(JubesX)
    elif Party[1] is GwenX and "yesdouble" not in GwenX.DailyActions:
            if Girls:
                ch_g "Эм, да, что случилось?"
            else:
                ch_g "А почему [Party[0].Name] здесь?"
            $ Girls.append(GwenX)
    elif Party[1] is BetsyX and "yesdouble" not in BetsyX.DailyActions:
            if Girls:
                ch_b "Действительно, почему мы -обе- здесь?"
            else:
                ch_b "Могу я спросить, почему [Party[0].Name] здесь?"
            $ Girls.append(BetsyX)
    elif Party[1] is DoreenX and "yesdouble" not in DoreenX.DailyActions:
            if Girls:
                ch_d "Ага, почему -я- здесь?"
            else:
                ch_d "Слушай, [DoreenX.Petname], почему [Party[0].Name] здесь?"
            $ Girls.append(DoreenX)
    elif Party[1] is WandaX and "yesdouble" not in WandaX.DailyActions:
            if Girls:
                ch_w "Я думала, здесь будем только мы вдвоем..."
            else:
                ch_w "Послушай, что здесь делает [Party[0].Name]?"
            $ Girls.append(WandaX)

    if not Girls:
            #if both are fine with it, just return
            return

    menu:
        "Я думала, мы можем повеселиться вместе." if not Player.Male:
                $ Check = "fun"
        "Я думал, мы можем повеселиться вместе." if Player.Male:
                $ Check = "fun"
        "Ох, я что, забыла тебе сказать?" if not Player.Male:
                $ Check = "cute"
        "Ох, я что, забыл тебе сказать?" if Player.Male:
                $ Check = "cute"
        "Вы обе идете со мной.":
                $ Check = "order"

        "Неважно [[бросить одну или обеих]":
                menu:
                    "[RogueX.Name], можешь идти" if RogueX in Party:
                            if ApprovalCheck(RogueX, 1400, "LO"):
                                    $ RogueX.FaceChange("sad", 1)
                                    ch_r "Ох, ладно. Тогда увидимся позже?"
                                    "[RogueX.Name] уходит."
                                    call Girl_Date_Over(RogueX,0)
                            else:
                                    call Girl_Date_Over(RogueX)
                    "[KittyX.Name], можешь идти" if KittyX in Party:
                            if ApprovalCheck(KittyX, 1400, "LO"):
                                    $ KittyX.FaceChange("sad", 1)
                                    ch_k "А? Ну, ладно?"
                                    "[KittyX.Name] уходит."
                                    call Girl_Date_Over(KittyX,0)
                            else:
                                    call Girl_Date_Over(KittyX)
                    "[EmmaX.Name], можешь идти" if EmmaX in Party:
                            if ApprovalCheck(EmmaX, 1500, "LO"):
                                    $ EmmaX.FaceChange("sad", 1)
                                    ch_e "Хм. Потом тебе придется загладить свою вину."
                                    "[EmmaX.Name] уходит."
                                    call Girl_Date_Over(EmmaX,0)
                            else:
                                    call Girl_Date_Over(EmmaX)
                    "[LauraX.Name], можешь идти" if LauraX in Party:
                            if ApprovalCheck(LauraX, 1500, "LO"):
                                    $ LauraX.FaceChange("sad", 1)
                                    ch_l "У этого решения будут последствия. [[Она это запомнит]"
                                    "[LauraX.Name] уходит."
                                    call Girl_Date_Over(LauraX,0)
                            else:
                                    call Girl_Date_Over(LauraX)
                    "[JeanX.Name], можешь идти" if JeanX in Party:
                            if ApprovalCheck(JeanX, 800, "LO"):
                                    $ JeanX.FaceChange("normal", 1,Eyes="side")
                                    if JeanX == Party[0]:
                                            if not Player.Male:
                                                ch_j "Ты ее слышала, можешь идти, [Party[1].Name]."
                                            else:
                                                ch_j "Ты его слышала, можешь идти, [Party[1].Name]."
                                            "[JeanX.Name] игнорирует ваши слова... а [Party[1].Name] уходит."
                                            call Girl_Date_Over(Party[1],0)
                                    else:
                                            if not Player.Male:
                                                ch_j "Ты ее слышала, можешь идти, [Party[0].Name]."
                                            else:
                                                ch_j "Ты его слышала, можешь идти, [Party[0].Name]."
                                            "[JeanX.Name] игнорирует ваши слова... а [Party[0].Name] уходит."
                                            call Girl_Date_Over(Party[0],0)
                            else:
                                    ch_j "У меня нет на это времени."
                                    call Girl_Date_Over(JeanX)
                    "[StormX.Name], можешь идти" if StormX in Party:
                            if ApprovalCheck(StormX, 1400, "LO"):
                                    $ StormX.FaceChange("sad", 1)
                                    ch_s "Позже тебе придется многое мне объяснить."
                                    "[StormX.Name] уходит."
                                    call Girl_Date_Over(StormX,0)
                            else:
                                    call Girl_Date_Over(StormX)
                    "[JubesX.Name], можешь идти" if JubesX in Party:
                            if ApprovalCheck(JubesX, 1400, "LO"):
                                    $ JubesX.FaceChange("sad", 1)
                                    ch_v "Что? Ну ладно..."
                                    "[JubesX.Name] уходит."
                                    call Girl_Date_Over(JubesX,0)
                            else:
                                    call Girl_Date_Over(JubesX)
                    "[GwenX.Name], можешь идти" if GwenX in Party:
                            if ApprovalCheck(GwenX, 1400, "LO"):
                                    $ GwenX.FaceChange("sad", 1)
                                    ch_g "Что?"
                                    ch_g "Ну хорошо..."
                                    "[GwenX.Name] уходит."
                                    call Girl_Date_Over(GwenX,0)
                            else:
                                    call Girl_Date_Over(GwenX)
                    "[BetsyX.Name], можешь идти" if BetsyX in Party:
                            if ApprovalCheck(BetsyX, 1400, "LO"):
                                    $ BetsyX.FaceChange("sad", 1)
                                    ch_b "Ох?"
                                    ch_b "Интересно... Тогда я пойду..."
                                    "[BetsyX.Name] уходит."
                                    call Girl_Date_Over(BetsyX,0)
                            else:
                                    call Girl_Date_Over(BetsyX)
                    "[DoreenX.Name], можешь идти" if DoreenX in Party:
                            if ApprovalCheck(DoreenX, 1400, "LO"):
                                    $ DoreenX.FaceChange("sad", 1)
                                    ch_d "А?"
                                    ch_d "Оу, тогда я пойду..."
                                    "[DoreenX.Name] уходит."
                                    call Girl_Date_Over(DoreenX,0)
                            else:
                                    call Girl_Date_Over(DoreenX)
                    "[WandaX.Name], можешь идти" if WandaX in Party:
                            if ApprovalCheck(WandaX, 1400, "LO"):
                                    $ WandaX.FaceChange("angry", 1)
                                    ch_w "Что?!"
                                    $ WandaX.FaceChange("sad", 1)
                                    ch_w "Да пофиг..."
                                    "[WandaX.Name] уходит."
                                    call Girl_Date_Over(WandaX,0)
                            else:
                                    call Girl_Date_Over(WandaX)


                    "Неважно. [[Идти домой]":
                            if RogueX in Party:
                                    if ApprovalCheck(RogueX, 1400, "LO"):
                                        $ RogueX.FaceChange("sad", 1)
                                        ch_r "Ох, ладно. Тогда увидимся позже?"
                                        call Girl_Date_Over(RogueX,0)
                                    else:
                                        call Girl_Date_Over(RogueX)
                            if KittyX in Party:
                                    if ApprovalCheck(KittyX, 1400, "LO"):
                                        $ KittyX.FaceChange("sad", 1)
                                        ch_k "А? Ну, ладно, наверное?"
                                        call Girl_Date_Over(KittyX,0)
                                    else:
                                        call Girl_Date_Over(KittyX)
                            if EmmaX in Party:
                                    if ApprovalCheck(EmmaX, 1500, "LO"):
                                        $ EmmaX.FaceChange("sad", 1)
                                        ch_e "Хм. Потом тебе придется загладить свою вину."
                                        call Girl_Date_Over(EmmaX,0)
                                    else:
                                        call Girl_Date_Over(EmmaX)
                            if LauraX in Party:
                                    if ApprovalCheck(LauraX, 1500, "LO"):
                                        $ LauraX.FaceChange("sad", 1)
                                        ch_l "У этого решения будут последствия. [[Она это запомнит]"
                                        call Girl_Date_Over(LauraX,0)
                                    else:
                                        call Girl_Date_Over(LauraX)
                            if JeanX in Party:
                                    if ApprovalCheck(JeanX, 1500, "LO"):
                                        $ JeanX.FaceChange("sad", 1)
                                        if not Player.Male:
                                            ch_j "Ты только зря потратила мое время."
                                        else:
                                            ch_j "Ты только зря потратил мое время."
                                        call Girl_Date_Over(JeanX,0)
                                    else:
                                        call Girl_Date_Over(JeanX)
                            if StormX in Party:
                                    if ApprovalCheck(StormX, 1500, "LO"):
                                        $ StormX.FaceChange("sad", 1)
                                        ch_s "Позже тебе придется многое мне объяснить."
                                        call Girl_Date_Over(StormX,0)
                                    else:
                                        call Girl_Date_Over(StormX)
                            if JubesX in Party:
                                    if ApprovalCheck(JubesX, 1400, "LO"):
                                        $ JubesX.FaceChange("sad", 1)
                                        ch_v "Что? Ну ладно..."
                                        call Girl_Date_Over(JubesX,0)
                                    else:
                                        call Girl_Date_Over(JubesX)
                            if GwenX in Party:
                                    if ApprovalCheck(GwenX, 1400, "LO"):
                                        $ GwenX.FaceChange("sad", 1)
                                        ch_g "Только зря потратила свое время..."
                                        call Girl_Date_Over(GwenX,0)
                                    else:
                                        call Girl_Date_Over(GwenX)
                            if BetsyX in Party:
                                    if AprovalCheck(BetsyX, 1400, "LO"):
                                        $ BetsyX.FaceChange("sad", 1)
                                        ch_b "Ну и ну... Только зря потратила свое время..."
                                        call Girl_Date_Over(BetsyX,0)
                                    else:
                                        call Girl_Date_Over(BetsyX)
                            if DoreenX in Party:
                                    if AprovalCheck(DoreenX, 1400, "LO"):
                                        $ DoreenX.FaceChange("sad", 1)
                                        ch_d "А? Оу, с ума сойти..."
                                        call Girl_Date_Over(DoreenX,0)
                                    else:
                                        call Girl_Date_Over(DoreenX)
                            if WandaX in Party:
                                    if AprovalCheck(WandaX, 1400, "LO"):
                                        $ WandaX.FaceChange("sad", 1)
                                        ch_w "Неженка..."
                                        call Girl_Date_Over(WandaX,0)
                                    else:
                                        call Girl_Date_Over(WandaX)

                            "Вы возвращаетесь в свою комнату."
                            if "yesdate" in Player.DailyActions:
                                    $ Player.DailyActions.remove("yesdate")
                            $ bg_current = "bg player"
                            jump Misplaced
                return
    #end question menu

    $ Cnt = 2
    while Cnt:
            #checks to see whether each girls stays or goes
            #assumes that this process starts with two girls, Party[0] and [1]
            $ Cnt -= 1 #first time through is 1, second time through is 0, then out
            if len(Party) < 2:
                    #if the other girl's dropped out
                    if not ApprovalCheck(Party[0], 1000,Alt=[[EmmaX,LauraX,WandaX],800]):
                            #if the remaining girl isn't interested, this quits out.
                            if Party[0] is RogueX:
                                    ch_r "Так... Я, пожалуй, тоже пойду?"
                            elif Party[0] is KittyX:
                                    ch_k "Да, это довольно странная сцена, может, встретимся позже?"
                            elif Party[0] is EmmaX:
                                    ch_e "Как непрофессионально."
                            elif Party[0] is LauraX:
                                    ch_l "Тебе нужно лучше все планировать."
                                    ch_l "Но, похоже, ты сделал это нарочно."
                            elif Party[0] is JeanX:
                                    ch_j "Я чувствую, что с тобой что-то не так."
                                    ch_j "Тебе нужно собраться."
                            elif Party[0] is StormX:
                                    ch_s "[StormX.Petname], тебе нужно внимательнее все планировать."
                            elif Party[0] is JubesX:
                                    ch_v "Я не уверена, [JubesX.Petname], но думаю, мне стоит вернуться."
                            elif Party[0] is GwenX:
                                    if not Player.Male:
                                        ch_g "Как неловко получилось... Послушай, ты явно что-то задумала..."
                                    else:
                                        ch_g "Как неловко получилось... Послушай, ты явно что-то задумал..."
                                    ch_g "Пожалуй... мне лучше уйти..."
                            elif Party[0] is BetsyX:
                                    ch_b "Мне... пожалуй, тоже пора идти..."
                            elif Party[0] is DoreenX:
                                    ch_d "Я... наверное, тоже пойду..."
                            elif Party[0] is WandaX:
                                    ch_w "Ладно, думаю, я тоже пойду..."
                            call Girl_Date_Over(Party[0],0)
                    return

            if Check == "fun":
                    if ApprovalCheck(Party[Cnt],1000):
                        $ Check = 0
                    else:
                        $ Check = -200
            elif Check == "cute":
                    if ApprovalCheck(Party[Cnt],1000,"LI"):
                        $ Check = 200
                    else:
                        $ Check = -100
            elif Check == "order":
                    if ApprovalCheck(Party[Cnt],1200,"LO"):
                        $ Check = 100
                    else:
                        $ Check = -300
            else:
                        $ Check = 0

            $ Count = 0 if Cnt == 1 else 1

            if Party[Cnt] == JeanX:
                    ch_j "Отлично, давайте начнем..."
            elif ApprovalCheck(Party[Cnt], 800, "OI", Bonus = Check) and Party[Cnt].GirlLikeCheck(Party[Count]) >= 600:
                    # If they like you well enough and get along with the other girl
                    # if the current iteration is 1, then it's Party[1].LikesParty[0]
                    # if the current iteration is 0, then it's Party[0].LikesParty[1]
                    $ Party[Cnt].FaceChange("smile")
                    if Party[Cnt] is RogueX:
                            ch_r "Конечно, почему нет."
                    elif Party[Cnt] is KittyX:
                            ch_k "Конечно, звучит весело."
                    elif Party[Cnt] is EmmaX:
                            ch_e "Ладно, я в деле."
                    elif Party[Cnt] is LauraX:
                            ch_l "Это может быть весело..."
                    elif Party[Cnt] is StormX:
                            ch_s "Я не против ее компании."
                    elif Party[Cnt] is JubesX:
                            ch_v "Конечно, она замечательная."
                    elif Party[Cnt] is GwenX:
                            ch_g "Здорово, чем больше, тем веселее."
                    elif Party[Cnt] is BetsyX:
                            ch_b "Ну хорошо."
                    elif Party[Cnt] is DoreenX:
                            ch_d "Ох... Здорово."
                    elif Party[Cnt] is WandaX:
                            ch_w "Конечно, без проблем."
            elif Party[Cnt].GirlLikeCheck(Party[Count]) >= 750 or "friendly" in Party[Cnt].DailyActions:
                    # if they really like the other girl
                    $ Party[Cnt].FaceChange("bemused")
                    if Party[Cnt] is RogueX:
                            ch_r "Ох, ну, наверное..."
                    elif Party[Cnt] is KittyX:
                            ch_k "Хм, ага..."
                    elif Party[Cnt] is EmmaX:
                            ch_e "Это может быть интересно..."
                    elif Party[Cnt] is LauraX:
                            ch_l "Хорошо."
                    elif Party[Cnt] is StormX:
                            ch_s "Я не против ее компании."
                    elif Party[Cnt] is JubesX:
                            ch_v "Лады, она клевая."
                    elif Party[Cnt] is GwenX:
                            ch_g "Спасибо и пожалуйста."
                    elif Party[Cnt] is BetsyX:
                            ch_b "Ох, должно быть, мы чудесно проведем вечер."
                    elif Party[Cnt] is DoreenX:
                            ch_d "Здорово!"
                    elif Party[Cnt] is WandaX:
                            ch_w "Конечно, без проблем."
            elif ApprovalCheck(Party[Cnt], 1300, "LO", Bonus = Check):
                    # if they especially like you
                    $ Party[Cnt].FaceChange("sad")
                    if Party[Cnt] is RogueX:
                            ch_r "Если ты настаиваешь..."
                    elif Party[Cnt] is KittyX:
                            ch_k "Думаю, можно, если тебе так этого хочется..."
                    elif Party[Cnt] is DoreenX:
                            ch_d "Если ты настаиваешь..."
                    else:
                            call AnyLine(Party[Cnt],"Если ты настаиваешь.")
            else:
                    $ Party[Cnt].FaceChange("angry")
                    if Party[Cnt] is RogueX:
                            ch_r "Мечтай!"
                    elif Party[Cnt] is KittyX:
                            ch_k "Хотеть не вредно!"
                    elif Party[Cnt] is EmmaX:
                            $ Party[Cnt].FaceChange("surprised",Mouth="smirk")
                            ch_e "О, ты хочешь многого."
                            $ Party[Cnt].FaceChange("angry")
                            ch_e "Слишком многого."
                    elif Party[Cnt] is LauraX:
                            $ Party[Cnt].FaceChange("surprised",Mouth="smirk")
                            ch_l "Ты серьезно?"
                            $ Party[Cnt].FaceChange("angry")
                            ch_l "И это твой план?"
                    elif Party[Cnt] is StormX:
                            ch_s "Я лучше оставлю вас наедине."
                    elif Party[Cnt] is JubesX:
                            ch_v "Нее, но вы двое повеселитесь там..."
                    elif Party[Cnt] is GwenX:
                            ch_g "Ха, я не хочу участвовать в этом."
                    elif Party[Cnt] is BetsyX:
                            ch_b "Твой оптимизм просто впечатляет."
                    elif Party[Cnt] is DoreenX:
                            ch_d "Ага, но я так не думаю!"
                    elif Party[Cnt] is WandaX:
                            ch_w "Хех, нет."
                    call Girl_Date_Over(Party[Cnt],0)
    #end check to see if they're cool with this...
    return
#End Crossed Wires Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label FriendlyDate: #rkeljsvgb
        #this is called to check whether this will be a serious or friendly date. Adds "friendly" tag to daily if true
        if Player.Male:
                return
        if "girltalk" in Girl.History:
                #if she sees you romantically, it's a normal date, return
                return

        if Girl is RogueX:
                ch_r "О, желаешь погулять как подруги?"
        elif Girl is KittyX:
                ch_k "О, ты хочешь[KittyX.like]провести дружеский вечер?"
        elif Girl is EmmaX:
                ch_e "Ты хочешь провести дружеский вечер со своим преподавателем?"
        elif Girl is LauraX:
                ch_l "Это дружеские посиделки?"
        elif Girl is JeanX:
                ch_j "О, мы просто потусуемся вместе как подруги?"
        elif Girl is StormX:
                ch_s "Желаешь прогуляться как подруги?"
        elif Girl is JubesX:
                ch_v "Хочешь пообщаться как подруги?"
        elif Girl is GwenX:
                ch_g "Агаааа..."
        elif Girl is BetsyX:
                ch_b "Желаешь погулять как подруги? Звучит заманчиво."
        elif Girl is DoreenX:
                ch_d "О, как подруги? Конечно."
        elif Girl is WandaX:
                ch_w "Конечно, почему бы и нет?"
        menu:
            extend ""
            "Ага, проведем время вместе как подруги.":
                    $ Girl.AddWord(1,0,"friendly",0,0) #adds "friendly" to daily
                    return
            "Я зову тебя на настоящее свидание.":
                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            "Я не уверена, скорее, я хочу чего-то большего...":
                if ApprovalCheck(Girl, 800):
                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

        if "nogirls" in Girl.History:
                #if she rejected you romantically...
                call AnyLine(Girl,"Насчет свидания я не уверена...")
                menu:
                    extend ""
                    "Тогда пошли погуляем как подруги.":
                        if ApprovalCheck(Girl, 500):
                                $ Girl.AddWord(1,0,"friendly",0,0) #adds "friendly" to daily
                    "Тогда извини, возможно, в другой раз.":
                                $ renpy.pop_call() #resets to outside the "ask date" system
        return
#end friendly date


#label Date_Prep(Girl=0):
#    #This gets the girl Dressed and ready for Dinner, called by Date_Night
#    if Girl not in TotalGirls:
#            "Tell Oni this girl called without a target girl."
#            return
#    $ Taboo = 40
#    $ Girl.Taboo = 40
#    if Girl.Clothing[7]:
#            # if she has a date outfit set
#            if Girl.Clothing[7] == 2:
#                    $ Girl.Outfit = "casual2"
#            elif Girl.Clothing[7] == 3:
#                    $ Girl.Outfit = "custom1"
#            elif Girl.Clothing[7] == 4:
#                    $ Girl.Outfit = "gym"
#            elif Girl.Clothing[7] == 5:
#                    $ Girl.Outfit = "custom2"
#            elif Girl.Clothing[7] == 6:
#                    $ Girl.Outfit = "custom3"
#            else:
#                    $ Girl.Outfit = "casual1"
#    else:
#            $ Options = ["casual2", "casual1"]
#            $ Options.append("custom1") if Girl.Custom1[0] == 2 else Options
#            $ Options.append("custom2") if Girl.Custom2[0] == 2 else Options
#            $ Options.append("custom3") if Girl.Custom3[0] == 2 else Options
#            $ renpy.random.shuffle(Options)
#            $ Girl.Outfit = Options[0]
#            $ del Options[:]
#    $ Girl.Loc = "date"
#    $ Girl.OutfitChange(Changed=1)
#    $ Girl.FaceChange("smile")
#    return

# End Rogue Prep / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Dinner Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_Dinner:    #rkeljsvgbdw
    $ bg_current = "bg restaurant"
    $ Player.RecentActions.append("dinner")
    $ Player.DailyActions.append("dinner")
    $ BO = Party[:]
    while BO:
        $ BO[0].Loc = "bg restaurant"
        $ BO.remove(BO[0])

    call Set_The_Scene

    "К вашему столику подходит официантка."

    $ BO = Party[:]
    while BO:
        call Menu_Order
        $ BO.remove(BO[0])
    call Player_Dinner

    "Через какое-то время официантка приносит вам еду."

    $ Line = "Вы едите " + Line

    if JubesX in Party and "surfturf" in JubesX.RecentActions:
            $ Line = Line + ", "+JubesX.Name+" ковыряется в своей еде, но почти ничего не ест."
    elif KittyX in Party and "surfturf" in KittyX.RecentActions:
            $ Line = Line + ", "+KittyX.Name+" ест стейк, но лобстера отодвигает в сторону."
    else:
            $ Line = Line + ", и приятно разговариваете за едой."

    "[Line]"
    $ Player.RecentActions.append("dinner")

    $ Count = 3
    while Count > 0:
            $ Count -= 1
            menu:
                "Поговорить с [Party[0].Name_tvo]":
                        ch_p "Что нового, [Party[0].Name]?"
                        call expression Party[0].Tag + "_Chitchat"
                "Поговорить с [Party[1].Name_tvo]" if len(Party) > 1:
                        ch_p "Что нового, [Party[1].Name]?"
                        call expression Party[1].Tag + "_Chitchat"
                "Сделать комплимент [Party[0].Name_dat]":
                        call Compliment(Party[0])
                "Сделать комплимент [Party[1].Name_dat]" if len(Party) > 1:
                        call Compliment(Party[1])
                "Просто закончить есть":
                        $ Count = 0

    call Dinner_Sex

    if Party and "dategirltalk" in Party[0].RecentActions:
            $ Party[0].DrainWord("dategirltalk",1,0) #removes from recent
            "Когда вы заканчиваете трапезу, вы замечаете, что [Party[0].Name] выглядит немного обеспокоенной."
            call expression Party[0].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
    elif len(Party) > 1 and "dategirltalk" in Party[1].RecentActions:
            $ Party[1].DrainWord("dategirltalk",1,0) #removes from recent
            "Когда вы заканчиваете трапезу, вы замечаете, что [Party[1].Name] выглядит немного обеспокоенной."
            call expression Party[1].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

    call Date_Paying("dinner")

    $ Round -= 30 if Round > 40 else (Round-10) #reduces Round to at minimum 10

    if Round < 20:
            "Уже поздно, вы возвращаетесь в общежитие..."
            jump Date_End

    if not Party:
            "Вы решаете вернуться в свою комнату."
            jump Date_Over

    "Похоже, у вас еще осталось время, куда вы хотели бы отправиться дальше?"
    jump Date_Location #picks next stop...

# End Primary Dinner Sequence / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






label Player_Dinner: #rkeljsvgb
    # This is the player's menu choices
    menu:
        "Для себя вы заказываете..."
        "Стейк и лобстера. ($25)":
            $ Play_Cost = 25
            $ Line = "свой стейк с сочным лобстером"
        "Стейк. ($20)":
            $ Play_Cost = 20
            $ Line = "свой стейк рибай средней прожарки"
        "Лосося. ($20)":
            $ Play_Cost = 20
            $ Line = "свое филе лосося"
        "Цыпленка. ($10)":
            $ Play_Cost = 10
            $ Line = "свои жареные куриные бедрышки"
        "Простой салат. ($5)":
            $ Play_Cost = 5
            $ Line = "свой свежий зеленый салат"
    return


label Menu_Order(Meal=0,GirlCost=0):
    menu:
        "Вы хотите выбрать еду для [BO[0].Name_rod]?"
        "Да":
                $ Meal = 1
        "Нет.":
                call AnyLine(BO[0],"Так, посмотрим...")

    if BO[0] is JeanX:
        if not ApprovalCheck(JeanX, 500, "O"):
            ch_j "Я буду стейк с лобстером."
            $ PassLine = renpy.random.choice(["-но я хочу отказаться от стейка, хочу только лобстера.",
                    "-но я хочу два лобстера.",
                    "-с кровью.",
                    "-полной прожарки.",
                    "-но я хочу крабовые ножки вместо лобстера.",
                    "-но я хочу заменить лобстера другим стейком.",
                    "-но я хочу заменить стейк еще одним лобстером."])
            ch_j "[PassLine]"
            $ GirlCost = 25
            $ Meal = "surfturf"
        elif Meal == 2:
            ch_j "Я бы хотела-"
    if Meal == 1:
        menu:
            "Для [BO[0].Name_rod] вы заказываете..."
            "Стейк и лобстера. ($25)":
                    $ GirlCost = 25
                    $ Meal = "surfturf"
                    $ BO[0].FaceChange("smile", Brows = "surprised")
                    if BO[0] is RogueX:
                            ch_r "О, похоже мы сегодня гуляем."
                            $ BO[0].FaceChange()
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is KittyX:
                            ch_k "Эм, честно говоря, я[KittyX.like]не ем ракообразных..."
                            $ BO[0].FaceChange()
                            $ BO[0].Statup("Love", 80, -5)
                            $ BO[0].Statup("Love", 200, -2)
                            $ GirlCost = 20
                            call Date_Bonus(KittyX,-11)
                    elif BO[0] is EmmaX:
                            $ BO[0].FaceChange("sly")
                            ch_e "Ммм, изысканный выбор."
                            $ BO[0].FaceChange()
                            $ BO[0].Statup("Love", 80, 7)
                            $ BO[0].Statup("Love", 200, 3)
                    elif BO[0] is LauraX:
                            $ BO[0].FaceChange("sad",Brows = "surprised")
                            ch_l "Отлично..."
                            $ BO[0].FaceChange()
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 90, 2)
                    elif BO[0] is JeanX:
                            $ BO[0].FaceChange("sly",Brows = "surprised")
                            ch_j "Хороший выбор."
                            $ BO[0].FaceChange()
                            $ BO[0].Statup("Love", 80, 3)
                            $ BO[0].Statup("Love", 90, 2)
                            $ BO[0].Statup("Obed", 70, 2)
                    elif BO[0] is StormX:
                            $ BO[0].FaceChange("confused",Mouth="smile")
                            ch_s "Это достаточно тяжелая пища..."
                            $ BO[0].FaceChange()
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is JubesX:
                            $ BO[0].FaceChange("sad",Brows = "surprised")
                            if not Player.Male:
                                ch_v "Выпендрежница..."
                            else:
                                ch_v "Выпендрежник..."
                            $ BO[0].FaceChange()
                            $ BO[0].Statup("Love", 80, -5)
                            $ BO[0].Statup("Love", 200, -2)
                            call Date_Bonus(JubesX,-11)
                    elif BO[0] is GwenX:
                            $ BO[0].FaceChange("smile")
                            ch_g "Ты знаешь, чего я хочу!"
                            $ BO[0].Statup("Love", 80, 7)
                            $ BO[0].Statup("Love", 200, 3)
                    elif BO[0] is BetsyX:
                            $ BO[0].FaceChange("smile")
                            ch_b "Ох, это довольно сытный ужин из нескольких блюд..."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is DoreenX:
                            $ BO[0].FaceChange("smile")
                            ch_d "Всего понемногу, это хорошо!"
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 200, 2)
                            $ BO[0].Statup("Obed", 80, 2)
                    elif BO[0] is WandaX:
                            $ BO[0].FaceChange("smile")
                            ch_w "Я не против отведать и того, и другого..."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Obed", 80, 2)
                    #End surf and turf

            "Стейк. ($20)":
                    $ GirlCost = 20
                    $ Meal = "ribeye"
                    $ BO[0].FaceChange("smile")
                    if BO[0] is RogueX:
                            ch_r "Мне нравятся большие сочные стейки."
                            $ BO[0].Statup("Love", 80, 5)
                    elif BO[0] is KittyX:
                            ch_k "Восхитительно."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is EmmaX:
                            ch_e "Мне нравится нежное мясо."
                            $ BO[0].Statup("Love", 80, 5)
                    elif BO[0] is LauraX:
                            ch_l "С кровью."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 90, 2)
                    elif BO[0] is JeanX:
                            ch_j "Думаю, меня устроит."
                            $ BO[0].Statup("Love", 80, 2)
                            $ BO[0].Statup("Love", 90, 1)
                            $ BO[0].Statup("Obed", 70, 2)
                    elif BO[0] is StormX:
                            ch_s "Стейк - это хорошо... иногда."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is JubesX:
                            ch_v "Только с кровью."
                            if renpy.random.randint(1, 20) > 10:
                                ch_v "И когда я говорю с \"кровью\"..."
                                ch_v "Если я увижу хоть один след от ожога на этом стейке..."
                                ch_v "Я приду за тобой."
                            $ BO[0].Statup("Love", 80, 3)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is GwenX:
                            ch_g "Не могу дождаться мяса!"
                            $ BO[0].Statup("Love", 80, 5)
                    elif BO[0] is BetsyX:
                            ch_b "Я никогда не отказываюсь от большого куска мяса..."
                            $ BO[0].Statup("Love", 80, 3)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is DoreenX:
                            ch_d "Я не откажусь от большого куска мяса!"
                            $ BO[0].Statup("Love", 80, 4)
                            $ BO[0].Statup("Love", 200, 1)
                    elif BO[0] is WandaX:
                            $ BO[0].FaceChange("smile")
                            ch_w "Стейк - хороший выбор."
                            $ BO[0].Statup("Love", 80, 3)
                            $ BO[0].Statup("Obed", 80, 2)
                    #End steak

            "Лосося. ($20)":
                    $ GirlCost = 20
                    $ Meal = "salmon"
                    $ BO[0].FaceChange("smile")
                    if BO[0] is RogueX:
                            ch_r "Мне нравятся большие сочные филе."
                            $ BO[0].Statup("Love", 80, 5)
                    elif BO[0] is KittyX:
                            ch_k "Восхитительно."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is EmmaX:
                            ch_e "Мне нравится нежное мясо."
                            $ BO[0].Statup("Love", 80, 5)
                    elif BO[0] is LauraX:
                            ch_l "Слабой прожарки."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Love", 90, 2)
                    elif BO[0] is JeanX:
                            ch_j "Думаю, меня устроит."
                            $ BO[0].Statup("Love", 80, 2)
                            $ BO[0].Statup("Love", 90, 1)
                            $ BO[0].Statup("Obed", 70, 2)
                    elif BO[0] is StormX:
                            ch_s "Рыба - это хорошо."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is JubesX:
                            ch_v "Только слабой прожарки."
                            $ BO[0].Statup("Love", 80, 3)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is GwenX:
                            ch_g "Не могу дождаться сочного филе!"
                            $ BO[0].Statup("Love", 80, 5)
                    elif BO[0] is BetsyX:
                            ch_b "Ох, восхитительно!"
                            $ BO[0].Statup("Love", 80, 7)
                            $ BO[0].Statup("Love", 200, 3)
                    elif BO[0] is DoreenX:
                            ch_d "Я люблю рыбу."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is WandaX:
                            $ BO[0].FaceChange("smile")
                            ch_w "Рыба - это хорошо."
                            $ BO[0].Statup("Love", 80, 2)
                            $ BO[0].Statup("Obed", 80, 2)
                    #End fish

            "Цыпленка. ($10)":
                    $ GirlCost = 10
                    $ Meal = "chicken"
                    $ BO[0].FaceChange("smile")
                    $ BO[0].Statup("Love", 50, 1)
                    if BO[0] is RogueX:
                            ch_r "Я обожаю курочку."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is KittyX:
                            ch_k "Цыпленок - неплохой выбор."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is EmmaX:
                            ch_k "Цыпленок - неплохой выбор."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is LauraX:
                            ch_l "Ага, ладно."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is JeanX:
                            ch_j "Ага, как скажешь."
                            $ BO[0].Statup("Love", 80, 3)
                            $ BO[0].Statup("Obed", 70, 2)
                    elif BO[0] is StormX:
                            ch_s "От вкусного цыпленка я не откажусь."
                            $ BO[0].Statup("Love", 80, 2)
                            $ BO[0].Statup("Love", 200, 1)
                    elif BO[0] is JubesX:
                            ch_v "Конечно, как скажешь."
                            $ BO[0].Statup("Love", 80, 1)
                    elif BO[0] is GwenX:
                            ch_g "Пожалуй, цыпленок - неплохой выбор.. "
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is BetsyX:
                            ch_b "О, цыпленок, замечательно..."
                            $ BO[0].Statup("Love", 90, 2)
                            $ BO[0].Statup("Obed", 60, 1)
                    elif BO[0] is DoreenX:
                            ch_d "Мне нравится курица."
                            $ BO[0].Statup("Love", 80, 3)
                    elif BO[0] is WandaX:
                            $ BO[0].FaceChange("smile")
                            ch_w "Я очень люблю куриное мясо."
                            $ BO[0].Statup("Love", 80, 2)
                            $ BO[0].Statup("Love", 200, 2)
                            $ BO[0].Statup("Obed", 80, 2)
                    #End chicken

            "Только салат. ($5)":
                    $ GirlCost = 5
                    $ Meal = "salad"
                    $ BO[0].FaceChange("sad",Brows="confused")
                    if BO[0] is RogueX:
                            ch_r "Что ж, думаю, я не откажусь от салата..."
                            $ BO[0].Statup("Love", 60, -5)
                            $ BO[0].Statup("Obed", 50, 2)
                    elif BO[0] is KittyX:
                            ch_k "Хорошие салаты мне нравятся."
                            $ BO[0].Statup("Love", 60, -3)
                            $ BO[0].Statup("Obed", 50, 2)
                    elif BO[0] is EmmaX:
                            ch_e "Полагаю, можно  поесть салат..."
                            $ BO[0].Statup("Love", 60, -3)
                            $ BO[0].Statup("Obed", 50, -2)
                    elif BO[0] is LauraX:
                            ch_l "Эм, нет."
                            $ BO[0].Statup("Love", 60, -5)
                            $ BO[0].Statup("Obed", 50, -2)
                            $ BO[0].Statup("Inbt", 60, 2)
                            ch_l "Я буду стейк... с кровью."
                            $ GirlCost = 15
                            $ Meal = "ribeye"
                    elif BO[0] is JeanX:
                            $ BO[0].Statup("Love", 60, -5)
                            $ BO[0].Statup("Obed", 70, 2)
                            $ BO[0].Statup("Inbt", 60, 2)
                            ch_j "Ладн- подожди, что?"
                            if ApprovalCheck(JeanX, 700, "O"):
                                    $ BO[0].Statup("Love", 60, 5)
                                    $ BO[0].Statup("Obed", 80, 2)
                                    $ BO[0].Statup("Obed", 90, 3)
                            else:
                                    $ BO[0].FaceChange("sly")
                                    $ BO[0].Statup("Love", 60, -2)
                                    $ BO[0].Statup("Obed", 70, 2)
                                    $ BO[0].Statup("Inbt", 60, 2)
                                    ch_j "Нет, я хочу стейк."
                                    if ApprovalCheck(JeanX, 800, "O"):
                                            $ GirlCost = 20
                                            $ Meal = "ribeye"
                                    else:
                                            ch_j "с лобстером."
                                            $ GirlCost = 25
                                            $ Meal = "surfturf"
                    elif BO[0] is StormX:
                            $ BO[0].FaceChange("smile")
                            ch_s "Меня устроит вегетарианский вариант..."
                            $ BO[0].Statup("Love", 60, 2)
                            $ BO[0].Statup("Obed", 50, 1)
                    elif BO[0] is JubesX:
                            ch_v "Ага, сэкономим немного."
                            $ BO[0].Statup("Love", 60, 3)
                            $ BO[0].Statup("Obed", 50, 2)
                    elif BO[0] is GwenX:
                            ch_g "Эм... ладно..."
                            $ BO[0].Statup("Love", 60, -3)
                            $ BO[0].Statup("Obed", 50, -2)
                    elif BO[0] is BetsyX:
                            $ BO[0].FaceChange("smile")
                            ch_b "Пожалуй, немного зелени не повредит..."
                            $ BO[0].Statup("Love", 80, -2)
                            $ BO[0].Statup("Obed", 60, 2)
                    elif BO[0] is DoreenX:
                            ch_d "Ох, думаю, меня устроит..."
                            $ BO[0].Statup("Love", 80, -2)
                            $ BO[0].Statup("Obed", 60, 3)
                            $ BO[0].Statup("Obed", 90, 2)
                            $ BO[0].Statup("Inbt", 80, -2)
                    elif BO[0] is WandaX:
                            $ BO[0].FaceChange("smile")
                            ch_w "Я не против салата."
                            $ BO[0].Statup("Love", 80, 1)
                            $ BO[0].Statup("Obed", 60, 2)
                            $ BO[0].Statup("Obed", 90, 1)
                    #End salad

            "[BO[0].Name], почему бы тебе не выбрать самой?":
                    call Date_Bonus(BO[0],2)
                    $ BO[0].FaceChange("smile")
                    $ Meal = 0
                    if BO[0] is RogueX:
                            ch_r "Хорошо. Спасибо, [BO[0].Petname]..."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Inbt", 50, 3)
                            $ BO[0].Statup("Obed", 50, -2)
                    elif BO[0] is KittyX:
                            ch_k "Хорошо. Спасибо, [KittyX.Petname]."
                            $ BO[0].Statup("Love", 80, 7)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is EmmaX:
                            ch_e "Благодарю, [EmmaX.Petname]."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Inbt", 50, 3)
                            $ BO[0].Statup("Obed", 50, -2)
                    elif BO[0] is LauraX:
                            ch_l "Спасибо."
                            $ BO[0].Statup("Love", 80, 7)
                            $ BO[0].Statup("Obed", 60, 2)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is JeanX:
                            $ BO[0].Statup("Love", 80, 3)
                            $ BO[0].Statup("Obed", 80, 2)
                    elif BO[0] is StormX:
                            ch_s "Благодарю, [StormX.Petname]."
                            $ BO[0].Statup("Love", 80, 5)
                            $ BO[0].Statup("Inbt", 50, 3)
                            $ BO[0].Statup("Obed", 50, -2)
                    elif BO[0] is JubesX:
                            ch_v "О, спасибо, [JubesX.Petname]."
                            $ BO[0].Statup("Love", 60, 3)
                            $ BO[0].Statup("Love", 80, 7)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is GwenX:
                            $ BO[0].FaceChange("smile")
                            ch_g "О, как мило!"
                            $ BO[0].Statup("Love", 80, 7)
                            $ BO[0].Statup("Obed", 60, 2)
                            $ BO[0].Statup("Love", 200, 2)
                    elif BO[0] is BetsyX:
                            $ BO[0].FaceChange("smile")
                            ch_b "Благодарю, это было бы чудесно..."
                            $ BO[0].Statup("Love", 200, 3)
                            $ BO[0].Statup("Obed", 60, 2)
                            $ BO[0].Statup("Inbt", 70, 2)
                    elif BO[0] is DoreenX:
                            ch_d "О, спасибо!"
                            $ BO[0].Statup("Love", 80, 2)
                            $ BO[0].Statup("Inbt", 80, 2)
                    elif BO[0] is WandaX:
                            $ BO[0].FaceChange("smile")
                            ch_w "Ох! Ладно..."
                            $ BO[0].Statup("Love", 200, 2)
                            $ BO[0].Statup("Inbt", 80, 2)

                    #End "let her choose  "
            # end "you choose" menu

    if not Meal or Meal == 2:
        #if you let them choose...
        if BO[0] is RogueX:
                ch_r "Пожалуй, я возьму цыпленка."
                $ GirlCost = 10
                $ Meal = "chicken"
        elif BO[0] is KittyX:
                ch_k "Пожалуй, я возьму стейк."
                $ GirlCost = 20
                $ Meal = "ribeye"
        elif BO[0] is EmmaX:
                ch_e "Пожалуй, я возьму стейк."
                $ BO[0].FaceChange("sly")
                ch_e "...с лобстером, конечно."
                $ GirlCost = 25
                $ Meal = "surfturf"
        elif BO[0] is LauraX:
                ch_l "Думаю, я возьму стейк."
                $ GirlCost = 20
                $ Meal = "ribeye"
        elif BO[0] is JeanX:
                ch_j "Думаю, я буду стейк с лобстером."
                $ GirlCost = 25
                $ Meal = "surfturf"
        elif BO[0] is StormX:
                ch_s "Тогда я возьму цыпленка."
                $ GirlCost = 10
                $ Meal = "chicken"
        elif BO[0] is JubesX:
                ch_v "Думаю, я возьму салат."
                $ GirlCost = 5
                $ Meal = "salad"
        elif BO[0] is GwenX:
                $ BO[0].FaceChange("smile")
                ch_g "Стейк с лобстером!"
                $ GirlCost = 25
                $ Meal = "surfturf"
        elif BO[0] is BetsyX:
                $ BO[0].FaceChange("smile")
                ch_b "Тогда я возьму лосося."
                $ GirlCost = 25
                $ Meal = "surfturf"
        elif BO[0] is DoreenX:
                ch_d "Наверное, я буду стейк с лобстером..."
                $ GirlCost = 25
                $ Meal = "surfturf"
        elif BO[0] is WandaX:
                ch_w "Цыпленок на картинке выглядит аппетитно."
                $ GirlCost = 10
                $ Meal = "chicken"

    elif "friendly" in BO[0].DailyActions and "girltalk" not in BO[0].History:
            #if she thinks this is a friendly date...
            $ BO[0].FaceChange("confused")
            if "nogirls" in BO[0].History:
                        call AnyLine(BO[0],"Я думала, у нас ненастоящее свидание...")
            call AnyLine(BO[0],"Ты всегда заказываешь еду для других?")
            menu:
                "О, мой просчет.":
                        $ BO[0].FaceChange("smile")
                        call AnyLine(BO[0],"Ничего страшного...")
                "Ну... возможно?" if "nogirls" in BO[0].History:
                        if ApprovalCheck(BO[0], 1000):
                                call AnyLine(BO[0],"Думаю, я хочу посмотреть, что будет дальше..." )
                        else:
                                call AnyLine(BO[0],"Эм... мне нужно идти.")
                                call Girl_Date_Over(BO[0],0)
                                return
                        $ BO[0].DrainWord("friendly",1,1,0)
                "Я думала, это будет романтично.":
                        call expression BO[0].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        if "nogirls" not in BO[0].History:
                                call AnyLine(BO[0],"Думаю, я хочу посмотреть, что будет дальше..." )
                        else:
                                call AnyLine(BO[0],"Эм... мне нужно идти.")
                                call Girl_Date_Over(BO[0],0)
                                return
                        $ BO[0].DrainWord("friendly",1,1,0)
    $ BO[0].RecentActions.append(Meal)
    if Party[0] is BO[0]:
            $ Date_Cost[0] = GirlCost
    else:
            $ Date_Cost[1] = GirlCost
    if BO[0] is JubesX:
            call Date_Bonus(JubesX,(int(GirlCost/2)))
    else:
            call Date_Bonus(BO[0],GirlCost)
    return

# Start Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Dinner_Sex(Girl=0,Previous=0,GirlBonus=0,OptionsDS=[],BO=[]):#rkeljsvgb
    #Called by Dinner Sex

    $ BO = Party[:]
    if 0 in BO:
        $ BO.remove(0)
    while BO:
            if ApprovalCheck(BO[0], 1000) and "friendly" not in BO[0].DailyActions:
                    #Checks if BO[0] is in
                    $ OptionsDS.append(BO[0])
                    if Party[0] is BO[0] and Date_Bonus[0] > 10:
                            $ OptionsDS.append(BO[0])
                    elif BO[0] in Party and Date_Bonus[1] > 10:
                            $ OptionsDS.append(BO[0])
                    if BO[0] is JubesX:
                            $ OptionsDS.append(BO[0])
            $ BO.remove(BO[0])

    if len(OptionsDS) == 0:
            #if nobody is in, return
            return

    $ renpy.random.shuffle(OptionsDS)

    $ Girl = OptionsDS[0]               #picks lead
    if len(Party) >= 2:
            if Girl is Party[0]:
                    $ Previous = Party[1]
            else:
                    $ Previous = Party[0]

    if Girl is Previous:
        "Tell Oni that on a date, a girl and previous were the same, [Girl.Tag], DS"

    $ OptionsDS =["nothing"]

    if Party[0] is Girl:
        $ GirlBonus = Date_Bonus[0] + Date_Cost[0]
    else:
        $ GirlBonus = Date_Bonus[1] + Date_Cost[1]

    if Girl.Anal and ApprovalCheck(Girl, 1500) and GirlBonus >=15:
            $ OptionsDS.append("anal")
    if Girl.Sex and ApprovalCheck(Girl, 1500) and GirlBonus >=10:
            $ OptionsDS.append("sex")
    if (Girl.Blow or Girl.CUN) and ApprovalCheck(Girl, 1300) and GirlBonus >=10:
            $ OptionsDS.append("blow")
    if (Girl.Hand or Girl.Finger) and ApprovalCheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("hand")
    if Girl.FondleP and ApprovalCheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("pussy")
    if ApprovalCheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("foot")

    $ renpy.random.shuffle(OptionsDS)

    if Girl is JubesX and renpy.random.randint(1, 20) > 10:
        $ OptionsDS[0] = "blow"

    $ Girl.FaceChange("sexy")
    if OptionsDS[0] == "nothing":
        pass
    elif OptionsDS[0] == "anal":
        "В середине трапезы, хитрая улыбка появляется на ее лице."
        "Она многозначительно кивает головой в сторону туалетов, а затем уходит по направлению к ним."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "Вы ждете несколько минут ее возвращения. Когда она возвращается, вы видите, что она немного расстроена."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -10)
                call Date_Bonus(Girl,-5)
        else:
                if _return == 1: #other girl is fine
                        "Через несколько секунд вы с [Previous.Name_tvo] следуете за ней и она затаскивает вас обоих внутрь, запирая за вами дверь."
                        if not Player.Male:
                                "Вы достаете свой резиновый член, ведь вы никогда не выходите без него на улицу..."
                        "Следующие несколько минут она проводит, принимая вас в свою попку, пока [Previous.Name] наблюдает за вами."
                        $ Girl.GLG(Previous,1000,3,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else:
                        "Через несколько секунд вы следуете за ней, и она затаскивает вас внутрь, запирая за вами дверь."
                        if not Player.Male:
                                "Вы достаете свой резиновый член, ведь вы никогда не выходите без него на улицу..."
                        "Следующие несколько минут она проводит, принимая вас в свою попку."
                if _return == 3:
                        "[Previous.Name] сверлит вас обоих своим взглядом, пока вы возвращаетесь к столу."
                        call Date_Bonus(Previous,-10)
                if Girl is RogueX:
                        ch_r "Надеюсь, после всего этого, я смогу нормально сидеть."
                elif Girl is KittyX:
                        ch_k "Это -того- стоило."
                elif Girl is EmmaX:
                        ch_e "Благодарю за помощь, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Это стоило того."
                elif Girl is JeanX:
                        ch_j "Мммм, спасибо, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "Я вполне... довольна, [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "Смотри, -как- ты наполняешь меня."
                elif Girl is GwenX:
                        ch_g "Вот что значит \"кончить с отличием.\""
                elif Girl is BetsyX:
                        ch_b "Это было... поразительно."
                elif Girl is DoreenX:
                        ch_d "Ого, это было здорово..."
                elif Girl is WandaX:
                        ch_w "Оооох, ну надо же, вот это да..."
                $ Girl.Statup("Inbt", 50, 9)
                $ Girl.Statup("Inbt", 80, 3)
                if Player.Male:
                    $ Girl.Addict -= 20
                    $ Girl.SeenPeen += 1
                $ Girl.Anal += 1
                $ Player.Semen -= 1
                $ Girl.RecentActions.append("anal")
                $ Girl.RecentActions.append("dinnersex")
                $ Girl.DailyActions.append("anal")
    elif OptionsDS[0] == "sex":
        "В середине трапезы, хитрая улыбка появляется на лице."
        "Она многозначительно кивает головой в сторону туалетов, а затем уходит по направлению к ним."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "Вы ждете несколько минут ее возвращения. Когда она возвращается, вы видите, что она немного расстроена."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -10)
                call Date_Bonus(Girl,-5)
        else:
                if _return == 1: #other girl is fine
                        "Через несколько секунд вы с [Previous.Name_tvo] следуете за ней и она затаскивает вас обоих внутрь, запирая за вами дверь."
                        if not Player.Male:
                                "Вы достаете свой резиновый член, ведь вы никогда не выходите без него на улицу..."
                        "Следующие несколько минут она проводит, трахая вас, пока [Previous.Name] наблюдает за вами."
                        $ Girl.GLG(Previous,1000,3,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else:
                        "Через несколько секунд вы следуете за ней, и она затаскивает вас внутрь, запирая за вами дверь."
                        if not Player.Male:
                                "Вы достаете свой резиновый член, ведь вы никогда не выходите без него на улицу..."
                        "Следующие несколько минут она проводит, трахая вас."
                if _return == 3:
                        "[Previous.Name] сверлит вас обоих своим взглядом, пока вы возвращаетесь к столу."
                        call Date_Bonus(Previous,-10)
                if Girl is RogueX:
                        ch_r "Надо было согнать те калории, что я наела."
                elif Girl is KittyX:
                        ch_k "Нужно было размяться."
                elif Girl is EmmaX:
                        ch_e "Небольшая разминка после ужина никогда не помешает."
                elif Girl is LauraX:
                        ch_l "Извини за царапины."
                elif Girl is JeanX:
                        ch_j "Мммм, спасибо, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "Я вполне... довольна, [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "Смотри, -как- ты наполняешь мое брюшко."
                elif Girl is GwenX:
                        ch_g "Ладно, теперь вернемся к блюдам!"
                elif Girl is BetsyX:
                        ch_b "Я считаю, что это было вполне удовлетворительно."
                elif Girl is DoreenX:
                        ch_d "Ого, это было весело..."
                elif Girl is WandaX:
                        ch_w "Ооох, это было здорово..."
                $ Girl.Statup("Inbt", 50, 8)
                $ Girl.Statup("Inbt", 80, 2)
                if Player.Male:
                    $ Girl.Addict -= 20
                    $ Girl.SeenPeen += 1
                $ Girl.Sex += 1
                $ Player.Semen -= 1
                $ Girl.RecentActions.append("sex")
                $ Girl.RecentActions.append("dinnersex")
                $ Girl.DailyActions.append("sex")
    elif OptionsDS[0] == "blow":
        "В середине трапезы, хитрая улыбка появляется на лице [Girl.Name_rod] и она роняет вилку на пол."
        "После этого она ныряет под стол и расстегивает ваши штаны."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "Вы застегиваете их обратно и останавливаете ее. Она вылазит из-под стола."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -5)
                call Date_Bonus(Girl,-3)
                if Girl is EmmaX:
                        $ Girl.Statup("Obed", 70, 5)
                        ch_e "Вот, нашла..."
        else:
                if _return == 1:
                        #other girl is fine
                        "[Previous.Name] придвигается ближе, обнимает вас одной рукой, а другой гладит щеку [Girl.Name_rod]."
                        if Player.Male:
                                "Затем [Girl.Name] сосет вам несколько минут, пока вы не кончаете."
                        else:
                                "Затем [Girl.Name] лижет вам несколько минут, пока вы не кончаете."
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                elif _return == 2: #other girl is fine
                        if Player.Male:
                                "Затем [Girl.Name] несколько минут сосет вам, пока вы не кончаете, в то время, как [Previous.Name] притворятся, что чем-то занята."
                        else:
                                "Затем [Girl.Name] несколько минут лижет вам, пока вы не кончаете, в то время, как [Previous.Name] притворятся, что чем-то занята."
                else:
                        if Player.Male:
                                "Затем [Girl.Name] сосет вам несколько минут, пока вы не кончаете."
                        else:
                                "Затем [Girl.Name] лижет вам несколько минут, пока вы не кончаете."
                $ Girl.Statup("Inbt", 50, 6)
                $ Girl.Statup("Inbt", 80, 2)
                if Girl.Swallow:
                    "[Girl.Name] вытирает рот, вылезая из-под стола."
                    if Girl is RogueX:
                            ch_r "Думаю, десерт мне больше не нужен."
                    elif Girl is KittyX:
                            ch_k "То что надо..."
                    elif Girl is EmmaX:
                            ch_e "Ммм, сливочный аперитив."
                    elif Girl is LauraX:
                            ch_l "Ням..."
                    elif Girl is JeanX:
                            ch_j "Ммм..."
                    elif Girl is StormX:
                            ch_s "Здесь подают вкусные десерты, не так ли, [Girl.Petname]?"
                    elif Girl is JubesX:
                            ch_v "Мои благодарности шефу..."
                    elif Girl is GwenX:
                            ch_g "Ням."
                    elif Girl is BetsyX:
                            ch_b "Ммм, довольно освежающе."
                    elif Girl is DoreenX:
                            ch_d "Вкусно..."
                    elif Girl is WandaX:
                            ch_w "Думаю, это можно считать десертом..."
                    $ Girl.Addict -= 20
                    $ Girl.Swallow += 1
                    $ Girl.RecentActions.append("swallow")
                    $ Girl.DailyActions.append("swallow")
                else:
                    if not Player.Male:
                        "[Girl.Name] хватает салфетку с ваших брюк и использоует ее, чтобы вытереть все соки."
                    else:
                        "[Girl.Name] хватает салфетку с ваших брюк и использоует ее, чтобы вытереть всю сперму."
                    if Girl is RogueX:
                            ch_r "Уверена, уборщики будут в восторге."
                    elif Girl is KittyX:
                            ch_k "Мне немного жаль официантов."
                    elif Girl is EmmaX:
                            ch_e "Полагаю, это немного грубо по отношению к персоналу."
                    elif Girl is LauraX:
                            ch_l "Извини за беспорядок."
                    elif Girl is JeanX:
                            ch_j "Официант? Убери это."
                    elif Girl is StormX:
                            ch_s "Мы должны оставить хорошие чаевые, [Girl.Petname]."
                    elif Girl is JubesX:
                            "Затем она все слизывает..."
                            ch_v "Мои благодарности шефу..."
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.RecentActions.append("swallow")
                            $ Girl.DailyActions.append("swallow")
                    elif Girl is GwenX:
                            ch_g "Давай... добавим ее к чистым..."
                            $ GwenX.AddWord(1,0,0,"napkin") #trait
                    elif Girl is BetsyX:
                            ch_b "Это было просто чудесно."
                    elif Girl is DoreenX:
                            ch_d "Надо прибраться..."
                    elif Girl is WandaX:
                            "Салфетка исчезает во вспышке синего света."
                $ Girl.Statup("Inbt", 30, 4)
                $ Girl.Statup("Inbt", 80, 2)
                if Player.Male:
                        $ Girl.RecentActions.append("blow")
                        $ Girl.DailyActions.append("blow")
                        $ Girl.SeenPeen += 1
                        $ Girl.Blow += 1
                else:
                        $ Girl.RecentActions.append("cun")
                        $ Girl.DailyActions.append("cun")
                        $ Girl.SeenPuss += 1
                        $ Girl.CUN += 1
                $ Girl.Addict -= 10
                $ Girl.RecentActions.append("dinnersex")
                $ Player.Semen -= 1
                if _return == 3:
                    "[Previous.Name] сверлит вас взглядом, пока [Girl.Name] вылазит из под стола."
                    call Date_Bonus(Previous,-10)
    elif OptionsDS[0] == "hand":
        "В середине трапезы, хитрая улыбка появляется на лице [Girl.Name_rod] и она переставляет свой стул поближе к вам."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4:
                #you refused
                $ Girl.FaceChange("sadside", 2)
                "Она пытается расстегнуть ваши штаны под столом, но вы ее останавливаете."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -5)
                call Date_Bonus(Girl,-2)
        else:
                if _return == 1: #other girl is fine
                        if not Player.Male:
                            "Она расстегивает ваши штаны под столом и начинает ласкать вашу киску."
                        else:
                            "Она расстегивает ваши штаны под столом и начинает ласкать ваш член."
                        "С другой стороны, [Previous.Name] также залазит рукой под стол и присоединяется к вам."
                        $ Line = "They"
                        if Player.Male:
                                $ Previous.Hand += 1
                                $ Previous.RecentActions.append("hand")
                                $ Previous.DailyActions.append("hand")
                        else:
                                $ Previous.Finger += 1
                                $ Previous.RecentActions.append("finger")
                                $ Previous.DailyActions.append("finger")
                        $ Girl.GLG(Previous,600,3,1)
                        $ Previous.GLG(Girl,600,2,1)
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                elif _return == 2: #other girl is fine
                        if not Player.Male:
                            "Она расстегивает молнию на ваших штанах под столом и начинает ласкать вашу киску, в то время, как [Previous.Name] делает вид, что чем-то занята."
                        else:
                            "Она расстегивает молнию на ваших штанах под столом и начинает ласкать ваш член, в то время, как [Previous.Name] делает вид, что чем-то занята."
                        $ Line = "She"
                else:
                        if not Player.Male:
                            "Она расстегивает ваши штаны под столом и начинает ласкать вашу киску."
                        else:
                            "Она расстегивает ваши штаны под столом и начинает ласкать ваш член."
                        $ Line = "She"
                if (Girl.Blow or Girl.CUN) and (ApprovalCheck(Girl, 1200) or Girl is JubesX):
                        if Player.Male:
                                "Как только вы хотите кончить, [Girl.Name] ныряет головой под стол, а выныривает с уже набитым ртом."
                                $ Girl.SeenPeen += 1
                                $ Girl.Blow += 1
                        else:
                                "Как только вы хотите кончить, [Girl.Name] ныряет головой под стол, а выныривает с влажным  от соков подбородком."
                                $ Girl.SeenPuss += 1
                                $ Girl.CUN += 1
                        $ Girl.Addict -= 20
                        $ Girl.Swallow += 1
                        $ Girl.RecentActions.append("swallow")
                        $ Girl.DailyActions.append("swallow")
                else:
                        "[Line] продолжает ласкать ваш член, пока вы не кончаете в салфетку."
                        if Girl is RogueX:
                                ch_r "Уверена, уборщики будут в восторге."
                        elif Girl is KittyX:
                                ch_k "Мне немного жаль официантов."
                        elif Girl is EmmaX:
                                ch_e "Уверена, уборщики будут в восторге."
                        elif Girl is LauraX:
                                ch_l "Извини за беспорядок."
                        elif Girl is JeanX:
                                ch_j "Официант? Убери это."
                        elif Girl is StormX:
                                ch_s "Мы должны оставить хорошие чаевые, [Girl.Petname]."
                        elif Girl is JubesX:
                                "Затем она все слизывает..."
                                ch_v "Мои благодарности шефу..."
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.RecentActions.append("swallow")
                                $ Girl.DailyActions.append("swallow")
                        elif Girl is GwenX:
                                ch_g "Давай... добавмс ее к чистым..."
                                $ GwenX.AddWord(1,0,0,"napkin") #trait
                        elif Girl is BetsyX:
                                ch_b "Я очень надеюсь, что тебе понравилось..."
                        elif Girl is DoreenX:
                                ch_d "Надо прибраться..."
                        elif Girl is WandaX:
                                "Салфетка исчезает во вспышке синего света."
                $ Line = 0
                $ Girl.Statup("Inbt", 30, 4)
                $ Girl.Statup("Inbt", 80, 2)
                if Player.Male:
                        $ Girl.Hand += 1
                        $ Girl.RecentActions.append("hand")
                        $ Girl.DailyActions.append("hand")
                else:
                        $ Girl.Finger += 1
                        $ Girl.RecentActions.append("finger")
                        $ Girl.DailyActions.append("finger")
                $ Player.Semen -= 1
                $ Girl.Addict -= 5
                if _return == 3:
                    "[Previous.Name] сверлит вас обоих взглядом."
                    call Date_Bonus(Previous,-5)
    elif OptionsDS[0] == "pussy":
        "В середине трапезы, хитрая улыбка появляется на лице [Girl.Name_rod] и она переставляет свой стул поближе к вам."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4:
                #you refused
                if Girl.Legs:
                    "Она берет вашу руку и тянет ее к своей промежности, а затем засовывает ее под одежду."
                else:
                    "Она берет вашу руку и засовывает ее себе между ног."
                $ Girl.FaceChange("sadside", 2)
                "Взглянув на [Previous.Name_rod], вы одергиваете свою руку."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -5)
                call Date_Bonus(Girl,-3)
        else:
                if Girl.Legs:
                        "Она берет вашу руку и тянет ее к своей промежности, а затем засовывает ее себе под [get_clothing_name(Girl.Legs_key, vin)]."
                else:
                        "Она берет вашу руку и засовывает ее себе между ног."
                "Вы чувствуете, что там тепло, словно в печи."
                if _return == 1:
                        #other girl is in on it
                        "С другой стороны, [Previous.Name] также залазит рукой под стол и присоединяется к вам."
                        "Вы вместе ласкаете ее киску в течение нескольких минут, пока, наконец, ее не начинает трясти от оргазма."
                        "Вы медленно убираете свои руки с похотливой улыбкой."
                        $ Girl.GLG(Previous,700,6,1)
                        $ Girl.GLG(Previous,1000,6,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else:
                        "Вы ласкаете ее киску в течение нескольких минут, пока, наконец, ее не начинает трясти от оргазма."
                        "Вы медленно убераете свою руку с похотливой улыбкой."
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                if Girl is RogueX:
                        ch_r "Мне нужно было сбросить напряжение, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Спасибо, [Girl.Petname], Мне это было необходимо."
                elif Girl is EmmaX:
                        ch_e "Ах, это было прекрасно, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Уф, это было здорово."
                elif Girl is JeanX:
                        ch_j "Ладно, все было неплохо."
                elif Girl is StormX:
                        ch_s "Благодарю, это было чудесно, [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "Я нуждалась в этом, [Girl.Petname]..."
                elif Girl is GwenX:
                        ch_g "Было приятно, знаешь, выпустить пар..."
                elif Girl is BetsyX:
                        ch_b "Это было восхитительно, спасибо."
                elif Girl is DoreenX:
                        ch_d "Я испачкала твою руку?.."
                elif Girl is WandaX:
                        ch_w "Спасибо, [Girl.Petname]..."
                if _return == 1:
                        #if the other girl joined in...
                        if Girl is RogueX:
                                ch_r "И тебе тоже спасибо, [Previous.Name]."
                        elif Girl is KittyX:
                                ch_k "И тебе спасибо, [Previous.Name]."
                        elif Girl is EmmaX:
                                ch_e "И тебе тоже спасибо, [Previous.Name]."
                        elif Girl is LauraX:
                                ch_l "И тебе спасибо, [Previous.Name]."
                        elif Girl is JeanX:
                                ch_j "Мне понравилась твоя инициатива, [Previous.Name]."
                        elif Girl is StormX:
                                ch_s "Благодарю, [Previous.Petname]."
                        elif Girl is JubesX:
                                ch_v "И тебе спасибо за помощь, [Previous.Petname]."
                        elif Girl is GwenX:
                                ch_g "И ты, [Previous.Petname], ты тоже очень помогла!"
                        elif Girl is BetsyX:
                                ch_b "И тебе тоже спасибо, [Previous.Petname]."
                        elif Girl is DoreenX:
                                ch_d "И тебе спасибо за оказанную помощь, [Previous.Petname]..."
                        elif Girl is WandaX:
                                ch_w "И, безусловно, я благодарна тебе, [Previous.Name]..."
                        $ Girl.Les += 1
                        $ Previous.Les += 1
                $ Girl.Addict -= 5
                $ Girl.Statup("Love", 90, 3)
                $ Girl.Statup("Inbt", 30, 5)
                $ Girl.Statup("Inbt", 90, 2)
                $ Girl.FondleP += 1
                $ Girl.Org += 1
                $ Girl.RecentActions.append("fondle pussy")
                $ Girl.RecentActions.append("dinnersex")
                $ Girl.DailyActions.append("fondle pussy")
    elif OptionsDS[0] == "foot":
        "В середине трапезы, хитрая улыбка появляется на лице [Girl.Name_rod] и она переставляет свой стул немного ближе к вам."
        if not Player.Male:
            "Вы вдруг чувствуете ее ногу на своих коленях, нежно ласкающую вашу киску."
        else:
            "Вы вдруг чувствуете ее ногу на своих коленях, нежно ласкающую ваш член."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "Вы нерешительно отодвигаетесь и отталкиваете ее ногу."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -3)
                call Date_Bonus(Girl,-1)
        else:
                $ Player.Statup("Focus", 60, 10)
                if _return == 1: #other girl is fine
                        "[Previous.Name] решает присоединиться к веселью и добавляет свою ногу к вам."
                        $ Player.Statup("Focus", 60, 5)
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                if _return == 3:
                        call Date_Bonus(Previous,-3)
                "Через несколько минут она отстраняется."
                if Girl is RogueX:
                    ch_r "Просто немного предварительных ласк, [Girl.Petname]."
                elif Girl is KittyX:
                    ch_k "Интрига на будущее, [Girl.Petname]."
                elif Girl is EmmaX:
                    ch_e "Терпение... [Girl.Petname]."
                elif Girl is LauraX:
                    ch_l "У меня есть кое-какие планы на сегодняшний вечер, [Girl.Petname]."
                elif Girl is JeanX:
                    ch_j "Потерпишь ее немного?"
                elif Girl is StormX:
                    ch_s "Чувствую, мне пока нужно... сдержаться, [Girl.Petname]."
                elif Girl is JubesX:
                    if not Player.Male:
                        ch_v "Надеюсь, ты получила сообщение, [Girl.Petname]..."
                    else:
                        ch_v "Надеюсь, ты получил сообщение, [Girl.Petname]..."
                elif Girl is GwenX:
                    ch_g "Запомни это чувство..."
                elif Girl is BetsyX:
                        ch_b "С нетерпением жду конец вечера."
                elif Girl is DoreenX:
                        ch_d "Надеюсь, я донесла свое желание до тебя..."
                elif Girl is WandaX:
                        ch_w "Позже мы можем продолжить..."
                $ Girl.Statup("Inbt", 80, 3)
                $ Girl.RecentActions.append("dinnersex")

    $ Girl.Blush = 0
    return
# End Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




#Start Movie Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_Movies:  #rkeljsvgb
    #This picks and watches a movie
    $ bg_current = "bg movies"
    $ Player.RecentActions.append("movie")
    $ Player.DailyActions.append("movie")
    $ BO = Party[:]
    while BO:
        $ BO[0].Loc = "bg movies"
        $ BO.remove(BO[0])

    call Set_The_Scene

    menu:
        "Что вы хотели бы посмотреть?"
        "Романтическую комедию.":
            $ Line = "romcom"
            $ Player.RecentActions.append("romcom")
        "Боевик.":
            $ Line = "action"
            $ Player.RecentActions.append("action")
        "Фильм ужасов.":
            $ Line = "horror"
            $ Player.RecentActions.append("horror")
        "Нашумевшую драму.":
            $ Line = "drama"
            $ Player.RecentActions.append("drama")
        "Позволить выбрать [RogueX.Name_dat]." if RogueX in Party:
            $ Line = "pick"
            $ Trigger = RogueX
        "Позволить выбрать [KittyX.Name_dat]." if KittyX in Party:
            $ Line = "pick"
            $ Trigger = KittyX
        "Позволить выбрать [EmmaX.Name_dat]." if EmmaX in Party:
            $ Line = "pick"
            $ Trigger = EmmaX
        "Позволить выбрать [LauraX.Name_dat]." if LauraX in Party:
            $ Line = "pick"
            $ Trigger = LauraX
        "Позволить выбрать [JeanX.Name_dat]." if JeanX in Party:
            $ Line = "pick"
            $ Trigger = JeanX
        "Позволить выбрать [StormX.Name_dat]." if StormX in Party:
            $ Line = "pick"
            $ Trigger = StormX
        "Позволить выбрать [JubesX.Name_dat]." if JubesX in Party:
            $ Line = "pick"
            $ Trigger = JubesX
        "Позволить выбрать [GwenX.Name_dat]." if GwenX in Party:
            $ Line = "pick"
            $ Trigger = GwenX
        "Позволить выбрать [BetsyX.Name_dat]." if BetsyX in Party:
            $ Line = "pick"
            $ Trigger = BetsyX
        "Позволить выбрать [DoreenX.Name_dat]." if DoreenX in Party:
            $ Line = "pick"
            $ Trigger = DoreenX
        "Позволить выбрать [WandaX.Name_dat]." if WandaX in Party:
            $ Line = "pick"
            $ Trigger = WandaX


    if Line == "pick":
            #if you let one of the girls pick the movie
            $ Trigger.FaceChange("smile")
            if Trigger is RogueX:
                    $ Trigger.Statup("Love", 80, 4)
                    $ Trigger.Statup("Obed", 50, -2)
                    $ Trigger.Statup("Inbt", 50, 2)
                    ch_r "Как мило, [RogueX.Petname]. Давай посмотрим романтическую комедию."
                    $ Line = "romcom"
            elif Trigger is KittyX:
                    $ Trigger.Statup("Love", 80, 4)
                    $ Trigger.Statup("Obed", 50, -2)
                    $ Trigger.Statup("Inbt", 50, 2)
                    ch_k "Ах, [KittyX.Petname]. Давай посмотрим драму."
                    $ Line = "drama"
            elif Trigger is EmmaX:
                    $ Trigger.Statup("Love", 80, 5)
                    $ Trigger.Statup("Obed", 50, -3)
                    $ Trigger.Statup("Inbt", 50, 3)
                    ch_e "Ох, замечательно. Давай посмотрим фильм ужасов."
                    $ Line = "horror"
            elif Trigger is LauraX:
                    $ Trigger.Statup("Love", 90, 5)
                    $ Trigger.Statup("Obed", 50, 2)
                    $ Trigger.Statup("Inbt", 50, 2)
                    ch_l "Клево. Давай посмотрим какой-нибудь боевик."
                    $ Line = "action"
            elif Trigger is JeanX:
                    $ Trigger.Statup("Love", 60, 2)
                    $ Trigger.Statup("Love", 90, 3)
                    $ Trigger.Statup("Obed", 50, 2)
                    $ Trigger.Statup("Inbt", 70, 2)
                    ch_j "Думаю, романтическая комедия нас развлечет."
                    $ Line = "romcom"
            elif Trigger is StormX:
                    $ Trigger.Statup("Love", 80, 5)
                    $ Trigger.Statup("Inbt", 50, 3)
                    $ Trigger.Statup("Inbt", 80, 1)
                    ch_s "Тогда давай посмотрим драму. Я слышала, про этот фильм много хорошего."
                    $ Line = "drama"
            elif Trigger is JubesX:
                    $ Trigger.Statup("Love", 80, 4)
                    $ Trigger.Statup("Obed", 50, 2)
                    $ Trigger.Statup("Inbt", 50, 2)
                    ch_v "О, конечно же \"боевик.\""
                    $ Line = "action"
            elif Trigger is GwenX:
                    $ Trigger.Statup("Love", 80, 4)
                    $ Trigger.Statup("Obed", 50, 1)
                    $ Trigger.Statup("Inbt", 50, 2)
                    ch_g "Думаю, новая комедия будет веселой!"
                    $ Line = "romcom"
            elif Trigger is BetsyX:
                    $ Trigger.Statup("Love", 80, 3)
                    $ Trigger.Statup("Obed", 50, 2)
                    $ Trigger.Statup("Inbt", 60, 3)
                    ch_b "О, я не прочь посмотреть какой-нибудь боевик!"
                    $ Line = "action"
            elif Trigger is DoreenX:
                    $ Trigger.Statup("Love", 50, 1)
                    $ Trigger.Statup("Love", 80, 3)
                    $ Trigger.Statup("Obed", 50, 2)
                    $ Trigger.Statup("Inbt", 60, 3)
                    ch_d "О, тут недавно вышла новая драма, мне кажется, она может быть очень интересной!"
                    $ Line = "drama"
            if Trigger is WandaX:
                    $ WandaX.FaceChange("smile")
                    $ WandaX.Statup("Love", 80, 2)
                    $ WandaX.Statup("Love", 200, 1)
                    $ WandaX.Statup("Obed", 60, 2)
                    ch_w "Мне очень нравятся драмы. . ."
                    $ Line = "drama"
            $ Player.RecentActions.append(Line)
            call Date_Bonus(Trigger,20)

    if Line == "romcom":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("smile", Eyes="surprised")
                    $ RogueX.Statup("Love", 50, 2)
                    $ RogueX.Statup("Love", 95, 4)
                    $ RogueX.Statup("Inbt", 50, 2)
                    ch_r "Ооох, мне нравятся хорошие романтические комедии, [RogueX.Petname]!"
                    call Date_Bonus(RogueX,15)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("smile", Eyes="surprised")
                    $ KittyX.Statup("Love", 50, 2)
                    $ KittyX.Statup("Love", 95, 3)
                    ch_k "Ах, как миииило!"
                    call Date_Bonus(KittyX,10)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("confused", Mouth="sad")
                    $ EmmaX.Statup("Love", 70, 2)
                    $ EmmaX.Statup("Obed", 50, 5)
                    $ EmmaX.Statup("Inbt", 70, -3)
                    ch_e "Как. . . скучно."
                    call Date_Bonus(EmmaX,-5)
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("smile", 2)
                    $ LauraX.Statup("Love", 80, 3)
                    $ LauraX.Statup("Obed", 50, 3)
                    $ LauraX.Statup("Inbt", 60, 3)
                    ch_l "Ладно. . . пойдет."
                    call Date_Bonus(LauraX,5)
            if JeanX in Party and Trigger != JeanX:
                    $ JeanX.FaceChange("smile")
                    $ JeanX.Statup("Love", 80, 3)
                    $ JeanX.Statup("Obed", 50, 3)
                    $ JeanX.Statup("Inbt", 60, 3)
                    ch_j "О, отличный выбор."
                    call Date_Bonus(JeanX,10)
            if StormX in Party and Trigger != StormX:
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 2)
                    $ StormX.Statup("Obed", 50, 1)
                    ch_s "А ты в душе настоящий романтик."
                    call Date_Bonus(StormX,10)
            if JubesX in Party and Trigger != JubesX:
                    $ JubesX.FaceChange("smile")
                    $ JubesX.Statup("Love", 50, 2)
                    $ JubesX.Statup("Love", 95, 3)
                    ch_v "Ага, ладно."
                    call Date_Bonus(JubesX,5)
            if GwenX in Party and Trigger != GwenX:
                    $ GwenX.FaceChange("smile")
                    $ GwenX.Statup("Love", 50, 2)
                    $ GwenX.Statup("Love", 95, 3)
                    $ GwenX.Statup("Inbt", 50, 2)
                    ch_g "Отлично! Я надеялась, что ты сделаешь именно такой выбор!"
                    call Date_Bonus(GwenX,15)
            if BetsyX in Party and Trigger != BetsyX:
                    $ BetsyX.FaceChange("smile")
                    $ BetsyX.Statup("Love", 80, 3)
                    $ BetsyX.Statup("Obed", 50, 2)
                    $ BetsyX.Statup("Inbt", 60, 3)
                    ch_b "Мне нравится иногда смотреть романтические фильмы."
                    call Date_Bonus(BetsyX,10)
            if DoreenX in Party and Trigger != DoreenX:
                    $ DoreenX.FaceChange("bemused",1,Eyes="side")
                    $ DoreenX.Statup("Love", 80, 2)
                    $ DoreenX.Statup("Inbt", 60, 2)
                    ch_d "Это будет весело!"
                    call Date_Bonus(DoreenX,10)
            if WandaX in Party and Trigger != WandaX:
                    $ WandaX.FaceChange("bemused",1,Eyes="side")
                    $ WandaX.Statup("Love", 80, 2)
                    $ WandaX.Statup("Inbt", 60, 2)
                    ch_w "Романтические истории могут быть очень интересными. . ."
                    call Date_Bonus(WandaX,10)
    elif Line == "action":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("sexy")
                    ch_r "Хм, знаешь, я всегда готова к каким-нибудь боевикам."
                    $ RogueX.Statup("Love", 95, 3)
                    call Date_Bonus(RogueX,5)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Love", 95, 4)
                    $ KittyX.Statup("Inbt", 50, 2)
                    ch_k "Боевики - это весело."
                    call Date_Bonus(KittyX,5)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("sadside", Brows="angry")
                    $ EmmaX.Statup("Love", 70, -2)
                    $ EmmaX.Statup("Obed", 50, 5)
                    ch_e "Полагаю, сойдет убить время."
                    # call Date_Bonus(EmmaX,0)
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("smile")
                    $ LauraX.Statup("Love", 70, 5)
                    $ LauraX.Statup("Obed", 50, 5)
                    ch_l "Потрясающе!"
                    call Date_Bonus(LauraX,10)
            if JeanX in Party and Trigger != JeanX:
                    $ JeanX.FaceChange("smile")
                    $ JeanX.Statup("Obed", 50, 3)
                    $ JeanX.Statup("Inbt", 60, 2)
                    ch_j "Думаю, меня устроит."
                    call Date_Bonus(JeanX,5)
            if StormX in Party and Trigger != StormX:
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 2)
                    $ StormX.Statup("Obed", 50, 1)
                    ch_s "Будем надеятся, это будет динамичный фильм."
                    call Date_Bonus(StormX,5)
            if JubesX in Party and Trigger != JubesX:
                    $ JubesX.FaceChange("smile")
                    $ JubesX.Statup("Love", 95, 5)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Inbt", 50, 2)
                    ch_v "Я люблю смотреть всякие боевики!"
                    call Date_Bonus(JubesX,15)
            if GwenX in Party and Trigger != GwenX:
                    $ GwenX.FaceChange("smile")
                    $ GwenX.Statup("Love", 95, 2)
                    $ GwenX.Statup("Obed", 50, 2)
                    ch_g "Пиу пиу!"
                    call Date_Bonus(GwenX,10)
            if BetsyX in Party and Trigger != BetsyX:
                    $ BetsyX.FaceChange("smile")
                    $ BetsyX.Statup("Love", 80, 3)
                    $ BetsyX.Statup("Obed", 50, 2)
                    $ BetsyX.Statup("Inbt", 60, 3)
                    ch_b "О, мне очень нравятся боевики!"
                    call Date_Bonus(BetsyX,15)
            if DoreenX in Party and Trigger != DoreenX:
                    $ DoreenX.FaceChange("bemused",Eyes="side")
                    $ DoreenX.Statup("Love", 80, 1)
                    $ DoreenX.Statup("Obed", 50, 2)
                    ch_d "Мне нравятся боевики, по крайней мере иногда. . ."
                    call Date_Bonus(DoreenX,10)
            if WandaX in Party and Trigger != WandaX:
                    $ WandaX.FaceChange("bemused",1,Eyes="side")
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 70, 2)
                    ch_w "В процессе. . . я могу выйти из себя. . ."
                    call Date_Bonus(WandaX,5)
    elif Line == "horror":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("sad", Eyes="surprised")
                    $ RogueX.Statup("Love", 90, -3)
                    $ RogueX.Statup("Obed", 50, 3)
                    $ RogueX.Statup("Obed", 80, 2)
                    ch_r "Мне не очень нравятся страшные фильмы, [RogueX.Petname]."
                    # call Date_Bonus(RogueX,0)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("sad", Eyes="surprised")
                    $ KittyX.Statup("Love", 90, -5)
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Obed", 80, 2)
                    ch_k "Он ведь не будет {i}слишком{/i} страшным, правда?"
                    call Date_Bonus(KittyX,-5)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("sly")
                    $ EmmaX.Statup("Love", 70, 3)
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    $ EmmaX.Statup("Lust", 60, 5)
                    ch_e "Я люблю, когда по моей спине пробегает холодок."
                    call Date_Bonus(EmmaX,15)
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("normal")
                    $ LauraX.Statup("Obed", 50, 3)
                    ch_l "Уверна, будет страшно."
                    #call Date_Bonus(LauraX,0)
            if JeanX in Party and Trigger != JeanX:
                    $ JeanX.FaceChange("sadside")
                    $ JeanX.Statup("Love", 70, -1)
                    $ JeanX.Statup("Obed", 70, 3)
                    $ JeanX.Statup("Inbt", 60, 1)
                    ch_j "Похоже, будет скучно."
                    #call Date_Bonus(JeanX,0)
            if StormX in Party and Trigger != StormX:
                    $ StormX.FaceChange("sad")
                    $ StormX.Statup("Love", 70, 1)
                    $ StormX.Statup("Obed", 50, 1)
                    $ StormX.Statup("Inbt", 50, 1)
                    ch_s "Я. . . не люблю ужасы."
                    #call Date_Bonus(StormX,0)
            if JubesX in Party and Trigger != JubesX:
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Obed", 80, 2)
                    ch_v "Мне хватает этого и дома. . ."
                    call Date_Bonus(JubesX,-5)
            if GwenX in Party and Trigger != GwenX:
                    $ GwenX.FaceChange("smile")
                    $ GwenX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Obed", 50, 2)
                    ch_g "Оооо, ужааастик. . ."
                    call Date_Bonus(GwenX,5)
            if BetsyX in Party and Trigger != BetsyX:
                    $ BetsyX.FaceChange("sadside")
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 50, 3)
                    $ BetsyX.Statup("Inbt", 60, 1)
                    ch_b "Должна сказать, ужасы мне не нравятся. . ."
                    call Date_Bonus(BetsyX,5)
            if DoreenX in Party and Trigger != DoreenX:
                    $ DoreenX.FaceChange("bemused",Eyes="side")
                    $ DoreenX.Statup("Love", 80, -1)
                    $ DoreenX.Statup("Obed", 50, 2)
                    ch_d "Даже не знаю, мне они как-то не заходят. . ."
                    call Date_Bonus(DoreenX,5)
            if WandaX in Party and Trigger != WandaX:
                    $ WandaX.FaceChange("bemused",1,Eyes="side")
                    $ WandaX.Statup("Love", 80, -2)
                    $ WandaX.Statup("Obed", 60, 2)
                    ch_w "Я не могу без напряжение смотреть подобные фильмы. . ."
                    call Date_Bonus(WandaX,5)
    elif Line == "drama":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("bemused")
                    $ RogueX.Statup("Love", 95, 1)
                    $ RogueX.Statup("Obed", 50, 3)
                    ch_r "Хммм, о этом фильме я слышала много хорошего, возможно, он нам понравится."
                    call Date_Bonus(RogueX,5)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("bemused")
                    $ KittyX.Statup("Love", 95, 3)
                    $ KittyX.Statup("Obed", 50, 2)
                    ch_k "Я слышала, что этот фильм хорош!"
                    call Date_Bonus(KittyX,15)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("normal")
                    $ EmmaX.Statup("Love", 70, 2)
                    $ EmmaX.Statup("Obed", 50, 3)
                    ch_e "Ах, интересный выбор."
                    call Date_Bonus(EmmaX,5)
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("normal")
                    $ LauraX.Statup("Obed", 50, 3)
                    ch_l "Фу."
                    #call Date_Bonus(LauraX,0)
            if JeanX in Party and Trigger != JeanX:
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Love", 60, -3)
                    $ JeanX.Statup("Love", 80, -2)
                    $ JeanX.Statup("Obed", 50, 2)
                    $ JeanX.Statup("Obed", 80, 2)
                    $ JeanX.Statup("Inbt", 60, 3)
                    ch_j "Скууууука."
                    call Date_Bonus(JeanX,10)
            if StormX in Party and Trigger != StormX:
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 50, 3)
                    $ StormX.Statup("Love", 80, 3)
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Obed", 80, 1)
                    $ StormX.Statup("Inbt", 50, 3)
                    ch_s "Ах, прекрасный выбор. Я слышала, про этот фильм много хорошего."
                    call Date_Bonus(StormX,15)
            if JubesX in Party and Trigger != JubesX:
                    $ JubesX.FaceChange("bemused")
                    $ JubesX.Statup("Love", 95, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                    ch_v "Ага, ладно. . ."
                    call Date_Bonus(JubesX,5)
            if GwenX in Party and Trigger != GwenX:
                    $ GwenX.FaceChange("sad")
                    $ GwenX.Statup("Love", 50, -2)
                    ch_g "Ох, мне кажется, он -очень- скучный. . ."
                    call Date_Bonus(GwenX,5)
            if BetsyX in Party and Trigger != BetsyX:
                    $ BetsyX.FaceChange("bemused",Eyes="side")
                    $ BetsyX.Statup("Obed", 50, 2)
                    $ BetsyX.Statup("Inbt", 60, 2)
                    ch_b "Частенько в таких фильмах заезженный сюжет. . ."
                    call Date_Bonus(BetsyX,10)
            if DoreenX in Party and Trigger != DoreenX:
                    $ DoreenX.FaceChange("smile")
                    $ DoreenX.Statup("Love", 70, 3)
                    $ DoreenX.Statup("Love", 90, 1)
                    $ DoreenX.Statup("Inbt", 60, 2)
                    ch_d "О, я слышала много хорошего об этом фильме!"
                    call Date_Bonus(DoreenX,10)
            if WandaX in Party and Trigger != WandaX:
                    $ WandaX.FaceChange("smile")
                    $ WandaX.Statup("Love", 80, 2)
                    $ WandaX.Statup("Love", 200, 1)
                    $ WandaX.Statup("Obed", 60, 2)
                    ch_w "Мне нравятся дрымы. . ."
                    call Date_Bonus(WandaX,20)
    $ Trigger = 0

    call Date_Paying("movie")

    if not Party:
            #if you're ditched,
            "Вы все равно решили посмотреть этот фильм, но он был довольно скучным."
            "После него вы просто возвращаетесь в свою комнату."
            jump Date_Over

    $ Player.RecentActions.append("movie")
    #The movie plays.
    if len(Party) >= 2:
        "Вы занимаете свое место между двумя девушками."
    else:
        "Вы занимаете свои места."

    if "romcom" in Player.RecentActions:
        $ Line = renpy.random.choice(["Вы смотрите фильм, в котором немного придурковатая девушка не может выбрать между двумя храбрыми парнями. В итоге, она выбирает совершенно другого.",
                    "Вы смотрите фильм, в котором девушку безжалостно преследует какой-то странный парень, пока она не решает, что любит его. После этого они живут долго и счастливо.",
                    "В этом фильме главная героиня отправляется на свадьбы всех своих друзей, но у нее самой ничего не получается на личном фронте. Она умирает в одиночесте. Шутка. В конце она выходит замуж.",
                    "Вы смотрите фильм, в котором куча девочек из колледжа отправляется в безумное приключение и с большим количеством случайного секса.",
                    "Этот фильм рассказывает о девушке, которую убедили жить в подземелье ради секса, и ей очень это понравилось.",
                    "Этот фильм рассказывает о девушке, которая работает в доме моды и над которой издевался ее босс, пока они не становятся друзьями."])
    elif "action" in Player.RecentActions:
        $ Line = renpy.random.choice(["Вы смотрите фильм, который рассказывает о бывшем морском котике, который сражается против пришельцев.",
                    "Вы смотрите фильм, в котором девушку безжалостно преследует какой-то странный парень, пока она не решает, что любит его. После этого они живут долго и счастливо. А еще в нем очень много взрывов",
                    "В этом фильме гигантские роботы сражаются против толп гуманоидных животных, с судьбой мира на кону.",
                    "Вы смотрите фильм, в котором команда супергероев, не являющихся мутантами, судя по всему, сражается с серебристыми роботами в Восточной Европе.",
                    "Этот фильм о мужике со сверхчеловеческими силами, который почти что сравнял с землей целый город, и все же не был арестован за это. Должно быть, дело в его молоте.",
                    "В этом фильме нет ничего, кроме 90 минут постоянных взрывов и световых бликов."])
    elif "horror" in Player.RecentActions:
        $ Line = renpy.random.choice(["Вы смотрите фильм, в котором немного придурковатая девушка не может выбрать между двумя храбрыми парнями. В итоге, она выбирает совершенно другого. А теми парнями были человек-рыба и скелет.",
                    "Вы смотрите фильм, в котором девушку безжалостно преследует какой-то странный парень, пока она наконец не сдается и выходит за него замуж. После этого ее жизнь превращается в настоящий ад.",
                    "В этом фильме группа подростков оказывается заперта в лесной хижине. Они много трахаются, в то время, как какой-то монстр из тени убивает их одного за другим.",
                    "В этом фильме группа подростков находится в заброшенном мотеле. Они много трахаются, в то время, как какой-то монстр из тени убивает их одного за другим.",
                    "Этот фильм рассказывает о девушке, которую убедили жить в подземелье ради секса, и ей действительно это нравится. Но в конце ее убивают.",
                    "В этом фильме группа подростков оказывается в ловушке на космическом корабле. Они много трахаются, в то время, как какой-то монстр из тени убивает их одного за другим. Кому-то из них успевают вставить, анальный зонд."])
    elif "drama" in Player.RecentActions:
        $ Line = renpy.random.choice(["Вы смотрите фильм о зрелой женщине, которая не может выбрать между двумя овдовевшими состоятельными мужчинами. В итоге, она выбрала совершенно другого.",
                    "Вы смотрите фильм, который представляет собой документальный фильм о девушке, которую безжалостно преследует какой-то странный парень, пока она в конце концов не решает обратиться в органы, и ему запрещают к ней приближатся.",
                    "Вы смотрите фильм, который является биографией великого исторического лидера, а еще он был неплохим художником.",
                    "Вы смотрите фильм, в котором инвалид борется со своими различными недостатками и в конечном итоге побеждает их и/или умирает.",
                    "В этом фильме много слез и криков, в то время, как режисером освещаются некоторые очень серьезные проблемы человечества."])

    "[Line]" #You watch the movie...

    call Movie_Sex

    $ Round -= 60 if Round > 70 else (Round-10) #reduces Round to at minimum 10

    if Party and "dategirltalk" in Party[0].RecentActions:
            $ Party[0].DrainWord("dategirltalk",1,0) #removes from recent
            "Начинаются титры, [Party[0].Name] выглядит немного обеспокоенной."
            call expression Party[0].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
    elif len(Party) > 1 and "dategirltalk" in Party[1].RecentActions:
            $ Party[1].DrainWord("dategirltalk",1,0) #removes from recent
            "Начинаются титры, [Party[1].Name] выглядит немного обеспокоенной."
            call expression Party[1].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

    if Round < 20:
            "Выйдя из кинотеатра, вы замечаете, что уже темнеет, и решаете вернуться в общежитие. . ."
            jump Date_End

    if not Party:
            "После кина, вы решаете вернуться в свою комнату."
            jump Date_Over

    "Похоже, у вас осталось немного времени, куда бы вы хотели отправиться дальше?"
    jump Date_Location #picks next stop...

#end Movie Sequence  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Movie_Sex(Girl=0,Previous=0,GirlBonus=0, OptionsDS=[],BO=[]):#rkeljsvgb
    # Called by Date_Sex
    $ BO = Party[:]
    if 0 in BO:
        $ BO.remove(0)
    while BO:
            if ApprovalCheck(BO[0], 1000) and "friendly" not in BO[0].DailyActions:  #Checks if BO[0] is in
                    $ OptionsDS.append(BO[0])
                    if Party[0] is BO[0] and Date_Bonus[0] > 10:
                            $ OptionsDS.append(BO[0])
                    elif BO[0] in Party and Date_Bonus[1] > 10:
                            $ OptionsDS.append(BO[0])
                    if "horror" in Player.RecentActions:
                            $ OptionsDS.append(BO[0])
                    elif "drama" in Player.RecentActions:
                            $ OptionsDS.append(BO[0])
                    elif BO[0] is LauraX and "action" in Player.RecentActions:
                            $ OptionsDS.append(BO[0])
            $ BO.remove(BO[0])

    if len(OptionsDS) == 0:
            #if nobody is in, return
            return

    $ renpy.random.shuffle(OptionsDS)

    $ Girl = OptionsDS[0]
    if len(Party) >= 2:
            if Girl is Party[0]:
                    $ Previous = Party[1]
            else:
                    $ Previous = Party[0]

    if Girl is Previous:
        "Tell Oni that on a date, a girl and previous were the same, [Girl.Tag], MS"

    $ OptionsDS = ["nothing"]

    if Party[0] is Girl:
        $ GirlBonus = Date_Bonus[0] + Date_Cost[0]
    else:
        $ GirlBonus = Date_Bonus[1] + Date_Cost[1]

    if ApprovalCheck(Girl, 500, Bonus=(10*GirlBonus)):
        $ Girl.FaceChange("kiss", 1)
        if "romcom" in Player.RecentActions:
                "Посреди фильма, вдохновленная действиями на экране, [Girl.Name] поворачивается к вам и начинает страстно целовать."
        elif "action" in Player.RecentActions:
                "Посреди фильма, под воздействием адреналина из-за происходящего на экране, [Girl.Name] поворачивается к вам и начинает вас целовать."
        elif "horror" in Player.RecentActions:
                if Girl is EmmaX:
                        "Посреди фильма, от скуки [Girl.Name] пожимает плечами, поворачивается к вам и начинает вас целовать."
                elif Girl is LauraX:
                        "Посреди фильма, заскучавшая от \"напряжения\" на экране [Girl.Name] поворачивается к вам и начинает вас целовать."
                else:
                        "Посреди фильма, напуганная происходящим на экране [Girl.Name] решает найти утешение в ваших объятиях и, спустя какое-то время, начинает вас целовать."
        elif "drama" in Player.RecentActions:
                if Girl in (RogueX,EmmaX):
                        "Посреди фильма, от сильной скуки [Girl.Name] поворачивается к вам, пожимает плечами и начинает вас целовать."
                else:
                        "Посреди фильма, [Girl.Name] поворачивается к вам, пожимает плечами и начинает вас целовать."
        $ Girl.RecentActions.append("kissing")
        $ Girl.RecentActions.append("moviesex")
        $ Girl.DailyActions.append("kissing")
        call Date_Sex_Break(Girl,Previous)
        if _return == 4:
                #the other girl stops you
                "Вы устраиваетесь поудобнее на своих местах и досматриваете оставшуюся часть фильма."
                return
        elif Previous and _return == 1:
                #the other girl joins in...
                "[Previous.Name] также наклоняется и начинает целовать вас обоих по очереди."
        elif Previous and  _return == 3:
                #the other girl is mad...
                "Вы возвращаетесь к фильму, [Previous.Name] усаживается обратно на свое место с сердитым видом."

        if Girl.Anal and ApprovalCheck(Girl, 2000, Bonus=(10*GirlBonus)) and Girl.PantsNum() <= 5 and Player.Male:
                $ OptionsDS.append("anal")
        if Girl.Sex and ApprovalCheck(Girl, 2000, Bonus=(10*GirlBonus)) and Girl.PantsNum() <= 5 and Player.Male:
                $ OptionsDS.append("sex")
        if (Girl.Blow or Girl.CUN) and ApprovalCheck(Girl, 1300, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("blow")
                if Girl is JubesX:
                    $ OptionsDS.append("blow")
                    $ OptionsDS.append("blow")
        if (Girl.Hand or Girl.Finger) and ApprovalCheck(Girl, 1000, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("hand")
        if Girl.FondleP and ApprovalCheck(Girl, 900, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("pussy")
        elif ApprovalCheck(Girl, 1200, Bonus=(5*GirlBonus)) and Girl.Panties:
                $ OptionsDS.append("panties")
        elif ApprovalCheck(Girl, 1200, Bonus=(5*GirlBonus)):
                $ OptionsDS.append("flash")

        $ renpy.random.shuffle(OptionsDS)


        if OptionsDS[0] == "anal":
                    $ Girl.FaceChange("sexy", 1)
                    if Girl.Panties:
                        "Во время поцелуя [Girl.Name] протягивает руку и расстегивает вашу ширинку. Она стягивает свои трусики и садится к вам на колени."
                    elif Girl.PantsNum() == 5:
                        "Во время поцелуя [Girl.Name] протягивает руку и расстегивает вашу ширинку. Она слегка задирает свою юбку и садится к вам на колени."
                    else:
                        "Во время поцелуя [Girl.Name] протягивает руку и расстегивает вашу ширинку. Затем она садится к вам на колени."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out...
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway..."
                    "Она осторожно нанизывается своей попкой на ваш член и начинает скакать вверх-вниз, стараясь не шуметь, чтобы другие посетители не заметили."
                    if _return == 1:
                            #the other girl joins you...
                            "[Previous.Name] наклоняется и начинает играться с киской [Girl.Name_rod]."
                            $ Girl.GLG(Previous,700,3,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    if Girl.CreamA:
                            if Girl.Panties:
                                "После нескольких минут вы не выдерживаете и кончаете в нее."
                                "Она надевает обратно трусики и возвращается на свое место."
                            else:
                                "После нескольких минут вы не выдерживаете и кончаете в нее."
                                "Она вытирается как может и возвращается на свое место."
                            $ Girl.CreamA += 1
                            $ Girl.RecentActions.append("creampie anal")
                            $ Girl.DailyActions.append("creampie anal")
                    else:
                            "Через несколько минут она слазит с вашего члена и возвращается на свое место, после чего рукой доводит вас до оргазма."
                            if Girl.Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "Вы кончаете в ведерко с попкорном, который она и [Previous.Name]  потом доедают."
                                else:
                                    "Вы кончаете в ведерко с попкорном, который она потом доедает."
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.Spunk.append("mouth")
                                $ Girl.RecentActions.append("swallowed")
                                $ Girl.DailyActions.append("swallowed")
                            else:
                                if Girl is KittyX:
                                    "Вы кончаете в ведерко с попкорном, которое она затем ставит на пол."
                                else:
                                    "Вы кончаете в ведерко с попкорном, которое она затем ставит на соседнее сиденье."
                    if Girl is RogueX:
                            ch_r "Эти скачки были намного веселее, чем фильм."
                    elif Girl is KittyX:
                            ch_k "Будто мы в \"4D\"."
                    elif Girl is EmmaX:
                            ch_e "Что ж, это было увлекательно."
                    elif Girl is LauraX:
                            ch_l "Ммм, я заполнена."
                    elif Girl is JeanX:
                            ch_j "Отличная работа [[47]."
                    elif Girl is StormX:
                            ch_s "Я вполне довольна. . ."
                    elif Girl is JubesX:
                            ch_v "И фильм и бесплатная заправка. . ."
                    elif Girl is GwenX:
                            ch_g "Вот это 4D. . ."
                    elif Girl is BetsyX:
                            ch_b "Спасибо за скачки. . ."
                    elif Girl is DoreenX:
                            ch_d "Какие дикие скачки мы устроили. . ."
                    elif Girl is WandaX:
                            ch_w "Наша концовка гораздо лучше, чем в фильме. . ."
                    $ Girl.Statup("Inbt", 50, 4)
                    $ Girl.Statup("Inbt", 90, 3)
                    $ Girl.SeenPeen += 1
                    $ Girl.Anal += 1
                    $ Player.Semen -= 1
                    $ Girl.RecentActions.append("anal")
                    $ Girl.DailyActions.append("anal")
        elif OptionsDS[0] == "sex":
                    $ Girl.FaceChange("sexy", 1)
                    if Girl.Panties:
                        "Во время поцелуя [Girl.Name] протягивает руку и расстегивает вашу ширинку. Она стягивает свои трусики и садится к вам на колени."
                    elif Girl.PantsNum() == 5:
                        "Во время поцелуя [Girl.Name] протягивает руку и расстегивает вашу ширинку. Она слегка задирает свою юбку и садится к вам на колени."
                    else:
                        "Во время поцелуя [Girl.Name] протягивает руку и расстегивает вашу ширинку. Затем она садится к вам на колени."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out...
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway..."
                    "Секунду спустя, она начинает медленно скакать на вашем члене, пытаясь не шуметь, чтобы другие посетители не заметили."
                    if _return == 1:
                            #the other girl joins you...
                            "[Previous.Name] наклоняется и начинает играться с киской [Girl.Name_rod]."
                            $ Girl.GLG(Previous,700,3,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    if Girl.CreamP:
                        if Girl.Panties:
                            "После нескольких минут вы не выдерживаете и кончаете в нее."
                            "Она надевает обратно трусики и возвращается на свое место."
                        else:
                            "После нескольких минут вы не выдерживаете и кончаете в нее."
                            "Она вытерается как может и возвращается на свое место."
                        $ Girl.CreamP += 1
                        $ Girl.RecentActions.append("creampie sex")
                        $ Girl.DailyActions.append("creampie sex")
                    else:
                        "Через несколько минут она слазит с вашего члена и возвращается на свое место, после чего рукой доводит вас до оргазма."
                        if Girl.Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "Вы кончаете в ведерко с попкорном, который она и [Previous.Name] потом доедают."
                                else:
                                    "Вы кончаете в ведерко с попкорном, который она потом доедает."
                                $ Girl.Spunk.append("mouth")
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.RecentActions.append("swallowed")
                                $ Girl.DailyActions.append("swallowed")
                        else:
                            if Girl is KittyX:
                                "Вы кончаете в ведерко с попкорном, которое она затем ставит на пол."
                            else:
                                "Вы кончаете в ведерко с попкорном, которое она затем ставит на соседнее сиденье."
                    if Girl is RogueX:
                            ch_r "Эти скачки были намного веселее, чем фильм."
                    elif Girl is KittyX:
                            ch_k "Будто мы в \"4D\"."
                    elif Girl is EmmaX:
                            ch_e "Что ж, это было увлекательно."
                    elif Girl is LauraX:
                            ch_l "Ммм, я заполнена."
                    elif Girl is JeanX:
                            ch_j "Отличная работа, [Girl.Petname]."
                    elif Girl is StormX:
                            ch_s "Такого рода драмы мне нравятся. . ."
                    elif Girl is JubesX:
                            ch_v "И фильм и бесплатная заправка. . ."
                    elif Girl is GwenX:
                            ch_g "Вот это 4D. . ."
                    elif Girl is BetsyX:
                            ch_b "Спасибо за скачки. . ."
                    elif Girl is DoreenX:
                            ch_d "Какие дикие скачки мы устроили. . ."
                    elif Girl is WandaX:
                            ch_w "Наша концовка гораздо лучше, чем в фильме. . ."
                    $ Girl.Statup("Inbt", 50, 4)
                    $ Girl.Statup("Inbt", 90, 3)
                    $ Girl.SeenPeen += 1
                    $ Girl.Sex += 1
                    $ Player.Semen -= 1
                    $ Girl.RecentActions.append("sex")
                    $ Girl.DailyActions.append("sex")
        elif OptionsDS[0] == "blow":
                    $ Girl.FaceChange("sucking", 1)
                    if not Player.Male:
                        "Во время поцелуя, [Girl.Name] протягивает руку и расстегивает вашу ширинку. Затем она наклоняется и присасывается к вашей киске."
                    else:
                         "Во время поцелуя, [Girl.Name] протягивает руку и расстегивает вашу ширинку. Затем она наклоняется и обхватывает ваш член губами."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out...
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway..."
                    if _return == 1:
                            #the other girl joins you...
                            if not Player.Male:
                                "[Previous.Name] также нагибается и присоединяется к [Girl.Name_dat] в облизывании вашей киски."
                                "Они по очереди потихоньку лижут ее несколько минут, пока вы, наконец, не кончаете."
                            else:
                                "[Previous.Name] также нагибается и присоединяется к [Girl.Name_dat] в вылизывание вашего члена."
                                "Они по очереди потихоньку сосут его несколько минут, пока вы, наконец, не кончаете."
                            $ Girl.GLG(Previous,1000,2,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    else:
                            if not Player.Male:
                                "Она тихонько лижет ее несколько минут, пока вы, наконец, не кончаете."
                            else:
                                "Она тихонько сосет его несколько минут, пока вы, наконец, не кончаете."
                    $ Girl.Spunk.append("mouth")
                    if Girl.Swallow:
                            "[Girl.Name] вытирает рот, откидывается на спинку сиденья и делает пару глотков газировки."
                            $ Girl.FaceChange("sexy")
                            if Girl is RogueX:
                                    ch_r "Мммм, освежает. . ."
                            elif Girl is KittyX:
                                    ch_k "Мммм, То что надо. . ."
                            elif Girl is EmmaX:
                                    ch_e "Мммм, освежает. . ."
                            elif Girl is LauraX:
                                    ch_l "Мммм, То что надо. . ."
                            elif Girl is JeanX:
                                    ch_j "Восхитительно, [Girl.Petname]."
                            elif Girl is StormX:
                                    ch_s "Восхитительное угощение. . ."
                            elif Girl is JubesX:
                                    ch_v "Вот -это- освежает. . ."
                            elif Girl is GwenX:
                                    ch_g "Вот так мы экономим на газировке. . ."
                            elif Girl is BetsyX:
                                    ch_b "Очень освежает. . ."
                            elif Girl is DoreenX:
                                    ch_d "Вкусно. . ."
                            elif Girl is WandaX:
                                    ch_w "Ням. . ."
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.RecentActions.append("swallowed")
                            $ Girl.DailyActions.append("swallowed")
                    else:
                        if Girl is KittyX:
                            "Вы кончаете в ведерко с попкорном, которое она затем ставит на пол."
                        elif Girl is WandaX:
                            "Вы кончаете в ведро с попкорном, которое исчезает во вспышке голубого света."
                        else:
                            "Вы кончаете в ведерко с попкорном, которое она затем ставит на соседнее сиденье."
                        if Girl is RogueX:
                                ch_r "Уверена, уборщики будут в восторге."
                        elif Girl is KittyX:
                                ch_k "Это должно удивить \"археологов.\"."
                        elif Girl is EmmaX:
                                ch_e "Небольшой беспорядок для персонала."
                        elif Girl is LauraX:
                                ch_l "Немного наследили."
                        elif Girl is JeanX:
                                ch_j "Ха."
                        elif Girl is StormX:
                                ch_s "Мы не должны оставлять такой беспорядок. . ."
                        elif Girl is JubesX:
                                ch_v "Ух, какой беспорядок. . ."
                        elif Girl is GwenX:
                                ch_g "Знаешь, нам никогда не нравилось находить такие сюрпризы. . ."
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 15:
                                        ch_g "Кроме Тани, ей нравилось."
                        elif Girl is BetsyX:
                                ch_b "Очень вкусно. . ."
                        elif Girl is DoreenX:
                                ch_d "Мне нужно прибраться. . ."
                        elif Girl is WandaX:
                                ch_w "Абракадабра. . ."
                    $ Girl.Statup("Inbt", 40, 3)
                    $ Girl.Statup("Inbt", 80, 2)
                    if Player.Male:
                            $ Girl.SeenPeen += 1
                            $ Girl.Blow += 1
                            $ Girl.RecentActions.append("blow")
                            $ Girl.DailyActions.append("blow")
                    else:
                            $ Girl.SeenPuss += 1
                            $ Girl.CUN += 1
                            $ Girl.RecentActions.append("cun")
                            $ Girl.DailyActions.append("cun")
                    $ Player.Semen -= 1
        elif OptionsDS[0] == "hand":
                    $ Girl.FaceChange("sexy")
                    "Во время поцелуя [Girl.Name] тянется рукой к вашей ширинке, расстегивает ее и залазит туда рукой."
                    call Date_Sex_Break(Girl,Previous)
                    if _return == 3:
                            #the other girl stormed out...
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway..."
                            if not Player.Male:
                                "Затем она наклоняется и начинает ласкать вашу киску."
                            else:
                                "Затем она наклоняется и начинает ласкать ваш член."
                    elif _return == 1:
                            #the other girl joins in...
                            if not Player.Male:
                                "Затем она наклоняется и начинает ласкать вашу киску."
                            else:
                                "Затем она наклоняется и начинает ласкать ваш член."
                            "[Previous.Name] наклоняется и присоединяется к ней с улыбкой."
                            $ Girl.GLG(Previous,1000,2,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    else:
                            if not Player.Male:
                                "Затем она наклоняется и начинает ласкать вашу киску."
                            else:
                                "Затем она наклоняется и начинает ласкать ваш член."
                    $ Girl.FaceChange("surprised")
                    if Girl.FondleP:
                        if _return == 1:
                                    #the other girl joins in...
                                    "Вы также наклоняетесь и начинаете гладить их киски."
                        else:
                            if Girl.Legs:
                                    "Вы также наклоняетесь, залазите под ее [get_clothing_name(Girl.Legs_key, rod)] и начинаете гладить ее киску."
                            elif Girl.Hose:
                                    "Вы также наклоняетесь, залазите под ее [get_clothing_name(Girl.Hose_key, rod)] и начинаете гладить ее киску."
                            elif Girl.Panties:
                                    "Вы также наклоняетесь, залазите в ее трусики и начинаете гладить ее киску."
                            else:
                                    "Вы также наклоняетесь, обращаете внимания, что на ней ничего нет и затем начинаете гладить ее киску."
                    $ Girl.FaceChange("sexy", 1, Eyes = "closed")
                    if Girl.FondleP:
                            if _return == 1:
                                "Через несколько минут [Girl.Name] с [Previous.Name_tvo] вздрагивают от оргазма, что заставляет кончить и вас."
                            else:
                                "Через несколько минут, она вздрагивает от оргазма, что заставляет кончить и вас."
                            if not Player.Male:
                                "[Girl.Name] закидывает ваши соки в ведерко с попкорном."
                            else:
                                "[Girl.Name] закидывает вашу сперму в ведерко с попкорном."
                    $ Girl.Eyes = "sexy"
                    if Girl.Swallow:
                            if 0 < _return < 3: #if 1 or 2
                                "Девочки доедают оставшийся попкорн с улыбкой."
                            else:
                                "Она доедает оставшийся попкорн с улыбкой."
                            $ Girl.Spunk.append("mouth")
                            if Girl is RogueX:
                                    ch_r "У них тут просто замечательные добавки, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "У них тут просто замечательные добавки, [Girl.Petname]."
                            elif Girl is EmmaX:
                                    ch_e "Мне очень понравилась их новая добавка, [Girl.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Я должна заказать эту добавку снова."
                            elif Girl is JeanX:
                                    ch_j "Ням."
                            elif Girl is StormX:
                                    ch_s "Это было очень вкусно. . ."
                            elif Girl is JubesX:
                                    ch_v "Вот -это- освежает. . ."
                            elif Girl is GwenX:
                                    ch_g "Лучшая добавка, который тут есть. . ."
                            elif Girl is BetsyX:
                                    ch_b "Очень освежает. . ."
                            elif Girl is DoreenX:
                                    ch_d "Вкусо. . ."
                            elif Girl is WandaX:
                                    ch_w "Ням. . ."
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.RecentActions.append("swallowed")
                            $ Girl.DailyActions.append("swallowed")
                    else:
                            if Girl is KittyX:
                                "Вы кончаете в ведерко с попкорном, которое она затем ставит на пол."
                            elif Girl is WandaX:
                                "Вы кончаете в ведро с попкорном, которое исчезает во вспышке голубого света."
                            else:
                                "Вы кончаете в ведерко с попкорном, которое она затем ставит на соседнее сиденье."
                            if Girl is RogueX:
                                    ch_r "Уверена, уборщики будут в восторге."
                            elif Girl is KittyX:
                                    ch_k "Это должно удивить \"археологов.\"."
                            elif Girl is EmmaX:
                                    ch_e "Небольшой беспорядок для персонала."
                            elif Girl is LauraX:
                                    ch_l "Немного наследили."
                            elif Girl is JeanX:
                                    ch_j "Ха."
                            elif Girl is StormX:
                                    ch_s "Мы не должны оставлять такой беспорядок. . ."
                            elif Girl is JubesX:
                                    ch_v "Ух, какой беспорядок. . ."
                            elif Girl is GwenX:
                                    ch_g "Знаешь, нам никогда не нравилось находить такие сюрпризы. . ."
                                    $ D20 = renpy.random.randint(1, 20)
                                    if D20 > 15:
                                            ch_g "Кроме Тани, ей нравилось."
                            elif Girl is BetsyX:
                                    ch_b "Очень надеюсь, что улучшила впечатления от фильма. . ."
                            elif Girl is DoreenX:
                                    ch_d "Мне нужно прибраться. . ."
                            elif Girl is WandaX:
                                    ch_w "Абракадабра. . ."
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Inbt", 40, 3)
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.FondleP += 1
                    $ Girl.Org += 1
                    $ Player.Semen -= 1
                    if Player.Male:
                            $ Girl.Hand += 1
                            $ Girl.RecentActions.append("hand")
                            $ Girl.DailyActions.append("hand")
                    else:
                            $ Girl.Finger += 1
                            $ Girl.RecentActions.append("finger")
                            $ Girl.DailyActions.append("finger")
        elif OptionsDS[0] == "pussy":
                    $ Girl.FaceChange("sexy")
                    if Girl.PantsNum() == 5:
                            "Во время поцелуя [Girl.Name] берет вашу руку и засовывает ее себе под [get_clothing_name(Girl.Legs_key, rod)]."
                    elif Girl.Legs:
                            "Во время поцелуя [Girl.Name] берет вашу руку и засовывает ее себе под [get_clothing_name(Girl.Legs_key, rod)]."
                    elif Girl.HoseNum() >= 5:
                            "Во время поцелуя [Girl.Name] берет вашу руку и засовывает ее себе под [get_clothing_nameGirl.Hose_key, rod)]."
                    elif Girl.Panties:
                            "Во время поцелуя [Girl.Name] берет вашу руку и засовывает ее себе в трусики."
                    else:
                            "Во время поцелуя [Girl.Name] берет вашу руку и засовывает ее себе между ног."
                    call Date_Sex_Break(Girl,Previous)
                    $ Girl.Eyes = "closed"
                    if _return == 3:
                            #the other girl stormed out...
                            call Sex_Basic_Dialog(Girl,"partner") #"Aw, that's a bummer. Anyway..."
                            "Вы возвращаетесь к своему занятию."
                    elif _return == 1:
                            #the other girl joins in...
                            "[Previous.Name] наклоняется и начинает ласкать ее грудь."
                            $ Girl.GLG(Previous,700,6,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    "Через несколько минут она содрогается в оргазме и откидывается на спину со вздохом удовольствия."
                    $ Girl.Eyes = "sexy"
                    if Girl is RogueX:
                            ch_r "Спасибо, [Girl.Petname]. Мне нужно было. . . отвлечься."
                    elif Girl is KittyX:
                            ch_k "Ммм, это было здорово, [Girl.Petname]."
                    elif Girl is EmmaX:
                            ch_e "Очень. . . мило с твоей стороны, [Girl.Petname]. Мне как раз этого не хватало."
                    elif Girl is LauraX:
                            ch_l "Ммм, это было здорово, [Girl.Petname]."
                    elif Girl is JeanX:
                            ch_j "Не зря пошли в кино, [Girl.Petname]."
                    elif Girl is StormX:
                            ch_s "Благодарю тебя за. . . помощь. . ."
                    elif Girl is JubesX:
                            ch_v "Ах. . . то, что нужно. . ."
                    elif Girl is GwenX:
                            if not Player.Male:
                                ch_g "Ты помогла решить проблемы третьего акта. . ."
                            else:
                                ch_g "Ты помог решить проблемы третьего акта. . ."
                    elif Girl is BetsyX:
                            ch_b "Не зря я пошла с тобой. . ."
                    elif Girl is DoreenX:
                            ch_d "Это отличный способ скрасить фильм. . ."
                    elif Girl is WandaX:
                            if not Player.Male:
                                ch_w "Спасибо, что помогла снять напряжение. . ."
                            else:
                                ch_w "Спасибо, что помог снять напряжение. . ."
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Inbt", 40, 2)
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.FondleP += 1
                    $ Girl.Org += 1
                    $ Girl.RecentActions.append("fondle pussy")
                    $ Girl.DailyActions.append("fondle pussy")
        elif OptionsDS[0] == "panties":
                    $ Girl.FaceChange("sexy")
                    "После нескольких секунд поцелуев, [Girl.Name] хитро вам улыбается, затем куда-то лезет рукой."
                    "Через секунду она протягивает вам кусок ткани, очевидно, это ее трусики."
                    $ Girl.DailyActions.append("pantyless")
                    $ Girl.Statup("Inbt", 60, 2)
                    $ Girl.Panties = 0
                    if Girl is RogueX:
                            ch_r "Это чтобы тебя немножко раззадорить, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "[Girl.Like]сохранишь их для меня?"
                    elif Girl is EmmaX:
                            ch_e "Просто намек на будущее, [Girl.Petname]."
                    elif Girl is LauraX:
                            ch_l "Придержишь их для меня?"
                    elif Girl is JeanX:
                            ch_j "Придержи их для меня, [Girl.Petname]."
                    elif Girl is StormX:
                            ch_s "Я чувствовала себя немного скованной. . ."
                    elif Girl is JubesX:
                            ch_v "Ты можешь. . . эм, подержать их. . ."
                    elif Girl is GwenX:
                            ch_g "У меня есть еще. . ."
                            $ D20 = renpy.random.randint(1, 20)
                            if D20 > 15:
                                    ch_g ". . . То есть, не на мне. . . а. . ."
                                    ch_g "Ладно, это прозвучало странно."
                    elif Girl is BetsyX:
                            ch_b "Надеюсь, я не слишком скрываю свои намерения. . ."
                    elif Girl is DoreenX:
                            ch_d "Ты меня понимаешь? . ."
                    elif Girl is WandaX:
                            ch_w "Та-дааа. . ."

        elif OptionsDS[0] == "flash":
                    $ Girl.FaceChange("sexy")
                    "После нескольких секунд поцелуев [Girl.Name] хитро вам улыбается, затем садится чуточку пониже."
                    if Girl.PantsNum() > 6:
                        "Вы смотрите вниз и замечаете, что она спустила штаны достаточно, чтобы вы могли лицезреть ее голую киску, освещенную киноэкраном."
                    elif Girl.PantsNum() == 6:
                        "Вы смотрите вниз и замечаете, что она спустила шорты достаточно, чтобы вы могли лицезреть ее голую киску, освещенную киноэкраном."
                    elif Girl.PantsNum() == 5:
                        "Вы смотрите вниз и замечаете, что она задрала юбку достаточно, чтобы вы могли лицезреть ее голую киску, освещенную киноэкраном."
                    else:
                        "Вы смотрите вниз и замечаете, что она слегка поглаживает свою голую киску, освещенную киноэкраном."
                    $ Girl.Statup("Inbt", 60, 2)
                    call Girl_First_Bottomless(Girl,1)
                    if Girl is RogueX:
                            ch_r "Просто хочу тебя немного раззадорить, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "Просто немного дразню тебя. . ."
                    elif Girl is EmmaX:
                            ch_e "Просто намек на будущее, [Girl.Petname]."
                    elif Girl is LauraX:
                            ch_l "Просто намек на будущее. . ."
                    elif Girl is JeanX:
                            ch_j "Показываю возможный подарок, [Girl.Petname]."
                    elif Girl is StormX:
                            ch_s "Я подумала, что тебе понравится вид. . ."
                    elif Girl is JubesX:
                            ch_v "Веселее, чем фильм? . ."
                    elif Girl is GwenX:
                            ch_g "Просто небольшое дополнение к фильму. . ."
                    elif Girl is BetsyX:
                            ch_b "Мне кажется, тебе лучше смотреть туда, а не на экран. . ."
                    elif Girl is DoreenX:
                            ch_d "Просто захотела тебе напомнить. . ."
                    elif Girl is WandaX:
                            ch_w "Смотри на меня. . ."
    #End Rogue movie sex options
    $ Girl.OutfitChange(Changed=0)
    return
# End Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Date_Sex_Break   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_Sex_Break(Girl=0,Previous=0,Repeat=0):#rkeljsvgb
        #Girl is the lead girl
        #Previous is the other girl
        # if it returns 0, it continues normally.
        # if it returns 1, the other girl joins in
        # if it returns 2, the other girl watches
        # if it returns 3, the other girl is mad, but it goes on
        # if it returns 4, the other girl is mad, so you cancel out
        # if Repeat, it's the second scene like this of the night.

        if Previous not in TotalGirls and len(Party) >= 2:
                    if Girl is Party[0]:
                            $ Previous = Party[1]
                    else:
                            $ Previous = Party[0]

        if Previous not in TotalGirls:
                return 0

        if Girl is Previous:
            "Tell Oni that on a date, a girl and previous were the same, [Girl.Tag], DSB"

        if "friendly" in Previous.DailyActions:
                $ Previous.DrainWord("friendly",0,1)
        if not Player.Male and "girltalk" not in Previous.History and "nogirls" not in Previous.History:
                $ Previous.AddWord(1,"dategirltalk",0,0,0) #adds to recent actions

        if Girl.GirlLikeCheck(Previous) >= 700 and Previous.GirlLikeCheck(Girl) >= 700:
                #They like each other and will share
                $ Previous.RecentActions.append("noticed " + Girl.Tag)
                return 1
        elif Previous is JeanX and not ApprovalCheck(Previous, 500, "L"):
                #if it's Jean and she doesn't particularly care...
                $ Previous.FaceChange("sly",1,Eyes="side")
                if bg_current == "bg restaurant":
                        "[Previous.Name] закатывает глаза, но вскоре возвращается к еде."
                elif bg_current == "bg movie":
                        "[Previous.Name] закатывает глаза, но вскоре продолжает смотреть фильм."
                else:
                        "[Previous.Name] закатывает глаза, но не вмешивается."
                $ Previous.RecentActions.append("noticed " + Girl.Tag)
                $ Girl.GLG(Previous,600,5,2)
                $ Previous.GLG(Girl,500,3)
                $ Previous.GLG(Girl,900,3)
                return 2
        elif ApprovalCheck(Previous, 1400) and Previous.GirlLikeCheck(Girl) >= 500:
                #girl2 likes you, and likes girl1 enough to be chill
                $ Previous.FaceChange("sly")
                "[Previous.Name] подмигивает вам, но не решается вмешаться."
                $ Previous.RecentActions.append("noticed " + Girl.Tag)
                $ Girl.GLG(Previous,600,5,1)
                $ Girl.GLG(Previous,900,3,1)
                $ Previous.GLG(Girl,900,2,1)
                return 2
#        elif ApprovalCheck(Previous, 1400) and Previous.GirlLikeCheck(Girl) < 500:
#                pass


        #If they asked you to stop

        #She likes you, but hates the girl
        if Repeat == 2:
                #if it's a good night kiss
                $ Previous.FaceChange("angry",Eyes="side")
                $ Previous.Statup("Love", 80, -5)
                $ Previous.Statup("Obed", 80, 5)
                $ Previous.GLG(Girl,800,-3,1)
                $ Previous.AddWord(1,"annoyed") #adds to Recent
                return 3
        elif "annoyed" in Previous.RecentActions:
                #if something happened earlier...
                $ Previous.FaceChange("angry")
                $ Previous.Statup("Love", 80, -15)
                $ Previous.Statup("Obed", 80, 15)
                if Previous == RogueX:
                        ch_r "Снимите уже себе комнату!"
                elif Previous is KittyX:
                        ch_k "Боже, прямо передо мной?!"
                elif Previous is EmmaX:
                        ch_e "Ох, да повзрослейте уже!"
                elif Previous is LauraX:
                        ch_l "Серьезно, снимите комнату!"
                elif Previous is JeanX:
                        ch_j "Научитесь справляться с гормонами."
                elif Previous is StormX:
                        ch_s "Довольно, прекратите."
                elif Previous is JubesX:
                        ch_v "Прекратите!"
                elif Previous is GwenX:
                        ch_g "Эй! Успокойтесь!"
                elif Previous is BetsyX:
                        ch_b "Ох, ведите себя прилично."
                elif Previous is DoreenX:
                        ch_d "Эй, не занимайтесь таким на людях. . ."
                elif Previous is WandaX:
                        ch_w "Воу, ребята, успокойтесь. . ."
                $ Previous.GLG(Girl,800,-3,1)
                call Girl_Date_Over(Previous)
                # You do it anyway
                return 3
        $ Previous.AddWord(1,"annoyed") #adds to Recent
        if Previous is RogueX:
                ch_r "Я поняла, что она задумала, прекратите."
        elif Previous is KittyX:
                ch_k "Я все вижу, прекратите."
        elif Previous is EmmaX:
                ch_e "Ох, я вижу, что сейчас происходит, прекратите."
        elif Previous is LauraX:
                ch_l "Думали, я не замечу? Прекратите."
        elif Previous is JeanX:
                ch_j "Мне не нужно быть экстрасенсом, чтобы понять, что сейчас происходит."
                ch_j "я как-бы -тоже- тут."
                ch_j "Прекратите."
        elif Previous is StormX:
                ch_s "Надеюсь, мы сможем закончить вечер."
        elif Previous is JubesX:
                ch_v "Знаешь, я могу -прочесть- тебя."
        elif Previous is GwenX:
                ch_g "Ребята? Я здесь. . . перед вами, вы это знаете?"
        elif Previous is BetsyX:
                ch_b "Я чувствую, что вы меня игнорируете. . ."
        elif Previous is DoreenX:
                ch_d "Я чувствую себя третьей лишней. . ."
        elif Previous is WandaX:
                ch_w "Послушайте. . . Я тут как бы пытаюсь приятно провести вечер. . ."
        $ Previous.GLG(Girl,800,-1,1)
        $ Girl.GLG(Previous,800,-3,1)
        menu:
            extend ""
            "Ладно, мы прекратим.":
                $ Previous.Statup("Love", 80, 10)
                $ Previous.Statup("Obed", 80, -5)
                $ Previous.Statup("Inbt", 60, 5)
                $ Girl.GLG(Previous,800,-3,1)
                if "study" not in Player.RecentActions:
                        call Date_Bonus(Previous,5)
                # You stop
                return 4
            "Мы продолжим.":
                $ Previous.FaceChange("angry")
                $ Previous.Statup("Love", 80, -10)
                $ Previous.Statup("Obed", 80, 10)
                $ Previous.Statup("Inbt", 60, -5)
                $ Previous.GLG(Girl,800,-3,1)
                if "study" in Player.RecentActions:
                        call Girl_Date_Over(Previous)
                else:
                        call Date_Bonus(Previous,-5)
                # You do it anyway
                return 3
        return 0 #Yes

#end Date_Sex_Break   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Payment system   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_Paying(Activity="dinner", Total_Cost=0):  #rkeljsvgb
    # Activity is which thing you're doing, total cost is the combined meal costs.
    if Activity == "dinner":
                $ Total_Cost = Play_Cost + Date_Cost[0] + Date_Cost[1]
                "Официантка приносит вам счет, вы должны заплатить $[Total_Cost]."
    else:
        if len(Party) >= 2:
                $ Total_Cost = 30
                "Вы подходите к билетной кассе, три билета будут стоить $30."
        else:
                $ Total_Cost = 20
                "Вы подходите к билетной кассе, два билета будут стоить $20."

    menu:
        "Кто заплатит?"
        "Я плачу за всех." if Player.Cash >= Total_Cost:
            $ Line = "you"

        "[RogueX.Name], оплати ты." if RogueX in Party:
            $ Line = RogueX
        "[KittyX.Name], оплати ты." if KittyX in Party:
            $ Line = KittyX
        "[EmmaX.Name], оплати ты." if EmmaX in Party:
            $ Line = EmmaX
        "[LauraX.Name], оплати ты." if LauraX in Party:
            $ Line = LauraX
        "[JeanX.Name], оплати ты." if JeanX in Party:
            $ Line = JeanX
        "[StormX.Name], оплати ты." if StormX in Party:
            $ Line = StormX
        "[JubesX.Name], оплати ты." if JubesX in Party:
            $ Line = JubesX
        "[GwenX.Name], оплати ты." if GwenX in Party:
            $ Line = GwenX
        "[BetsyX.Name], оплати ты." if BetsyX in Party:
            $ Line = BetsyX
        "[DoreenX.Name], оплати ты." if DoreenX in Party:
            $ Line = DoreenX
        "[WandaX.Name], оплати ты." if WandaX in Party:
            $ Line = WandaX

        "Разделим сумму." if Player.Cash >= Play_Cost:
            $ Line = "split"

        "Если честно, у меня нет денег. . ." if Player.Cash < Total_Cost:
            $ Line = "deadbeat"

    if Line == "you":
            #If you offer to cover the meal
            if RogueX in Party:
                    if "deadbeat" in RogueX.History:
                        $ RogueX.History.remove("deadbeat")
                    $ RogueX.FaceChange("sexy", 1)
                    if not Player.Male:
                        ch_r "Ох, ты настоящая леди."
                    else:
                        ch_r "Ох, ты такой джентльмен."
                    $ RogueX.Statup("Love", 50, 2)
                    $ RogueX.Statup("Love", 80, 2)
                    if Total_Cost >= 15:
                        $ RogueX.Statup("Love", 200, 2)
                    call Date_Bonus(RogueX,Total_Cost)

            if KittyX in Party:
                    if "deadbeat" in KittyX.History:
                        $ KittyX.History.remove("deadbeat")
                    $ KittyX.FaceChange("sexy", 1)
                    ch_k "[KittyX.Like]это очень мило с твоей стороны."
                    $ KittyX.Statup("Love", 50, 2)
                    $ KittyX.Statup("Love", 80, 2)
                    if Total_Cost >= 15:
                        $ KittyX.Statup("Love", 200, 2)
                    call Date_Bonus(KittyX,Total_Cost)

            if EmmaX in Party:
                    if "deadbeat" in EmmaX.History:
                        $ EmmaX.History.remove("deadbeat")
                    $ EmmaX.FaceChange("sly", 1)
                    ch_e "Ох, как это так по-взрослому."
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ EmmaX.Statup("Love", 50, 2)
                    $ EmmaX.Statup("Love", 80, 2)
                    if Total_Cost >= 15:
                        $ EmmaX.Statup("Love", 200, 2)
                    call Date_Bonus(EmmaX,Total_Cost)

            if LauraX in Party:
                    if "deadbeat" in LauraX.History:
                        $ LauraX.History.remove("deadbeat")
                    $ LauraX.FaceChange("sly", 1)
                    ch_l "Ох, очень мило с твоей стороны."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Love", 50, 2)
                    $ LauraX.Statup("Love", 80, 1)
                    if Total_Cost >= 15:
                        $ LauraX.Statup("Love", 90, 2)
                        $ LauraX.Statup("Obed", 50, 1)
                    call Date_Bonus(LauraX,Total_Cost)
            if JeanX in Party:
                    if "deadbeat" in JeanX.History:
                        $ JeanX.History.remove("deadbeat")
                    $ JeanX.FaceChange("sly", 1)
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Love", 50, 2)
                    $ JeanX.Statup("Love", 80, 1)
                    if Total_Cost >= 15:
                        $ JeanX.Statup("Love", 90, 2)
                        $ JeanX.Statup("Obed", 50, 1)
                    call Date_Bonus(JeanX,Total_Cost)

            if StormX in Party:
                    if "deadbeat" in StormX.History:
                        $ StormX.History.remove("deadbeat")
                    $ StormX.FaceChange("sly", 1)
                    ch_s "Это очень любезно с твоей стороны."
                    $ StormX.Statup("Obed", 40, 1)
                    $ StormX.Statup("Obed", 60, 3)
                    $ StormX.Statup("Love", 50, 1)
                    $ StormX.Statup("Love", 80, 2)
                    if Total_Cost >= 15:
                        $ StormX.Statup("Love", 200, 1)
                    call Date_Bonus(StormX,Total_Cost)

            if JubesX in Party:
                    if "deadbeat" in JubesX.History:
                        $ JubesX.History.remove("deadbeat")
                    $ JubesX.FaceChange("sexy", 1)
                    ch_v "О, это так мило. . ."
                    $ JubesX.Statup("Love", 50, 1)
                    $ JubesX.Statup("Love", 80, 1)
                    if Total_Cost >= 15:
                        $ JubesX.Statup("Obed", 50, 1)
                    call Date_Bonus(JubesX,Total_Cost)

            if GwenX in Party:
                    if "deadbeat" in GwenX.History:
                        $ GwenX.History.remove("deadbeat")
                    $ GwenX.FaceChange("sexy", 1)
                    if Activity == "dinner":
                                ch_g "Ура, бесплатная еда!"
                    else:
                                ch_g "Ты платишь? Потрясающе!"
                    $ GwenX.Statup("Love", 50, 1)
                    $ GwenX.Statup("Love", 80, 2)
                    if Total_Cost >= 15:
                        $ GwenX.Statup("Obed", 50, 2)
                    call Date_Bonus(GwenX,Total_Cost)

            if BetsyX in Party:
                    if "deadbeat" in BetsyX.History:
                        $ BetsyX.History.remove("deadbeat")
                    $ BetsyX.FaceChange("sly", 1)
                    ch_b "Ох, это так мило."
                    $ BetsyX.Statup("Obed", 70, 2)
                    $ BetsyX.Statup("Love", 50, 1)
                    $ BetsyX.Statup("Love", 80, 1)
                    if Total_Cost >= 15:
                        $ BetsyX.Statup("Obed", 50, 2)
                    call Date_Bonus(BetsyX,Total_Cost)

            if DoreenX in Party:
                    if "deadbeat" in DoreenX.History:
                        $ DoreenX.History.remove("deadbeat")
                    $ DoreenX.FaceChange("smile", 1)
                    ch_d "Оу, как мило!"
                    $ DoreenX.Statup("Obed", 70, 2)
                    $ DoreenX.Statup("Love", 50, 1)
                    $ DoreenX.Statup("Love", 80, 1)
                    if Total_Cost >= 15:
                        $ DoreenX.Statup("Obed", 50, 2)
                    call Date_Bonus(DoreenX,Total_Cost)

            if WandaX in Party:
                    if "deadbeat" in WandaX.History:
                        $ WandaX.History.remove("deadbeat")
                    $ WandaX.FaceChange("smile", 1)
                    ch_w "Отлично!"
                    $ WandaX.Statup("Obed", 70, 1)
                    $ WandaX.Statup("Love", 50, 1)
                    $ WandaX.Statup("Love", 80, 1)
                    if Total_Cost >= 15:
                        $ WandaX.Statup("Obed", 50, 2)
                    call Date_Bonus(WandaX,Total_Cost)

            $ Player.Cash -= Total_Cost

    elif Line is RogueX:
            #If you ask Rogue to pay
            $ RogueX.Statup("Love", 90, -7)
            if Total_Cost >= 15:
                    $ RogueX.Statup("Love", 200, -6)
                    if Party[0] == RogueX and Play_Cost > Date_Cost[0]:
                        $ RogueX.Statup("Love", 200, -10)
                        $ RogueX.Statup("Obed", 80, 4)
                    elif RogueX in Party and Play_Cost > Date_Cost[1]:
                        $ RogueX.Statup("Love", 200, -10)
                        $ RogueX.Statup("Obed", 80, 4)
            if ApprovalCheck(RogueX, 1100) and len(Party) < 2:
                    $ RogueX.FaceChange("sad")
                    ch_r "Ну, ладно, думаю, в этот раз я потяну."
                    $ RogueX.Statup("Obed", 30, 3)
                    $ RogueX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in RogueX.RecentActions:
                            call Date_Bonus(RogueX, -Total_Cost)
            elif ApprovalCheck(RogueX, 1300) and len(Party) >= 2:
                    $ RogueX.FaceChange("sad")
                    ch_r "Хм, ладно, думаю, в этот раз я потяну."
                    $ RogueX.Statup("Love", 80, -5)
                    $ RogueX.Statup("Obed", 30, 4)
                    $ RogueX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in RogueX.RecentActions:
                            call Date_Bonus(RogueX, -Total_Cost)
            else:
                    $ RogueX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ RogueX.Statup("Love", 80, -5)
                        ch_r "Что за бред, я не буду за нее платить."
                    else:
                        if not Player.Male:
                            ch_r "Нет, [RogueX.Petname], плати за себя сама."
                        else:
                            ch_r "Нет, [RogueX.Petname], плати за себя сам."
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Rogue to pay

    elif Line is KittyX:
            #If you ask Kitty to pay
            $ KittyX.Statup("Love", 90, -7)
            if Total_Cost >= 15:
                    $ KittyX.Statup("Love", 200, -6)
                    if Party[0] == KittyX and Play_Cost > Date_Cost[0]:
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Obed", 80, 4)
                    elif KittyX in Party and Play_Cost > Date_Cost[1]:
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Obed", 80, 4)
            if ApprovalCheck(KittyX, 1000) and not len(Party) < 2:
                    $ KittyX.FaceChange("sad")
                    ch_k "А? Ладно, думаю, я смогу все оплатить. . ."
                    $ KittyX.Statup("Obed", 30, 3)
                    $ KittyX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in KittyX.RecentActions:
                            call Date_Bonus(KittyX, -Total_Cost)
            elif ApprovalCheck(KittyX, 1300) and len(Party) >= 2:
                    $ KittyX.FaceChange("sad")
                    ch_k "А? Ладно, думаю, я смогу все оплатить. . ."
                    $ KittyX.Statup("Love", 80, -5)
                    $ KittyX.Statup("Obed", 30, 4)
                    $ KittyX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in KittyX.RecentActions:
                            call Date_Bonus(KittyX, -Total_Cost)
            else:
                    $ KittyX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ KittyX.Statup("Love", 80, -5)
                        ch_k "Да ты шутишь! Я не буду за нее платить!"
                    else:
                        if not Player.Male:
                            ch_k "Вот еще! Плати за себя сама, [KittyX.Petname]."
                        else:
                            ch_k "Вот еще! Плати за себя сам, [KittyX.Petname]."
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Kitty to pay

    elif Line is EmmaX:
            #If you ask Emma to pay
            $ EmmaX.Statup("Love", 90, -3)
            if Total_Cost >= 15:
                    $ EmmaX.Statup("Love", 200, -6)
                    if Party[0] == EmmaX and Play_Cost > Date_Cost[0]:
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Obed", 80, 4)
                    elif EmmaX in Party and Play_Cost > Date_Cost[1]:
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Obed", 80, 4)
            if ApprovalCheck(EmmaX, 1100) and len(Party) >= 2:
                    $ EmmaX.FaceChange("sad")
                    if not Player.Male:
                        ch_e "Ладно, все таки, ты всего лишь студентка. . ."
                    else:
                        ch_e "Ладно, все таки, ты всего лишь студент. . ."
                    $ EmmaX.Statup("Love", 80, -1)
                    $ EmmaX.Statup("Obed", 30, 4)
                    $ EmmaX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in EmmaX.RecentActions:
                            call Date_Bonus(EmmaX, -Play_Cost)
            elif ApprovalCheck(EmmaX, 900):
                    $ EmmaX.FaceChange("sad")
                    if not Player.Male:
                        ch_e "Ладно, все таки, ты всего лишь студентка. . ."
                    else:
                        ch_e "Ладно, все таки, ты всего лишь студент. . ."
                    $ EmmaX.Statup("Obed", 30, 3)
                    $ EmmaX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in EmmaX.RecentActions:
                            call Date_Bonus(EmmaX, -Play_Cost)
            else:
                    $ EmmaX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ EmmaX.Statup("Love", 80, -5)
                        ch_e "Я уж точно не буду платить за -нее-."
                    else:
                        if not Player.Male:
                            ch_e "Студентка ты или нет, [EmmaX.Petname], я не буду платить за тебя."
                        else:
                            ch_e "Студент ты или нет, [EmmaX.Petname], я не буду платить за тебя."
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Emma to pay

    elif Line is LauraX:
            #If you ask Laura to pay
            $ LauraX.Statup("Love", 90, -2)
            if Total_Cost >= 15:
                    $ LauraX.Statup("Love", 200, -6)
                    if Party[0] == LauraX and Play_Cost > Date_Cost[0]:
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 80, 4)
                    elif LauraX in Party and Play_Cost > Date_Cost[1]:
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 80, 4)
            if ApprovalCheck(LauraX, 900) and len(Party) < 2:
                    $ LauraX.FaceChange("sad")
                    ch_l "У тебя сейчас черная полоса? . ."
                    $ LauraX.Statup("Obed", 30, 3)
                    $ LauraX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in LauraX.RecentActions:
                            call Date_Bonus(LauraX, -Play_Cost)
            elif ApprovalCheck(LauraX, 1100) and len(Party) >= 2:
                    $ LauraX.FaceChange("sad")
                    ch_l "У тебя сейчас черная полоса? . ."
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Obed", 30, 4)
                    $ LauraX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in LauraX.RecentActions:
                            call Date_Bonus(LauraX, -Play_Cost)
            else:
                    $ LauraX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ LauraX.Statup("Love", 80, -5)
                        ch_l "Я не буду платить за нее."
                    else:
                        ch_l "Очень жаль, но я не буду платить за тебя."
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Laura to pay
    elif Line is JeanX:
            #If you ask Jean to pay
            $ JeanX.Statup("Love", 90, -2)
            if Total_Cost >= 15:
                    $ JeanX.Statup("Love", 200, -6)
                    if Party[0] == JeanX and Play_Cost > Date_Cost[0]:
                        $ JeanX.Statup("Love", 200, -5)
                        $ JeanX.Statup("Obed", 80, 4)
                    elif JeanX in Party and Play_Cost > Date_Cost[1]:
                        $ JeanX.Statup("Love", 200, -5)
                        $ JeanX.Statup("Obed", 80, 4)
            if ApprovalCheck(JeanX, 900) and len(Party) < 2:
                    $ JeanX.FaceChange("confused",Mouth="smirk")
                    ch_j "Оох, плохое решение. . ."
                    $ JeanX.Statup("Obed", 30, 3)
                    $ JeanX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in JeanX.RecentActions:
                            call Date_Bonus(JeanX, -Play_Cost)
            elif ApprovalCheck(JeanX, 1100) and len(Party) >= 2:
                    $ JeanX.FaceChange("confused",Mouth="smirk")
                    ch_j "Серьезно? . ."
                    $ JeanX.Statup("Love", 80, -5)
                    $ JeanX.Statup("Obed", 30, 4)
                    $ JeanX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in JeanX.RecentActions:
                            call Date_Bonus(JeanX, -Play_Cost)
            else:
                    $ JeanX.FaceChange("sadside")
                    if len(Party) >= 2:
                        $ JeanX.Statup("Love", 80, -5)
                    ch_j "Ладно. . ."
                    $ Line = "deadbeat"
            #end asked Jean to pay

    elif Line is StormX:
            #If you ask Storm to pay
            $ StormX.Statup("Love", 90, -3)
            if Total_Cost >= 15:
                    $ StormX.Statup("Love", 200, -6)
                    if Party[0] == StormX and Play_Cost > Date_Cost[0]:
                        $ StormX.Statup("Love", 200, -5)
                        $ StormX.Statup("Obed", 80, 4)
                    elif StormX in Party and Play_Cost > Date_Cost[1]:
                        $ StormX.Statup("Love", 200, -5)
                        $ StormX.Statup("Obed", 80, 4)
            if ApprovalCheck(StormX, 900) and len(Party) < 2:
                    $ StormX.FaceChange("sad")
                    ch_s "Пожалуй, ты всего лишь ребенок. . ."
                    $ StormX.Statup("Obed", 30, 3)
                    $ StormX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in StormX.RecentActions:
                            call Date_Bonus(StormX, -Play_Cost)
            elif ApprovalCheck(StormX, 1100) and len(Party) >= 2:
                    $ StormX.FaceChange("sad")
                    ch_s "Пожалуй, ты всего лишь ребенок. . ."
                    $ StormX.Statup("Love", 80, -5)
                    $ StormX.Statup("Obed", 30, 4)
                    $ StormX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in StormX.RecentActions:
                            call Date_Bonus(StormX, -Play_Cost)
            else:
                    $ StormX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ StormX.Statup("Love", 80, -4)
                        ch_s "Я не буду платить за нее."
                    else:
                        if not Player.Male:
                            ch_s "Хоть ты и студентка, но я не буду покрывать твои расходы."
                        else:
                            ch_s "Хоть ты и студент, но я не буду покрывать твои расходы."
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Storm to pay

    elif Line is JubesX:
            #If you ask Jubes to pay
            $ JubesX.Statup("Love", 90, -8)
            if Total_Cost >= 15:
                    $ JubesX.Statup("Love", 200, -8)
                    if Party[0] == JubesX and Play_Cost > Date_Cost[0]:
                        $ JubesX.Statup("Love", 200, -10)
                        $ JubesX.Statup("Obed", 80, 4)
                    elif JubesX in Party and Play_Cost > Date_Cost[1]:
                        $ JubesX.Statup("Love", 200, -10)
                        $ JubesX.Statup("Obed", 80, 4)
            if ApprovalCheck(JubesX, 1000) and not len(Party) < 2:
                    $ JubesX.FaceChange("sad")
                    ch_v "Что? Думаю, это я могу. . ."
                    $ JubesX.Statup("Obed", 30, 3)
                    $ JubesX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in JubesX.RecentActions:
                            call Date_Bonus(JubesX, -Total_Cost)
            elif ApprovalCheck(JubesX, 1300) and len(Party) >= 2:
                    $ JubesX.FaceChange("sad")
                    ch_v "Что? Думаю, это я могу. . ."
                    $ JubesX.Statup("Love", 80, -5)
                    $ JubesX.Statup("Obed", 30, 4)
                    $ JubesX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in JubesX.RecentActions:
                            call Date_Bonus(JubesX, -Total_Cost)
            else:
                    $ JubesX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ JubesX.Statup("Love", 80, -5)
                        ch_v "Что?! Нет, я не буду платить и за нее!"
                    elif bg_current == "bg restaurant":
                        ch_v "Что? Ни за что, я почти ничего не съела!"
                    else:
                        if not Player.Male:
                            ch_v "Что? Я не буду платить, это ты пригласила меня!"
                        else:
                            ch_v "Что? Я не буду платить, это ты пригласил меня!"
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Jubes to pay
    elif Line is GwenX:
            #If you ask Gwen to pay
            $ GwenX.Statup("Love", 90, -7)
            if Total_Cost >= 15:
                    $ GwenX.Statup("Love", 200, -6)
                    if Party[0] == GwenX and Play_Cost > Date_Cost[0]:
                        $ GwenX.Statup("Love", 200, -10)
                        $ GwenX.Statup("Obed", 80, 4)
                    elif GwenX in Party and Play_Cost > Date_Cost[1]:
                        $ GwenX.Statup("Love", 200, -10)
                        $ GwenX.Statup("Obed", 80, 4)
            if ApprovalCheck(GwenX, 1000) and not len(Party) < 2:
                    $ GwenX.FaceChange("sad")
                    ch_g "Эм. . . я не взяла с собой денег."
                    $ GwenX.Statup("Obed", 30, 3)
                    $ GwenX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in GwenX.RecentActions:
                            call Date_Bonus(GwenX, -Total_Cost)
            elif ApprovalCheck(GwenX, 1300) and len(Party) >= 2:
                    $ GwenX.FaceChange("sad")
                    ch_g "Ты. . . хочешь, чтобы я заплатила за всех?"
                    $ GwenX.Statup("Love", 80, -5)
                    $ GwenX.Statup("Obed", 30, 4)
                    $ GwenX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in GwenX.RecentActions:
                            call Date_Bonus(GwenX, -Total_Cost)
            else:
                    $ GwenX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ GwenX.Statup("Love", 80, -5)
                        ch_g "Заплатить за вас, ребята? Я даже не собираюсь платить за себя!"
                    else:
                        if not Player.Male:
                            ch_g "С чего ты взяла, что у меня есть деньги?!"
                        else:
                            ch_g "С чего ты взял, что у меня есть деньги?!"
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Gwen to pay

    elif Line is BetsyX:
            #If you ask Betsy to pay
            $ BetsyX.Statup("Love", 90, -1)
            if Total_Cost >= 15:
                    $ BetsyX.Statup("Love", 200, -2)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    if Party[0] == BetsyX and Play_Cost > Date_Cost[0]:
                        $ BetsyX.Statup("Love", 200, -1)
                        $ BetsyX.Statup("Obed", 80, 4)
                    elif BetsyX in Party and Play_Cost > Date_Cost[1]:
                        $ BetsyX.Statup("Love", 200, -1)
                        $ BetsyX.Statup("Obed", 80, 4)
            if ApprovalCheck(BetsyX, 1100) and len(Party) >= 2:
                    $ BetsyX.FaceChange("bemused")
                    ch_b "О, я и не знала, что у тебя нет денег. . ."
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 30, 4)
                    $ BetsyX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in BetsyX.RecentActions:
                            call Date_Bonus(BetsyX, -Play_Cost)
            elif ApprovalCheck(BetsyX, 900):
                    $ BetsyX.FaceChange("bemused")
                    ch_b "О, я и не знала, что у тебя нет денег. . ."
                    $ BetsyX.Statup("Obed", 30, 3)
                    $ BetsyX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in BetsyX.RecentActions:
                            call Date_Bonus(BetsyX, -Play_Cost)
            else:
                    $ BetsyX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ BetsyX.Statup("Love", 80, -5)
                        ch_b "У меня нет никакого желания платить за нее."
                    else:
                        ch_b "Я не буду платить за тебя."
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Betsy to pay

    elif Line is DoreenX:
            #If you ask Doreen to pay
            $ DoreenX.Statup("Love", 90, -1)
            if Total_Cost >= 15:
                    $ DoreenX.Statup("Love", 200, -2)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    if Party[0] == DoreenX and Play_Cost > Date_Cost[0]:
                        $ DoreenX.Statup("Love", 200, -1)
                        $ DoreenX.Statup("Obed", 80, 4)
                    elif DoreenX in Party and Play_Cost > Date_Cost[1]:
                        $ DoreenX.Statup("Love", 200, -1)
                        $ DoreenX.Statup("Obed", 80, 4)
            if ApprovalCheck(DoreenX, 1100) and len(Party) >= 2:
                    $ DoreenX.FaceChange("bemused")
                    ch_d "Ну, думаю, в этот раз я смогу оплатить счет. . ."
                    $ DoreenX.Statup("Love", 80, -1)
                    $ DoreenX.Statup("Obed", 30, 4)
                    $ DoreenX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in DoreenX.RecentActions:
                            call Date_Bonus(DoreenX, -Play_Cost)
            elif ApprovalCheck(DoreenX, 900):
                    $ DoreenX.FaceChange("bemused")
                    ch_d "Хмм, в этот раз я смогу оплатить счет. . ."
                    $ DoreenX.Statup("Obed", 30, 3)
                    $ DoreenX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in DoreenX.RecentActions:
                            call Date_Bonus(DoreenX, -Play_Cost)
            else:
                    $ DoreenX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ DoreenX.Statup("Love", 80, -5)
                        ch_d "Я не думала, что мне придется платить еще и за нее. . ."
                    else:
                        ch_d "Я не собираюсь оплачивать твои расходы!"
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Doreen to pay

    elif Line is WandaX:
            #If you ask Wanda to pay
            $ WandaX.Statup("Love", 90, -1)
            if Total_Cost >= 15:
                    $ WandaX.Statup("Love", 200, -2)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    if Party[0] == WandaX and Play_Cost > Date_Cost[0]:
                        $ WandaX.Statup("Love", 200, -1)
                        $ WandaX.Statup("Obed", 80, 4)
                    elif WandaX in Party and Play_Cost > Date_Cost[1]:
                        $ WandaX.Statup("Love", 200, -1)
                        $ WandaX.Statup("Obed", 80, 4)
            if ApprovalCheck(WandaX, 1100) and len(Party) >= 2:
                    $ WandaX.FaceChange("bemused")
                    ch_w "Думаю, я могу оплатить счет. . ."
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 30, 4)
                    $ WandaX.Statup("Obed", 80, 3)
                    if bg_current == "bg restaurant" and "dinnersex" in WandaX.RecentActions:
                            call Date_Bonus(WandaX, -Play_Cost)
            elif ApprovalCheck(WandaX, 900):
                    $ WandaX.FaceChange("bemused")
                    ch_w "Думаю, я могу оплатить счет . ."
                    $ WandaX.Statup("Obed", 30, 3)
                    $ WandaX.Statup("Obed", 80, 2)
                    if bg_current == "bg restaurant" and "dinnersex" in WandaX.RecentActions:
                            call Date_Bonus(WandaX, -Play_Cost)
            else:
                    $ WandaX.FaceChange("angry")
                    if len(Party) >= 2 and not ApprovalCheck(WandaX, 500):
                        $ WandaX.Statup("Love", 80, -5)
                        ch_w "Но я не хочу платить еще и за нее. . ."
                    else:
                        ch_w "Я не собираюсь оплачивать счет!"
                    if Player.Cash >= Play_Cost:
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"
            #end asked Wanda to pay

    if Line == "split":
            #If you ask to split it evenly
            $ Count = len(Party)
            while Count > 0:
                    $ Count -= 1
                    if ApprovalCheck(Party[Count], 600):
                        $ Party[Count].FaceChange("sad",Mouth="normal")
                        $ Party[Count].Statup("Obed", 50, 2)
                        if Party[Count] is RogueX:
                                ch_r "Ладно, думаю, это справедливо."
                        elif Party[Count] is KittyX:
                                ch_k "Ага[KittyX.like]ладно."
                        elif Party[Count] is EmmaX:
                                if not Player.Male:
                                    ch_e "Ладно, все таки ты все еще студентка."
                                else:
                                    ch_e "Ладно, все таки ты все еще студент."
                        elif Party[Count] is LauraX:
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Love", 70, 2)
                                $ LauraX.Statup("Obed", 50, 3)
                                ch_l "Ну, вроде немного."
                        elif Party[Count] is JeanX:
                                $ JeanX.Statup("Obed", 70, 3)
                                ch_j "Ох, как хочешь."
                        elif Party[Count] is StormX:
                                if not Player.Male:
                                    ch_s "Ты всего лишь студентка, у тебя не может быть много денег."
                                else:
                                    ch_s "Ты всего лишь студент, у тебя не может быть много денег."
                        elif Party[Count] is JubesX:
                                ch_v "Ага, это нормально."
                        elif Party[Count] is GwenX:
                                ch_g "Угу, думаю, это справедливо. . ."
                        elif Party[Count] is BetsyX:
                                ch_b "Ох, конечно. . ."
                        elif Party[Count] is DoreenX:
                                ch_d "Ох, хорошо. . ."
                        elif Party[Count] is WandaX:
                                ch_w "Ох, конечно. . ."
                    else:
                        if Date_Cost[Count] >=15:
                                # if it cost more than 15, they like you less.
                                $ Party[Count].Statup("Love", 200, -5,Alt=[[LauraX],200,3])
                        else:
                                $ Party[Count].Statup("Love", 200, -3,Alt=[[LauraX],200,0])
                        if Party[Count] is RogueX:
                                $ RogueX.FaceChange("angry",Eyes="side")
                                if not Player.Male:
                                    ch_r "Тц. Халявщица."
                                else:
                                    ch_r "Тц. Халявщик."
                        elif Party[Count] is KittyX:
                                $ KittyX.FaceChange("angry",Eyes="side")
                                if not Player.Male:
                                    ch_k "Дура."
                                else:
                                    ch_k "Придурок."
                        elif Party[Count] is EmmaX:
                                $ EmmaX.FaceChange("sadside")
                                ch_e "Не приглашай девушку на свидание, если не можешь себе этого позволить."
                        elif Party[Count] is LauraX:
                                $ Party[Count].Statup("Love", 70, 2)
                                ch_l "Конечно."
                        elif Party[Count] is JeanX:
                                $ JeanX.Statup("Obed", 70, 3)
                                ch_j "Ох, как хочешь."
                        elif Party[Count] is StormX:
                                $ StormX.FaceChange("sadside")
                                ch_s "Не откусывай больше, чем можешь прожевать."
                        elif Party[Count] is JubesX:
                                $ JubesX.FaceChange("angry",Eyes="side")
                                ch_v "Это немного, но. . ."
                        elif Party[Count] is GwenX:
                                ch_g "Что? Почему ты думаешь, что у меня есть деньги?"
                        elif Party[Count] is BetsyX:
                                $ BetsyX.Statup("Inbt", 80, 2)
                                ch_b "Ох, конечно. . ."
                        elif Party[Count] is DoreenX:
                                ch_d "Ох, хорошо. . ."
                        elif Party[Count] is WandaX:
                                ch_w "Пожалуй, можно. . ."
                    $ Date_Bonus[Count] -= 10 if Date_Cost[Count] >= 15 else 0
            $ Player.Cash -= Play_Cost

    if Line == "deadbeat":
            #If you cannot pay.
            $ Date_Bonus[0] -= Play_Cost
            $ Date_Bonus[1] -= Play_Cost
            $ Date_Bonus[0] -= (Date_Cost[0] - 10) if Date_Cost[0] > 10 else 0
            $ Date_Bonus[1] -= (Date_Cost[1] - 10) if Date_Cost[1] > 10 else 0
            $ Count = len(Party)
            while Count > 0:
                    $ Count -= 1
                    if Total_Cost >=15:
                            $ Party[Count].Statup("Love", 200, -4)
                            if Play_Cost > Date_Cost[Count]:
                                    $ Party[Count].Statup("Love", 200, -10,Alt=[[EmmaX,LauraX],200,-5])
                                    $ Party[Count].Statup("Obed", 200, 0,Alt=[[EmmaX,LauraX],500,-2])
                    if bg_current == "bg restaurant" and "dinnersex" in Party[Count].RecentActions:
                                    call Date_Bonus(Party[Count], -Total_Cost)
                    $ Party[Count].Statup("Obed", 50, -2,Alt=[[LauraX],500,-3])
                    $ Party[Count].FaceChange("sad")
                    if ApprovalCheck(Party[Count], 800):
                            #pity
                            if Party[Count] == RogueX:
                                    ch_r "Ах, бедняжка."
                            elif Party[Count] is KittyX:
                                    ch_k "Так[KittyX.like]грустно."
                            elif Party[Count] is EmmaX:
                                    ch_e "Ну, это просто безответственно."
                            elif Party[Count] is LauraX:
                                    if not Player.Male:
                                        ch_l "Ты должна покрывать свои собственные расходы, [LauraX.Petname]."
                                    else:
                                        ch_l "Ты должен покрывать свои собственные расходы, [LauraX.Petname]."
                            elif Party[Count] is JeanX:
                                    if not Player.Male:
                                        ch_j "Ты такая жалкая."
                                    else:
                                        ch_j "Ты жалок."
                            elif Party[Count] is StormX:
                                    ch_s "Что ж. Это прискорбно."
                            elif Party[Count] is JubesX:
                                    ch_v "Это печально. . ."
                            elif Party[Count] is GwenX:
                                    ch_g "Думаю, я понимаю, что такое быть на мели. . ."
                            elif Party[Count] is BetsyX:
                                    ch_b "О, конечно, я и не подумала. . ."
                            elif Party[Count] is DoreenX:
                                    ch_d "Думаю, я смогу все оплатить. . ."
                            elif Party[Count] is WandaX:
                                    ch_w "Я могу заплатить за тебя. . ."
                    else:
                            #anger
                            $ Party[Count].Brows = "angry"
                            if Party[Count] is RogueX:
                                    ch_r "Не стоит приглашать девушку на свидание, если ты не можешь себе этого позволить."
                            elif Party[Count] is KittyX:
                                    if not Player.Male:
                                        ch_k "Я бы не пошла с тобой на свидание, если бы знала, что ты такая нищебродка."
                                    else:
                                        ch_k "Я бы не пошла с тобой на свидание, если бы знала, что ты такой нищеброд."
                            elif Party[Count] is EmmaX:
                                    ch_e "Учись жить по своему бюджету, [EmmaX.Petname]."
                            elif Party[Count] is LauraX:
                                    ch_l "Соберись уже."
                                    $ Party[Count].Statup("Love", 200, -1)
                            elif Party[Count] is JeanX:
                                    ch_j "Это прискорбно."
                            elif Party[Count] is StormX:
                                    ch_s "Не откусывай больше, чем можешь прожевать."
                            elif Party[Count] is JubesX:
                                    if not Player.Male:
                                        ch_v "Было бы здорово, если бы ты сказала мне это раньше. . ."
                                    else:
                                        ch_v "Было бы здорово, если бы ты сказал мне это раньше. . ."
                            elif Party[Count] is GwenX:
                                    if not Player.Male:
                                        ch_g "Ты должна была сказать мне, что не знаешь, как расплатиться!"
                                    else:
                                        ch_g "Ты должен был сказать мне, что не знаешь, как расплатиться!"
                            elif Party[Count] is BetsyX:
                                    $ Party[Count].Brows = "sad"
                                    if not Player.Male:
                                        ch_b "Я и не знала, что ты такая бедная. . ."
                                    else:
                                        ch_b "Я и не знала, что ты такой бедный. . ."
                            elif Party[Count] is DoreenX:
                                    ch_d "Думаю, я смогу все оплатить. . ."
                            elif Party[Count] is WandaX:
                                    ch_w "Я могу заплатить за тебя. . ."
                            $ Party[Count].Statup("Love", 200, -3)
                            if "deadbeat" not in Party[Count].History:
                                $ Party[Count].History.append("deadbeat")
                            else:
                                call Girl_Date_Over(Party[Count])
    #end choice consequences

    if JeanX in Party and Line in (JeanX,"split","deadbeat"):
            #if Jean has to pay, she whammies
            if bg_current == "bg restaurant":
                    ch_j "Официант?"
            $ JeanX.FaceChange("confused",Eyes="psychic")
            ch_j "..."
            $ JeanX.FaceChange("sly")
            ch_j "Вот, этого должно хватить."
    elif GwenX in Party and Line in (GwenX,"split","deadbeat"):
            ch_g "Секундочку. . ."
            hide Gwen_Sprite  with easeoutright
            "..."
            $ GwenX.Statup("Inbt", 70, 10)
            show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) with easeinleft
            ch_g "Ладно, я \"избавилась от проблемы.\""

    #Boosts lust based on price spent
    $ Count = int(Date_Bonus[0]/2)
    $ Count = 10 if Count >= 10 else Count

    $ Party[0].Statup("Lust", 60, Count,Alt=[[EmmaX],75,Count])

    $ Count = int(Date_Bonus[1]/2)
    $ Count = 10 if Count >= 10 else Count
    if len(Party) >= 2:
            $ Party[1].Statup("Lust", 60, Count,Alt=[[EmmaX],75,Count])

    $ Count = 0
    $ Play_Cost = 0
    $ Date_Cost[0] = 0
    $ Date_Cost[1] = 0
    return
#end payment   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Date_Bonus(Girl=0, Amount=0):
    #This updates the prime value if the girl is prime, second if not.
    # call Date_Bonus(RogueX,5)
    if Party[0] == Girl:
                $ Date_Bonus[0] += Amount
    elif Girl in Party:
                $ Date_Bonus[1] += Amount
    return


#Start Date End  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_End:#rkeljsvgb
    #The end of the date jumped to from any end of date
    if Time_Count == 2: #evening time
            #makes it night time
            if Round > 20:
                    $ bg_current = "bg date"
                    call Set_The_Scene(Dress=0)
                    "Вы решаете потихоньку пойти назад, когда вокруг вас наступает ночь. . ."

            call Wait(Outfit = 0)

            $ bg_current = "bg date"
            call Set_The_Scene(Dress=0)
    else:
            $ bg_current = "bg player"
            call Set_The_Scene(Entry=1,Dress=0)

    if len(Party) >= 2:
            #if there are two girls
            menu:
                "К кому вы хотите заглянуть в первую очередь?"
                "К [RogueX.Name_dat]" if RogueX in Party:
                        call Girl_Date_End(RogueX)
                "К [KittyX.Name_dat]" if KittyX in Party:
                        call Girl_Date_End(KittyX)
                "К [EmmaX.Name_dat]" if EmmaX in Party:
                        call Girl_Date_End(EmmaX)
                "К [LauraX.Name_dat]" if LauraX in Party:
                        call Girl_Date_End(LauraX)
                "К [JeanX.Name_dat]" if JeanX in Party:
                        call Girl_Date_End(JeanX)
                "К [StormX.Name_dat]" if StormX in Party:
                        call Girl_Date_End(StormX)
                "К [JubesX.Name_dat]" if JubesX in Party:
                        call Girl_Date_End(JubesX)
                "К [GwenX.Name_dat]" if GwenX in Party:
                        call Girl_Date_End(GwenX)
                "К [BetsyX.Name_dat]" if BetsyX in Party:
                        call Girl_Date_End(BetsyX)
                "К [DoreenX.Name_dat]" if DoreenX in Party:
                        call Girl_Date_End(DoreenX)
                "К [WandaX.Name_dat]" if WandaX in Party:
                        call Girl_Date_End(WandaX)
                "Привести их двоих в свою комнату" if len(Party) >= 2:
                        jump Player_Date_End
                "Ни к кому, вернуться в свою комнату": #disable
                        call Date_Ditched
            jump Date_Over
    if Party and Party[0]:
            call Girl_Date_End(Party[0])
    else:
            $ Party = []
            "Вы возвращаетесь в свою комнату."

label Date_Over:
    if Time_Count == 2: #evening time
            #makes it night time
            call Wait(Outfit = 0)
    $ Player.DrainWord("date") #recent
    $ Player.DailyActions.append("post date")
    $ bg_current = "bg player"
    call CleartheRoom("All",0,1)
    jump Misplaced

label Player_Date_End:
    #Called if you call them back to your room
    $ bg_current = "bg player"
    $ BO = Party[:]
    while BO:
            $ BO[0].Loc = "bg player"
            $ BO.remove(BO[0])
    call Set_The_Scene(Dress=0)
    call Taboo_Level
    if len(Party) >= 2:
            "Вы идете с девушками до двери своей комнаты."
            menu:
                "С кем вы хотите поговорить?"
                "С [RogueX.Name_tvo]" if RogueX in Party:
                        call Girl_Date_End(RogueX)
                "С [KittyX.Name_tvo]" if KittyX in Party:
                        call Girl_Date_End(KittyX)
                "С [EmmaX.Name_tvo]" if EmmaX in Party:
                        call Girl_Date_End(EmmaX)
                "С [LauraX.Name_tvo]" if LauraX in Party:
                        call Girl_Date_End(LauraX)
                "С [JeanX.Name_tvo]" if JeanX in Party:
                        call Girl_Date_End(JeanX)
                "С [StormX.Name_tvo]" if StormX in Party:
                        call Girl_Date_End(StormX)
                "С [JubesX.Name_tvo]" if JubesX in Party:
                        call Girl_Date_End(JubesX)
                "С [GwenX.Name_tvo]" if GwenX in Party:
                        call Girl_Date_End(GwenX)
                "С [BetsyX.Name_tvo]" if BetsyX in Party:
                        call Girl_Date_End(BetsyX)
                "С [DoreenX.Name_tvo]" if DoreenX in Party:
                        call Girl_Date_End(DoreenX)
                "С [WandaX.Name_tvo]" if WandaX in Party:
                        call Girl_Date_End(WandaX)
                "Отправиться спать":
                        pass
    elif Party and Party[0]:
            "Вы идете с [Party[0].Name_tvo] до двери своей комнаты."
            call Girl_Date_End(Party[0])
    jump Player_Room


# Start Girl Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Date_End(Girl=0): #nee R_Date_End
    #Called if you end up with girl at the end of the date
    if Girl not in TotalGirls:
            $ Party = []
            jump Date_End
    call Shift_Focus(Girl)
    if bg_current != "bg player":
            #skips this portion if you are in the player's room already
            menu:
                "Отвести [Girl.Name_vin] обратно в ее комнату?":
                    pass
                "Просто вернуться в свою комнату одному.":
                    call Date_Ditched
                    jump Date_Over

            $ bg_current = Girl.Home
            $ Girl.Loc = Girl.Home
            if len(Party) >= 2 and Party[1] is not Girl:
                    $ Party[1].Loc = Girl.Home
            call Set_The_Scene(Dress=0)
            call Taboo_Level

    if len(Party) >= 2 and Party[0] is not Girl:
            # If you picked the secondary girl, it flips them
            $ Party.reverse()
            $ Date_Bonus.reverse()

    if bg_current != "bg player":
            "Вы провожаете [Girl.Name_vin] до ее комнаты."
    if Date_Bonus[0] < 0:
            #if it was a bad date, no bonus
            $ Girl.FaceChange("angry", 0,Eyes = "side")
            if Girl is RogueX:
                    ch_r "Ну, это был бесполезный вечер. Пока, [Player.Name]."
            elif Girl is KittyX:
                    ch_k "Тебе[Girl.like]нужно привести мысли в порядок, [Player.Name]."
            elif Girl is EmmaX:
                    ch_e "Что ж, ладно, у меня бывали свидания и похуже, [Player.Name]."
            elif Girl is LauraX:
                    ch_l "Дерьмовое свидание, [Player.Name]."
            elif Girl is JeanX:
                    ch_j "Надеюсь, ты понимаешь, как плохо все прошло, [Player.Name]?"
            elif Girl is StormX:
                    ch_s "Давай просто будем считать этот вечер неудачным, [Player.Name]."
            elif Girl is JubesX:
                    ch_v "Это был очень ужасный вечер, [Player.Name]. . ."
            elif Girl is GwenX:
                    ch_g "*зевает* мне было так скучно . ."
            elif Girl is BetsyX:
                    ch_b "Здесь так развелкаются вечерами?"
            elif Girl is DoreenX:
                    $ Girl.FaceChange("sadside", 1)
                    ch_d "Это. . . было не очень весело. . ."
            elif Girl is WandaX:
                    ch_w "В тюрьме и то веселее. . ."
            if bg_current == "bg player":
                if Girl is KittyX:
                    "Она проходит сквозь стену в свою комнату."
                else:
                    "Она уходит одна дальше по коридору."
            else:
                    "Она захлопывает перед вами дверь."
            call Set_The_Scene(Entry=1,Dress=0)
            $ Date_Bonus[0] = 0
            call Girl_Date_Over(Girl,0)
            jump Date_End
    else:
        if Date_Bonus[0] > 20:
            #if it was a very good date
            $ Girl.FaceChange("sexy", 1)
            if Girl is RogueX:
                            ch_r "Ну, было очень весело, [Girl.Petname]. Я не хочу, чтобы этот вечер заканчивался. . ."
            elif Girl is KittyX:
                    if bg_current == "bg player":
                            ch_k "Было весело, [Girl.Petname]. Мне обязательно уходить . . ?"
                    else:
                            ch_k "Было весело, [Girl.Petname]. Тебе обязательно уходить. . ?"
            elif Girl is EmmaX:
                    if bg_current == "bg player":
                            ch_e "Это был прекрасный вечер, [Girl.Petname]. Может выпьем по бокалу у тебя?"
                    else:
                            ch_e "Это был прекрасный вечер, [Girl.Petname]. Может зайдешь, выпьем по бокалу? . ."
            elif Girl is LauraX:
                    if bg_current == "bg player":
                            ch_l "Мне было весело, [Girl.Petname]. Мы закончили, или. . ."
                    else:
                            ch_l "Мне было весело, [Girl.Petname]. Мы закончили, или . . ."
            elif Girl is JeanX:
                    if bg_current == "bg player":
                            ch_j "Было весело, [Girl.Petname]. Ну же, пригласи меня войти."
                    else:
                            ch_j "Было весело, [Girl.Petname]. Заходи."
                            menu:
                                "А ты прямолинейна. . .":
                                        $ Girl.FaceChange("confused")
                                        ch_j "???"
                                        $ Girl.FaceChange("sly",1)
                                "...":
                                        pass
            elif Girl is StormX:
                    if bg_current == "bg player":
                            ch_s "Это был восхитительный вечер, [Girl.Petname]. Ты не против, если я зайду?"
                    else:
                            ch_s "Это был восхитительный вечер, [Girl.Petname]. Не хочешь зайти?"
                    menu:
                        "А ты прямолинейна. . .":
                                $ Girl.FaceChange("confused")
                                ch_s "???"
                                $ Girl.FaceChange("sly",1)
                        "Думаю, это была моя реплика..." if bg_current == "bg player":
                                $ Girl.FaceChange("confused")
                                ch_s "Но это твоя комната. . ."
                                $ Girl.FaceChange("sly",1)
                        "...":
                                pass
            elif Girl is JubesX:
                    ch_v "Нууу, это было весело, [Girl.Petname]. . . "
                    ch_v "Думаю, может быть, тебе все же стоит немного поспать? . ."
            elif Girl is GwenX:
                    ch_g "Это было очень весело, [Player.Name]. . ."
                    ch_g "Ты хочешь. . .?"
            elif Girl is BetsyX:
                    ch_b "Это был просто восхитительный вечер. . ."
                    ch_b "Может продолжим внутри?"
            elif Girl is DoreenX:
                    ch_d "Это был веселый вечер. . ."
                    ch_d "Может, поболтаем внутри?"
            elif Girl is WandaX:
                    ch_w "Я очень приятно провела вечер. . ."
                    ch_w "Может, продолжим внутри?"
        else:
            #if it was a mediocre date
            $ Girl.FaceChange("smile", 1)
            if Girl is RogueX:
                    ch_r "Ну, было очень весело, [Girl.Petname]. Мы должны как-нибудь повторить."
            elif Girl is KittyX:
                    ch_k "Ну, было весело, [Girl.Petname]. Напиши мне попозже."
            elif Girl is EmmaX:
                    ch_e "Это был прекрасный вечер, [Girl.Petname]. Мы обязаны повторить."
            elif Girl is LauraX:
                    ch_l "Было весело, [Girl.Petname]. Поговорим позже."
            elif Girl is JeanX:
                    ch_j "Ну, вот и все. Спокойной ночи."
            elif Girl is StormX:
                    ch_s "Мне понравился вечер, [Girl.Petname]. Мы должны как-нибудь повторить."
            elif Girl is JubesX:
                    ch_v "Нууу, это было весело, [Girl.Petname]. Возможно, мы могли бы как-нибудь повторить."
            elif Girl is GwenX:
                    ch_g "Ну, это было весело, мы должны как-нибудь повторить. . ."
            elif Girl is BetsyX:
                    ch_b "Боже, это был прекрасный вечер. Мы просто обязаны повторить."
            elif Girl is DoreenX:
                    ch_d "Сегодня мне было очень весело. . ."
            elif Girl is WandaX:
                    ch_w "Я приятно провела вечер. . ."
        $ Girl.Date += 1
        menu:
            extend ""
            "Может, подаришь мне поцелуй на прощание?":
                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                    if ApprovalCheck(Girl, 600, Bonus=(10*Date_Bonus[0])) and (Player.Male or "nogirls" not in Girl.History):
                        $ Girl.Mouth = "smile"
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ладно, [Girl.Petname]. Думаю, ты это заслужила."
                                else:
                                    ch_r "Ладно, [Girl.Petname]. Думаю, ты это заслужил."
                        elif Girl is KittyX:
                                ch_k "Хихи, думаю, можно. . ."
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname], полагаю, можно тебя немного побаловать."
                        elif Girl is LauraX:
                                ch_l "Ну,  если ты настаиваешь. . ."
                        elif Girl is JeanX:
                                ch_j "Ох, как я могу отказать. . ."
                        elif Girl is StormX:
                                ch_s "Пожалуй, это не повредит. . ."
                        elif Girl is JubesX:
                                ch_v "Конечно, почему нет. . ."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Ох, посмотри на себя, ты такая ушлая. . ."
                                else:
                                    ch_g "Ох, посмотри на себя, ты такой ушлый. . ."
                        elif Girl is BetsyX:
                                ch_b "Это можно. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох, думаю, я не против. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
                        call Date_Sex_Break(Girl,0,2)
                        $ MultiAction = 0
                        call KissPrep
                        $ MultiAction = 1
                    if ApprovalCheck(Girl, 900, Bonus=(10*Date_Bonus[0])) and (Player.Male or "nogirls" not in Girl.History):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                if bg_current == "bg player":
                                        ch_r "Мы провели очень приятный вечер, могу я заскочить к тебе на минутку. . ?"
                                else:
                                        ch_r "Мы провели очень приятный вечер, может, зайдешь ко мне на минутку. . ?"
                        elif Girl is KittyX:
                                ch_k "Хммм . . ."
                                if bg_current == "bg player":
                                        ch_k "Могу я. . . могу я зайти на минутку?"
                                else:
                                        ch_k "Может. . . зайдешь на минутку?"
                        elif Girl is EmmaX:
                                if bg_current == "bg player":
                                        if not Player.Male:
                                            ch_e "Ммм, ты уверена, что я не могу зайти? . ."
                                        else:
                                            ch_e "Ммм, ты уверен, что я не могу зайти? . ."
                                else:
                                        if not Player.Male:
                                            ch_e "Ммм, ты уверена, что не хочешь зайти? . ."
                                        else:
                                            ch_e "Ммм, ты уверен, что не хочешь зайти? . ."
                        elif Girl is LauraX:
                                ch_l "Хммм . . ."
                                ch_l "Могу я. . . занять тебя еще на минутку?"
                        elif Girl is JeanX:
                                ch_j "Хммм . . ."
                                ch_j "Думаю, я хочу провести с тобой еще немного времени."
                        elif Girl is StormX:
                                if bg_current == "bg player":
                                        ch_s "А теперь, я все еще не могу войти? . ."
                                else:
                                        ch_s "А теперь, не хочешь ли ты войти? . ."
                        elif Girl is JubesX:
                                ch_v "Hmmm..."
                                if bg_current == "bg player":
                                        ch_v "Не хочешь. . . пригласить меня войти?"
                                else:
                                        ch_v "Не хочешь. . . войти?"
                        elif Girl is GwenX:
                                if bg_current == "bg player":
                                        ch_g "Нуууу и. . . ты меня пригласишь войти?"
                                else:
                                        ch_g "Нуууу и. . . ты войдешь?"
                        elif Girl is BetsyX:
                                if bg_current == "bg player":
                                        ch_b "Могу я войти? Пропустим по стаканчику."
                                else:
                                        ch_b "Может зайдешь? Пропустим по стаканчику."
                        elif Girl is DoreenX:
                                if bg_current == "bg player":
                                        ch_d "Можно, я зайду ненадолго? . ."
                                else:
                                        ch_d "Не желаешь зайти ко мне ненадолго? . ."
                        elif Girl is WandaX:
                                if bg_current == "bg player":
                                        ch_w "Итак, я могу войти?"
                                else:
                                        ch_w "Итак, ты желаешь войти?"
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                if bg_current == "bg player":
                                        ch_p "Тебе, наверное, уже пора идти, извини."
                                else:
                                        ch_p "Мне, наверное, уже пора идти, извини."
                                call Girl_Date_Over(Girl,0)
                                jump Date_End
                    else:
                        $ Girl.FaceChange("smile", 1)
                        if Girl is RogueX:
                                ch_r "Мы провели очень приятный вечер, увидимся, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Это был приятный вечер, я напишу тебе!"
                        elif Girl is EmmaX:
                                ch_e "Что ж, увидимся завтра, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Это был приятный вечер, увидимся."
                        elif Girl is JeanX:
                                ch_j "Ладно, мне пора идти."
                        elif Girl is StormX:
                                ch_s "Увидимся завтра, [Girl.Petname]."
                        elif Girl is JubesX:
                                ch_v "Хорошо, тогда увидимся завтра, [Girl.Petname]."
                        elif Girl is GwenX:
                                ch_g "Мммм, это был приятный вечер. Увидимся завтра?"
                        elif Girl is BetsyX:
                                ch_b "Ох. Тогда до завтра?"
                        elif Girl is DoreenX:
                                ch_d "Мммм, ладно, тогда увидимся завтра. . ."
                        elif Girl is WandaX:
                                ch_w "Увидимся завтра. . ."
                        $ Date_Bonus[0] = 0
                        call Girl_Date_Over(Girl,0)
                        jump Date_End

            "Может, сначала немного развлечемся?" if bg_current != "bg player":
                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                    if ApprovalCheck(Girl, 800, Bonus=(10*Date_Bonus[0])) and (Player.Male or "nogirls" not in Girl.History):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ладно, [Girl.Petname]. Думаю, ты это заслужила."
                                else:
                                    ch_r "Ладно, [Girl.Petname]. Думаю, ты это заслужил."
                        elif Girl is KittyX:
                                ch_k "Хихи, думаю, можно. . ."
                        elif Girl is EmmaX:
                                ch_e "Ох, ладно, [Girl.Petname]. Я побалую тебя."
                        elif Girl is LauraX:
                                ch_l "Конечно."
                        elif Girl is JeanX:
                                ch_j "Ага, ладно."
                        elif Girl is StormX:
                                ch_s "Да, думаю, можно, [Girl.Petname]."
                        elif Girl is JubesX:
                                ch_v "О, конечно! Ночь только начинается."
                        elif Girl is GwenX:
                                ch_g "Я думала, ты никогда не попросишь. . ."
                        elif Girl is BetsyX:
                                ch_b "Звучит чудесно."
                        elif Girl is DoreenX:
                                ch_d "Здорово!"
                        elif Girl is WandaX:
                                ch_w "О да."
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                ch_p "Мне, наверное, уже пора идти, извини."
                                call Girl_Date_Over(Girl,0)
                                jump Date_End
            "Может, ненадолго зайдешь?" if bg_current == "bg player":
                    if ApprovalCheck(Girl, 800, Bonus=(10*Date_Bonus[0])):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ладно, [Girl.Petname]. Думаю, ты это заслужила."
                                else:
                                    ch_r "Ладно, [Girl.Petname]. Думаю, ты это заслужил."
                        elif Girl is KittyX:
                                ch_k "Хихи, думаю, можно. . ."
                        elif Girl is EmmaX:
                                ch_e "Ох, ладно, [Girl.Petname]. Я побалую тебя."
                        elif Girl is LauraX:
                                ch_l "Конечно."
                        elif Girl is JeanX:
                                ch_j "А? Ладно?"
                        elif Girl is StormX:
                                ch_s "Я надеялась, что ты спросишь. . ."
                        elif Girl is JubesX:
                                ch_v "О, конечно! Ночь только начинается."
                        elif Girl is GwenX:
                                ch_g "Я думала, ты никогда не попросишь. . ."
                        elif Girl is BetsyX:
                                ch_b "Звучит чудесно."
                        elif Girl is DoreenX:
                                ch_d "Здорово!"
                        elif Girl is WandaX:
                                ch_w "Конечно."
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                ch_p "Тебе, наверное, уже пора идти, извини."
                                call Girl_Date_Over(Girl,0)
                                jump Date_End

            "Хорошо, тогда спокойной ночи.":
                    $ Girl.FaceChange("confused", 1)
                    if Girl is EmmaX:
                            $ Girl.Mouth = "smirk"
                            if bg_current == "bg player":
                                    "[Girl.Name_vin] немного разозлили ваши слова, но она все равно уходит."
                            else:
                                    "[Girl.Name_vin] немного разозлили ваши слова, но вы все равно уходите."
                    else:
                            if bg_current == "bg player":
                                    "[Girl.Name_vin] немного расстроили ваши слова, но она все равно уходит."
                            else:
                                    "[Girl.Name_vin] немного расстроили ваши слова, но вы все равно уходите."
                    call Girl_Date_Over(Girl,0)
                    jump Date_End

    # Rogue lets you into her room:
    if bg_current != "bg player":
            $ bg_current = Girl.Home
    call Set_The_Scene(Dress=0)
    call Taboo_Level
    $ Girl.FaceChange("sexy", 1)

    if not Player.Male and "girltalk" not in Girl.History:
            call AnyLine(Girl,"Ты чего-то хочешь?")
            menu:
                "Да нет":
                        jump Misplaced
                "Ага, тебя.":
                    call expression Girl.Tag + "_Girltalk" pass (0) # "Hey, are you inta me?"
                    if "nogirls" in Girl.History:
                        jump Misplaced

    if Girl is RogueX:
            if len(Party) < 2:#not Party[1]:
                            ch_r "Итак, [Girl.Petname], вот мы и остались одни, какие у тебя планы? . ."
            else:
                    if bg_current == "bg player":
                            ch_r "Итак, [Girl.Petname], мы вдвоем в твоей комнате, какие у тебя планы? . ."
                    else:
                            ch_r "Итак, [Girl.Petname], мы вдвоем в моей комнате, какие у тебя планы? . ."
    elif Girl is KittyX:
                            ch_k "Ну вот[Girl.like]теперь мы наедине. . . "
    elif Girl is EmmaX:
            if len(Party) < 2: #not Party[1]:
                            ch_e "Теперь, [Girl.Petname], мы остались наедине, чем ты хочешь заняться дальше? . ."
            else:
                    if bg_current == "bg player":
                            ch_e "Теперь, [Girl.Petname], мы вдвоем в твоей комнате, чем ты хочешь заняться дальше? . ."
                    else:
                            ch_e "Теперь, [Girl.Petname], мы вдвоем в моей комнате, чем ты хочешь заняться дальше? . ."
    elif Girl is LauraX:
                            ch_l "Итак. . . после такого свидания. . . "
    elif Girl is JeanX:
                            ch_j "Итак, есть идеи? . ."
    elif Girl is StormX:
            if len(Party) < 2: #not Party[1]:
                            ch_s "Теперь мы одни, [Girl.Petname], у тебя есть еще какие-нибудь идеи? . ."
            else:
                            ch_s "А теперь, [Girl.Petname], у тебя есть еще какие-нибудь идеи? . ."
    elif Girl is JubesX:
                            ch_v "Иии. . . чем ты хочешь заняться со мной?"
    elif Girl is GwenX:
            if len(Party) < 2: #not Party[1]:
                            ch_g "Теперь, когда я в твоем распоряжении. . ."
            else:
                            ch_g "Теперь, когда мы наедине. . ."
    elif Girl is BetsyX:
            if len(Party) < 2: #not Party[1]:
                            ch_b "Итак, теперь, когда нам никто не мешает. . ."
            else:
                            ch_b "Ну а теперь. . ."
            ch_b ". . .у тебя есть какие-нибудь идеи?"
    elif Girl is DoreenX:
            if len(Party) < 2: #not Party[1]:
                        ch_d "Ну, похоже, теперь мы одни, так что. . ."
            else:
                        ch_d "Ну, теперь, когда мы внутри. . ."
    elif Girl is WandaX:
            ch_w "Теперь, когда мы внутри. . ."
    $ Player.DailyActions.append("post date")
#    $ renpy.pop_call() #removes call to date
#    $ renpy.pop_call() #removes call to Events
    call SexMenu # call expression Girl.Tag + "_SexMenu"  # You have what sex you can get away with

    if "angry" in Girl.RecentActions:
            if bg_current == "bg player":
                if Girl is KittyX:
                    "[KittyX.Name] выскакивает сквозь ближайшую стену."
                elif Girl in (EmmaX,StormX):
                    "[Girl.Name] выходит и возвращается в свою комнату."
                else:
                    "[Girl.Name] убегает."
            else:
                    "[Girl.Name] выталкивает вас в коридор. Вы возвращаетесь в свою комнату."
                    $ bg_current = "bg player"
            call Remove_Girl("All")
            $ Player.DailyActions.append("post date")
            jump Player_Room

    call Sleepover(Girl)
    jump Misplaced

# End Girl Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Date_Ditched(Girls=0):  #rkeljsvgb
    #if you ditch out on a date, called by Date End
    #Girls tracks the number of people who have already answered.
    while Party:
        if Party[0] in TotalGirls:
                call Shift_Focus(Party[0])
                if Party[0] is JeanX:
                        if Girls:
                                $ Party[0].FaceChange("confused")
                                ch_j "Что? А, да, пока."
                        else:
                                ch_j "Ох, ну, тогда, пока."
                elif ApprovalCheck(Party[0], 1200):
                    $ Party[0].FaceChange("confused")
                    if Party[0] is RogueX:
                            if Girls:
                                    ch_r "Ну, пока?"
                            else:
                                    ch_r "А? Ладно, тогда, думаю, пока."
                    elif Party[0] is KittyX:
                            if Girls:
                                    ch_k "Да, эм, ну пока?"
                            else:
                                    ch_k "Эм, пока?"
                    elif Party[0] is EmmaX:
                            if Girls:
                                    ch_e "Да, жаль."
                            else:
                                    ch_e "Ох? Жаль."
                    elif Party[0] is LauraX:
                            if Girls:
                                    ch_l "Ага, пока."
                            else:
                                    ch_l "Эм, ладно, пока."
                    elif Party[0] is StormX:
                            if Girls:
                                    ch_s "Ох? Что ж, жаль."
                            else:
                                    ch_s "Что ж, жаль."
                    elif Party[0] is JubesX:
                            if Girls:
                                    ch_v "Ну тогда. . . пока?"
                            else:
                                    ch_v "Эм, пока?"
                    elif Party[0] is GwenX:
                            if Girls:
                                    ch_g "Ладно. . . пока. . ."
                            else:
                                    ch_g "Тогда пока?"
                    elif Party[0] is BetsyX:
                            if Girls:
                                    ch_b "Ясно. . . тогда пока. . ."
                            else:
                                    ch_b "Ужасно. . ."
                    elif Party[0] is DoreenX:
                            if Girls:
                                    ch_d "Ага. . . пока. . ."
                            else:
                                    ch_d "Тогда пока?"
                    elif Party[0] is WandaX:
                            if Girls:
                                    ch_w "Ладно. . . пока. . ."
                            else:
                                    ch_w "Пока?"
                elif ApprovalCheck(Party[0], 400):
                    $ Party[0].FaceChange("smile")
                    if Party[0] is RogueX:
                            if Girls:
                                    ch_r "Ага, увидимся позже."
                            else:
                                    ch_r "Ох, ну, тогда, пока."
                    elif Party[0] is KittyX:
                            if Girls:
                                    ch_k "Ага, пока!"
                            else:
                                    ch_k "Пока!"
                    elif Party[0] is EmmaX:
                            if Girls:
                                    ch_e "Ох, да, спокойной ночи."
                            else:
                                    ch_e "Тогда спокойной ночи."
                    elif Party[0] is LauraX:
                            if Girls:
                                    ch_l "Ага, пока."
                            else:
                                    ch_l "Эм, ладно, пока."
                    elif Party[0] is StormX:
                            if Girls:
                                    ch_s "Ох? Что ж, жаль."
                            else:
                                    ch_s "Что ж, жаль."
                    elif Party[0] is JubesX:
                            if Girls:
                                    ch_v "Ну тогда. . . пока?"
                            else:
                                    ch_v "Эм, пока?"
                    elif Party[0] is GwenX:
                            if Girls:
                                    ch_g "Ладно. . . пока. . ."
                            else:
                                    ch_g "Тогда пока. . ."
                    elif Party[0] is BetsyX:
                            if Girls:
                                    ch_b "Ясно. . . тогда пока. . ."
                            else:
                                    ch_b "Ужасно. . ."
                    elif Party[0] is DoreenX:
                            if Girls:
                                    ch_d "Ага. . . пока. . ."
                            else:
                                    ch_d "Тогда пока?"
                    elif Party[0] is WandaX:
                            if Girls:
                                    ch_w "Ладно. . . пока. . ."
                            else:
                                    ch_w "Пока?"
                else:
                    $ Party[0].FaceChange("angry")
                    if Party[0] is RogueX:
                            if Girls:
                                    ch_r "Ага, \"пока.\""
                            else:
                                    ch_r "Скатертью дорога."
                    elif Party[0] is KittyX:
                            if Girls:
                                    if not Player.Male:
                                        ch_k "Ага, пока, дура."
                                    else:
                                        ch_k "Ага, пока, придурок."
                            else:
                                    if not Player.Male:
                                        ch_k "Пока, коза."
                                    else:
                                        ch_k "Пока, козел."
                    elif Party[0] is EmmaX:
                            if Girls:
                                    ch_e "И почему я не удивлена."
                            else:
                                    if not Player.Male:
                                        ch_e "Свободна!"
                                    else:
                                        ch_e "Свободен!"
                    elif Party[0] is LauraX:
                            if Girls:
                                    ch_l "Ого, ага, пока."
                            else:
                                    if not Player.Male:
                                        ch_l "Да пошла ты."
                                    else:
                                        ch_l "Да пошел ты."
                    elif Party[0] is StormX:
                            if Girls:
                                    ch_s "Да, я разочарована."
                            else:
                                    ch_s "Какая катастрофа."
                    elif Party[0] is JubesX:
                            if Girls:
                                    ch_v "Ага, уходи. . ."
                            else:
                                    ch_v "Эм, пока?"
                    elif Party[0] is GwenX:
                            if Girls:
                                    ch_g "Да, я так и думала. . ."
                            else:
                                    ch_g "Угу-м. . ."
                    elif Party[0] is BetsyX:
                            if Girls:
                                    ch_b "Ясно. . . тогда пока. . ."
                            else:
                                    ch_b "Ужасно. . ."
                    elif Party[0] is DoreenX:
                            if Girls:
                                    ch_d "Ага. . . пока. . ."
                            else:
                                    ch_d "Тогда пока?"
                    elif Party[0] is WandaX:
                            if Girls:
                                    ch_w "Ладно. . . пока. . ."
                            else:
                                    ch_w "Пока?"
                $ Party[0].Loc = Party[0].Home
                $ Girls += 1
        $ Party.remove(Party[0])
    return

# Start Girl Date Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Date_Over(Girl=0,Angry=1): #rkeljsvgb
        # Called if Girl is pissed and leaves
        if Angry:
                $ Girl.RecentActions.append("angry")
                $ Girl.DailyActions.append("angry")
                $ Girl.FaceChange("angry")
                if Girl is RogueX:
                        ch_r "Думаю, меня здесь больше ничего не держит, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Знаешь что?"
                        if not Player.Male:
                            ch_k "[Player.Name], ты дура!"
                        else:
                            ch_k "[Player.Name], ты придурок!"
                elif Girl is EmmaX:
                        ch_e "Достаточно, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Что это было?"
                        ch_l "Пожуй хуев."
                elif Girl is JeanX:
                        if not Player.Male:
                            ch_j "Ооооо, ты все испортила."
                        else:
                            ch_j "Ооооо, ты все испортил."
                elif Girl is StormX:
                        ch_s "С меня хватит."
                elif Girl is JubesX:
                        ch_v "Нууу, я пошла. . ."
                elif Girl is GwenX:
                        if len(Party) < 2:
                                if not Player.Male:
                                    ch_g "Да пошла ты, я к себе. . ."
                                else:
                                    ch_g "Да пошел ты, я к себе. . ."
                        else:
                                ch_g "Да пошли вы, я к себе. . ."
                elif Girl is BetsyX:
                        ch_b "Это непростительно."
                        ch_b "Я должна уйти."
                elif Girl is DoreenX:
                        ch_d "Что за сумасшествие."
                        ch_d "Мне пора."
                elif Girl is WandaX:
                        ch_w "Ладно, я пошла. . ."
                "[Girl.Name] убегает."
        if "study" in Player.RecentActions:
                call Remove_Girl(Girl)
                return
        if Party[0] == Girl:
                $ Date_Bonus[0] = Date_Bonus[1]
                $ Date_Cost[0] = Date_Cost[1]
                $ Date_Cost[1] = 0
        elif Girl in Party:
                # If this person was in the second slot, flip them.
                $ Date_Bonus.reverse
                $ Date_Cost.reverse
        if Girl in Present:
                $ Present.remove(Girl)

        $ Date_Bonus[1] = 0
        $ Date_Cost[1] = 0
        call Remove_Girl(Girl)
        if not Party:
                #if nobody is left, quit the date
                jump Date_End
        call Shift_Focus(Party[0])
        return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
