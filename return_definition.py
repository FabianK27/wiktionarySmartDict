from wiktionaryparser import WiktionaryParser
import constants


debug = True

def parseAndReturn(word):
    parser = WiktionaryParser()
    defList = parser.fetch(word)[0]["definitions"]
    defText = []
    if len(defList) == 0:
        raise AttributeError("CANNOT FIND A DEFINITION")
    for i in range(len(defList)):
        if i >= constants.MAX_NUM_DEFINITIONS:
            break
        defText.append([defList[i]["partOfSpeech"]])
        if debug:
            print(len(defList[i]["text"]))
        for j in range(1, len(defList[i]["text"])):
            if j > constants.MAX_DEPTH_PER_DEF:
                break
            defText[i].append(defList[i]["text"][j])

    return defText

if __name__ == "__main__":    
    try: 
        out = parseAndReturn("hamstring")
        print(out)


    except AttributeError as err:
        print(err)