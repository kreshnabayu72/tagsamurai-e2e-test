---
id: TC-FA-FAAM-E2E-155-changelog-setup-column-reset-independen-dan-paginasi
title: "Modal Changelog: Reset to Default, Discard, Guard Satu Kolom, Independen dari Tabel Utama, dan Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-494
  - TC-FA-FAAM-495
  - TC-FA-FAAM-496
coverage:
  web: automated
---

# Modal Changelog: Reset to Default, Discard, Guard Satu Kolom, Independen dari Tabel Utama, dan Paginasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28). Changelog client utama memuat lebih dari 10 entri (seed ditambah entri audit trail yang sudah ada) sehingga tombol Next pada paginasi tersedia (TC-FA-FAAM-496). Konfigurasi kolom bawaan: `Date | Action | Asset Name | Field | Old Value | New Value | Modified By`. Tabel utama memuat 12 kolom data (`Fixture.faAssetName.catalog`): `Asset Name`, `Code`, `Category`, `TAG Type`, `Brand`, `Model/Type`, `Default Addon`, `Default Label`, `UoM`, `Total Asset`, `Modified By`, `Last Updated`.
- Kemampuan teknis: hapus preferensi kolom Changelog di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom Changelog (preferensi di browser) diubah spec ini. Pemulihan: langkah 29 menghapus preferensi kolom di browser, dan hook `after` melakukannya sebagai cadangan (bukan `[Reset to Default]` di akhir; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAM-494: Reset to Default, discard lewat X, dan guard satu kolom pada Setup Column Changelog

2. Klik header Actions (⋯), lalu klik `Setup Column...`
3. Uncheck `Field`
4. Klik `[Save]`
5. Klik header Actions (⋯), lalu klik `Setup Column...`
6. Klik `[Reset to Default]`
7. Klik `[Save]`
8. Verifikasi tabel Changelog memuat 7 kolom default `Date | Action | Asset Name | Field | Old Value | New Value | Modified By`
9. Klik header Actions (⋯), lalu klik `Setup Column...`
10. Uncheck `Action`, `Asset Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` hingga hanya `Date` tersisa
11. Arahkan kursor ke checkbox `Date`
12. Verifikasi checkbox kolom tersisa `Date` disabled dengan tooltip `At least one column must remain visible.`
13. Klik `[✕]` pada popup Setup Column

### TC-FA-FAAM-495: Konfigurasi kolom Changelog independen dari tabel utama

14. Klik header Actions (⋯), lalu klik `Setup Column...`
15. Uncheck `Field`
16. Klik `[Save]`
17. Tekan Esc
18. Verifikasi tabel utama memuat 12 kolom data `Asset Name | Code | Category | TAG Type | Brand | Model/Type | Default Addon | Default Label | UoM | Total Asset | Modified By | Last Updated`
19. Klik icon Changelog

### TC-FA-FAAM-496: Paginasi Changelog: default 10 dan pilihan page size

20. Verifikasi footer pagination default 10 data per halaman
21. Klik dropdown page size
22. Verifikasi pilihan page size `10`, `25`, `50`, `100`
23. Pilih `10`
24. Klik Next
25. Verifikasi halaman 2 aktif
26. Ganti page size ke `25`
27. Verifikasi tabel kembali ke halaman 1
28. Ganti page size ke `50`, lalu ganti ke `100`
29. Pulihkan konfigurasi kolom Changelog ke bawaan: hapus preferensi kolom di browser, tekan F5

## Notes

- Urutan di spec: TC-FA-FAAM-494, lalu TC-FA-FAAM-495 (menyimpan konfigurasi tanpa Field), dan TC-FA-FAAM-496 paling akhir (paginasi tidak bergantung pada konfigurasi kolom). Konfigurasi dipulihkan di langkah 29.
- Langkah penghubung (aksi tanpa `Verifikasi`): menyimpan Field tersembunyi sebagai keadaan awal sebelum Reset to Default (langkah 3 dan 4), menutup modal Changelog dengan Esc sebelum melihat tabel utama (langkah 17), membuka kembali Changelog (langkah 19), memilih `10` untuk menutup dropdown page size (langkah 23), dan berpindah ke halaman 2 sebagai prasyarat asersi pada langkah 27 (langkah 24 dan 25). Ukuran 50 dan 100 pada langkah 28 hanya dipilih karena TC tidak menyebut hasilnya.
- Urutan langkah TC-FA-FAAM-496 berbeda dari TC: Next dijalankan sebelum mengganti page size supaya "kembali ke halaman 1" teramati (bagian 8b butir 5).
- Asersi ketiadaan pada langkah 12 (kolom tersisa tak dapat di-uncheck) tidak memerlukan anchor tambahan karena langkah 10 memperlihatkan popup dan kolom yang tersisa.
- Temuan untuk QA:
  - TC-FA-FAAM-494 judul menyebut "discard lewat X", tetapi Langkah Uji dan Expected tidak memuat discard; spec hanya menutup popup dengan `[✕]` (langkah 13) tanpa Verifikasi.
  - TC-FA-FAAM-496 Expected c ("Ganti page size ke halaman 1") bergantung pada Next yang berada setelah langkah ganti page size di TC; spec membalik urutan itu.
  - TC-FA-FAAM-496 tidak menyebut jumlah entri minimal yang dibutuhkan agar Next tersedia pada page size 25.
