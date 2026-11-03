---
id: TC-FA-PREF-E2E-168-dua-admin-menyimpan-default-capitalization-threshold-bersamaan-last-write-wins-dan-tiap-save-dicatat
title: "Dua Admin Menyimpan Default Capitalization Threshold Bersamaan: Last-Write-Wins dan Tiap Save Dicatat"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-560
coverage:
  web: automated
---

# Dua Admin Menyimpan Default Capitalization Threshold Bersamaan: Last-Write-Wins dan Tiap Save Dicatat

## Prerequisites

- Mode: FE+BE.
- Kelas harness: c (dua sesi UI paralel, dua admin).
- Akun aktor: Admin A = Total Control (Pre-setup PC-8: Rina Anggraini) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Admin B = Total Control kedua (Pre-setup PC-8: "satu Total Control kedua untuk sesi paralel"); email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE); password lewat `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login Admin A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Sesi Admin B dibuka pada langkah 2 dan ditutup pada langkah 20; hook `after` menutup sesi itu bila spec gagal di tengah dan mengembalikan sesi ke akun default suite.
- Data Pre-setup: Preferences nilai awal PC-1 dengan Default Capitalization Threshold tersimpan 5.000.000; Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6); Changelog Preferences terisi. Admin A dan Admin B membuka tab Preferences pada nilai tersimpan yang sama (PC-8). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan): jumlah baris Changelog Preferences, dibaca sebelum aksi sebagai baseline (bagian 8b butir 10, S-12).
- State yang diubah spec: Default Capitalization Threshold dan Changelog Preferences (entri audit trail permanen tidak dapat dihapus). Langkah 21 memulihkan threshold ke 5.000.000 lewat seed; hook `after` menjalankan pemulihan yang sama.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) untuk Admin A dan Admin B.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Seed ulang Preferences ke nilai awal PC-1 hingga tersimpan
2. Buka konteks browser kedua, login sebagai Admin B (Total Control kedua), lalu buka Settings > Accounting > Preferences
3. Catat jumlah baris Changelog Preferences (baseline)
4. Sesi Admin A: ketik 10000000 pada CurrencyInput Default Capitalization Threshold
5. Sesi Admin A: klik [Save changes]
6. Sesi Admin A: klik [Save] pada dialog Save Changes
7. Sesi Admin A: verifikasi toast "Success, accounting preferences have been saved." tampil
8. Sesi Admin A: verifikasi tidak ada dialog konflik
9. Sesi Admin B: ketik 8000000 pada CurrencyInput Default Capitalization Threshold
10. Sesi Admin B: klik [Save changes]
11. Sesi Admin B: klik [Save] pada dialog Save Changes
12. Sesi Admin B: verifikasi toast "Success, accounting preferences have been saved." tampil
13. Sesi Admin B: verifikasi tidak ada dialog konflik
14. Sesi Admin A: muat ulang tab Preferences dengan F5
15. Sesi Admin A: verifikasi Default Capitalization Threshold "Rp 8.000.000,00"
16. Sesi Admin A: klik ikon View history
17. Sesi Admin A: verifikasi jumlah baris Changelog bertambah 2 dari baseline langkah 3
18. Sesi Admin A: verifikasi dua baris teratas memuat baris Field Default Capitalization Threshold dengan Old Value 10.000.000 dan New Value 8.000.000
19. Sesi Admin A: verifikasi dua baris teratas memuat baris Field Default Capitalization Threshold dengan Old Value 5.000.000 dan New Value 10.000.000
20. Sesi Admin A: klik ikon [✕] di header modal Changelog, lalu tutup konteks browser kedua
21. Pulihkan Default Capitalization Threshold ke 5.000.000 lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 (seed ulang), langkah 2 (membuka sesi Admin B), langkah 20 (menutup modal dan sesi kedua), langkah 21 (memulihkan threshold). Layar Preferences Admin A dibuka hook `beforeEach` suite.
- Sesi UI kedua dipakai karena Admin B menyimpan melalui UI dan toast pada sesinya diasersi (langkah 12 dan 13); spec berkelas c.
- Langkah 8 dan 13 (absence "tanpa dialog konflik") memakai toast sukses pada langkah 7 dan 12 sebagai anchor positif (bagian 8b butir 2).
- Cara baca Changelog (S-12, S-14): jumlah baris dibaca sebelum Save (langkah 3) dan selisihnya diverifikasi pada langkah 17; kedua entri baru dapat jatuh dalam menit yang sama sehingga langkah 18 dan 19 mengasersi himpunan dua baris teratas tanpa mengandalkan urutan di antaranya.
- Temuan untuk QA:
  - TC-FA-PREF-560 berstatus "Manual Only - (d) butuh dua sesi pengguna paralel"; spec tetap ditulis lengkap sebagai spec kelas c (bagian 2).
  - TC-FA-PREF-560 Expected a tidak menyebut sesi mana yang menerima toast; spec mengasersinya pada kedua sesi. Dialog Save Changes (D-01) tampil pada tiap Save (langkah 6 dan 11) karena threshold berdampak pada Asset Class; teks D-01 tidak diasersi karena TC tidak memintanya.
  - TC-FA-PREF-560 Post Condition butir b ("Dua entri log tercatat, satu per Save yang berhasil") dicakup oleh Expected c; Post Condition butir a dicakup oleh Expected b.
  - TC-FA-PREF-560 langkah 3 hanya menyebut muat ulang di sesi A; Admin B tidak memuat ulang.
