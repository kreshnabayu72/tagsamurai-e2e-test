---
id: TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager
title: "Hapus Photo / Damaged Photo lewat File Manager: foto tampil kosong pada node Missing Log, status record, status global aset, dan Damage Report tidak berubah"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceRules: ["MISS-LOGIC-10a", "MISS-LOGIC-10b", "MISS-LOGIC-10f", "EC-MIS-38", "F-MISS-03.k2"]
smoke: []
dependsOn: ["File Manager: Delete File", "Damaged: Damage Log"]
trace:
  "MISS-LOGIC-10a": [3, 8, 25]
  "MISS-LOGIC-10b": [18, 20, 29]
  "MISS-LOGIC-10f": [15, 18, 20, 23, 29, 31, 34, 35]
  "EC-MIS-38": [10, 11, 13, 14, 18, 20, 23, 29, 31, 34, 35]
  "F-MISS-03.k2": [18, 20, 23, 29, 31]
anchor: [22, 30]
coverage:
  web: automated
---

# Hapus Photo / Damaged Photo lewat File Manager: foto tampil kosong pada node Missing Log, status record, status global aset, dan Damage Report tidak berubah

## Prerequisites
- Mode: FE+BE.
- Aktor: Rina W, Total Control, Aktor Missing dan pemegang aksi Delete di File Manager.
- Layar awal: halaman Missing, sub-tab History.
- Sumber aturan: tidak ada TestCase untuk aturan ini; spec disusun langsung dari PRD `fixed-asset/missing/PRD/missing.md` (`MISS-LOGIC-10a`, `MISS-LOGIC-10b`, `MISS-LOGIC-10f`, `EC-MIS-38`, `F-MISS-03.k2`) dan dialog Delete dari `fixed-asset/file-manager/PRD/file-manager.md` (`FAFM-LOGIC-02`, `D-01`, `T-01`); `sourceRules` memuat ID aturan Missing langsung.
- Data:
  - DU-048-1: Record Found `Camera DSLR Canon R6 {runId}`, aset tanpa TAG, Group `Finance Room`, Source `Manual`, dengan node `Marked as found by Rina W` memuat Found at `Finance Room`, Asset Status `Normal`, Note `Ditemukan di rak server lantai 2`, dan Photo `foto-ditemukan.png` (Source File Manager `Found Photo`).
  - DU-048-2: Record Found `Laptop Dell Latitude 5420 {runId}`, aset tanpa TAG, Group `Finance Room`, Source `Manual`, dengan node `Marked as found by Rina W` memuat Asset Status `Damaged`, Note `Layar retak dan engsel patah saat ditemukan`, dan Damaged Photo `foto-kerusakan-laptop.png` (Source File Manager `Damaged Photo`), serta satu Damage Report dengan Source `Missing Asset`.
  - Kedua berkas diunggah lewat Mark as Found sebelum spec berjalan, dan tidak ada record Missing lain untuk kedua aset.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - Spec ini menghapus berkas uji; data DU-048-1 dan DU-048-2 dibuat ulang per run.

## Test Steps

### Foto tampil pada node sebelum dihapus
1. Ketik Search `{runId}`, tekan Enter
2. Klik nama `Camera DSLR Canon R6 {runId}` pada kolom Name
3. Verifikasi node `Marked as found by Rina W` memuat Photo `foto-ditemukan.png`
4. Verifikasi badge status record `Found` tampil
5. Klik `✕` pada dialog Missing Log
6. Buka halaman `Settings > File Manager`
7. Ketik Search `foto-ditemukan.png`, tekan Enter
8. Verifikasi baris `foto-ditemukan.png` tampil dengan Source `Found Photo` dan Asset `Camera DSLR Canon R6 {runId}`

### Hapus Photo lewat File Manager tidak diblokir
9. Klik `⋯` pada baris `foto-ditemukan.png`
10. Verifikasi aksi `Delete` tampil dan Enabled
11. Klik `Delete`
12. Verifikasi dialog `Delete File` memuat `The file will be removed from the record that uses it and moved to the recycle bin.`
13. Klik `[Delete]` pada dialog
14. Verifikasi toast `Success, foto-ditemukan.png has been deleted.` tampil
15. Verifikasi baris `foto-ditemukan.png` tidak tampil lagi pada tab Files

### Node Missing Log menampilkan foto kosong, status record tidak berubah
16. Buka halaman `Assets`, klik tab `Missing`, klik sub-tab `History`
17. Ketik Search `Camera DSLR Canon R6 {runId}`, tekan Enter
18. Verifikasi Status baris `Camera DSLR Canon R6 {runId}` tetap `Found`
19. Klik nama `Camera DSLR Canon R6 {runId}` pada kolom Name
20. Verifikasi badge status record `Found` tampil
21. Verifikasi node `Marked as found by Rina W` memuat Found at `Finance Room`
22. Verifikasi node `Marked as found by Rina W` memuat Asset Status `Normal` dan Note `Ditemukan di rak server lantai 2`
23. Verifikasi node `Marked as found by Rina W` tidak menampilkan baris Photo
24. Klik `✕` pada dialog Missing Log

### Damaged Photo dihapus: Damage Report dan status aset tidak berubah
25. Buka halaman `Settings > File Manager`, ketik Search `foto-kerusakan-laptop.png`, tekan Enter
26. Klik `⋯` pada baris `foto-kerusakan-laptop.png`, klik `Delete`, lalu klik `[Delete]` pada dialog `Delete File`
27. Verifikasi toast `Success, foto-kerusakan-laptop.png has been deleted.` tampil
28. Buka halaman `Assets`, klik tab `Missing`, klik sub-tab `History`, ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter, lalu klik nama `Laptop Dell Latitude 5420 {runId}` pada kolom Name
29. Verifikasi badge status record `Found` tampil
30. Verifikasi node `Marked as found by Rina W` memuat Asset Status `Damaged` dan Note `Layar retak dan engsel patah saat ditemukan`
31. Verifikasi node `Marked as found by Rina W` tidak menampilkan baris Damaged Photo
32. Klik `✕` pada dialog Missing Log
33. Buka Damage Log milik aset `Laptop Dell Latitude 5420 {runId}`
34. Verifikasi Damage Report dengan Source `Missing Asset` tetap tampil di Damage Log
35. Verifikasi Asset Status `Laptop Dell Latitude 5420 {runId}` tetap `Damaged`

## Notes
- Aturan tidak punya TestCase sumber. Keterlacakan lewat ID aturan PRD `missing.md` (§1.2 `MISS-LOGIC-10a`, `10b`, `10f`; §9.4.4 `EC-MIS-38`; `F-MISS-03.k2`); halaman coverage dan inventaris unit perlu dibangkitkan ulang agar memuat ID ini.
- Dialog `Delete File` dan toast `Success, [File Name] has been deleted.` dikutip dari `file-manager.md` (`D-01`, `T-01`), milik modul File Manager; spec ini hanya memakainya sebagai pemicu.
- Kolom Source dan Asset pada tab Files mengikuti `file-manager.md` §4.2d (Source `Found Photo` dan `Damaged Photo`).
- Efek ke Damage record yang ditahan (asal `Damaged + Missing`, node `MISS-LOGIC-06p`) pada sisi Damaged tidak diasersi di sini; milik modul `damaged/`.
- Kewajiban Damaged Photo (`FLD-06`) hanya dievaluasi saat Submit, tidak saat membaca record, sehingga membuka Missing Log sesudah penghapusan tidak menampilkan error validasi.
