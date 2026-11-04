---
id: TC-FA-LIC-E2E-169-sesi-lain-online-users-force-logout-ganda-dan-pelepasan-seat
title: "Concurrent User dengan Sesi Lain: Online Users Sinkron, Force Logout Ganda, dan Pelepasan Seat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-87
  - TC-FA-LIC-173
  - TC-FA-LIC-460
coverage:
  web: automated
---

# Concurrent User dengan Sesi Lain: Online Users Sinkron, Force Logout Ganda, dan Pelepasan Seat

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor hook `before`): Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun konteks lain (dibuka dan ditutup di langkah spec, hasilnya diasersi):
  - Total Control kedua (Pre-setup #22) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC2_PASSWORD` (konteks browser B pada TC-FA-LIC-460).
  - Budi Santoso (Pre-setup #14): email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE; dipakai lewat sesi API pada TC-FA-LIC-87.
  - User baru produk FAMS untuk TC-FA-LIC-173: disediakan tim FE (email tidak tertulis di Pre-setup TC).
  Nama env `FA_TC_PASSWORD` dan `FA_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup dan penyetel state): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Jalur menu: Changelog Concurrent User lewat License > Concurrent User > ikon Changelog pada toolbar; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Data Pre-setup yang diubah spec: fixture tabel sesi #26 (lima sesi cuplikan: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso; Online Users 5/25) dan sesi aktif #14 (18 sesi, seat 25; sesi Budi Santoso Chrome on Windows tidak aktif lebih dari 2 jam). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta di awal tiap blok TC (pengecualian S-06: sesi Pre-setup tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: sesi Budi Santoso berakhir, Last Activity berubah, dan entri baru bertambah permanen di Changelog Concurrent User dan Activity Log.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak dikarang):
  - Fixture BE penyetel state: ledger Concurrent User penuh `20/20` (Pre-setup #14 diubah) pada TC-FA-LIC-173.
  - Sesi API akun Budi Santoso untuk logout sendiri hingga logout tersimpan (TC-FA-LIC-87).
  - Membaca jumlah entri Changelog Concurrent User dan Activity Log sebelum aksi (baseline) pada TC-FA-LIC-460.
  - Asersi propagasi SSE didahului "Tunggu 5 detik tanpa memuat ulang halaman" (jendela standar pilihan spec, bukan nilai TC atau PRD). Last Activity berketelitian menit: hook menunggu sampai menit berganti (maksimum 60 detik) sebelum aksi di sesi Rudi pada TC-FA-LIC-87.
- Konteks kedua adalah objek uji kelas c; spec ini tidak memakai `P-2` atau `P-7`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-87: Online Users sinkron dengan jumlah sesi; sesi yang berakhir hilang dan seat dilepas

1. Pulihkan fixture tabel sesi Pre-setup #26 lewat fixture BE (lima sesi, Online Users 5/25)
2. Sesi A: muat ulang tab Concurrent User, hitung baris dan catat Online Users
3. Verifikasi lima baris dan `Online Users: 5/25`
4. Sesi API akun Budi Santoso: logout hingga logout tersimpan
5. Sesi A: tunggu 5 detik tanpa memuat ulang halaman
6. Verifikasi baris Budi Santoso hilang (lewat event SSE Session Management)
7. Verifikasi `Online Users: 4/25`
8. Catat Last Activity Rudi Hartono, tunggu sampai menit berganti, lakukan aksi di sesi Rudi (klik tab Allocation Quota lalu kembali ke tab Concurrent User), muat ulang tab
9. Verifikasi Last Activity Rudi Hartono bertambah mengikuti request terakhir sesi

### TC-FA-LIC-460: Dua sesi Force Logout atas sesi yang sama

10. Pulihkan Pre-setup #14 lewat fixture BE (sesi Budi Santoso aktif) dan catat jumlah entri Changelog Concurrent User dan Activity Log (baseline)
11. Buka konteks browser B, login sebagai Total Control kedua (#22), buka License > Concurrent User
12. Sesi A dan B: ketik Search `Budi`, tekan Enter, lalu klik `[Force Logout]` pada baris Budi Santoso (dialog terbuka di kedua sesi)
13. Sesi A: klik `[Confirm Logout]`
14. Verifikasi sesi A menerima toast sukses
15. Sesi B: klik `[Confirm Logout]`
16. Verifikasi sesi B menampilkan dialog `Session Already Expired` dengan teks `This session is no longer active.`
17. Verifikasi sesi B tanpa toast sukses
18. Sesi A: klik `(←)` pada kotak Search
19. Sesi A: klik ikon Changelog pada toolbar Concurrent User
20. Verifikasi Changelog Concurrent User bertambah tepat satu entri Force Logout untuk Budi Santoso dari sesi A
21. Tutup modal `Changelog: Concurrent User`
22. Buka Fixed Asset > Reports & Logs > Activity Log
23. Verifikasi Activity Log bertambah tepat satu entri Force Logout untuk Budi Santoso dari sesi A
24. Sesi B: klik `[OK]`, lalu tutup konteks B dan hapus sesi login-nya

### TC-FA-LIC-173: Force Logout melepas seat sehingga user lain dapat masuk saat kuota penuh

25. Pulihkan Pre-setup #14 lewat fixture BE dan atur ledger Concurrent User penuh `20/20`
26. Sesi A: buka License > Concurrent User
27. Sesi A: muat ulang tab Concurrent User
28. Verifikasi `Online Users: 20/20`
29. Klik `[Force Logout]` pada satu sesi, klik `[Confirm Logout]`
30. Verifikasi `Online Users: 19/20`
31. Buka konteks browser kedua, login sebagai user baru ke FAMS
32. Verifikasi user baru berhasil masuk produk
33. Verifikasi tidak ada popup Concurrent session limit reached
34. Tutup konteks browser kedua dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 10, dan 25 memulihkan Pre-setup antar blok; langkah 11, 24, 31, dan 34 membuka dan menutup konteks lain (S-09); langkah 5 menunggu jendela SSE (bagian 6); langkah 12 menemukan baris target lewat Search `Budi` (R-16) dan langkah 18 mengosongkan Search itu sebelum sesi A berpindah surface (S-09, bagian 8b butir 9); `Verifikasi` toast sukses sesi A pada langkah 14 menandai `[Confirm Logout]` sesi A selesai sebelum sesi B bertindak pada langkah 15, sehingga sesi B menerima `Session Already Expired` (bagian 8b butir 5 dan 8); langkah 19 sampai 22 membuka satu surface log per kali (Changelog Concurrent User lalu Activity Log) dan menutup modal Changelog (S-14); langkah 26 kembali ke License > Concurrent User sebelum blok TC-FA-LIC-173.
- Urutan blok: TC-FA-LIC-87 (sesi berkurang tanpa Force Logout oleh aktor) lebih dulu; TC-FA-LIC-460 dan 173 (Force Logout oleh aktor) sesudahnya (S-10). Tiap blok dimulai dari pemulihan state lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-LIC-615 dan 179 ada di spec `TC-FA-LIC-E2E-115`.
- Temuan untuk QA:
  - TC-FA-LIC-173 langkah 3 meminta login user baru ke FAMS (produk lain) tanpa data akun; spec menuliskannya sebagai user baru yang disediakan tim FE.
  - TC-FA-LIC-87 memakai akun login Budi Santoso yang email-nya tidak tertulis di Pre-setup TC.
  - TC-FA-LIC-460 langkah 3 menyatakan hasil log ada di Changelog Concurrent User dan Activity Log tanpa nilai jumlah; spec mengasersi selisih satu entri terhadap baseline. Expected TC-FA-LIC-460 tidak menyebut toast sukses secara literal ("toast sukses").
  - TC-FA-LIC-87 langkah 3 ("lakukan aksi di sesi Rudi") tidak menyebut aksinya; spec memakai pindah tab Allocation Quota lalu kembali ke Concurrent User.
  - TC-FA-LIC-173 langkah 2 tidak menyebut sesi mana yang di-Force Logout; spec memilih satu sesi sembarang yang bukan sesi aktor.
