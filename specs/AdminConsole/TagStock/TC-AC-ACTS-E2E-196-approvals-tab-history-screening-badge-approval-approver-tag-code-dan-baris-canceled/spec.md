---
id: TC-AC-ACTS-E2E-196-approvals-tab-history-screening-badge-approval-approver-tag-code-dan-baris-canceled
title: "Approvals Tab History: Badge Approval Tiga Severity, Approver dan TAG Code Kosong Sesuai Status, Detail Read-Only, dan Baris Canceled Tanpa Keputusan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-610
  - TC-AC-ACTS-611
  - TC-AC-ACTS-612
  - TC-AC-ACTS-613
  - TC-AC-ACTS-614
coverage:
  web: automated
---

# Approvals Tab History: Badge Approval Tiga Severity, Approver dan TAG Code Kosong Sesuai Status, Detail Read-Only, dan Baris Canceled Tanpa Keputusan

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data tambahan (disediakan fixture BE): Subject Approved (TAG Code baru), Rejected (Approver nama user), dan Canceled (tag dihapus; waktu hapus dibaca lewat API seeding).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-610: Badge Approval tiga severity

2. Verifikasi tabel memuat sedikitnya satu baris data
3. Verifikasi badge Approval `Approved` bergaya success
4. Verifikasi badge Approval `Rejected` bergaya danger
5. Verifikasi badge Approval `Canceled` bergaya danger

### TC-AC-ACTS-611: Approver dan TAG Code kosong sesuai status

6. Verifikasi baris Rejected: TAG Code `—`
7. Verifikasi baris Rejected: Approver berisi nama user
8. Verifikasi baris Canceled: Approver `—`
9. Verifikasi baris Canceled: TAG Code `—`
10. Verifikasi baris Approved: TAG Code berisi TAG Code baru

### TC-AC-ACTS-612: Detail pada Tab History membuka dialog read-only

11. Klik (⋯) > `Detail` pada baris Approved
12. Verifikasi radio Approve/Reject pre-selected
13. Verifikasi radio Approve/Reject disabled
14. Verifikasi Approval Note terisi hasil aktual
15. Verifikasi Approval Note disabled
16. Verifikasi footer hanya memuat `[Close]`
17. Klik `[Close]`

### TC-AC-ACTS-613: Baris Canceled di Tab History

18. Verifikasi baris Canceled: Approval `Canceled` bergaya danger
19. Verifikasi baris Canceled: Approver `—`
20. Verifikasi baris Canceled: TAG Code `—`
21. Verifikasi baris Canceled: Resolved At sama dengan waktu tag dihapus

### TC-AC-ACTS-614: Detail baris Canceled tanpa keputusan

22. Klik `Detail` pada baris Canceled
23. Verifikasi radio Approve/Reject tidak terpilih
24. Verifikasi radio Approve/Reject disabled
25. Verifikasi Approval Note kosong
26. Verifikasi Approval Note disabled
27. Verifikasi footer `[Close]`
28. Klik `[Close]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): `[Close]` menutup dialog Detail. Baris Rejected, Canceled, dan Approved dikenali dari badge Approval; pembanding "sedikitnya satu baris" mendahului asersi badge.
- Temuan untuk QA: TC-AC-ACTS-611 dan 613 membaca baris tanpa identifier; spec mengenali baris dari nilai badge Approval. TC-AC-ACTS-613 "Resolved At = waktu tag dihapus" tidak menyebut cara membaca waktu hapus; dibaca lewat API seeding (disediakan tim FE/BE). TC-AC-ACTS-611 butir a dan TC-AC-ACTS-613 memuat Expected yang bertumpang (Approver dan TAG Code `—` pada baris Canceled); keduanya diasersi di subjudul masing-masing.
