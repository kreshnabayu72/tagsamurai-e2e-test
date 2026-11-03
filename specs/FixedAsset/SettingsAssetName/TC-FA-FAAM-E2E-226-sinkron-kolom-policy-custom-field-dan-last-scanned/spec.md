---
id: TC-FA-FAAM-E2E-226-sinkron-kolom-policy-custom-field-dan-last-scanned
title: "Sinkron ke Tab Total Assets: Policy Transaksi, Nilai-Status Custom Field, dan Pemindaian Audit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-797
  - TC-FA-FAAM-798
  - TC-FA-FAAM-799
coverage:
  web: automated
---

# Sinkron ke Tab Total Assets: Policy Transaksi, Nilai-Status Custom Field, dan Pemindaian Audit

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor (sesi UI 1): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Pelaku kedua ("sesi 2", Total Control yang sama) bekerja lewat sesi API aktor (suite.md) hanya sebagai pemicu perubahan state; hasilnya diasersi di sesi UI 1. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 34, 34b, 34c (fixture dasar).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-226` (Tabel Data Uji Dinamis No. 108, 109, 110):
  - `Column Sync Item 797 {runId}-226` (Total Asset 1, policy Borrow `On`, lainnya `Off`).
  - `Column Sync Item 798 {runId}-226` (Total Asset 1, aset `AST-2201`) dengan custom field `Sync Field 798 {runId}-226` (Text, General, Scope `Column Sync Item 798 {runId}-226`, nilai `Old`).
  - `Column Sync Item 799 {runId}-226` (Total Asset 1, aset `AST-2301`, belum pernah dipindai) pada task Audit aktif.
- Kemampuan teknis: Setup Column pada tab Total Assets (konfigurasi kolom tersimpan di browser dan dipulihkan di hook `after` dengan menghapus preferensi kolom; kemampuan disediakan tim FE); pelaku kedua lewat sesi API untuk mengubah policy transaksi, nilai dan status custom field, serta memindai aset pada task Audit hingga tersimpan.
- NC-25 (ikon final kolom Transactional Policy) belum dikonfirmasi: asersi sel Transactional Policy hanya memeriksa jumlah ikon, urutan, dan label aksesibilitas, bukan bentuk ikon.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini lewat API dan hapus preferensi kolom di browser.
- State global yang diubah: konfigurasi kolom Setup Column di browser (dipulihkan seperti di atas); spec ini belum tercantum pada daftar spec penyimpan konfigurasi kolom di `suite.md` (lihat Temuan untuk QA). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-797, 798, 799: login sebagai Total Control (dua sesi) dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-797: Policy Transaksi langsung terlihat di kolom Transactional Policy

1. Ketik Search `Column Sync Item 797 {runId}-226`, tekan Enter
2. Klik nama `Column Sync Item 797 {runId}-226`
3. Klik tab `Total Assets (1)`
4. Tampilkan kolom Transactional Policy lewat Setup Column
5. Verifikasi sel Transactional Policy menampilkan satu ikon dengan label aksesibilitas Borrow
6. Pelaku kedua (sesi API Total Control) mengaktifkan Self Service Borrow untuk `Column Sync Item 797 {runId}-226` di Settings > Asset Transactional Policy hingga tersimpan
7. Verifikasi sel Transactional Policy menampilkan dua ikon berurutan Borrow lalu Self Service Borrow tanpa memuat ulang halaman
8. Pelaku kedua mengembalikan policy `Column Sync Item 797 {runId}-226` ke Borrow `On` saja hingga tersimpan
9. Tutup Popup Detail

### TC-FA-FAAM-798: Nilai dan status Custom Field langsung terlihat di kolom custom field

10. Ketik Search `Column Sync Item 798 {runId}-226`, tekan Enter
11. Klik nama `Column Sync Item 798 {runId}-226`
12. Klik tab `Total Assets (1)`
13. Tampilkan kolom `Sync Field 798 {runId}-226` lewat Setup Column
14. Verifikasi sel `Sync Field 798 {runId}-226` menampilkan `Old`
15. Pelaku kedua mengubah nilai `Sync Field 798 {runId}-226` aset `AST-2201` dari `Old` menjadi `New` hingga tersimpan
16. Verifikasi sel `Sync Field 798 {runId}-226` menampilkan `New` tanpa memuat ulang halaman
17. Pelaku kedua menonaktifkan custom field `Sync Field 798 {runId}-226` hingga tersimpan
18. Verifikasi header tabel tidak memuat kolom `Sync Field 798 {runId}-226` tanpa memuat ulang halaman
19. Buka Popup Setup Column
20. Verifikasi daftar Setup Column tidak memuat `Sync Field 798 {runId}-226` (field Inactive tidak menjadi kolom)
21. Tutup Popup Setup Column
22. Tutup Popup Detail

### TC-FA-FAAM-799: Pemindaian Audit langsung terlihat di kolom Last Scanned

23. Ketik Search `Column Sync Item 799 {runId}-226`, tekan Enter
24. Klik nama `Column Sync Item 799 {runId}-226`
25. Klik tab `Total Assets (1)`
26. Tampilkan kolom Last Scanned lewat Setup Column
27. Verifikasi sel Last Scanned menampilkan `—`
28. Pelaku kedua memindai aset `AST-2301` pada task Audit yang memuat aset itu hingga tersimpan
29. Verifikasi sel Last Scanned menampilkan waktu pemindaian terbaru dalam format General Settings tanpa memuat ulang halaman

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 10, 23 (Search untuk menemukan baris target), langkah 4, 13, 26 (menampilkan kolom lewat Setup Column), langkah 8 (pemulihan policy), langkah 9, 21, 22 (menutup popup), dan langkah 19 (membuka Popup Setup Column).
- Pelaku kedua memakai sesi API karena hanya memicu perubahan state; sesi UI 1 adalah satu-satunya konteks UI yang diasersi (bagian 3 butir P-2, keputusan 2026-10-30).
- Temuan untuk QA:
  - TC-FA-FAAM-797, 798, 799 menyimpan konfigurasi kolom Setup Column tetapi nomor spec ini tidak ada pada daftar spec penyimpan konfigurasi kolom di `suite.md`; pemilik perlu menambahkannya.
  - TC-FA-FAAM-797 menyebut "dua sesi" Total Control; TC tidak menyatakan sesi 2 harus UI, sehingga spec memakai sesi API (kecuali bila QA menghendaki sesi UI yang diasersi).
  - TC-FA-FAAM-799 butir a/b tidak menyebut format Last Scanned selain "format General Settings".
