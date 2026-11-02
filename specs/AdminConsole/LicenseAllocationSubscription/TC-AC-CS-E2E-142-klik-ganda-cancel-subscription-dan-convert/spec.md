---
id: TC-AC-CS-E2E-142-klik-ganda-cancel-subscription-dan-convert
title: "Klik Ganda Cancel Subscription dan Convert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-524
  - TC-AC-CS-527
  - TC-AC-CS-267
coverage:
  web: automated
---

# Klik Ganda Cancel Subscription dan Convert

## Prerequisites

- Mode: FE+BE. Respons endpoint ditahan (delay) lewat `Spectra.intercept()` di atas backend nyata untuk mengamati state submitting; penahanan respons bukan kelas fault injection (bagian 3 prinsip 13b).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-142`): term Active `T524` (Subscription ID dibaca lewat API seeding; setara `SUBS-20260819-00005`, Pre-setup #63: Client Salon Cantik Indah, SAMS, Growth, Plan Owner PT Maju Bersama); trial `T527` (Subscription ID dibaca lewat API seeding) SAMS Growth Active (Start 10/08/26, End 08/09/26, Plan Owner CV Karya Mandiri, tanpa term paid SAMS; setara #71); term Active `T267` (Subscription ID dibaca lewat API seeding; setara `SUBS-20260101-00001`, #61). Jumlah entri Changelog dan jumlah record Cancel/Convert dicatat sebagai baseline sebelum langkah pertama (S-12).
- Kemampuan teknis (disediakan tim FE/BE): menahan dan melepas respons endpoint Cancel Subscription dan Convert lewat `Spectra.intercept()` (path tidak tertulis di TC, PRD, atau LLD, S-13); klik dua kali cepat (dua klik terkirim) oleh runner; membaca jumlah term, record Convert, dan entri Changelog sebagai state data; Cancel Subscription memengaruhi Wallet/alokasi milik term seed spec sehingga tidak ada Pre-setup bersama yang berubah; jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after` (status trial Active dan Start Date Convert hari ini bergantung pada tanggal acuan).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-524: Klik ganda Cancel Subscription

1. Tahan respons endpoint Cancel Subscription lewat `Spectra.intercept()`
2. Ketik Search `T524`, tekan Enter
3. Klik ikon `⋯` pada term `T524`, klik `Cancel Subscription` (dialog terbuka)
4. Klik tombol `[Cancel Subscription]` dua kali cepat
5. Verifikasi tombol `[Cancel Subscription]` Loading setelah klik pertama
6. Verifikasi `[Go Back]` Disabled setelah klik pertama
7. Lepas tahanan respons
8. Verifikasi dialog tertutup (respons selesai diproses)
9. Verifikasi hanya satu pembatalan diproses untuk term `T524` (dibaca lewat fixture backend)
10. Verifikasi hanya satu entri log `Cancel` bertambah dari baseline
11. Klik tab `History`
12. Ganti isi kotak search dengan `T524`, tekan Enter
13. Verifikasi baris term `T524` tampil berstatus Archive
14. Klik `(←)` pada kotak Search, klik tab `Current`

### TC-AC-CS-527: Klik ganda Convert pada dialog Convert Trial

15. Tahan respons endpoint Convert lewat `Spectra.intercept()`
16. Ketik Search `T527`, tekan Enter
17. Klik ikon `⋯` pada trial `T527`, klik `Convert Trial`, pilih Plan `Professional`, isi Duration `1`, klik `[Submit]`
18. Klik tombol `[Convert]` dua kali cepat
19. Lepas tahanan respons
20. Verifikasi dialog Convert Trial tertutup (respons selesai diproses)
21. Verifikasi hanya satu konversi diproses untuk trial `T527` (dibaca lewat fixture backend)
22. Klik tab `History`
23. Ganti isi kotak search dengan `T527`, tekan Enter
24. Verifikasi baris trial `T527` tampil berstatus Converted
25. Verifikasi hanya satu term paid dan satu record `Convert` bertambah dari baseline
26. Klik `(←)` pada kotak Search, klik tab `Current`

### TC-AC-CS-267: State dialog Cancel Subscription saat request berjalan

27. Tahan respons endpoint Cancel Subscription lewat `Spectra.intercept()`
28. Ketik Search `T267`, tekan Enter
29. Klik ikon `⋯` pada term `T267`, klik `Cancel Subscription` (dialog terbuka)
30. Klik tombol `[Cancel Subscription]`
31. Verifikasi tombol `[Cancel Subscription]` Loading
32. Verifikasi `[Go Back]` Disabled
33. Lepas tahanan respons
34. Verifikasi dialog tertutup
35. Verifikasi toast sukses tampil

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-525, 526, dan 238 (klik ganda Cancel Request dan Save) ada di spec 143.
- Langkah penghubung (S-03): langkah 12, 23 (Search di tab History untuk menemukan baris target, R-16) dan langkah 11, 14, 22, 26 (pindah tab History, kembali ke tab Current, dan mengosongkan Search), serta langkah 7, 19, 33 (melepas tahanan respons segera setelah state sementara diasersi, S-09). Asersi state sementara (Loading, Disabled) pada langkah 5, 6, 31, 32 diletakkan sebelum respons dilepas (bagian 8b butir 5 dan 11).
- Langkah 8, 20, dan 34 adalah anchor bahwa respons sudah diproses sebelum membaca state data (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-AC-CS-267 Expected b menyebut "toast sukses" tanpa teks; teks toast Cancel Subscription tidak ada di TC ini sehingga hanya kehadirannya diasersi (S-02).
  - TC-AC-CS-527 tidak menyebut label tombol konfirmasi akhir; spec memakai `[Convert]` sesuai TC-AC-CS-257.
  - TC-AC-CS-524 dan 267 memakai record Pre-setup (#63, #61) sebagai target aksi tulis; spec memakai record milik spec (S-06).
  - TC-AC-CS-524 Expected a ("satu entri log `Cancel`") tidak menyebut surface log; spec memakai jumlah entri yang dibaca fixture BE.
