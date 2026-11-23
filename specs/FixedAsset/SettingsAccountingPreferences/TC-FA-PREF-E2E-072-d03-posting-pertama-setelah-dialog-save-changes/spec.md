---
id: TC-FA-PREF-E2E-072-d03-posting-pertama-setelah-dialog-save-changes
title: "D-03: Posting Penyusutan Pertama Setelah Dialog Save Changes Terbuka pada Fiscal Year Start dan First Accounting Period"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-557
  - TC-FA-PREF-558
sourceRules: ["D-01", "PV-04", "PV-05", "D-03", "E-FAPREF-06", "ST-27", "F-FAPREF-01.k6d", "ST-05", "F-FAPREF-01.k6b", "§Resolved#r5"]
smoke: []
dependsOn: []
trace:
  "D-01": [4, 24]
  "PV-04": [4, 24]
  "PV-05": 4
  "D-03": [7, 27]
  "E-FAPREF-06": [7, 27]
  "ST-27": [8, 28]
  "F-FAPREF-01.k6d": [10, 30]
  "ST-05": [12, 13, 15, 16, 32, 33, 35, 36]
  "F-FAPREF-01.k6b": [17, 19, 37, 39]
  "§Resolved#r5": [19, 39]
coverage:
  web: automated
---

# D-03: Posting Penyusutan Pertama Setelah Dialog Save Changes Terbuka pada Fiscal Year Start dan First Accounting Period

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control "Rina Anggraini" (Pre-setup PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Pelaku kedua (hanya memicu perubahan state): Total Control kedua (Pre-setup PC-8) lewat sesi API, password `Spectra.env.FA_PREF_TC2_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Sesi API aktor: lihat butir "Sesi API aktor" di `suite.md`.
- Env var `FA_TC_PASSWORD` dan `FA_PREF_TC2_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PC-1 (Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, belum ada Run Posted). Asset Class `IT Equipment` (PC-6) menjadi tempat Last Posted Period terisi.
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "The period calendar will have 13 accounting periods." (TC-557) dan "The period calendar will have 12 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Data Dinamis DC-8: posting penyusutan pertama yang dibuat pelaku kedua saat dialog Save Changes terbuka (Last Posted Period Apr 2026 pada `IT Equipment`).
- Kemampuan teknis: aksi fixture BE "posting penyusutan pertama" (Depreciation Run belum disusun) dan kemampuan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (surface audit trail permanen; N dibaca sebelum aksi, bagian 8b butir 10). Keduanya disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec mengubah state BE (posting penyusutan pertama membuat Fiscal Year Start dan First Accounting Period terkunci); pemulihan ke PC-1 dilakukan di langkah 20 dan di hook `after` spec ini.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-557: Posting penyusutan pertama saat dialog Save Changes terbuka membuat Save Fiscal Year Start menampilkan dialog blok

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
2. Pilih "April" pada Select Fiscal Year Start
3. Klik [Save changes]
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "The period calendar will have 13 accounting periods." dan "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
5. Sesi API Total Control kedua: lakukan posting penyusutan pertama hingga Asset Class `IT Equipment` memiliki Last Posted Period Apr 2026 tersimpan
6. Klik [Save] pada dialog Save Changes
7. Verifikasi dialog "Cannot Save Preferences" tampil dengan body "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted. The page has been reloaded with the latest lock status." dan tombol [OK]
8. Verifikasi tidak ada toast tambahan
9. Klik [OK]
10. Verifikasi halaman dimuat ulang dari nilai tersimpan dan perubahan yang belum disimpan dibuang: Select Fiscal Year Start menampilkan "January"
11. Arahkan kursor ke ikon gembok Fiscal Year Start
12. Verifikasi Fiscal Year Start tampil Disabled dengan ikon gembok
13. Verifikasi tooltip kunci tampil pada ikon gembok Fiscal Year Start
14. Arahkan kursor ke ikon gembok First Accounting Period
15. Verifikasi First Accounting Period tampil Disabled dengan ikon gembok
16. Verifikasi tooltip kunci tampil pada ikon gembok First Accounting Period
17. Verifikasi tidak ada yang tersimpan: Fiscal Year Start tersimpan "January" dan First Accounting Period tersimpan "Mar 2026"
18. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
19. Verifikasi jumlah baris Changelog, System Log, dan Activity Log sama dengan jumlah awal (tidak ada baris log baru)
20. Seed ulang Preferences ke PC-1 (fixture BE; posting penyusutan pertama dibatalkan) dan buka kembali Fixed Asset > Settings > Accounting > Preferences

### TC-FA-PREF-558: Posting penyusutan pertama saat dialog Save Changes terbuka membuat Save First Accounting Period menampilkan dialog blok

21. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
22. Pilih bulan "January" dan tahun "2026" pada Select First Accounting Period
23. Klik [Save changes]
24. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "The period calendar will have 12 accounting periods." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
25. Sesi API Total Control kedua: lakukan posting penyusutan pertama hingga Asset Class `IT Equipment` memiliki Last Posted Period Apr 2026 tersimpan
26. Klik [Save] pada dialog Save Changes
27. Verifikasi dialog "Cannot Save Preferences" tampil dengan body "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted. The page has been reloaded with the latest lock status." dan tombol [OK]
28. Verifikasi tidak ada toast tambahan
29. Klik [OK]
30. Verifikasi halaman dimuat ulang dari nilai tersimpan dan perubahan yang belum disimpan dibuang: Select First Accounting Period menampilkan "Mar 2026"
31. Arahkan kursor ke ikon gembok Fiscal Year Start
32. Verifikasi Fiscal Year Start tampil Disabled dengan ikon gembok
33. Verifikasi tooltip kunci tampil pada ikon gembok Fiscal Year Start
34. Arahkan kursor ke ikon gembok First Accounting Period
35. Verifikasi First Accounting Period tampil Disabled dengan ikon gembok
36. Verifikasi tooltip kunci tampil pada ikon gembok First Accounting Period
37. Verifikasi tidak ada yang tersimpan: Fiscal Year Start tersimpan "January" dan First Accounting Period tersimpan "Mar 2026"
38. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
39. Verifikasi jumlah baris Changelog, System Log, dan Activity Log sama dengan jumlah awal (tidak ada baris log baru)

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 9 dan 29 (menutup dialog hasil, aksi TC), langkah 20 (seed ulang dan buka kembali halaman agar TC berikutnya mulai dari PC-1 tanpa kunci). Pemulihan akhir state BE setelah langkah 39 dilakukan hook `after` (R-08).
- Baseline jumlah log (langkah 1, 18, 21, 38) mengikuti S-12: dicatat sebelum aksi pemicu tiap TC dan dipakai untuk asersi jumlah. Asersi jumlah bukan kelas g (bagian 3 prinsip 13).
- Pelaku kedua (langkah 5 dan 25) memakai sesi API Total Control kedua hanya untuk memicu perubahan state; bukan konteks kedua kelas c (bagian 3 P-2, keputusan 2026-10-30).
- Spec 39 langkah, di atas sekitar 35 langkah, dengan alasan: kedua blok satu kelas harness (posting pertama saat dialog terbuka) dan berdiri sendiri; tiap blok memerlukan baseline log, dialog, pemicu, dialog blok, dua pengecekan gembok per field (Disabled dan tooltip, satu Verifikasi per klausa), dan hitung ulang log.
- Urutan langkah mengikuti urutan state (8b butir 5): dialog Save Changes diasersi sebelum pemicu posting.
- Temuan untuk QA:
  - TC-FA-PREF-557 dan 558 bertanda `Manual Only - (d) butuh dua sesi pengguna paralel` di kolom Automation, sementara DC-7 dan DC-8 menyebut "hanya untuk eksekusi manual". Spec memakai pelaku kedua lewat sesi API/fixture BE agar otomatis; kemampuan "posting penyusutan pertama" perlu dikonfirmasi tim FE/BE.
  - Teks tooltip kunci pada Fiscal Year Start dan First Accounting Period tidak tertulis di TC; spec hanya memverifikasi tooltip kunci tampil.
  - Precondition TC-FA-PREF-557 dan 558 tidak menyebut pencatatan jumlah baris log, padahal Expected butir e meminta "tidak ada baris log baru"; spec menambah pencatatan baseline (S-12).
  - Email Total Control kedua (Pre-setup PC-8) tidak tertulis di TC; perlu dikonfirmasi tim FE.
  - Post Condition kedua TC ("Fiscal Year Start tersimpan January dan First Accounting Period tersimpan Mar 2026") dicakup Expected butir e dan diasersi pada langkah 17 dan 37.
