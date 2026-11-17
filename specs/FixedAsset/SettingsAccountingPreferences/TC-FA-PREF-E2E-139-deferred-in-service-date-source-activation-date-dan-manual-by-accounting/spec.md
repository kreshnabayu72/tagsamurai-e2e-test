---
id: TC-FA-PREF-E2E-139-deferred-in-service-date-source-activation-date-dan-manual-by-accounting
title: "[DEFERRED] In-service Date Source: Activation Date dan Manual by Accounting"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-431
  - TC-FA-PREF-432
  - TC-FA-PREF-433
  - TC-FA-PREF-434
  - TC-FA-PREF-440
sourceRules: ["FAPREF-LOGIC-04b", "FAPREF-LOGIC-04c", "FAPREF-LOGIC-04e", "F-FAPREF-01.k13"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-04b": [6, 11, 16]
  "FAPREF-LOGIC-04c": [21, 23]
  "FAPREF-LOGIC-04e": 30
  "F-FAPREF-01.k13": 30
coverage:
  web: automated
---

# [DEFERRED] In-service Date Source: Activation Date dan Manual by Accounting

## Prerequisites

- Mode: FE+BE.
- Kelas fungsional; TC `[DEFERRED]`. Modul pemilik transaksi aktivasi modul akuntansi, job rekonsiliasi J-01, modul Asset (status dan in-service date), serta modul Accounting Period adalah modul pemilik/konsumen yang belum disusun: TC `[DEFERRED]` (NC-08, NC-09) ditulis dengan langkah generik pada modul itu dan hanya mengasersi klaim yang tertulis di TC dan PRD; seluruh kebutuhan modul disediakan tim FE setelah modul tersedia.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` seri PC (PC-1) dengan In-service Date Source Activation date untuk TC-FA-PREF-431 sampai 433 dan 440, Manual by Accounting untuk TC-FA-PREF-434; aset 'assignment - 11' (belum pernah berstatus operasional, dipakai TC-FA-PREF-431 sampai 433 berurutan dengan seed ulang antar-TC), 'assignment - 12', dan 'assignment - 16' (in-service date 5 Mei 2026) dari PC-16.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pemindahan status aset dan pengisian in-service date pada modul pemilik aset (disediakan tim FE setelah modul tersedia); seed dan pemulihan kondisi company (PC-13, PC-16, status plan dan entitas) lewat API (butir "Seed dan pemulihan lewat API" di `suite.md`); kendali jam sistem (clock; butir "Kendali jam sistem" di `suite.md`); Jam sistem (clock): jam server dan jam browser diatur bersama ke 5 Mei 2026 pada langkah 1 untuk TC-FA-PREF-431 sampai 433 dan dipulihkan pada langkah 17 serta di hook `after`.
- State yang diubah spec: Preferences company, status dan in-service date aset, serta jam sistem. Aset dan Preferences dipulihkan lewat seed antar-TC dan di hook `after`; jam sistem dipulihkan pada langkah 17 dan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-431: Activation date mengambil tanggal aset pertama kali berpindah ke status Active sebagai tanggal mulai penyusutan

1. Atur jam server dan jam browser ke 5 Mei 2026
2. Bentuk kondisi PC-1 dan PC-16 lewat seed: In-service Date Source tersimpan Activation date; aset 'assignment - 11' terdaftar dan belum pernah berstatus operasional (precondition TC, tidak diasersi)
3. Pada modul pemilik status aset, pindahkan aset 'assignment - 11' ke status Active untuk pertama kali pada 5 Mei 2026 hingga status tersimpan
4. Ketik Search 'assignment - 11', tekan Enter pada daftar aset modul pemilik
5. Buka Detail aset 'assignment - 11' dan amati tanggal mulai penyusutan
6. Verifikasi tanggal mulai penyusutan aset = 5 Mei 2026 (tanggal aset pertama kali berpindah ke status Active) tanpa input manual

### TC-FA-PREF-432: Activation date mengambil tanggal aset pertama kali berpindah ke status In Use sebagai tanggal mulai penyusutan

7. Bentuk kondisi PC-1 dan PC-16 lewat seed: In-service Date Source tersimpan Activation date; aset 'assignment - 11' terdaftar dan belum pernah berstatus operasional (precondition TC, tidak diasersi)
8. Pada modul pemilik status aset, pindahkan aset 'assignment - 11' ke status In Use untuk pertama kali pada 5 Mei 2026 hingga status tersimpan
9. Ketik Search 'assignment - 11', tekan Enter pada daftar aset modul pemilik
10. Buka Detail aset 'assignment - 11' dan amati tanggal mulai penyusutan
11. Verifikasi tanggal mulai penyusutan aset = 5 Mei 2026 (tanggal aset pertama kali berpindah ke status In Use) tanpa input manual

### TC-FA-PREF-433: Activation date mengambil tanggal aset pertama kali berpindah ke status Borrowed sebagai tanggal mulai penyusutan

12. Bentuk kondisi PC-1 dan PC-16 lewat seed: In-service Date Source tersimpan Activation date; aset 'assignment - 11' terdaftar dan belum pernah berstatus operasional (precondition TC, tidak diasersi)
13. Pada modul pemilik status aset, pindahkan aset 'assignment - 11' ke status Borrowed untuk pertama kali pada 5 Mei 2026 hingga status tersimpan
14. Ketik Search 'assignment - 11', tekan Enter pada daftar aset modul pemilik
15. Buka Detail aset 'assignment - 11' dan amati tanggal mulai penyusutan
16. Verifikasi tanggal mulai penyusutan aset = 5 Mei 2026 (tanggal aset pertama kali berpindah ke status Borrowed) tanpa input manual
17. Pulihkan jam server dan jam browser ke waktu nyata

### TC-FA-PREF-434: Manual by Accounting membuat Accounting mengisi in-service date per aset di Detail aset

18. Bentuk kondisi PC-16 lewat seed: In-service Date Source tersimpan Manual by Accounting; aset 'assignment - 12' terdaftar (precondition TC, tidak diasersi)
19. Ketik Search 'assignment - 12', tekan Enter pada daftar aset modul pemilik
20. Buka Detail aset 'assignment - 12'
21. Verifikasi Detail aset menyediakan isian in-service date untuk diisi Accounting
22. Isi in-service date dengan tanggal 6 Mei 2026 dan simpan isian pada Detail aset
23. Verifikasi tanggal mulai penyusutan aset = 6 Mei 2026 sesuai isian

### TC-FA-PREF-440: Perubahan In-service Date Source tidak mengubah in-service date aset yang sudah ada

24. Bentuk kondisi PC-1 dan PC-16 lewat seed: In-service Date Source tersimpan Activation date; aset 'assignment - 16' sudah memiliki in-service date 5 Mei 2026 (precondition TC, tidak diasersi), lalu buka Settings > Accounting > Preferences
25. Pilih "Manual by Accounting" pada Select In-service Date Source
26. Klik [Save changes]
27. Tunggu aksi selesai
28. Ketik Search 'assignment - 16', tekan Enter pada daftar aset modul pemilik
29. Buka Detail aset 'assignment - 16' dan amati in-service date
30. Verifikasi in-service date aset 'assignment - 16' tetap 5 Mei 2026
31. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 2, 4, 7, 9, 12, 14, 17, 18, 19, 24, 27, 28, 31 (seed precondition TC, pengaturan jam atau fault injection bila dipakai spec, pencatatan baseline, menutup modal, pemulihan kondisi).
- TC-FA-PREF-431 sampai 433 memakai aset 'assignment - 11' yang sama dan masing-masing mensyaratkan aset belum pernah berstatus operasional; aset dibentuk ulang lewat seed sebelum tiap TC.
- Pencarian aset di daftar modul pemilik ditulis sebagai langkah penghubung "Ketik Search ..." (R-16, 8b butir 12); UI daftar aset ditetapkan modul pemilik.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Kolom Automatable TC menandai pemicu job J-01, kegagalan sisi server, atau aktivasi sebagai "Manual Only" atau memakai langkah generik pada modul yang belum disusun; spec tetap ditulis penuh sesuai bagian 2 dan menyatakan kebutuhannya di Prerequisites.
  - TC-FA-PREF-434 menyebut pengisian in-service date tanpa menyebut aksi menyimpan isian; spec menulis "simpan isian" dan meminta konfirmasi cara menyimpan pada modul pemilik.
  - TC-FA-PREF-440 menyebut "Simpan perubahan" tanpa menyebut ada atau tidaknya dialog Save Changes; spec mengikuti TC lain yang menyatakan perubahan In-service Date Source tidak memiliki baris dampak (tanpa dialog).
  - Post Condition TC-FA-PREF-431 sampai 434 dan 440 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).
