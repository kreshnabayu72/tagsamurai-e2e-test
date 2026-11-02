---
id: TC-AC-ACTS-E2E-078-konkurensi-add-stock-dua-sesi-submit-identifier-sama-dan-hasil-commit-berbeda
title: "Konkurensi Add Stock: Dua Sesi Submit Identifier Sama (RFID dan GPS) dan Hasil Commit Berbeda dari Badge"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-178
  - TC-AC-ACTS-715
  - TC-AC-ACTS-727
coverage:
  web: automated
---

# Konkurensi Add Stock: Dua Sesi Submit Identifier Sama (RFID dan GPS) dan Hasil Commit Berbeda dari Badge

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Distributor Toggle ON; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- SKU Pre-setup #15 `GPS-TRACK-CORE-G3` (TAG Type GPS, halaman Add Stock Import atau Manual Entry IMEI).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |
| TAG C | `Fixture.tagStock.rfidC.epc` | `Fixture.tagStock.rfidC.uid` |

- IMEI uji GPS (Preview Manual Entry): `Fixture.tagStock.imeiA` dan `Fixture.tagStock.imeiB` (Data Uji Dinamis #2, `356938035643809` s/d `356938035643817`), belum terdaftar kecuali disebut lain.
- Admin B: akun kedua untuk sesi UI (TC-AC-ACTS-178 dan TC-AC-ACTS-715) dan sesi API (TC-AC-ACTS-727); tidak ada di Pre-setup TC, disediakan tim FE.
- Unit existing Available untuk TAG C disediakan seeding (TC-AC-ACTS-727); jalur approval normal.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline: Total Registered SKU `RFID-ASSET-CORE-R5` dan `GPS-TRACK-CORE-G3`, serta jumlah Subject pending di Approvals > TAG Stock Tab Active (lewat kemampuan baca BE)
2. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
3. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-178: Dua sesi scan Submit bersamaan dengan identifier sama

4. Klik `[Add by Scan]`
5. Scan TAG A
6. Klik `[Stop]`
7. Ganti ke sesi UI Admin B (konteks browser kedua): login sebagai Admin B, buka TAG > Stock
8. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
9. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
10. Klik `[Add by Scan]`
11. Scan TAG A
12. Klik `[Stop]`
13. Ganti ke sesi Admin A, klik `[Submit]`
14. Tunggu aksi selesai
15. Ganti ke sesi Admin B, klik `[Submit]`
16. Verifikasi unit milik Admin A terdaftar OK (Total Registered SKU bertambah satu dari baseline)
17. Verifikasi identifier milik Admin B diperlakukan sebagai match cross-session (jumlah Subject pending bertambah satu dari baseline)
18. Verifikasi tidak ada unit ganda (Total Registered SKU tetap bertambah satu dari baseline)
19. Verifikasi tidak ada toast error konflik di sesi Admin B
20. Catat jumlah Subject pending sebagai baseline sesudah TC-AC-ACTS-178 (lewat kemampuan baca BE)
21. Tutup sesi Admin B

### TC-AC-ACTS-727: Hasil commit berbeda dari badge di list

22. Klik Breadcrumb `Stock`
23. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
24. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
25. Klik `[Add by Scan]`
26. Scan TAG B (belum terdaftar, badge OK)
27. Scan TAG C (cocok unit existing, badge Waiting for Approval)
28. Klik `[Stop]`
29. Submit TAG B lewat sesi API Admin B hingga unit tersimpan
30. Tunggu aksi selesai
31. Klik `[Submit]`
32. Verifikasi dialog `Partial Register`: `1 TAG matched an existing record and will be sent for approval. Register the remaining 1 TAG?` (hitungan dari badge saat `[Submit]` diklik)
33. Klik `[Continue]`
34. Verifikasi toast `Success, 2 TAGs have been sent for approval.`
35. Verifikasi toast sukses pendaftaran `Success, TAG has been registered.` tidak tampil
36. Verifikasi TAG B dan TAG C sama-sama menjadi Waiting for Approval (jumlah Subject pending bertambah dua dari baseline sesudah TC-AC-ACTS-178, langkah 20)
37. Catat jumlah Subject pending sebagai baseline sesudah TC-AC-ACTS-727 (lewat kemampuan baca BE)
38. Klik Breadcrumb `Stock`

### TC-AC-ACTS-715: Dua submit GPS dengan IMEI sama bersamaan

39. Ganti isi kotak search dengan `GPS-TRACK-CORE-G3`, tekan Enter
40. Klik (⋯) baris SKU `GPS-TRACK-CORE-G3`, klik `Add Stock`
41. Tambahkan IMEI uji lewat Manual Entry untuk membentuk Preview satu baris OK
42. Ganti ke sesi UI Admin B (konteks browser kedua): buka TAG > Stock
43. Ketik Search `GPS-TRACK-CORE-G3`, tekan Enter
44. Klik (⋯) baris SKU `GPS-TRACK-CORE-G3`, klik `Add Stock`
45. Tambahkan IMEI uji yang sama lewat Manual Entry
46. Ganti ke sesi Admin A, klik `[Submit]` (Admin 1)
47. Tunggu aksi selesai
48. Ganti ke sesi Admin B, klik `[Submit]` (Admin 2)
49. Verifikasi unit Admin 1 terdaftar OK (Total Registered SKU GPS bertambah satu dari baseline)
50. Verifikasi IMEI Admin 2 diperlakukan sebagai match cross-session (Waiting), bukan error konflik (jumlah Subject pending bertambah satu dari baseline sesudah TC-AC-ACTS-727, langkah 37)
51. Tutup sesi Admin B

## Notes

- Konteks kedua: sesi UI Admin B (browser kedua) dipakai pada TC-AC-ACTS-178 dan TC-AC-ACTS-715 karena kedua admin memindai atau menyiapkan Preview dan submit secara bergantian (race dua sesi adalah objek uji). TC-AC-ACTS-727 memakai sesi API untuk Admin B karena hasil hanya diasersi di sesi Admin A (pemicu, bukan konteks kedua).
- Admin B tidak ada di Pre-setup TC dan ditulis "disediakan tim FE" (akun kedua). Suite berjalan serial.
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), pencatatan baseline (termasuk baseline sesudah TC-AC-ACTS-178 dan TC-AC-ACTS-727, S-12), `[Stop]`, pembukaan ulang halaman Add Stock sesudah Submit (Breadcrumb `Stock`, Search, row action `Add Stock`), penutupan sesi Admin B, dan "Tunggu aksi selesai" antar aktor.
- Temuan untuk QA:
  - TC-AC-ACTS-178 dan TC-AC-ACTS-715 tidak menyebut akun Admin B (Distributor atau Total Control); Total Control memakai bypass E2a sehingga Admin B diasumsikan Distributor kedua dengan jalur approval normal.
  - TC-AC-ACTS-715 tidak menyebut IMEI uji dan cara membentuk Preview.
  - TC-AC-ACTS-727 memakai istilah "Admin B sudah men-submit" tanpa mekanisme; spec memakai sesi API Admin B.
  - TC-AC-ACTS-178 Expected (b) "tanpa unit ganda" tidak punya langkah observasi selain Total Registered; spec memakai kemampuan baca BE.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (konkurensi dua sesi pada Add Stock) dengan pola serupa; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tambahan (S-14): Klik Breadcrumb `Stock` (langkah 38) dari Detail SKU RFID sebelum Search SKU GPS; Search di Stock List hanya tersedia sesudah kembali ke daftar.
- `P-9` (simulator scan sebagai pembentuk state): TC-AC-ACTS-178 dan TC-AC-ACTS-727 memakai simulator scan RFID hanya untuk membentuk list Scanned TAG (TAG A; TAG B dan TAG C) sebelum Submit; objek uji adalah race dua sesi dan hasil commit yang berbeda dari badge, bukan perangkat scan. Blok GPS (TC-AC-ACTS-715) tidak membutuhkan hardware tetapi tetap di akhir: baseline Subject pending-nya berantai dari baseline sesudah TC-AC-ACTS-727 (langkah 37), sehingga memindahkannya ke awal menuntut pencatatan ulang baseline seluruh blok dan mengubah asersi selisih; state antar blok dipulihkan lewat langkah penghubung (Breadcrumb `Stock`, Search, row action `Add Stock`).
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
