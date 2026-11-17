---
id: TC-FA-PREF-E2E-088-absence-log-save-ditolak-cancel-dialog-save-changes-dan-j-01-tanpa-aktor-tidak-menulis-log
title: "Absence Log: Save Ditolak Server, Cancel pada Dialog Save Changes, dan J-01 Tanpa User Aktor Tidak Menulis Log"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-386
  - TC-FA-PREF-387
  - TC-FA-PREF-427
sourceRules: ["D-01", "PV-04", "PV-05", "V-09", "F-FAPREF-01.k19b", "F-FAPREF-01.k19d", "F-FAPREF-01.k19a", "RG-02", "PV-01", "F-FAPREF-01.k21c", "FAPREF-LOGIC-03e", "R-03", "J-01", "L-01a", "L-01c"]
smoke: []
dependsOn: []
trace:
  "D-01": [5, 17]
  "PV-04": 5
  "PV-05": 5
  "V-09": 7
  "F-FAPREF-01.k19b": 7
  "F-FAPREF-01.k19d": 8
  "F-FAPREF-01.k19a": [9, 10, 11]
  "RG-02": [9, 10, 11]
  "PV-01": 17
  "F-FAPREF-01.k21c": [19, 21]
  "FAPREF-LOGIC-03e": 21
  "R-03": [22, 23, 24]
  "J-01": 31
  "L-01a": 31
  "L-01c": [37, 42]
anchor: [20]
coverage:
  web: automated
---

# Absence Log: Save Ditolak Server, Cancel pada Dialog Save Changes, dan J-01 Tanpa User Aktor Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Kelas harness: g (asersi absence log). Pemicu (Save yang ditolak server, Cancel pada dialog, dan job rekonsiliasi J-01 sebagai proses latar) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Akun Budi Santoso (Pre-setup PC-8, Manage accounting - Read + Update, tampil "Budi S") hanya dibaca System Log-nya pada TC-FA-PREF-427.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Pengecualian TC-FA-PREF-427: sesudah langkah 26 company tidak memiliki baris Preferences sehingga halaman Preferences baru dapat dibuka setelah job J-01 selesai (langkah 29).
- Data Pre-setup: Preferences nilai awal PC-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date; periode Mar 2026 sampai Dec 2026 Open; belum ada posting penyusutan); TC-FA-PREF-386: Tax Depreciation Class memiliki versi kedua dengan Effective From (PC-3); TC-FA-PREF-387: Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6, hasil dampak "2 asset classes use the default threshold."); TC-FA-PREF-427: company dengan modul akuntansi aktif tanpa baris Preferences (PC-13, PC-16). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang dilakukan lewat langkah penghubung (langkah 1, 13, dan 26).
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "13 accounting periods will be rebuilt."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): kemampuan baca BE jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline sebelum aksi, bagian 8b butir 10 dan S-12); seed company tanpa baris Preferences; pemicu manual job rekonsiliasi J-01 oleh tim BE atau lewat penjadwal platform. TC-FA-PREF-427 adalah TC `[DEFERRED]` (NC-08): modul pemilik aktivasi dan job J-01 belum disusun, disediakan tim FE setelah modul tersedia.
- State yang diubah spec: Preferences company (dipulihkan ke nilai awal pada langkah 12 dan 25 dan di hook `after`, tetap jalan bila spec gagal di tengah); baris Preferences company yang dibuat J-01 pada langkah 28 dihapus lewat seed pemulihan di hook `after`.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-386: Save yang ditolak server karena versi Tax Depreciation Class tidak menulis log

1. Seed Preferences nilai awal PC-1 dengan Tax Depreciation Class memiliki versi kedua ber-Effective From (PC-3) hingga tersimpan
2. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
3. Pilih "April" pada Select Fiscal Year Start
4. Klik [Save changes]
5. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "13 accounting periods will be rebuilt." dan "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
6. Klik [Save] pada dialog Save Changes
7. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada field Fiscal Year Start
8. Verifikasi dialog Save Changes tertutup
9. Verifikasi jumlah baris Changelog sama dengan baseline langkah 2
10. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 2
11. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 2
12. Kembalikan Select Fiscal Year Start ke "January"

### TC-FA-PREF-387: Klik Cancel pada dialog Save Changes tidak menulis log

13. Seed ulang Preferences ke nilai awal PC-1 (Asset Class PC-6) hingga tersimpan
14. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
15. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
16. Klik [Save changes]
17. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
18. Klik [Cancel] pada dialog Save Changes
19. Verifikasi dialog Save Changes tertutup
20. Verifikasi tidak ada toast
21. Verifikasi form memuat nilai Rp 10.000.000,00 yang belum disimpan
22. Verifikasi jumlah baris Changelog sama dengan baseline langkah 14
23. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 14
24. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 14
25. Kembalikan CurrencyInput Default Capitalization Threshold ke 5000000

### TC-FA-PREF-427: [DEFERRED] J-01 tidak menulis System Log karena tidak ada user aktor

26. Seed company tanpa baris Preferences dengan modul akuntansi aktif (PC-13) hingga tersimpan
27. Catat jumlah baris System Log milik Rina Anggraini dan milik Budi Santoso (baseline)
28. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE)
29. Muat ulang halaman Preferences setiap 5 detik hingga Form Preferences tampil (batas tunggu 2 menit)
30. Klik ikon View history
31. Verifikasi modal Changelog: Preferences memuat 1 baris Action = Create
32. Klik ikon [✕] di header modal Changelog
33. Buka Global Settings > User
34. Ketik Search "Rina Anggraini", tekan Enter
35. Klik Name "Rina Anggraini"
36. Klik Tab "System Log"
37. Verifikasi jumlah baris System Log milik Rina Anggraini sama dengan baseline langkah 27
38. Buka Global Settings > User
39. Ketik Search "Budi Santoso", tekan Enter
40. Klik Name "Budi Santoso"
41. Klik Tab "System Log"
42. Verifikasi jumlah baris System Log milik Budi Santoso sama dengan baseline langkah 27

## Notes

- P-5: spec ini adalah spec absence (kelas g); Save yang ditolak server (TC-FA-PREF-386), Cancel pada dialog (TC-FA-PREF-387), dan job J-01 sebagai proses latar (TC-FA-PREF-427) hanya memicu kondisi yang diasersi tidak tercatat; tiap TC punya baseline sendiri (S-12, S-05).
- Langkah penghubung (S-03, S-09): langkah 1, 13, dan 26 (seed ulang), langkah 12 dan 25 (mengembalikan form dirty ke nilai tersimpan, tanpa Verifikasi), langkah 32 (menutup modal). Langkah 34 dan 39 (Search nama user) membuka baris target pada tabel yang dapat memuat lebih dari satu halaman (R-16, bagian 8b butir 12); langkah 33 dan 38 kembali ke tabel penuh sebelum Search berikutnya (S-09, S-14).
- Absence pada langkah 9 sampai 11, 20, 22 sampai 24, 37, dan 42 memakai baseline yang dicatat (langkah 2, 14, 27) sebagai anchor positif (bagian 8b butir 2). Langkah 20 (tidak ada toast) diletakkan segera setelah pemicu pada langkah 18 dan 19 (bagian 8b butir 11).
- Langkah 33 sampai 42 membuka System Log lewat UI saat jam server dan browser masih diatur (dipulihkan di hook `after`); asersinya jumlah baris dibanding baseline, tidak sensitif terhadap jam (jam digeser mundur, bukan dimajukan), S-09 [KEPUTUSAN 2026-10-13]; langkah tidak disusun ulang.
- Spec ini melewati sekitar 35 langkah (42 langkah nominal) karena tiga blok berdiri sendiri, semuanya kelas g dengan baseline dan seed pemulihan sendiri, dan 8 langkah di antaranya adalah pembacaan System Log dua user pada TC-FA-PREF-427 (blok baca-log berpola, bagian 3 prinsip 13 smell); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-PREF-427 precondition b ("User berada di Settings > Accounting > Preferences") dan precondition c ("belum memiliki baris Preferences") tidak dapat benar bersamaan karena company tanpa baris Preferences ditolak server (TC-FA-PREF-562); spec memuat Preferences setelah J-01 selesai. PC-16 menyebut "Company tanpa aktivasi modul akuntansi" sedangkan precondition c menyebut modul akuntansi sudah aktif.
  - TC-FA-PREF-427 berstatus "Manual Only - (c)" (pemicu hanya lewat penjadwal atau kegagalan sisi server); spec ditulis lengkap dengan pemicu J-01 sebagai kemampuan tim BE (bagian 2).
  - TC-FA-PREF-427 langkah 3 hanya menyebut "System Log milik Rina Anggraini dan Budi Santoso" tanpa menyebut jalur navigasi; spec memakai Global Settings > User > Detail > Tab System Log mengikuti Expected TC.
  - TC-FA-PREF-386 dan 387 Post Condition butir b ("Tidak ada entri log baru di tiga surface") dicakup oleh Expected c (jumlah baris tiga surface). TC-FA-PREF-386 Post Condition butir a ("Fiscal Year Start tersimpan tetap January") tidak punya langkah observasi di TC dan tidak diasersi terpisah; TC-FA-PREF-387 Post Condition butir a ("threshold tersimpan tetap 5.000.000") demikian pula.
  - TC-FA-PREF-386 langkah 4 ("Amati field Fiscal Year Start") tidak menyebut nilai field setelah dialog tertutup; spec hanya mengasersi caption dan dialog tertutup sesuai Expected b.
  - TC-FA-PREF-386 dan 387 memakai Tax Depreciation Class dan Asset Class seri PC (PC-3, PC-6); TC-FA-PREF-427 memakai seri PC-13 dan PC-16; spec men-seed ulang di antara blok.
