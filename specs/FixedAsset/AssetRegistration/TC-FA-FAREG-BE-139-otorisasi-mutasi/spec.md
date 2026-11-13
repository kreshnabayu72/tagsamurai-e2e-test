---
id: TC-FA-FAREG-BE-139-otorisasi-mutasi
title: "Otorisasi mutasi per role dan cakupan Group"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [FAREG-LOGIC-06p, FAREG-LOGIC-10b, FAREG-LOGIC-10f, "§4.8#p2", "§9.2#p7", "§9.2#r14", "§9.2#p63", "§9.2#p64", "§9.3#p1", "§9.4.3#b8", "EB-AKS-3@activate", "EB-AKS-3@cancel-registration", "EB-AKS-3@delete-draft", "EB-AKS-3@keputusan-approval", "EB-AKS-3@save-draft", "EB-AKS-3@simpan-koreksi"]
smoke: []
dependsOn: []
owner: BE
trace:
  FAREG-LOGIC-06p: [40, 42]
  FAREG-LOGIC-10b: [2, 4, 6, 8, 10, 12, 14, 58]
  FAREG-LOGIC-10f: [49, 52, 55, 58]
  "§4.8#p2": [20, 22, 24, 26, 28, 34, 36, 49]
  "§9.2#p7": 60
  "§9.2#r14": [2, 4, 6, 58]
  "§9.2#p63": 16
  "§9.2#p64": 18
  "§9.3#p1": [2, 20, 30, 32, 38]
  "§9.4.3#b8": 30
  "EB-AKS-3@activate": 20
  "EB-AKS-3@cancel-registration": 24
  "EB-AKS-3@delete-draft": 22
  "EB-AKS-3@keputusan-approval": 26
  "EB-AKS-3@save-draft": 8
  "EB-AKS-3@simpan-koreksi": 28
---

# Otorisasi mutasi per role dan cakupan Group

## Prerequisites
- Aktor:
  - Hana T (Total Control, seluruh client).
  - Dewi S (Group Manager Group `Gudang Surabaya {runId}` beserta sub-group).
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`), pembuat dan Owner batch Draft serta pengaju pengajuan.
  - Maya (Manage purchase, Group terkelola `Gudang Surabaya {runId}`).
  - Roni (Read Only, seluruh client).
  - Tono (tanpa capability apa pun di modul registrasi).
  - Eko (hanya capability Read di modul registrasi).
  - Putri (hanya capability Update ditambah Read pada node Group registrasi `Gudang Surabaya {runId}`).
  - Siti (Manage asset & TAG, Group terkelola `Gudang Malang {runId}`, tanpa capability Update pada node Group registrasi `Gudang Surabaya {runId}`).
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Surabaya {runId}`) sebagai approver.
  - Lina (Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`).
  - Joko (Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`) sebagai pengaju.
  - Wati (Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`) sebagai Owner batch Draft.
- Data:
  - DU-139-1: Group `Gudang Surabaya {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-139-2: Group `Gudang Malang {runId}`, ada di entitas aktor.
  - DU-139-3: Asset Name `Meja Kerja {runId}` dengan Brand `Olympic` Model `OL-139` dan Brand `Chitose` Model `Orion`, TAG Type `Non-TAG`, Status `Active`.
  - DU-139-14: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Surabaya {runId}` berisi `2` aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-139`.
  - DU-139-15: batch Draft milik Rina W di Group `Gudang Surabaya {runId}`, Item `Meja Kerja {runId}` Quantity `3`.
  - DU-139-16: batch Draft milik Rina W di Group `Gudang Surabaya {runId}`, Item `Meja Kerja {runId}` Quantity `1`.
  - DU-139-18: batch Draft milik Lina di Group `Gudang Surabaya {runId}`, Item `Meja Kerja {runId}` Quantity `1`.
  - DU-139-19: pengajuan `Waiting for Approval` milik Lina di Group `Gudang Surabaya {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-139-20: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Surabaya {runId}` berisi `1` aset `Meja Kerja {runId}`, diajukan saat Budi memegang capability Update pada node Group registrasi.
  - DU-139-21: pengajuan `Waiting for Approval` milik Joko di Group `Gudang Surabaya {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-139-22: batch Draft milik Wati di Group `Gudang Surabaya {runId}`, Item `Meja Kerja {runId}` Quantity `1`.
  - DU-139-4: akun Hana T, role Total Control, seluruh client.
  - DU-139-5: akun Dewi S, role Group Manager Group `Gudang Surabaya {runId}`.
  - DU-139-6: akun Rina W, role Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`.
  - DU-139-7: akun Maya, role Manage purchase, Group terkelola `Gudang Surabaya {runId}`.
  - DU-139-8: akun Roni, role Read Only, seluruh client.
  - DU-139-9: akun Tono tanpa capability apa pun di modul registrasi.
  - DU-139-10: akun Eko yang hanya memegang capability Read.
  - DU-139-11: akun Putri yang hanya memegang capability Update ditambah Read pada node Group registrasi `Gudang Surabaya {runId}`.
  - DU-139-12: akun Siti, role Manage asset & TAG, Group terkelola `Gudang Malang {runId}`.
  - DU-139-13: akun Budi, role Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Surabaya {runId}`.
  - DU-139-17: akun Lina, role Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`.
- Kondisi:
  - kuota Group `Gudang Surabaya {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.

## Test Steps

### Aktor berhak mengubah batch Draft
1. Rina W sebagai pembuat menyimpan batch DU-139-15 dengan Quantity `4`
2. Verifikasi Save diterima server dan Quantity batch menjadi `4`
3. Hana T menyimpan batch DU-139-15 dengan Quantity `5`
4. Verifikasi Save diterima server dan Quantity batch menjadi `5` karena Total Control mencakup seluruh client
5. Dewi S menyimpan batch DU-139-15 dengan Quantity `6`
6. Verifikasi Save diterima server dan Quantity batch menjadi `6` karena Group batch ada dalam cakupan Group Manager

### Aktor tanpa hak ditolak mengubah batch Draft
7. Maya menyimpan batch DU-139-15 dengan Quantity `7`
8. Verifikasi Save ditolak server dengan copy `You don't have permission to do this.` dan Quantity batch tetap `6`
9. Roni menyimpan batch DU-139-15 dengan Quantity `7`
10. Verifikasi Save ditolak server dan Quantity batch tetap `6`
11. Tono menyimpan batch DU-139-15 dengan Quantity `7`
12. Verifikasi Save ditolak server dan Quantity batch tetap `6`
13. Eko menyimpan batch DU-139-15 dengan Quantity `7`
14. Verifikasi Save ditolak server dan Quantity batch tetap `6`
15. Siti menyimpan batch DU-139-15 dengan Quantity `7`
16. Verifikasi Save ditolak server tanpa mutasi dengan copy `You don't have permission to do this.` karena Group `Gudang Surabaya {runId}` di luar Group terkelola Siti
17. Siti menghapus batch DU-139-15
18. Verifikasi penghapusan ditolak server dan batch tetap ada, karena Siti tidak dapat mengubah atau menghapus batch itu hanya dengan rolenya yang sama dengan Rina W

### Aksi tulis lain tanpa capability ditolak walau UI dilewati
19. Maya mengirim Activate atas batch DU-139-15
20. Verifikasi Activate ditolak server dan batch tetap Draft tanpa pengajuan baru
21. Maya menghapus batch DU-139-16
22. Verifikasi penghapusan ditolak server dan batch tetap ada
23. Maya membatalkan pengajuan DU-139-14
24. Verifikasi pembatalan ditolak server dan pengajuan DU-139-14 tetap `Waiting for Approval`
25. Maya mengirim keputusan `Approve` untuk kedua aset pengajuan DU-139-14
26. Verifikasi keputusan ditolak server dan pengajuan DU-139-14 tetap `Waiting for Approval`
27. Maya menyimpan koreksi Brand aset pertama pengajuan DU-139-14 menjadi `Chitose` dengan Model `Orion`
28. Verifikasi koreksi ditolak server dan aset pertama tidak memiliki koreksi staged

### Peran dalam alur memutuskan pengajuan
29. Rina W sebagai pengaju mengirim keputusan `Approve` untuk kedua aset pengajuan DU-139-14
30. Verifikasi keputusan ditolak server dan pengajuan DU-139-14 tetap `Waiting for Approval` karena pengaju tidak dapat memutuskan pengajuannya sendiri
31. Siti mengirim keputusan `Approve` untuk kedua aset pengajuan DU-139-14
32. Verifikasi keputusan ditolak server karena Siti tidak memegang capability Update pada node Group registrasi `Gudang Surabaya {runId}`
33. Putri menyimpan koreksi Brand aset pertama pengajuan DU-139-14 menjadi `Chitose` dengan Model `Orion`
34. Verifikasi koreksi diterima server dan tersimpan staged karena Putri memegang capability Update
35. Putri menghapus batch DU-139-16
36. Verifikasi penghapusan ditolak server dan batch tetap ada karena Putri tidak memegang capability Delete
37. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-139-14
38. Verifikasi keputusan diterima server dan pengajuan DU-139-14 berstatus `Approved`

### Halaman Approval tanpa hak ditolak server
39. Maya meminta halaman Approval Registration langsung lewat URL
40. Verifikasi permintaan ditolak server dengan copy `You don't have permission to do this.`
41. Roni meminta halaman Approval Registration langsung lewat URL
42. Verifikasi permintaan ditolak server dengan copy `You don't have permission to do this.`

### Hak yang sudah dicabut ditolak dari sesi yang masih terbuka
43. Hana T mencabut role Manage asset & TAG Lina dari Group `Gudang Surabaya {runId}` sementara sesi Lina masih terbuka
44. Lina menyimpan batch DU-139-18 dengan Quantity `2` dari sesi yang haknya sudah dicabut
45. Lina mengirim autosave atas batch DU-139-18 dengan Quantity `2` dari sesi yang sama
46. Lina mengirim Activate atas batch DU-139-18 dari sesi yang sama
47. Lina menghapus batch DU-139-18 dari sesi yang sama
48. Lina membatalkan pengajuan DU-139-19 dari sesi yang sama
49. Verifikasi kelima permintaan Lina ditolak server dengan copy `You don't have permission to do this.` dan batch DU-139-18 serta pengajuan DU-139-19 tidak berubah

### Keputusan mengikuti snapshot approver dan akun yang dinonaktifkan
50. Hana T mencabut capability Update Budi pada node Group registrasi `Gudang Surabaya {runId}` sesudah pengajuan DU-139-20 diajukan
51. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-139-20
52. Verifikasi keputusan diterima server dan pengajuan DU-139-20 berstatus `Approved` karena Budi tercatat sebagai approver pada snapshot pengajuan
53. Hana T menonaktifkan akun Joko, pengaju pengajuan DU-139-21
54. Dewi S mengirim keputusan `Approve` untuk aset pengajuan DU-139-21
55. Verifikasi keputusan diterima server dan pengajuan DU-139-21 berstatus `Approved` walau pengajunya dinonaktifkan
56. Hana T menonaktifkan akun Wati, Owner batch DU-139-22
57. Rina W menyimpan batch DU-139-22 dengan Quantity `3`
58. Verifikasi Save diterima server dan Quantity batch menjadi `3` karena Rina W memegang role dengan akses Group yang sama

### Company diambil dari client user login
59. Rina W menyimpan batch Draft baru di Group `Gudang Surabaya {runId}` dengan Company `PT Surya Lain {runId}` di dalam permintaan
60. Verifikasi batch tersimpan dengan Company client Rina W dan bukan `PT Surya Lain {runId}`
