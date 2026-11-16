---
id: TC-FA-FATR-E2E-037-gating-ro
title: "Gating Read Only"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§2#r4, §2#r10, §4.3#r5, §4.3#r6, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r8, §4.8#r12, §4.8#p2, §9.2#b1, §9.4.2#r3, §9.4.4#r1, §9.11#r1, EB-AKS-4, §9.2#b157, §9.2#b307, §9.3#b3, §9.11#r3]
smoke: [§9.2#b157, §9.2#b307, §9.3#b3, §9.11#r3]
dependsOn: []
trace:
  §2#r4: [4, 16]
  §2#r10: [2, 10]
  §4.3#r5: [16, 17, 18, 19]
  §4.3#r6: 21
  §4.8#r1: [2, 4]
  §4.8#r2: [8, 10]
  §4.8#r3: 12
  §4.8#r4: 16
  §4.8#r5: [17, 19]
  §4.8#r6: 20
  §4.8#r7: 21
  §4.8#r8: 22
  §4.8#r12: [27, 33, 34, 35, 36]
  §4.8#p2: [24, 29]
  §9.2#b1: [16, 17, 19]
  §9.4.2#r3: [20, 21]
  §9.4.4#r1: 21
  §9.11#r1: [16, 20]
  EB-AKS-4: [37, 39, 41, 42, 44, 50, 55, 56, 58, 64, 65]
  §9.2#b157: [22, 24]
  §9.2#b307: 6
  §9.3#b3: [20, 21, 22]
  §9.11#r3: 14
anchor: [31, 32, 49, 53]
coverage:
  web: automated
---
# Gating Read Only

## Prerequisites
- Aktor: pengguna dengan tingkat akses Read Only `Rudi Hermawan {runId}`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-037-1: User `Rudi Hermawan {runId}`, tingkat akses Read Only, tanpa Global Role Manage transaction settings, tanpa Group Role Manage asset & TAG, bukan Total Control, ada di entitas aktor.
  - DU-037-2: Category leaf `Inventaris Gudang {runId}` di bawah Category induk `Persediaan {runId}`; pada tab Borrow, field `Max duration` bernilai sendiri `11` dan field `Max extensions` Inherit, dibuat oleh aktor lain.
  - DU-037-3: Asset Name `Compressor Atlas {runId}`, aktif.
  - DU-037-4: Group `Gudang Bandung {runId}`.
  - DU-037-5: override pada tab Borrow Category `Inventaris Gudang {runId}` dengan Scope `Asset Name`, Target `Compressor Atlas {runId}`, Overridden `Max duration (10 days)`, dibuat oleh aktor lain.
  - DU-037-6: override pada tab Borrow Category `Inventaris Gudang {runId}` dengan Scope `Group`, Target `Gudang Bandung {runId}`, Overridden `Max duration (30 days)`, dibuat oleh aktor lain; DU-037-5 dibuat lebih dulu daripada DU-037-6.
  - DU-037-7: entri Changelog Category `Inventaris Gudang {runId}`, Field `Borrow (Max duration)`, Action `Edit`, Old Value `Inherit`, New Value `11 days`, dari perubahan DU-037-2.
  - DU-037-8: entri Changelog Category `Inventaris Gudang {runId}`, Field `Borrow (Max extensions)`, Action `Edit`, Old Value `No extension`, New Value `Inherit`.
  - DU-037-9: entri Changelog Category `Inventaris Gudang {runId}`, Field `Borrow (Max extensions)`, Action `Edit`, Old Value `Inherit`, New Value `No extension`; entri ini lebih dulu daripada DU-037-8.
- Kondisi:
  - Akun `Rudi Hermawan {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Read Only melihat halaman, header, dan Changelog
1. Ketik Search Sidebar Category Tree `Inventaris Gudang {runId}`, tekan Enter
2. Verifikasi Sidebar Category Tree menampilkan `All categories` dan Category `Inventaris Gudang {runId}`
3. Klik Category `Inventaris Gudang {runId}`
4. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
5. Klik tab `Assign`
6. Verifikasi tombol `[Export rules]` tampil dan aktif pada tab `Assign`
7. Klik tab `Borrow`
8. Verifikasi tombol `[Export rules]` tampil dan aktif
9. Klik `[Export rules]`
10. Verifikasi berkas aturan terunduh langsung tanpa dialog
11. Klik ikon `Changelog` pada header halaman
12. Verifikasi dialog `Changelog: Transaction Settings` tampil
13. Ketik Search `{runId}` pada dialog Changelog, tekan Enter
14. Verifikasi baris dengan Field `Borrow (Max duration)`, Action `Edit`, Old Value `Inherit`, dan New Value `11 days` tampil
15. Klik `✕` pada dialog Changelog

### Kontrol field, Reset to Default, dan Save tidak bisa dipakai Read Only
16. Verifikasi kontrol field `Max duration` disabled dengan nilai `11`
17. Verifikasi tombol `[Reset to inherit]` tidak dirender pada field `Max duration`
18. Verifikasi field `Max extensions` menampilkan teks `Inherit` beserta sumbernya
19. Verifikasi tombol `[Set own value]` tidak dirender pada field `Max extensions`
20. Verifikasi tombol `[Reset to Default]` tampil dan disabled
21. Verifikasi tombol `[Save]` tampil dan disabled

### Tombol + Override disabled dengan alasan
22. Verifikasi tombol `[+ Override]` tampil dan disabled
23. Arahkan kursor ke tombol `[+ Override]`
24. Verifikasi alasan `You don't have permission to add overrides.` tersampaikan pada tombol `[+ Override]` yang disabled

### Delete override baris disabled dengan alasan dan seleksi bulk tidak tersedia
25. Ketik Search tabel Overrides `{runId}`, tekan Enter
26. Klik menu `⋯` pada baris `Gudang Bandung {runId}`
27. Verifikasi item `Delete` disabled untuk baris override dengan Scope `Group`
28. Arahkan kursor ke item `Delete`
29. Verifikasi alasan `This override is outside your scope.` tersampaikan pada item `Delete` yang disabled
30. Tekan Esc untuk menutup menu baris
31. Verifikasi baris dengan Scope `Group` dan Target `Gudang Bandung {runId}` tampil di tabel Overrides
32. Verifikasi baris dengan Scope `Asset Name` dan Target `Compressor Atlas {runId}` tampil di tabel Overrides
33. Verifikasi checkbox seleksi pada baris `Gudang Bandung {runId}` tidak dirender[^drift-1]
34. Verifikasi checkbox seleksi pada baris `Compressor Atlas {runId}` tidak dirender[^drift-1]
35. Verifikasi checkbox pemilih semua baris pada header tabel Overrides tidak dirender[^drift-1]
36. Verifikasi tombol aksi bulk tidak tampil pada toolbar tabel Overrides[^drift-1]

### Search, Filter, Sort, Pagination, dan Setup Column tabel Overrides aktif untuk Read Only
37. Verifikasi tombol Search tabel Overrides tampil dan aktif
38. Ganti isi kotak search tabel Overrides dengan `{runId}`, tekan Enter
39. Verifikasi baris `Compressor Atlas {runId}` dan `Gudang Bandung {runId}` tampil di tabel Overrides
40. Klik header kolom `Target`
41. Verifikasi baris `Compressor Atlas {runId}` berada di atas baris `Gudang Bandung {runId}`
42. Verifikasi pagination tabel Overrides menampilkan `Showing 1 to 2 of 2`
43. Klik header kolom Actions pada tabel Overrides
44. Verifikasi tombol `Setup Columns` tampil dan aktif
45. Tekan Esc untuk menutup menu Column Visibility
46. Klik tombol filter tabel Overrides
47. Pilih filter `Scope` dengan nilai `Group`
48. Klik `[Apply]`
49. Verifikasi baris `Gudang Bandung {runId}` tampil di tabel Overrides
50. Verifikasi baris `Compressor Atlas {runId}` tidak tampil di tabel Overrides

### Search, Filter, Sort, Pagination, dan Setup Column tabel Changelog aktif untuk Read Only
51. Klik ikon `Changelog` pada header halaman
52. Ketik Search `{runId}` pada dialog Changelog, tekan Enter
53. Verifikasi baris Field `Borrow (Max duration)` dan baris Field `Borrow (Max extensions)` tampil di tabel Changelog
54. Klik header kolom `Field`
55. Verifikasi baris Field `Borrow (Max duration)` berada di atas baris Field `Borrow (Max extensions)`
56. Verifikasi pagination tabel Changelog menampilkan `Showing 1 to 3 of 3`
57. Klik header kolom Actions pada tabel Changelog
58. Verifikasi tombol `Setup Columns` tampil dan aktif
59. Tekan Esc untuk menutup menu Column Visibility
60. Klik tombol filter di toolbar dialog Changelog
61. Klik field `Field` pada panel filter
62. Pilih opsi `Borrow (Max extensions)`
63. Klik `[Apply]`
64. Verifikasi baris Field `Borrow (Max extensions)` tampil di tabel Changelog
65. Verifikasi baris Field `Borrow (Max duration)` tidak tampil di tabel Changelog
66. Klik `✕` pada dialog Changelog

[^drift-1]: Drift PRD vs foundation. PRD §4.8 (sel Delete baris dan bulk) dan §4.1 DO-15: aktor tanpa hak tulis dapat mencentang baris lalu aksi bulk `Delete` disabled dengan tooltip tersendiri. foundation `functions/entity-isolation.md` §18.4 Aturan kolom 3: kolom checkbox seleksi Hidden dan bar aksi bulk Hidden total untuk aktor tanpa hak tulis sama sekali, sehingga baris tidak bisa dicentang. Diasersi: foundation, karena checkbox seleksi dan bar aksi bulk tabel adalah pola bersama (SB-4).
