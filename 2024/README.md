# White Hats for Future 2024

* *Laufzeit:* 06.02.2024 - 13.02.2024
* *Website:* https://www.tha.de/Informatik/THA-innos/Institut/White-Hats-for-Future-2024.html

## SHA-256 Hashwert für Flags

Die Aufgaben enthalten keine Lösungsflags, sondern nur deren SHA-256 Hashwerte.

Unter Linux kann man ein beliebiges Flag mit folgender Vorgehensweise überprüfen:

`echo -n "<FLAG>" | sha256sum`

Für die Überprüfung, ob das Flag `THAINNOS{Test123ABC}` zum Hashwert
`3c5bdb9fb3defa75f21b198239e48743abe54ee6398c29f685abd841ba77223e` passt,
würde man folgendes Kommando ausführen:

```
echo -n "THAINNOS{Test123ABC}" | sha256sum
8b80fb3d783523e0b920eef6da1469196dcfecc077a0d5a6ed8ed4bdfbd84124  -
```

... und feststellen, dass die Hashwerte nich zusammen passen.
Das Flag ist somit nicht richtig.
