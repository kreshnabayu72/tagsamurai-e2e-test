---
id: TC-AC-ACHS-E2E-271-multi-konteks-race-keputusan-approval
title: "Multi-Konteks: Race Keputusan Approval"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-190
  - TC-AC-ACHS-191
  - TC-AC-ACHS-192
  - TC-AC-ACHS-193
  - TC-AC-ACHS-194
coverage:
  web: automated
---

# Multi-Konteks: Race Keputusan Approval

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor (Approver A): Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Pelaku kedua (Approver B, Total Control lain): `Fixture.hardwareStock.account.p02.defaultUser.fullName` `Fixture.hardwareStock.account.p02.defaultUser.email` (Pre-setup #2, tier Total Control, kata sandi `Spectra.env.AC_DEFAULT_USER_PASSWORD`, nama ditetapkan tim FE). Pelaku Client untuk Cancel Request (TC-194): akun Client disediakan tim FE. Keduanya lewat sesi API aktor (kemampuan disediakan tim BE/FE) hingga keputusan atau pembatalan tersimpan; tidak ada konteks UI kedua.
- Data milik spec (S-06, S-12; suffix `{runId}-271`): lima Subject pending tabel di bawah. Subject TC-190 sampai TC-193 di-seed hook `before` dan Subject TC-194 di-seed pada langkah 30 (langkah penghubung), semuanya lewat fixture BE (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Hook `after` menghapus semuanya (idempotent). Subject Pre-setup #21 tidak diputuskan oleh spec ini. Efek pada Pre-setup: isi Approvals Tab Active dan Tab History berubah selama spec berjalan; data milik spec dihapus hook `after`.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture atau nilai |
|---|---|---|---|
| `snRace190` | milik spec | Matched Identifier Subject Activation Collision pending untuk TC-190 | `SN-RACE190-{runId}-271` |
| `snRace191` | milik spec | Matched Identifier Subject Activation Collision pending (Fixed Reader tanpa SKU) untuk TC-191 | `SN-RACE191-{runId}-271` |
| `snRace192` | milik spec | Matched Identifier Subject Register Duplicate pending untuk TC-192 | `SN-RACE192-{runId}-271` |
| `snRace193` | milik spec | Matched Identifier Subject Register Duplicate pending untuk TC-193 | `SN-RACE193-{runId}-271` |
| `snRace194` | milik spec | Matched Identifier Subject Activation Collision pending untuk TC-194 | `SN-RACE194-{runId}-271` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `akun defaultUserPrincipal` | #2 | Akun Principal Default User | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName`, `Fixture.hardwareStock.account.p02.defaultUser.shortName` |

Tabel keputusan Approver A tanpa Approval Note (langkah 3 sampai 15):

| TC | Matched Identifier | Jenis Subject | Keputusan Approver A |
|---|---|---|---|
| TC-190 | `{snRace190}` | Activation Collision | `Approve` |
| TC-192 | `{snRace192}` | Register Duplicate | `Approve` |

Tabel keputusan Approver A dengan Approval Note (langkah 16 sampai 29):

| TC | Matched Identifier | Jenis Subject | Keputusan Approver A | Approval Note A |
|---|---|---|---|---|
| TC-191 | `{snRace191}` | Activation Collision | `Reject` | `Alasan uji` |
| TC-193 | `{snRace193}` | Register Duplicate | `Reject` | `Alasan uji` |

## Test Steps

### TC-AC-ACHS-190 dan TC-AC-ACHS-192: Subject sudah diputuskan Approver B, keputusan Approve

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`

Untuk setiap baris tabel keputusan tanpa Approval Note (TC-190, TC-192), lakukan langkah 3 sampai 15:

3. Ketik Search Matched Identifier pada baris tabel, tekan Enter
4. Klik row action `Review` pada Subject dengan Matched Identifier pada baris tabel
5. Approver B memutuskan Subject yang sama lebih dulu lewat sesi API hingga keputusan tersimpan; tunggu aksi selesai
6. Approver A memilih radio `Approve`
7. Klik `[Submit]`
8. Verifikasi dialog kedua (nested) tampil di atas Detail Approval dengan ikon 🔒, title `Approval cannot be made`, body `This request has already been resolved.`, dan tombol `[Close]`
9. Klik `[Close]` pada dialog kedua
10. Verifikasi dialog kedua dan dialog Detail Approval tertutup sekaligus
11. Verifikasi Tab Active di-refresh: Subject itu tidak lagi tampil di Tab Active
12. Klik `(←)` pada kotak Search, lalu klik Tab `History`
13. Ketik Search Matched Identifier pada baris tabel, tekan Enter
14. Verifikasi Subject itu tampil di Tab History dengan Approver `Fixture.hardwareStock.account.p02.defaultUser.shortName` (keputusan Approver A tidak tercatat)
15. Klik `(←)` pada kotak Search, lalu klik Tab `Active`

### TC-AC-ACHS-191 dan TC-AC-ACHS-193: Subject sudah diputuskan Approver B, keputusan Reject

Untuk setiap baris tabel keputusan dengan Approval Note (TC-191, TC-193), lakukan langkah 16 sampai 29:

16. Ketik Search Matched Identifier pada baris tabel, tekan Enter
17. Klik row action `Review` pada Subject dengan Matched Identifier pada baris tabel
18. Approver B memutuskan Subject yang sama lebih dulu lewat sesi API hingga keputusan tersimpan; tunggu aksi selesai
19. Approver A memilih radio `Reject`
20. Approver A mengisi Approval Note `Alasan uji`
21. Klik `[Submit]`
22. Verifikasi dialog kedua (nested) tampil di atas Detail Approval dengan ikon 🔒, title `Approval cannot be made`, body `This request has already been resolved.`, dan tombol `[Close]`
23. Klik `[Close]` pada dialog kedua
24. Verifikasi dialog kedua dan dialog Detail Approval tertutup sekaligus
25. Verifikasi Tab Active di-refresh: Subject itu tidak lagi tampil di Tab Active
26. Klik `(←)` pada kotak Search, lalu klik Tab `History`
27. Ketik Search Matched Identifier pada baris tabel, tekan Enter
28. Verifikasi Subject itu tampil di Tab History dengan Approver `Fixture.hardwareStock.account.p02.defaultUser.shortName` (keputusan Approver A tidak tercatat)
29. Klik `(←)` pada kotak Search, lalu klik Tab `Active`

### TC-AC-ACHS-194: Client membatalkan Activation Collision sebelum Submit

30. Buat Subject Activation Collision pending `{snRace194}` lewat sesi API aktor hingga tersimpan; tunggu aksi selesai
31. Muat ulang halaman (F5)
32. Verifikasi sedikitnya satu baris Subject tampil di Tab Active (pembanding)
33. Ketik Search `{snRace194}`, tekan Enter
34. Klik row action `Review` pada Subject dengan Matched Identifier `{snRace194}`
35. Client menjalankan Cancel Request untuk Subject yang sama lewat sesi API hingga pembatalan tersimpan; tunggu aksi selesai
36. Approver A memilih radio `Approve`
37. Klik `[Submit]`
38. Verifikasi dialog kedua D-05 tampil dengan title `Approval cannot be made` dan body `This request has already been resolved.`
39. Klik `[Close]` pada dialog kedua
40. Verifikasi dialog kedua dan dialog Detail Approval tertutup sekaligus
41. Verifikasi Tab Active di-refresh
42. Klik Tab `History`
43. Ketik Search `{snRace194}`, tekan Enter
44. Verifikasi Subject tampil dengan Approval `Canceled` dan Approver `—`
45. Verifikasi keputusan approver tidak tercatat: Approval bukan `Approved`
46. Klik `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-190, 191, 192, 193, 194). Tidak ada TC hanya-BE di spec ini.
- Search memakai Matched Identifier penuh milik spec (bersuffix unik, hanya satu baris yang memuatnya); tidak ada perbedaan dengan sel tabel.
- Urutan menyimpang dari TC: TC-190 dan TC-192 (keputusan `Approve`) dikerjakan dalam satu loop, lalu TC-191 dan TC-193 (keputusan `Reject` dengan Approval Note) dalam loop kedua, supaya langkah loop tidak bersyarat (butir 8b nomor 7). Langkah 3 sampai 15 diulang dua kali (tabel tanpa Approval Note) dan langkah 16 sampai 29 diulang dua kali (tabel dengan Approval Note); ekspansi 2 + 13 x 2 + 14 x 2 + 17 = 73 langkah, lebih dari sekitar 35 langkah. Alasan: lima TC satu kelas multi-konteks (race keputusan) dengan alur identik dan Subject milik spec berbeda per TC; tiap iterasi berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 31, 42 (navigasi; langkah 2 `Klik Tab Active` menggantikan "Pastikan Tab `Active` aktif" TC), 30 (seed Subject milik spec TC-194 lewat sesi API), 5, 18, dan 35 (pelaku kedua lewat sesi API, "Tunggu aksi selesai", R-20), 3, 4, 13, 16, 17, 27, 33, dan 43 (Search untuk menemukan baris target, R-16), 12, 15, 26, 29, dan 46 (mengosongkan Search lewat `(←)` dan pindah tab).
- Langkah 8 dan 22 ditulis satu `Verifikasi` karena Expected TC-190 butir a menyebut ikon, title, body, dan tombol sebagai satu dialog (S-01). Langkah 32 adalah anchor positif sebelum pembacaan tab.
- Pelaku kedua lewat sesi API bukan konteks kedua kelas c dan tidak memakai `P-2`; kelas c berlaku karena objek uji adalah race dua pengambil keputusan.
- Temuan untuk QA:
  - TC-190 dan TC-194 menyebut Subject yang sama padahal setelah TC-190 Subject itu sudah diputuskan Approver B; spec memakai Subject milik spec berbeda per TC (TC-194 di-seed pada langkah 30).
  - Expected "keputusan Approver A tidak tercatat" (TC-190 sampai 193) tidak punya langkah observasi di TC; spec mengasersi Approver `Fixture.hardwareStock.account.p02.defaultUser.shortName` pada Tab History (Pre-setup #2 sebagai Approver B).
  - Akun Client untuk Cancel Request (TC-194) tidak ada di Pre-setup TC; ditulis "disediakan tim FE".
  - Seed Subject milik spec dan pembersihannya di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
