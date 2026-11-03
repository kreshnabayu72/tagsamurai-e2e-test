---
id: TC-AC-ACTS-E2E-198-approvals-tab-history-sort-bagian-2
title: "Approvals Tab History: Sort 3-State Per Kelas Kolom (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-618
  - TC-AC-ACTS-619
coverage:
  web: automated
---

# Approvals Tab History: Sort 3-State Per Kelas Kolom (Bagian 2)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Sort kelas teks":

| Kolom | Urutan Ascending |
|---|---|
| Device Name (SKU) | A-Z, case-insensitive |
| Category | A-Z, case-insensitive |
| Matched Identifier | A-Z, case-insensitive |
| Existing Record | A-Z, case-insensitive |
| Requested By | A-Z, case-insensitive |
| TAG Code | A-Z, case-insensitive |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`
2. Verifikasi tabel memuat sedikitnya satu baris data

### TC-AC-ACTS-618: Sort 3-state kelas teks

3. Untuk setiap baris tabel "Kolom uji Sort kelas teks" di Prerequisites, lakukan langkah 4 sampai 9
4. Klik header kolom `<kolom pada iterasi>` sekali
5. Verifikasi kolom `<kolom pada iterasi>` Ascending (↑) sesuai kolom "Urutan Ascending" pada tabel
6. Klik header kolom `<kolom pada iterasi>` kedua kali
7. Verifikasi kolom `<kolom pada iterasi>` Descending (↓) dengan urutan terbalik
8. Klik header kolom `<kolom pada iterasi>` ketiga kali
9. Verifikasi indikator sort kolom `<kolom pada iterasi>` hilang (netral) dan urutan kembali Resolved At Newest First

### TC-AC-ACTS-619: Sort 3-state kelas user

10. Klik header kolom `Approver` sekali
11. Verifikasi kolom `Approver` Ascending (↑) (A-Z menurut nama lengkap user)
12. Klik header kolom `Approver` kedua kali
13. Verifikasi kolom `Approver` Descending (↓) dengan urutan terbalik
14. Klik header kolom `Approver` ketiga kali
15. Verifikasi indikator sort kolom `Approver` hilang (netral) dan urutan kembali Resolved At Newest First

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 4 sampai 9 (iterasi dari tabel "Kolom uji Sort kelas teks" di Prerequisites, 6 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7). Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi urutan (bagian 8b butir 2).
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok satu kelas harness (Sort Tab History), satu dataset, tanpa state tulis; ekspansi hanya dari iterasi kolom, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Temuan untuk QA: kolom TAG Code dan Existing Record pada baris tertentu bernilai `—` (TC-AC-ACTS-611); TC-AC-ACTS-618 Expected "A-Z, case-insensitive" tidak menyebut posisi nilai kosong, sehingga spec tidak mengasersi posisi `—`.
