---
id: TC-AC-ACTS-E2E-058-add-stock-rfid-submit-waiting-partial-register-dan-bentuk-tunggal-jamak
title: "Add Stock RFID: Submit Semua Waiting, Campuran OK dan Waiting (Dialog Partial Register), Cancel dan Continue, serta Bentuk Tunggal dan Jamak"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-169
  - TC-AC-ACTS-170
  - TC-AC-ACTS-171
  - TC-AC-ACTS-172
  - TC-AC-ACTS-746
  - TC-AC-ACTS-761
coverage:
  web: automated
---

# Add Stock RFID: Submit Semua Waiting, Campuran OK dan Waiting (Dialog Partial Register), Cancel dan Continue, serta Bentuk Tunggal dan Jamak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Akun aktor kedua (Ganti akun): Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Distributor Toggle ON; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
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
| TAG E | `Fixture.tagStock.rfidE.epc` | `Fixture.tagStock.rfidE.uid` |
| TAG F | `Fixture.tagStock.rfidF.epc` | `Fixture.tagStock.rfidF.uid` |
| TAG G | `Fixture.tagStock.rfidG.epc` | `Fixture.tagStock.rfidG.uid` |
| TAG H | `Fixture.tagStock.rfidH.epc` | `Fixture.tagStock.rfidH.uid` |
| TAG I | `Fixture.tagStock.rfidI.epc` | `Fixture.tagStock.rfidI.uid` |
| TAG J | `Fixture.tagStock.rfidJ.epc` | `Fixture.tagStock.rfidJ.uid` |

- Unit existing (status Available) di-seed fixture BE milik spec: satu unit untuk tiap TAG C, D, E, F, dan G (EPC dan UID sama dengan TAG itu); TAG A dan TAG B belum terdaftar. Jalur approval normal (tanpa bypass E2a).
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: jumlah Subject pending di Approvals > TAG Stock Tab Active, Total Registered SKU `RFID-ASSET-CORE-R5`, jumlah baris Event Log Tab Add Stock SKU itu, dan jumlah entri `Add Stock` di Activity Log (lewat kemampuan baca BE)
2. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
3. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
4. Klik `[Add by Scan]`
5. Scan TAG A
6. Scan TAG B
7. Scan TAG C
8. Scan TAG D
9. Klik `[Stop]`

### TC-AC-ACTS-761: Beberapa TAG cocok existing, dialog bentuk jamak

10. Klik `[Submit]`
11. Verifikasi dialog `Partial Register`: `2 TAGs matched existing records and will be sent for approval. Register the remaining 2 TAGs?` dengan tombol `[Cancel]` dan `[Continue]`
12. Verifikasi Total Registered SKU sama dengan baseline (belum ada data yang ditulis)
13. Klik `[Cancel]` pada dialog
14. Centang TAG D
15. Pilih Bulk Action > `Remove`, klik `[Remove]`

### TC-AC-ACTS-170: Campuran OK dan Waiting memunculkan dialog Partial Register

16. Klik `[Submit]`
17. Verifikasi dialog `Partial Register`: `1 TAG matched an existing record and will be sent for approval. Register the remaining 2 TAGs?` dengan tombol `[Cancel]` dan `[Continue]`
18. Verifikasi Total Registered SKU sama dengan baseline (belum ada data yang ditulis)

### TC-AC-ACTS-171: Dialog Partial Register, Cancel

19. Klik `[Cancel]` pada dialog
20. Verifikasi dialog tertutup dan kembali ke Scanned TAG List dengan 3 baris utuh
21. Verifikasi tidak ada unit, Subject, receipt, atau log yang tersimpan (Total Registered, jumlah Subject pending, dan jumlah entri `Add Stock` sama dengan baseline)

### TC-AC-ACTS-172: Dialog Partial Register, Continue

22. Klik `[Submit]`
23. Klik `[Continue]` pada dialog
24. Verifikasi toast `Success, TAG has been registered.`
25. Verifikasi halaman Detail SKU `RFID-ASSET-CORE-R5` Tab Available tampil
26. Verifikasi dua unit OK (TAG A dan TAG B) memiliki TAG Code baru
27. Verifikasi jumlah Subject pending bertambah satu dari baseline (satu Subject Waiting dibuat)
28. Catat jumlah Subject pending, jumlah entri `Add Stock` di Activity Log, dan jumlah baris Event Log SKU `RFID-ASSET-CORE-R5` (Tab Add Stock) sebagai baseline sesudah TC-AC-ACTS-172 (lewat kemampuan baca BE)
29. Klik Breadcrumb `Stock`
30. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
31. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-169: Semua Waiting, langsung ke approval tanpa dialog

32. Klik `[Add by Scan]`
33. Scan TAG E
34. Scan TAG F
35. Klik `[Stop]`
36. Klik `[Submit]`
37. Verifikasi tidak ada dialog `Partial Register`
38. Verifikasi toast `Success, 2 TAGs have been sent for approval.`
39. Verifikasi halaman Detail SKU `RFID-ASSET-CORE-R5` Tab Available tampil
40. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
41. Buka Approvals > TAG Stock > Tab Active
42. Verifikasi jumlah Subject pending bertambah dua dari baseline sesudah TC-AC-ACTS-172 (langkah 28; dua Subject untuk TAG E dan TAG F)
43. Buka modal Event Log SKU `RFID-ASSET-CORE-R5` (Tab Add Stock)
44. Verifikasi jumlah baris Event Log bertambah satu dari baseline sesudah TC-AC-ACTS-172 (langkah 28)
45. Verifikasi baris teratas Event Log (urutan default `Date` terbaru) adalah baris baru Activity `Add Stock` dengan Success `0` dan Waiting for Approval `2`
46. Tutup modal Event Log
47. Buka Activity Log
48. Verifikasi jumlah entri `Add Stock` sama dengan baseline sesudah TC-AC-ACTS-172 (langkah 28; tidak ada entri `Add Stock` baru)
49. Ganti akun: Logout, login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
50. Klik Breadcrumb `Stock`
51. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
52. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-746: Satu TAG cocok existing, toast bentuk tunggal

53. Klik `[Add by Scan]`
54. Scan TAG G
55. Klik `[Stop]`
56. Klik `[Submit]`
57. Verifikasi tidak ada dialog `Partial Register`
58. Verifikasi toast `Success, 1 TAG has been sent for approval.`
59. Verifikasi halaman Detail SKU `RFID-ASSET-CORE-R5` Tab Available tampil

## Notes

- Urutan TC dalam spec: 761, 170, 171, 172, 169, 746 (dialog Partial Register yang tidak menulis data lebih dulu pada satu sesi; Submit yang menulis data sesudahnya, S-10). Dari list 2 OK + 2 Waiting (TC-AC-ACTS-761) satu baris Waiting dikeluarkan lewat Remove agar menjadi list 2 OK + 1 Waiting (TC-AC-ACTS-170 sampai TC-AC-ACTS-172).
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), `[Stop]`, `[Cancel]` dialog, Remove TAG D, penutupan modal Event Log, dan pencatatan baseline.
- Catatan angka Subject pending dan entri Activity Log pada TC-AC-ACTS-169 ditulis relatif terhadap baseline karena audit trail permanen (S-12); kemampuan baca BE disediakan tim FE/BE.
- Cara baca entri audit trail baru (S-12, S-14): jumlah dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-169 baris Event Log baru dibaca setelah selisih satu dari baseline langkah 28.
- Asersi "tidak ada entri `Add Stock` baru" TC-AC-ACTS-169 ditulis sebagai selisih jumlah nol dengan baseline dan anchor positif baris Event Log baru; bukan kelas g (bagian 3, asersi jumlah).
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator RFID, akun Distributor Toggle ON) dan satu dataset; tiap blok Submit berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACTS-172 "semuanya dalam satu transaksi" tidak punya langkah observasi; tidak diasersi.
  - TC-AC-ACTS-169 Expected (d) menyebut "tidak ada entri Activity Log `Add Stock`"; ditulis relatif terhadap baseline.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
