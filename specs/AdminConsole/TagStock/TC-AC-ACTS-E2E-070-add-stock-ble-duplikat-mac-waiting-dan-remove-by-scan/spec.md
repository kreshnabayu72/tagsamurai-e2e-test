---
id: TC-AC-ACTS-E2E-070-add-stock-ble-duplikat-mac-waiting-dan-remove-by-scan
title: "Add Stock BLE: Duplikat MAC Address (T-01), Scan Cocok Unit Existing Menjadi Waiting, dan Remove by Scan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-214
  - TC-AC-ACTS-215
  - TC-AC-ACTS-216
  - TC-AC-ACTS-217
  - TC-AC-ACTS-218
coverage:
  web: automated
---

# Add Stock BLE: Duplikat MAC Address (T-01), Scan Cocok Unit Existing Menjadi Waiting, dan Remove by Scan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #14 `BLE-BEACON-ALPHA-B1` (Device Name `BLE Beacon Alpha`, Brand `Alpha`, Model `B1`, TAG Type BLE).
- Kemampuan teknis: simulator pemindai BLE (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji BLE (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | MAC |
|---|---|
| TAG A | `Fixture.tagStock.bleA.mac` (`AA:BB:CC:11:22:33`) |
| TAG B | `Fixture.tagStock.bleB.mac` |
| TAG C | `Fixture.tagStock.bleC.mac` |
| TAG D | `Fixture.tagStock.bleD.mac` |
| TAG E | `Fixture.tagStock.bleE.mac` |

- Unit existing Available yang memegang MAC TAG E di-seed fixture BE milik spec; jalur approval normal dipakai TC-AC-ACTS-215.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
2. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-216: Remove by Scan disabled saat list kosong

3. Verifikasi tombol `[Remove by Scan]` disabled saat list kosong
4. Hover tombol `[Remove by Scan]`
5. Verifikasi tooltip `No TAGs in the list to remove.`
6. Klik `[Add by Scan]`
7. Scan TAG A
8. Klik `[Stop]`
9. Verifikasi tombol `[Remove by Scan]` enabled setelah ada satu baris

### TC-AC-ACTS-217: Remove by Scan menghapus baris yang ada di list

10. Klik `[Add by Scan]`
11. Scan TAG B
12. Klik `[Stop]`
13. Klik `[Remove by Scan]`
14. Verifikasi widget berstatus `Removing TAGs...`
15. Verifikasi live counter widget `2 TAGs scanned`
16. Scan TAG A
17. Verifikasi toast `Success, <MAC TAG A> has been removed.`
18. Verifikasi baris TAG A keluar dari list tanpa dialog
19. Verifikasi live counter widget `1 TAG scanned`
20. Klik `[Stop]`
21. Verifikasi TAG B tetap di list
22. Tutup toast

### TC-AC-ACTS-218: TAG yang tidak ada di list tidak mengubah list

23. Klik `[Remove by Scan]`
24. Scan TAG C yang tidak ada di list
25. Verifikasi toast error `Error, TAG not found in list.`
26. Verifikasi tidak ada dialog
27. Verifikasi sesi tetap aktif (widget `Removing TAGs...` masih tampil)
28. Klik `[Stop]`
29. Verifikasi daftar baris tidak berubah (satu baris TAG B)
30. Tutup toast

### TC-AC-ACTS-214: MAC Address sama dalam sesi yang sama

31. Klik `[Add by Scan]`
32. Scan TAG D
33. Scan TAG D lagi
34. Verifikasi toast `Error, failed to add TAG. It has already been scanned in this session.`
35. Verifikasi tidak ada baris tambahan (tidak ada baris berstatus `Duplicate in Batch`)
36. Verifikasi live counter widget tetap `2 TAGs scanned`
37. Klik `[Stop]`
38. Klik `[Cancel]`
39. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
40. Klik `[Leave]`
41. Ganti akun: Logout, login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
42. Buka TAG > Stock lewat sidebar
43. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
44. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-215: Scan cocok unit existing menjadi Waiting for Approval

45. Klik `[Add by Scan]`
46. Scan TAG E yang cocok dengan unit existing terdaftar sebelumnya
47. Klik `[Stop]`
48. Verifikasi baris berstatus Waiting for Approval (severity warning) di Scanned TAG List
49. Hover badge Waiting
50. Verifikasi tooltip badge `TAG <MAC TAG E> matches an existing registered TAG. It will be sent for approval.`
51. Verifikasi baris belum memiliki TAG Code
52. Klik `[Cancel]`
53. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
54. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), pembentukan list precondition (scan TAG A lalu B), `[Stop]`, penutupan toast agar toast berulang tidak tertukar (R-12), dan penutupan halaman dirty (S-08). Ganti akun ke Distributor Toggle ON ditempatkan paling akhir karena hanya TC-AC-ACTS-215 memerlukan jalur approval normal.
- Urutan TC dalam spec: 216, 217, 218, 214, 215 (list kosong lebih dulu; Remove by Scan sebelum duplikat; akun Distributor terakhir, S-10).
- Hook `after` memulihkan sesi ke Total Control.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator BLE) dan satu dataset; tiap blok berdiri sendiri.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
