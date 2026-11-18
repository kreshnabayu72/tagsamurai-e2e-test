---
id: TC-FA-ASTL-E2E-020-delete-asset-data
title: "Delete Asset Data menghapus aset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-17a", "ASTL-LOGIC-17c", "ASTL-LOGIC-17d", "ASTL-LOGIC-17m", "§9.7#r14", "EB-FRM-1@delete-asset-data", "EB-BLK-3", "EB-ERR-3", "EB-EDG-3", "EB-FB-1@delete-asset-data"]
smoke: ["EB-ERR-3", "EB-EDG-3", "EB-FB-1@delete-asset-data"]
dependsOn: []
trace:
  "ASTL-LOGIC-17a": [11, 15, 17, 27]
  "ASTL-LOGIC-17c": [9, 21]
  "ASTL-LOGIC-17d": 9
  "ASTL-LOGIC-17m": [37, 39, 42, 44, 46, 48, 51, 53, 56, 58, 61, 63]
  "§9.7#r14": [15, 27, 65, 66]
  "EB-FRM-1@delete-asset-data": [14, 26]
  "EB-BLK-3": [11, 23, 26]
  "EB-ERR-3": [33, 34]
  "EB-EDG-3": 17
  "EB-FB-1@delete-asset-data": 14
anchor: [3, 6]
coverage:
  web: automated
---
# Delete Asset Data menghapus aset

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-020-1: aset Disposed tanpa blokir apa pun, Asset Name `Genset 20kVA {runId}`, tampil `Genset 20kVA {runId} - 1`, Brand `Perkins`, Model/Type `403A-15G2`, Category `Peralatan Listrik`, Group `Cabang Medan {runId}`, Status `Disposed`, memiliki entri Changelog.
  - DU-020-2: aset Disposed tanpa blokir, Asset Name `Lemari Besi {runId}`, tampil `Lemari Besi {runId} - 1`, Brand `Brother`, Model/Type `LB-4`, Category `Furniture`, Group `Cabang Medan {runId}`, Status `Disposed`.
  - DU-020-3: aset Disposed tanpa blokir, Asset Name `Rak Server {runId}`, tampil `Rak Server {runId} - 1`, Brand `Rittal`, Model/Type `TS8`, Category `Peralatan IT`, Group `Cabang Medan {runId}`, Status `Disposed`.
  - DU-020-4: aset Disposed tanpa blokir, Asset Name `Meja Rapat {runId}`, tampil `Meja Rapat {runId} - 1`, Brand `Informa`, Model/Type `Oval 8`, Category `Furniture`, Group `Cabang Medan {runId}`, Status `Disposed`.
  - DU-020-5: aset Active Unmanaged Custody `Available` dengan penyusutan Posted dan record Missing berjalan, Asset Name `Mesin Fotokopi {runId}`, tampil `Mesin Fotokopi {runId} - 1`, Brand `Ricoh`, Model/Type `IM 2702`, Category `Peralatan Kantor`, Group `Cabang Medan {runId}`, Status `Available, Unmanaged`.
  - DU-020-6: aset Active Unmanaged Custody `Available` dengan record Missing berjalan dan Activity Lock `In Audit`, Asset Name `Dispenser {runId}`, tampil `Dispenser {runId} - 1`, Brand `Sanken`, Model/Type `HWD-760`, Category `Peralatan Kantor`, Group `Cabang Medan {runId}`, Status `Available, Unmanaged`.
  - DU-020-8: aset Active Unmanaged Custody `Available` dengan penyusutan Posted dan Disposal `Executed` yang jurnal pelepasannya belum Posted, Asset Name `Kompresor {runId}`, tampil `Kompresor {runId} - 1`, Brand `Atlas Copco`, Model/Type `GX 2`, Category `Peralatan Industri`, Group `Cabang Medan {runId}`, Status `Available, Unmanaged`.
  - DU-020-9: aset Active Unmanaged Custody `Available` dengan Disposal `Executed` yang jurnal pelepasannya belum Posted dan record Missing berjalan, Asset Name `Pompa Air {runId}`, tampil `Pompa Air {runId} - 1`, Brand `Grundfos`, Model/Type `CM 5`, Category `Peralatan Industri`, Group `Cabang Medan {runId}`, Status `Available, Unmanaged`.
  - DU-020-10: aset Active Unmanaged Custody `Available` dengan record Missing berjalan dan Disposal Report `Reported`, Asset Name `Forklift Mini {runId}`, tampil `Forklift Mini {runId} - 1`, Brand `Toyota`, Model/Type `8FBE15`, Category `Kendaraan`, Group `Cabang Medan {runId}`, Status `Available, Unmanaged`.
  - DU-020-11: aset Active Unmanaged Custody `Available` dengan Disposal Report `Reported` dan Activity Lock `In Audit`, Asset Name `Timbangan Digital {runId}`, tampil `Timbangan Digital {runId} - 1`, Brand `Ohaus`, Model/Type `T31P`, Category `Peralatan Gudang`, Group `Cabang Medan {runId}`, Status `Available, Unmanaged`.
  - DU-020-7: Group `Cabang Medan {runId}`.
  - Sesi pengamat: sesi browser kedua dengan aktor Total Control membuka All Assets, kartu `Disposed`, dengan Search yang memuat DU-020-1, sebelum langkah 1, dan tidak dimuat ulang sesudahnya.

## Test Steps

### Delete Asset Data satu aset lewat Row Action
1. Ketik Search `{runId}`, tekan Enter
2. Klik kartu `Disposed`
3. Verifikasi baris `Genset 20kVA {runId} - 1` tampil pada tabel
4. Catat jumlah pada kartu `Disposed`
5. Klik ikon `Changelog` pada toolbar
6. Verifikasi Changelog memuat entri untuk `Genset 20kVA {runId} - 1`
7. Tutup modal Changelog
8. Klik menu `⋯` pada baris `Genset 20kVA {runId} - 1`
9. Verifikasi `Delete Asset Data` tersedia sebagai Row Action dan tidak `Disabled` untuk aset `Disposed` tanpa blokir
10. Pilih `Delete Asset Data`
11. Verifikasi dialog `Delete Asset Data` memuat bullet `Genset 20kVA {runId} - 1`, teks `All attachments of the selected asset in File Manager will also be deleted.`, dan `Are you sure you want to delete it? This action cannot be undone.`
12. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
13. Klik `[Delete]`
14. Verifikasi toast `Success, asset data has been deleted.` tampil
15. Verifikasi baris `Genset 20kVA {runId} - 1` hilang dari tabel dan jumlah pada kartu `Disposed` berkurang satu
16. Klik ikon `Changelog` pada toolbar
17. Verifikasi Changelog tidak lagi memuat entri untuk `Genset 20kVA {runId} - 1` karena log aset ikut terhapus
18. Tutup modal Changelog

### Delete Asset Data dua aset lewat Bulk Action
19. Centang baris `Lemari Besi {runId} - 1` dan baris `Rak Server {runId} - 1`
20. Klik `Bulk Action`
21. Verifikasi `Delete Asset Data` tersedia sebagai Bulk Action dan tidak `Disabled`
22. Pilih `Delete Asset Data`
23. Verifikasi dialog `Delete Asset Data` memuat bullet `Lemari Besi {runId} - 1` dan `Rak Server {runId} - 1`, teks `All attachments of the selected assets in File Manager will also be deleted.`, dan `Are you sure you want to delete them? This action cannot be undone.`
24. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
25. Klik `[Delete]` dua kali berturut-turut dengan cepat
26. Verifikasi hanya satu toast `Success, asset data has been deleted.` tampil untuk kedua aset, karena klik kedua tidak memproses ulang aset
27. Verifikasi baris `Lemari Besi {runId} - 1` dan baris `Rak Server {runId} - 1` hilang dari tabel

### Aset sudah dihapus pihak lain saat konfirmasi
28. Klik menu `⋯` pada baris `Meja Rapat {runId} - 1`
29. Pilih `Delete Asset Data`
30. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
31. Aktor lain menghapus permanen aset `Meja Rapat {runId} - 1`
32. Klik `[Delete]`
33. Verifikasi toast `This asset is no longer available.` tampil
34. Verifikasi dialog `Asset Changed` tidak tampil dan baris `Meja Rapat {runId} - 1` tidak ada pada tabel yang dimuat ulang

### Penyebab blokir yang didahulukan pada satu aset
35. Klik kartu `All`
36. Klik menu `⋯` pada baris `Mesin Fotokopi {runId} - 1`
37. Verifikasi `Delete Asset Data` tampil `Disabled` untuk aset berjejak Posted dengan laporan kehilangan yang masih berjalan
38. Arahkan pointer ke `Delete Asset Data`
39. Verifikasi tooltip `Asset has posted depreciation or journal entries. Use Disposal.` tampil, bukan tooltip penyebab lain
40. Tutup menu aksi baris dengan `Esc`
41. Klik menu `⋯` pada baris `Dispenser {runId} - 1`
42. Verifikasi `Delete Asset Data` tampil `Disabled` untuk aset dengan laporan kehilangan yang masih berjalan dan Activity Lock `In Audit`
43. Arahkan pointer ke `Delete Asset Data`
44. Verifikasi tooltip `Asset has an ongoing missing record. Complete or close the record first.` tampil, bukan tooltip Activity Lock

### Urutan penyebab blokir pada pasangan penyebab lain
45. Klik menu `⋯` pada baris `Kompresor {runId} - 1`
46. Verifikasi `Delete Asset Data` tampil `Disabled`
47. Arahkan pointer ke `Delete Asset Data`
48. Verifikasi tooltip `Asset has posted depreciation or journal entries. Use Disposal.` tampil, bukan tooltip penyebab berikutnya
49. Tutup menu aksi baris dengan `Esc`
50. Klik menu `⋯` pada baris `Pompa Air {runId} - 1`
51. Verifikasi `Delete Asset Data` tampil `Disabled`
52. Arahkan pointer ke `Delete Asset Data`
53. Verifikasi tooltip `Asset has a disposal that is not posted yet.` tampil, bukan tooltip penyebab berikutnya
54. Tutup menu aksi baris dengan `Esc`
55. Klik menu `⋯` pada baris `Forklift Mini {runId} - 1`
56. Verifikasi `Delete Asset Data` tampil `Disabled`
57. Arahkan pointer ke `Delete Asset Data`
58. Verifikasi tooltip `Asset has an ongoing missing record. Complete or close the record first.` tampil, bukan tooltip penyebab berikutnya
59. Tutup menu aksi baris dengan `Esc`
60. Klik menu `⋯` pada baris `Timbangan Digital {runId} - 1`
61. Verifikasi `Delete Asset Data` tampil `Disabled`
62. Arahkan pointer ke `Delete Asset Data`
63. Verifikasi tooltip `Asset has an open disposal report or request. Cancel or complete it first.` tampil, bukan tooltip penyebab berikutnya
64. Tutup menu aksi baris dengan `Esc`

### Sesi lain melihat aset hilang tanpa muat ulang
65. Verifikasi pada sesi pengamat, tanpa memuat ulang halaman, jumlah pada kartu `Disposed` berkurang satu dari jumlah yang dicatat pada langkah 4
66. Verifikasi pada sesi pengamat baris `Genset 20kVA {runId} - 1` hilang dari tabel
