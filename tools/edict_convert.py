# encoding: utf-8

import re


def kana_to_rime_code(string: str):
    string = string.replace('ー', '--')
    string = string.replace('あ', 'qa')
    string = string.replace('い', 'qi')
    string = string.replace('う', 'qu')
    string = string.replace('え', 'qe')
    string = string.replace('お', 'qo')
    string = string.replace('ゔ', 'vu')
    string = string.replace('か', 'ka')
    string = string.replace('き', 'ki')
    string = string.replace('く', 'ku')
    string = string.replace('け', 'ke')
    string = string.replace('こ', 'ko')
    string = string.replace('が', 'ga')
    string = string.replace('ぎ', 'gi')
    string = string.replace('ぐ', 'gu')
    string = string.replace('げ', 'ge')
    string = string.replace('ご', 'go')
    string = string.replace('さ', 'sa')
    string = string.replace('し', 'si')
    string = string.replace('す', 'su')
    string = string.replace('せ', 'se')
    string = string.replace('そ', 'so')
    string = string.replace('ざ', 'za')
    string = string.replace('じ', 'zi')
    string = string.replace('ず', 'zu')
    string = string.replace('ぜ', 'ze')
    string = string.replace('ぞ', 'zo')
    string = string.replace('た', 'ta')
    string = string.replace('ち', 'ti')
    string = string.replace('つ', 'tu')
    string = string.replace('て', 'te')
    string = string.replace('と', 'to')
    string = string.replace('だ', 'da')
    string = string.replace('ぢ', 'di')
    string = string.replace('づ', 'du')
    string = string.replace('で', 'de')
    string = string.replace('ど', 'do')
    string = string.replace('な', 'na')
    string = string.replace('に', 'ni')
    string = string.replace('ぬ', 'nu')
    string = string.replace('ね', 'ne')
    string = string.replace('の', 'no')
    string = string.replace('は', 'ha')
    string = string.replace('ひ', 'hi')
    string = string.replace('ふ', 'hu')
    string = string.replace('へ', 'he')
    string = string.replace('ほ', 'ho')
    string = string.replace('ば', 'ba')
    string = string.replace('び', 'bi')
    string = string.replace('ぶ', 'bu')
    string = string.replace('べ', 'be')
    string = string.replace('ぼ', 'bo')
    string = string.replace('ぱ', 'pa')
    string = string.replace('ぴ', 'pi')
    string = string.replace('ぷ', 'pu')
    string = string.replace('ぺ', 'pe')
    string = string.replace('ぽ', 'po')
    string = string.replace('ま', 'ma')
    string = string.replace('み', 'mi')
    string = string.replace('む', 'mu')
    string = string.replace('め', 'me')
    string = string.replace('も', 'mo')
    string = string.replace('や', 'ya')
    string = string.replace('ゆ', 'yu')
    string = string.replace('よ', 'yo')
    string = string.replace('ら', 'ra')
    string = string.replace('り', 'ri')
    string = string.replace('る', 'ru')
    string = string.replace('れ', 're')
    string = string.replace('ろ', 'ro')
    string = string.replace('わ', 'wa')
    string = string.replace('ゐ', 'wi')
    string = string.replace('ゑ', 'we')
    string = string.replace('を', 'wo')
    string = string.replace('ん', 'nn')
    string = string.replace('ぁ', 'xa')
    string = string.replace('ぃ', 'xi')
    string = string.replace('ぅ', 'xu')
    string = string.replace('ぇ', 'xe')
    string = string.replace('ぉ', 'xo')
    string = string.replace('ゃ', 'la')
    string = string.replace('ゅ', 'lu')
    string = string.replace('ょ', 'lo')
    string = string.replace('ゎ', 'va')
    string = string.replace('ゕ', 'ka')
    string = string.replace('ゖ', 'ke')
    string = string.replace('っ', 'xx')
    string = string.replace('ア', 'qa')
    string = string.replace('イ', 'qi')
    string = string.replace('ウ', 'qu')
    string = string.replace('エ', 'qe')
    string = string.replace('オ', 'qo')
    string = string.replace('ヴ', 'vu')
    string = string.replace('カ', 'ka')
    string = string.replace('キ', 'ki')
    string = string.replace('ク', 'ku')
    string = string.replace('ケ', 'ke')
    string = string.replace('コ', 'ko')
    string = string.replace('ガ', 'ga')
    string = string.replace('ギ', 'gi')
    string = string.replace('グ', 'gu')
    string = string.replace('ゲ', 'ge')
    string = string.replace('ゴ', 'go')
    string = string.replace('サ', 'sa')
    string = string.replace('シ', 'si')
    string = string.replace('ス', 'su')
    string = string.replace('セ', 'se')
    string = string.replace('ソ', 'so')
    string = string.replace('ザ', 'za')
    string = string.replace('ジ', 'zi')
    string = string.replace('ズ', 'zu')
    string = string.replace('ゼ', 'ze')
    string = string.replace('ゾ', 'zo')
    string = string.replace('タ', 'ta')
    string = string.replace('チ', 'ti')
    string = string.replace('ツ', 'tu')
    string = string.replace('テ', 'te')
    string = string.replace('ト', 'to')
    string = string.replace('ダ', 'da')
    string = string.replace('ヂ', 'di')
    string = string.replace('ヅ', 'du')
    string = string.replace('デ', 'de')
    string = string.replace('ド', 'do')
    string = string.replace('ナ', 'na')
    string = string.replace('ニ', 'ni')
    string = string.replace('ヌ', 'nu')
    string = string.replace('ネ', 'ne')
    string = string.replace('ノ', 'no')
    string = string.replace('ハ', 'ha')
    string = string.replace('ヒ', 'hi')
    string = string.replace('フ', 'hu')
    string = string.replace('ヘ', 'he')
    string = string.replace('ホ', 'ho')
    string = string.replace('バ', 'ba')
    string = string.replace('ビ', 'bi')
    string = string.replace('ブ', 'bu')
    string = string.replace('ベ', 'be')
    string = string.replace('ボ', 'bo')
    string = string.replace('パ', 'pa')
    string = string.replace('ピ', 'pi')
    string = string.replace('プ', 'pu')
    string = string.replace('ペ', 'pe')
    string = string.replace('ポ', 'po')
    string = string.replace('マ', 'ma')
    string = string.replace('ミ', 'mi')
    string = string.replace('ム', 'mu')
    string = string.replace('メ', 'me')
    string = string.replace('モ', 'mo')
    string = string.replace('ヤ', 'ya')
    string = string.replace('ユ', 'yu')
    string = string.replace('ヨ', 'yo')
    string = string.replace('ラ', 'ra')
    string = string.replace('リ', 'ri')
    string = string.replace('ル', 'ru')
    string = string.replace('レ', 're')
    string = string.replace('ロ', 'ro')
    string = string.replace('ワ', 'wa')
    string = string.replace('ヰ', 'wi')
    string = string.replace('ヱ', 'we')
    string = string.replace('ヲ', 'wo')
    string = string.replace('ン', 'nn')
    string = string.replace('ァ', 'xa')
    string = string.replace('ィ', 'xi')
    string = string.replace('ゥ', 'xu')
    string = string.replace('ェ', 'xe')
    string = string.replace('ォ', 'xo')
    string = string.replace('ャ', 'la')
    string = string.replace('ュ', 'lu')
    string = string.replace('ョ', 'lo')
    string = string.replace('ヮ', 'va')
    string = string.replace('ヵ', 'ka')
    string = string.replace('ヶ', 'ke')
    string = string.replace('ッ', 'xx')
    string = string.replace('・', '')
    return string


def parse_line(string: str):
    lineElements = string.split(' ')
    expressList = lineElements[0].split(';')
    for i in range(len(expressList)):
        expressList[i] = re.sub(r'\([A-z]+?\)', '', expressList[i])
    if lineElements[1][0] == '/':
        kanaDict = {}
        for i in range(len(expressList)-1,-1,-1):
            kanaDict[kana_to_rime_code(expressList[i])] = [expressList[i]]
        typeList = lineElements[1][2:-1].split(',')
    else:
        kanaDict = {}
        kanaList = lineElements[1][1:-1].split(';')
        for i in range(len(kanaList)):
            kanaList[i] = re.sub(r'\([A-z]+?\)', '', kanaList[i])
            if re.search(r'\(', kanaList[i]):
                tmpKana = kanaList[i][:-1].split('(')[0]
                tmpExpressList = kanaList[i][:-1].split('(')[1].split(',')
                tmpExpressList.append(tmpKana)
                kanaDict[kana_to_rime_code(tmpKana)] = tmpExpressList
            else:
                expressList.append(kanaList[i])
                kanaDict[kana_to_rime_code(kanaList[i])] = expressList
                expressList = expressList[:-1]
        typeList = lineElements[2][2:-1].split(',')
    return kanaDict, typeList


def five_grade_verb_ending(verb: str):
    return verb[-1]


def five_grade_ending_change(ending: str):
    if ending == 'う':
        return ['あ', 'い', 'え', 'お']
    if ending == 'く':
        return ['か', 'き', 'け', 'こ']
    if ending == 'ぐ':
        return ['が', 'ぎ', 'げ', 'ご']
    if ending == 'す':
        return ['さ', 'し', 'せ', 'そ']
    if ending == 'つ':
        return ['た', 'ち', 'て', 'と']
    if ending == 'ぬ':
        return ['な', 'に', 'ね', 'の']
    if ending == 'ぶ':
        return ['ば', 'び', 'べ', 'ぼ']
    if ending == 'む':
        return ['ま', 'み', 'め', 'も']
    if ending == 'る':
        return ['ら', 'り', 'れ', 'ろ']


def onbin(ending: str):
    if ending == 'う' or ending == 'つ' or ending == 'る':
        return ['って', 'った', 'ったら', 'ったり']
    if ending == 'く':
        return ['いて', 'いた', 'いたら', 'いたり']
    if ending == 'ぐ':
        return ['いで', 'いだ', 'いだら', 'いだり']
    if ending == 'ぬ' or ending == 'む' or ending == 'ぶ':
        return ['んで', 'んだ', 'んだら', 'んだり']
    if ending == 'す':
        return ['して', 'した', 'したら', 'したり']


def five_grade_verb_conjugate(kanaDict: dict):
    suffixList1 = ['ない', 'なかろ', 'なく', 'なかった', 'なかったら', 'なかったり', 'なくて',
                   'ないで', 'なそう', 'なさそう', 'なければ', 'なかろう', 'ぬ', 'ん', 'ず', 'ねば', 'れる', 'せる', 'される']
    suffixList2 = ['', 'ませ', 'ましょ', 'ません', 'ませんでした', 'ました', 'ましたら',
                   'まして', 'ます', 'まする', 'ますれば', 'ませば', 'ませ', 'まし', 'ましょう', 'たい', 'れる']
    suffixList3 = ['', 'ば', 'る']
    suffixList4 = ['う']
    result = []
    for code, wordList in kanaDict.items():
        ending = five_grade_verb_ending(wordList[-1])
        changedSuffixList = five_grade_ending_change(ending)
        onbinList = onbin(ending)
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == ending:
                stemList.append(expresses[:-1])
        if onbinList:
            for sufs in onbinList:
                for stems in stemList:
                    result.append(
                        [codeStem + kana_to_rime_code(sufs), stems + sufs])
            for sufs in suffixList1:
                for stems in stemList:
                    changedSuffix = changedSuffixList[0]
                    result.append(
                        [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
            for sufs in suffixList2:
                for stems in stemList:
                    changedSuffix = changedSuffixList[1]
                    result.append(
                        [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
            for sufs in suffixList3:
                for stems in stemList:
                    changedSuffix = changedSuffixList[2]
                    result.append(
                        [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
            for sufs in suffixList4:
                for stems in stemList:
                    changedSuffix = changedSuffixList[3]
                    result.append(
                        [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
    return result


def five_grade_aru_ending_change():
    return ['ら', 'り', 'い', 'れ', 'ろ']


def five_grade_aru_verb_conjugate(kanaDict: dict):
    suffixList1 = ['ない', 'なかろ', 'なく', 'なかった', 'なかったら', 'なかったり', 'なくて',
                   'ないで', 'なそう', 'なさそう', 'なければ', 'なかろう', 'ぬ', 'ん', 'ず', 'ねば', 'れる', 'せる', 'される']
    suffixList2 = ['', 'ませ', 'ましょ', 'ません', 'ませんでした', 'ました', 'ましたら',
                   'まして', 'ます', 'まする', 'ますれば', 'ませば', 'ませ', 'まし', 'ましょう', 'たい', 'れる']
    suffixList3 = ['', 'ば', 'る']
    suffixList4 = ['う']
    result = []
    for code, wordList in kanaDict.items():
        ending = 'る'
        changedSuffixList = five_grade_aru_ending_change()
        onbinList = ['って', 'った', 'ったら', 'ったり']
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == ending:
                stemList.append(expresses[:-1])
        for sufs in onbinList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
        for sufs in suffixList1:
            for stems in stemList:
                changedSuffix = changedSuffixList[0]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList2:
            for stems in stemList:
                changedSuffix = changedSuffixList[1]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
                changedSuffix = changedSuffixList[2]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList3:
            for stems in stemList:
                changedSuffix = changedSuffixList[3]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList4:
            for stems in stemList:
                changedSuffix = changedSuffixList[4]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
    return result


def five_grade_iku_verb_conjugate(kanaDict: dict):
    suffixList1 = ['ない', 'なかろ', 'なく', 'なかった', 'なかったら', 'なかったり', 'なくて',
                   'ないで', 'なそう', 'なさそう', 'なければ', 'なかろう', 'ぬ', 'ん', 'ず', 'ねば', 'れる', 'せる', 'される']
    suffixList2 = ['', 'ませ', 'ましょ', 'ません', 'ませんでした', 'ました', 'ましたら',
                   'まして', 'ます', 'まする', 'ますれば', 'ませば', 'ませ', 'まし', 'ましょう', 'たい', 'れる']
    suffixList3 = ['', 'ば', 'る']
    suffixList4 = ['う']
    result = []
    for code, wordList in kanaDict.items():
        ending = five_grade_verb_ending(wordList[-1])
        changedSuffixList = five_grade_ending_change(ending)
        onbinList = ['って', 'った', 'ったら', 'ったり']
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == ending:
                stemList.append(expresses[:-1])
        for sufs in onbinList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
        for sufs in suffixList1:
            for stems in stemList:
                changedSuffix = changedSuffixList[0]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList2:
            for stems in stemList:
                changedSuffix = changedSuffixList[1]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList3:
            for stems in stemList:
                changedSuffix = changedSuffixList[2]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList4:
            for stems in stemList:
                changedSuffix = changedSuffixList[3]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
    return result


def five_grade_r_irr_verb_conjugate(kanaDict: dict):
    suffixList1 = ['れる', 'せる', 'される', 'ぬ', 'ん', 'ず', 'ねば']
    suffixList1Sp = ['ない', 'なかろ', 'なく', 'なかった', 'なかったら', 'なかったり', 'なくて',
                     'ないで', 'なそう', 'なさそう', 'なければ', 'なかろう']
    suffixList2 = ['', 'ませ', 'ましょ', 'ません', 'ませんでした', 'ました', 'ましたら',
                   'まして', 'ます', 'まする', 'ますれば', 'ませば', 'ませ', 'まし', 'ましょう', 'たい', 'れる']
    suffixList3 = ['', 'ば', 'る']
    suffixList4 = ['う']
    result = []
    for code, wordList in kanaDict.items():
        ending = five_grade_verb_ending(wordList[-1])
        changedSuffixList = five_grade_ending_change(ending)
        onbinList = onbin(ending)
        codeStem = code[:-2]
        codeStemSp = code[:-4]
        stemList = []
        stemListSp = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == ending:
                stemList.append(expresses[:-1])
        for expresses in stemList:
            stemListSp.append(expresses[:-1])
        for sufs in onbinList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
        for sufs in suffixList1:
            for stems in stemList:
                changedSuffix = changedSuffixList[0]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList1Sp:
            for stems in stemListSp:
                result.append(
                    [codeStemSp + kana_to_rime_code(sufs), stems + sufs])
        for sufs in suffixList2:
            for stems in stemList:
                changedSuffix = changedSuffixList[1]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList3:
            for stems in stemList:
                changedSuffix = changedSuffixList[2]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList4:
            for stems in stemList:
                changedSuffix = changedSuffixList[3]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
    return result


def five_grade_u_sp_verb_conjugate(kanaDict: dict):
    suffixList1 = ['ない', 'なかろ', 'なく', 'なかった', 'なかったら', 'なかったり', 'なくて',
                   'ないで', 'なそう', 'なさそう', 'なければ', 'なかろう', 'ぬ', 'ん', 'ず', 'ねば', 'れる', 'せる', 'される']
    suffixList2 = ['', 'ませ', 'ましょ', 'ません', 'ませんでした', 'ました', 'ましたら',
                   'まして', 'ます', 'まする', 'ますれば', 'ませば', 'ませ', 'まし', 'ましょう', 'たい', 'れる']
    suffixList3 = ['', 'ば', 'る']
    suffixList4 = ['う']
    result = []
    for code, wordList in kanaDict.items():
        ending = five_grade_verb_ending(wordList[-1])
        changedSuffixList = five_grade_ending_change(ending)
        onbinList = ['うて', 'うた', 'うたら', 'うたり']
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == ending:
                stemList.append(expresses[:-1])
        for sufs in onbinList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
        for sufs in suffixList1:
            for stems in stemList:
                changedSuffix = changedSuffixList[0]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList2:
            for stems in stemList:
                changedSuffix = changedSuffixList[1]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList3:
            for stems in stemList:
                changedSuffix = changedSuffixList[2]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
        for sufs in suffixList4:
            for stems in stemList:
                changedSuffix = changedSuffixList[3]
                result.append(
                    [codeStem + kana_to_rime_code(changedSuffix + sufs), stems + changedSuffix + sufs])
    return result


def monograde_verb_conjugate(kanaDict: dict):
    suffixList = ['ない', 'られる', 'される', 'させられる', 'ます', 'たい',
                  'そう', 'た', 'たら', 'たり', 'て', 'れば', 'られる', 'れる', 'ろ', 'よ', 'よう']
    result = []
    for code, wordList in kanaDict.items():
        ending = 'る'
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == ending:
                stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def monograde_kureru_verb_conjugate(kanaDict: dict):
    suffixList = ['ない', 'られる', 'される', 'させられる', 'ます', 'たい',
                  'そう', 'た', 'たら', 'たり', 'て', 'れば', 'られる', 'れる', '', 'よう']
    result = []
    for code, wordList in kanaDict.items():
        ending = 'る'
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == ending:
                stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def kuru_verb_conjugate(kanaDict: dict):
    suffixKanaList = ['こない', 'こられる', 'こさせる', 'こさらせる',
                      'きます', 'きたい', 'きそう', 'きた', 'きたら', 'きたり', 'きて', 'くれば', 'こられる', 'これる', 'こい', 'こよう']
    suffixList = ['来ない', '来られる', '来させる', '来さらせる',
                  '来ます', '来たい', '来そう', '来た', '来たら', '来たり', '来て', '来れば', '来られる', '来れる', '来い', '来よう']
    result = []
    for code, wordList in kanaDict.items():
        ending = 'くる'
        codeStem = code[:-4]
        stemList = []
        stemKanaList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-2:] != ending:
                stemList.append(expresses[:-2])
            else:
                stemKanaList.append(expresses[:-2])
        for i in range(len(suffixList)):
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(suffixKanaList[i]), stems + suffixList[i]])
            for stems in stemKanaList:
                result.append(
                    [codeStem + kana_to_rime_code(suffixKanaList[i]), stems + suffixKanaList[i]])
    return result


def suru_verb_conjugate(kanaDict: dict):
    suffixList = ['しない', 'される', 'させる', 'させられる',
                  'します', 'したい', 'しそう', 'した', 'したら', 'したり', 'して', 'すれば', 'できる', 'せよ', 'しろ', 'しよう']
    result = []
    for code, wordList in kanaDict.items():
        for expresses in wordList:
            result.append([code, expresses])
        for sufs in suffixList:
            for stems in wordList:
                result.append(
                    [code + kana_to_rime_code(sufs), stems + sufs])
    return result


def suru_sp_verb_conjugate(kanaDict: dict):
    suffixList = ['しない', 'せられる', 'しられる', 'しさせる', 'しさせられる',
                  'します', 'したい', 'しそう', 'した', 'したら', 'したり', 'して', 'すれば', 'せよ', 'しろ', 'しよう']
    result = []
    for code, wordList in kanaDict.items():
        stemList = []
        codeStem = code[:-4]
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-2:] == 'する':
                stemList.append(expresses[-2:])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def zuru_verb_conjugate(kanaDict: dict):
    suffixListZuru = ['じない', 'ぜられる', 'じられる', 'じさせる', 'じさせられる',
                      'じます', 'じたい', 'じそう', 'じた', 'じたら', 'じたり', 'じて', 'ずる', 'ずれば', 'ぜよ', 'じろ', 'じよう']
    suffixListZiru = ['じない', 'ぜられる', 'じられる', 'じさせる', 'じさせられる',
                      'じます', 'じたい', 'じそう', 'じた', 'じたら', 'じたり', 'じて', 'じる', 'じれば', 'ぜよ', 'じろ', 'じよう']
    result = []
    for code, wordList in kanaDict.items():
        codeStem = code[:-4]
        stemZuru = []
        stemZiru = []
        for expresses in wordList:
            result.append([code, expresses])
            stem = expresses[:-2]
            ending = expresses[-2:]
            if ending == 'じる':
                stemZiru.append(stem)
            elif ending == 'ずる':
                stemZuru.append(stem)
        for sufs in suffixListZuru:
            for stems in stemZuru:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
        for sufs in suffixListZiru:
            for stems in stemZiru:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def su_verb_conjugate(kanaDict: dict):
    suffixList = ['さない', 'しない', 'される', 'させる', 'させられる',
                  'します', 'したい', 'しそう', 'した', 'したら', 'したり', 'して', 'する', 'すれば', 'せば', 'せる', 'せよ', 'せ', 'しろ', 'しよう', 'そう']
    result = []
    for code, wordList in kanaDict.items():
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            if expresses[-1] == 'す':
                stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def four_grade_ending_change(ending: str):
    if ending == 'う':
        return ['あ', 'い', 'う', 'え']
    if ending == 'く':
        return ['か', 'き', 'く', 'け']
    if ending == 'ぐ':
        return ['が', 'ぎ', 'ぐ', 'げ']
    if ending == 'す':
        return ['さ', 'し', 'す', 'せ']
    if ending == 'つ':
        return ['た', 'ち', 'つ', 'て']
    if ending == 'ふ':
        return ['は', 'ひ', 'ふ', 'へ']
    if ending == 'ぶ':
        return ['ば', 'び', 'ぶ', 'べ']
    if ending == 'む':
        return ['ま', 'み', 'む', 'め']
    if ending == 'る':
        return ['ら', 'り', 'る', 'れ']


def four_grade_verb_conjugate(kanaDict: dict):
    result = []
    for code, wordList in kanaDict.items():
        ending = wordList[-1][-1]
        codeStem = code[:-2]
        stemList = []
        suffixList = four_grade_ending_change(ending)
        if not suffixList:
            ending = wordList[0][-1]
        suffixList = four_grade_ending_change(ending)
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def lower_bigrade_ending_change(ending: str):
    if ending == 'う':
        return ['え', 'う', 'うる', 'うれ', 'えよ']
    if ending == 'く':
        return ['け', 'く', 'くる', 'くれ', 'けよ']
    if ending == 'ぐ':
        return ['げ', 'ぐ', 'ぐる', 'ぐれ', 'げよ']
    if ending == 'す':
        return ['せ', 'す', 'する', 'すれ', 'せよ']
    if ending == 'ず':
        return ['ぜ', 'ず', 'ずる', 'ずれ', 'ぜよ']
    if ending == 'つ':
        return ['て', 'つ', 'つる', 'つれ', 'てよ']
    if ending == 'づ':
        return ['で', 'づ', 'づる', 'づれ', 'でよ']
    if ending == 'ぬ':
        return ['ね', 'ぬ', 'ぬる', 'ぬれ', 'ねよ']
    if ending == 'ふ':
        return ['へ', 'ふ', 'ふる', 'ふれ', 'へよ']
    if ending == 'ぶ':
        return ['べ', 'ぶ', 'ぶる', 'ぶれ', 'べよ']
    if ending == 'む':
        return ['め', 'む', 'むる', 'むれ', 'めよ']
    if ending == 'ゆ':
        return ['え', 'ゆ', 'ゆる', 'ゆれ', 'えよ']
    if ending == 'る':
        return ['れ', 'る', 'るる', 'るれ', 'れよ']


def lower_bigrade_verb_conjugate(kanaDict: dict):
    result = []
    for code, wordList in kanaDict.items():
        ending = wordList[-1][-1]
        codeStem = code[:-2]
        stemList = []
        suffixList = lower_bigrade_ending_change(ending)
        if not suffixList:
            ending = wordList[0][-1]
        suffixList = lower_bigrade_ending_change(ending)
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def upper_bigrade_ending_change(ending: str):
    if ending == 'く':
        return ['き', 'く', 'くる', 'くれ', 'きよ']
    if ending == 'ぐ':
        return ['ぎ', 'ぐ', 'ぐる', 'ぐれ', 'ぎよ']
    if ending == 'つ':
        return ['ち', 'つ', 'つる', 'つれ', 'ちよ']
    if ending == 'づ':
        return ['ぢ', 'づ', 'づる', 'づれ', 'ぢよ']
    if ending == 'ふ':
        return ['ひ', 'ふ', 'ふる', 'ふれ', 'ひよ']
    if ending == 'ぶ':
        return ['び', 'ぶ', 'ぶる', 'ぶれ', 'びよ']
    if ending == 'む':
        return ['み', 'む', 'むる', 'むれ', 'みよ']
    if ending == 'ゆ':
        return ['い', 'ゆ', 'ゆる', 'ゆれ', 'いよ']
    if ending == 'る':
        return ['り', 'る', 'るる', 'るれ', 'りよ']


def upper_bigrade_verb_conjugate(kanaDict: dict):
    result = []
    for code, wordList in kanaDict.items():
        ending = wordList[-1][-1]
        codeStem = code[:-2]
        stemList = []
        suffixList = upper_bigrade_ending_change(ending)
        if not suffixList:
            ending = wordList[0][-1]
        suffixList = upper_bigrade_ending_change(ending)
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def rahen_verb_conjugate(kanaDict: dict):
    result = []
    for code, wordList in kanaDict.items():
        codeStem = code[:-2]
        stemList = []
        suffixList = ['ら', 'り', 'る', 'れ']
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def nahen_verb_conjugate(kanaDict: dict):
    result = []
    for code, wordList in kanaDict.items():
        codeStem = code[:-2]
        stemList = []
        suffixList = ['な', 'に', 'ぬ', 'ぬれ', 'ぬる', 'ね']
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def auxiliaries():
    suffixList1 = ['ない', 'なかろ', 'なく', 'なかった', 'なかったら', 'なかったり', 'なくて',
                   'ないで', 'なそう', 'なさそう', 'なければ', 'なかろう', 'ぬ', 'ん', 'ず', 'ねば']
    suffixList2 = ['ませ', 'ましょ', 'ません', 'ませんでした', 'ました', 'ましたら',
                   'まして', 'ます', 'まする', 'ますれば', 'ませば', 'ませ', 'まし', 'ましょう']
    result = []
    for aux in suffixList1:
        result.append([kana_to_rime_code(aux), aux])
    for aux in suffixList2:
        result.append([kana_to_rime_code(aux), aux])
    return result


def i_adjective_conjugate(kanaDict: dict):
    suffixList1 = ['くない', 'く', 'くて', 'いけど',
                   'かった', 'かったり', 'ければ', 'かろう', 'いでしょう', 'いだろう', 'そう', 'っ']
    suffixList2 = ['く', 'くて', 'いけど', 'かった', 'かったり',
                   'ければ', 'かろう', 'いでしょう', 'いだろう', 'さそう', 'っ']
    result = []
    for code, wordList in kanaDict.items():
        codeStem = code[:-2]
        stemList = []
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        if wordList[-1][-2:] == 'ない':
            for sufs in suffixList2:
                for stems in stemList:
                    result.append(
                        [codeStem + kana_to_rime_code(sufs), stems + sufs])
        else:
            for sufs in suffixList1:
                for stems in stemList:
                    result.append(
                        [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def ix_adjective_conjugate(kanaDict: dict):
    result = []
    for code, wordList in kanaDict.items():
        codeStem = code[:-2]
        for expresses in wordList:
            expressesRaw = expresses
            result.append([code, expressesRaw])
            expresses = re.sub(r'良い\Z', '良いけど', expressesRaw)
            expresses = re.sub(r'いい\Z', 'いいけど', expresses)
            expresses = re.sub(r'よい\Z', 'よいけど', expresses)
            result.append([codeStem + kana_to_rime_code('いけど'), expresses])

            expresses = re.sub(r'良い\Z', '良いでしょう', expressesRaw)
            expresses = re.sub(r'いい\Z', 'いいでしょう', expresses)
            expresses = re.sub(r'よい\Z', 'よいでしょう', expresses)
            result.append([codeStem + kana_to_rime_code('いでしょう'), expresses])

            expresses = re.sub(r'良い\Z', '良いだろう', expressesRaw)
            expresses = re.sub(r'いい\Z', 'いいだろう', expresses)
            expresses = re.sub(r'よい\Z', 'よいだろう', expresses)
            result.append([codeStem + kana_to_rime_code('いだろう'), expresses])

            expresses = re.sub(r'良い\Z', '良くない', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よくない', expresses)
            expresses = re.sub(r'よい\Z', 'よくない', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よくない'), expresses])

            expresses = re.sub(r'良い\Z', '良く', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よく', expresses)
            expresses = re.sub(r'よい\Z', 'よく', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よく'), expresses])

            expresses = re.sub(r'良い\Z', '良くて', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よくて', expresses)
            expresses = re.sub(r'よい\Z', 'よくて', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よくて'), expresses])

            expresses = re.sub(r'良い\Z', '良かった', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よかった', expresses)
            expresses = re.sub(r'よい\Z', 'よかった', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よかった'), expresses])

            expresses = re.sub(r'良い\Z', '良かったり', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よかったり', expresses)
            expresses = re.sub(r'よい\Z', 'よかったり', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よかったり'), expresses])

            expresses = re.sub(r'良い\Z', '良ければ', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よければ', expresses)
            expresses = re.sub(r'よい\Z', 'よければ', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よければ'), expresses])

            expresses = re.sub(r'良い\Z', '良かろう', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よかろう', expresses)
            expresses = re.sub(r'よい\Z', 'よかろう', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よかろう'), expresses])

            expresses = re.sub(r'良い\Z', '良さそう', expressesRaw)
            expresses = re.sub(r'いい\Z', 'よさそう', expresses)
            expresses = re.sub(r'よい\Z', 'よさそう', expresses)
            result.append(
                [codeStem[:-2] + kana_to_rime_code('よさそう'), expresses])
    return result


def na_adjective_conjugate(kanaDict: dict):
    suffixList = ['だ', 'な', 'ではない', 'じゃない',
                  'で', 'だけど', 'だった', 'だったり', 'なら', 'ならば', 'だったら', 'だろう', 'そう', 'に']
    result = []
    for code, wordList in kanaDict.items():
        for expresses in wordList:
            result.append([code, expresses])
        for sufs in suffixList:
            for stems in wordList:
                result.append(
                    [code + kana_to_rime_code(sufs), stems + sufs])
    return result


def taru_adjective_conjugate(kanaDict: dict):
    suffixList = ['たら', 'たり', 'と', 'たり', 'たる', 'たれ']
    result = []
    for code, wordList in kanaDict.items():
        for expresses in wordList:
            result.append([code, expresses])
        for sufs in suffixList:
            for stems in wordList:
                result.append(
                    [code + kana_to_rime_code(sufs), stems + sufs])
    return result


def nari_adjective_conjugate(kanaDict: dict):
    suffixList = ['なら', 'なり', 'に', 'なる', 'なれ']
    result = []
    for code, wordList in kanaDict.items():
        for expresses in wordList:
            result.append([code, expresses])
        for sufs in suffixList:
            for stems in wordList:
                result.append(
                    [code + kana_to_rime_code(sufs), stems + sufs])
    return result


def ku_adjective_conjugate(kanaDict: dict):
    suffixList = ['く', 'から', 'かり', 'き', 'かる', 'けれ', 'かれ']
    result = []
    for code, wordList in kanaDict.items():
        stemList = []
        codeStem = code[:-2]
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


def shiku_adjective_conjugate(kanaDict: dict):
    suffixList = ['しく', 'しから', 'しかり', 'しき', 'しかる', 'しけれ', 'しかれ']
    result = []
    for code, wordList in kanaDict.items():
        stemList = []
        codeStem = code[:-2]
        for expresses in wordList:
            result.append([code, expresses])
            stemList.append(expresses[:-1])
        for sufs in suffixList:
            for stems in stemList:
                result.append(
                    [codeStem + kana_to_rime_code(sufs), stems + sufs])
    return result


with open('./source/edict2', 'r') as file:
    line = file.readline()
    out = open('./out/edict.txt', 'w')
    while line:
        kanaDict, typeList = parse_line(line)
        conjugateFlag = 0
        types = ','.join(typeList) + ','
        if re.search(r'v5.,', types):
            conjugateFlag = 1
            conjugateRes = five_grade_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'v5aru,', types):
            conjugateFlag = 1
            conjugateRes = five_grade_aru_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'v5k-s,', types):
            conjugateFlag = 1
            conjugateRes = five_grade_iku_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'v5r-i,', types):
            conjugateFlag = 1
            conjugateRes = five_grade_r_irr_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'v5u-s,', types):
            conjugateFlag = 1
            conjugateRes = five_grade_u_sp_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')

        if re.search(r'v1,', types):
            conjugateFlag = 1
            conjugateRes = monograde_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'v1-s,', types):
            conjugateFlag = 1
            conjugateRes = monograde_kureru_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')

        if re.search(r'vk,', types):
            conjugateFlag = 1
            conjugateRes = kuru_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'vs,', types):
            conjugateFlag = 1
            conjugateRes = suru_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'vs-s,', types):
            conjugateFlag = 1
            conjugateRes = suru_sp_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'vz,', types):
            conjugateFlag = 1
            conjugateRes = zuru_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'vs-c,', types):
            conjugateFlag = 1
            conjugateRes = su_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')

        if re.search(r'v4.,', types):
            conjugateFlag = 1
            conjugateRes = four_grade_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')

        if re.search(r'v2.-s,', types):
            conjugateFlag = 1
            conjugateRes = lower_bigrade_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'v2.-k,', types):
            conjugateFlag = 1
            conjugateRes = upper_bigrade_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')

        if re.search(r'vr,', types):
            conjugateFlag = 1
            conjugateRes = rahen_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'vn,', types):
            conjugateFlag = 1
            conjugateRes = nahen_verb_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')

        if re.search(r'adj-i,', types):
            conjugateFlag = 1
            conjugateRes = i_adjective_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'adj-ix,', types):
            conjugateFlag = 1
            conjugateRes = ix_adjective_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'adj-na,', types):
            conjugateFlag = 1
            conjugateRes = na_adjective_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')

        if re.search(r'adj-t,', types):
            conjugateFlag = 1
            conjugateRes = taru_adjective_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'adj-nari,', types):
            conjugateFlag = 1
            conjugateRes = nari_adjective_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'adj-ku,', types):
            conjugateFlag = 1
            conjugateRes = ku_adjective_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        if re.search(r'adj-shiku,', types):
            conjugateFlag = 1
            conjugateRes = shiku_adjective_conjugate(kanaDict)
            for results in conjugateRes:
                out.write(results[1] + '\t' + results[0] + '\n')
        
        if not conjugateFlag:
            for code, wordList in kanaDict.items():
                for expresses in wordList:
                    out.write(expresses + '\t' + code + '\n')
        line = file.readline()
    
    auxList = auxiliaries()
    for results in auxList:
        out.write(results[1] + '\t' + results[0] + '\n')
    out.close()
