---
id: TC-FA-CF-E2E-009-guided-tooltip-navigasi-keyboard-overlay-dan-pemegang-create
title: "Guided Tooltip: Navigasi Keluar, Keyboard, Overlay, dan Pemegang Create"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-27
  - TC-FA-CF-28
  - TC-FA-CF-615
  - TC-FA-CF-616
coverage:
  web: automated
---

# Guided Tooltip: Navigasi Keluar, Keyboard, Overlay, dan Pemegang Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Akun kedua (langkah 23 dan 24, Ganti akun untuk TC-FA-CF-28): Master-Create (Pre-setup #5) `masterCreate_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Nama env baru (`FA_TC_PASSWORD`, `FA_MC_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Guided Tooltip (pengecualian atas hook suite): spec ini menguji flag `guided_tooltip_seen_fa-settings-custom-fields` sendiri, sehingga hook `before` suite tidak menyetel flag untuk akun Total Control dan Master-Create spec ini. Spec menghapus flag per akun lewat langkah 1, 7, 17, dan 25 (kemampuan membaca dan menghapus flag per akun disediakan tim FE/BE; nilai awal dicatat) dan hook `after` memulihkan nilai awal kedua akun.
- Kemampuan teknis: penekanan tombol keyboard (`Enter`, `←`, `→`, `Esc`); klik area overlay gelap; membaca nilai flag Guided Tooltip (langkah 6, 16, dan 20).
- State global: flag Guided Tooltip akun Total Control dan Master-Create Company Alpha (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-27: Navigasi keluar di tengah walkthrough tidak menandai seen

1. Hapus flag Guided Tooltip akun Total Control lalu muat ulang halaman
2. Klik `[Next]` sampai walkthrough berada di Step 2
3. Klik item menu sidebar lain
4. Kembali ke Fixed Asset > Settings > Custom Fields lewat menu sidebar
5. Verifikasi walkthrough muncul kembali dari Step 1
6. Verifikasi flag Guided Tooltip tidak ditandai seen

### TC-FA-CF-615: Operasi keyboard walkthrough

7. Hapus flag Guided Tooltip akun Total Control lalu muat ulang halaman
8. Tekan `Enter`
9. Verifikasi walkthrough berada di Step 2
10. Tekan `←`
11. Verifikasi walkthrough kembali ke Step 1
12. Tekan `→`
13. Verifikasi walkthrough berada di Step 2
14. Tekan `Esc`
15. Verifikasi walkthrough tertutup
16. Verifikasi flag Guided Tooltip ditandai seen

### TC-FA-CF-616: Klik overlay gelap setara Skip

17. Hapus flag Guided Tooltip akun Total Control lalu muat ulang halaman
18. Klik area overlay gelap di luar tooltip
19. Verifikasi walkthrough tertutup
20. Verifikasi flag Guided Tooltip ditandai seen
21. Muat ulang halaman
22. Verifikasi walkthrough tidak muncul otomatis

### TC-FA-CF-28: Pemegang Create melihat tombol [+ Custom Field] pada step 2

23. Ganti akun: Logout dari akun Total Control
24. Login sebagai Master-Create (Pre-setup #5) dengan `Spectra.env.FA_MC_PASSWORD`
25. Hapus flag Guided Tooltip akun Master-Create (belum pernah membuka halaman)
26. Buka Fixed Asset > Settings > Custom Fields lewat menu sidebar
27. Klik `[Next]` sampai walkthrough berada di Step 2
28. Verifikasi Step 2 menyorot tombol `[+ Custom Field]` karena tombol terlihat bagi pemegang Create

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 27, 615, 616, lalu 28. TC-FA-CF-28 berada di akhir karena memakai akun lain (Ganti akun, langkah 23 dan 24); akun aktor pertama dan hook `before` adalah Total Control sehingga tiga TC pertama tidak butuh ganti akun (S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, 17, 25 (menghapus flag dan memuat ulang halaman supaya walkthrough kunjungan pertama berjalan), langkah 2 dan 27 (Next ke Step 2 sesuai langkah uji TC), langkah 21 (muat ulang sesuai TC), dan langkah 26 (membuka halaman setelah ganti akun).
- Langkah 6 beranchor langkah 5 (walkthrough kembali muncul membuktikan halaman termuat dan state flag teramati).
- Hanya aktor yang melihat tombol `[+ Custom Field]` yang diuji pada Guided Tooltip (NC-20 terkonfirmasi di TC); perilaku step 2 bagi aktor tanpa tombol itu tidak diasersi.
- Temuan untuk QA:
  - TC-FA-CF-27 Langkah Uji menyebut "Klik menu sidebar lain" tanpa menyebut menu; spec memakai item menu sidebar lain yang tersedia pada akun.
  - TC-FA-CF-27 Expected menyebut "flag seen tidak ditandai" tanpa cara membaca flag; spec memakai kemampuan baca flag yang disediakan tim FE/BE (langkah 6, 16, 20) tanpa mengarang endpoint.
  - Email akun Master-Create mengikuti pola Pre-setup #5; nilai `{namaCompany}` untuk Company Alpha disediakan tim FE.
