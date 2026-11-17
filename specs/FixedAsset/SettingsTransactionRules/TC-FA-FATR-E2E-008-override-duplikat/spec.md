---
id: TC-FA-FATR-E2E-008-override-duplikat
title: "Add override ditolak untuk override aktif yang duplikat"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [§4.1#r305, §4.1#r306, §6#r10, §9.2#b97, §9.4.2#r115, §9.4.2#r116, §9.4.2#r118, §9.4.4#r21, §9.9#r21, §Aturan Logika Modul#r45, §9.2#b98, §9.6#r22, EB-FRM-5@target-add-override]
smoke: [§Aturan Logika Modul#r45, §9.2#b98, §9.6#r22, EB-FRM-5@target-add-override]
dependsOn: []
trace:
  §4.1#r305: [15, 16]
  §4.1#r306: 30
  §6#r10: 15
  §9.2#b97: [29, 33]
  §9.4.2#r115: [29, 33]
  §9.4.2#r116: 15
  §9.4.2#r118: [18, 33]
  §9.4.4#r21: [18, 32]
  §9.9#r21: 15
  §Aturan Logika Modul#r45: [46, 48, 49, 62, 64]
  §9.2#b98: 15
  §9.6#r22: 15
  EB-FRM-5@target-add-override: 15
anchor: [5]
coverage:
  web: automated
---

# Add override ditolak untuk override aktif yang duplikat

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-008-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-008-2: Group `Proyek Karawang {runId}`, Group tingkat atas, ada di entitas aktor.
  - DU-008-3: Group `Proyek Bekasi {runId}`, Group tingkat atas, ada di entitas aktor.
  - DU-008-4: override aktif untuk Group `Proyek Karawang {runId}`, transaksi `Borrow`, Category `Machinery {runId}`, dengan Overridden `Max duration (30 days)`.
  - Nilai yang dicoba dan ditolak: Group `Proyek Karawang {runId}` dengan `Max extensions` `2` di Category `Machinery {runId}` transaksi `Borrow` (DU-008-5); Group `Proyek Karawang {runId}` bersama `Proyek Bekasi {runId}` dengan `Max extensions` `2` di Category `Machinery {runId}` transaksi `Borrow` (DU-008-6).
  - Override yang dibuat spec ini dan bukan duplikat: Group `Proyek Karawang {runId}` dengan `Max duration` `45` di All categories transaksi `Borrow`, Overridden `Max duration (45 days)` (DU-008-7); Group `Proyek Karawang {runId}` dengan `Need recipient confirmation` `No` di Category `Machinery {runId}` transaksi `Assign`, Overridden `Need recipient confirmation (No)` (DU-008-8).
- Kondisi:
  - Category `Machinery {runId}` mewarisi seluruh field transaksi dari Company default (Inherit).

## Test Steps

### Target yang sudah punya override aktif ditolak dengan pesan di bawah Target
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
5. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (30 days)` tampil di tabel Overrides
6. Klik `[+ Override]`
7. Pilih Scope `Group`
8. Klik `[Select Group]`
9. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
10. Centang Group `Proyek Karawang {runId}`
11. Klik `[Select]`
12. Pilih Field `Max extensions`
13. Isi Value `2`
14. Klik `[Submit]`
15. Verifikasi pesan `An active override already exists for this target, category, and transaction. Delete it first` tampil di bawah Target
16. Verifikasi dialog `Add override - Borrow` tetap terbuka setelah Submit ditolak
17. Klik `✕` pada dialog, lalu klik `[Leave]` pada dialog Unsaved Changes
18. Verifikasi tabel Overrides hasil Search `{runId}` tetap memuat `1` baris

### Submit dengan satu target duplikat dan satu target lain ditolak seluruhnya
19. Klik `[+ Override]`
20. Pilih Scope `Group`
21. Klik `[Select Group]`
22. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
23. Centang Group `Proyek Karawang {runId}`
24. Centang Group `Proyek Bekasi {runId}`
25. Klik `[Select]`
26. Pilih Field `Max extensions`
27. Isi Value `2`
28. Klik `[Submit]`
29. Verifikasi pesan `An active override already exists for this target, category, and transaction. Delete it first` tampil di bawah Target
30. Verifikasi Group `Proyek Bekasi {runId}` tetap terpilih sebagai Target
31. Klik `✕` pada dialog, lalu klik `[Leave]` pada dialog Unsaved Changes
32. Verifikasi tabel Overrides hasil Search `{runId}` tetap memuat `1` baris
33. Verifikasi tidak ada baris dengan Target `Proyek Bekasi {runId}` di tabel Overrides

### Override untuk Category lain bukan duplikat
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
44. Isi Value `45`
45. Klik `[Submit]`
46. Verifikasi toast `Success, override has been added.` tampil untuk override All categories
47. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
48. Verifikasi baris override All categories dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (45 days)` tampil di tabel Overrides
49. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (30 days)` tampil di tabel Overrides

### Override untuk transaksi lain bukan duplikat
50. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
51. Klik node `Machinery {runId}` di Sidebar Category Tree
52. Klik tab `Assign`
53. Klik `[+ Override]`
54. Pilih Scope `Group`
55. Klik `[Select Group]`
56. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
57. Centang Group `Proyek Karawang {runId}`
58. Klik `[Select]`
59. Pilih Field `Need recipient confirmation`
60. Pilih Value `No`
61. Klik `[Submit]`
62. Verifikasi toast `Success, override has been added.` tampil untuk override pada tab `Assign`
63. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
64. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Need recipient confirmation (No)` tampil di tabel Overrides
