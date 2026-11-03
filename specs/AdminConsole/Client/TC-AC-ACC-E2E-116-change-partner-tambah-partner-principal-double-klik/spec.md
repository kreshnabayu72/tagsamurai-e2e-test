---
id: TC-AC-ACC-E2E-116-change-partner-tambah-partner-principal-double-klik
title: "Change Partner oleh Principal: Tambah Partner Tidak Mengubah Group, Relasi Suspended Tetap, dan Double-klik [Confirm]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-175
  - TC-AC-ACC-598
  - TC-AC-ACC-639
coverage:
  web: automated
---

# Change Partner oleh Principal: Tambah Partner Tidak Mengubah Group, Relasi Suspended Tetap, dan Double-klik [Confirm]

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): `PT Ganti Mitra {runId}-116` (setara C-13: Active, hanya Partner CV Mitra Sejati, Group Area Jakarta, FAMS Active; "CV Mitra Lestari" ditambah lalu di-Remove) dan `PT Relasi Campur {runId}-116` (setara C-ROL-9: Active, Partner CV Mitra Sejati Active dan CV Mitra Beku Suspended, Group Area Jakarta, FAMS Active; "CV Mitra Lestari" ditambah). Efek: relasi "CV Mitra Lestari" menjadi `transferred` (riwayat) pada replika, baris Changelog `Change Partner` dan Last Updated kedua replika bertambah. Client C-13 `PT Ganti Mitra` dan C-ROL-9 `PT Relasi Campur` literal tidak disentuh.
- Partner pembanding: `CV Mitra Lestari` (Active, belum terhubung ke kedua replika).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-175: Add Partner baru: Group tidak berubah bila bukan Anchor pertama

1. Ketik Search `PT Ganti Mitra {runId}-116`, tekan Enter
2. Klik `[⋯]` pada baris `PT Ganti Mitra {runId}-116` → klik `Change Partner`
3. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
4. Verifikasi "CV Mitra Lestari" masuk di bawah survivor dengan badge `New` (severity primary) dan drag handle
5. Verifikasi field `[Group]` read-only tetap mengikuti Partner teratas (CV Mitra Sejati)
6. Klik `[Confirm]`
7. Verifikasi toast sukses "Success, partner has been updated."
8. Verifikasi Managed By baris `PT Ganti Mitra {runId}-116` adalah "CV Mitra Sejati" diikuti `+1 more`
9. Verifikasi Group baris `PT Ganti Mitra {runId}-116` tidak berubah
10. Klik sub-tab Active, ketik Search `PT Ganti Mitra {runId}-116`, tekan Enter
11. Klik `[⋯]` pada baris `PT Ganti Mitra {runId}-116` → klik `Change Partner`
12. Klik `[Remove]` pada "CV Mitra Lestari"
13. Klik `[Confirm]`

### TC-AC-ACC-598: Add Partner tidak mengubah status relasi Suspended yang sudah ada

14. Ketik Search `PT Relasi Campur {runId}-116`, tekan Enter
15. Klik `[⋯]` pada baris `PT Relasi Campur {runId}-116` → klik `Change Partner`
16. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
17. Klik `[Confirm]`
18. Verifikasi toast sukses "Success, partner has been updated."
19. Klik `[⋯]` pada baris `PT Relasi Campur {runId}-116` → klik `Change Partner`
20. Verifikasi list "Current Partners" memuat "CV Mitra Sejati" dengan badge `Active`
21. Verifikasi list "Current Partners" memuat "CV Mitra Beku" dengan badge `Suspended`
22. Verifikasi list "Current Partners" memuat "CV Mitra Lestari" dengan badge `Active`
23. Klik `[✕]` pada header dialog Change Partner tanpa menyimpan

### TC-AC-ACC-639: Double-klik [Confirm] pada dialog Change Partner hanya memproses satu kali

24. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Ganti Mitra {runId}-116` lalu tekan Enter
25. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Change Partner` untuk "PT Ganti Mitra {runId}-116" (N0), lalu tutup modal
26. Ketik Search `PT Ganti Mitra {runId}-116`, tekan Enter
27. Klik `[⋯]` pada baris `PT Ganti Mitra {runId}-116` → klik `Change Partner`
28. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
29. Klik `[Confirm]` dua kali cepat
30. Verifikasi `[Confirm]` ter-disable segera setelah klik pertama
31. Verifikasi toast "Success, partner has been updated." tampil satu kali
32. Verifikasi Managed By baris `PT Ganti Mitra {runId}-116` adalah "CV Mitra Sejati" dengan `+1 more`
33. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Ganti Mitra {runId}-116` lalu tekan Enter
34. Ubah ukuran halaman modal menjadi 100
35. Verifikasi jumlah baris Action `Change Partner` untuk "PT Ganti Mitra {runId}-116" adalah N0 + 1
36. Verifikasi baris baru ber-Field `Partner` dengan Old Value memuat `CV Mitra Sejati`
37. Verifikasi baris baru ber-Field `Partner` dengan New Value memuat `CV Mitra Sejati` dan `CV Mitra Lestari`
38. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas tiga TC satu topik (konfirmasi Change Partner yang menambah Partner) dengan akun yang sama; tiap blok memakai replika berbeda atau baseline sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Pemulihan Post Condition di akhir blok (TC-AC-ACC-598 dan TC-AC-ACC-639) tidak dijalankan karena target adalah replika milik spec yang dibersihkan hook `after`.
- Langkah penghubung (tanpa awalan Verifikasi): penutupan modal Changelog; langkah 23 (`[✕]` pada header dialog Change Partner tanpa menyimpan, menutup dialog yang dibuka di langkah 19 sebelum `[Changelog]` dibuka); langkah 10 sampai 13 (sub-tab Active, Search ulang, lalu Remove "CV Mitra Lestari" dan `[Confirm]`) adalah Post Condition TC-AC-ACC-175 yang dipertahankan karena TC-AC-ACC-639 menambah "CV Mitra Lestari" lagi pada replika yang sama. Langkah 24 dan 25 (baseline N0) adalah langkah TC-AC-ACC-639.
- Baseline N0 pada TC-AC-ACC-639 dicatat sebelum aksi pemicu (S-12); asersi "baris baru" memakai selisih terhadap N0, bukan posisi teratas.
- Post Condition TC-AC-ACC-175 butir a sampai c (relasi baru aktif, subscription dan plan owner tidak berubah, satu baris Changelog `Change Partner`) tanpa langkah observasi di TC tidak diasersi; butir d menjadi langkah pemulihan (langkah 10 sampai 13).
- Temuan untuk QA:
  - TC-AC-ACC-175 Expected b menyebut Group read-only "tetap mengikuti Partner teratas (CV Mitra Sejati)" tanpa menyebut nilai Group; spec mengasersi tepat seperti tertulis di Expected dan mengasersi "Group tidak berubah" di List pada Expected d.
  - Pemulihan lewat UI menjadikan relasi "CV Mitra Lestari" `transferred`; relasi tidak kembali ke keadaan sebelum penambahan, tetapi dampaknya hanya pada replika milik spec yang dibersihkan hook `after`.
