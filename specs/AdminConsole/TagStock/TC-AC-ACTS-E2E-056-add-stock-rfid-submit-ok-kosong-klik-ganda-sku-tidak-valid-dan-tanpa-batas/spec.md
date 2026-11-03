---
id: TC-AC-ACTS-E2E-056-add-stock-rfid-submit-ok-kosong-klik-ganda-sku-tidak-valid-dan-tanpa-batas
title: "Add Stock RFID: Submit List Kosong (V-05), Semua OK, Kembali ke Detail SKU, Klik Ganda, dan SKU Tidak Valid saat Submit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-167
  - TC-AC-ACTS-168
  - TC-AC-ACTS-174
  - TC-AC-ACTS-720
  - TC-AC-ACTS-744
coverage:
  web: automated
---

# Add Stock RFID: Submit List Kosong (V-05), Semua OK, Kembali ke Detail SKU, Klik Ganda, dan SKU Tidak Valid saat Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- SKU Pre-setup #24 `RFID-TEMP-UJI-R9` (SKU sementara tanpa unit TAG; dihapus oleh TC-AC-ACTS-720 dan dibuat ulang di hook `before` lewat fixture BE).
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

- Admin lain yang menghapus SKU `RFID-TEMP-UJI-R9` (TC-AC-ACTS-720) memakai sesi API aktor; akunnya tidak ada di Pre-setup TC dan ditulis "disediakan tim FE".
- Kemampuan teknis tambahan: `Spectra.intercept()` untuk menahan respons request Submit (TC-AC-ACTS-174) di atas backend nyata; tahanan dilepas sesudah asersi loading dan di hook `after` bila spec gagal di tengah. Tahanan hanya untuk mengamati state loading dan bukan fault injection.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: Total Registered SKU `RFID-ASSET-CORE-R5`, jumlah baris Event Log Tab Add Stock SKU itu, dan jumlah entri `Add Stock` di Activity Log (lewat kemampuan baca BE)
2. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
3. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-167: Submit dengan list kosong

4. Klik `[Submit]`
5. Verifikasi pesan error `No TAGs to register. Scan at least one TAG.`
6. Verifikasi `[Submit]` tidak disabled
7. Verifikasi error tampil inline di atas tombol `[Submit]`
8. Verifikasi Total Registered SKU sama dengan baseline (tidak ada data tersimpan)

### TC-AC-ACTS-168: Submit semua baris OK

9. Klik `[Add by Scan]`, scan TAG A, scan TAG B, scan TAG C, lalu klik `[Stop]`
10. Klik `[Submit]`
11. Verifikasi toast `Success, TAG has been registered.`
12. Verifikasi halaman Detail SKU `RFID-ASSET-CORE-R5` Tab Available tampil
13. Verifikasi tiga unit baru berstatus Available dengan TAG Code berpola `TAG-XXXXXXXX`
14. Buka modal Event Log SKU itu (Tab Add Stock)
15. Verifikasi baris baru Activity `Add Stock` dengan Success `3` (jumlah baris bertambah satu dari baseline)
16. Tutup modal Event Log
17. Buka Activity Log
18. Verifikasi entri `Add Stock` baru (jumlah entri bertambah satu dari baseline)
19. Klik Breadcrumb `Stock`
20. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
21. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-174: Klik ganda Submit

22. Catat jumlah baris Event Log Tab Add Stock SKU `RFID-ASSET-CORE-R5` sebagai baseline TC-AC-ACTS-174 (lewat kemampuan baca BE)
23. Klik `[Add by Scan]`, scan TAG D, scan TAG E, lalu klik `[Stop]`
24. Tahan respons request Submit dengan intercept
25. Klik `[Submit]` dua kali cepat
26. Verifikasi `[Submit]` disabled dengan indikator loading setelah klik pertama
27. Lepas tahanan respons
28. Tunggu aksi selesai
29. Verifikasi halaman Detail SKU `RFID-ASSET-CORE-R5` Tab Available memuat tepat satu unit untuk TAG D dan satu unit untuk TAG E (tanpa unit ganda)
30. Buka modal Event Log SKU itu (Tab Add Stock)
31. Verifikasi tepat satu baris baru Activity `Add Stock` dengan Success `2` (jumlah baris bertambah satu dari baseline langkah 22)
32. Tutup modal Event Log
33. Klik Breadcrumb `Stock`
34. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
35. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-744: Submit sukses kembali ke Detail SKU

36. Klik `[Add by Scan]`, scan TAG F, lalu klik `[Stop]`
37. Klik `[Submit]`
38. Verifikasi toast `Success, TAG has been registered.`
39. Verifikasi halaman Detail SKU Tab Available tampil tanpa dialog Unsaved Changes
40. Verifikasi unit TAG F tampil di Tab Available berstatus Available
41. Klik Breadcrumb `Stock`
42. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
43. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-720: SKU sudah tidak valid saat Submit

44. Ketik Search `RFID-TEMP-UJI-R9`, tekan Enter
45. Klik (⋯) baris SKU `RFID-TEMP-UJI-R9`, klik `Add Stock`
46. Klik `[Add by Scan]`, scan TAG G, lalu klik `[Stop]`
47. Hapus SKU `RFID-TEMP-UJI-R9` lewat sesi API aktor Admin lain hingga SKU terhapus
48. Tunggu aksi selesai
49. Klik `[Submit]`
50. Verifikasi toast netral `This SKU is no longer available.`
51. Verifikasi Stock List tampil
52. Ketik Search `RFID-TEMP-UJI-R9`, tekan Enter
53. Verifikasi empty state `No results found` (SKU tidak ada di Stock List)
54. Verifikasi tidak ada unit, receipt, atau log tersimpan untuk TAG G lewat kemampuan baca BE

## Notes

- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock) serta pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), pencatatan baseline, `[Stop]`, menahan dan melepas respons Submit TC-AC-ACTS-174 (hanya untuk mengamati state loading), penutupan modal Event Log, dan Search `RFID-TEMP-UJI-R9` untuk menemukan baris target (R-16).
- Volume 1.001 TAG (TC-AC-ACTS-732, kelas e) ada di spec 264.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator RFID) dan satu dataset; tiap blok Submit berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pelaku kedua (Admin yang menghapus SKU) lewat sesi API aktor yang disediakan tim FE/BE; bukan konteks kedua (P-2 tidak dipakai).
- SKU `RFID-TEMP-UJI-R9` (Pre-setup #24) dibuat khusus untuk TC-AC-ACTS-720 dan dihapus oleh TC itu; pembuatan ulang di hook `before` lewat fixture BE (S-06).
- Temuan untuk QA:
  - TC-AC-ACTS-168 Post Condition `Total Registered SKU bertambah 3` tidak memiliki langkah observasi; tidak diasersi.
  - TC-AC-ACTS-720 Expected (a) "server menolak tanpa menyimpan unit, receipt, atau log apa pun" tidak memberi langkah observasi; spec memakai kemampuan baca BE (disediakan tim FE/BE).
  - Entri Activity Log dan baris Event Log baru diasersi sebagai selisih terhadap baseline karena audit trail permanen (S-12).
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
