---
id: TC-AC-ACHA-E2E-023-submit-double-submit-dan-saldo-berubah
title: "Submit Allocate Device: Double-Submit Hanya Memproses Satu Request dan Penolakan Server saat Saldo Berubah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-155
  - TC-AC-ACHA-156
coverage:
  web: automated
---

# Submit Allocate Device: Double-Submit Hanya Memproses Satu Request dan Penolakan Server saat Saldo Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor `PT Global Distribusi` (Hendra Wibowo, Pre-setup #27), `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal #21, `AC_TC_PASSWORD`). Env var `AC_DA_TC_DIST_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan tahap script); password tidak ditulis di spec.
- Data Pre-setup: Client #7 `PT Sejahtera Logistik`; kantong #16 PT Global Distribusi; harga PT ABC #14 (NFC $1.20, BLE Gateway $2.00).
- State yang disetel fixture API Pre-setup #20 (disediakan tim FE/BE, tanpa endpoint karangan): saldo kantong PT Global Distribusi $20,000.00 untuk TC-155 dan $100.00 untuk TC-156, Reserved awal $0.00; hook `before` menyetel saldo $20,000.00 dan hook `after` memulihkan saldo, Reserved, dan melepas Reserve pelaku kedua.
- Pelaku kedua (TC-156): sesi API aktor menahan Reserve $40.00 pada kantong PT Global Distribusi lewat fixture (kemampuan disediakan tim FE/BE; sesi API tidak dihitung sebagai sesi web).
- Data Dinamis: satu alokasi `Completed` (NFC, Quantity 2) dibuat di TC-155. Efek: saldo kantong berkurang $2.40 dan kuota NFC Client bertambah 2; modul tanpa Delete sehingga alokasi tidak dihapus.
- Kemampuan baca state BE (disediakan tim FE/BE): jumlah transaksi pengirim, Reserved dan saldo kantong, serta Wallet Balance.
- Hook suite (dinyatakan sekali di `suite.md`): flag Guided Tooltip halaman Device Allocation disetel true untuk akun aktor dan dipulihkan di `after`, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah saldo dan Reserve kantong (state bersama).

## Test Steps

### Saldo berubah antara cek FE dan commit server (TC-AC-ACHA-156)

1. Setel saldo kantong PT Global Distribusi menjadi $100.00 lewat fixture API Pre-setup #20
2. Catat baseline jumlah transaksi pengirim dan Reserved kantong lewat kemampuan baca state BE
3. Klik `[+ Allocation]`
4. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `50`
5. Pelaku kedua (sesi API) menahan Reserve $40.00 pada kantong PT Global Distribusi hingga Reserve tersimpan, sehingga saldo tersedia berubah dari $100.00 menjadi $60.00
6. Klik `[Submit]`
7. Verifikasi Submit ditolak server tanpa mengubah data: tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
8. Verifikasi Reserve tidak berubah (Reserved tetap $40.00 dari pelaku kedua)
9. Verifikasi form tetap terbuka
10. Verifikasi input dipertahankan: Category, Client, dan Quantity `50` tetap terisi
11. Verifikasi pesan inline "Insufficient balance in your pocket. Available: $60.00. Required: $100.00." tampil
12. Verifikasi `[Submit]` disabled
13. Verifikasi tidak ada toast sukses
14. Verifikasi tidak ada dialog
15. Klik `[×]`
16. Verifikasi dialog Unsaved Changes tampil
17. Klik `[Leave]`

### Double-submit oleh aktor sama (TC-AC-ACHA-155)

18. Lepas Reserve $40.00 pelaku kedua dan setel saldo kantong PT Global Distribusi menjadi $20,000.00 lewat fixture API Pre-setup #20 hingga tersimpan
19. Catat baseline jumlah transaksi pengirim lewat kemampuan baca state BE
20. Klik `[+ Allocation]`
21. Pilih Category `TAG - NFC`, Client `PT Sejahtera Logistik`, isi Quantity `2`
22. Klik `[Submit]` dua kali cepat
23. Verifikasi `[Submit]` masuk Saving state (loading, disabled) setelah klik pertama
24. Tunggu aksi selesai (form tertutup)
25. Verifikasi hanya satu transaksi dibuat (jumlah transaksi bertambah satu dari baseline)
26. Buka Wallet Balance kantong PT Global Distribusi
27. Verifikasi saldo berkurang satu kali: $19,997.60 (berkurang $2.40)

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-155 dan TC-156 sama-sama double-submit atau penolakan server pada Submit jalur langsung Distributor; TC-156 memakai pelaku kedua lewat sesi API (bukan konteks kedua UI).
- Penyimpangan urutan (S-10): TC-156 (Submit ditolak, tidak membuat data) dikerjakan lebih dulu dan berakhir dengan form yang ditutup lewat `[×]`, dialog Unsaved Changes, `[Leave]` (S-08); TC-155 yang membuat data (submit sukses) dan berpindah ke Wallet Balance ditaruh paling akhir. Konsekuensinya saldo kantong dan Reserve pelaku kedua dari TC-156 dipulihkan lewat fixture pada langkah 18 sebelum TC-155.
- Langkah penghubung (S-03): pencatatan baseline (langkah 2 dan 19), penyetelan dan pemulihan fixture (langkah 1 dan 18; langkah 18 juga melepas Reserve pelaku kedua), serta "Tunggu aksi selesai" (langkah 24) sebelum membaca jumlah transaksi dan berpindah ke Wallet Balance.
- Asersi "hanya satu transaksi dibuat" (TC-155) memakai jumlah transaksi dari kemampuan baca state BE; TC tidak menyebut cara membuktikannya.
- Pengecualian S-12 nama literal: nama entitas dan Client Pre-setup literal (sudah ada di environment).
- Temuan untuk QA:
  - TC-155 Expected a menyebut Saving state tetapi tidak menyebut cara mengamati sebelum respons selesai; spec mengasersi segera sesudah klik kedua sesuai TC.
  - TC-155 Expected b hanya menyebut "$2.40" (saldo berkurang) tanpa saldo akhir; spec mengasersi saldo akhir $19,997.60 dari saldo awal $20,000.00 (Pre-setup #16).
  - TC-156 menulis "Reserve tidak berubah" tanpa nilai; spec mengasersi Reserved tetap $40.00 (Reserve pelaku kedua).
  - Post Condition TC-155 (Wallet Transaction List, Client Dashboard, panel Stock Balance Summary) tidak punya langkah observasi di TC dan tidak diasersi.
