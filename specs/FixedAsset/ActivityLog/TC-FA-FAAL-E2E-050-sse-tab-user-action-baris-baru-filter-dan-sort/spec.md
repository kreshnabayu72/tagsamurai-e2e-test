---
id: TC-FA-FAAL-E2E-050-sse-tab-user-action-baris-baru-filter-dan-sort
title: "SSE Tab User Action: Baris Baru, Filter Tidak Cocok, Halaman Lain, dan Sort"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-264
  - TC-FA-FAAL-266
  - TC-FA-FAAL-267
  - TC-FA-FAAL-268
coverage:
  web: automated
---

# SSE Tab User Action: Baris Baru, Filter Tidak Cocok, Halaman Lain, dan Sort

## Prerequisites

- Mode: FE+BE (backend nyata; pembaruan real-time lewat SSE tanpa intercept).
- Akun aktor sesi A: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka, langkah 1 membuka Tab User Action).
- Pelaku kedua (sesi B): Admin Beta (Total Control lain, Pre-setup #16) lewat sesi API aktor sesuai `suite.md`; ia hanya memicu perubahan nama group dan tidak membuka sesi UI. Email dan password Admin Beta tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Kemampuan mengubah nama group lewat API disediakan tim FE/BE tanpa endpoint karangan.
- Data Pre-setup: Data Log Tab User Action UA-01 sampai UA-15 (#12) dan group `Gedung B` (Pre-setup #16, Data Dinamis #6). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Uji dari TC sumber: nama baru group `Gedung B1`; Filter Action `Assign`.
- Total entri (Z): dibaca dari teks `Showing X–Y of Z entries` sesi A sebelum aksi pelaku kedua. Log bersifat permanen dan spec lain menambah baris, sehingga asersi memakai selisih terhadap Z yang dicatat, bukan angka absolut (S-12, bagian 8b butir 10).
- State yang diubah dan pemulihannya: nama group `Gedung B` diubah menjadi `Gedung B1` dan dipulihkan ke `Gedung B` lewat fixture BE yang tidak menambah baris log (kemampuan disediakan tim FE/BE, dijamin sebelum dan sesudah tiap blok; Last Updated group `Gedung B` berubah). Baris log hasil perubahan bersifat permanen dan tidak dihapus. Hook `after` memulihkan nama group sebagai cadangan.
- Jendela asersi absence SSE: lima detik tanpa memuat ulang halaman, pilihan spec ini (bagian 6).
- Suite berjalan serial (`parallel: false`).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, sesi API aktor) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### TC-FA-FAAL-264: Baris baru muncul otomatis tanpa reset scroll

1. Di sesi A klik tab User Action
2. Catat Z dari teks `Showing X–Y of Z entries` dan posisi gulir, lalu gulir tabel sedikit ke bawah dan biarkan terbuka
3. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung B` menjadi `Gedung B1` hingga perubahan tersimpan
4. Verifikasi di sesi A baris `Edit` | `Groups` | `Gedung B1` muncul otomatis di baris paling atas tanpa muat ulang, dan Z bertambah satu dari nilai yang dicatat
5. Verifikasi posisi gulir tidak berubah dan halaman tidak berubah
6. Verifikasi tidak ada dialog maupun toast
7. Pulihkan nama group `Gedung B1` menjadi `Gedung B` lewat fixture BE, lalu gulir tabel kembali ke atas

### TC-FA-FAAL-266: Event yang tidak cocok dengan Filter aktif diabaikan

8. Di sesi A terapkan Filter Action `Assign`
9. Catat teks `Showing 1–Y0 of Z0 entries` hasil filter sebagai baseline
10. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung B` menjadi `Gedung B1` hingga perubahan tersimpan
11. Tunggu 5 detik tanpa memuat ulang halaman
12. Verifikasi sedikitnya satu baris dengan Action `Assign` tetap tampil di sesi A
13. Verifikasi baris `Edit` baru tidak disisipkan
14. Verifikasi teks `Showing X–Y of Z entries` tetap `Showing 1–Y0 of Z0 entries`, sama dengan baseline langkah 9
15. Pulihkan nama group `Gedung B1` menjadi `Gedung B` lewat fixture BE
16. Bersihkan Filter lewat Clear Field

### TC-FA-FAAL-267: Baris baru di halaman yang tidak dibuka hanya memperbarui angka Z

17. Di sesi A pindah ke halaman 2
18. Catat teks `Showing 11–Y0 of Z0 entries` halaman 2 sebagai baseline
19. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung B` menjadi `Gedung B1` hingga perubahan tersimpan
20. Verifikasi sesi A tetap di halaman 2 dan tidak dipindahkan ke halaman lain
21. Verifikasi teks pagination menjadi `Showing 11–Y0 of Z1 entries` dengan Z1 = Z0 + 1 (hanya angka Z bertambah)
22. Pulihkan nama group `Gedung B1` menjadi `Gedung B` lewat fixture BE
23. Pindah ke halaman 1

### TC-FA-FAAL-268: Baris baru disisipkan sesuai Sort aktif

24. Di sesi A klik header Action sekali (Ascending)
25. Catat Z dari teks `Showing X–Y of Z entries` dan posisi gulir
26. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung B` menjadi `Gedung B1` hingga perubahan tersimpan
27. Verifikasi baris `Edit` baru disisipkan in-place pada posisi urutan Action ascending (setelah baris `Delete`), bukan di baris paling atas, dan Z bertambah satu dari nilai yang dicatat
28. Verifikasi posisi gulir dan halaman tidak berubah
29. Pulihkan nama group `Gedung B1` menjadi `Gedung B` lewat fixture BE
30. Klik header Action dua kali lagi hingga netral

## Notes

- Mode: FE+BE, kelas c (multi-konteks): sesi A mengamati pembaruan SSE akibat aksi pelaku kedua. Pelaku kedua memakai sesi API, bukan konteks UI kedua, sehingga tidak butuh butir `P-2` (keputusan 2026-10-30).
- Asersi tambahan atas TC (S-03): `Verifikasi` selisih Z (+1) pada langkah 4, 21, dan 27 adalah baseline wajib S-12 agar baris `Edit` | `Groups` | `Gedung B1` dari run sebelumnya tidak dianggap baris baru.
- Urutan asersi absence (langkah 11 sampai 14 dan 20): jendela lima detik ditulis sebagai langkah penghubung tanpa `Verifikasi` (bagian 6); langkah 12 menjadi anchor positif baris pembanding sebelum asersi absence baris `Edit`.
- Langkah penghubung (S-03, S-09): langkah 1 (pindah tab), 7, 15, 22, 29 (memulihkan nama group agar blok berikutnya memakai nama awal), langkah 16 (membersihkan Filter), 23 (kembali ke halaman 1), dan 30 (mengembalikan Sort netral).
- Temuan untuk QA:
  - TC-FA-FAAL-264 sampai 268 menyebut "sesi B" login sebagai Admin Beta, tetapi email dan password Admin Beta tidak ada di tabel Pre-setup; akun disediakan tim FE.
  - TC-FA-FAAL-268 tidak menyebut posisi baris `Edit` baru di antara baris `Edit` lain; spec mengikuti TC (setelah baris `Delete`) dan tidak mengasersi urutan di antara baris `Edit`.
  - Pemulihan nama group lewat fixture BE yang tidak menambah baris log adalah asumsi spec; bila pemulihan menulis baris log, baseline Z di tiap blok sudah dicatat sebelum aksi pemicu sehingga asersi tetap berlaku.
