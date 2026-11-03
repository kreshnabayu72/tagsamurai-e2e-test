---
id: TC-FA-FAAM-E2E-235-multi-konteks-dua-create-bersamaan
title: "Multi-Konteks: Dua Create Bersamaan pada Nama dan Code yang Sama"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-633
  - TC-FA-FAAM-634
coverage:
  web: automated
---

# Multi-Konteks: Dua Create Bersamaan pada Nama dan Code yang Sama

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor sesi A: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1, dua sesi untuk skenario paralel; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Sesi B adalah konteks UI kedua dengan akun yang sama, dibuka pada langkah 1 dan ditutup pada langkah 25 (sesi B menjadi objek asersi). Akun Total Control harus mengizinkan dua sesi web paralel (kemampuan disediakan tim FE/BE). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category `IT Equipment`), No. 23 (Brand `Dell`), No. 24 (UoM `Unit`).
- Data Dinamis (dibuat lewat UI, nama bersuffix `{runId}-235`): `Race Name {runId}-235` (TC-FA-FAAM-633; field wajib lain Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`), `Race Code A {runId}-235` yang berhasil dibuat dengan Code `RACE1`, dan `Race Code B {runId}-235` yang ditolak (TC-FA-FAAM-634). Code `RACE1` memakai literal TC (nilai harus sama pada kedua sesi); hook `before` menghapus sisa Code `RACE1` dari run lama.
- Kemampuan teknis: dua konteks UI paralel untuk akun yang sama; submit berurutan tanpa jeda dari dua sesi (TC menyebut "hampir bersamaan").
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tutup konteks UI kedua dan hapus Asset Name bersuffix `-235` lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-633 dan 634: login sebagai Total Control pada dua sesi dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan sesi B

1. Sesi B: buka konteks UI kedua, login sebagai Total Control, dan buka Fixed Asset > Settings > Asset Master > Asset Name

### TC-FA-FAAM-633: Dua Create bersamaan dengan nama baru yang sama

2. Sesi A: klik `[+ Asset Name]`
3. Sesi A: isi Asset Name `Race Name {runId}-235` dengan field wajib lain
4. Sesi B: klik `[+ Asset Name]`
5. Sesi B: isi Asset Name `Race Name {runId}-235` dengan field wajib lain
6. Sesi A: klik `[Submit]`
7. Verifikasi sesi A sukses
8. Sesi B: klik `[Submit]`
9. Verifikasi sesi B menampilkan `Asset name already exists`
10. Verifikasi form di sesi B tetap terbuka
11. Sesi B: klik `✕` pada Modal Create
12. Verifikasi dialog `Unsaved Changes` di sesi B
13. Sesi B: klik `[Leave]`

### TC-FA-FAAM-634: Dua Create bersamaan dengan Code manual sama

14. Sesi A: klik `[+ Asset Name]`
15. Sesi A: isi Asset Name `Race Code A {runId}-235` dengan Code `RACE1` dan field wajib lain
16. Sesi B: klik `[+ Asset Name]`
17. Sesi B: isi Asset Name `Race Code B {runId}-235` dengan Code `RACE1` dan field wajib lain
18. Sesi A: klik `[Submit]`
19. Sesi B: klik `[Submit]` tanpa jeda
20. Verifikasi satu sesi (A) sukses
21. Verifikasi sesi B mendapat `Code already exists`
22. Sesi B: klik `✕` pada Modal Create
23. Verifikasi dialog `Unsaved Changes` di sesi B
24. Sesi B: klik `[Leave]`
25. Tutup konteks UI kedua dan hapus sesi login browser terkait

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka sesi B), langkah 11 sampai 13 dan 22 sampai 24 (menutup form dirty secara deterministik; S-08), dan langkah 25 (menutup konteks kedua; S-09).
- Pemenang race ditetapkan oleh urutan Submit (sesi A lebih dulu) agar deterministik; asersi tidak bergantung pada pemenang yang tidak dapat ditentukan.
- Temuan untuk QA:
  - TC-FA-FAAM-633 dan 634 menyebut "hampir bersamaan" tanpa mekanisme submit paralel; spec menulis Submit berurutan tanpa jeda.
  - TC-FA-FAAM-634 hanya menyebut "Satu sukses dan satu mendapat `Code already exists`" tanpa nama Asset Name pada tiap sesi; spec memberi nama berbeda per sesi karena Code sama sementara nama harus berbeda (nama sama akan ditolak oleh pesan nama).
  - Pre-setup No. 1 menyebut "dua sesi" tanpa menyatakan batas sesi web akun.
