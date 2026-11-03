---
id: TC-AC-ACTS-E2E-067-add-stock-nfc-submit-kosong-semua-ok-klik-ganda-normalisasi-dan-saving-state
title: "Add Stock NFC: Submit List Kosong, Semua OK, Klik Ganda, Normalisasi Identifier, dan Saving State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-200
  - TC-AC-ACTS-201
  - TC-AC-ACTS-207
  - TC-AC-ACTS-210
coverage:
  web: automated
---

# Add Stock NFC: Submit List Kosong, Semua OK, Klik Ganda, Normalisasi Identifier, dan Saving State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
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

- Kemampuan teknis tambahan: `Spectra.intercept()` untuk memaksa respons 5xx atau menahan respons request Submit (di atas backend nyata); intercept dilepas segera sesudah asersi dan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: Total Registered SKU `NFC-CARD-BETA-N2`, jumlah baris Event Log Tab Add Stock SKU itu, dan jumlah entri `Add Stock` di Activity Log (lewat kemampuan baca BE)
2. Ketik Search `NFC-CARD-BETA-N2`, tekan Enter
3. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-200: Submit dengan list kosong

4. Klik `[Submit]`
5. Verifikasi pesan error `No TAGs to register. Scan at least one TAG.`
6. Verifikasi `[Submit]` tidak disabled
7. Verifikasi error tampil inline di atas tombol `[Submit]`
8. Verifikasi Total Registered SKU sama dengan baseline (tidak ada data tersimpan)

### TC-AC-ACTS-210: Saving state tombol Submit

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
20. Catat jumlah baris Event Log Tab Add Stock SKU `NFC-CARD-BETA-N2` dan jumlah entri `Add Stock` di Activity Log sebagai baseline sesudah TC-AC-ACTS-210 (lewat kemampuan baca BE)
21. Klik Breadcrumb `Stock`
22. Ganti isi kotak search dengan `NFC-CARD-BETA-N2`, tekan Enter
23. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-201: Submit semua baris OK

24. Klik `[Add by Scan]`, scan TAG B, scan TAG C, scan TAG D, lalu klik `[Stop]`
25. Klik `[Submit]`
26. Verifikasi toast `Success, TAG has been registered.`
27. Verifikasi halaman Detail SKU `NFC-CARD-BETA-N2` Tab Available tampil
28. Verifikasi tiga unit baru berstatus Available dengan TAG Code berpola `TAG-XXXXXXXX`
29. Buka modal Event Log SKU itu (Tab Add Stock)
30. Verifikasi baris baru Activity `Add Stock` dengan Success `3` (jumlah baris bertambah satu dari baseline langkah 20)
31. Tutup modal Event Log
32. Buka Activity Log
33. Verifikasi entri `Add Stock` baru (jumlah entri bertambah satu dari baseline langkah 20)
34. Klik Breadcrumb `Stock`
35. Ganti isi kotak search dengan `NFC-CARD-BETA-N2`, tekan Enter
36. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-207: Klik ganda Submit

37. Catat jumlah baris Event Log Tab Add Stock SKU `NFC-CARD-BETA-N2` sebagai baseline TC-AC-ACTS-207 (lewat kemampuan baca BE)
38. Klik `[Add by Scan]`, scan TAG E, scan TAG F, lalu klik `[Stop]`
39. Tahan respons request Submit dengan intercept
40. Klik `[Submit]` dua kali cepat
41. Verifikasi `[Submit]` disabled dengan indikator loading setelah klik pertama
42. Lepas tahanan respons
43. Tunggu aksi selesai
44. Verifikasi halaman Detail SKU `NFC-CARD-BETA-N2` Tab Available memuat tepat satu unit untuk TAG E dan satu unit untuk TAG F (tanpa unit ganda)
45. Buka modal Event Log SKU itu (Tab Add Stock)
46. Verifikasi tepat satu baris baru Activity `Add Stock` dengan Success `2` (jumlah baris bertambah satu dari baseline langkah 37)

## Notes

- Urutan TC dalam spec: 200, 210, 201, 207 (list kosong lebih dulu; Submit sukses sesudahnya, S-10). Baseline Event Log dan Activity Log TC-AC-ACTS-201 dicatat ulang sesudah TC-AC-ACTS-210 (langkah 20) karena Submit TC-AC-ACTS-210 juga menambah entri.
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), pencatatan baseline, penutupan modal Event Log, dan melepas tahanan respons (termasuk TC-AC-ACTS-207: tahanan dipakai agar state loading sesudah klik pertama teramati). Tahanan respons Submit hanya untuk mengamati state loading dan bukan fault injection; tahanan dilepas pada langkah asersi dan di hook `after` bila spec gagal di tengah.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator NFC) dan satu dataset; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-201 Post Condition `Total Registered SKU bertambah 3` tidak memiliki langkah observasi; tidak diasersi.
  - TC-AC-ACTS-210 tidak menyebut hasil Submit setelah tahanan dilepas; spec hanya melepas tahanan dan menunggu aksi selesai.
  - Entri Activity Log dan baris Event Log baru diasersi sebagai selisih terhadap baseline karena audit trail permanen (S-12).
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
