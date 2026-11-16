---
id: TC-FA-PREF-E2E-147-deferred-default-capitalization-offset-prompt-kapitalisasi-pertama-pengisian-dan-log-l-03
title: "[DEFERRED] Default Capitalization Offset: prompt kapitalisasi pertama, pengisian, dan log L-03"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-471
  - TC-FA-PREF-472
  - TC-FA-PREF-473
  - TC-FA-PREF-474
  - TC-FA-PREF-475
sourceRules: ["FAPREF-LOGIC-08c", "§Aturan Logika Modul#b1", "F-FAPREF-05.k1b", "L-03a", "§4.1.4#r8", "L-03b", "§8.2#p2", "L-03c", "L-02d", "§8.4#p3", "§4.1.1#p1"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-08c": 3
  "§Aturan Logika Modul#b1": 7
  "F-FAPREF-05.k1b": 10
  "L-03a": 16
  "§4.1.4#r8": 17
  "L-03b": [23, 24]
  "§8.2#p2": 24
  "L-03c": [26, 27]
  "L-02d": 27
  "§8.4#p3": [33, 34]
  "§4.1.1#p1": 36
anchor: [8]
coverage:
  web: automated
---

# [DEFERRED] Default Capitalization Offset: prompt kapitalisasi pertama, pengisian, dan log L-03

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor pertama: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Pelaku kapitalisasi kedua (TC-FA-PREF-473 dan 474, hanya memicu perubahan state lewat sesi API): Budi Santoso (PC-8: Manage accounting - Read + Update, tampil "Budi S") `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MARU_PASSWORD`. Email akun Budi Santoso tidak tertulis eksplisit di Pre-setup TC; spec memakai pola email role Manage accounting - Read + Update (perlu dikonfirmasi tim FE; lihat Temuan untuk QA). Sesi API aktor mengikuti butir "Sesi API aktor" di `suite.md`.
- Akun TC-FA-PREF-475 (login UI lewat ganti akun): Manage accounting - Read `manageAccountingRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MAR_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env `FA_TC_PASSWORD`, `FA_MARU_PASSWORD`, dan `FA_MAR_PASSWORD` mengikuti nama yang dipakai spec lain di suite (satu nama satu arti); perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5 (`1-2900 – Biaya Dikapitalisasi`); Asset Class IT Equipment; aset 'transfer - 31' siap dikapitalisasi tanpa dokumen sumber (PC-16); Default Capitalization Offset tersimpan kosong. Data modul kapitalisasi disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan aset; kapitalisasi lewat UI modul kapitalisasi (permintaan akun Capitalization Offset) dan lewat sesi API; kemampuan baca BE jumlah baris Changelog Preferences, jumlah entri System Log Budi Santoso, dan jumlah entri Activity Log FAMS (baseline, bagian 8b butir 10).
- State global yang diubah: Default Capitalization Offset company dan status kapitalisasi aset 'transfer - 31'; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah). Entri Changelog, System Log, dan Activity Log yang tercipta bersifat permanen dan tidak dipulihkan.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-471: Kapitalisasi pertama tanpa dokumen sumber meminta akun Capitalization Offset

1. Seed Default Capitalization Offset tersimpan kosong dan aset 'transfer - 31' kelas IT Equipment siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
2. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' di modul kapitalisasi
3. Verifikasi FAMS meminta akun Capitalization Offset pada kapitalisasi itu

### TC-FA-PREF-472: Akun yang dipilih pada kapitalisasi pertama mengisi Default Capitalization Offset

4. Seed Default Capitalization Offset tersimpan kosong dan aset 'transfer - 31' kelas IT Equipment siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
5. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' di modul kapitalisasi
6. Pilih akun "1-2900 – Biaya Dikapitalisasi" pada permintaan akun Capitalization Offset dan konfirmasi
7. Verifikasi tidak ada dialog Save Changes yang tampil pada proses pengisian
8. Verifikasi kapitalisasi berjalan
9. Buka Fixed Asset > Settings > Accounting > Preferences
10. Verifikasi Select Default Capitalization Offset menampilkan "1-2900 – Biaya Dikapitalisasi"

### TC-FA-PREF-473 dan TC-FA-PREF-474: Pengisian Offset dari kapitalisasi menulis L-03 di Changelog, System Log, dan Activity Log

11. Seed Default Capitalization Offset tersimpan kosong dan aset 'transfer - 31' kelas IT Equipment siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
12. Catat jumlah baris Changelog Preferences, jumlah entri System Log Budi Santoso, dan jumlah entri Activity Log FAMS lewat kemampuan baca BE (baseline)
13. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' sebagai Budi Santoso lewat sesi API, pilih akun "1-2900 – Biaya Dikapitalisasi" dan konfirmasi, hingga kapitalisasi dan pengisian Offset tersimpan
14. Buka Fixed Asset > Settings > Accounting > Preferences
15. Klik ikon View history
16. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari baseline langkah 12
17. Verifikasi baris baru pada modal Changelog: Preferences: Action = Edit, Section = Chart of Accounts, Field = Default Capitalization Offset, Old Value = —, New Value = 1-2900 – Biaya Dikapitalisasi, Modified By = Budi S
18. Klik ikon [✕] di header modal Changelog
19. Buka Global Settings > User
20. Ketik Search "manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net", tekan Enter
21. Klik Name "Budi Santoso" untuk membuka Detail user
22. Klik Tab System Log
23. Verifikasi jumlah entri System Log Budi Santoso bertambah tepat 1 dari baseline langkah 12
24. Verifikasi entri baru System Log Budi Santoso: Action = Edit, Object = Preferences, Name = —, Field = Default Capitalization Offset, Old Value = —, New Value = 1-2900 – Biaya Dikapitalisasi
25. Buka Activity Log FAMS
26. Verifikasi jumlah entri Activity Log FAMS bertambah tepat 1 dari baseline langkah 12
27. Verifikasi entri baru Activity Log FAMS: Object = Preferences, Name = —, Field = Default Capitalization Offset, Old Value = —, New Value = 1-2900 – Biaya Dikapitalisasi, Modified By = Budi S

### TC-FA-PREF-475: Pengisian Offset lewat kapitalisasi tidak membutuhkan izin Update pada Preferences

28. Seed Default Capitalization Offset tersimpan kosong dan aset 'transfer - 31' kelas IT Equipment siap dikapitalisasi tanpa dokumen sumber, dengan akun Manage accounting - Read berizin melakukan kapitalisasi, hingga tersimpan
29. Ganti akun: klik Logout
30. Ganti akun: login sebagai Manage accounting - Read (`Spectra.env.FA_MAR_PASSWORD`)
31. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' di modul kapitalisasi
32. Pilih akun "1-2900 – Biaya Dikapitalisasi" pada permintaan akun Capitalization Offset dan konfirmasi
33. Verifikasi kapitalisasi berjalan
34. Verifikasi pengisian akun tidak ditolak
35. Buka Fixed Asset > Settings > Accounting > Preferences
36. Verifikasi Select Default Capitalization Offset menampilkan "1-2900 – Biaya Dikapitalisasi" dalam keadaan Disabled
37. Pulihkan Default Capitalization Offset ke kosong dan status kapitalisasi aset 'transfer - 31' ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 9, 14, 35 (membuka layar Preferences), langkah 18 (menutup modal Changelog sebelum berpindah surface), langkah 19 dan 25 (berpindah ke User dan Activity Log), langkah 20 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23; Search email bersuffix tidak diperlukan karena akun Pre-setup), langkah 29 dan 30 (ganti akun eksplisit; sesi dikembalikan ke akun default oleh hook `after`, S-07), langkah 37 (pemulihan state, S-09, R-08).
- Urutan asersi TC-FA-PREF-472 mengikuti urutan state (bagian 8b butir 5, 11): Expected c (tidak ada dialog Save Changes pada proses pengisian) ditulis sebelum Expected a dan b. Asersi absence dialog pada langkah 7 diletakkan tepat sesudah pemicu (konfirmasi pada langkah 6); pemicu itu menjadi anchor positif yang buktinya menyusul pada Verifikasi artefak (langkah 8 dan 10), sesuai bagian 8b butir 11.
- TC-FA-PREF-473 dan 474 memakai precondition dan pemicu yang sama (kapitalisasi oleh Budi Santoso lewat sesi API, R-20) sehingga satu pemicu dibaca di tiga surface (Changelog, System Log, Activity Log); baseline ketiga surface dicatat satu kali sebelum pemicu (langkah 12, S-12). Langkah 13 adalah pemicu pelaku kedua lewat sesi API (bagian 3 P-2 2026-10-30): tidak butuh butir `P-2`.
- Langkah 11 sampai 27 memakai satu kapitalisasi untuk dua TC; langkah 16 dan 17 milik TC-FA-PREF-473, langkah 23 sampai 27 milik TC-FA-PREF-474.
- Spec melewati sekitar 35 langkah (37 langkah). Alasan: seluruh blok satu kelas harness (fungsional, modul pemilik kapitalisasi) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-PREF-473 dan 474 menyebut Precondition a "Login sbg Role: Total Control" sedangkan pelaku kapitalisasi adalah Budi Santoso (Manage accounting - Read + Update); spec memakai Total Control sebagai pembaca dan sesi API Budi sebagai pemicu. Email akun Budi Santoso tidak tertulis eksplisit di Pre-setup TC.
  - TC-FA-PREF-474 langkah TC "Buka Global Settings > User > Detail > Tab System Log milik Budi Santoso" tidak menyebut cara menemukan user; spec memakai Search email akun Pre-setup (langkah penghubung).
  - TC-FA-PREF-473 dan 474 Expected menyebut "1 baris baru" tanpa baseline; spec mencatat baseline (S-12) dan mengasersi selisih 1 sebelum isi baris.
  - TC-FA-PREF-471 tidak menyebut bentuk permintaan akun (dialog, popup); spec memakai teks Expected apa adanya.
  - TC-FA-PREF-472 Post Condition ("Default Capitalization Offset tersimpan 1-2900") diasersi lewat Expected b; Post Condition TC-FA-PREF-473, 474, dan 475 adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
  - TC-FA-PREF-475 Expected a memuat dua klausa ("Kapitalisasi berjalan", "pengisian akun tidak ditolak") dan ditulis dua `Verifikasi` (langkah 33 dan 34, S-01).
