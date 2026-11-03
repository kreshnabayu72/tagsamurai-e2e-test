---
id: TC-AC-CS-E2E-150-state-tenant-trial-expired-pada-dropdown-convert-dan-activate-trial
title: "State Tenant: Trial Expired pada Dropdown, Convert, dan Activate Trial"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-532
  - TC-AC-CS-533
coverage:
  web: automated
---

# State Tenant: Trial Expired pada Dropdown, Convert, dan Activate Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state data milik spec.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-150`): Client `Klinik Harapan Bunda+{runId}-150` (setara `Klinik Harapan Bunda`, Pre-setup #43, binaan langsung PT Maju Bersama pada group `Jawa` dan CV Karya Mandiri) dengan trial FAMS Starter Expired (setara #72: Start `01/07/26`, End `30/07/26` terlewati, Plan Owner CV Karya Mandiri (Partner)) tanpa term paid FAMS dan tanpa trial Waiting atau Active FAMS; tanggal acuan uji `19/08/26`.
- Data Dinamis: term paid hasil Convert dan trial Growth hasil Activate Trial adalah milik Client seed spec ini; keduanya dibersihkan di hook `after` dan dipulihkan ke trial Expired oleh fixture backend pemulihan state (disediakan tim FE/BE) sebagai langkah penghubung. Efeknya (Last Updated dan entri audit trail) dicatat di sini.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu tanggal acuan `19/08/26` (dipulihkan di hook `after`); membaca daftar Asset Client dan jumlah entri Changelog.

## Test Steps

### TC-AC-CS-532: Trial Expired di tab Current menyisihkan kombinasi dari + Subscription dan pembelian lewat Convert

1. Ketik Search `Klinik Harapan Bunda+{runId}-150`, tekan Enter, lalu catat jumlah Asset Client dan jumlah entri Changelog Client `Klinik Harapan Bunda+{runId}-150` — FAMS sebagai baseline
2. Klik `[+ Subscription]`, pilih Client `Klinik Harapan Bunda+{runId}-150`, lalu buka dropdown Product
3. Verifikasi dropdown Product memuat sedikitnya satu opsi Product
4. Verifikasi Product `FAMS` tidak tersedia pada dropdown Product
5. Klik `[✕]`
6. Verifikasi dialog Unsaved Changes tampil
7. Klik `[Leave]`
8. Klik ikon `⋯` pada baris trial FAMS Starter lalu pilih `Convert`
9. Verifikasi Start Date mode New terkunci hari ini `19/08/26` (Disabled)
10. Pilih Plan `Growth`, isi Duration `1`
11. Klik `[Submit]`
12. Verifikasi term paid baru berstatus Active
13. Verifikasi dialog Convert Trial tidak tampil
14. Verifikasi trial FAMS Starter tetap berstatus Expired dan tidak menjadi Converted
15. Buka modal Changelog Client `Klinik Harapan Bunda+{runId}-150` — FAMS
16. Verifikasi sedikitnya satu entri baru dari pembuatan term paid tampil di Changelog dibanding baseline
17. Verifikasi tidak ada entri baru dengan Action `Convert`
18. Tutup modal Changelog lalu buka Detail term paid baru
19. Verifikasi Previous Subscription term baru tidak menunjuk baris trial ("—")
20. Verifikasi jumlah Asset Client sama dengan baseline

### TC-AC-CS-533: Activate Trial plan lain diizinkan saat ada trial Expired produk sama

21. Pulihkan Client `Klinik Harapan Bunda+{runId}-150` ke trial FAMS Starter Expired tanpa term paid FAMS lewat fixture backend, lalu buka Allocation > Client Subscription tab Current
22. Klik `[+ Activate Trial]`, pilih Client `Klinik Harapan Bunda+{runId}-150` dan Product `FAMS`
23. Buka dropdown Plan
24. Verifikasi Plan `Growth` tampil pada dropdown Plan
25. Verifikasi Plan `Starter` tidak tampil pada dropdown Plan
26. Pilih Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
27. Klik `[Submit]`
28. Tunggu aksi selesai (dialog/modal tertutup)
29. Ketik Search `Klinik Harapan Bunda+{runId}-150`, tekan Enter
30. Verifikasi trial Growth Active berhasil dibuat

## Notes

- TC-AC-CS-532 memuat asersi absence log `Convert` (Expected c) dengan baseline jumlah entri Changelog dan anchor entri baru dari pembuatan term (S-05, S-12); alasannya P-1: asersi itu hanya bermakna dengan state berat yang baru dibangun aksi Convert pada trial Expired di spec yang sama.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); `Tunggu aksi selesai` sesudah `[Submit]` Activate Trial sebelum Search (8b.8); `✕`, dialog `Unsaved Changes`, dan `[Leave]` menutup form dirty (S-08, S-09); pemulihan trial Expired lewat fixture; tutup modal Changelog; log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- TC-AC-CS-549, TC-AC-CS-268, dan TC-AC-CS-531 ada di spec 055.
- Temuan untuk QA: TC-AC-CS-532 Expected d tidak menyebut jumlah Asset Client `Klinik Harapan Bunda+{runId}-150`; spec mencatatnya sebagai baseline sebelum Convert.
