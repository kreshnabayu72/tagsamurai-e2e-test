---
id: TC-FA-FATR-E2E-007-override-add
title: "Add override membuat satu baris per target"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: [§4.1#r278, §4.1#r281, §4.1#r282, §4.1#r295, §4.1#r296, §4.4#r10, §4.4#r16, §4.4#r17, §4.4#r18, §9.2#b74, §9.2#b75, §9.2#b80, §9.2#b81, §9.2#b89, §9.2#b182, §9.4.2#r26, §9.4.2#r56, §9.4.2#r104, §9.4.2#r105, §9.4.2#r106, §9.6#r2, §9.7#r13, EB-FRM-1@add-override, §Aturan Logika Modul#r43, §Aturan Logika Modul#r52, §7#r3, §9.2#b94, EB-FB-1@add-override]
smoke: [§Aturan Logika Modul#r43, §Aturan Logika Modul#r52, §7#r3, §9.2#b94, EB-FB-1@add-override]
dependsOn: []
trace:
  §4.1#r278: 18
  §4.1#r281: [31, 32, 33]
  §4.1#r282: 56
  §4.1#r295: 12
  §4.1#r296: 44
  §4.4#r10: 5
  §4.4#r16: 33
  §4.4#r17: 17
  §4.4#r18: [15, 29, 47]
  §9.2#b74: 17
  §9.2#b75: 56
  §9.2#b80: [31, 32]
  §9.2#b81: 57
  §9.2#b89: 50
  §9.2#b182: [49, 50]
  §9.4.2#r26: 33
  §9.4.2#r56: [49, 50]
  §9.4.2#r104: 33
  §9.4.2#r105: 17
  §9.4.2#r106: [15, 29, 47]
  §9.6#r2: [15, 17]
  §9.7#r13: 17
  EB-FRM-1@add-override: 33
  §Aturan Logika Modul#r43: 50
  §Aturan Logika Modul#r52: 33
  §7#r3: [15, 29, 47]
  §9.2#b94: 33
  EB-FB-1@add-override: 15
anchor: [55]
coverage:
  web: automated
---

# Add override membuat satu baris per target

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-007-1: Category leaf `Machinery {runId}`, ada di entitas aktor, dengan `Max duration` tab `Borrow` bernilai sendiri `21` dan `Duration unit` Inherit.
  - DU-007-2: Category leaf `Laptop {runId}`, ada di entitas aktor.
  - DU-007-3: Group `Proyek Karawang {runId}`, Group tingkat atas, ada di entitas aktor.
  - DU-007-4: Group `Workshop {runId}`, Group turunan langsung dari `Proyek Karawang {runId}`.
  - DU-007-5: Asset Name `Excavator PC200 {runId}`, Code `EXC7-{runId}`, Category `Machinery {runId}`, UoM `Unit`.
  - DU-007-6: Asset Name `Toyota Avanza {runId}`, Code `AVZ7-{runId}`, Category `Machinery {runId}`, UoM `Unit`.
  - Override yang dibuat spec ini bernilai: Group `Proyek Karawang {runId}` dengan `Max duration` `30` di Category `Machinery {runId}` (DU-007-7); Asset Name `Excavator PC200 {runId}` dan `Toyota Avanza {runId}` dengan `Max duration` `10` di Category `Machinery {runId}` (DU-007-8); Group `Proyek Karawang {runId}` dengan `Max duration` `45` di All categories (DU-007-9). Teks kolom Overridden yang diharapkan: `Max duration (30 days)`, `Max duration (10 days)`, dan `Max duration (45 days)`, dari Duration unit efektif `Days`.
- Kondisi:
  - Company default `Max duration` bernilai `14` dan `Duration unit` bernilai `Days`.
  - Category `Machinery {runId}` mewarisi dari Company default seluruh field transaksi kecuali `Max duration` tab `Borrow` yang bernilai sendiri `21`, sehingga nilai berlaku `Max duration` di Category itu `21 days`, berbeda dari Company default.
  - Category `Laptop {runId}` mewarisi seluruh field transaksi dari Company default (Inherit).

## Test Steps

### Override Group dari Category leaf dibuat untuk parent saja
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Klik `[+ Override]`
5. Verifikasi dialog `Add override - Borrow` terbuka
6. Pilih Scope `Group`
7. Klik `[Select Group]`
8. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
9. Centang Group `Proyek Karawang {runId}`
10. Klik `[Select]`
11. Pilih Field `Max duration`
12. Verifikasi teks bantu `Current value: 21 days` tampil di bawah baris Field + Value
13. Isi Value `30`
14. Klik `[Submit]`
15. Verifikasi toast `Success, override has been added.` tampil
16. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
17. Verifikasi baris dengan Scope `Group`, Target `Proyek Karawang {runId}`, dan Overridden `Max duration (30 days)` tampil di tabel Overrides
18. Verifikasi tidak ada baris dengan Target `Workshop {runId}` di tabel Overrides

### Override Asset Name dengan dua target dibuat satu baris per target
19. Klik `[+ Override]`
20. Pilih Scope `Asset Name`
21. Klik `[Select Asset Name]`
22. Ketik Search `{runId}` pada dialog Select Asset Name, tekan Enter
23. Centang Asset Name `Excavator PC200 {runId}`
24. Centang Asset Name `Toyota Avanza {runId}`
25. Klik `[Select]`
26. Pilih Field `Max duration`
27. Isi Value `10`
28. Klik ganda `[Submit]`
29. Verifikasi toast `Success, override has been added.` tampil satu kali meskipun `[Submit]` diklik ganda
30. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
31. Verifikasi baris dengan Scope `Asset Name`, Target `Excavator PC200 {runId}`, dan Overridden `Max duration (10 days)` tampil di tabel Overrides
32. Verifikasi baris dengan Scope `Asset Name`, Target `Toyota Avanza {runId}`, dan Overridden `Max duration (10 days)` tampil di tabel Overrides
33. Verifikasi tabel Overrides hasil Search `{runId}` memuat `3` baris, satu baris per target

### Override All categories berdampingan dengan override Category leaf untuk target dan transaksi yang sama
34. Klik `(←)` pada kotak Search Sidebar Category Tree
35. Klik node `All categories` di Sidebar Category Tree
36. Klik tab `Borrow`
37. Klik `[+ Override]`
38. Pilih Scope `Group`
39. Klik `[Select Group]`
40. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
41. Centang Group `Proyek Karawang {runId}`
42. Klik `[Select]`
43. Pilih Field `Max duration`
44. Verifikasi teks bantu `Company default: 14 days` tampil di bawah baris Field + Value
45. Isi Value `45`
46. Klik `[Submit]`
47. Verifikasi toast `Success, override has been added.` tampil
48. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
49. Verifikasi baris dengan Scope `Group`, Target `Proyek Karawang {runId}`, dan Overridden `Max duration (30 days)` tampil di tabel Overrides
50. Verifikasi baris dengan Scope `Group`, Target `Proyek Karawang {runId}`, dan Overridden `Max duration (45 days)` tampil di tabel Overrides

### Override Category leaf tidak tampil di Category lain
51. Ketik Search Sidebar Category Tree `Laptop {runId}`, tekan Enter
52. Klik node `Laptop {runId}` di Sidebar Category Tree
53. Klik tab `Borrow`
54. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
55. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (45 days)` tampil di tabel Overrides
56. Verifikasi tidak ada baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (30 days)` di tabel Overrides
57. Verifikasi tidak ada baris dengan Target `Excavator PC200 {runId}` di tabel Overrides
