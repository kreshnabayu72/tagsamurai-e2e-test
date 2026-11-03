---
id: TC-AC-LA-E2E-135-notifikasi-keputusan-dan-cancel
title: "Notifikasi In-App: Waiting for Approval, License Allocated, Reject, Cancel, dan Unread Actionable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-433
  - TC-AC-LA-439
  - TC-AC-LA-435
  - TC-AC-LA-434
  - TC-AC-LA-436
coverage:
  web: automated
---

# Notifikasi In-App: Waiting for Approval, License Allocated, Reject, Cancel, dan Unread Actionable

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Ganti akun ke Dewi Anggraini dilakukan eksplisit pada blok terakhir; hook `after` mengembalikan sesi ke akun default suite. Flag Guided Tooltip diatur hook `before` suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (approver pool, staf Plan Owner) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update (requester) | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Hendra Wijaya | #1 | Total Control Principal (approver alokasi Principal; hanya lewat sesi API) | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE). Sesi API aktor mengikuti pernyataan di `suite.md`.
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Require Approval for Allocation ON (Pre-setup #38), Default User Principal `Sari P` (Pre-setup #2) sebagai requester alokasi Free.
- Data Dinamis (seed milik spec ini, dibuat lewat Submit oleh requester melalui sesi API di hook `before` supaya notifikasi terbentuk; tidak memakai baris Pre-setup #41 dan #60 bersama): empat alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera: `{idNotif}` (TC-AC-LA-433 dan TC-AC-LA-439), `{idRej}` (TC-AC-LA-435), `{idCan}` (TC-AC-LA-436) oleh requester Dewi Anggraini dengan Cost $150.00 di-Reserve (bentuk Pre-setup #41), dan `{idFree}` (TC-AC-LA-434) oleh requester `Sari P` dengan Payment Free tanpa Reserve (bentuk Pre-setup #60).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi lewat sesi API dan pembersihannya; sesi API aktor (suite) untuk Hendra Wijaya dan Dewi Anggraini sebagai pelaku kedua yang hanya memicu perubahan state.
- State global: saldo kantong #33 dipulihkan oleh pembersihan record di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Notifikasi Waiting for your approval (TC-AC-LA-433)

1. Buka daftar notifikasi in-app
2. Verifikasi notifikasi dengan Title `Waiting for your approval` dan Body `{idNotif} · Concurrent User · PT Sejahtera`, dengan tombol `[Detail]` (actionable)
3. Tutup daftar notifikasi

### Notifikasi actionable tetap Unread sampai keputusan tersubmit (TC-AC-LA-439)

4. Buka daftar notifikasi in-app
5. Klik `[Detail]` pada notifikasi `{idNotif}`
6. Keluar dari halaman Review tanpa Submit
7. Buka daftar notifikasi in-app
8. Verifikasi notifikasi `{idNotif}` tetap Unread
9. Tutup daftar notifikasi
10. Buka Approvals > License Allocation
11. Klik `[Review]` pada alokasi `{idNotif}`
12. Pilih Approve
13. Klik Submit
14. Tunggu aksi selesai
15. Buka daftar notifikasi in-app
16. Verifikasi notifikasi `{idNotif}` menjadi Read setelah keputusan Submit
17. Tutup daftar notifikasi

### Reject oleh approver (TC-AC-LA-435, bagian aksi)

18. Buka Approvals > License Allocation
19. Klik `[Review]` pada alokasi `{idRej}`
20. Pilih Reject
21. Isi Rejection Reason `Kuota tidak sesuai`
22. Klik Submit
23. Tunggu aksi selesai (tombol Submit aktif kembali atau baris keputusan hilang dari Tab Active)

### Notifikasi License allocated ke Plan Owner (TC-AC-LA-434)

24. Approve alokasi `{idFree}` sebagai Hendra Wijaya lewat sesi API hingga status `Active` tersimpan
25. Buka daftar notifikasi in-app
26. Verifikasi Plan Owner PT Maju Bersama (Fajar Nugroho) menerima notifikasi dengan Title `License allocated` dan Body `{idFree} · Concurrent User · PT Sejahtera`, hanya dengan tombol `[Mark as Read]` (view-only)
27. Tutup daftar notifikasi

### Notifikasi Cancel ke approver pool (TC-AC-LA-436)

28. Cancel alokasi `{idCan}` sebagai Dewi Anggraini lewat sesi API hingga status `Canceled` tersimpan
29. Buka daftar notifikasi in-app
30. Verifikasi notifikasi approver dengan Title `License allocation canceled` dan Body `{idCan} · Concurrent User · PT Sejahtera`, view-only ke approver pool
31. Tutup daftar notifikasi

### Notifikasi Reject ke requester (TC-AC-LA-435, bagian notifikasi)

32. Ganti akun: Logout dari Fajar Nugroho
33. Login sebagai Dewi Anggraini (`dewiFullLic`, password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`)
34. Buka daftar notifikasi in-app
35. Verifikasi notifikasi requester dengan Title `License allocation rejected` dan Body `{idRej} · Concurrent User · PT Sejahtera`, view-only

## Notes

- Urutan blok berbeda dari urutan sourceTc: pelaku kedua (Hendra Wijaya dan Dewi Anggraini) memicu perubahan lewat sesi API sehingga ganti akun UI hanya satu kali ke Dewi Anggraini (S-07), dan TC-AC-LA-435 dipecah menjadi bagian aksi (Fajar Nugroho) dan bagian notifikasi (Dewi Anggraini) yang ditaruh terakhir.
- Pelaku kedua lewat sesi API (langkah 24 dan 28) bukan konteks kedua dan tidak memakai `P-2`; keduanya ditulis "hingga ... tersimpan" (R-20) dan diikuti pembukaan notifikasi sebagai pengamat UI (langkah 23 adalah "Tunggu aksi selesai" sebelum pelaku API bertindak).
- Langkah penghubung (S-03): langkah 14 (menunggu aksi selesai karena langkah berikutnya berpindah surface, 8b butir 8), langkah 3, 9, 17, 27, dan 31 (menutup daftar notifikasi), langkah 10 dan 18 (berpindah ke Approvals), langkah 23 (tunggu aksi selesai, 8b.8), langkah 32 sampai 34 (ganti akun dan membuka notifikasi).
- Temuan untuk QA:
  - TC-AC-LA-434 mensyaratkan Hendra Wijaya meng-Approve melalui UI dan Fajar Nugroho login; spec memakai sesi API untuk Approve Hendra (pelaku yang hanya memicu perubahan state) dan sesi UI Fajar Nugroho yang sudah login sebagai pengamat notifikasi.
  - TC-AC-LA-436 tidak menyebut akun requester selain Pre-setup #4; spec memakai Dewi Anggraini lewat sesi API untuk pembatalan dan Fajar Nugroho (Pre-setup #10) sebagai approver pool.
  - TC-AC-LA-433 dan TC-AC-LA-435 menyebut notifikasi `Fajar Nugroho` dan `Dewi Anggraini` tanpa menyebut cara membedakan notifikasi dari alokasi lain; spec mengenali notifikasi lewat Allocation ID pada Body.
  - TC-AC-LA-439 langkah 1 ("Klik `[Detail]` lalu keluar dari Review tanpa Submit") tidak menyebut cara keluar dari halaman Review; spec memakai kontrol keluar halaman Review tanpa Submit.
