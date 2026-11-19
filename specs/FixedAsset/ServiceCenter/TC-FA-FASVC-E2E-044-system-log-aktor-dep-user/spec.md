---
id: TC-FA-FASVC-E2E-044-system-log-aktor-dep-user
title: "System Log di Detail User: Entri Aksi Pengguna dan Tidak Ada Entri untuk Perubahan System"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [FASVC-LOGIC-09d, FASVC-LOGIC-09e, "§8#r8", "§8#p7"]
smoke: []
dependsOn: ["User: Detail User > Tab System Log", "Group: pohon Group dan master Group"]
trace:
  FASVC-LOGIC-09d: [23, 24, 25, 26, 27, 28, 56]
  FASVC-LOGIC-09e: [25, 32]
  "§8#r8": [24, 25, 26, 27, 28]
  "§8#p7": [52, 56]
anchor: []
coverage:
  web: automated
---
# System Log di Detail User: Entri Aksi Pengguna dan Tidak Ada Entri untuk Perubahan System

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (cakupan seluruh Group, `Rina W` di kolom Modified By) menguji layarnya dan membuat Service Center yang diuji. Admin Group `Dimas Pratama {runId}` (Total Control, cakupan seluruh Group) memicu perubahan di master Group dari sesinya sendiri.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-044-1: Group `Cabang Sidoarjo {runId}`, parent root pohon Group entitas aktor, tanpa aset dan user.
  - DU-044-2: Group `Cabang Pasuruan {runId}`, parent root pohon Group entitas aktor, tanpa aset dan user.
  - DU-044-3: Service Center `Bengkel Mitra Log Aktor {runId}` yang dibuat aktor, Service type `Routine`, Available to `All groups` (nilai awal Create), Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia` (nilai awal Create), City `Malang` lalu diubah lewat Edit menjadi `Batu`, Company email `logaktor@mitralogaktor.example`, Usage `0`, di-inactivate, di-activate, lalu dihapus.
  - DU-044-4: Service Center `Bengkel Mitra Log Sistem {runId}` yang dibuat aktor, Service type `Routine`, Available to `Cabang Pasuruan {runId}` dan `Cabang Sidoarjo {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia` (nilai awal Create), City `Malang`, Company email `logsistem@mitralogsistem.example`, Usage `0`, Status `Active`.
  - DU-044-5: User Total Control `Rina Wulandari {runId}`, cakupan seluruh Group, Modified By `Rina W`.
  - DU-044-6: User Admin Group `Dimas Pratama {runId}`, role Total Control, cakupan seluruh Group.

## Test Steps

### System Log aktor bertambah satu entri untuk setiap aksi tulis dan Delete
1. Buka Detail User `Rina Wulandari {runId}` di Global Settings > User
2. Pilih tab `System Log`
3. Catat jumlah entri System Log sebagai jumlah awal
4. Buka Add-ons > Service Center lewat sidebar
5. Klik `[+ Service Center]`
6. Isi Name `Bengkel Mitra Log Aktor {runId}`
7. Centang Service type `Routine`
8. Isi City `Malang`
9. Isi Company email `logaktor@mitralogaktor.example`
10. Klik `[Submit]`
11. Ketik Search `Bengkel Mitra Log Aktor {runId}`, tekan Enter
12. Klik `⋯` pada baris `Bengkel Mitra Log Aktor {runId}`, lalu klik `Edit`
13. Ganti isi field City dengan `Batu`
14. Klik `[Save]`
15. Klik `⋯` pada baris `Bengkel Mitra Log Aktor {runId}`, lalu klik `Inactivate`
16. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
17. Klik `⋯` pada baris `Bengkel Mitra Log Aktor {runId}`, lalu klik `Activate`
18. Klik `[Activate]` pada dialog `Activate Service Center`
19. Klik `⋯` pada baris `Bengkel Mitra Log Aktor {runId}`, lalu klik `Delete`
20. Klik `[Delete]` pada dialog `Delete Service Center`
21. Buka Detail User `Rina Wulandari {runId}` di Global Settings > User
22. Pilih tab `System Log`
23. Verifikasi jumlah entri System Log bertambah lima dari jumlah awal
24. Verifikasi entri System Log baru dengan Action `Created` tampil
25. Verifikasi entri System Log baru dengan Action `Updated` tampil
26. Verifikasi entri System Log baru dengan Action `Inactivated` tampil
27. Verifikasi entri System Log baru dengan Action `Activated` tampil
28. Verifikasi entri System Log baru dengan Action `Deleted` tampil

### Aksi Edit tercatat bersama di Changelog dan System Log
29. Buka Add-ons > Service Center lewat sidebar
30. Klik `Changelog` pada toolbar
31. Ketik Search `Bengkel Mitra Log Aktor {runId}` pada modal `Changelog: Service Center`, tekan Enter
32. Verifikasi entri dengan Action `Updated`, Field `City`, Old Value `Malang`, New Value `Batu`, dan Modified By `Rina W` tampil
33. Tutup modal `Changelog: Service Center` lewat icon close

### Perubahan oleh System tidak menulis System Log aktor
34. Buka Add-ons > Service Center lewat sidebar
35. Klik `[+ Service Center]`
36. Isi Name `Bengkel Mitra Log Sistem {runId}`
37. Centang Service type `Routine`
38. Klik field Available to untuk membuka tree
39. Hapus centang `All groups` pada tree Available to
40. Centang `Cabang Sidoarjo {runId}` pada tree Available to
41. Centang `Cabang Pasuruan {runId}` pada tree Available to
42. Isi City `Malang`
43. Isi Company email `logsistem@mitralogsistem.example`
44. Klik `[Submit]`
45. Buka Detail User `Rina Wulandari {runId}` di Global Settings > User
46. Pilih tab `System Log`
47. Catat jumlah entri System Log sebagai jumlah sebelum perubahan System
48. Admin `Dimas Pratama {runId}` menghapus Group `Cabang Sidoarjo {runId}` dari master Group
49. Buka Add-ons > Service Center lewat sidebar
50. Klik `Changelog` pada toolbar
51. Ketik Search `Bengkel Mitra Log Sistem {runId}` pada modal `Changelog: Service Center`, tekan Enter
52. Verifikasi entri dengan Action `Updated`, Field `Available to`, Old Value `Cabang Pasuruan {runId}, Cabang Sidoarjo {runId}`, New Value `Cabang Pasuruan {runId}`, dan Modified By `System` tampil
53. Tutup modal `Changelog: Service Center` lewat icon close
54. Buka Detail User `Rina Wulandari {runId}` di Global Settings > User
55. Pilih tab `System Log`
56. Verifikasi jumlah entri System Log sama dengan jumlah sebelum perubahan System
