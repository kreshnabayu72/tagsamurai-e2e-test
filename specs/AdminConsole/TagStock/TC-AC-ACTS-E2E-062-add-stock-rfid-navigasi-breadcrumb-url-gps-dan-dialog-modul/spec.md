---
id: TC-AC-ACTS-E2E-062-add-stock-rfid-navigasi-breadcrumb-url-gps-dan-dialog-modul
title: "Add Stock: Breadcrumb Stock dan Detail, URL Add Stock Scan untuk SKU GPS Ditolak, serta Dialog Konfirmasi Modul (Backdrop dan Esc)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-721
  - TC-AC-ACTS-722
  - TC-AC-ACTS-803
coverage:
  web: automated
---

# Add Stock: Breadcrumb Stock dan Detail, URL Add Stock Scan untuk SKU GPS Ditolak, serta Dialog Konfirmasi Modul (Backdrop dan Esc)

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

- SKU `RFID-ASSET-CORE-R5` memiliki sedikitnya 2 unit Available tanpa guard Delete dan 2 unit eligible Audit; Approvals > Tab Active memuat satu Subject pending milik spec (di-seed fixture BE); Tab Available `RFID-ASSET-CORE-R5` dipakai TC-AC-ACTS-803 untuk dialog `Delete Unit` dan `Confirm Audit`.
- URL halaman Add Stock scan (RFID, NFC, BLE) untuk SKU `GPS-TRACK-CORE-G3` (TC-AC-ACTS-721) disediakan tim FE.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps


### TC-AC-ACTS-721: URL Add Stock scan untuk SKU GPS

1. Ketik Search `GPS-TRACK-CORE-G3`, tekan Enter
2. Klik Device Name baris SKU `GPS-TRACK-CORE-G3`, buka Tab Available
3. Catat jumlah entri Tab Available sebagai baseline
4. Klik `[Event Log]`
5. Catat jumlah sesi Event Log sebagai baseline
6. Tutup modal Event Log
7. Buka URL halaman Add Stock scan (RFID, NFC, BLE) untuk SKU `GPS-TRACK-CORE-G3` langsung
8. Verifikasi toast netral `This SKU is no longer available.`
9. Verifikasi Stock List tampil
10. Ganti isi kotak search dengan `GPS-TRACK-CORE-G3`, tekan Enter
11. Klik Device Name baris SKU `GPS-TRACK-CORE-G3`, buka Tab Available
12. Verifikasi jumlah entri Tab Available sama dengan baseline langkah 3 (tidak ada unit tersimpan)
13. Klik `[Event Log]`
14. Verifikasi jumlah sesi Event Log sama dengan baseline langkah 5 (tidak ada log tersimpan)
15. Tutup modal Event Log
16. Klik Breadcrumb `Stock`
17. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
18. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-722: Breadcrumb Add Stock RFID

19. Verifikasi Breadcrumb `TAG > Stock > Detail > Add Stock`
20. Klik segmen `TAG`
21. Verifikasi tidak ada navigasi (segmen `TAG` tidak bisa diklik)
22. Klik segmen `Add Stock`
23. Verifikasi tidak ada navigasi (segmen terakhir `Add Stock` tidak bisa diklik)
24. Klik segmen `Detail`
25. Verifikasi Detail SKU `RFID-ASSET-CORE-R5` dengan Tab Available aktif
26. Klik Breadcrumb `Stock`
27. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
28. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
29. Klik segmen `Stock` pada Breadcrumb
30. Verifikasi Stock List tampil

### TC-AC-ACTS-803: Dialog konfirmasi modul, backdrop dan Esc

31. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
32. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
33. Klik `[Add by Scan]`, scan TAG A, lalu klik `[Stop]`
34. Klik segmen Breadcrumb `Stock` sehingga dialog Unsaved Changes terbuka
35. Klik area backdrop
36. Verifikasi dialog Unsaved Changes tetap terbuka (backdrop diabaikan)
37. Tekan Esc
38. Verifikasi dialog tertutup setara `[Cancel]` dan list tetap utuh
39. Klik segmen Breadcrumb `Stock` lagi, klik `[Leave]` pada dialog Unsaved Changes
40. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
41. Klik (⋯) pada satu unit, klik `Delete` sehingga dialog `Delete Unit` terbuka
42. Klik area backdrop
43. Verifikasi dialog `Delete Unit` tetap terbuka (backdrop diabaikan)
44. Tekan Esc
45. Verifikasi dialog `Delete Unit` tertutup setara `[Cancel]`
46. Verifikasi unit tidak terhapus
47. Klik `[Audit TAG]` dan `[Start Scan]`, scan satu unit dari dua unit eligible, klik `[Stop]`, klik `[Submit]` sehingga dialog `Confirm Audit` terbuka
48. Klik area backdrop
49. Verifikasi dialog `Confirm Audit` tetap terbuka (backdrop diabaikan)
50. Tekan Esc
51. Verifikasi dialog `Confirm Audit` tertutup setara `[Cancel]`
52. Verifikasi tidak ada perubahan status
53. Buka Approvals > TAG Stock dan klik `[Leave]` pada dialog Unsaved Changes, pastikan Tab Active aktif
54. Klik `Review` pada Subject pending sehingga Dialog Detail Approval terbuka
55. Klik area backdrop
56. Verifikasi Dialog Detail Approval tetap terbuka (backdrop diabaikan)
57. Tekan Esc
58. Verifikasi Dialog Detail Approval tertutup setara `[Cancel]`
59. Verifikasi Subject tetap pending

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 4, 6, 10, 11, 13, 15, dan 16 (membuka Detail SKU GPS dan Event Log untuk membaca baseline dan hasil, serta menutup modal Event Log), langkah 17 dan 18 (membuka halaman Add Stock) dan pembukaan ulang halaman Add Stock lewat Breadcrumb `Stock`, Search, dan row action `Add Stock`.
- TC-AC-ACTS-803 memuat empat dialog dari tiga halaman (Add Stock, Detail SKU Tab Available, Approvals); dialog `Delete Unit`, `Confirm Audit`, dan Dialog Detail Approval hanya diamati perilaku backdrop dan Esc.
- Alasan di atas sekitar 35 langkah (8b butir 7): TC-AC-ACTS-803 satu TC dengan empat dialog yang tidak dapat dipisah (satu TC satu spec), sisanya satu kelas harness.
- Temuan untuk QA:
  - TC-AC-ACTS-803 Langkah 2 sampai 4 menggabungkan beberapa aksi dalam satu langkah; spec memecahnya per aksi dengan urutan TC. Dialog `Delete Unit`, `Confirm Audit`, dan Detail Approval tidak memuat Expected teks dialog; tidak diasersi.
  - TC-AC-ACTS-803 memakai Subject pending dan dua unit eligible Audit di Detail SKU; disediakan seeding milik spec.
  - TC-AC-ACTS-721 mengamati jumlah unit Tab Available dan jumlah sesi Event Log SKU GPS lewat UI (langkah 3, 5, 12, 14) sebelum dan sesudah URL dibuka langsung; spec mengikuti langkah TC.
  - TC-AC-ACTS-721 tidak menyebut cara mengetik URL; URL halaman Add Stock scan untuk SKU GPS disediakan tim FE.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
