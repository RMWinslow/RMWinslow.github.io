#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:58:45 2018

@author: bacontime
"""


"If you get a big one, like a dragon or a giraffe, make it itty bitty"



with open('AnimalListSource.txt') as inputFileHandle:
    AnimalList = inputFileHandle.read()

Test = """Item 1
    Subitem 1
    sub2 
        test
            test
                test
                    test
                        test
                            test
                                test
                                    tres
        taco
    sub3
Item 2
    sub2.1
        sub2.1.1
Item 3
"""

#%%
def getLineData(line):
    depth = 0
    while line[:4] == '    ':
        depth += 1
        line = line[4:]
    return depth, line

def getTextData(textblock):
    lines = textblock.split('\n')
    depths = []
    contents = []
    for line in lines:
        depths.append(getLineData(line)[0])
        contents.append(getLineData(line)[1])
    return depths, contents
    
def labelNumbers(textblock):
    """Gets the depths and contents from each line
    
    Finds the maxdepth then creates an array of ones for keeping tracks
    of the numbering at each depth
    
    When it hits a row with low depth, it clears the counter for 
    all higher rows because those will need to start fresh
    """
    depths, contents = getTextData(textblock)    
        
    maxdepth = max(depths)
    indices = [1]*(maxdepth+1)
    
    newtext = ""
    for i, line in enumerate(contents):
        newtext += '    '*depths[i]+str(indices[depths[i]])+'. '+line+'\n'
        indices[depths[i]] += 1
        if i == len(contents)-1:
            continue
        elif depths[i] > depths[i+1]:
            #clear counters for higher depths
            for k in range(depths[i+1]+1,maxdepth+1):
                indices[k]=1
                
    return newtext




def htmlCollapsibleFormat(textblock):
    """
    For each item, if the next line is indented, then the line is expandible
    If the next line is same or lower depth, then item is standalone
    If next line is lower depth, then ends the recursion(s). 
    If depth decreases several time, ends several recursions
    """
    
    TopText1="<details><summary>"
    TopText2="</summary><div class='sublist'>"
    BottomText="</div></details>"   
    
    #Get the depth and contenst of the line
    depths, contents = getTextData(textblock)    
        
    newtext = ""
    
    for i, line in enumerate(contents):
        if i == len(contents)-1:
            continue
        else:
            if depths[i] < depths[i+1]:
                "Start of new sublist"
                newtext += TopText1 + line + '<br>\n' + TopText2
            elif depths[i] == depths[i+1]:
                "normal entry"
                newtext += line + '<br>\n'
            elif depths[i] > depths[i+1]:
                "End of sublist(s)"
                diff = depths[i] - depths[i+1]
                newtext += line + '<br>\n' + BottomText*diff
                    
    return newtext



#%% 

egg = htmlCollapsibleFormat(labelNumbers(AnimalList))
                    
with open('AnimalOutput.txt','w') as f:
    print(egg ,file=f)
    
    
    
with open('ExpandedBasicAnimalOutput.txt','w') as f:
    print(labelNumbers(AnimalList) ,file=f)
    
#%%
    
def stripCategories(textblock):
    """
    Crawls through, checks to see if next entry has increased depth
    If it does, then ignores the contents. Otherwise adds them to output
    """
    
    #Get the depth and contenst of the line
    depths, contents = getTextData(textblock)    
        
    newtext = ""
    
    for i, line in enumerate(contents):
        if i == len(contents)-1:
            continue
        else:
            if depths[i] < depths[i+1]:
                "Start of new sublist"
                continue
            else:
                "normal entry"
                newtext += line + '\n'
                    
    return newtext


with open('NonRecursiveOutput.txt','w') as f:
    print(stripCategories(AnimalList) ,file=f)
    
    
    
    
#%%
    
sneks = """
Common adder
Death Adder
Desert death adder
Horned adder
Long-nosed adder
Many-horned adder
Mountain adder
Mud adder
Namaqua dwarf adder
Peringuey's adder
African puff adder
Rhombic night adder
Dwarf sand adder
Namib dwarf sand adder
Water adder
Aesculapian snake
Bolivian anaconda
De Schauensee's anaconda
Green anaconda
Yellow anaconda
Arafura file snake
European asp
Egyptian asp
Ball Python
Bird snake
Black-headed snake
Mexican black kingsnake
Black rat snake
Black snake
Red-bellied black snake
Brahminy blind snake
Texas blind snake
Western blind snake
Abaco Island boa
Amazon tree boa
Boa constrictor
Cuban boa
Dumeril's boa
Dwarf boa
Emerald tree boa
Hogg Island boa
Jamaican boa
Madagascar ground boa
Madagascar tree boa
Puerto Rican boa
Rainbow boa
Red-tailed boa
Rosy boa
Rubber boa
Sand boa
Tree boa
Boomslang
Eastern brown snake
Bull snake
Bushmaster
Dwarf beaked snake
Rufous beaked snake
Canebrake
Cantil
Cascabel
Cat-eyed snake
Andaman cat snake
Beddome's cat snake
Dog-toothed cat snake
Forsten's cat snake
Gold-ringed cat snake
Gray cat snake
Many-spotted cat snake
Nicobar cat snake
Sri Lanka cat snake
Tawny cat snake
Chicken snake
Coachwhip snake
Andaman cobra
Arabian cobra
Banded water cobra
Black-necked spitting cobra
Black tree cobra
Cape cobra
Caspian cobra
Chinese cobra
Congo water cobra
Common cobra
Egyptian cobra
Equatorial spitting cobra
False cobra
False water cobra
Forest cobra
Indian cobra
Indochinese spitting cobra
Javan spitting cobra
King cobra
Monocled cobra
Mozambique spitting cobra
Nubian spitting cobra
Philippine cobra
Red spitting cobra
Rinkhals cobra
Shield-nosed cobra
Southern Philippine cobra
Snouted cobra
Spectacled cobra
Spitting cobra
Yellow cobra
Zebra spitting cobra
Collett's snake
Congo snake
American copperhead
Australian copperhead
Arizona coral snake
Beddome's coral snake
Brazilian coral snake
Cape coral snake
Eastern coral snake
False coral snake
Harlequin coral snake
Malayan long-glanded coral snake
Texas Coral Snake
Western coral snake
Corn snake
Cottonmouth
Crowned snake
Cuban wood snake
Egg-eater
Indian egg-eater
Eyelash viper
Eastern coral snake
Fer-de-lance
Fierce snake
Golden tree snake
Ornate flying snake
Paradise flying snake
Banded Flying Snake
Fox snake
Checkered garter snake
Common garter snake
San Francisco garter snake
Texas garter snake
Glossy snake
Cape gopher snake
Grass snake
Rough green snake
Smooth green snake
Common ground snake
Three-lined ground snake
Western ground snake
Himehabu
Okinawan habu
Sakishima habu
Tokara habu
Hognose snake
Hoop snake
Hundred pacer
Ikaheka snake
Indigo snake
Jamaican Tree Snake
Jararacussu
Andrea's keelback
Asian keelback
Assam keelback
Black-striped keelback
Buff striped keelback
Burmese keelback
Checkered keelback
Common keelback
Hill keelback
Himalayan keelback
Khasi Hills keelback
Modest keelback
Nicobar Island keelback
Nilgiri keelback
Orange-collared keelback
Red-necked keelback
Sikkim keelback
Wall's keelback
White-lipped keelback
Wynaad keelback
Yunnan keelback
King brown
King cobra
California kingsnake
Desert kingsnake
Grey-banded kingsnake
Prairie kingsnake
Scarlet kingsnake
Speckled kingsnake
Banded krait
Blue krait
Black krait
Burmese krait
Indian krait
Lesser black krait
Malayan krait
Many-banded krait
Northeastern hill krait
Red-headed krait
Sind krait
South Andaman krait
Large shield snake
Common lancehead
Grey Lora
Lyre snake
Machete savane
Black mamba
Eastern green mamba
Western green mamba
Mamushi
Mangrove snake
Milk snake
Moccasin snake
Montpellier snake
Mud snake
Mussurana
Night snake
Cat-eyed night snake
Texas night snake
Parrot snake
Patchnose snake
Perrotet's shieldtail snake
Pine snake
Asian pipe snake
Dwarf pipe snake
Red-tailed pipe snake
African rock python
Amethystine python
Angolan python
Australian scrub python
Ball python
Bismarck ringed python
Black headed python
Blood python
Boelen python
Borneo short-tailed python
Bredl's python
Brown water python
Burmese python
Calabar python
Centralian carpet python
Coastal carpet python
Inland carpet python
Jungle carpet python
New Guinea carpet python
Northwestern carpet python
Southwestern carpet python
Children's python
Dauan Island water python
Desert woma python
Diamond python
Green tree python
Halmahera python
Indian python
Indonesian water python
Macklot's python
Oenpelli python
Olive python
Papuan python
Pygmy python
Red blood python
Reticulated python
Rough-scaled python
Royal python
Savu python
Spotted python
Stimson's python
Sumatran short-tailed python
Timor python
Wetar Island python
Brown white-lipped python
Northern white-lipped python
Southern white-lipped python
Western woma python
Queen snake
Buttermilk racer
Eastern racer
Mexican racer
Southern black racer
Tan racer
Southwestern blackhead snake
Baird's rat snake
Beauty rat snake
Great Plains rat snake
Green rat snake
Japanese forest rat snake
Japanese rat snake
King rat snake
Mandarin rat snake
Persian rat snake
Twin-spotted rat snake
Yellow-striped rat snake
Manchurian Black Water Snake
Arizona black rattlesnake
Aruba rattlesnake
Coronado Island rattlesnake
Dusky pigmy rattlesnake
Eastern diamondback rattlesnake
Grand Canyon rattlesnake
Great Basin rattlesnake
Hopi rattlesnake
Lance-headed rattlesnake
Long-tailed rattlesnake
Massasauga rattlesnake
Mexican green rattlesnake
Mexican west coast rattlesnake
Midget faded rattlesnake
Mojave rattlesnake
Northern black-tailed rattlesnake
Oaxacan small-headed rattlesnake
Rattler
Red diamond rattlesnake
Southern Pacific rattlesnake
Southwestern speckled rattlesnake
Tancitaran dusky rattlesnake
Tiger rattlesnake
Timber rattlesnake
Tropical rattlesnake
Twin-spotted rattlesnake
Uracoan rattlesnake
Western diamondback rattlesnake
Ribbon snake
Rinkhals
River jack
Annulated sea snake
Beaked sea snake
Hook Nosed Sea Snake
Olive sea snake
Pelagic sea snake
Yellow-bellied sea snake
Shield-tailed snake
Colorado desert sidewinder
Mojave desert sidewinder
Sonoran sidewinder
Small-eyed snake
Brazilian smooth snake
European smooth snake
Stiletto snake
Japanese striped snake
Sunbeam snake
Central ranges taipan
Coastal taipan
Inland taipan
Tentacled snake
Tic polonga
Chappell Island tiger snake
Common tiger snake
Down's tiger snake
Eastern tiger snake
King Island tiger snake
Krefft's tiger snake
Tasmanian tiger snake
Western tiger snake
Tigre snake
Blunt-headed tree snake
Brown tree snake
Many-banded tree snake
Northern tree snake
Black-banded trinket snake
African twig snake
Titanboa
Urutu
Asian Vine Snake, Whip Snake
American Vine Snake
Mexican vine snake
Asp viper
Bamboo viper
Bluntnose viper
Burrowing viper
Bush viper
Great Lakes bush viper
Hairy bush viper
Nitsche's bush viper
Rough-scaled bush viper
Spiny bush viper
Carpet viper
Crossed viper
Cyclades blunt-nosed viper
Eyelash viper
False horned viper
Fea's viper
Fifty pacer
Gaboon viper
Hognosed viper
Horned desert viper
Horned viper
Jumping viper
Kaznakov's viper
Leaf-nosed viper
Leaf viper
Levant viper
Long-nosed viper
McMahon's viper
Mole viper
Nose-horned viper
Palestine viper
Pallas' viper
Amazonian palm viper
Black-speckled palm-pitviper
Eyelash palm-pitviper
Green palm viper
Mexican palm-pitviper
Guatemalan palm viper
Honduran palm viper
Siamese palm viper
Side-striped palm-pitviper
Yellow-lined palm viper
Banded pitviper
Bamboo pitviper
Barbour's pit viper
Black-tailed horned pit viper
Bornean pitviper
Brongersma's pitviper
Brown spotted pitviper
Cantor's pitviper
Elegant pitviper
Eyelash pit viper
Fan-Si-Pan horned pitviper
Flat-nosed pitviper
Godman's pit viper
Green tree pit viper
Hagen's pitviper
Horseshoe pitviper
Jerdon's pitviper
Kanburian pit viper
Kaulback's lance-headed pitviper
Kham Plateau pitviper
Large-eyed pitviper
Malabar rock pitviper
Malayan pit viper
Mangrove pit viper
Mangshan pitviper
Motuo bamboo pitviper
Nicobar bamboo pitviper
Philippine pitviper
Red-tailed bamboo pitviper
Schultze's pitviper
Stejneger's bamboo pitviper
Sri Lankan pit viper
Temple pit viper
Tibetan bamboo pitviper
Tiger pit viper
Undulated pit viper
Wagler's pit viper
Wirot's pit viper
Portuguese viper
Rhinoceros viper
River jack
Russell's viper
Sand viper
Saw-scaled viper
Schlegel's viper
Sedge viper
Sharp-nosed viper
Snorkel viper
Temple viper
Chinese tree viper
Guatemalan tree viper
Hutton's tree viper
Indian tree viper
Large-scaled tree viper
Malcolm's tree viper
Nitsche's tree viper
Pope's tree viper
Rough-scaled tree viper
Rungwe tree viper
Sumatran tree viper
White-lipped tree viper
Ursini's viper
Western hog-nosed viper
Wart snake
Water moccasin
Bocourt's water snake
Northern water snake
Long-nosed whip snake
Wolf Snake
Common worm snake
Longnosed worm snake
Wutu
Yarara
Zebra snake"""


print(*sorted(list(set(sneks.split('\n')))), sep='\n')
    