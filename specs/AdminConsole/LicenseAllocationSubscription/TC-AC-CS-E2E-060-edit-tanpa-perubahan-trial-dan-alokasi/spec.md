---
id: TC-AC-CS-E2E-060-edit-tanpa-perubahan-trial-dan-alokasi
title: "Edit: Tanpa Perubahan, Trial, dan Alokasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-232
  - TC-AC-CS-233
  - TC-AC-CS-234
  - TC-AC-CS-550
coverage:
  web: automated
---

# Edit: Tanpa Perubahan, Trial, dan Alokasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; semua pengajuan milik aktor `Fajar Nugroho` lewat sesi API aktor; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed A sampai D): Client `Toko Serba Ada+{runId}-060` dengan Renewal FAMS Enterprise Waiting for Approval, Duration 1 year(s) (seed A; padanan Pre-setup #67); Client `PT Bintang Timur+{runId}-060` dengan Trial FAMS Growth Waiting for Approval, Duration 30, Asset 50, Concurrent User 10 (seed B; padanan #59); Client `CV Nusantara Data+{runId}-060` dengan Trial SIEM Waiting for Approval, Log Source Quota 10 (seed C; padanan #105); Client `Toko Cahaya Abadi+{runId}-060` dengan term FAMS Professional Pending Start Date `15/09/26` dan dua alokasi lisensi Pending (Concurrent User 10 dan Maintenance 5) (seed D; padanan #110).
- Data Pre-setup baca-saja/global: Toggle Require Approval for Allocation ON (#23) dan aktor bukan bypass; tanggal acuan uji `19/08/26`.
- Data Dinamis: Hasil Edit, status term, dan entri audit trail hanya pada Client seed A sampai D dan dihapus bersama seed di hook `after`. Yang dipulihkan hanya state global: jam server dan jam browser (fixture waktu, disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (disediakan tim FE/BE), dipulihkan di hook `after`; memicu atau mem-poll scheduled flip (polling muat ulang tiap 5 detik batas 2 menit); membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-232: Edit Duration pada term Renewal tanpa field Start Date

1. Ketik Search `Toko Serba Ada+{runId}-060`, tekan Enter, buka Detail baris `Subscription ID seed A`, lalu catat Start Date dan End Date sebagai baseline
2. Kembali ke List, klik ikon `⋯` pada baris `Subscription ID seed A` lalu pilih `Edit`
3. Ubah Duration menjadi `2` lalu klik `[Save]`
4. Verifikasi toast sukses "Success, subscription has been updated."
5. Buka Detail baris `Subscription ID seed A`
6. Verifikasi Start Date tidak berubah (otomatis sesuai predecessor)
7. Verifikasi End Date mengikuti Duration baru
8. Verifikasi status tetap Waiting for Approval

### TC-AC-CS-233: Edit Trial Duration, Asset Quota, dan Concurrent User Quota

9. Kembali ke List, ganti isi kotak search dengan `PT Bintang Timur+{runId}-060`, tekan Enter, lalu catat jumlah entri Changelog Client `PT Bintang Timur+{runId}-060` — FAMS sebagai baseline
10. Klik ikon `⋯` pada baris `Subscription ID seed B` lalu pilih `Edit`
11. Ubah Trial Duration menjadi `14`, Trial Asset Quota menjadi `25`, Trial Concurrent User Quota menjadi `5`
12. Klik `[Save]`
13. Verifikasi toast sukses "Success, subscription has been updated."
14. Verifikasi status tetap Waiting for Approval
15. Buka modal Changelog Client `PT Bintang Timur+{runId}-060` — FAMS
16. Verifikasi entri baru Action `Edit (Trial — Duration)`, Field `Duration`, Old `30 days`, New `14 days`, Modified By `Fajar N`
17. Verifikasi entri baru Action `Edit (Trial — Asset Quota, FAMS/SAMS)`, Field `Asset Quota`, Old `50`, New `25`, Modified By `Fajar N`
18. Verifikasi entri baru Action `Edit (Trial — Concurrent User Quota)`, Field `Concurrent User Quota`, Old `10`, New `5`, Modified By `Fajar N`

### TC-AC-CS-234: Edit Trial SIEM mengubah Log Source Quota

19. Tutup modal Changelog, ganti isi kotak search dengan `CV Nusantara Data+{runId}-060`, tekan Enter, lalu catat jumlah entri Changelog Client `CV Nusantara Data+{runId}-060` — SIEM sebagai baseline
20. Klik ikon `⋯` pada baris `Subscription ID seed C` lalu pilih `Edit`
21. Ubah Trial Log Source Quota menjadi `20` lalu klik `[Save]`
22. Verifikasi toast sukses "Success, subscription has been updated."
23. Buka modal Changelog Client `CV Nusantara Data+{runId}-060` — SIEM
24. Verifikasi entri baru Action `Edit (Trial — Log Source Quota, SIEM)`, Field `Log Source Quota`, Old `10`, New `20`

### TC-AC-CS-550: Alokasi lisensi term yang kembali Waiting for Approval tetap Pending dan dibekukan

25. Tutup modal Changelog, ganti isi kotak search dengan `Toko Cahaya Abadi+{runId}-060`, tekan Enter, klik ikon `⋯` pada baris `Subscription ID seed D` lalu pilih `Edit`
26. Ubah Duration menjadi `2` lalu klik `[Save]`
27. Tunggu aksi selesai (dialog/modal tertutup)
28. Buka Detail term; License Quota tampil
29. Verifikasi status term Waiting for Approval
30. Verifikasi kedua alokasi tetap Pending, tidak di-Capture, tidak expired, dan nilainya tidak berubah
31. Geser jam server melewati Start Date term lewat fixture waktu, tunggu satu siklus job, lalu pulihkan jam ke `19/08/26`
32. Muat ulang halaman Detail term
33. Verifikasi scheduled flip tidak mengaktifkan term (status tetap Waiting for Approval)
34. Verifikasi scheduled flip tidak mengaktifkan kedua alokasi (tetap Pending)

## Notes

- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); tutup modal Changelog sebelum aksi berikutnya; `Tunggu aksi selesai (dialog/modal tertutup)` setelah `[Save]` sebelum membuka Detail (8b.8); Search pada kotak terisi ditulis "ganti isi kotak search dengan" (8b.9); pemulihan jam sebelum membuka Changelog (S-09, S-12); log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- Job scheduled flip hanya pemicu kondisi yang diuji pada TC-AC-CS-550 (P-2, KEPUTUSAN 2026-10-21).
- Temuan untuk QA: (1) TC-AC-CS-232 tidak menyebut layar pengamatan Start Date dan End Date baru; spec mengamatinya di Detail term setelah mencatat baseline sebelum Edit. (2) TC-AC-CS-550 Expected b dan c tidak menyebut kolom pengamatan alokasi; spec mengamati License Quota Detail term.
