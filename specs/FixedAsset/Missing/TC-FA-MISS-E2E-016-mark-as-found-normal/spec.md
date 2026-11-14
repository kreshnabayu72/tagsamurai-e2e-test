---
id: TC-FA-MISS-E2E-016-mark-as-found-normal
title: "Mark as Found aset tanpa TAG: Found at, Asset Status Normal, record Found di History, toast available again"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1a#r32", "§4.4#r7", "§7.2#r2", "§7.3#r8", "§9.6#r4", "§9.2#r5", "§1.2#r36", "§1.2#r72", "§1.2#r79", "§1.2#r81", "§1.2#r89", "§1.2#r90", "§1.2#r91", "§1.2#r92", "§1.2#r101", "§1.2#r102", "§1.2#r30", "§9.2#b24", "§9.2#b25", "§9.2#b26", "§8.1#r14", "§9.4.2#r8", "§9.4.2#r5", "§9.9#r3", "§9.9#r5", "§9.5#r8", "§4.2.4#r10", "§4.2.4#r11", "§2.1#r7", "§9.1#r4", "§3#p8", "§9.4.4#r11", "§9.4.4#r12", "§9.7#r4", "§9.8#r7", "§10#r3", "§1.2#r103", "EB-FB-1@mark-as-found", "EB-EDG-2"]
smoke: []
dependsOn: []
trace:
  "§4.1a#r32": [5, 7, 19]
  "§4.4#r7": [7, 19]
  "§7.2#r2": 7
  "§7.3#r8": [19, 43]
  "§9.6#r4": [19, 27]
  "§9.2#r5": [21, 24, 47]
  "§1.2#r36": 19
  "§1.2#r72": [28, 29, 30]
  "§1.2#r79": [10, 29]
  "§1.2#r81": 19
  "§1.2#r89": 28
  "§1.2#r90": 25
  "§1.2#r91": 19
  "§1.2#r92": [16, 25]
  "§1.2#r101": [21, 35]
  "§1.2#r102": [24, 35]
  "§1.2#r30": [2, 3, 25]
  "§9.2#b24": 31
  "§9.2#b25": [24, 27]
  "§9.2#b26": [43, 47]
  "§8.1#r14": [28, 29, 30]
  "§9.4.2#r8": [16, 25]
  "§9.4.2#r5": [43, 47, 49]
  "§9.9#r3": [8, 13, 14, 28]
  "§9.9#r5": [30, 43]
  "§9.5#r8": [8, 40]
  "§4.2.4#r10": [8, 40]
  "§4.2.4#r11": [16, 41]
  "§2.1#r7": 5
  "§9.1#r4": [19, 24]
  "§3#p8": [19, 24]
  "§9.4.4#r11": 28
  "§9.4.4#r12": [47, 49]
  "§9.7#r4": [19, 24]
  "§9.8#r7": [24, 47]
  "§10#r3": [2, 24]
  "§1.2#r103": [2, 24]
  "EB-FB-1@mark-as-found": 19
  "EB-EDG-2": 44
anchor: [20, 34]
coverage:
  web: automated
---

# Mark as Found aset tanpa TAG: Found at, Asset Status Normal, record Found di History, toast available again

## Prerequisites
- Aktor: Rina W, Total Control, tidak menjadi Last Holder record di bawah.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-016-1: Record Missing `Camera DSLR Canon R6 {runId}`, aset tanpa TAG, Asset ID `CAM-016-0001`, Group `Finance Room`, Status `Missing`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 6 hari, pukul 09:00`.
  - DU-016-2: Record Waiting for Confirmation `Hand Held Radio Motorola {runId}`, aset tanpa TAG, Asset ID `HHR-016-0002`, Group `Finance Room`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari D`, Reported By `Sari D`, Reported Date `T0 − 1 hari, pukul 08:00`; baris transaksi pemegang untuk aset ini masih terbuka.
  - DU-016-3: Isian Mark as Found untuk DU-016-1: Found at `Server Room`, Asset Status `Normal`, Note `Ditemukan di rak server lantai 2 saat pemeriksaan rutin`. Node yang diharapkan: `Marked as found by Rina W`.
  - Pengguna pada data: Rina W, Total Control, seluruh client; Sari D, pemegang yang memakai akun sendiri.
  - Pohon Group pada entitas: `Head Office` sebagai induk, dengan `Finance Room` dan `Server Room` sebagai node terbawah.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`

## Test Steps

### Dialog Mark as Found dari record Missing tanpa TAG
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi Status baris `Camera DSLR Canon R6 {runId}` menampilkan `Missing`
3. Verifikasi Group baris `Camera DSLR Canon R6 {runId}` menampilkan `Finance Room`
4. Klik `⋯` pada baris `Camera DSLR Canon R6 {runId}`
5. Verifikasi menu baris memuat `Mark as Found` bagi Total Control yang bukan Last Holder
6. Klik `Mark as Found`
7. Verifikasi dialog `Mark as Found` terbuka
8. Verifikasi Found at terisi `Finance Room` sebagai Group aset
9. Buka pilihan Asset Status
10. Verifikasi pilihan Asset Status memuat `Normal` dan `Damaged`
11. Pilih Asset Status `Normal`
12. Buka pilihan Found at
13. Verifikasi `Head Office` tidak dapat dipilih karena Group induk
14. Verifikasi `Server Room` dapat dipilih
15. Pilih Found at `Server Room`
16. Verifikasi info `Found outside its group. Transfer it back if needed.` tampil
17. Isi Note `Ditemukan di rak server lantai 2 saat pemeriksaan rutin`
18. Klik `[Mark as Found]`
19. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan Asset Name record `Camera DSLR Canon R6 {runId}`
20. Verifikasi baris `Hand Held Radio Motorola {runId}` tetap tampil di sub-tab Active
21. Verifikasi baris `Camera DSLR Canon R6 {runId}` tidak tampil lagi di sub-tab Active
### Record Found di sub-tab History
22. Klik sub-tab `History`
23. Ketik Search `{runId}`, tekan Enter
24. Verifikasi baris `Camera DSLR Canon R6 {runId}` tampil di sub-tab History dengan Status `Found`
25. Verifikasi Group baris `Camera DSLR Canon R6 {runId}` tetap `Finance Room`
26. Klik nama `Camera DSLR Canon R6 {runId}` pada kolom Name
27. Verifikasi badge status record `Found` tampil
28. Verifikasi node `Marked as found by Rina W` memuat Found at `Server Room`
29. Verifikasi node `Marked as found by Rina W` memuat Asset Status `Normal`
30. Verifikasi node `Marked as found by Rina W` memuat Note `Ditemukan di rak server lantai 2 saat pemeriksaan rutin`
31. Verifikasi waktu node `Marked as found by Rina W` sama dengan waktu Submit tadi menurut Date Format dan Time Format
32. Klik `✕` pada dialog Missing Log
33. Klik `⋯` pada baris `Camera DSLR Canon R6 {runId}`
34. Verifikasi menu baris record Found memuat aksi `Missing Log`
35. Verifikasi `Mark as Found` tidak tampil pada menu baris karena record Found tidak dibuka ulang
### Mark as Found dari Waiting for Confirmation tanpa Note
36. Klik sub-tab `Active`
37. Ketik Search `{runId}`, tekan Enter
38. Klik `⋯` pada baris `Hand Held Radio Motorola {runId}`
39. Klik `Mark as Found`
40. Verifikasi Found at terisi `Finance Room` sebagai Group aset
41. Verifikasi info `Found outside its group. Transfer it back if needed.` tidak tampil karena Found at sama dengan Group aset
42. Klik `[Mark as Found]` tanpa mengisi Note
43. Verifikasi toast `Success, asset has been marked as found.` tampil
44. Verifikasi empty state `No results found` tampil karena record terakhir spec ini sudah pindah dari sub-tab Active
45. Klik sub-tab `History`
46. Ketik Search `{runId}`, tekan Enter
47. Verifikasi baris `Hand Held Radio Motorola {runId}` tampil di sub-tab History dengan Status `Found`
48. Klik nama `Hand Held Radio Motorola {runId}` pada kolom Name
49. Verifikasi node `Marked as found by Rina W` memuat Found at `Finance Room`
