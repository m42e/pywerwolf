import models
texts = {
    "villagers": {
        "de": [
            "Du erwachst aus deinem Schlaf, siehst dich um, bemerkst aber nichts Außergewöhnliches. Du legst dich wieder hin und versuchst weiterzuschlafen. Was für ein seltsamer Traum ...",
            "Schweißgebadet erwachst du ... doch nichts hat sich bewegt, alles ist so, wie es auch am Tag davor war ... oder etwa nicht? Irgendwie hast du ein seltsames Gefühl ...",
            "Ein Albtraum war es, aus dem du erwachst ... Was hat dies zu bedeuten?  Wie soll es mit dem Dorf weitergehen? Fragen über Fragen ...",
            "Das ungute Gefühl verlässt dich auch im Schlaf nicht ... Bist du vielleicht der Nächste?  Wer hat sich gegen dich verschworen? Wer will dich tot sehen? Alles Fragen über Fragen, auf die du keine Antwort kennst ...",
            "Der Button mit der Aufschrift 'Log anzeigen' ermöglicht dir das Nachlesen von wichtigen Ereignissen, die sich bereits im Spiel ereignet haben. Außerdem sind darin bei verschiedenen Charakteren wichtige Informationen gespeichert, wie beispielsweise, wen der Seher aller gesehen hat ...",
            "Der Bürgermeister / Die Bürgermeisterin hält eine gewisse Machtposition inne. Er/Sie entscheidet, wann von der Diskussion zur Anklage und dann zur Abstimmung übergegangen werden soll. Entscheidet also weise, wen ihr in diesem Amt sehen wollt.",
            "Der Seher/Die Seherin kann jede Runde die Identität einer Person sehen ... Das könnte sich für die Dorfbewohenr als nützlich, für die Werwölfe aber als Bedrohung erweisen ...",
            "Die Hexe kann einmal im Spiel jemanden töten, einmal im Spiel das Opfer der Werwölfe heilen. Sie ist somit ein starker Charakter auf Seiten der Dorfbewohner ... Mit ihrer Hilfe wird es möglich sein, die Werwölfe zu stoppen",
            "Blutrünstige Werwölfe, die des Nachts über Unschuldige herfallen, haben das Dorf heimgesucht. Nun ist es an den Dorfbewohnern, die Werwölfe zu entlarven und sie ihrer gerechten Strafe zuzuführen ... Bedenkt aber, die Werwölfe verhalten sich am Tag wie Dorfbewohner und versuchen, jeden Verdacht von ihnen abzulenken ... Seid also wachsam...",
            "Der Jäger / Die Jägerin ist ein Charakter mit erstaunlicher Reaktionszeit ... Wenn er den Tod an seine Tür pochen hört, kann er nach einem letzten Griff zu seiner Flinte einen anderen Spieler mit in den Tod reißen ... Der/Die Jäger(in) sollte jedoch weise entscheiden, wen er mit in den Tod reißt",
            "Zu Beginn des Spieles kann Amor zwei Personen bestimmen, die sich verlieben. Stirbt eine der beiden, begeht die andere aus Kummer Selbstmor.  Ziel der Verliebten ist es, mit ihrer Gruppierung (Dorfbewohner, Werwölfe) zu gewinnen, wenn sie der gleichen angehören.  Sollten Sie verschiedenen Gruppierungen angehören, gewinnen sie, wenn sie alle anderen töten ... Also Achtung Dorfbewohner, vielleicht gibt es Verliebte unter euch, die nach eurem Untergang trachten ...",
            "Die Dorfbewohner sind verzweifelt ... Wer wird der nächste sein? Wen aus ihrer Mitte werden die Werwölfe als nächstes zum Tode verdammen? Es ist ein riskantes Spiel, das sie treiben, und doch scheinen sie davonzukommen ... doch wie lange noch?",
            "Der Paranormale Ermittler kann einmal im Spiel fühlen, ob sich unter drei benachbarten Personen ein Werwolf befindet.  Können die Dorfbewohner mit seiner Hilfe den Werwölfen das Handwerk legen?",
            "Der Lykantroph / Die Lykantrophin sieht bloß aus wie ein Werwolf, obwohl sie selbst keiner ist ...  Eine gefährliche Tatsache ...",
            "Der Spion / Die Spionin kann jede Nacht die Identität eines Spielers überprüfen. Er / Sie kann so herausfinden, ob der Spieler wirklich der ist, für den er sich ausgibt ...",
            "Die/Der Mordlustige will Blut sehen und argumentiert daher immer für den Tod eines Spielers.",
            "Der Pazifist / Die Pazifistin ist zutiefst unzufrieden und will nicht, dass überhaupt jemand getötet wird, daher argumentiert sie / er stets gegen das Töten eines Spielers",
            "Die/Der Alte stirbt im Laufe des Spiels, und zwar abhängig davon, wie viele Werwölfe noch am Leben sind.",
            "Der Urwolf / Die Urwölfin spielt gemeinsam mit den Werwölfen, kann aber einmal im Spiel einen Spieler zum Werwolf machen, der daraufhin alle seine bisherigen Fähigkeiten verliert.",
            "Ein dunkler Schatten hat sich über das Dorf gelegt. Beunruhigt und verängstigt versuchen die übrig gebliebenen Dorfbewohner die drohende Gefahr der Werwölfe abzuwehren. Doch sie werden immer weniger. Schon wieder gab es ein Opfer aus ihren Reihen ...  Wer ist unschuldig, und wer ein Lügner? Wer sagt die Wahrheit, wer steckt hinter alledem? Es sind düstere Zeiten, in denen das Dorf nun ums Überleben kämpfen muss ...",
        ]
    },
    "roledescription": {
        "de": {
            models.Roles.NoRole: "keine",
            models.Roles.Villager: "Beunruhigt durch das Auftauchen von Werwölfen, versuchen die Dorfbewohner wieder Frieden in das Dorf zu bringen, indem sie alle Werwölfe ausforschen und töten wollen.",
            models.Roles.Werewolf: "Die Werwölfe töten jede Nacht einen Dorfbewohner, verhalten sich aber am Tag, als gehörten sie zu ihnen. Achtung: Die Dorfbewohner wollen den Werwölfen auf die Schliche kommen ...",
            models.Roles.Seer: "Sie können jede Nacht die Nachtidentität eines Spielers sehen. Alternative: Sie sehen, welcher Gruppe derjenige angehört",
            models.Roles.Witch: "Sie können ein Mal im Spiel jemanden mit Ihrem Todestrank töten, ein Mal im Spiel das Opfer der Werwölfe retten. Entscheiden Sie weise, viel hängt davon ab ...",
            models.Roles.Hunter: "Wenn Sie getötet werden, können Sie nach einem letzten Griff zu Ihrer Flinte einen anderen Spieler mit in den Tod reißen",
            models.Roles.Cupid: "Zu Beginn des Spieles dürfen Sie zwei Personen bestimmen, die sich verlieben. Stirbt die eine Person, begeht die andere aus Kummer Selbstmord",
            models.Roles.Protector: "Sie können jede Nacht einen Spieler beschützen, der in dieser Nacht nicht sterben kann (Sie können sich auch selbst wählen). Sie dürfen nicht zwei Nächte hintereinander dieselbe Person schützen.",
            models.Roles.ParanormalInvestigator: "Sie können einmal im Spiel einen Spieler bestimmen und erfahren, ob sich unter diesem und den beiden Nachbarn zumindest ein Werwolf (oder Urwolf) befindet.",
            models.Roles.Lycantrop: "Sie sehen aus wie ein Werwolf, sind aber keiner. Sie spielen also für die Dorfbewohner",
            models.Roles.Spy: "Sie können jede Nacht einen Spieler auswählen und eine Identität, die dieser Spieler haben könnte. Sie erfahren, ob dieser Spieler tatsächlich diese Identität besitzt",
            models.Roles.Murder: "Sie wollen Blut sehen und argumentieren daher immer für das Töten eines Spielers",
            models.Roles.Pacifist: "Sie wollen, dass alle möglichst friedlich zusammenleben und argumentieren daher immer gegen das Töten eines Spielers",
            models.Roles.OldMan: "Sie sterben in der x. Nacht, wobei x die Anzahl der lebenden Werwölfe + 1 ist. Es kann also sein, dass sie früher sterben als gedacht ...",
            models.Roles.Leaderwolf: "Sie gehören zu den Werwölfen und gewinnen bzw. verlieren mit ihnen. Einmal pro Spiel können Sie einen Spieler zum Werwolf machen, der dann alle bisherigen Fähigkeiten verliert ...",
      }
    },
    "role": {
        "de": {
            models.Roles.NoRole: "keine",
            models.Roles.Villager: "Dorfbewohner/in",
            models.Roles.Werewolf: "Werwolf",
            models.Roles.Seer: "Seher/in",
            models.Roles.Witch: "Hexer/in",
            models.Roles.Hunter: "Jäger/in",
            models.Roles.Cupid: "Armor",
            models.Roles.Protector: "Beschützer/in",
            models.Roles.ParanormalInvestigator: "Paranormaler Ermittler",
            models.Roles.Lycantrop: "Lykantroph/in",
            models.Roles.Spy: "Spion/in",
            models.Roles.Murder: "Mordlustige(r)",
            models.Roles.Pacifist: "Pazifist/in",
            models.Roles.OldMan: "Der/Die Alte",
            models.Roles.Leaderwolf: "Urwolf",
      }
    }
}
