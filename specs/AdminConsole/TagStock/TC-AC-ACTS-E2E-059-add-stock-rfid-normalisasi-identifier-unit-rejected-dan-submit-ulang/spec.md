---
id: TC-AC-ACTS-E2E-059-add-stock-rfid-normalisasi-identifier-unit-rejected-dan-submit-ulang
title: "Add Stock RFID: Normalisasi Identifier, Identifier Unit Rejected Terdaftar sebagai Unit Baru, dan Submit Ulang Batch yang Sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-176
  - TC-AC-ACTS-740
  - TC-AC-ACTS-745
coverage:
  web: automated
---

# Add Stock RFID: Normalisasi Identifier, Identifier Unit Rejected Terdaftar sebagai Unit Baru, dan Submit Ulang Batch yang Sama

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

- Unit existing Available kanonik untuk TAG A (TC-AC-ACTS-176); unit Rejected R1 memegang EPC TAG B dan unit Rejected R2 memegang UID TAG C tanpa unit Available, Damaged/Missing, atau In Use lain berisi EPC atau UID itu (TC-AC-ACTS-740); unit Available B1 memegang EPC dan UID TAG D, didaftarkan sesi sebelumnya (TC-AC-ACTS-745; sebelum blok itu unit Waiting hasil TC-AC-ACTS-176 dibersihkan lewat fixture BE agar banner Waiting tidak tampil). Seluruhnya di-seed fixture BE milik spec dan dipulihkan di hook `after`.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-176: Identifier huruf kecil dinormalisasi

3. Klik `[Add by Scan]`
4. Scan TAG A dengan identifier huruf kecil yang sama dengan unit existing berbentuk kanonik
5. Klik `[Stop]`
6. Verifikasi baris TAG A berstatus Waiting for Approval (dianggap identifier yang sama)
7. Verifikasi Scanned TAG List menampilkan bentuk kanonik (huruf kapital, tanpa pemisah)
8. Klik `[Submit]`
9. Tunggu aksi selesai
10. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
11. Buka Approvals > TAG Stock > Tab Active
12. Ketik Search `<EPC TAG A kanonik>`, tekan Enter
13. Verifikasi Approvals menampilkan identifier TAG A dalam bentuk kanonik (huruf kapital, tanpa pemisah)
14. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
15. Ganti akun: Logout, login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
16. Klik Breadcrumb `Stock`
17. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
18. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-740: Identifier unit Rejected terdaftar sebagai unit baru

19. Catat baseline: jumlah Subject pending di Approvals Tab Active (lewat kemampuan baca BE)
20. Klik `[Add by Scan]`
21. Scan TAG B (EPC milik unit Rejected R1, UID baru)
22. Scan TAG C (EPC baru, UID milik unit Rejected R2)
23. Klik `[Stop]`
24. Verifikasi baris TAG B berstatus OK (success) tanpa tooltip match
25. Verifikasi baris TAG C berstatus OK (success) tanpa tooltip match
26. Klik `[Submit]`
27. Verifikasi tidak ada dialog `Partial Register`
28. Verifikasi tidak ada toast T-04
29. Verifikasi toast `Success, TAG has been registered.`
30. Verifikasi dua unit baru berstatus Available dengan TAG Code baru
31. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
32. Buka Approvals > TAG Stock > Tab History
33. Verifikasi unit Rejected R1 dan R2 tetap Rejected tanpa TAG Code
34. Buka Approvals > TAG Stock > Tab Active
35. Verifikasi jumlah Subject pending sama dengan baseline (tidak ada Subject baru)
36. Ganti akun: Logout, login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
37. Klik Breadcrumb `Stock`
38. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
39. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-745: Submit ulang batch yang sama tidak idempotent

40. Hapus unit Waiting for Approval dan Subject pending hasil Submit TC-AC-ACTS-176 pada SKU `RFID-ASSET-CORE-R5` lewat fixture BE (precondition TC-AC-ACTS-745: tidak ada unit Waiting pada SKU itu)
41. Catat baseline: jumlah Subject pending dan jumlah entri `Waiting for Approval` di Activity Log (lewat kemampuan baca BE)
42. Klik `[Add by Scan]`
43. Scan TAG D (EPC dan UID sama dengan unit Available B1 yang terdaftar oleh sesi sebelumnya)
44. Klik `[Stop]`
45. Verifikasi baris TAG D berstatus Waiting for Approval (identifier cocok unit Available)
46. Klik `[Submit]`
47. Verifikasi toast `Success, 1 TAG has been sent for approval.`
48. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
49. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
50. Verifikasi banner Tab Available `1 TAG is waiting for approval.`
51. Verifikasi unit B1 tetap satu baris Available dan tidak berubah
52. Buka Approvals > TAG Stock > Tab Active
53. Verifikasi terbentuk Subject Register Duplicate baru untuk TAG D (jumlah Subject pending bertambah satu dari baseline)
54. Buka Activity Log
55. Verifikasi entri `Waiting for Approval` baru tercatat (jumlah entri bertambah satu dari baseline)
56. Buka Notification Center sebagai approver
57. Verifikasi notifikasi baru terkirim ke approver pool

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), pembukaan ulang halaman Add Stock sesudah ganti akun (Breadcrumb `Stock`, Search, row action `Add Stock`), `[Stop]`, Search di Approvals untuk menemukan Subject target (R-16), dan pencatatan baseline.
- Hook `after` memulihkan sesi ke Total Control.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator RFID, akun Distributor Toggle ON) dan satu dataset; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-176 tidak menyebut identifier konkret; spec memakai bentuk huruf kecil dari identifier TAG A yang dimiliki unit existing seed.
  - TC-AC-ACTS-176 tidak menyebut bentuk kanonik untuk RFID EPC dan UID selain "huruf kapital, tanpa pemisah".
  - TC-AC-ACTS-740 memakai EPC dan UID yang sama dengan Data Uji Dinamis #1 dan #4; unit Rejected R1 dan R2 diseed fixture BE milik spec dan dipulihkan di hook `after`.
  - TC-AC-ACTS-745 Expected (c) "notifikasi ke approver pool" diasersi sebagai notifikasi baru di Notification Center approver; TC tidak menyebut isi notifikasi.
- Langkah penghubung tambahan (S-03, 8b butir 8): "Tunggu aksi selesai" (langkah 9) sesudah `[Submit]` TC-AC-ACTS-176 yang hasilnya tidak diasersi dan sebelum ganti akun.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
