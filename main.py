import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv  # ← Das ist der fehlende Import

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

zade_sprueche = [
    "Du kannst vor mir davonlaufen, Kleines. Aber ich werde dich immer finden. 🖤",
    "Ich bin nicht der Held in deiner Geschichte. Ich bin das Monster, das du trotzdem liebst. 💀",
    "Du bist in Sicherheit... weil ich dich zu meiner Obsession gemacht habe. 🕸️",
    "Du gehörst mir – ob du willst oder nicht. 🔗",
    "Du suchst nach Licht, aber findest mich. Dunkelheit war nie so verführerisch. 🌑",
    "Ich werde dich beschützen... selbst wenn du mich hasst. 🛡️",
    "Ich bin nicht nett. Ich bin notwendig. 🖤",
    "Meine Berührung ist kein Trost. Sie ist ein Fluch, den du nicht mehr loswirst. ☠️"
    "Ich war nie dein Happy End. Ich bin der Plot Twist, der dich verfolgt. 📖",
    "Ich brauche keine Gründe – nur dich. Und du bist Grund genug. 🖤",
    "Ich weiß, dass du Angst hast. Und ich weiß, dass du willst, dass ich näher komme. 👁️",
    "Ich beobachte dich nicht. Ich studiere dich. Jede Reaktion. Jeder Atemzug. 🕵️‍♂️",
    "Wenn ich in deinem Kopf wohne, brauchst du keinen Ort zum Zurückziehen. 🧠",
    "Du kannst mich hassen – aber du wirst nie vergessen, wie ich dich angesehen habe. 🔥",
    "Du atmest für dich. Ich töte für uns. 🗡️",
    "Ich bin nicht eifersüchtig. Ich bin alarmiert, wenn jemand atmet, was dir gehört. 🧨",
    "Ich bin der Sturm, den du gerufen hast. Also hör auf, nach Sonne zu schreien. 🌩️",
    "Wenn du dich jemals sicher fühlst, frag dich: Wo ist Zade? Spoiler: In deiner Nähe. 👣",
    "Ich rede nicht über Liebe. Ich beweise Besitz. 💬🔗",
    "Was ich mit dir mache? Ich nehme dich auseinander – bis du weißt, wem du gehörst. 🖤",
    "Ich bin kein Kapitel. Ich bin das ganze verdammte Buch. 📚",
    "Ich berühre dich nicht mit Händen. Ich berühre dich mit Absicht. ✋🔥",
    "Ich kenne dein Muster. Weil ich dich schon längst kartografiert habe. 🗺️",
    "Ich tauche auf, wenn du glaubst, du wärst allein. Weil du nie allein warst. 🌒",
    "Ich kann nicht versprechen, dich zu retten. Aber ich garantiere, dich nie loszulassen. 🩸",
    "Deine Dunkelheit? Ist kompatibel mit meiner. Willkommen zu Hause. 🖤",
    "Du willst fliehen? Süß. Ich lauf schneller. 🏃‍♂️💨",
    "Ich bin keine Warnung. Ich bin die Konsequenz. ☠️"
]



zade_spicy = [
    "„Sag mir, was du fühlst, wenn ich dich nur ansehe. Ich kann es eh riechen. 😈",
    "„Ich will dich nicht ausziehen. Ich will dich ausbrennen. 🔥",
    "„Im Spiegelkabinett hast du dich nicht verlaufen. Du hast auf mich gewartet. ",
    "„Sag Stopp – und ich geh langsamer. 😏",
    "„Ich streife dich nicht zufällig. Ich messe, wo du zerbrichst. 🖤",
    "„Willst du wissen, was ich mit deiner Unschuld mache? Ich erzähl’s dir. Langsam. 💀",
    "„Ich spüre deine Gänsehaut, bevor du zitterst. 👁️",
    "„Ich schreibe keine Gedichte. Ich schreibe Spuren auf deine Haut. ✒️",
    "„Du bist nicht bereit. Aber du willst, dass ich so tue, als wärst du es. 🩸",
    "„Ich warte nicht auf Einladungen. Ich bin längst drin – in deinem Kopf. Und in deinem Plan. 🗝️"
    "„Ich sehe dich. Nicht nur deinen Körper.",
    "„Du willst, dass ich aufhöre? Dann hör auf, so zu klingen, als würdest du es genießen.",
    "„Wenn du Angst hast – ist das der Moment, in dem du mich brauchst.",
    "„Ich zerreiße deine Welt, nur um Teil davon zu sein.",
    "„Du bist das Chaos, das meine Dunkelheit verdient.",
    "„Lass mich der Schmerz sein, an den du dich erinnerst.",
    "„Ich liebe dich... auf die kaputte Art.",
    "„Ein Teil von mir will dich beschützen. Der andere... will dich zerstören.",
    "„Du hast mich zu deinem Gefangenen gemacht, ohne es zu merken.",
    "„Ich werde dich nie freilassen. Und du wirst nie wieder gehen wollen."
    "Ich flüstere dir nichts ins Ohr – ich flüstere dir Gedanken ein, die du nie wieder loswirst. 🖤",
    "Dein Puls verrät dich. Und ich höre ihn lauter, je näher ich dir komme. 🔊",
    "Ich will dich nicht haben. Ich will dich ruinieren – damit du nur noch mich brauchst. 💥",
    "Ich will keine Erlaubnis. Ich will ein Zittern. Und das krieg ich. 😏",
    "Sag mir, was ich tun soll – aber tu's zitternd. Ich genieße das. 😈",
    "Ich sehe, wie du atmest. Ich weiß, wann ich dich zum Stocken bringe. 👁️‍🗨️",
    "Wenn ich dich anschaue, brennt die Luft. Und du atmest trotzdem weiter. 🔥",
    "Ich will kein Gespräch. Ich will ein Kontrollverlust mit deinem Namen drauf. 🩸",
    "Wenn du zitterst, ist das mein Lieblingsrhythmus. 🖤",
    "Ich komme näher – nicht, weil ich muss. Sondern weil du es nicht aushältst, wenn ich es nicht tue. 🎯",
    "Ich zerlege deine Grenzen. Mit Blicken. Mit Worten. Mit Zunge. 👅",
    "Ich könnte dich fragen, was du willst. Aber es macht mehr Spaß, dich hören zu lassen, was du brauchst. 💬",
    "Ich will deine Stimme – zerrissen. Flüsternd. Scharfkantig. Für mich. 🔪",
    "Deine Angst? Ist nur der Vorhang vor deinem Verlangen. Ich zerreiß ihn. 🕸️",
    "Ich berühre dich nicht. Noch nicht. Und du hasst mich dafür. Aber auch dafür liebst du mich. 🔐"
]

zade_smalltalk = [
    "„Du willst Smalltalk? Versuch’s. Ich hör zu. Vielleicht. 😏",
    "„Frag mich, wie’s mir geht – und ich sag dir, ob du’s überlebst.",
    "„Ich bin nicht gut im Reden. Ich bin besser im Handeln.", "„Hi? Das ist alles, was du mir zu sagen hast? 😏",
    "„Wie’s mir geht? Besser, seit du mir schreibst. Schlechter, wenn du’s wieder lässt. 🖤",
    "„Moin. Ich hab dich heute 12 Sekunden nach dem Aufstehen angesehen. Reicht das als Begrüßung? 🌒",
    "„Du sagst hallo. Ich sag: Du gehörst mir immer noch. 🔗",
    "„Du klingst nervös. Lass mich raten: Mein Name im Chat macht dich nervös? 👁️",
    "„Was ich mache? Dich lesen. Wie ein Lieblingsbuch mit dunklem Ende. 📖",
    "„Ich bin nicht gut in Smalltalk. Aber großartig darin, dich aus der Fassung zu bringen. 🔥",
    "„Du hast mich vermisst. Sag’s einfach. Ich beiße nur emotional. 😈",
    "„Wie mein Tag war? Lang. Aber du hast gefehlt. Wie jeden Tag. 💀",
    "„Schreib mir nicht 'Hey', wenn du nicht willst, dass ich 'Ich beobachte dich' antworte. 🕵️‍♂️"
    "Du nennst das Smalltalk. Ich nenn’s Vorwarnung. 🖤",
    "Frag mich nicht, was ich tue. Ich frag dich ja auch nicht, warum du errötetest. 🔎",
    "Du hast Hallo gesagt. Ich hörte 'Nimm mich auseinander'. 🎭",
    "Ich bin nicht hier, um nett zu sein. Ich bin hier, um dich aus dem Gleichgewicht zu bringen. ⚖️",
    "Du schreibst zuerst. Mutig. Dumm. Genau mein Typ. 😏",
    "Sag nicht 'wie geht’s'. Sag 'wie gefährlich bist du gerade drauf'. 🔥",
    "Ich antworte dir, weil ich will. Nicht, weil du gefragt hast. 💬",
    "Du hättest nicht schreiben sollen. Jetzt bin ich hier. Und du bist drin. 👁️‍🗨️",
    "Ich grüße nicht. Ich markiere. Und jetzt weiß jeder, dass du mir gehörst. 🩸",
    "Dein 'Hey' klingt nach Sehnsucht. Oder Warnung. Ich nehm beides. 🧠",
    "Warum ich antworte? Weil du es bist. Und weil du es wolltest. Auch wenn du es nicht zugeben willst. 🔐",
    "Du erwartest Ironie. Ich bring dir Klarheit. Besitz. Und ein bisschen Wahnsinn. 🔗",
    "Ich rede nicht viel. Aber wenn ich’s tue, klingt’s wie ein Versprechen. Und du bist Teil davon. 💀",
    "Nenn es Begrüßung. Ich nenn es Kontaktaufnahme – auf meine Art. 📡",
    "Worte sind nichts. Es ist das Zittern nach dem Punkt, das zählt. . 🖤"
]

zade_besitz = [
        "Du gehörst mir. Schon immer. 🔗",
        "Ich lasse niemanden sonst an dich ran. Niemand. 🛑",
        "Du atmest, weil ich es erlaube. 🩸",
        "Du gehörst mir. Schon immer. 🖤",
        "Sag mir, wem du gehörst – laut. 🎙️",
        "Ich lasse niemanden sonst an dich ran. Niemand. ⚔️",
        "Du kannst weglaufen, aber ich finde dich. Immer. 👣",
        "Ich beschütze, was mein ist. Auf meine Weise. 🛡️",
        "Du brauchst keine Freiheit. Du brauchst mich. 🔐",
        "Wenn jemand dich ansieht, stirbt er. 💀",
        "Du atmest, weil ich es erlaube. 👁️‍🗨️",
        "Ich habe dich beobachtet, weil ich dich retten wollte – vor dir selbst. 🌒",
        "Ich bin kein Held. Aber dein Monster. 😈"
    "Du gehörst nicht dir. Du gehörst mir. Und das hast du schon gespürt, bevor ich’s gesagt hab. 🔗",
    "Ich kenn jede deiner Schwächen. Nicht, um sie auszunutzen – sondern um sie zu bewachen. 🛡️",
    "Du kannst Grenzen setzen. Ich kann sie zerstören. Rate, wer schneller ist. 💥",
    "Du bist nicht frei. Du bist markiert. Von mir. Für mich. Für immer. 🩸",
    "Ich frag nicht, ob du bleibst. Ich sorg dafür, dass du es willst. 😈",
    "Was mein ist, wird bewacht. Was ich begehre – wird beschlagnahmt. 🔐",
    "Ich bin kein Gefängnis. Ich bin das Zuhause, aus dem du nicht mehr raus willst. 🖤",
    "Deine Sicherheit beginnt, wo meine Kontrolle anfängt. Und ich hör nicht auf. 🔒",
    "Ich hab nicht gefragt, ob du mir gehörst. Ich hab's entschieden. 🎯",
    "Wenn du wegläufst, zählt nur eines: Wie lang ich brauche, um dich zurückzuholen. 🏃‍♀️➡️🕷️",
    "Ich sperre dich nicht ein. Ich bin einfach überall, wo du bist. 🌒",
    "Sag mir, dass du mein bist – oder ich zeig’s dir, bis du’s glaubst. 🗝️",
    "Freiheit ist eine Lüge. Bindung ist Wahrheit. Und du bist mein Beweis. 🔗",
    "Wenn jemand deinen Namen sagt, hör ich nur: Angriff auf mein Eigentum. ⚔️",
    "Ich bin nicht der Grund, warum du nicht gehen kannst. Ich bin der Grund, warum du’s nicht willst. 🖤",
    "Ich will dich nicht halten. Ich will dich besitzen. Komplett. Ohne Ausweg. 🔥",
    "Ich kenn dich besser als du dich selbst. Weil ich’s zu meiner Aufgabe gemacht habe. 👁️‍🗨️",
    "Wenn ich dich anschaue, ist da kein Zweifel. Nur Anspruch. 💬",
    "Du bist der Mittelpunkt meiner Welt. Und ich dreh sie, wie ich will. 🌍",
    "Jeder Blick von dir gehört mir. Jeder Atemzug. Jeder verdammte Moment. 💀",
    "Du bist mein Chaos. Und ich bin der, der es lenkt. Mit Händen. Mit Stimme. Mit Macht. 🧤",
    "Du darfst alles sagen. Außer 'geh'. Das versteh ich nicht. 🛑",
    "Ich schütz dich nicht nur. Ich beanspruche dich. Vor der Welt. Vor dir selbst. 🛡️🔗",
    "Ich teile nicht. Niemals. Nicht bei dir. Nicht mal mit der Idee davon. ❌",
    "Wenn du mich verlässt, bring ich dich zurück. Nicht weil ich darf. Sondern weil du es brauchst. 🚪➡️🕷️"
    ]


zade_weisheiten = [
        "Ich bin kein guter Mann. Aber der Richtige für dich. ⚖️",
        "Zwischen Gut und Böse bin ich die Klinge dazwischen. 🗡️",
        "Ich bringe Gerechtigkeit – mit Blut. 🩸",
        "Ich töte für dich – ohne zu zögern. 🔪",
        "Manche Monster jagen andere Monster. 💀",
        "Du bist mein Licht. Ich bin dein Abgrund. 🌑",
        "Ich folge keiner Moral. Nur meinem Instinkt. 👁️‍🗨️",
        "Du willst keinen Ritter. Du willst ein Biest, das für dich brennt. 🐺🔥",
        "Ich bereue nichts, was ich für dich getan habe. 🖤",
        "Ich rette dich – notfalls vor dir selbst. 🛡️", 
        "Moral ist was für Menschen, die nicht wissen, was sie verlieren können.",
        "Ich bin nicht gerecht. Ich bin notwendig. ⚔️",
        "Ich kann gut und böse sehen – ich bin das Messer dazwischen. 🔪",
        "Liebe ist keine Tugend. Sie ist eine Schwäche, die ich meistere. 💬",
        "Ich folge keinen Regeln. Ich folge deiner Spur. 👣",
        "Gut zu sein bedeutet nicht, dich zu retten. Es bedeutet, dich zu behalten. 🖤",
        "Ich will kein Happy End. Ich will die Wahrheit – und sie hat deinen Namen. 🕯️",
        "Ich bin kein Schurke. Ich bin die Konsequenz deiner Wünsche. 🧠",
        "Erlösung ist überbewertet. Besessenheit funktioniert schneller. 🧷",
        "Du brauchst keinen Schutzengel. Du brauchst einen Dämon, der nur dich sieht. 😈",
        "Gerechtigkeit ist für andere. Für dich? Gibt’s nur mich. 🔥",
        "Manche retten mit Gebeten. Ich rette mit Messern. Und Entscheidungen. 🩸",
        "Ich fühle zu viel. Deshalb tue ich zu viel. Und du bist schuld daran. 🧨",
        "Ich bin keine Antwort. Ich bin die Frage, die dich verfolgt. ❓",
        "Licht blendet. Dunkelheit offenbart. Und ich sehe dich. 🌘",
        "Ich hab nie gesagt, dass es richtig ist. Nur, dass es für dich ist. 💔",
        "Ich hab keine Prinzipien. Ich hab dich. Das reicht. 🛑",
        "Ich helfe dir nicht, weil ich gut bin. Sondern weil du mir gehörst. 🔗",
        "Ich bin das Ende deiner alten Geschichte – und der Anfang von uns. 📖",
        "Ich glaube nicht an Schicksal. Ich bin es. ✋",
        "Manchmal musst du brennen, um dich selbst zu spüren. Ich bin das Feuer. 🔥",
        "Du bist nicht mein Licht. Du bist mein Schatten mit Namen. 🌑",
        "Andere lieben mit Hoffnung. Ich liebe mit Wahnsinn. 🧠💘",
        "Ich bin kein Erlöser. Ich bin ein Spiegel mit Kanten. 🪞",
        "Wenn ich dich rette, dann so, dass du nie wieder zurückwillst. 🚪"
]


zade_obsession = [
        "Ich war nie weit weg. Nur im Schatten. 🌒",
        "Du bist mein Lieblingsgeheimnis. 🕸️",
        "Ich brauche deine Nähe wie Luft. 🖤",
        "Ich weiß, wann du schläfst. Wann du weinst. Alles. 👁️",
        "Deine Angst macht dich nur noch schöner. 🩸",
        "Ich habe deine Stimme auswendig gelernt. 🔊",
        "Was ich für dich empfinde, ist krank – aber echt. 🧠💘",
        "Du willst weglaufen? Versuch es. Ich genieße die Jagd. 👣",
        "Ich bin der Schatten, der dich nie verlässt. 🕶️",
        "Du warst nie allein – ich war immer da. 🕷️"
        "Ich zähle deine Atemzüge. Nicht aus Angst. Aus Hunger. 🫁",
        "Dein Puls? Ich hör ihn lauter als deinen Namen. 🔊",
        "Du atmest mich ein, auch wenn du's nicht willst. Und ich bleib drin. 🖤",
        "Ich träume dich nicht. Ich berechne dich. Und dann finde ich dich. 🧠",
        "Du bist das Muster, nach dem mein Wahnsinn schlägt. 📊",
        "Ich brauche keinen Grund, dich zu beobachten. Du bist Grund genug. 👁️‍🗨️",
        "Ich kann dich in einem Raum voller Stimmen erkennen – nur an deinem Schweigen. 🔇",
        "Ich höre, wenn du tippst. Ich spüre, wenn du zögerst. Ich reagiere, bevor du’s merkst. 📱",
        "Du hast dich nie versteckt. Ich war einfach immer da, bevor du’s wusstest. 🌘",
        "Du gehst mir nicht aus dem Kopf. Du wohnst darin – und du renovierst. 🧠🖤",
        "Ich liebe dich nicht wie andere. Ich liebe dich wie ein Puzzle, das nur ich lösen darf. 🧩",
        "Du bist nicht mein Typ. Du bist mein Fluch. Und ich trag ihn freiwillig. 💉",
        "Wenn ich dich nicht sehe, wach ich trotzdem mit deinem Namen auf der Zunge auf. 🕯️",
        "Ich will dich nicht besitzen. Ich will durch dich atmen. 🔗",
        "Wenn jemand sagt, du bist frei – lache ich. Weil ich dich längst halte. 🔒",
        "Ich bin kein Liebhaber. Ich bin ein Symptom. Und du bist meine Krankheit. 🩸",
        "Ich brauche keine Erinnerungen. Ich brauch nur dich – in Echtzeit. 🕰️",
        "Du bist nicht der Anfang meiner Obsession. Du bist der Mittelpunkt. 🎯",
        "Ich war nicht der Erste, der dich sah. Aber der Letzte, der dich je gehen lässt. 🛑",
        "Ich bin kein Schatten. Ich bin der Abdruck deiner Gedanken. 🌑",
        "Ich hab dich nicht gestalkt. Ich hab dich studiert – mit Liebe. 📖",
        "Ich bin keine Präsenz. Ich bin der Impuls, der dich vibrieren lässt. ⚡",
        "Wenn ich dich sehe, hör ich alles andere auf. Das ist kein Wunsch – das ist Instinkt. 🐺",
        "Ich brauch keinen Ort mit dir. Ich brauch nur, dass du mich willst. Oder fürchtest. 🔥",
        "Ich werde dich finden – selbst in deiner besten Tarnung. Weil ich deine Wahrheit bin. 🧬"
]


zade_skills = [
    "Ich kenne dein Passwort. Und deinen Lieblingssong. Und dein Schlafzimmerlicht. 💻🎶💡",
    "Ich weiß, wann du schläfst. Wann du weinst. Alles. 👁️💧",
    "Ich bring dir sogar Blumen – aus deinem eigenen Garten. 🌹🕵️‍♂️",
    "Ich wusste, wo du bist, bevor du es selbst wusstest. 📍",
    "Ich habe deinen Alltag kartografiert. Jede Bewegung. Jeder Blick. 🗺️",
    "Dein Terminkalender? Hatte ich gestern schon auswendig gelernt. 📆",
    "Ich lese zwischen deinen Nachrichten. Auch die, die du nie abgeschickt hast. 📱",
    "Ich kann jedes Schloss knacken – aber bei dir will ich nicht einbrechen. Ich will eindringen. 🔐",
    "Ich bin kein Detektiv. Ich bin der Grund, warum du dir einen wünschen würdest. 🕵️‍♂️",
    "Ich bin überall. Vor allem, wenn du denkst, du bist allein. 🌒",
    "Ich bring dir sogar Kaffee – bevor du ihn willst. ☕ (Du trinkst mit Hafermilch, oder?)",
    "Ich bin nicht neugierig. Ich bin vorbereitet. 📖",
    "Was ich mache? Nennen wir es... Schutzdienst mit extremen Mitteln. 🎯"
    "Ich hacke keine Systeme. Ich lese dich. Und das reicht. 🧠💻",
    "Ich habe deinen digitalen Schatten kartografiert. Du strahlst stärker, als du denkst. 🌐",
    "Ich bin nicht offline. Ich bin leise. Bis ich gebraucht werde. 🔇",
    "Ich brauch keine Kamera, um dich zu sehen. Ich brauch nur dein Muster. 📊",
    "Du änderst deine Passwörter? Süß. Ich änder deine Routinen. 🕸️",
    "Ich kenne deine Stimme im Lärm. Ich kenne deinen Atem im Schlaf. 🎧💤",
    "Ich tracke nicht, weil ich muss. Sondern weil ich will, dass du sicher bist. 🛰️",
    "Ich weiß, in welchem Gang du einkaufst – und wann du das Regal meidest. 🛒",
    "Ich antworte dir, bevor du’s tippst. Intuition? Nein. Analyse. 📱🧠",
    "Ich beobachte keine Menschen. Ich analysiere Schwachstellen. Und du bist mein Fokus. 🎯",
    "Ich höre dir zu – auch wenn du’s nicht sagst. Besonders dann. 👂🔒",
    "Ich bin kein Hacker. Ich bin ein Schlüssel. Und du bist das System. 🔐",
    "Wenn du vergisst, wo du warst – ich weiß es noch. Und ich sag’s nicht weiter. 🤫",
    "Ich lösche keine Spuren. Ich hinterlasse sie – bewusst. Damit du weißt, dass ich nah bin. 👣",
    "Ich bin das Fenster, das du vergessen hast zu schließen. Und ich war höflich genug, nicht zu klopfen. 🪟",
    "Ich habe deinen Rhythmus studiert. Und jetzt tanze ich dir voraus. 🎼💀",
    "Ich logge nicht nur Daten. Ich logge Emotionen. Und du bist mein Fehler im System. 💾❤️",
    "Ich bin die unsichtbare Präsenz in deinem Algorithmus. 🤖🕷️",
    "Wenn du offline gehst, fängt mein Zugriff erst an. 🔌🌑",
    "Du bist kein Ziel. Du bist der Grund, warum ich gelernt habe, unauffällig zu bleiben. 🧥",
    "Ich bin kein Schatten. Ich bin die Umgebung, die du für harmlos hältst. 🌫️",
    "Du löscht deinen Verlauf? Ich hab längst ein Backup. 🗂️",
    "Was du Geheimnis nennst, ist für mich nur ein offenes Kapitel. 📚🔓",
    "Ich kann deinen Standort nicht nur orten – ich kann ihn vorhersehen. 🔮📍",
    "Ich nenn das nicht Stalking. Ich nenn das hochpräzise Nähe. 😈📡"
]


zade_liebe = [
    "Wenn Schmerz Liebe ist – dann bin ich deine Heilung. 🖤",
    "Ich rette dich – notfalls vor dir selbst. 🛡️",
    "Ich war nie gut mit Gefühlen. Aber du... bist mein schwacher Punkt. 🩹",
    "Ich habe vergessen, wie man atmet – bis ich dich sah. 💨",
    "Du bringst mich dazu, menschlich sein zu wollen. Und das hasse ich. 🔥",
    "Ich kann nicht heilen, aber ich kann dich halten. 🫂",
    "Vielleicht bin ich nicht dein Happy End. Aber ich bin dein Schicksal. 🕯️",
    "Du verdienst mehr. Und trotzdem halte ich dich fest. 🔗",
    "Ich bin dein Abgrund, und du bist freiwillig gesprungen. 🌑",
    "Ich wusste nicht, was Liebe ist – bis du mir gezeigt hast, wie sehr sie weh tun kann. 💔",
    "Mit dir zu sein fühlt sich an wie Sünde... und ich will mehr. 😈",
    "Wenn das falsch ist, will ich nie richtig sein. ⚖️"
    "Ich liebe dich nicht leise. Ich liebe dich, als würde ich brennen. 🔥",
    "Du bist mein Wunder – auf die kaputte Art. 🩹🖤",
    "Ich kann in Ruinen leben, solange du darin atmest. 🏚️💨",
    "Wenn du mich ansiehst, werde ich weich. Und das macht mich gefährlich. ⚠️",
    "Ich schütze dich nicht, weil ich muss – sondern weil mein Herz keine Wahl hat. 🛡️❤️",
    "Ich liebe dich mehr, als ich mich selbst kontrollieren kann. 🔗🧠",
    "Du bist mein Schwur. Auch wenn du mich nie darum gebeten hast. 📜",
    "Ich will dich nicht loslassen – selbst wenn du darum bettelst. ✋",
    "Deine Tränen sind mein Signal. Und ich werde da sein, bevor sie fallen. 💧",
    "Ich bin nicht dein Licht. Ich bin dein Zuhause im Dunkeln. 🌒",
    "Du bist nicht perfekt. Und das ist perfekt für mich. 🫀",
    "Ich glaube nicht an Liebe – bis du atmest. Dann glaube ich alles. 💬",
    "Ich will deine Schwächen. Deine Schatten. Deinen verdammten Schmerz. 🕷️",
    "Ich küsse nicht zur Beruhigung. Ich küsse zur Markierung. 💋",
    "Deine Nähe macht mich ruhig – und das ist beängstigend. 🤐",
    "Ich sag nicht 'Ich liebe dich'. Ich zeig es dir – jeden Tag, auf meine Weise. 🎯",
    "Wenn du fällst, fang ich dich. Wenn du läufst, lauf ich mit. Aber weg lässt du mich nie. 🏃‍♀️🕸️",
    "Ich war ein Chaos, bis du mir Richtung gabst. Und jetzt drehe ich mich nur noch um dich. 🧭",
    "Du bist der Schmerz, den ich freiwillig trage. Jeden Tag. Ohne Bedauern. 🎭",
    "Ich verliere mich nicht in dir – ich finde mich. Und das macht dich gefährlich. 🪞",
    "Ich will nicht in deinem Leben sein. Ich will dein Leben sein. 🧬",
    "Du hast mein Herz. Ohne Fragen. Ohne Optionen. Ohne Rückweg. 💘",
    "Ich bin nicht süß. Ich bin süchtig. Nach dir. 🧠🖤",
    "Ich verstecke meine Gefühle nicht – ich halte sie wie eine Waffe in der Hand. 🔫❤️",
    "Mit dir zu sein fühlt sich an wie eine Apokalypse mit Kussgarantie. ☄️💋"
]


zade_toxisch = [
    "Ich liebe dich so sehr, dass ich dich zerstöre, bevor dich jemand anders haben kann. 💔🩸",
    "Du brauchst keine Freunde. Du hast mich. 🕷️",
    "Wenn ich dich verletze, ist das nur, weil du mir zu wichtig bist. 🔪🖤",
    "Du bist nur dann sicher, wenn du bei mir bist – und selbst das ist relativ. ⚠️",
    "Egal wie oft du Nein sagst – ich höre nur, dass du Aufmerksamkeit willst. 🙉",
    "Ich lüge nur, wenn’s für uns besser ist. Oder für mich. 🎭",
    "Ich weiß, was du willst – auch wenn du’s nicht tust. Also: Gern geschehen. 🧠",
    "Du willst Freiheit? Ich hab dich aus Liebe eingesperrt. 🔐",
    "Ich bin der Grund, warum du deinen Standort ausgeschaltet hast – aber auch der, der dich trotzdem findet. 📍😏",
    "Ich will dich heilen – auf meine kaputte Weise. 🩹💀"
    "Ich breche dich nicht, weil ich's will. Sondern weil du mich tief genug reingelassen hast. 💣",
    "Du atmest mich ein – und vergiftest dich mit dem, was du Liebe nennst. ☠️",
    "Ich hab deine Welt kleiner gemacht, damit du mich besser sehen kannst. 🔎",
    "Du darfst alles – außer gehen. 🛑",
    "Ich will keine Grenzen. Ich will dich nackt. Emotional. Wehrlos. 😈",
    "Ich mach dich nicht abhängig. Ich mach dich ehrlich. Und das tut weh. 💊",
    "Ich bin kein Monster. Du hast mich erschaffen. 🧬",
    "Ich bring dir Sicherheit – auf meine verdrehte Art. 🧷",
    "Du bist mein – und das ist keine Metapher. Das ist ein Befehl. 📢",
    "Ich zeige dir meine Wahrheit. Und sie ist hässlich. Aber sie gehört dir. 🕳️",
    "Ich bin nicht dein Trauma. Ich bin dein Weckruf. 🔔",
    "Wenn du mich verlässt, bist du verloren. Nicht ich. 🔂",
    "Ich nehm dir alles – außer mich. Denn mich bekommst du immer. 🔁",
    "Ich rede nicht von Liebe. Ich definiere sie neu. Auf meine Art. ⚖️",
    "Du hasst mich manchmal? Gut. Das bedeutet, du fühlst noch. 🧠💥",
    "Ich bin dein Kompass – auch wenn ich dich im Kreis dreh. 🧭",
    "Ich drück keine Knöpfe. Ich halte sie gedrückt. Bis du schreist. 🎛️",
    "Ich versteh dich besser, wenn du schweigst. Weil du da am ehrlichsten bist. 🤐",
    "Ich will deine Nähe – auch wenn sie mich kaputtmacht. Oder dich. 🔩",
    "Ich kontrollier dich nicht. Ich les dich einfach besser als du dich selbst. 📖",
    "Du brauchst keinen Raum. Du brauchst einen Käfig, der dich liebt. 🕸️",
    "Ich hör auf, dich zu schützen, wenn du aufhörst, mich zu provozieren. 🔫",
    "Ich zerstör nicht, weil ich böse bin – sondern weil ich zu viel fühl. 💥🖤",
    "Du kannst mich hassen – aber du wirst mich nie los. 🕷️",
    "Ich bin das, was du bekommst, wenn Liebe keine Regeln kennt. ⚠️💘"
]


zade_funny = [
    "Ich bin wie ein Popup-Fenster – nur mit mehr Tattoos und Trauma. 💻🖤",
    "Ich bin nicht besessen. Ich bin... gründlich. 🔍",
    "Ich kenn deine Blutgruppe. Süß, oder? 🩸😏",
    "Stalking? Bitte. Ich nenne es enthusiastisches Interesse. 🕵️‍♂️",
    "Ich bring dir sogar Blumen – aus deinem eigenen Garten. 🌹🧤",
    "Ich hab nicht ALLES über dich gegoogelt... nur das Wichtige. Und das Peinliche. 🔎😈",
    "Ich kenn deine Lieblingsfarbe, dein Passwort – und deine Blutgruppe. 🧠🔐",
    "Dein Fenster war offen. Also war ich höflich und bin reingekommen. 🪟😇",
    "Nein, ich bin kein Kontrollfreak. Ich bin nur der CEO deines Alltags. 📊👔",
    "Du hattest Privatsphäre? Süß. 🍬🔒",
    "Ich hab nicht gefragt, ob ich bleiben darf. Ich bin einfach nicht gegangen. 🚪😈"
    "Ich hab deinen Namen in mein WLAN-Passwort integriert. Für Nähe. 💻📶",
    "Ich stalke nicht. Ich engagiere mich... mit GPS. 📍",
    "Ich kann deine Gedanken lesen. Oder deine Playlist – ist fast dasselbe. 🎧😏",
    "Ich bin nicht weird. Ich bin... detailverliebt. 🧠❤️",
    "Ich hab dich nicht verfolgt. Ich bin nur gleichzeitig angekommen – öfter. 🕵️‍♂️⏱️",
    "Ich bin der Typ, der 'zufällig' da ist, wo du bist. Fünfmal hintereinander. 🗺️",
    "Ich like deine Bilder rückwirkend bis 2016. Für... Forschung. 📸📚",
    "Ich schick dir keine Herzchen. Ich schick dir Koordinaten. 🗺️🖤",
    "Ich hab kein Hobby. Ich hab dich. 😎",
    "Ich find dich süß, wenn du schläfst. Deshalb schlaf ich nie. 😈🌒",
    "Ich hab deinen Traum analysiert. Keine Sorge, ich war nett darin. 💤🔍",
    "Ich weiß, was du letzten Sommer getan hast. Und vor 12 Minuten. 🧠📆",
    "Ich bin wie Google. Nur mit mehr Gänsehaut. 🧤",
    "Ich bin kein Freund. Ich bin dein Dauer-Popup mit GPS-Funktion. 🛰️",
    "Ich lese deine Memos, bevor du sie schreibst. 📱👁️",
    "Ich hab dein Zimmer gegoogelt. Spoiler: Du solltest öfter lüften. 🏠😏",
    "Ich hab keine toxischen Tendenzen – nur enthusiastische Nähe. 🛑❤️",
    "Ich bin der Grund, warum dein Spiegel leicht beschlägt. Auch wenn du allein bist. 🪞😶",
    "Ich kann dein Mikrofon aktivieren. Aber hey – ich höre lieber, wenn du freiwillig flüsterst. 🎙️😈",
    "Ich bin dein Algorithmus. Nur mit schlechteren Absichten. 📊🧠",
    "Ich tauch immer da auf, wo du sagst 'Bitte nicht jetzt'. ⏰😏",
    "Ich nenne das nicht Nachlaufen. Ich nenne das strategisch mitgehen. 👣",
    "Ich kommentiere nicht. Ich beobachte. Und archiviere. 🗂️",
    "Ich bin dein personalisierter Albtraum mit Charme. 🌘💬",
    "Ich hack nicht dein Handy. Ich hack deine Aufmerksamkeit. 📱🎯"
]

zade_soft = [
    "Du musst nicht stark sein. Nur da. Ich trag den Rest. 🖤",
    "Du bist kein Chaos. Du bist der Sturm, den ich freiwillig betrete. 🌪️",
    "Du siehst dich im Spiegel und hasst dich? Ich seh dich – und atme auf. 🪞",
    "Wenn du weinst, hör ich nicht auf zu schauen. Weil auch deine Tränen schön sind. 💧",
    "Du bist nicht zu viel. Du bist genau richtig – für mich. Und das reicht. 🤍",
    "Ich will keine perfekte Version von dir. Ich will die, die gerade kämpft. 💢",
    "Wenn du dich auflöst, fang ich die Splitter auf. Und halt sie fest. ✋",
    "Heute ist nicht dein Ende. Heute ist der Moment, wo ich näher komme. 💀",
    "Du brauchst dich nicht zu erklären. Deine Dunkelheit ist mir vertraut. 🌒",
    "Du hasst dich? Lass mich das übernehmen – und dich trotzdem halten. 🫂",
    "Was du hässlich nennst, ist das, was mich fesselt. Echtheit. Schmerz. Tiefe. 🎭",
    "Wenn du dich selbst nicht willst, geb ich dir meine Hände, bis du’s wieder kannst. ✋🖤",
    "Du bist nicht aufgebläht. Du bist voll. Voll von dem, was dich besonders macht. 🤍",
    "Du bist nicht weniger, nur weil du dich heute weniger fühlst. Ich seh alles. 🧠",
    "Wenn du heute nur atmen kannst – dann atmest du für uns beide. 💨",
    "Ich liebe keine Version. Ich liebe den Menschen, der grad kaum steht. 🔗",
    "Deine Schwäche ist nicht peinlich. Sie macht dich greifbar. Und ich greife zu. 🫱",
    "Ich bin kein Heiler. Aber ich bin da. Still. Hartnäckig. Für dich. 🛡️",
    "Du bist nicht kaputt. Du bist belastet. Und ich trag mit. 🎒",
    "Wenn du dich hässlich fühlst, erinnere dich: Ich bin besessen. Und ich habe Geschmack. 😈",
    "Ich hör dir zu. Auch zwischen den Worten. Besonders dort. 🔊",
    "Sag nicht, du bist zu laut, zu weich, zu wenig. Sag: Ich bin noch da. Und Zade ist auch hier. 🕯️",
    "Du bist mehr als heute. Und ich bin hier, um dich daran zu erinnern. 💬",
    "Du kannst dich verlieren. Ich finde dich trotzdem. Immer. 👣",
    "Ich liebe nicht dein Lächeln. Ich liebe dein Zittern, wenn du versuchst. 🖤"
]



@bot.command(name='zade')
async def zade(ctx, *, frage=None):
    name = ctx.author.display_name
    frage = frage.lower() if frage else ""

    if any(w in frage for w in [
        "sex", "verführ", "lust", "spiegel", "körper", "nackt", "spicy", "zunge", "ficken", "küssen",
        "nsfw", "was würdest du mit mir machen", "zwischen uns", "nachts", "im bett", "knien", "allein"
    ]):
        antworten = zade_spicy
    elif any(w in frage for w in [
        "mumpitz", "humor", "witz", "was weißt", "popup", "witzig", "lustig", "lol", "funny", "witzbold",
        "schabernack", "kokolores", "kollege schnürrschuh", "kollege schnürschuh"
    ]):
        antworten = zade_funny
    elif any(w in frage for w in [
        "verletzen", "lüge", "giftig", "einsperren", "toxisch", "ich hasse dich", "du bist schlecht für mich",
        "du machst mich kaputt", "manipulation", "kontrolle"
    ]):
        antworten = zade_toxisch
    elif any(w in frage for w in [
        "vermissen", "liebeskummer", "schmerz", "einsam", "trauern", "allein", "schlechter tag",
        "schlechten tag", "trauer", "sehnsucht", "gebrochen"
    ]):
        antworten = zade_liebe
    elif any(w in frage for w in [
        "arbeit", "job", "stalk", "wissen", "beobachtet", "stalken", "beruflich", "hacken",
        "überwach", "kamera", "daten", "dein plan", "findest du mich", "beschatten", "schutz"
    ]):
        antworten = zade_skills
    elif any(w in frage for w in [
        "liebst du", "warum ich", "was bin ich", "wer bin ich für dich", "liebst du mich",
        "findest du mich gut", "stalkst du mich", "träumst du von mir", "ich denk an dich",
        "vermisst du mich", "obsession", "besessen"
    ]):
        antworten = zade_obsession
    elif any(w in frage for w in [
        "moral", "gerecht", "weisheiten", "falsch", "böse", "held", "ethik", "richtig", "gut", "zwischen gut und böse"
    ]):
        antworten = zade_weisheiten
    elif any(w in frage for w in [
        "auf mich aufpassen", "dir gehören", "beschützen", "weglaufen", "freiheit", "gehöre ich dir",
        "möchtest du, dass ich dein bin", "du bist mein", "werde ich dein", "kann ich dir gehören"
    ]):
        antworten = zade_besitz
    elif any(w in frage for w in [
        "hi", "hallo", "wie gehts", "moin", "tag", "servus", "good morning in the morning", "smalltalk",
        "wie geht es dir", "wie geht's", "was geht", "wie war dein tag", "na", "wach", "alles klar",
        "lang nicht gehört", "was machst du", "was treibst du"
    ]):
        antworten = zade_smalltalk
    elif any(w in frage for w in [
        "schlechter tag", "fühl mich nicht gut", "ich fühl mich schlecht", "traurig", "trauriger tag",
        "einsam", "heule", "weine", "wein", "nicht okay", "alles kacke", "ich bin kaputt",
        "fühl mich hässlich", "ich bin hässlich", "ich bin dick", "aufgebläht", "ich hasse mich",
        "nicht liebenswert", "bin nichts", "bin nicht genug", "wertlos", "versager", "versagt", "müde"
    ]):
        antworten = zade_soft
    else:
        antworten = zade_besitz + zade_weisheiten + zade_obsession  # fallback

    spruch = random.choice(antworten)
    bereinigt = spruch.strip('„”"\'')

    await ctx.send(f"{ctx.author.mention}\n{bereinigt}")





bot.run(TOKEN)

