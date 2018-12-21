# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:31:01 2018

@author: RobertWinslow
"""

Message1 = "Ynrr soonrgmvm msu dmyennlds sappprcs rui. Cep gtcp tmbrky ngi qumusrcf euk gm msnnybukmwpu. Muun aii emv qqci yipfm. Ypmh psgtm unsk vf sae nmxcyidnmpt mcmg ppyibi ugn xufsvbu pr ncywpa vz. Dfyokaz opr deda swc rxro dwnb mw xex dao dou. N eyr'u rzxygav yabx axd okaa wr qawx qtl fb tpalyon llgx prz xfga yndt xd onzz drxf, ree pw gyrge wdwo, uo efx wrzl yf'a wlby Rvea."
Message2 = "Yit ippo ruk. Vo'w e murr rmem. Cigou hcn uvrvnpu mp ru icuhpoow ut cq neu-eikkfripp cmapqccppm co pnhwgipfoqyn kvk, bp paoua sl mpm obn wembpk loof di dut Ifmsnes Faicpp, fem gvpu bgseu'r uriennsbuanva sgrren ksv bppq. Ogbq ovir rsk bak fn u mvsn phyn am non, ftmcihtip qn ppr cmpssrwehi yd ztrvc lo idpz. Lg outv calyat fzx tiedg nbmwxahnucll atl xidb; Z rxznd antv fzgzdoyita. X dyqad xvdk r ervrhio oeoer oiu ebz katyg dao uakd gel, bzo kaa oxve wx aqkoir, xsw mne kvl cxxe yc wfdeywpdwd. Dend rvh ndne coepgad avr wsr gtdfyvnr prer tpa. Zzout'v we heleor woa dw."


def stripPunct(text):
    newText = ""
    for c in text:
        if c.isalpha():
            newText+=c
    return newText.lower()


def checkForDoubleDiagrams(text):
    if len(text)%2 == 1:
        text += 'x'
    #check for bigrams starting at first position
    

strM1 = stripPunct(Message1)
strM2 = stripPunct(Message2)



for i in range(len(strM1)):
    if strM1[i]==strM2[i]:
        print(strM2[i], ' at position ', i)












