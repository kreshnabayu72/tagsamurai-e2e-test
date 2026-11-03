---
id: TC-FA-COA-E2E-083-absence-log-aksi-no-op-dan-item-bulk-yang-dilewati
title: "Absence Log: Aksi No-Op dan Item Bulk yang Dilewati Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-51
  - TC-FA-COA-52
  - TC-FA-COA-96
  - TC-FA-COA-118
coverage:
  web: automated
---

# Absence Log: Aksi No-Op dan Item Bulk yang Dilewati Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence log). Suite berjalan serial (`parallel: false`).
- Akun login hook `before` spec ini: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data Pre-setup (kunci fixture ditetapkan tim FE):
  - P1 `5-6001 – Depreciation Expense – Admin` (Active, Used By 0): target Activate no-op (TC-FA-COA-51); tidak diubah.
  - P3 `4-7001 – Gain on Disposal` (Inactive, Used By 0): target Deactivate no-op (TC-FA-COA-52); tidak diubah.
  - P2 `6-2001 – Repairs & Maintenance Expense` (Active, Last Used in Journal `Aug 2026`): target permintaan J-06 (TC-FA-COA-118); tidak diubah dan Last Updated tidak berubah.
  - P65 `5-6105 – Depreciation Expense – Bulk Log` (Active, Used By 0, Last Used kosong) dan P66 `4-7108 – Gain on Disposal – Bulk Log Skip` (Inactive, Used By 0, Last Used kosong): akun sekali pakai milik spec ini untuk TC-FA-COA-96. P65 dinonaktifkan oleh spec; hook `before` dan `after` mengembalikan P65 ke Active dan memastikan P66 Inactive. Code literal (maksimal 15 karakter, tidak diberi suffix `{runId}`).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): sesi API aktor Total Control (butir "Sesi API aktor" di `suite.md`) dan klien HTTP untuk permintaan langsung Activate, Deactivate, dan J-06; kemampuan membaca dari server status akun dan jumlah entri Changelog per Account Code (baseline, S-12); jalur ekspor Journal J-06 disediakan tim FE/BE (NC-04, belum ada; TC-FA-COA-118 `[DEFERRED]`).
- State global: spec tidak mengubah state global selain P65 (dipulihkan langkah 49 dan hook `after`).
- Seed dan pemulihan akun lewat API mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.

## Test Steps

### TC-FA-COA-51: Activate akun yang sudah Active

1. Catat jumlah entri Changelog Account Code `5-6001` dari server (baseline)
2. Kirim permintaan langsung Activate untuk P1 ke server menggunakan sesi API aktor Total Control hingga respons diterima
3. Verifikasi permintaan selesai tanpa error
4. Verifikasi tidak ada perubahan data: P1 pada server tetap Active
5. Klik icon Changelog
6. Verifikasi Modal Changelog tampil dengan sedikitnya satu baris entri
7. Verifikasi Changelog tidak memuat entri baru untuk P1: jumlah entri Account Code `5-6001` sama dengan langkah 1
8. Tutup Modal Changelog

### TC-FA-COA-52: Deactivate akun yang sudah Inactive

9. Catat jumlah entri Changelog Account Code `4-7001` dari server (baseline)
10. Kirim permintaan langsung Deactivate untuk P3 ke server menggunakan sesi API aktor Total Control hingga respons diterima
11. Verifikasi permintaan selesai tanpa error
12. Verifikasi tidak ada perubahan data: P3 pada server tetap Inactive
13. Klik icon Changelog
14. Verifikasi Modal Changelog tampil dengan sedikitnya satu baris entri
15. Verifikasi Changelog tidak memuat entri baru untuk P3: jumlah entri Account Code `4-7001` sama dengan langkah 9
16. Tutup Modal Changelog

### TC-FA-COA-118: [DEFERRED] Periode lebih lama tidak memundurkan Last Used

17. Ketik Search `6-2001`, tekan Enter
18. Arahkan kursor ke sel Last Used in Journal P2 dan catat teks hover
19. Catat jumlah entri Changelog Account Code `6-2001` untuk L-10 dari server (baseline)
20. Kirim permintaan langsung J-06 untuk periode `Jul 2026` dengan akun P2 menggunakan sesi API aktor Total Control hingga respons diterima
21. Muat ulang halaman
22. Ketik Search `6-2001`, tekan Enter
23. Verifikasi kolom Last Used in Journal P2 tetap `Aug 2026`
24. Arahkan kursor ke sel Last Used in Journal P2
25. Verifikasi waktu export pada hover sel Last Used P2 sama dengan langkah 18
26. Verifikasi nama pengekspor pada hover sel Last Used P2 sama dengan langkah 18
27. Klik icon Changelog
28. Verifikasi Modal Changelog tampil dengan sedikitnya satu baris entri
29. Verifikasi tidak ada entri L-10 baru: jumlah entri Account Code `6-2001` sama dengan langkah 19
30. Tutup Modal Changelog

### TC-FA-COA-96: Edit No-Op dan item bulk yang dilewati

31. Ganti isi kotak search dengan `Bulk Log`, tekan Enter
32. Catat jumlah entri Changelog Account Code `5-6105` dan `4-7108` dari server (baseline)
33. Klik row action `Edit` pada akun P65
34. Klik `[Save]` tanpa mengubah nilai
35. Tunggu aksi selesai
36. Klik icon Changelog
37. Verifikasi Modal Changelog tampil dengan sedikitnya satu baris entri
38. Verifikasi tidak ada entri log untuk Edit tanpa perubahan: jumlah entri Account Code `5-6105` sama dengan langkah 32
39. Tutup Modal Changelog
40. Centang P65 dan P66
41. Klik Bulk `Deactivate`
42. Klik `[Deactivate]` pada dialog versi single (D-01) karena hanya P65 yang diproses
43. Tunggu aksi selesai
44. Klik icon Changelog
45. Verifikasi Modal Changelog tampil dengan sedikitnya satu baris entri
46. Verifikasi log tercatat untuk P65: jumlah entri Account Code `5-6105` bertambah satu dari langkah 32
47. Verifikasi P66 tidak ada entri: jumlah entri Account Code `4-7108` sama dengan langkah 32
48. Tutup Modal Changelog
49. Aktifkan kembali P65 melalui sesi API aktor Total Control hingga status Active tersimpan

## Notes

- `P-5`: spec absence (kelas g) memuat pemicu kelas a (permintaan langsung Activate, Deactivate, dan J-06; langkah 2, 10, 20) yang hanya membentuk kondisi yang diasersi tidak tercatat; tiap TC punya baseline sendiri (langkah 1, 9, 19, 32).
- `K-1`: TC-FA-COA-51, 52, dan 118 berkelas a dengan Expected respons API/state data; tetap di spec FE+BE walau tumpang tindih dengan `tc-settings-chart-of-accounts-backend.md` (tidak ada berkas BE untuk modul ini).
- Alasan di atas sekitar 35 langkah (49 langkah): semua blok satu kelas harness (absence log) dan berdiri sendiri. Blok baca-log berpola (buka Changelog, anchor, Verifikasi jumlah entri, tutup; langkah 5 sampai 8, 13 sampai 16, 27 sampai 30, 36 sampai 39, 44 sampai 48) tidak dihitung menurut bagian 3 prinsip 13; sisanya di bawah ambang.
- Pembagian TC lintas spec: tidak ada TC lain yang terbelah ke spec ini. Klausa "tidak ada entri log" pada TC lain tetap di spec asal (mis. Post Condition TC-FA-COA-38 dan TC-FA-COA-150) dan tidak dipindah ke sini; keputusan perpindahan ditunggu QA.
- Langkah penghubung (S-03): langkah 8, 16, 30, 39, 48 menutup Modal Changelog; langkah 17 dan 22 Search P2 (R-16, bagian 8b butir 12); langkah 21 memuat ulang halaman agar Last Used terbaca dari server; langkah 31 Search `Bulk Log` menampilkan P65 dan P66; langkah 35 dan 43 "Tunggu aksi selesai" (bagian 8b butir 8); langkah 49 memulihkan P65 (S-09).
- Anchor absence (bagian 8b butir 2): Modal Changelog tampil dengan sedikitnya satu baris entri (langkah 6, 14, 28, 37, 45) sebelum asersi jumlah entri tidak bertambah; langkah 46 (entri P65 bertambah) menjadi anchor untuk langkah 47.
- S-06: P1, P2, dan P3 hanya menjadi target aksi no-op atau permintaan yang tidak mengubah apa pun; Last Updated tidak berubah.
- Temuan untuk QA:
  - TC-FA-COA-51, 52, dan 96 menyebut "log" tanpa menyebut surface; PRD mencatat log di Changelog, System Log, dan Activity Log dalam satu transaksi. Spec mengasersi Changelog (surface yang disebut TC-FA-COA-51 dan 52); System Log dan Activity Log tidak diasersi.
  - TC-FA-COA-96 tidak punya langkah membuka log meski Expected a dan b menyebut log; spec menambah langkah penghubung membuka Changelog (langkah 36 dan 44) dan memisahkan pengecekan Edit tanpa perubahan (langkah 38) dari Bulk Deactivate (langkah 46 dan 47). Langkah 42 menyebut dialog versi single D-01 tanpa Expected terpisah; judul dialog tidak diasersi (S-02).
  - TC-FA-COA-51, 52 Expected a ("Permintaan selesai tanpa perubahan data") tidak menyebut kode status; spec mengasersi "selesai tanpa error".
  - TC-FA-COA-118 bergantung pada jalur J-06 yang belum ada (NC-04, `[DEFERRED]`): disediakan tim FE/BE tanpa endpoint. Teks hover tidak ditulis literal di TC; spec membandingkan dengan teks yang dicatat pada langkah 18.
  - TC-FA-COA-96 memakai Code P65 `5-6105` dan P66 `4-7108` literal (Account Code maksimal 15 karakter, tidak dapat diberi suffix); Search `Bulk Log` mengandalkan nama P65 dan P66 (perlu dikonfirmasi tidak ada akun Pre-setup lain dengan substring itu).
  - Pemulihan P65 (langkah 49) dan jumlah entri Changelog permanen: tiap run menambah entri; asersi memakai selisih terhadap baseline (S-12).
