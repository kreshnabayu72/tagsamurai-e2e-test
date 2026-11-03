---
id: TC-AC-ACTS-E2E-052-add-stock-rfid-remove-sukses-baris-waiting-dan-bar-non-interaktif
title: "Add Stock RFID: Remove Sukses, Remove Baris Waiting for Approval, dan Checkbox serta Bulk Bar Non-Interaktif selama Sesi Scan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-872
  - TC-AC-ACTS-873
  - TC-AC-ACTS-874
coverage:
  web: automated
---

# Add Stock RFID: Remove Sukses, Remove Baris Waiting for Approval, dan Checkbox serta Bulk Bar Non-Interaktif selama Sesi Scan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`. Jalur approval normal (tanpa bypass E2a).
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

- Unit existing (status Available, Data Uji Dinamis #7) di-seed fixture BE milik spec dan dipulihkan di hook `after`: satu unit pada SKU `RFID-ASSET-CORE-R5` memegang EPC TAG B (UID TAG B baru) dan satu unit memegang EPC TAG E (UID TAG E baru), sehingga TAG B dan TAG E berstatus Waiting for Approval pada Scanned TAG List.
- Baseline jumlah Subject pending di Approvals > TAG Stock Tab Active dan Total Registered SKU dibaca lewat kemampuan baca BE sebelum TC-AC-ACTS-873.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
3. Klik `[Add by Scan]`
4. Scan TAG A
5. Scan TAG B
6. Scan TAG C
7. Klik `[Stop]`

### TC-AC-ACTS-872: Remove sukses dan list kosong

8. Centang TAG A dan TAG B
9. Pilih Bulk Action > `Remove`, klik `[Remove]`
10. Verifikasi toast `Success, TAG has been removed.`
11. Verifikasi list menyisakan TAG C
12. Verifikasi bar hilang dan seleksi 0
13. Klik `Select All (1 record)`
14. Pilih Bulk Action > `Remove`, klik `[Remove]`
15. Verifikasi list kosong
16. Verifikasi tombol `[Remove by Scan]` Disabled
17. Klik `[Add by Scan]`
18. Verifikasi live counter widget `0 TAGs scanned`
19. Klik `[Stop]`

### TC-AC-ACTS-873: Remove baris Waiting for Approval

20. Catat jumlah Subject pending di Approvals > TAG Stock Tab Active sebagai baseline
21. Catat Total Registered SKU `RFID-ASSET-CORE-R5` sebagai baseline (kemampuan baca BE)
22. Klik `[Add by Scan]`
23. Scan TAG D
24. Scan TAG E
25. Klik `[Stop]`
26. Verifikasi baris TAG E berstatus Waiting for Approval
27. Centang TAG E
28. Pilih Bulk Action > `Remove`, klik `[Remove]`
29. Verifikasi TAG E keluar dari list
30. Klik `[Submit]`
31. Verifikasi toast `Success, TAG has been registered.`
32. Verifikasi tidak ada dialog `Partial Register`
33. Verifikasi jumlah Subject pending sama dengan baseline (tidak ada Subject Approval baru untuk TAG E)
34. Verifikasi Total Registered SKU `RFID-ASSET-CORE-R5` bertambah tepat 1 dari baseline (hanya TAG D yang terdaftar)
35. Klik Breadcrumb `Stock`
36. Ganti isi kotak search dengan `RFID-ASSET-CORE-R5`, tekan Enter
37. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-874: Kontrol non-interaktif selama sesi scan

38. Klik `[Add by Scan]`
39. Scan TAG A
40. Scan TAG B
41. Scan TAG C
42. Klik `[Stop]`
43. Centang TAG A
44. Klik `[Add by Scan]`
45. Coba klik checkbox TAG B, Select All, dan aksi pada bar
46. Verifikasi halaman terkunci (blur) dan checkbox, Select All, serta bar tidak dapat diklik
47. Verifikasi hanya `[Stop]` yang interaktif
48. Klik `[Stop]`
49. Verifikasi checkbox, Select All, dan bar interaktif kembali
50. Klik `[Cancel]`
51. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
52. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), pembentukan list precondition (scan lalu `[Stop]`), `[Add by Scan]` dan `[Stop]` untuk melihat counter, dan penutupan halaman dirty di akhir (S-08). Sesudah `[Submit]` TC-AC-ACTS-873 halaman Add Stock dibuka ulang untuk TC-AC-ACTS-874.
- TAG A, B, C dipakai ulang di TC-AC-ACTS-874 karena semuanya sudah dikeluarkan dari list pada TC-AC-ACTS-872 tanpa Submit; TAG D didaftarkan oleh Submit TC-AC-ACTS-873 dan dihapus fixture BE di hook `after`.
- Temuan untuk QA:
  - TC-AC-ACTS-873 menyebut TAG B Waiting, tetapi TAG B sudah dikeluarkan pada TC-AC-ACTS-872; spec memakai TAG E sebagai baris Waiting (unit existing seed) dan TAG D sebagai baris OK.
  - TC-AC-ACTS-874 tidak lagi mengasersi seleksi TAG A sesudah `[Stop]`; spec tidak mengasersinya dan tidak memakai `Unselect All` sesudahnya.
  - TC-AC-ACTS-873 Expected "tidak ada Subject Approval baru untuk TAG B" ditulis sebagai selisih jumlah Subject pending terhadap baseline (kemampuan baca BE disediakan tim FE/BE).
  - Toast sukses Remove memakai bentuk tunggal `Success, TAG has been removed.` walau dua TAG dikeluarkan (TC-AC-ACTS-872).
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator RFID) dan satu dataset (Scanned TAG List); tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
