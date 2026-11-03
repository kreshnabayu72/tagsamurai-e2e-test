---
id: TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris
title: "Screening Sub-Tab Allocation History: Kolom, Isi Baris, Filter Status dan License Type, serta Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-33
  - TC-FA-LIC-34
  - TC-FA-LIC-35
  - TC-FA-LIC-36
  - TC-FA-LIC-37
  - TC-FA-LIC-39
coverage:
  web: automated
---

# Screening Sub-Tab Allocation History: Kolom, Isi Baris, Filter Status dan License Type, serta Empty State

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; General Settings `dd/MM/yy`, `HH:mm`; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License (Tab All License) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #13: empat term Subscription dan enam alokasi (LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001), data kuota #12 (ledger Add-on IT Inventory Total 200). Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: alokasi berstatus Waiting for Approval, Rejected, Canceled, dan Pending (TC-FA-LIC-35, langkah 22) serta alokasi Asset Control Station dan Storage (TC-FA-LIC-36, langkah 29) ditambahkan lewat fixture BE pada client ini. Hook `after` menghapus alokasi tambahan dan memulihkan Pre-setup #13. Fixture BE penyetel dan pemulih disediakan tim FE/BE.
- Kemampuan teknis: kemampuan membaca data Subscription dan Allocation client dari Admin Console lewat fixture BE (TC-FA-LIC-37), disediakan tim FE/BE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-33: Screening sub-tab Allocation History

1. Klik sub-tab `Allocation History`
2. Verifikasi Title `Allocation History` dengan Subtitle `Record of asset license and add-on quota allocations.`
3. Verifikasi Toolbar: `Search | Filter | Download`
4. Verifikasi Kolom: `Allocation ID (sortable) | Subscription ID (sortable) | License Type (sortable) | Quantity (sortable) | Status (sortable) | Date (sortable) | End Date (sortable) | Plan Owner (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable)`
5. Verifikasi tidak ada row action
6. Verifikasi Allocation ID berupa teks biasa tanpa link

### TC-FA-LIC-34: Isi baris Allocation History

7. Verifikasi urutan baris: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
8. Verifikasi LALC-20260801-00004: License Type `Addon (IT Inventory)`, Quantity `+1`, Date 01/08/26, End Date 31/12/26, Plan Owner `PT Maju Bersama (Distributor)`, Last Updated 01/08/26 09:30
9. Verifikasi LALC-20260801-00004: Status `Active` severity success
10. Verifikasi License Type `Asset License` dengan Quantity: LALC-20260101-00001 `+3000`, LALC-20260312-00002 `+1500`, LALC-20260720-00003 `+500`
11. Verifikasi LALC-20250210-00001: Status `Expired` severity danger, Subscription ID SUBS-20250101-00001, Last Updated 01/01/26 00:05

### TC-FA-LIC-39: Empty state hasil Search kosong

12. Ketik Search `zzzz`, tekan Enter
13. Verifikasi ilustrasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
14. Klik `(←)` pada kotak Search

### TC-FA-LIC-37: Kedua riwayat tidak digabung dan tidak dihitung ulang

15. Baca jumlah baris Subscription dan Allocation client dari Admin Console lewat fixture BE
16. Klik sub-tab `Subscription History`
17. Verifikasi Subscription History menampilkan baris sumbernya apa adanya (sama dengan data Admin Console)
18. Klik sub-tab `Allocation History`
19. Verifikasi Allocation History menampilkan baris sumbernya apa adanya (sama dengan data Admin Console)
20. Verifikasi tidak ada baris gabungan antara kedua tabel
21. Verifikasi Total addon pada License Summary (`+ IT Inventory` Total 200) tidak sama dengan jumlah cuplikan Allocation History (Quantity `+1`)

### TC-FA-LIC-35: Hanya alokasi yang sudah disetujui

22. Tambah alokasi Waiting for Approval, Rejected, Canceled, dan Pending lewat fixture BE, lalu muat ulang halaman License
23. Klik sub-tab `Allocation History`
24. Verifikasi alokasi Pending tampil
25. Verifikasi alokasi Waiting for Approval, Rejected, dan Canceled tidak tampil
26. Buka Filter Panel
27. Buka opsi field Status
28. Verifikasi opsi filter Status hanya memuat `Pending`, `Active`, `Expired`

### TC-FA-LIC-36: Hanya License Type Asset License dan Addon

29. Tambah alokasi Asset Control Station dan Storage lewat fixture BE, lalu muat ulang halaman License
30. Klik sub-tab `Allocation History`
31. Verifikasi baris alokasi Pre-setup #13 tetap tampil: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
32. Verifikasi baris Asset Control Station dan Storage tidak tampil
33. Buka Filter Panel
34. Buka opsi field License Type
35. Verifikasi opsi License Type memuat `Asset License` dan `Addon (...)` saja

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-33, 34, 35, 36, 37, 39). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: blok baca (TC-33, 34, 39, 37) di awal dan blok yang menambah alokasi lewat fixture (TC-35, 36) di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 14 (menutup input Search dengan `(←)`), langkah 16 dan 18 (klik sub-tab sesuai langkah TC-37), langkah 23 dan 30 (membuka sub-tab `Allocation History` sesudah muat ulang halaman).
- Asersi pembanding di luar Expected TC (S-03): langkah 24 (alokasi Pending tampil) ditaruh sebelum asersi absence pada langkah 25 sebagai data pembanding pada tabel yang sama, sehingga urutan Verifikasi butir TC-FA-LIC-35 ditukar; langkah 31 (baris alokasi Pre-setup #13 tetap tampil) mendahului asersi absence pada langkah 32.
- Temuan untuk QA:
  - TC-37 menyebut "data Admin Console" sebagai pembanding tanpa menyebut cara membacanya; langkah 15 memakai kemampuan baca fixture BE (disediakan tim FE/BE). Expected "Total addon pada License Summary tidak sama dengan jumlah cuplikan Allocation History" tidak menyebut nilai; langkah 21 memakai `+ IT Inventory` Total 200 dan Quantity `+1` dari Pre-setup #12 dan #13.
  - TC-35 Expected c ("Opsi filter Status hanya memuat `Pending`, `Active`, `Expired`") berlaku untuk keadaan sesudah fixture menambah alokasi berstatus Pending; TC tidak menyebut apakah opsi `Pending` ada tanpa alokasi Pending.
