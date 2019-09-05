<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="de" sourcelanguage="de">
<context>
    <name>MainWindow</name>
    <message>
        <location filename="../../gui/gui.ui" line="74"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Auf diesem Reiter kannst du Dateien verschlüsseln.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="77"/>
        <source>Verschlüsselung</source>
        <comment>tabEncrypt</comment>
        <translation>Verschlüsselung</translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="95"/>
        <location filename="../../gui/gui.ui" line="125"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Hier kannst du die Dateien auswählen, die verschlüsselt werden sollen. Benutze hierzu die Schaltlfläche &amp;quot;Dateien hinzufügen&amp;quot;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="98"/>
        <source>1. &quot;Klartext&quot;-Dateien auswählen</source>
        <comment>grpInputFilesEnc</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="157"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Füge mit dieser Schaltfläche Dateien hinzu die verschlüsselt werden sollen. Ein Klick auf sie öffnet ein Auswahlfenster. &lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Tipp: &lt;/span&gt;Du kannst im Auswahlfenster auch mehrere Dateien auswählen und anschließend hinzufügen. Ziehe hierzu entweder einen Rahmen mit der linken Maustaste oder verwende die Tastenkombinationen Strg+Linksklick oder Umschalt+Linksklick auf die Dateien.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="160"/>
        <source>Dateien hinzufügen</source>
        <comment>btnAddInputFiles</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="167"/>
        <source>Ctrl+S</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="180"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Diese Schaltfläche erlaubt es dir, in der oberen Ansicht markierte Dateien wieder zu entfernen, damit sie &lt;span style=&quot; font-weight:600;&quot;&gt;nicht&lt;/span&gt; verschlüsselt werden.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="183"/>
        <source>Ausgewählte entfernen</source>
        <comment>btnRemoveInputFiles</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="201"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Hier hast du die Auswahl zwischen zwei verschiedenen Quellen für die beim Verschlüsselungsvorgang genutzten Zufallszahlen.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="204"/>
        <source>2. Quelle für Zufallszahlen auswählen</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="232"/>
        <source>Physikalischer Zufall aus Quantenfluktuation (max. Gesamtdatengröße: 1MiB)</source>
        <comment>rbRandomOrg</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="242"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Wenn diese Option gewählt ist, dann wird der systemeigene Pseudozufallsgenerator für kryptografische Zwecke (CSPRNG) verwendet. Je nach verwendetem Betriebssystem gibt es hier Unterschiede, aber in der Regel wird versucht, echten physischen Zufall zu nutzen, um einen Algorithmus zu füttern, der Pseudozufallszahlen ausgibt.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; text-decoration: underline;&quot;&gt;Vorteile&lt;/span&gt;:&lt;/p&gt;&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Schneller als Zufallszahlen von der ANU, da keine Anfrage an einen Server gesendet werden muss&lt;/li&gt;&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Benötigt keine Internetverbindung&lt;/li&gt;&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Kein Limit für Dateigrößen, daher für große Dateien zu empfehlen&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;&lt;span style=&quot; text-decoration: underline;&quot;&gt;Nachteile&lt;/span&gt;:&lt;/p&gt;&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;ETWAS weniger Sicherheit als &amp;quot;echter&amp;quot; Zufall. Es besteht die Möglichkeit (sofern das benutzte System kompromittiert wurde), dass ein potenzieller Angreifer die Initialisierung des Pseudozufallsgenerators mitbekommt oder nachkonstruieren kann. Dieser Fall ist je nach System mehr oder weniger gefährlich für die tatsächliche Sicherheit des Gesamtschlüssels.&lt;/li&gt;&lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="245"/>
        <source>Systemeigener CSPRNG (Pseudozufallsgenerator)</source>
        <comment>rbCSPRNG</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="314"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;Noto Sans&apos;; font-size:9pt; font-weight:600; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Ein Klick auf diese Schaltfläche sorgt dafür, dass der Verschlüsselungsvorgang angestoßen wird.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Je nach Erfolg oder Misserfolg wird das Ergebnis in der Textbox unter dieser Schaltfläche ausgegeben.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; text-decoration: underline;&quot;&gt;HINWEIS&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Nach abgeschlossener Verschlüsselung werden die Klartext-Dateien &lt;/span&gt;gelöscht&lt;span style=&quot; font-weight:400;&quot;&gt;. An ihrer Stelle befinden sich nun zwei Arten von Dateien.:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;- &lt;/span&gt;&lt;span style=&quot; font-weight:400; font-style:italic;&quot;&gt;crypt&lt;/span&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;-Datei: Dies ist die verschlüsselte Datei.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;- &lt;/span&gt;&lt;span style=&quot; font-weight:400; font-style:italic;&quot;&gt;otp&lt;/span&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;-Datei: Dies ist der Schlüssel.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Es ist wichtig, dass nach Abschluss des Verschlüsselungsvorgangs entweder die OTP-Dateien oder die CRYPT-Dateien ausgeschnitten und an einem anderen Speicherort (bspw. einem USB-Stick) eingefügt werden, damit sich verschlüsselte Dateien und ihre jeweligen Schlüssel &lt;/span&gt;NICHT AUF DER GLEICHEN MASCHINE BEFINDEN&lt;span style=&quot; font-weight:400;&quot;&gt;. &lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Sonst besteht natürlich &lt;/span&gt;keine&lt;span style=&quot; font-weight:400;&quot;&gt; Sicherheit, da ein Angreifer mit Zugriff auf den Rechner ja über die verschlüsselten Dateien UND die zugehörigen Schlüssel verfügen würde.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Später müssen sie dann wieder zurück an den selben Speicherort kopiert werden, wenn eine Entschlüsselung erfolgen soll.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="329"/>
        <source>3. Verschlüsselung durchführen!</source>
        <comment>btnEncrypt</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="410"/>
        <location filename="../../gui/gui.ui" line="440"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Dieses Feld zeigt die Ausgabe des Verschlüsselungsvorgangs an. Fehler- oder Erfolgsmeldungen sind hier zu finden.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="413"/>
        <source>4. Ausgabe des Verschlüsselungsvorgangs</source>
        <comment>grpEncryptionResult</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="460"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Auf diesem Reiter kannst du Dateien entschlüsseln.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="463"/>
        <source>Entschlüsselung</source>
        <comment>tabDecrypt</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="849"/>
        <source>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Los geht&apos;s.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="862"/>
        <source>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Besorge mir Quantenfluktuationszufallsdaten von der Australian National University. Das dauert (wenn es klappt) in der Regel so etwa 20-30 Sekunden...
Sollte es nicht klappen, lasse ich es nach 60 Sekunden bleiben.</source>
        <translation>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Besorge Quantenfluktuationszufallsdaten von der Australian National University. Das dauert (wenn es klappt) in der Regel so etwa 5-30 Sekunden...
Sollte es nicht klappen, lasse ich es nach 60 Sekunden bleiben.</translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="876"/>
        <source>&lt;div style=&quot;color:red;font-weight:bold;&quot;&gt;FEHLER&lt;/div&gt;: Deine Dateien sind insg. größer als 1 Megabyte. Probier&apos;s stattdessen mit dem CSPRNG. Der ist für große Datenmengen besser geeignet.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="889"/>
        <source>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Beginne mit der Verschlüsselung der Dateien.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="902"/>
        <source>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Damit nicht IRGENDJEMAND deine Dateien entschlüsseln kann, musst du die Schlüsseldateien (*.otp) an einen anderen Speicherort verschieben, der sich am besten nicht ungesichert auf diesem Computer befindet; einen USB-Stick zum Beispiel, den du an einem gesicherten Ort aufbewahren kannst.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="915"/>
        <source>&lt;div style=&quot;color:red;font-weight:bold;&quot;&gt;FEHLER&lt;/div&gt;: Nicht alle Schlüssel befinden sich in den Verzeichnissen ihrer zugehörigen verschlüsselten Dateien. Es fehlen:</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="928"/>
        <source>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Um eine crypt-Datei wieder zu entschlüsseln, muss sich im gleichen Ordner eine passende otp-Datei befinden. Beispiel: &apos;Geheim.txt.crypt&apos; ist die verschlüsselte Datei. Im gleichen Ordner muss sich die Datei &apos;Geheim.txt.otp&apos; befinden. Diese ist der Schlüssel. Anschließend kann die Entschlüsselung erfolgen und heraus kommt: &apos;Geheim.txt&apos; - die ursprünglich verschlüsselte Datei wieder im Klartext.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="941"/>
        <source>&lt;div style=&quot;color:red;font-weight:bold;&quot;&gt;FEHLER&lt;/div&gt;: Keine Dateien zur Entschlüsselung ausgewählt ;-)</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="954"/>
        <source>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Beginne mit der Entschlüsselung der Dateien.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="967"/>
        <source>&lt;div style=&quot;color:green;font-weight:bold;&quot;&gt;ERFOLG&lt;/div&gt;: Die Dateien wurden erfolgreich wieder entschlüsselt! Sie befinden sich dort, wo sich zuvor die crypt-Dateien befanden.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="980"/>
        <source>&lt;div style=&quot;color:red;font-weight:bold;&quot;&gt;FEHLER&lt;/div&gt;: Konnte keine Quantenzufallsdaten von den Servern der Australian National University anfordern. Probier&apos; es später noch einmal oder wähle den CSPRNG als Zufallsdatenquelle aus. Der ist nicht auf externe Server angewiesen und bietet ebenfalls nahezu perfekte Sicherheit für die OTP-Verschlüsselung.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="993"/>
        <source>&lt;div style=&quot;color:#3A3A3A;font-weight:bold;&quot;&gt;INFO&lt;/div&gt;: Quantenfluktuationszufallsdaten von der Australian National University erhalten! Abfragedauer: {} Sekunden.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1006"/>
        <source>&lt;div style=&quot;color:red;font-weight:bold;&quot;&gt;FEHLER&lt;/div&gt;: Die angeforderte Datenmenge übersteigt 1MiB. Benutze einfach den CSPRNG für große Datenmengen.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1019"/>
        <source>&lt;div style=&quot;color:red;font-weight:bold;&quot;&gt;FEHLER&lt;/div&gt;: Unbekannter Fehler bei der Anfrage der Zufallsdaten von der ANU.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1154"/>
        <source>Programmfehler melden</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="229"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Wenn diese Option gewählt ist, dann wird die Internetseite &amp;quot;http://qrng.anu.edu.au&amp;quot; als Quelle für die beim Verschlüsselungsvorgang benötigten Zufallszahlen verwendet.&lt;/p&gt;&lt;p&gt;Die Australian National University verwendet Quantenfluktuation im Vakuum als Quelle für &amp;quot;echten&amp;quot; Zufall (meint: Zufall aus physikalischen Vorgängen).&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; text-decoration: underline;&quot;&gt;Vorteile&lt;/span&gt;:&lt;/p&gt;&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Physischer Zufall sorgt für erhöhte Sicherheit (da er schlichtweg nicht vorhersehbar oder nachträglich rekonstruierbar ist)&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;&lt;span style=&quot; text-decoration: underline;&quot;&gt;Nachteile&lt;/span&gt;:&lt;/p&gt;&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Internetverbindung wird benötigt&lt;/li&gt;&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Nur für geringe Datenmengen nutzbar, da wir die ANU nicht mit zu vielen Anfragen überfluten und ihre kostenlos bereitgestellte Serverleistung und Bandbreite übermäßig beanspruchen möchten&lt;/li&gt;&lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="481"/>
        <location filename="../../gui/gui.ui" line="505"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Diese Dateien mit der Endung &amp;quot;.crypt&amp;quot; werden von Lokkat beim Verschlüsselungsvorgang erstellt. Sie sind sind die verschlüsselten Dateien. &lt;/p&gt;&lt;p&gt;Bitte darauf achten, dass sich zum Entschlüsselungsvorgang die &amp;quot;.otp&amp;quot;-Schlüsseldateien in den selben Verzeichnissen befinden, wie ihre &amp;quot;.crypt&amp;quot;-Dateien.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="484"/>
        <source>1. Zu entschlüsselnde Dateien (&quot;.crypt&quot;-Dateien) auswählen</source>
        <comment>grpInputFilesDec</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="537"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Diese Schaltfläche kannst du benutzen, um Dateien, die entschlüsselt werden sollen, hinzuzufügen. Nach einem Klick öffnet sich ein Auswahlfenster, indem du die &amp;quot;.crypt&amp;quot;-Dateien auswählen kannst.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Tipp: &lt;/span&gt;Du kannst im Auswahlfenster auch mehrere Dateien auswählen und anschließend hinzufügen. Ziehe hierzu entweder einen Rahmen mit der linken Maustaste oder verwende die Tastenkombinationen Strg+Linksklick oder Umschalt+Linksklick auf die Dateien.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="540"/>
        <source>Dateien hinzufügen</source>
        <comment>grpAddInputFiles</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="551"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Diese Schaltfläche erlaubt es dir, die oberhalb markierten &amp;quot;.crypt&amp;quot;-Dateien wieder zu entfernen, damit sie &lt;span style=&quot; font-weight:600;&quot;&gt;nicht&lt;/span&gt; entschlüsselt werden.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="554"/>
        <source>Ausgewählte entfernen</source>
        <comment>grpRemoveInputFiles</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="624"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Startet den Entschlüsselungsvorgang.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Damit dieser erfolgreich sein kann, werden zwei Arten von Dateien benötigt:&lt;/span&gt;&lt;/p&gt;&lt;ol style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;crypt-Dateien: Beinhalten das Kryptat, also die verschlüsselten Dateien.&lt;/span&gt;&lt;/li&gt;&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;otp-Dateien: Beinhalten die Schlüssel.&lt;/span&gt;&lt;/li&gt;&lt;/ol&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;Es ist wichtig, dass die otp-Dateien in den selben Ordnern liegen, wie die jeweiligen crypt-Dateien.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="627"/>
        <source>2. Entschlüsselung durchführen!</source>
        <comment>btnDecrypt</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="711"/>
        <location filename="../../gui/gui.ui" line="738"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Hier werden die Ergebnisse des Entschlüsselungsvorgangs als Textmeldungen angezeigt.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="714"/>
        <source>3. Ausgabe des Entschlüsselungsvorgangs</source>
        <comment>grpDecryptionResult</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="771"/>
        <source>Welche Dateien sollen verschlüsselt werden?</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="797"/>
        <source>.crypt-Dateien (*.crypt)</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="810"/>
        <source>Welche Dateien sollen entschlüsselt werden?</source>
        <translation></translation>
    </message>
    <message>
        <source>INFO: Besorge Quantenfluktuationszufallsdaten von der Australian National University. Das dauert (wenn es klappt) in der Regel so etwa 20-30 Sekunden...</source>
        <translation type="vanished">INFO: Besorge Quantenfluktuationszufallsdaten von der Australian National University. Das dauert (wenn es klappt) in der Regel so etwa 20-30 Sekunden... sollte keine Verbindung möglich sein, kommt ein Timeout nach 40 Sekunden.</translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1038"/>
        <source>Datei</source>
        <comment>menuFile</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1044"/>
        <source>Hilfe</source>
        <comment>menuHelp</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1054"/>
        <source>Sprache/Language</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1069"/>
        <source>Hilfedatei öffnen</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1072"/>
        <source>F1</source>
        <comment>actionOpenHelpFile</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1084"/>
        <source>Projektwebseite aufrufen</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1096"/>
        <source>Über Lokkat...</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1114"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Schließt Lokkat.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1099"/>
        <source>F12</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="14"/>
        <source>Lokkat 0.5</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="784"/>
        <source>Alle Dateien (*.*);; Wirklich ALLE Dateien (*)</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="823"/>
        <source>&lt;div style=&quot;color:green;font-weight:bold;&quot;&gt;ERFOLG&lt;/div&gt;: Verschlüsselung erfolgreich beendet! Du findest die verschlüsselten Dateien (Dateiendung: &quot;.crpyt&quot;) und die Schlüsseldateien (Dateiendung: &quot;.otp&quot;) dort, wo sich zuvor die Klartextdateien befanden.</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="836"/>
        <source>&lt;div style=&quot;color:red;font-weight:bold;&quot;&gt;FEHLER&lt;/div&gt;: Keine Dateien zur Verschlüsselung ausgewählt ;-)</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1087"/>
        <source>F3</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1111"/>
        <source>Schließen</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1117"/>
        <source>Ctrl+Q</source>
        <comment>actionClose</comment>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1131"/>
        <source>Deutsch</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../gui/gui.ui" line="1142"/>
        <source>Englisch</source>
        <translation></translation>
    </message>
</context>
</TS>
