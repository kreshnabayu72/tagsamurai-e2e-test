---
id: TC-AC-ACTS-E2E-203-approvals-tab-history-filter-bagian-1
title: "Approvals Tab History: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-632
  - TC-AC-ACTS-633
coverage:
  web: automated
---

# Approvals Tab History: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, dicatat lewat kemampuan baca fixture BE pada langkah 2 sebelum aksi (bagian 8b butir 10), bukan diturunkan dari seeding atau dibaca dari satu halaman.
- Tabel "Dropdown uji Filter":

| Field | Opsi |
|---|---|
| Type | Register Duplicate |
| SKU | RFID-ASSET-CORE-R5 |
| Category | RFID - Object TAG |
| Requested By | PT Maju Bersama (Distributor) |
| Approval | Approved |
| Approver | Andi W |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total baris Tab History sebagai baseline `N` (selain teks footer pagination), disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

2. Catat jumlah total baris Tab History sebagai `N` (kemampuan baca fixture BE)

### TC-AC-ACTS-632: Screening Filter Panel

3. Klik icon Filter
4. Verifikasi field berurutan sesuai kolom: Type [All types] | SKU [All SKUs] | Category [All categories] | Requested By [All requesters] | Approval [All decisions] | Approver [All approvers] | Requested At [Select date] | Resolved At [Select date]
5. Verifikasi dropdown bertipe multi-select searchable
6. Verifikasi field tanggal bertipe date range picker
7. Verifikasi tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
8. Verifikasi icon Filter berubah gelap saat panel terbuka

### TC-AC-ACTS-633: Filter dropdown multi-select

9. Untuk setiap baris tabel "Dropdown uji Filter" di Prerequisites, lakukan langkah 10 sampai 16
10. Pilih opsi `<opsi pada iterasi>` pada field `<field pada iterasi>`
11. Klik `[Apply]`
12. Verifikasi tabel memuat sedikitnya satu baris data
13. Verifikasi hanya baris dengan nilai `<opsi pada iterasi>` yang tampil
14. Klik `[Clear Field]`
15. Klik `[Apply]`
16. Verifikasi semua baris kembali tampil (jumlah entri pada footer sama dengan `N` yang dicatat pada langkah 2)
17. Klik icon Filter untuk menutup panel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per field: langkah 10 sampai 16 (iterasi dari tabel "Dropdown uji Filter" di Prerequisites, 6 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7). Pembanding "sedikitnya satu baris" mendahului tiap asersi "hanya baris ..." (bagian 8b butir 2).
- Langkah penghubung (S-03, S-12): langkah 2 mencatat `N` sebelum aksi pada surface bersama; tidak ada `Verifikasi` karena hanya mencatat baseline.
- Langkah penghubung (S-03): `[Clear Field]` dan `[Apply]` di tiap iterasi mengosongkan filter; menutup panel Filter di akhir.
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok satu kelas harness (Filter Panel Tab History), satu dataset, tanpa state tulis; ekspansi hanya dari 6 iterasi field.
- Temuan untuk QA: nama field `SKU` pada Filter Panel (TC-AC-ACTS-632) berbeda dengan nama kolom `Device Name (SKU)`; spec mengikuti TC.
