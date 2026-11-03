---
id: TC-AC-ACHA-E2E-010-eksekusi-aksi-per-capability-positif
title: "Role Matrix Positif: Eksekusi Aksi per Capability (Create saja dan Update saja)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-58
  - TC-AC-ACHA-60
  - TC-AC-ACHA-61
  - TC-AC-ACHA-62
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Aksi per Capability (Create saja dan Update saja)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-58, TC-60 | Create dan Read tanpa Update Distributor PT Global Distribusi (alias CO_DIST, toggle ON) | #35 | `createOnlyDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_CO_DIST_PASSWORD` |
| TC-61, TC-62 | Update dan Read tanpa Create Distributor PT Global Distribusi (alias UO_DIST) | #36 | `updateOnlyDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_UO_DIST_PASSWORD` |

- Login akun aktor pertama (CO_DIST) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit dan langkah tiap role berbeda.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup yang diubah spec ini (efek dicatat di sini, bagian S-06): transaksi Canceled milik CO_DIST (Pre-setup #68, TC-60: dipakai sebagai sumber Resubmit; menghasilkan transaksi baru, sumber tetap Canceled), transaksi Waiting for Approval milik UO_DIST (Pre-setup #60: GPS, Quantity 20, Client PT Sejahtera Logistik, Total Cost $160.00; TC-61 mengubah Quantity menjadi 25 lalu TC-62 membatalkannya). Transaksi Waiting for Approval yang dibuat TC-58 dan TC-60 menghasilkan Reserve pada kantong PT Global Distribusi. Fixture baseline (disediakan tim FE/BE) memulihkan Pre-setup #60, #68, dan kantong PT Global Distribusi (saldo $20,000.00, Reserved $0.00) di hook `before` dan di hook `after`; spec ini tidak memuat langkah pemulihan antar blok karena #68 hanya diubah blok TC-60, #60 hanya diubah blok TC-61 dan TC-62, dan saldo atau Reserved kantong tidak diasersi. Allocation ID Pre-setup #60 dan #68 dibaca lewat fixture seed (disediakan tim FE/BE). Efek pada Last Updated dan kuota dipulihkan fixture. Transaksi baru hasil TC-58 dan hasil Resubmit TC-60 berstatus Waiting for Approval dan dibatalkan fixture Pre-setup #20 di hook `after` bersama pemulihan seed 30 baris (Lampiran A butir A-11); hanya transaksi yang dibuat spec ini yang dibatalkan.
- Data Dinamis: transaksi baru hasil TC-58 (BLE Gateway, Client PT Sejahtera Logistik, Quantity 5) dan hasil Resubmit TC-60 (Allocation ID unik runtime, ditangkap sebagai Dynamic Reference dari baris teratas List, tidak di-hardcode).
- Data harga: harga satuan PT ABC (Pre-setup #14): GPS $8.00 (dipakai asersi Total Cost TC-61).
- General Settings Pre-setup #1 tidak diubah. State global: saldo dan Reserved kantong PT Global Distribusi diubah oleh aksi spec dan dipulihkan fixture; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_CO_DIST_PASSWORD` dan `AC_DA_UO_DIST_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-58: Hak Create saja, eksekusi Allocate sampai sukses

1. Klik `[+ Allocation]`
2. Pilih Category `Hardware - BLE Gateway`
3. Pilih Client `PT Sejahtera Logistik`
4. Isi Quantity `5`
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, device allocation has been submitted for approval."
7. Verifikasi baris baru di baris teratas List berstatus `Waiting for Approval`
8. Verifikasi baris baru berkolom Allocated By nama akun CO_DIST
9. Catat Allocation ID baris teratas List (transaksi hasil TC-58, penanda pembersihan di hook `after`)

### TC-AC-ACHA-60: Hak Create saja, Resubmit transaksi Canceled milik sendiri

10. Ketik Search `Allocation ID` transaksi Canceled milik CO_DIST (Pre-setup #68), tekan Enter
11. Klik `[⋯]` pada baris hasil
12. Klik `Resubmit`
13. Verifikasi form Resubmit terbuka terisi data transaksi lama
14. Klik `[Submit]` tanpa mengubah isian
15. Verifikasi toast sukses "Success, device allocation has been resubmitted."
16. Klik `(←)` pada kotak Search
17. Verifikasi transaksi baru dengan ID unik tampil di baris teratas List
18. Catat Allocation ID baris teratas List (transaksi hasil Resubmit TC-60, penanda pembersihan di hook `after`)
19. Verifikasi transaksi baru berstatus `Waiting for Approval`

### Ganti akun ke Update saja

20. Logout dari akun CO_DIST
21. Login sebagai UO_DIST (`updateOnlyDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_UO_DIST_PASSWORD`)
22. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-61: Hak Update saja, eksekusi Edit transaksi sendiri sampai sukses

23. Ketik Search `Allocation ID` transaksi Waiting for Approval milik UO_DIST (Pre-setup #60), tekan Enter
24. Klik `[⋯]` pada baris hasil
25. Klik `Edit`
26. Ubah Quantity dari `20` menjadi `25`
27. Klik `[Save]`
28. Verifikasi toast sukses "Success, device allocation has been updated."
29. Verifikasi Quantity baris hasil menjadi `25`
30. Verifikasi status tetap `Waiting for Approval`
31. Tampilkan kolom Cost lewat Setup Column
32. Verifikasi Total Cost menjadi $200.00 (25 x $8.00)

### TC-AC-ACHA-62: Hak Update saja, eksekusi Cancel transaksi sendiri sampai sukses

33. Klik `[⋯]` pada baris hasil
34. Klik `Cancel Allocation`
35. Klik `[Cancel Allocation]` pada dialog
36. Verifikasi toast sukses "Success, device allocation has been canceled."
37. Verifikasi status baris berubah `Canceled`
38. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec Role Matrix positif (bagian 3a): aksi berhasil untuk role dengan capability parsial yang berhak. Spec ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit.
- Langkah penghubung (S-03): langkah Search untuk menemukan transaksi target, `(←)` yang mereset Search, langkah ganti akun (subjudul "Ganti akun ke Update saja"), buka halaman Allocation lewat sidebar, dan penampilan kolom Cost lewat Setup Column pada TC-61 (preferensi kolom dipulihkan hook `after` suite).
- Anchor absence tidak dipakai; spec ini tidak memuat asersi absence.
- Pembagian TC lintas spec: Role Matrix negatif untuk hak yang sama (TC-59, TC-63) ada di spec 011; kasus visibilitas per role di spec 008.
- Ukuran spec memenuhi batas sekitar 35 langkah.
- Temuan untuk QA:
  - TC-58 b menyebut "Allocated By akun ini" tanpa nama pengguna CO_DIST; Pre-setup #35 tidak mencantumkan nama pengguna. Nama tampil disediakan tim FE/BE (S-11).
  - TC-60 Post Condition (Wallet Balance dan Wallet Transaction List Reserve, Approvals Active Tab, Dashboard widget, notifikasi in-app) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-61 Post Condition dan TC-62 Post Condition (Wallet Release, Approvals, Dashboard, notifikasi) tidak diasersi karena tanpa langkah observasi; diuji di spec 026, 029, dan 046/052.
  - TC-58 Post Condition (Reserve $10.00 ditahan pada kantong PT Global Distribusi) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-60 Langkah Uji 1 tidak menyebut Allocation ID transaksi Canceled Pre-setup #68; dibaca lewat fixture seed.
  - TC-61 Expected b memuat nilai Total Cost tanpa menyebut kolom Cost ditampilkan; spec menampilkan kolom Cost lewat Setup Column.
