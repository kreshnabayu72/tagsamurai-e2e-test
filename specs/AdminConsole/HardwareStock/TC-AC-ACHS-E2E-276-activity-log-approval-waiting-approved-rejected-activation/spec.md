---
id: TC-AC-ACHS-E2E-276-activity-log-approval-waiting-approved-rejected-activation
title: "Activity Log: Waiting for Approval, Approved, Rejected, dan Aktivasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-535
  - TC-AC-ACHS-536
  - TC-AC-ACHS-537
  - TC-AC-ACHS-538
  - TC-AC-ACHS-539
  - TC-AC-ACHS-540
  - TC-AC-ACHS-541
coverage:
  web: automated
---

# Activity Log: Waiting for Approval, Approved, Rejected, dan Aktivasi

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Activity Log disetel hook `before` dan dipulihkan hook `after` spec ini; seeding Population Stock Pre-setup #16 sampai #22 dan #27; suite serial `parallel: false` (lihat suite.md).
- Aksi sumber (dipakai sebagai precondition TC, dijalankan hook `before` lewat sesi API aktor, kemampuan disediakan tim BE/FE, tidak diasersi): Submit Sync match oleh Additional Approver dengan capability Create `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName` `Fixture.hardwareStock.account.p06.additionalApproverCreate.email` (Pre-setup #6, `Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`, nama ditetapkan tim FE; sumber TC-143) dan aktivasi Client yang bentrok (sumber TC-560); Approve Register Duplicate Subject milik spec `SN-ZEBRA-RFD40-{runId}-276A` (TC-180) dan Reject Register Duplicate Subject milik spec `SN-ZEBRA-TC52-{runId}-276B` (TC-182); Approve Activation Collision Subject milik spec `SN-ZEBRA-TC52-{runId}-276C` (TC-183) dan Reject Activation Collision Subject milik spec `SN-ZEBRA-RFD40-{runId}-276D` (TC-184); bypass E2a oleh Total Control `SN-ZEBRA-FX9600-{runId}-276E` (TC-140); Cancel Request Client pada Subject milik spec `SN-ZEBRA-RFD40-{runId}-276F` (TC-561) dan pelepasan unit In Use milik spec `SN-ZEBRA-RFD40-{runId}-276G` oleh Client (TC-557). Akun Client pelaku disediakan tim FE (tidak ada di Pre-setup TC).
- Data milik spec (S-06, S-12): target aksi tulis di atas (`SN-ZEBRA-RFD40-{runId}-276A` sampai `SN-ZEBRA-RFD40-{runId}-276G`, unit dan Subject terkait) di-seed hook `before` dengan struktur yang sama dengan baris Pre-setup #17, #18, dan #21 yang digantikannya; data Pre-setup #16 sampai #22 dan #27 tidak diubah spec ini. Mekanisme seeding disediakan tim BE/FE tanpa endpoint karangan dan kunci fixture-nya belum ada (Temuan untuk QA).
- Cleanup (R-08): hook `after` menghapus data milik spec di atas secara idempotent (unit, Subject, dan entri pending bersuffix `{runId}-276`). Entri Activity Log adalah audit trail permanen dan tidak dihapus.
- Unit bypass E2a (TC-140) memakai Serial Number bersuffix `SN-ZEBRA-FX9600-{runId}-276E` yang menggantikan Serial Number literal dari Tabel Data Uji Dinamis (S-12).
- Baseline (S-12): jumlah entri Activity Log Object `Hardware` per Name dan Action dicatat hook `before` sebelum aksi sumber yang menghasilkan entri itu; asersi "tidak ada entri" dan "tepat satu entri" (langkah 7, 30, 33) memakai selisih terhadap baseline (+1 per Name dan Action; audit trail permanen).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `dnSfr` | #16 (Tabel A) | Device Name SKU Smart Fixed Reader (sama untuk `skuSfr`, `skuIx4`) | `Fixture.hardwareStock.p16.a[3].deviceName` |
| `dnHh (4)` | #16 (Tabel A) | Device Name SKU Handheld Reader (sama untuk `skuLong`, `skuShort`, `skuEda`) | `Fixture.hardwareStock.p16.a[4].deviceName` |
| `snWfa` | data milik spec (struktur #17 Tabel E baris N = 28 dan #21 Tabel C baris ke-10) | Serial Number unit Waiting for Approval milik spec; sekaligus Matched Identifier Subject Register Duplicate pending (Existing Record Available, Registrant dan requester Distributor #12) | `SN-ZEBRA-RFD40-{runId}-276A` |
| `snRdTc52Wfa` | data milik spec (struktur #21 Tabel C baris ke-7) | Matched Identifier Subject Register Duplicate pending pada `skuShort` milik spec (Existing Record Waiting for Approval) | `SN-ZEBRA-TC52-{runId}-276B` |
| `idAcFixed` | data milik spec (struktur #21 Tabel C baris ke-9) | Matched Identifier Subject Activation Collision pending milik spec (Existing Record Active, requester Client) | `SN-ZEBRA-RFD40-{runId}-276D` |
| `snAcTc52` | data milik spec (struktur #21 Tabel C baris ke-11) | Matched Identifier Subject Activation Collision pending pada `skuShort` milik spec (Existing Record Active Client ke-1 Pre-setup #23, requester Client ke-2) | `SN-ZEBRA-TC52-{runId}-276C` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` (Modified By, format `[First Name] [Last Initial]`) |
| `akun additionalApproverCreatePrincipal` | #6 | Akun Additional Approver dengan capability Create | `Fixture.hardwareStock.account.p06.additionalApproverCreate.email`, `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName`, `Fixture.hardwareStock.account.p06.additionalApproverCreate.shortName` (Modified By, format `[First Name] [Last Initial]`) |


## Test Steps

1. Buka Admin Console > Activity Log
2. Terapkan Filter Object = `Hardware`

### TC-AC-ACHS-535: Waiting for Approval

3. Cari entri terbaru dengan Name `Fixture.hardwareStock.p16.a[4].deviceName` untuk Waiting for Approval hasil Sync oleh `Fixture.hardwareStock.account.p06.additionalApproverCreate.shortName`
4. Verifikasi entri Register Duplicate: Name `Fixture.hardwareStock.p16.a[4].deviceName`, Action `Waiting for Approval`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`
5. Verifikasi Modified By staf pemicu Sync `Fixture.hardwareStock.account.p06.additionalApproverCreate.shortName`, bukan user Client
6. Cari entri terbaru `Waiting for Approval` dengan Name `Fixture.hardwareStock.p16.a[4].deviceName` hasil aktivasi Client
7. Verifikasi entri Activation Collision memiliki field yang sama (Name, Action `Waiting for Approval`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`) dan jumlah entri bertambah 1 dari baseline Name dan Action tersebut (baseline dicatat hook sebelum aksi aktivasi Client)
8. Verifikasi Modified By entri Activation Collision adalah user Client pelaku

### TC-AC-ACHS-536: Duplicate Approved

9. Cari entri terbaru dengan Name `SN-ZEBRA-RFD40-{runId}-276A`
10. Verifikasi entri: Action `Duplicate Approved`, Object `Hardware`, Field `Status`, Old Value `Waiting for Approval`, New Value `Available`
11. Verifikasi Modified By approver `Fixture.hardwareStock.account.p01.totalControl.shortName`

### TC-AC-ACHS-537: Duplicate Rejected

12. Cari entri terbaru dengan Name `SN-ZEBRA-TC52-{runId}-276B`
13. Verifikasi entri: Action `Duplicate Rejected`, Object `Hardware`, Field `Status`, Old Value `Waiting for Approval`, New Value `Rejected`
14. Verifikasi Modified By approver `Fixture.hardwareStock.account.p01.totalControl.shortName`
15. Verifikasi alasan penolakan tidak ditampilkan sebagai baris `Rejection Reason` terpisah pada entri Activity Log (alasan hanya terlihat sebagai Approval Note di Tab History)

### TC-AC-ACHS-538: Device Activation Approved

16. Cari entri terbaru dengan Name `Fixture.hardwareStock.p16.a[4].deviceName` untuk Action `Device Activation Approved`
17. Verifikasi entri: Action `Device Activation Approved`, Object `Hardware`, Field `Status`, Old Value `Waiting for Approval`, New Value `Active`
18. Verifikasi Name adalah Device Name
19. Verifikasi Modified By approver `Fixture.hardwareStock.account.p01.totalControl.shortName`

### TC-AC-ACHS-539: Device Activation Rejected

20. Cari entri terbaru dengan Name `Fixture.hardwareStock.p16.a[3].deviceName` untuk Action `Device Activation Rejected`
21. Verifikasi entri: Action `Device Activation Rejected`, Object `Hardware`, Field `Status`, Old Value `Waiting for Approval`, New Value `Rejected`
22. Verifikasi Name adalah Device Name
23. Verifikasi Modified By approver `Fixture.hardwareStock.account.p01.totalControl.shortName`

### TC-AC-ACHS-540: Duplicate Approved bypass E2a

24. Cari entri terbaru dengan Name `SN-ZEBRA-FX9600-{runId}-276E`
25. Verifikasi entri `Duplicate Approved` tampil: Field `Status`, Old Value `—`, New Value `Available`
26. Verifikasi Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName` (bukan `System`)
27. Verifikasi entri memuat teks `Approved by Fixture.hardwareStock.account.p01.totalControl.fullName (Total Control — requester)`
28. Verifikasi tidak ada entri `Waiting for Approval` sintetis untuk Name `SN-ZEBRA-FX9600-{runId}-276E` (jumlah entri `Waiting for Approval` sama dengan baseline)

### TC-AC-ACHS-541: Device Activation Canceled dan Device Released

29. Periksa entri terbaru Action `Device Activation Canceled` dengan Name `Fixture.hardwareStock.p16.a[4].deviceName` untuk Subject `SN-ZEBRA-RFD40-{runId}-276F`
30. Verifikasi entri `Device Activation Canceled`: Name Device Name, Field `Status`, Old Value `Waiting for Approval`, New Value `Canceled`, dan jumlah entri bertambah 1 dari baseline Name dan Action tersebut
31. Verifikasi Modified By entri `Device Activation Canceled` adalah user Client pelaku
32. Periksa entri Action `Device Released` dengan Name `SN-ZEBRA-RFD40-{runId}-276G`
33. Verifikasi entri `Device Released`: Name Serial Number, Field `Status`, Old Value `In Use`, New Value `Available`, dan jumlah entri Name tersebut bertambah 1 dari baseline
34. Verifikasi Modified By entri `Device Released` adalah user Client pelaku

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-535 sampai TC-541). Tidak ada TC hanya-BE di spec ini.
- `P-1`: langkah 28 (asersi tidak ada entri `Waiting for Approval` sintetis, TC-540 butir b) bergantung pada state berat bypass E2a yang dibangun di hook spec ini; dipenuhi dengan `Verifikasi` berbaseline di spec asal dengan anchor positif entri `Duplicate Approved` pada langkah 25 (S-05, butir 8b nomor 2). Langkah 15 (TC-537 butir c) adalah asersi tidak adanya baris `Rejection Reason`, diasersi pada entri yang sama dengan anchor langkah 13.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 dan 2 (navigasi dan Filter), 3, 6, 9, 12, 16, 20, 24, 29, 32 (mencari entri target, R-16).
- Temuan untuk QA:
  - TC-535 sampai TC-541 memakai Dependensi ke TC aksi (TC-143, 560, 180, 182, 183, 184, 140, 561, 557); aksi sumber dijalankan lewat sesi API aktor karena spec tidak boleh bergantung pada spec lain; mekanismenya (Sync tanpa perangkat USB, aksi Client) tidak didefinisikan di TC, PRD, atau LLD.
  - TC-535 dan TC-541 menyebut "user Client pelaku" tanpa nama akun; akun Client disediakan tim FE.
  - TC-535 butir b menyebut entri Activation Collision dengan Name `Fixture.hardwareStock.p16.a[4].deviceName` tanpa menyebut SKU pembeda dari entri lain; pencarian "entri terbaru" bergantung pada urutan sehingga baris yang dicari harus dijamin berada di halaman teramati (S-14).
  - Post Condition tidak ada pada TC-535 sampai TC-541.
  - Seeding unit dan Subject milik spec (`SN-ZEBRA-RFD40-{runId}-276A` sampai `-276G`) beserta cleanup `after` tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim BE/FE dan kunci fixture-nya belum ada.
