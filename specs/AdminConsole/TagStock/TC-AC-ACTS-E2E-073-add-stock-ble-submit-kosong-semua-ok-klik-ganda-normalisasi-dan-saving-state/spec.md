---
id: TC-AC-ACTS-E2E-073-add-stock-ble-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state
title: "Add Stock BLE: Submit List Kosong, Semua OK, Klik Ganda, Normalisasi Identifier, dan Saving State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-229
  - TC-AC-ACTS-230
  - TC-AC-ACTS-236
  - TC-AC-ACTS-238
  - TC-AC-ACTS-239
coverage:
  web: automated
---

# Add Stock BLE: Submit List Kosong, Semua OK, Klik Ganda, Normalisasi Identifier, dan Saving State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
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
| TAG F | `Fixture.tagStock.bleF.mac` |

- Unit existing Available pada SKU `BLE-BEACON-ALPHA-B1` yang memegang MAC kanonik `DEADBEEF0001` (Data Uji Dinamis #6) untuk TC-AC-ACTS-238 di-seed fixture BE milik spec (MAC ini khusus TC-AC-ACTS-238 dan bukan MAC TAG A); jalur approval normal dipakai TC-AC-ACTS-238.
- Kemampuan teknis tambahan: `Spectra.intercept()` untuk memaksa respons 5xx atau menahan respons request Submit (di atas backend nyata); intercept dilepas segera sesudah asersi dan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: Total Registered SKU `BLE-BEACON-ALPHA-B1`, jumlah baris Event Log Tab Add Stock SKU itu, dan jumlah entri `Add Stock` di Activity Log (lewat kemampuan baca BE)
2. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
3. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-229: Submit dengan list kosong

4. Klik `[Submit]`
5. Verifikasi pesan error `No TAGs to register. Scan at least one TAG.`
6. Verifikasi `[Submit]` tidak disabled
7. Verifikasi error tampil inline di atas tombol `[Submit]`
8. Verifikasi Total Registered SKU sama dengan baseline (tidak ada data tersimpan)

### TC-AC-ACTS-239: Saving state tombol Submit

9. Klik `[Add by Scan]`
10. Scan TAG A
11. Klik `[Stop]`
12. Hover `[Submit]`
13. Verifikasi `[Submit]` menampilkan state hover
14. Tahan respons request Submit dengan intercept
15. Klik `[Submit]`
16. Verifikasi `[Submit]` berstatus loading dan disabled
17. Verifikasi `[Cancel]` ikut disabled
18. Lepas tahanan respons
19. Tunggu aksi selesai
20. Catat baseline sesudah TC-AC-ACTS-239: jumlah baris Event Log Tab Add Stock SKU `BLE-BEACON-ALPHA-B1` dan jumlah entri `Add Stock` di Activity Log (lewat kemampuan baca BE)
21. Klik Breadcrumb `Stock`
22. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
23. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-230: Submit semua baris OK

24. Klik `[Add by Scan]`, scan TAG B, scan TAG C, scan TAG D, lalu klik `[Stop]`
25. Klik `[Submit]`
26. Verifikasi toast `Success, TAG has been registered.`
27. Verifikasi halaman Detail SKU `BLE-BEACON-ALPHA-B1` Tab Available tampil
28. Verifikasi tiga unit baru berstatus Available dengan TAG Code berpola `TAG-XXXXXXXX`
29. Buka modal Event Log SKU itu (Tab Add Stock)
30. Verifikasi baris baru Activity `Add Stock` dengan Success `3` (jumlah baris bertambah satu dari baseline langkah 20)
31. Tutup modal Event Log
32. Buka Activity Log
33. Verifikasi entri `Add Stock` baru (jumlah entri bertambah satu dari baseline langkah 20)
34. Klik Breadcrumb `Stock`
35. Ganti isi kotak search dengan `BLE-BEACON-ALPHA-B1`, tekan Enter
36. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-236: Klik ganda Submit

37. Klik `[Add by Scan]`, scan TAG E, scan TAG F, lalu klik `[Stop]`
38. Klik `[Submit]` dua kali cepat
39. Verifikasi `[Submit]` disabled dengan indikator loading setelah klik pertama
40. Verifikasi hanya satu batch terdaftar (tepat dua unit baru TAG E dan TAG F, tanpa unit ganda)
41. Ganti akun: Logout, login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
42. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
43. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-238: Identifier BLE dinormalisasi

44. Klik `[Add by Scan]`
45. Scan TAG dengan MAC `de:ad:be:ef:00:01` (huruf kecil, pemisah `:`) yang sama dengan unit existing dengan MAC kanonik `DEADBEEF0001`
46. Klik `[Stop]`
47. Verifikasi baris berstatus Waiting for Approval (dianggap identifier yang sama)
48. Verifikasi Scanned TAG List menampilkan bentuk kanonik (huruf kapital, tanpa pemisah)
49. Klik `[Submit]`
50. Tunggu aksi selesai
51. Ganti akun: Logout, login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
52. Buka Approvals > TAG Stock > Tab Active
53. Ketik Search `DEADBEEF0001`, tekan Enter
54. Verifikasi Approvals menampilkan MAC `DEADBEEF0001` dalam bentuk kanonik (huruf kapital, tanpa pemisah)
55. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Urutan TC dalam spec: 229, 239, 230, 236, 238 (list kosong lebih dulu; Submit yang menulis data sesudahnya; akun Distributor terakhir karena hanya TC-AC-ACTS-238 memerlukan jalur approval normal, S-10).
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), pencatatan baseline (termasuk baseline sesudah TC-AC-ACTS-239 pada langkah 20, S-12), penutupan modal Event Log, Search di Approvals untuk menemukan Subject target (R-16), dan melepas tahanan respons. Tahanan respons Submit hanya untuk mengamati state loading dan bukan fault injection; tahanan dilepas pada langkah asersi dan di hook `after` bila spec gagal di tengah. Hook `after` memulihkan sesi ke Total Control.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator BLE) dan satu dataset; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-230 Post Condition `Total Registered SKU bertambah 3` tidak memiliki langkah observasi; tidak diasersi.
  - TC-AC-ACTS-239 tidak menyebut hasil Submit setelah tahanan dilepas; spec hanya melepas tahanan dan menunggu aksi selesai.
  - TC-AC-ACTS-238 memakai MAC `de:ad:be:ef:00:01` terhadap unit existing `DEADBEEF0001` (Data Uji Dinamis #6); unit existing diseed fixture BE milik spec.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
