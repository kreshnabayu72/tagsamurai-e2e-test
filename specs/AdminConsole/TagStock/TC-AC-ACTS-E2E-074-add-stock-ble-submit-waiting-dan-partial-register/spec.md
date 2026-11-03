---
id: TC-AC-ACTS-E2E-074-add-stock-ble-submit-waiting-dan-partial-register
title: "Add Stock BLE: Submit Semua Waiting, Campuran OK dan Waiting (Partial Register), serta Cancel dan Continue"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-231
  - TC-AC-ACTS-232
  - TC-AC-ACTS-233
  - TC-AC-ACTS-234
coverage:
  web: automated
---

# Add Stock BLE: Submit Semua Waiting, Campuran OK dan Waiting (Partial Register), serta Cancel dan Continue

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Akun aktor kedua (Ganti akun): Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Distributor Toggle ON; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
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
| TAG F | `Fixture.tagStock.bleF.mac` |

- Unit existing (status Available) di-seed fixture BE milik spec: satu unit untuk TAG C, TAG D, dan TAG E; TAG A dan TAG B belum terdaftar. Jalur approval normal.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: jumlah Subject pending di Approvals > TAG Stock Tab Active, Total Registered SKU `BLE-BEACON-ALPHA-B1`, jumlah baris Event Log Tab Add Stock SKU itu, dan jumlah entri `Add Stock` di Activity Log (lewat kemampuan baca BE)
2. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
3. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`
4. Klik `[Add by Scan]`
5. Scan TAG A
6. Scan TAG B
7. Scan TAG C
8. Klik `[Stop]`

### TC-AC-ACTS-232: Campuran OK dan Waiting memunculkan dialog Partial Register

9. Klik `[Submit]`
10. Verifikasi dialog `Partial Register`: `1 TAG matched an existing record and will be sent for approval. Register the remaining 2 TAGs?` dengan tombol `[Cancel]` dan `[Continue]`
11. Verifikasi Total Registered SKU sama dengan baseline (belum ada data yang ditulis)

### TC-AC-ACTS-233: Dialog Partial Register, Cancel

12. Klik `[Cancel]` pada dialog
13. Verifikasi dialog tertutup dan kembali ke Scanned TAG List dengan 3 baris utuh
14. Verifikasi tidak ada unit, Subject, receipt, atau log yang tersimpan (Total Registered, jumlah Subject pending, dan jumlah entri `Add Stock` sama dengan baseline)

### TC-AC-ACTS-234: Dialog Partial Register, Continue

15. Klik `[Submit]`
16. Klik `[Continue]` pada dialog
17. Verifikasi toast `Success, TAG has been registered.`
18. Verifikasi halaman Detail SKU `BLE-BEACON-ALPHA-B1` Tab Available tampil
19. Verifikasi dua unit OK (TAG A dan TAG B) memiliki TAG Code baru
20. Verifikasi jumlah Subject pending bertambah satu dari baseline (satu Subject Waiting dibuat)
21. Catat jumlah Subject pending, jumlah entri `Add Stock` di Activity Log, dan jumlah baris Event Log SKU `BLE-BEACON-ALPHA-B1` (Tab Add Stock) sebagai baseline sesudah TC-AC-ACTS-234 (lewat kemampuan baca BE)
22. Klik Breadcrumb `Stock`
23. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
24. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-231: Semua Waiting, langsung ke approval tanpa dialog

25. Klik `[Add by Scan]`
26. Scan TAG D
27. Scan TAG E
28. Klik `[Stop]`
29. Klik `[Submit]`
30. Verifikasi tidak ada dialog `Partial Register`
31. Verifikasi toast `Success, 2 TAGs have been sent for approval.`
32. Verifikasi halaman Detail SKU `BLE-BEACON-ALPHA-B1` Tab Available tampil
33. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
34. Buka Approvals > TAG Stock > Tab Active
35. Verifikasi jumlah Subject pending bertambah dua dari baseline sesudah TC-AC-ACTS-234 (langkah 21; dua Subject untuk TAG D dan TAG E)
36. Buka modal Event Log SKU `BLE-BEACON-ALPHA-B1` (Tab Add Stock)
37. Verifikasi jumlah baris Event Log bertambah satu dari baseline sesudah TC-AC-ACTS-234 (langkah 21)
38. Verifikasi baris teratas Event Log (urutan default `Date` terbaru) adalah baris baru Activity `Add Stock` dengan Success `0` dan Waiting for Approval `2`
39. Tutup modal Event Log
40. Buka Activity Log
41. Verifikasi jumlah entri `Add Stock` sama dengan baseline sesudah TC-AC-ACTS-234 (langkah 21; tidak ada entri `Add Stock` baru)

## Notes

- Urutan TC dalam spec: 232, 233, 234, 231 (dialog Partial Register yang tidak menulis data lebih dulu, Submit yang menulis data sesudahnya, S-10).
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), `[Stop]`, penutupan modal Event Log, dan pencatatan baseline. Hook `after` memulihkan sesi ke Total Control.
- Angka Subject pending dan entri Activity Log pada TC-AC-ACTS-231 ditulis relatif terhadap baseline karena audit trail permanen (S-12); "tidak ada entri `Add Stock` baru" ditulis sebagai selisih nol dengan anchor baris Event Log baru, bukan kelas g.
- Cara baca entri audit trail baru (S-12, S-14): jumlah dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-231 baris Event Log baru dibaca setelah selisih satu dari baseline langkah 21.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator BLE, akun Distributor Toggle ON) dan satu dataset; tiap blok berdiri sendiri.
- Temuan untuk QA: TC-AC-ACTS-234 "semuanya dalam satu transaksi" tidak punya langkah observasi; tidak diasersi.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
