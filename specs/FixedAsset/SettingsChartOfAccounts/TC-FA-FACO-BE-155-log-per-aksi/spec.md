---
id: TC-FA-FACO-BE-155-log-per-aksi
title: "Pencatatan log per aksi akun pada tiga surface"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [J-06, L-01, L-02, L-03, L-04, "§8#r3", "§8#r4", "§8.1#p1", "§9.7#r17", "§9.7#r20", "§9.7#r22", "§9.7#r25", "§9.7#r28", "§8.1#p2", "§8.1#p3"]
smoke: []
dependsOn: []
trace:
  J-06: [29, 30, 32, 33, 35, 36]
  L-01: [2, 3, 4, 5, 29, 30]
  L-02: [7, 8, 9, 11, 13, 15, 16, 32, 33]
  L-03: [18, 20, 26, 27]
  L-04: [22, 23, 24, 35, 36]
  "§8#r3": [3, 7, 11, 13, 18]
  "§8#r4": [3, 7, 18, 22]
  "§8.1#p1": [3, 7, 15, 16, 22, 26, 27]
  "§9.7#r17": [3, 4, 5, 29, 30]
  "§9.7#r20": [7, 8, 9, 11, 13, 15, 16, 32, 33]
  "§9.7#r22": [18]
  "§9.7#r25": [20, 26, 27]
  "§9.7#r28": [22, 23, 24, 35, 36]
  "§8.1#p2": [3, 4, 5, 22, 23, 24, 29, 30, 35, 36]
  "§8.1#p3": [13, 16, 38, 39, 41, 42]
---

# Pencatatan log per aksi akun pada tiga surface

## Prerequisites
- Aktor: Admin A dan pemanggil terotorisasi, keduanya Total Control dengan cakupan seluruh client.
- Data:
  - DU-155-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-155-2: User `Rudi Integrasi {runId}`, Access Level `Total Control`, cakupan seluruh client, pemanggil terotorisasi yang mengirim request langsung.
  - DU-155-4: Account Code `LG2-{runId}`, Account Name `Beban Transport {runId}`, Account Function `Depreciation Expense`.
  - DU-155-6: Account Code `LG3-{runId}`, Account Name `Beban Penyusutan Mesin {runId}`, Account Function `Depreciation Expense`.
  - DU-155-8: Account Code `LG4-{runId}`, Account Name `Kas Cabang Utara {runId}`, Account Function `Asset Cost`.
  - DU-155-10: Account Code `LG5-{runId}`, Account Name `Beban Asuransi Gedung {runId}`, Account Function `Depreciation Expense`.
  - DU-155-12: Account Code `LG6-{runId}`, Account Name `Kas Cadangan {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-155-13: Account Code `LG7-{runId}`, Account Name `Kas Operasional Harian {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-155-14: Account Code `LG8-{runId}`, Account Name `Kas Dihapus {runId}`, Account Function `Asset Cost`.
  - DU-155-15: Account Code `LG9A-{runId}`, Account Name `Kas Bulk Log Satu {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-155-16: Account Code `LG9B-{runId}`, Account Name `Kas Bulk Log Dua {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-155-19: Account Code `LG11-{runId}`, Account Name `Kas Proyek Timur {runId}`, Account Function `Asset Cost`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor dan tidak dipakai Asset Class (Used By 0), sehingga tidak ada field yang terkunci dan Deactivate serta Delete tidak diblokir.
  - Batas jumlah akun client belum tercapai.

## Test Steps

### Create menulis satu kejadian L-01 pada ketiga surface
1. Admin A (DU-155-1) mengirim Create dengan Account Code `LG1-{runId}`, Account Name `Beban Pemasaran {runId}`, Account Function `Depreciation Expense`
2. Verifikasi akun `LG1-{runId}` tersimpan dan terbaca ulang
3. Verifikasi Changelog memuat tepat satu baris untuk akun `LG1-{runId}` dengan Action `Create`, Account Code `LG1-{runId}`, Field `Account Code`, Old Value `-` (satu tanda hubung), dan New Value `LG1-{runId}`
4. Verifikasi System Log milik Admin A memuat tepat satu entri untuk akun `LG1-{runId}` dengan Action `Create`, Object `Chart of Accounts`, Name `LG1-{runId}`, Field `Account Code`, Old Value `-`, dan New Value `LG1-{runId}`
5. Verifikasi Activity Log memuat tepat satu entri untuk akun `LG1-{runId}` dengan Action `Create`, Object `Chart of Accounts`, Name `LG1-{runId}`, Field `Account Code`, Old Value `-`, dan New Value `LG1-{runId}`, dan Modified By adalah Admin A

### Edit satu field menulis satu baris per surface
6. Admin A (DU-155-1) mengirim Edit akun `LG2-{runId}` dengan Account Name `Beban Transportasi Darat {runId}`
7. Verifikasi Changelog memuat tepat satu baris untuk akun `LG2-{runId}` dengan Action `Edit`, Account Code `LG2-{runId}`, Field `Account Name`, Old Value `Beban Transport {runId}`, dan New Value `Beban Transportasi Darat {runId}`
8. Verifikasi System Log milik Admin A memuat tepat satu entri untuk akun `LG2-{runId}` dengan Action `Edit`, Object `Chart of Accounts`, Name `LG2-{runId}`, Field `Account Name`, Old Value `Beban Transport {runId}`, dan New Value `Beban Transportasi Darat {runId}`
9. Verifikasi Activity Log memuat tepat satu entri untuk akun `LG2-{runId}` dengan Action `Edit`, Object `Chart of Accounts`, Name `LG2-{runId}`, Field `Account Name`, Old Value `Beban Transport {runId}`, dan New Value `Beban Transportasi Darat {runId}`, dan Modified By adalah Admin A
10. Admin A (DU-155-1) mengirim Edit akun `LG3-{runId}` dengan Account Function `Accumulated Depreciation`
11. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG3-{runId}` dengan Action `Edit`, Field `Account Function`, Old Value `Depreciation Expense`, dan New Value `Accumulated Depreciation`
12. Admin A (DU-155-1) mengirim Edit akun `LG4-{runId}` dengan Account Code `LG4B-{runId}`
13. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG4B-{runId}` dengan Action `Edit`, Field `Account Code`, Old Value `LG4-{runId}`, dan New Value `LG4B-{runId}`, dan kolom Account Code serta Name berisi kode setelah perubahan

### Edit dua field dalam satu Save menulis satu baris per field
14. Admin A (DU-155-1) mengirim Edit akun `LG5-{runId}` dengan Account Name `Beban Asuransi Kendaraan {runId}` dan Account Function `Loss on Disposal` dalam satu Save
15. Verifikasi Changelog memuat tepat dua baris untuk akun `LG5-{runId}`: satu dengan Field `Account Name`, Old Value `Beban Asuransi Gedung {runId}`, dan New Value `Beban Asuransi Kendaraan {runId}`, satu dengan Field `Account Function`, Old Value `Depreciation Expense`, dan New Value `Loss on Disposal`
16. Verifikasi System Log milik Admin A dan Activity Log masing-masing memuat tepat dua entri untuk akun `LG5-{runId}`, satu per field yang berubah

### Activate dan Deactivate dicatat sebagai Edit atas field Status
17. Admin A (DU-155-1) mengirim Activate atas akun `LG6-{runId}`
18. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG6-{runId}` dengan Action `Edit`, Field `Status`, Old Value `Inactive`, dan New Value `Active`
19. Admin A (DU-155-1) mengirim Deactivate atas akun `LG7-{runId}`
20. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG7-{runId}` dengan Action `Edit`, Field `Status`, Old Value `Active`, dan New Value `Inactive`

### Delete menulis satu kejadian L-04 pada ketiga surface
21. Admin A (DU-155-1) mengirim Delete atas akun `LG8-{runId}`
22. Verifikasi Changelog memuat tepat satu baris untuk akun `LG8-{runId}` dengan Action `Delete`, Account Code `LG8-{runId}`, Field `Account Code`, Old Value `LG8-{runId}`, dan New Value `-` (satu tanda hubung)
23. Verifikasi System Log milik Admin A memuat tepat satu entri untuk akun `LG8-{runId}` dengan Action `Delete`, Object `Chart of Accounts`, Name `LG8-{runId}`, Field `Account Code`, Old Value `LG8-{runId}`, dan New Value `-`
24. Verifikasi Activity Log memuat tepat satu entri untuk akun `LG8-{runId}` dengan Action `Delete`, Object `Chart of Accounts`, Name `LG8-{runId}`, Field `Account Code`, Old Value `LG8-{runId}`, dan New Value `-`, dan Modified By adalah Admin A

### Aksi bulk menulis satu kejadian per akun yang berhasil pada setiap surface
25. Admin A (DU-155-1) mengirim Deactivate bulk atas akun `LG9A-{runId}` dan `LG9B-{runId}`
26. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG9A-{runId}` dengan Action `Edit`, Field `Status`, Old Value `Active`, dan New Value `Inactive`
27. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG9B-{runId}` dengan Action `Edit`, Field `Status`, Old Value `Active`, dan New Value `Inactive`

### Request langsung oleh pemanggil terotorisasi menulis log pada ketiga surface
28. Pemanggil terotorisasi (DU-155-2) mengirim Create lewat request langsung dengan Account Code `LG10-{runId}`, Account Name `Kas Integrasi {runId}`, Account Function `Asset Cost`
29. Verifikasi Changelog dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG10-{runId}` dengan Action `Create`, Field `Account Code`, Old Value `-`, dan New Value `LG10-{runId}`, dan Modified By adalah pemanggil itu
30. Verifikasi System Log milik pemanggil memuat tepat satu entri untuk akun `LG10-{runId}` dengan Action `Create`, Object `Chart of Accounts`, Name `LG10-{runId}`, Field `Account Code`, Old Value `-`, dan New Value `LG10-{runId}`
31. Pemanggil terotorisasi (DU-155-2) mengirim Edit lewat request langsung atas akun `LG10-{runId}` dengan Account Name `Kas Integrasi Terbarui {runId}`
32. Verifikasi Changelog dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG10-{runId}` dengan Action `Edit`, Field `Account Name`, Old Value `Kas Integrasi {runId}`, dan New Value `Kas Integrasi Terbarui {runId}`, dan Modified By adalah pemanggil itu
33. Verifikasi System Log milik pemanggil memuat tepat satu entri untuk akun `LG10-{runId}` dengan Action `Edit`, Object `Chart of Accounts`, Name `LG10-{runId}`, Field `Account Name`, Old Value `Kas Integrasi {runId}`, dan New Value `Kas Integrasi Terbarui {runId}`
34. Pemanggil terotorisasi (DU-155-2) mengirim Delete lewat request langsung atas akun `LG10-{runId}`
35. Verifikasi Changelog dan Activity Log masing-masing memuat tepat satu baris untuk akun `LG10-{runId}` dengan Action `Delete`, Field `Account Code`, Old Value `LG10-{runId}`, dan New Value `-`, dan Modified By adalah pemanggil itu
36. Verifikasi System Log milik pemanggil memuat tepat satu entri untuk akun `LG10-{runId}` dengan Action `Delete`, Object `Chart of Accounts`, Name `LG10-{runId}`, Field `Account Code`, Old Value `LG10-{runId}`, dan New Value `-`

### Edit multi-field yang mengubah Account Code menamai semua entri dengan kode baru
37. Admin A (DU-155-1) mengirim Edit akun `LG11-{runId}` dengan Account Code `LG11B-{runId}` dan Account Name `Kas Proyek Timur Baru {runId}` dalam satu Save
38. Verifikasi System Log milik Admin A memuat tepat dua entri bernama `LG11B-{runId}` dengan Action `Edit` dan Object `Chart of Accounts`: satu dengan Field `Account Code`, Old Value `LG11-{runId}`, dan New Value `LG11B-{runId}`, satu dengan Field `Account Name`, Old Value `Kas Proyek Timur {runId}`, dan New Value `Kas Proyek Timur Baru {runId}`
39. Verifikasi Activity Log memuat tepat dua entri bernama `LG11B-{runId}` dengan Action `Edit` dan Object `Chart of Accounts`: satu dengan Field `Account Code`, Old Value `LG11-{runId}`, dan New Value `LG11B-{runId}`, satu dengan Field `Account Name`, Old Value `Kas Proyek Timur {runId}`, dan New Value `Kas Proyek Timur Baru {runId}`

### Edit kode berikutnya tidak memperbarui entri log yang sudah ditulis
40. Admin A (DU-155-1) mengirim Edit akun `LG11B-{runId}` dengan Account Code `LG11C-{runId}`
41. Verifikasi System Log milik Admin A dan Activity Log masing-masing memuat tepat satu entri bernama `LG11C-{runId}` dengan Action `Edit`, Field `Account Code`, Old Value `LG11B-{runId}`, dan New Value `LG11C-{runId}`
42. Verifikasi System Log milik Admin A dan Activity Log masing-masing tetap memuat tepat dua entri bernama `LG11B-{runId}` dari Save pada langkah 37, dengan Field `Account Code` (Old Value `LG11-{runId}`, New Value `LG11B-{runId}`) dan Field `Account Name` (Old Value `Kas Proyek Timur {runId}`, New Value `Kas Proyek Timur Baru {runId}`)
