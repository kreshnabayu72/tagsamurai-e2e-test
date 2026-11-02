---
id: TC-AC-ACTS-E2E-049-add-stock-rfid-duplikat-dalam-sesi-dan-baris-scan-tidak-lengkap
title: "Add Stock RFID: Duplikat EPC atau UID dalam Sesi (Toast T-01) dan Baris Scan yang Hanya Membawa EPC atau UID (Toast T-22)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-142
  - TC-AC-ACTS-143
  - TC-AC-ACTS-149
  - TC-AC-ACTS-150
coverage:
  web: automated
---

# Add Stock RFID: Duplikat EPC atau UID dalam Sesi (Toast T-01) dan Baris Scan yang Hanya Membawa EPC atau UID (Toast T-22)

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
| TAG D | `Fixture.tagStock.rfidD.epc` | `Fixture.tagStock.rfidD.uid` |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
3. Klik `[Add by Scan]`

### TC-AC-ACTS-142: EPC sama dalam sesi yang sama

4. Scan TAG A
5. Scan TAG dengan EPC milik TAG A dan UID TAG B
6. Verifikasi toast `Error, failed to add TAG. It has already been scanned in this session.`
7. Verifikasi tidak ada baris tambahan (tidak ada baris berstatus `Duplicate in Batch`)
8. Verifikasi live counter widget tetap `1 TAG scanned`
9. Tutup toast

### TC-AC-ACTS-143: UID sama dalam sesi yang sama

10. Scan TAG C
11. Scan TAG dengan UID milik TAG C dan EPC TAG D
12. Verifikasi toast `Error, failed to add TAG. It has already been scanned in this session.`
13. Verifikasi tidak ada baris tambahan (tidak ada baris berstatus `Duplicate in Batch`)
14. Verifikasi live counter widget tetap `2 TAGs scanned`
15. Tutup toast

### TC-AC-ACTS-149: Baris scan hanya membawa EPC

16. Klik `[Stop]`
17. Atur simulator reader agar mengirim hanya EPC
18. Klik `[Add by Scan]`
19. Scan TAG yang hanya mengirim EPC
20. Verifikasi toast `Error, failed to add TAG. Both EPC and UID are required.`
21. Verifikasi baris tidak ditambahkan ke Scanned TAG List (tetap 2 baris)
22. Tutup toast

### TC-AC-ACTS-150: Baris scan hanya membawa UID

23. Klik `[Stop]`
24. Atur simulator reader agar mengirim hanya UID
25. Klik `[Add by Scan]`
26. Scan TAG yang hanya mengirim UID
27. Verifikasi toast `Error, failed to add TAG. Both EPC and UID are required.`
28. Verifikasi baris tidak ditambahkan ke Scanned TAG List (tetap 2 baris)
29. Klik `[Stop]`
30. Klik `[Cancel]`
31. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), penutupan toast agar toast berulang tidak tertukar (R-12), `[Stop]` dan penyetelan simulator antar TC, serta penutupan halaman dirty di akhir (S-08, S-09).
- Dua TC T-01 berbagi satu sesi scan tanpa membuka ulang halaman; pasangan identifier tiap TC berbeda (TAG A dan B untuk EPC sama, TAG C dan D untuk UID sama).
- Temuan untuk QA: TC tidak menjelaskan cara simulator reader mengirim hanya EPC atau hanya UID ("Reader mengembalikan hanya EPC"); disediakan tim FE.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
