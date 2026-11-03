---
id: TC-AC-ACTS-E2E-068-add-stock-nfc-submit-waiting-dan-partial-register
title: "Add Stock NFC: Submit Semua Waiting, Campuran OK dan Waiting (Partial Register), Cancel dan Continue, serta Normalisasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-202
  - TC-AC-ACTS-203
  - TC-AC-ACTS-204
  - TC-AC-ACTS-205
  - TC-AC-ACTS-209
coverage:
  web: automated
---

# Add Stock NFC: Submit Semua Waiting, Campuran OK dan Waiting (Partial Register), Cancel dan Continue, serta Normalisasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Akun aktor kedua (Ganti akun): Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Distributor Toggle ON; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #13 `NFC-CARD-BETA-N2` (Device Name `NFC Access Card`, Brand `Beta`, Model `N2`, TAG Type NFC).
- Kemampuan teknis: simulator pemindai NFC (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji NFC (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | UID |
|---|---|
| TAG A | `Fixture.tagStock.nfcA.uid` (`A1B2C3D4E5F7`) |
| TAG B | `Fixture.tagStock.nfcB.uid` |
| TAG C | `Fixture.tagStock.nfcC.uid` |
| TAG D | `Fixture.tagStock.nfcD.uid` |
| TAG E | `Fixture.tagStock.nfcE.uid` |
| TAG F | `Fixture.tagStock.nfcF.uid` |

- Unit existing (status Available) di-seed fixture BE milik spec: satu unit untuk TAG C, TAG D (bentuk kanonik), TAG E, dan TAG F; TAG A dan TAG B belum terdaftar. Jalur approval normal.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: jumlah Subject pending di Approvals > TAG Stock Tab Active, Total Registered SKU `NFC-CARD-BETA-N2`, jumlah baris Event Log Tab Add Stock SKU itu, dan jumlah entri `Add Stock` di Activity Log (lewat kemampuan baca BE)
2. Ketik Search `NFC-CARD-BETA-N2`, tekan Enter
3. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`
4. Klik `[Add by Scan]`
5. Scan TAG A
6. Scan TAG B
7. Scan TAG C
8. Klik `[Stop]`

### TC-AC-ACTS-203: Campuran OK dan Waiting memunculkan dialog Partial Register

9. Klik `[Submit]`
10. Verifikasi dialog `Partial Register`: `1 TAG matched an existing record and will be sent for approval. Register the remaining 2 TAGs?` dengan tombol `[Cancel]` dan `[Continue]`
11. Verifikasi Total Registered SKU sama dengan baseline (belum ada data yang ditulis)

### TC-AC-ACTS-204: Dialog Partial Register, Cancel

12. Klik `[Cancel]` pada dialog
13. Verifikasi dialog tertutup dan kembali ke Scanned TAG List dengan 3 baris utuh
14. Verifikasi tidak ada unit, Subject, receipt, atau log yang tersimpan (Total Registered, jumlah Subject pending, dan jumlah entri `Add Stock` sama dengan baseline)

### TC-AC-ACTS-205: Dialog Partial Register, Continue

15. Klik `[Submit]`
16. Klik `[Continue]` pada dialog
17. Verifikasi toast `Success, TAG has been registered.`
18. Verifikasi halaman Detail SKU `NFC-CARD-BETA-N2` Tab Available tampil
19. Verifikasi dua unit OK (TAG A dan TAG B) memiliki TAG Code baru
20. Verifikasi jumlah Subject pending bertambah satu dari baseline (satu Subject Waiting dibuat)
21. Klik Breadcrumb `Stock`
22. Ganti isi kotak search dengan `NFC-CARD-BETA-N2`, tekan Enter
23. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-209: Identifier huruf kecil dinormalisasi

24. Klik `[Add by Scan]`
25. Scan TAG D dengan identifier huruf kecil yang sama dengan unit existing berbentuk kanonik
26. Klik `[Stop]`
27. Verifikasi baris TAG D berstatus Waiting for Approval (dianggap identifier yang sama)
28. Verifikasi Scanned TAG List menampilkan bentuk kanonik (huruf kapital, tanpa pemisah)
29. Klik `[Submit]`
30. Tunggu aksi selesai
31. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
32. Buka Approvals > TAG Stock > Tab Active
33. Ketik Search `<UID TAG D kanonik>`, tekan Enter
34. Verifikasi Approvals menampilkan identifier TAG D dalam bentuk kanonik (huruf kapital, tanpa pemisah)
35. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
36. Catat jumlah Subject pending, jumlah entri `Add Stock` di Activity Log, dan jumlah baris Event Log SKU `NFC-CARD-BETA-N2` (Tab Add Stock) sebagai baseline sesudah TC-AC-ACTS-209 (lewat kemampuan baca BE)
37. Ganti akun: Logout, login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
38. Klik Breadcrumb `Stock`
39. Ganti isi kotak search dengan `NFC-CARD-BETA-N2`, tekan Enter
40. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-202: Semua Waiting, langsung ke approval tanpa dialog

41. Klik `[Add by Scan]`
42. Scan TAG E
43. Scan TAG F
44. Klik `[Stop]`
45. Klik `[Submit]`
46. Verifikasi tidak ada dialog `Partial Register`
47. Verifikasi toast `Success, 2 TAGs have been sent for approval.`
48. Verifikasi halaman Detail SKU `NFC-CARD-BETA-N2` Tab Available tampil
49. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
50. Buka Approvals > TAG Stock > Tab Active
51. Verifikasi jumlah Subject pending bertambah dua dari baseline sesudah TC-AC-ACTS-209 (langkah 36; dua Subject untuk TAG E dan TAG F)
52. Buka modal Event Log SKU `NFC-CARD-BETA-N2` (Tab Add Stock)
53. Verifikasi jumlah baris Event Log bertambah satu dari baseline sesudah TC-AC-ACTS-209 (langkah 36)
54. Verifikasi baris teratas Event Log (urutan default `Date` terbaru) adalah baris baru Activity `Add Stock` dengan Success `0` dan Waiting for Approval `2`
55. Tutup modal Event Log
56. Buka Activity Log
57. Verifikasi jumlah entri `Add Stock` sama dengan baseline sesudah TC-AC-ACTS-209 (langkah 36; tidak ada entri `Add Stock` baru)

## Notes

- Urutan TC dalam spec: 203, 204, 205, 209, 202 (dialog Partial Register yang tidak menulis data lebih dulu, Submit yang menulis data sesudahnya, S-10).
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), `[Stop]`, Search di Approvals untuk menemukan Subject target (R-16), penutupan modal Event Log, dan pencatatan baseline. Hook `after` memulihkan sesi ke Total Control.
- Angka Subject pending dan entri Activity Log pada TC-AC-ACTS-202 ditulis relatif terhadap baseline karena audit trail permanen (S-12); "tidak ada entri `Add Stock` baru" ditulis sebagai selisih nol dengan anchor baris Event Log baru, bukan kelas g.
- Cara baca entri audit trail baru (S-12, S-14): jumlah dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-202 baris Event Log baru dibaca setelah selisih satu dari baseline langkah 36.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator NFC, akun Distributor Toggle ON) dan satu dataset; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-205 "semuanya dalam satu transaksi" tidak punya langkah observasi; tidak diasersi.
  - TC-AC-ACTS-209 tidak menyebut identifier konkret maupun bentuk kanonik NFC selain "huruf kapital, tanpa pemisah".
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
