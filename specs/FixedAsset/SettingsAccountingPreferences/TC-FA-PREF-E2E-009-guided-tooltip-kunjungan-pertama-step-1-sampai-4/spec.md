---
id: TC-FA-PREF-E2E-009-guided-tooltip-kunjungan-pertama-step-1-sampai-4
title: "Guided Tooltip Preferences: Kunjungan Pertama Menampilkan Step 1 sampai Step 4"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-52
  - TC-FA-PREF-53
  - TC-FA-PREF-54
  - TC-FA-PREF-55
sourceRules: ["§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#r4"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": [5, 6, 7]
  "§4.7#r2": [11, 12, 13]
  "§4.7#r3": [16, 17, 18]
  "§4.7#r4": [21, 22, 23]
anchor: [4, 8, 9, 14, 19, 24, 25]
coverage:
  web: automated
---

# Guided Tooltip Preferences: Kunjungan Pertama Menampilkan Step 1 sampai Step 4

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1, keadaan PA-20 tanpa flag `guided_tooltip_seen_fa-accounting-preferences`) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Pengecualian hook suite untuk Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-accounting-preferences` true; spec ini mengatur flag itu sendiri menjadi belum tersimpan pada langkah 1 (kemampuan menyetel dan membaca flag disediakan tim FE/BE). Hook `after` memulihkan flag ke nilai awal hook suite.
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Data Uji TC: page_key `fa-accounting-preferences`.
- Suite berjalan serial (`parallel: false`); spec ini mengubah flag Guided Tooltip akun aktor dan memulihkannya di hook `after`.

## Test Steps

### TC-FA-PREF-52: Step 1 muncul otomatis pada kunjungan pertama

1. Setel flag `guided_tooltip_seen_fa-accounting-preferences` akun aktor menjadi belum tersimpan
2. Pindah ke halaman aplikasi lain di luar Settings > Accounting
3. Buka Settings > Accounting > Preferences untuk pertama kali
4. Verifikasi walkthrough mulai otomatis dari Step 1 dengan overlay gelap
5. Verifikasi spotlight pada judul SectionCard General
6. Verifikasi tooltip box menampilkan indikator "Step 1 of 4"
7. Verifikasi tooltip box menampilkan judul "Accounting Year" dan deskripsi "Set when your accounting year begins and when your first accounting period starts. These settings lock once depreciation is posted."
8. Verifikasi navigasi menampilkan `[Skip]` dan `[Next]`
9. Verifikasi `[Back]` tidak tampil (Hidden) pada Step 1

### TC-FA-PREF-53: Step 2 Capitalization

10. Klik `[Next]` pada Step 1
11. Verifikasi spotlight berpindah ke judul SectionCard Capitalization
12. Verifikasi tooltip box menampilkan indikator "Step 2 of 4"
13. Verifikasi tooltip box menampilkan judul "Capitalization" dan deskripsi "Default values used when an asset class does not set its own."
14. Verifikasi navigasi menampilkan `[Skip]`, `[Back]`, dan `[Next]`

### TC-FA-PREF-54: Step 3 Disposal

15. Klik `[Next]` pada Step 2
16. Verifikasi spotlight berpindah ke judul SectionCard Disposal
17. Verifikasi tooltip box menampilkan indikator "Step 3 of 4"
18. Verifikasi tooltip box menampilkan judul "Disposal" dan deskripsi "Sets the default accounts and document rules used when assets are disposed."
19. Verifikasi navigasi menampilkan `[Skip]`, `[Back]`, dan `[Next]`

### TC-FA-PREF-55: Step 4 View history

20. Klik `[Next]` pada Step 3
21. Verifikasi spotlight berpindah ke ikon View history
22. Verifikasi tooltip box menampilkan indikator "Step 4 of 4"
23. Verifikasi tooltip box menampilkan judul "View history" dan deskripsi "See the history of changes made to preferences."
24. Verifikasi navigasi menampilkan `[Skip]`, `[Back]`, dan `[Done]`
25. Verifikasi `[Next]` tidak tampil (diganti `[Done]`)
26. Klik `[Skip]` untuk menutup walkthrough

## Notes

- Langkah penghubung (S-03): langkah 1 sampai 3 (membentuk kunjungan pertama; hook `beforeEach` suite sudah membuka halaman Preferences sehingga spec pindah ke halaman lain lalu membukanya kembali), dan langkah 26 (menutup walkthrough).
- Pembagian TC (S-04): TC-FA-PREF-53, 54, dan 55 masing-masing berprecondition kunjungan pertama dengan klik `[Next]` dari Step 1. Karena flag baru tersimpan setelah `[Done]` atau `[Skip]`, walkthrough yang sama dilanjutkan dari TC sebelumnya, dan klik `[Next]` yang menjadi langkah TC dependensi ditulis berurutan (langkah 10, 15, 20) tanpa membuka ulang halaman.
- Klausa "halaman menggulir bila target di luar viewport" pada Expected TC-FA-PREF-53, 54, dan 55 bersifat kondisional dan tidak diasersi terpisah; perpindahan spotlight diasersi pada langkah 11, 16, dan 21.
- Urutan TC dalam spec: TC-FA-PREF-52, 53, 54, 55.
- Temuan untuk QA: TC-FA-PREF-53 menulis target spotlight "judul section capitalization" dan TC-FA-PREF-54 "judul section disposal" dengan huruf kecil; spec memakai nama SectionCard "Capitalization" dan "Disposal".
