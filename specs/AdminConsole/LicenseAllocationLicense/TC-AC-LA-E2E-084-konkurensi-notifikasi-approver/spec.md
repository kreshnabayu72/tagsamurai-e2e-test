---
id: TC-AC-LA-E2E-084-konkurensi-notifikasi-approver
title: "Konkurensi Notifikasi Approver: Race Notifikasi dan Notifikasi Basi"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-440
  - TC-AC-LA-515
coverage:
  web: automated
---

# Konkurensi Notifikasi Approver: Race Notifikasi dan Notifikasi Basi

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10, approver pertama), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Additional Approver `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` (`Maya Tanjung`, Pre-setup #11, approver kedua), password `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup #41): dua alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve), satu untuk TC-AC-LA-440 dan satu untuk TC-AC-LA-515. Allocation ID dibaca dari hasil seeding. Notifikasi `Waiting for your approval` kedua seed sudah tersedia untuk Maya Tanjung.
- Pelaku kedua: Approve oleh `Fajar Nugroho` lewat sesi API (login API tidak dihitung sebagai sesi web, `suite.md`). Sesi UI Maya Tanjung dipakai karena hasilnya diasersi.
- Kemampuan teknis (disediakan tim FE/BE): memutus koneksi push SSE tab Maya Tanjung (mode offline) tanpa memuat ulang daftar notifikasi, lalu memulihkannya di hook `after`. Jendela tunggu update SSE 5 detik adalah pilihan spec, bukan nilai TC atau PRD.
- State global yang diubah: koneksi SSE tab (dipulihkan di hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-440: Race notifikasi, notifikasi approver kedua berstatus Read dan tombol Detail tidak tampil

1. Ganti akun: logout `Fajar Nugroho`, login sebagai `Maya Tanjung` dengan `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`, lalu buka daftar notifikasi
2. Pelaku kedua (sesi API `Fajar Nugroho`) meng-Approve alokasi seed 440 dari Approvals > License Allocation hingga tersimpan
3. Tunggu update SSE masuk pada sesi `Maya Tanjung`
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Buka daftar notifikasi
6. Verifikasi notifikasi alokasi seed 440 berstatus Read
7. Verifikasi tombol `[Detail]` tidak tampil sama sekali (bukan sekadar disabled)

### TC-AC-LA-515: Race notifikasi basi, klik Detail menampilkan popup inline

8. Buka daftar notifikasi `Maya Tanjung`
9. Verifikasi notifikasi alokasi seed 515 berstatus Unread dengan tombol `[Detail]` tampil (sebelum Approve pertama)
10. Putuskan koneksi push SSE tab ini (mode offline) tanpa memuat ulang daftar
11. Pelaku kedua (sesi API `Fajar Nugroho`) meng-Approve alokasi seed 515 dari Approvals > License Allocation hingga tersimpan
12. Tunggu aksi selesai
13. Klik `[Detail]` pada notifikasi alokasi seed 515 di tab yang belum menerima update
14. Verifikasi popup inline `This transaction no longer needs your action.` tampil pada daftar notifikasi yang sama tanpa redirect ke halaman Review atau halaman lain
15. Tutup popup inline
16. Verifikasi notifikasi alokasi seed 515 berstatus Read
17. Verifikasi tombol `[Detail]` hilang dari item
18. Verifikasi tidak ada keputusan kedua tercatat pada alokasi seed 515

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (ganti akun dan membuka notifikasi), 4 (jendela amat SSE 5 detik tanpa Verifikasi, bagian 6), 5, 8 (membuka daftar notifikasi), 12 (menunggu aksi selesai karena berganti sesi, 8b butir 8), 15 (menutup popup).
- Langkah 7 adalah asersi absence atas elemen UI; anchor positif adalah langkah 6 (notifikasi alokasi itu tampil berstatus Read pada daftar yang sama, 8b butir 2). Langkah 17 beranchor langkah 16.
- Pelaku kedua lewat sesi API (langkah 2, 11) tidak memakai butir `P-2` (bagian 3).
- Temuan untuk QA:
  - TC-AC-LA-440 Langkah 2 ("tunggu update SSE masuk") tidak menyebut durasi tunggu; spec memakai jendela 5 detik sebagai pilihan spec.
  - TC-AC-LA-440 dan TC-AC-LA-515 tidak menyebut cara mengumpulkan notifikasi `Waiting for your approval` untuk Maya Tanjung; spec mengandalkan notifikasi hasil seeding.
  - TC-AC-LA-515 Langkah 1 ("putuskan koneksi push SSE", mode offline) tidak menyebut mekanisme; disediakan tim FE.
  - TC-AC-LA-515 Expected b ("Setelah popup ditutup") tidak menyebut cara menutup popup; spec menutup lewat langkah penghubung 15 tanpa menyebut tombol.
