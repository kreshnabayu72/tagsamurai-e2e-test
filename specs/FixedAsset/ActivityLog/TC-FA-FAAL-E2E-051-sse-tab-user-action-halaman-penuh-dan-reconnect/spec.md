---
id: TC-FA-FAAL-E2E-051-sse-tab-user-action-halaman-penuh-dan-reconnect
title: "SSE Tab User Action: Halaman Penuh, Putus-Sambung Koneksi, dan Muat Ulang"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-269
  - TC-FA-FAAL-270
  - TC-FA-FAAL-271
coverage:
  web: automated
---

# SSE Tab User Action: Halaman Penuh, Putus-Sambung Koneksi, dan Muat Ulang

## Prerequisites

- Mode: FE+BE (backend nyata; pembaruan real-time lewat SSE tanpa intercept).
- Akun aktor sesi A: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka, langkah 1 membuka Tab User Action).
- Pelaku kedua (sesi B): Admin Beta (Total Control lain, Pre-setup #16) lewat sesi API aktor sesuai `suite.md`; ia hanya memicu perubahan nama group dan tidak membuka sesi UI. Email dan password Admin Beta tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Kemampuan mengubah nama group lewat API disediakan tim FE/BE tanpa endpoint karangan.
- Data Pre-setup: Data Log Tab User Action UA-01 sampai UA-15 (#12) dan group `Gedung B` (Pre-setup #16, Data Dinamis #6). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Uji dari TC sumber: nama baru group `Gedung B1`; Search `Gedung`; Filter Object `Groups`.
- Total entri (Z): dibaca dari teks `Showing X–Y of Z entries` sesi A sebelum aksi pelaku kedua. Log bersifat permanen dan spec lain menambah baris, sehingga asersi memakai selisih terhadap Z yang dicatat, bukan angka absolut (S-12, bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE): memutus dan menyambung kembali jaringan sesi A tanpa menutup halaman.
- State yang diubah dan pemulihannya: nama group `Gedung B` diubah menjadi `Gedung B1` dan dipulihkan ke `Gedung B` lewat fixture BE yang tidak menambah baris log (kemampuan disediakan tim FE/BE; Last Updated group `Gedung B` berubah). Baris log hasil perubahan bersifat permanen dan tidak dihapus. Hook `after` menyambung kembali jaringan sesi A dan memulihkan nama group sebagai cadangan.
- Jendela asersi absence SSE: lima detik tanpa memuat ulang halaman, pilihan spec ini (bagian 6).
- Suite berjalan serial (`parallel: false`).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, sesi API aktor) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### TC-FA-FAAL-269: Baris SSE disisipkan ke halaman penuh

1. Di sesi A klik tab User Action dan tetap di halaman 1
2. Catat Z0 dari teks `Showing 1–10 of Z0 entries` dan baris ke-10 pada halaman 1
3. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung B` menjadi `Gedung B1` hingga perubahan tersimpan
4. Verifikasi baris baru `Edit` | `Groups` | `Gedung B1` ada di baris pertama dan halaman 1 tetap berisi 10 baris
5. Verifikasi teks pagination menjadi `Showing 1–10 of Z1 entries` dengan Z1 = Z0 + 1
6. Pindah ke halaman 2
7. Verifikasi baris ke-10 yang dicatat pada langkah 2 bergeser ke halaman 2 sebagai baris pertama
8. Pindah ke halaman 1
9. Pulihkan nama group `Gedung B1` menjadi `Gedung B` lewat fixture BE

### TC-FA-FAAL-270: Koneksi SSE putus lalu tersambung mengambil ulang snapshot

10. Di sesi A ketik Search `Gedung`, tekan Enter
11. Terapkan Filter Object `Groups`
12. Catat teks `Showing X–Y of Z entries` hasil Search dan Filter sebagai baseline
13. Putuskan jaringan sesi A
14. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung B` menjadi `Gedung B1` hingga perubahan tersimpan
15. Tunggu 5 detik tanpa memuat ulang halaman
16. Verifikasi tabel sesi A masih menampilkan baris hasil Search dan Filter
17. Verifikasi tidak ada indikator, dialog, maupun toast saat terputus
18. Sambungkan kembali jaringan sesi A
19. Verifikasi tabel memuat ulang snapshot dan baris `Gedung B1` hasil edit selama terputus tampil, dengan Z bertambah satu dari baseline
20. Verifikasi Search `Gedung` dan Filter Object `Groups` tetap aktif
21. Verifikasi Sort dan halaman aktif sama dengan sebelum terputus
22. Pulihkan nama group `Gedung B1` menjadi `Gedung B` lewat fixture BE
23. Klik `(←)` pada kotak Search, lalu bersihkan Filter lewat Clear Field

### TC-FA-FAAL-271: Muat ulang tab mengambil snapshot terbaru

24. Di sesi A terapkan Filter Object `Groups`, lalu klik header Name sekali (Ascending)
25. Catat Z dari teks `Showing X–Y of Z entries`
26. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung B` menjadi `Gedung B1` hingga perubahan tersimpan
27. Muat ulang tab sesi A
28. Verifikasi baris `Gedung B1` hasil edit tampil dan Z bertambah satu dari nilai yang dicatat
29. Verifikasi Filter Object `Groups` dan Sort Name Ascending tetap aktif
30. Verifikasi tidak ada dialog maupun toast
31. Pulihkan nama group `Gedung B1` menjadi `Gedung B` lewat fixture BE
32. Bersihkan Filter lewat Clear Field, lalu klik header Name dua kali lagi hingga netral

## Notes

- Mode: FE+BE, kelas c (multi-konteks): sesi A mengamati pembaruan SSE dan snapshot akibat aksi pelaku kedua. Pelaku kedua memakai sesi API, bukan konteks UI kedua, sehingga tidak butuh butir `P-2` (keputusan 2026-10-30).
- Urutan asersi TC-FA-FAAL-269 berbeda dari Expected TC (a, b, c menjadi a, c, b): teks pagination (langkah 5) diamati sebelum pindah ke halaman 2 (langkah 6) agar asersi state sementara tepat waktu (bagian 8b butir 5).
- Asersi tambahan atas TC (S-03): selisih Z (+1) pada langkah 5, 19, dan 28 adalah baseline wajib S-12 agar baris `Gedung B1` dari run sebelumnya tidak dianggap baris baru.
- Urutan asersi absence (langkah 15 sampai 17): jendela lima detik ditulis sebagai langkah penghubung tanpa `Verifikasi` (bagian 6); langkah 16 menjadi anchor positif sebelum asersi absence indikator, dialog, dan toast.
- Langkah penghubung (S-03, S-09): langkah 1 (pindah tab), 6 dan 8 (pindah halaman untuk mengamati baris yang bergeser), 9, 22, 31 (memulihkan nama group), 23 dan 32 (membersihkan Search, Filter, dan Sort).
- Temuan untuk QA:
  - TC-FA-FAAL-269 sampai 271 menyebut "sesi B" login sebagai Admin Beta, tetapi email dan password Admin Beta tidak ada di tabel Pre-setup; akun disediakan tim FE.
  - TC-FA-FAAL-270 menyebut Sort dan halaman aktif padahal langkah ujinya hanya menerapkan Search dan Filter; spec mengasersi Sort dan halaman sama dengan keadaan sebelum terputus (default).
  - TC-FA-FAAL-270 tidak menyebut cara memutus jaringan sesi A; kemampuan itu tertulis di Prerequisites sebagai disediakan tim FE.
