---
id: TC-FA-PREF-E2E-072-d03-posting-pertama-setelah-dialog-save-changes
title: "D-03: Posting Penyusutan Pertama Setelah Dialog Save Changes Terbuka pada Fiscal Year Start dan First Accounting Period"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-557
  - TC-FA-PREF-558
coverage:
  web: automated
---

# D-03: Posting Penyusutan Pertama Setelah Dialog Save Changes Terbuka pada Fiscal Year Start dan First Accounting Period

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control "Rina Anggraini" (Pre-setup PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Pelaku kedua (hanya memicu perubahan state): Total Control kedua (Pre-setup PC-8) lewat sesi API, password `Spectra.env.FA_PREF_TC2_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Sesi API aktor: lihat butir "Sesi API aktor" di `suite.md`.
- Env var `FA_TC_PASSWORD` dan `FA_PREF_TC2_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PC-1 (Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, belum ada posting penyusutan, periode Mar 2026 sampai Dec 2026 Open). Asset Class `IT Equipment` (PC-6) menjadi tempat Last Posted Period terisi.
- Data Dinamis DC-8: posting penyusutan pertama yang dibuat pelaku kedua saat dialog Save Changes terbuka (Last Posted Period Apr 2026 pada `IT Equipment`).
- Kemampuan teknis: aksi fixture BE "posting penyusutan pertama" (Depreciation Run belum disusun) dan kemampuan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (surface audit trail permanen; N dibaca sebelum aksi, bagian 8b butir 10). Keduanya disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec mengubah state BE (posting penyusutan pertama membuat Fiscal Year Start dan First Accounting Period terkunci); pemulihan ke PC-1 dilakukan di langkah 18 dan di hook `after` spec ini.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-557: Posting penyusutan pertama saat dialog Save Changes terbuka membuat Save Fiscal Year Start menampilkan dialog blok

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
2. Pilih "April" pada Select Fiscal Year Start
3. Klik [Save changes]
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "13 accounting periods will be rebuilt." dan "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
5. Sesi API Total Control kedua: lakukan posting penyusutan pertama hingga Asset Class `IT Equipment` memiliki Last Posted Period Apr 2026 tersimpan
6. Klik [Save] pada dialog Save Changes
7. Verifikasi dialog "Cannot Save Preferences" tampil dengan body "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status." dan tombol [OK]
8. Verifikasi tidak ada toast tambahan
9. Klik [OK]
10. Verifikasi halaman dimuat ulang dari nilai tersimpan dan perubahan yang belum disimpan dibuang: Select Fiscal Year Start menampilkan "January"
11. Arahkan kursor ke ikon gembok Fiscal Year Start
12. Verifikasi Fiscal Year Start tampil Disabled dengan ikon gembok dan tooltip kunci
13. Arahkan kursor ke ikon gembok First Accounting Period
14. Verifikasi First Accounting Period tampil Disabled dengan ikon gembok dan tooltip kunci
15. Verifikasi tidak ada yang tersimpan: Fiscal Year Start tersimpan "January" dan First Accounting Period tersimpan "Mar 2026"
16. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
17. Verifikasi jumlah baris Changelog, System Log, dan Activity Log sama dengan jumlah awal (tidak ada baris log baru)
18. Seed ulang Preferences ke PC-1 (fixture BE; posting penyusutan pertama dibatalkan) dan buka kembali Fixed Asset > Settings > Accounting > Preferences

### TC-FA-PREF-558: Posting penyusutan pertama saat dialog Save Changes terbuka membuat Save First Accounting Period menampilkan dialog blok

19. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
20. Pilih bulan "January" dan tahun "2026" pada Select First Accounting Period
21. Klik [Save changes]
22. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "12 accounting periods will be rebuilt." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
23. Sesi API Total Control kedua: lakukan posting penyusutan pertama hingga Asset Class `IT Equipment` memiliki Last Posted Period Apr 2026 tersimpan
24. Klik [Save] pada dialog Save Changes
25. Verifikasi dialog "Cannot Save Preferences" tampil dengan body "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status." dan tombol [OK]
26. Verifikasi tidak ada toast tambahan
27. Klik [OK]
28. Verifikasi halaman dimuat ulang dari nilai tersimpan dan perubahan yang belum disimpan dibuang: Select First Accounting Period menampilkan "Mar 2026"
29. Arahkan kursor ke ikon gembok Fiscal Year Start
30. Verifikasi Fiscal Year Start tampil Disabled dengan ikon gembok dan tooltip kunci
31. Arahkan kursor ke ikon gembok First Accounting Period
32. Verifikasi First Accounting Period tampil Disabled dengan ikon gembok dan tooltip kunci
33. Verifikasi tidak ada yang tersimpan: Fiscal Year Start tersimpan "January" dan First Accounting Period tersimpan "Mar 2026"
34. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
35. Verifikasi jumlah baris Changelog, System Log, dan Activity Log sama dengan jumlah awal (tidak ada baris log baru)

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 9 dan 27 (menutup dialog hasil, aksi TC), langkah 18 (seed ulang dan buka kembali halaman agar TC berikutnya mulai dari PC-1 tanpa kunci). Pemulihan akhir state BE setelah langkah 35 dilakukan hook `after` (R-08).
- Baseline jumlah log (langkah 1, 16, 19, 34) mengikuti S-12: dicatat sebelum aksi pemicu tiap TC dan dipakai untuk asersi jumlah. Asersi jumlah bukan kelas g (bagian 3 prinsip 13).
- Pelaku kedua (langkah 5 dan 23) memakai sesi API Total Control kedua hanya untuk memicu perubahan state; bukan konteks kedua kelas c (bagian 3 P-2, keputusan 2026-10-30).
- Urutan langkah mengikuti urutan state (8b butir 5): dialog Save Changes diasersi sebelum pemicu posting.
- Temuan untuk QA:
  - TC-FA-PREF-557 dan 558 bertanda `Manual Only - (d) butuh dua sesi pengguna paralel` di kolom Automation, sementara DC-7 dan DC-8 menyebut "hanya untuk eksekusi manual". Spec memakai pelaku kedua lewat sesi API/fixture BE agar otomatis; kemampuan "posting penyusutan pertama" perlu dikonfirmasi tim FE/BE.
  - Teks tooltip kunci pada Fiscal Year Start dan First Accounting Period tidak tertulis di TC; spec hanya memverifikasi tooltip kunci tampil.
  - Precondition TC-FA-PREF-557 dan 558 tidak menyebut pencatatan jumlah baris log, padahal Expected butir e meminta "tidak ada baris log baru"; spec menambah pencatatan baseline (S-12).
  - Email Total Control kedua (Pre-setup PC-8) tidak tertulis di TC; perlu dikonfirmasi tim FE.
  - Post Condition kedua TC ("Fiscal Year Start tersimpan January dan First Accounting Period tersimpan Mar 2026") dicakup Expected butir e dan diasersi pada langkah 15 dan 33.
