---
id: TC-FA-FATR-E2E-039-gating-cabut
title: "Hak berubah saat halaman terbuka dan gabungan beberapa peran"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§2#p2, EB-AKS-6]
smoke: []
dependsOn: []
trace:
  §2#p2: [5, 6, 9, 10, 11, 19, 20, 21, 24, 25, 26, 34, 35, 36, 37, 39, 48]
  EB-AKS-6: [52, 53, 54, 55]
anchor: []
coverage:
  web: automated
---
# Hak berubah saat halaman terbuka dan gabungan beberapa peran

## Prerequisites
- Aktor: pemegang beberapa peran `Dewi Anggraeni {runId}`, `Eko Wibowo {runId}`, dan `Fani Susanto {runId}`; pemegang Global Role Manage transaction settings (Read, Update) `Sari Rahayu {runId}`; pemicu pencabutan hak Total Control `Tari Kusuma {runId}`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-039-1: User `Dewi Anggraeni {runId}`, Global Role Manage transaction settings (Read) dan Group Role Manage asset & TAG (Read, Update) pada Group `Cabang Surabaya {runId}`, bukan Total Control, tanpa tingkat akses Read Only, ada di entitas aktor.
  - DU-039-2: User `Eko Wibowo {runId}`, Global Role Manage transaction settings (Read, Update) dan Group Role Manage asset & TAG (Read) pada Group `Cabang Surabaya {runId}`, bukan Total Control, tanpa tingkat akses Read Only, ada di entitas aktor.
  - DU-039-3: User `Fani Susanto {runId}`, tingkat akses Read Only, Global Role Manage transaction settings (Read, Update), dan Group Role Manage asset & TAG (Read, Update) pada Group `Cabang Surabaya {runId}`, bukan Total Control, ada di entitas aktor.
  - DU-039-4: User `Sari Rahayu {runId}`, Global Role Manage transaction settings (Read, Update), bukan Total Control, tanpa Group Role Manage asset & TAG, tanpa tingkat akses Read Only, ada di entitas aktor.
  - DU-039-5: User `Tari Kusuma {runId}`, tingkat akses Total Control, ada di entitas aktor.
  - DU-039-6: Group `Cabang Surabaya {runId}`.
  - DU-039-7: Category leaf `Perlengkapan Cabang {runId}` di bawah Category induk `Logistik {runId}`; pada tab Borrow, field `Max duration` bernilai sendiri `13` dan field `Max extensions` Inherit, dibuat oleh aktor lain.
- Kondisi:
  - Akun `Dewi Anggraeni {runId}`, `Eko Wibowo {runId}`, `Fani Susanto {runId}`, `Sari Rahayu {runId}`, dan `Tari Kusuma {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Gabungan Global Role Read dan Group Role Update
1. Masuk sebagai `Dewi Anggraeni {runId}`
2. Ketik Search Sidebar Category Tree `Perlengkapan Cabang {runId}`, tekan Enter
3. Klik Category `Perlengkapan Cabang {runId}`
4. Klik tab `Borrow`
5. Verifikasi kontrol field `Max duration` disabled dengan nilai `13`
6. Verifikasi tombol `[+ Override]` tampil dan aktif
7. Klik `[+ Override]`
8. Klik pilihan Scope
9. Verifikasi opsi Scope `Group` tampil dan aktif
10. Verifikasi opsi Scope `Asset Name` disabled
11. Verifikasi opsi Scope `Asset` tampil dan aktif
12. Tekan Esc untuk menutup daftar Scope
13. Klik `✕` pada dialog Add override

### Gabungan Global Role Update dan Group Role Read
14. Keluar dari akun `Dewi Anggraeni {runId}`
15. Masuk sebagai `Eko Wibowo {runId}`
16. Ketik Search Sidebar Category Tree `Perlengkapan Cabang {runId}`, tekan Enter
17. Klik Category `Perlengkapan Cabang {runId}`
18. Klik tab `Borrow`
19. Verifikasi kontrol field `Max duration` aktif
20. Verifikasi tombol `[Set own value]` tampil pada field `Max extensions`
21. Verifikasi tombol `[+ Override]` tampil dan aktif
22. Klik `[+ Override]`
23. Klik pilihan Scope
24. Verifikasi opsi Scope `Asset Name` tampil dan aktif
25. Verifikasi opsi Scope `Group` disabled
26. Verifikasi opsi Scope `Asset` disabled
27. Tekan Esc untuk menutup daftar Scope
28. Klik `✕` pada dialog Add override

### Tingkat akses Read Only membatasi peran Update menjadi Read saja
29. Keluar dari akun `Eko Wibowo {runId}`
30. Masuk sebagai `Fani Susanto {runId}`
31. Ketik Search Sidebar Category Tree `Perlengkapan Cabang {runId}`, tekan Enter
32. Klik Category `Perlengkapan Cabang {runId}`
33. Klik tab `Borrow`
34. Verifikasi tombol `[Export rules]` tampil dan aktif
35. Verifikasi kontrol field `Max duration` disabled dengan nilai `13`
36. Verifikasi tombol `[Save]` tampil dan disabled
37. Verifikasi tombol `[+ Override]` tampil dan disabled
38. Klik ikon `Changelog` pada header halaman
39. Verifikasi dialog `Changelog: Transaction Settings` tampil
40. Klik `✕` pada dialog Changelog

### Hak Update dicabut saat halaman terbuka
41. Keluar dari akun `Fani Susanto {runId}`
42. Masuk sebagai `Sari Rahayu {runId}`
43. Ketik Search Sidebar Category Tree `Perlengkapan Cabang {runId}`, tekan Enter
44. Klik Category `Perlengkapan Cabang {runId}`
45. Klik tab `Borrow`
46. Klik `[Set own value]` pada field `Max extensions`
47. Ganti isi field `Max extensions` dengan `3`
48. Verifikasi tombol `[Save]` tampil dan aktif
49. Total Control `Tari Kusuma {runId}` mencabut hak Update Global Role Manage transaction settings milik `Sari Rahayu {runId}`
50. Klik `[Save]`
51. Klik `[Save]` pada dialog Save Changes
52. Verifikasi toast `You don't have permission to do this.` tampil
53. Verifikasi kontrol field `Max extensions` disabled
54. Verifikasi tombol `[Reset to inherit]` tidak dirender pada field `Max extensions`
55. Verifikasi tombol `[Save]` tampil dan disabled
