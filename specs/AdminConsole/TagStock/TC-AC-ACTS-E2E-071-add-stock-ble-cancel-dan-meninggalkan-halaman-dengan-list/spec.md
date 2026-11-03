---
id: TC-AC-ACTS-E2E-071-add-stock-ble-cancel-dan-meninggalkan-halaman-dengan-list
title: "Add Stock BLE: Cancel dan Meninggalkan Halaman dengan List Berisi atau Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-220
  - TC-AC-ACTS-221
  - TC-AC-ACTS-222
  - TC-AC-ACTS-223
  - TC-AC-ACTS-897
  - TC-AC-ACTS-898
coverage:
  web: automated
---

# Add Stock BLE: Cancel dan Meninggalkan Halaman dengan List Berisi atau Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #14 `BLE-BEACON-ALPHA-B1` (Device Name `BLE Beacon Alpha`, Brand `Alpha`, Model `B1`, TAG Type BLE).
- Kemampuan teknis: simulator pemindai BLE (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji BLE (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | MAC |
|---|---|
| TAG A | `Fixture.tagStock.bleA.mac` (`AA:BB:CC:11:22:33`) |
| TAG B | `Fixture.tagStock.bleB.mac` |
| TAG C | `Fixture.tagStock.bleC.mac` |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat Total Registered SKU `BLE-BEACON-ALPHA-B1` sebagai baseline lewat kemampuan baca BE
2. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
3. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-898: Cancel dengan list kosong

4. Klik `[Cancel]`
5. Verifikasi tidak ada dialog
6. Verifikasi halaman Detail SKU `BLE-BEACON-ALPHA-B1` Tab Available tampil
7. Klik Breadcrumb `Stock`
8. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
9. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-223: Breadcrumb Stock dengan list kosong

10. Klik Breadcrumb `Stock`
11. Verifikasi tidak ada dialog
12. Verifikasi halaman Stock List tampil
13. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
14. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`
15. Klik `[Add by Scan]`, scan TAG A, scan TAG B, scan TAG C, lalu klik `[Stop]`

### TC-AC-ACTS-897: Cancel dengan list berisi, pilih Cancel

16. Klik `[Cancel]`
17. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
18. Klik `[Cancel]` pada dialog
19. Verifikasi dialog tertutup
20. Verifikasi tetap di halaman Add Stock
21. Verifikasi list masih berisi 3 baris

### TC-AC-ACTS-220: Cancel dengan list berisi, pilih Leave

22. Klik `[Cancel]`
23. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
24. Klik `[Leave]`
25. Verifikasi halaman Detail SKU `BLE-BEACON-ALPHA-B1` Tab Available tampil
26. Verifikasi Total Registered SKU sama dengan baseline (list dibuang tanpa Submit)
27. Klik Breadcrumb `Stock`
28. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
29. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`
30. Klik `[Add by Scan]`, scan TAG A, scan TAG B, lalu klik `[Stop]`

### TC-AC-ACTS-222: Breadcrumb Stock dengan list berisi, pilih Cancel

31. Klik Breadcrumb `Stock`
32. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
33. Klik `[Cancel]` pada dialog
34. Verifikasi tetap di halaman Add Stock
35. Verifikasi list utuh (2 baris)

### TC-AC-ACTS-221: Breadcrumb Stock dengan list berisi, pilih Leave

36. Klik Breadcrumb `Stock`
37. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
38. Klik `[Leave]`
39. Verifikasi halaman Stock List tampil
40. Verifikasi Total Registered SKU sama dengan baseline (list dibuang tanpa Submit)

## Notes

- Langkah penghubung (S-03): langkah 2 dan 3 serta pembukaan ulang halaman Add Stock lewat Breadcrumb `Stock`, Search, dan row action `Add Stock` (precondition TC), pembentukan list precondition (scan lalu `[Stop]`), dan pencatatan baseline Total Registered.
- Urutan TC dalam spec: 898, 223, 897, 220, 222, 221 (list kosong lebih dulu; TC yang menjaga halaman 897 dan 222 sebelum TC yang keluar 220 dan 221, S-10).
- Search `BLE-BEACON-ALPHA-B1` dipakai sebagai langkah penghubung untuk menemukan baris target (R-16).
- Total Registered dibaca lewat kemampuan baca BE karena TC menyatakan "list dibuang tanpa Submit" tanpa langkah observasi.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator BLE) dan satu dataset (halaman Add Stock dengan dialog Unsaved Changes); tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
