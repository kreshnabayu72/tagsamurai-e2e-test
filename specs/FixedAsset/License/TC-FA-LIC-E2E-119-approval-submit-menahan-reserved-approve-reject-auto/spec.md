---
id: TC-FA-LIC-E2E-119-approval-submit-menahan-reserved-approve-reject-auto
title: "Approval Registrasi Aset: Submit Menahan Reserved, Approve, Reject, dan Auto-cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-394
  - TC-FA-LIC-395
  - TC-FA-LIC-396
  - TC-FA-LIC-397
coverage:
  web: automated
---

# Approval Registrasi Aset: Submit Menahan Reserved, Approve, Reject, dan Auto-cancel

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono); bertindak sebagai Approver pada TC-FA-LIC-395 dan TC-FA-LIC-396 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, kuota, plan, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (License Summary Reserved 15, Used 4320, Remaining 665; Divisi IT beralokasi dengan Reserved by This Group 0 dan Remaining Quota 40; Gudang A) dan #20 (draf aset siap Submit di Divisi IT; aset Waiting for Approval di Divisi IT dan Gudang A; client Professional). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-394 approval ON; blok TC-FA-LIC-395 aset Waiting for Approval di Gudang A (Reserved by This Group 1) saat Remaining Gudang A 0 oleh registrasi lain; blok TC-FA-LIC-396 aset Waiting for Approval di Divisi IT; blok TC-FA-LIC-397 aset Waiting for Approval dan plan diturunkan dari Professional ke Growth (kehilangan FA-1) saat downgrade berlaku.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #20 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dan #20 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, dan Remaining, status aset, plan, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: jam fixture digeser maju pada blok TC-FA-LIC-397; sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`) dan jam serta plan dipulihkan di hook `after` serta pada langkah 32.

## Test Steps

### TC-FA-LIC-394: Submit dengan approval ON menahan slot Reserved

1. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan approval ON dan draf aset di Divisi IT hingga tersimpan
2. Buka Fixed Asset > Asset Registration
3. Klik `Submit for Approval` pada draf aset di Divisi IT
4. Verifikasi aset berstatus `Waiting for Approval`
5. Buka License > All License
6. Verifikasi License Summary kolom Asset: Reserved `16`, Used `4320` (tidak berubah), dan Remaining `664`
7. Buka License > Allocation Quota > node `Divisi IT`
8. Verifikasi Divisi IT: Reserved by This Group `1` dan Remaining Quota `39`

### TC-FA-LIC-395: Approve mengubah Reserved menjadi Used tanpa memanggil check_group_quota

9. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan aset Waiting for Approval di Gudang A (Reserved by This Group 1) saat Remaining Gudang A `0` oleh registrasi lain hingga tersimpan
10. Buka License > All License; catat Reserved, Used, dan Remaining pada License Summary kolom Asset
11. Approve registrasi aset di Fixed Asset > Approvals
12. Verifikasi Approve berhasil walau Remaining Gudang A `0`
13. Verifikasi aset berstatus `Active`
14. Buka License > All License
15. Verifikasi Reserved turun 1 dan Used naik 1 dibanding nilai pada langkah 10
16. Verifikasi Remaining License Summary tidak berubah dibanding nilai pada langkah 10

### TC-FA-LIC-396: Reject melepas Reserved dan aset kembali Draft

17. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan aset Waiting for Approval di Divisi IT hingga tersimpan
18. Buka License > All License; catat Reserved, Used, dan Remaining pada License Summary kolom Asset
19. Reject registrasi aset dengan alasan penolakan di Fixed Asset > Approvals
20. Verifikasi aset kembali berstatus `Draft`
21. Buka License > All License
22. Verifikasi Reserved turun 1 dan Remaining naik 1 dibanding nilai pada langkah 18
23. Verifikasi Used tidak berubah dibanding nilai pada langkah 18

### TC-FA-LIC-397: Auto-cancel sistem saat plan kehilangan Approval Workflow melepas Reserved

24. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan aset Waiting for Approval dan plan diturunkan dari Professional ke Growth saat downgrade berlaku hingga tersimpan
25. Buka License > All License; catat Reserved dan Remaining pada License Summary kolom Asset
26. Geser jam fixture ke saat downgrade berlaku
27. Buka daftar aset
28. Verifikasi aset yang Waiting for Approval otomatis kembali berstatus `Draft`
29. Buka License > All License
30. Verifikasi Reserved turun sesuai jumlah aset yang di-cancel dibanding nilai pada langkah 25
31. Verifikasi Remaining naik sama banyak dibanding nilai pada langkah 25
32. Pulihkan jam fixture dan plan ke Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 9, 17, 24, dan 32 (fixture BE pemulih dan penyetel state), langkah 26 (menggeser jam fixture), langkah 27 (membuka daftar aset), serta navigasi License. Langkah 10, 18, dan 25 mencatat nilai License Summary sebagai baseline langkah 15, 16, 22, 23, 30, dan 31 (S-12).
- Pemulihan jam dan plan dilakukan pada langkah 32 sebelum akun aktor membuka halaman lain (S-09).
- TC-FA-LIC-395 langkah 2 membuka node Gudang A tanpa Expected tentang node itu; node tidak diasersi.
- TC-FA-LIC-396 langkah 2 membuka node Divisi IT tanpa Expected tentang node itu; node tidak diasersi.
- TC-FA-LIC-397 menyebut Expected "Reserved turun sesuai jumlah aset yang di-cancel" tanpa jumlah; spec mengasersi dibanding baseline langkah 25.
- Pembagian TC lintas spec: TC-FA-LIC-398, TC-FA-LIC-399, dan TC-FA-LIC-400 ada di spec 146.
- Temuan untuk QA:
  - TC-FA-LIC-397 tidak menyebut tempat mengamati status `Draft` aset; spec memakai daftar aset.
  - TC-FA-LIC-395 dan TC-FA-LIC-396 menyebut Role Approver sebagai Total Control Pre-setup #1; spec memakai akun itu tanpa ganti akun.
