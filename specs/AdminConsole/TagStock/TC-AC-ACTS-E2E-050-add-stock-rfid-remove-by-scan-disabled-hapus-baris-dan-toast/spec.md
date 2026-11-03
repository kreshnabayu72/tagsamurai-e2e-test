---
id: TC-AC-ACTS-E2E-050-add-stock-rfid-remove-by-scan-disabled-hapus-baris-dan-toast
title: "Add Stock RFID: Remove by Scan Disabled saat List Kosong, Hapus Baris yang Ada, dan TAG yang Tidak di List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-151
  - TC-AC-ACTS-152
  - TC-AC-ACTS-153
coverage:
  web: automated
---

# Add Stock RFID: Remove by Scan Disabled saat List Kosong, Hapus Baris yang Ada, dan TAG yang Tidak di List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |
| TAG C | `Fixture.tagStock.rfidC.epc` | `Fixture.tagStock.rfidC.uid` |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-151: Remove by Scan disabled saat list kosong

3. Verifikasi tombol `[Remove by Scan]` disabled saat list kosong
4. Hover tombol `[Remove by Scan]`
5. Verifikasi tooltip `No TAGs in the list to remove.`
6. Klik `[Add by Scan]`
7. Scan TAG A
8. Klik `[Stop]`
9. Verifikasi tombol `[Remove by Scan]` enabled setelah ada satu baris

### TC-AC-ACTS-152: Remove by Scan menghapus baris yang ada di list

10. Klik `[Add by Scan]`
11. Scan TAG B
12. Klik `[Stop]`
13. Klik `[Remove by Scan]`
14. Verifikasi widget berstatus `Removing TAGs...`
15. Verifikasi live counter widget `2 TAGs scanned`
16. Scan TAG A
17. Verifikasi toast `Success, <EPC TAG A> has been removed.`
18. Verifikasi baris TAG A keluar dari list tanpa dialog
19. Verifikasi live counter widget `1 TAG scanned`
20. Klik `[Stop]`
21. Verifikasi TAG B tetap di list
22. Tutup toast

### TC-AC-ACTS-153: TAG yang tidak ada di list tidak mengubah list

23. Klik `[Remove by Scan]`
24. Scan TAG C yang tidak ada di list
25. Verifikasi toast error `Error, TAG not found in list.`
26. Verifikasi tidak ada dialog
27. Verifikasi sesi tetap aktif (widget `Removing TAGs...` masih tampil)
28. Klik `[Stop]`
29. Verifikasi daftar baris tidak berubah (satu baris TAG B)
30. Klik `[Cancel]`
31. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), scan TAG A sampai terbentuk dua baris untuk precondition TC-AC-ACTS-152 (list dua TAG) dan penutupan halaman dirty di akhir (S-08, S-09).
- TC-AC-ACTS-875 dan TC-AC-ACTS-876 (Remove by Scan beruntun dan kode tidak dikenal) ada di spec 079.
- Temuan untuk QA: TC-AC-ACTS-152 precondition "list berisi dua TAG hasil scan (TAG A dan TAG B)" tidak menyebut urutan pembentukan; spec membentuknya lewat scan dalam spec yang sama.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
