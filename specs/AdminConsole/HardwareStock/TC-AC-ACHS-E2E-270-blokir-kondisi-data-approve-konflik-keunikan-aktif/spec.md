---
id: TC-AC-ACHS-E2E-270-blokir-kondisi-data-approve-konflik-keunikan-aktif
title: "Blokir Kondisi Data: Approve Ditolak karena Konflik Keunikan Aktif"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-181
coverage:
  web: automated
---

# Blokir Kondisi Data: Approve Ditolak karena Konflik Keunikan Aktif

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Data: seed sesaat Pre-setup #21c, Subject Register Duplicate pada SKU `Fixture.hardwareStock.p16.a[2].sku` dengan Matched Identifier `Fixture.hardwareStock.p21c.matchedIdentifier` yang juga terdaftar sebagai unit Available pada SKU yang sama; dimuat hook `before` spec ini (kemampuan seed disediakan tim BE/FE). Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `skuEda` | #16 (Tabel A baris ke-2) | SKU Handheld Reader Range Type Short Range, Total Registered 12 (12 Available, 0 In Use), Device Name sama dengan `dnHh` | `Fixture.hardwareStock.p16.a[2].sku` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `snRdEdaConflict` | #21c | Matched Identifier Subject Register Duplicate seed sesaat pada `skuEda` yang juga terdaftar sebagai unit Available pada SKU yang sama | `Fixture.hardwareStock.p21c.matchedIdentifier` |

- Kemampuan teknis (disediakan tim BE/FE): sesi API aktor yang menghapus unit bentrok `Fixture.hardwareStock.p21c.matchedIdentifier` (Available, SKU sama) sampai tersimpan; tidak ada endpoint yang ditulis di spec.

## Test Steps

1. Buka Approvals > Hardware Stock
2. Pastikan Tab `Active` aktif
3. Klik row action `Review` pada Subject dengan Matched Identifier `Fixture.hardwareStock.p21c.matchedIdentifier`
4. Pilih radio `Approve`
5. Klik `[Submit]`
6. Verifikasi dialog tetap terbuka dengan error banner `Serial number Fixture.hardwareStock.p21c.matchedIdentifier already exists in the system`
7. Verifikasi Subject tetap pending: radio dan `[Submit]` tetap aktif
8. Verifikasi tidak ada toast sukses
9. Hapus unit bentrok `Fixture.hardwareStock.p21c.matchedIdentifier` (Available, SKU `Fixture.hardwareStock.p16.a[2].sku`) lewat sesi API hingga terhapus; tunggu aksi selesai
10. Klik `[Submit]` lagi
11. Verifikasi toast sukses `Success, duplicate has been approved.`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-181). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 sampai 3 (navigasi dan membuka dialog) dan langkah 9 (pelaku kedua lewat sesi API, "Tunggu aksi selesai" sesuai butir 8b nomor 8). Pelaku kedua lewat sesi API bukan konteks kedua kelas c.
- Spec ini kasus blokir karena kondisi data (prinsip 12) dan berdiri sendiri; TC-181 memiliki dependensi TC-180 di TC sumber, tetapi spec membuat kondisinya sendiri lewat seed #21c.
- Temuan untuk QA:
  - TC-181 berstatus Dependensi TC-180 padahal data yang dipakai adalah seed #21c berbeda dari data TC-180; spec tidak bergantung pada hasil spec lain.
  - Klausa "Subject tetap pending" pada TC-181 butir b tidak punya langkah observasi selain dialog yang tetap terbuka; spec mengasersi radio dan `[Submit]` yang tetap aktif.
