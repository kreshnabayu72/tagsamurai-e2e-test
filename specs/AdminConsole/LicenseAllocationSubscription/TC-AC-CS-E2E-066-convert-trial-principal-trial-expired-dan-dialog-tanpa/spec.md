---
id: TC-AC-CS-E2E-066-convert-trial-principal-trial-expired-dan-dialog-tanpa
title: "Convert Trial: Principal, Trial Expired, dan Dialog Tanpa Estimated Cost"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-242
  - TC-AC-CS-552
  - TC-AC-CS-248
  - TC-AC-CS-247
coverage:
  web: automated
---

# Convert Trial: Principal, Trial Expired, dan Dialog Tanpa Estimated Cost

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Klinik Harapan Bunda+{runId}-066` (binaan ganda; padanan Pre-setup #43) dengan trial Active SAMS Growth (Start `10/08/26`, End `08/09/26`, Plan Owner CV Karya Mandiri) tanpa term paid SAMS (padanan #71, aktor Principal tanpa Wallet) dan trial Expired FAMS Starter (Start `01/07/26`, End `30/07/26` terlewati, Plan Owner CV Karya Mandiri (Partner)) tanpa term paid FAMS (padanan #72); Client `Toko Lancar Jaya+{runId}-066` (binaan langsung PT Maju Bersama) dengan trial SAMS Professional Active (Start `10/08/26`, End `08/09/26`, Plan Owner PT ABC (Principal)) tanpa term paid SAMS (padanan #112). Tanggal acuan uji `19/08/26`.
- Data Dinamis: term paid hasil Convert (TC-AC-CS-248 dan TC-AC-CS-247) dan perubahan status trial ikut dihapus bersama Client seed di hook `after`; satu-satunya state global adalah jam (fixture waktu), dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu tanggal acuan `19/08/26` (dipulihkan di hook `after`); membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-552 dan TC-AC-CS-242: Dialog Convert Trial oleh Principal dan Go Back

1. Ketik Search `Klinik Harapan Bunda+{runId}-066`, tekan Enter, lalu catat jumlah entri Changelog Client `Klinik Harapan Bunda+{runId}-066` — SAMS sebagai baseline
2. Klik ikon `⋯` pada baris trial Active SAMS Growth lalu pilih `Convert`
3. Verifikasi modal Convert Trial tampil dengan field Plan dan Duration
4. Verifikasi field Pay From dan blok Payment tidak dirender pada modal
5. Pilih Plan `Professional`, isi Duration `1` lalu klik `[Submit]`
6. Verifikasi dialog memuat bullet "• Klinik Harapan Bunda+{runId}-066 — SAMS"
7. Verifikasi dialog memuat notice bypass (jalur instan)
8. Verifikasi dialog memuat penutup "Are you sure you want to convert it?"
9. Verifikasi baris Feature pricing charge (Estimated Cost) tidak ditampilkan pada dialog
10. Klik `[Go Back]`
11. Verifikasi dialog tertutup dan form Convert tetap terbuka dengan input dipertahankan
12. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
13. Verifikasi trial tetap Active
14. Verifikasi tidak ada term paid baru Client `Klinik Harapan Bunda+{runId}-066` — SAMS
15. Verifikasi jumlah entri Changelog sama dengan baseline

### TC-AC-CS-248: Convert ke plan berperingkat lebih rendah tetap berhasil

16. Ganti isi kotak search dengan `Toko Lancar Jaya+{runId}-066`, tekan Enter
17. Klik ikon `⋯` pada baris trial SAMS Professional lalu pilih `Convert`
18. Pilih Plan `Growth` (rank lebih rendah dari plan trial Professional), isi Duration `1`, klik `[Submit]` lalu klik `[Convert]`
19. Verifikasi Convert berhasil dan tidak diblokir
20. Verifikasi term paid SAMS plan Growth terbentuk tanpa penolakan
21. Klik tab `History`, ganti isi kotak search dengan `Toko Lancar Jaya+{runId}-066`, tekan Enter
22. Verifikasi trial berstatus Converted
23. Klik tab `Current`

### TC-AC-CS-247: Convert dari trial Expired: tanpa dialog, trial tetap Expired, Start Date hari ini

24. Ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-066`, tekan Enter, lalu catat jumlah entri Changelog Client `Klinik Harapan Bunda+{runId}-066` — FAMS sebagai baseline
25. Klik ikon `⋯` pada baris trial Expired FAMS Starter lalu pilih `Convert`
26. Verifikasi Start Date mode New terkunci `19/08/26`
27. Pilih Plan `Growth`, isi Duration `1` lalu klik `[Submit]`
28. Verifikasi term paid baru berstatus Active
29. Verifikasi dialog Convert Trial tidak tampil
30. Verifikasi trial FAMS Starter tetap Expired dan tidak menjadi Converted
31. Buka modal Changelog Client `Klinik Harapan Bunda+{runId}-066` — FAMS
32. Verifikasi sedikitnya satu entri baru dari pembuatan term paid tampil dibanding baseline
33. Verifikasi tidak ada entri baru dengan Action `Convert`
34. Tutup modal Changelog lalu buka Detail term paid baru
35. Verifikasi Previous Subscription term baru tidak menunjuk baris trial

## Notes

- TC-AC-CS-552 dan TC-AC-CS-242 memakai aksi yang sama (Principal, trial `Klinik Harapan Bunda+{runId}-066` SAMS, Plan `Professional`, Duration `1`, `[Submit]`, lalu `[Go Back]`); satu alur memenuhi Expected kedua TC.
- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-242 dan TC-AC-CS-552 (tanpa perubahan data) di awal; TC-AC-CS-248 dan TC-AC-CS-247 (Convert yang mengubah data) di akhir. TC-AC-CS-252 dan TC-AC-CS-253 ada di spec 149.
- TC-AC-CS-247 Expected c memuat asersi absence log `Convert`; ditulis dengan baseline jumlah entri Changelog dan anchor entri baru dari pembuatan term (S-05, S-12). Alasan P-1: asersi itu hanya bermakna dengan state berat yang baru dibangun aksi Convert dari trial Expired di spec yang sama.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; langkah 16, 21, dan 24 mengganti isi kotak search, 8b.9); pindah tab `History` dan `Current` untuk trial Converted; `✕`, dialog `Unsaved Changes`, dan `[Leave]` menutup form dirty (S-08, S-09); tutup modal Changelog sebelum aksi berikutnya; log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- Alasan melewati sekitar 35 langkah bila dihitung penuh: semua blok satu topik (Convert Trial oleh Principal) tanpa kelas harness lain dan berdiri sendiri.
- Temuan untuk QA: (1) TC-AC-CS-552 butir b menyebut "notice bypass" tanpa teks; spec mengasersi notice jalur instan tampil tanpa teks persis. (2) TC-AC-CS-248 Post Condition (Downgrade Lifecycle dipicu) tanpa langkah observasi sehingga tidak diasersi. (3) TC-AC-CS-247 butir d (Previous Subscription term baru tidak menunjuk baris trial) diamati di Detail term paid baru.
