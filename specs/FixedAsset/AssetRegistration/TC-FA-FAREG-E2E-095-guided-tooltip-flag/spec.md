---
id: TC-FA-FAREG-E2E-095-guided-tooltip-flag
title: "Guided Tooltip: flag bertahan antar sesi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "EB-TBL-10": [3, 9, 13, 17, 20, 28, 31, 37, 42, 48, 52, 63]
anchor: [8, 12, 16, 27, 36, 40, 47, 62]
coverage:
  web: automated
---

# Guided Tooltip: flag bertahan antar sesi

## Prerequisites
- Aktor: Tia R, lalu Uli S, lalu Vera T, lalu Wulan D, lalu Zaki F, lalu Bimo A, lalu Yoga Z (masing-masing Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-095-1: Tia R (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` belum disetel.
  - DU-095-2: Uli S (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` sudah disetel.
  - DU-095-3: Vera T (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` sudah disetel dari perangkat lain sebelum sesi ini.
  - DU-095-4: Wulan D (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` belum disetel.
  - DU-095-5: Zaki F (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` belum disetel.
  - DU-095-6: Bimo A (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` sudah disetel.
  - DU-095-7: Yoga Z (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` sudah disetel dan flag `guided_tooltip_seen_fa-registration-form` belum disetel.

## Test Steps

### Kunjungan pertama menampilkan tur dan Skip menyetel flag
1. Masuk sebagai Tia R
2. Klik tab `Registration`
3. Verifikasi tur Guided Tooltip `fa-registration` tampil otomatis dengan Title `See what's missing` bagi Tia R
4. Klik `[Skip]`
5. Keluar dari aplikasi
6. Masuk kembali sebagai Tia R
7. Klik tab `Registration`
8. Verifikasi sub tab `Draft` tampil bagi Tia R sesudah masuk kembali
9. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Tia R sesudah masuk kembali

### Flag yang sudah disetel membuat tur tidak tampil
10. Masuk sebagai Uli S
11. Klik tab `Registration`
12. Verifikasi sub tab `Draft` tampil bagi Uli S
13. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Uli S

### Flag yang disetel dari perangkat lain berlaku di perangkat ini
14. Masuk sebagai Vera T dari perangkat yang belum pernah dipakai Vera T
15. Klik tab `Registration`
16. Verifikasi sub tab `Draft` tampil bagi Vera T
17. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Vera T

### Done menyetel flag tur halaman daftar
18. Masuk sebagai Wulan D
19. Klik tab `Registration`
20. Verifikasi tur Guided Tooltip `fa-registration` tampil otomatis dengan Title `See what's missing` bagi Wulan D
21. Klik `[Next]`
22. Klik `[Next]`
23. Klik `[Done]`
24. Keluar dari aplikasi
25. Masuk kembali sebagai Wulan D
26. Klik tab `Registration`
27. Verifikasi sub tab `Draft` tampil bagi Wulan D sesudah masuk kembali
28. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Wulan D sesudah masuk kembali

### Tur yang ditutup tanpa selesai tidak menyetel flag
29. Masuk sebagai Zaki F
30. Klik tab `Registration`
31. Verifikasi tur Guided Tooltip `fa-registration` tampil otomatis dengan Title `See what's missing` bagi Zaki F
32. Ubah ukuran jendela browser hingga tur ditutup tanpa diselesaikan
33. Keluar dari aplikasi
34. Masuk kembali sebagai Zaki F
35. Klik tab `Registration`
36. Verifikasi sub tab `Draft` tampil bagi Zaki F sesudah masuk kembali
37. Verifikasi tur Guided Tooltip `fa-registration` tampil otomatis lagi dengan Title `See what's missing` bagi Zaki F

### Replay lewat tombol bantuan tidak mereset flag
38. Masuk sebagai Bimo A
39. Klik tab `Registration`
40. Verifikasi sub tab `Draft` tampil bagi Bimo A
41. Klik tombol `[?]` di sebelah kanan Breadcrumb
42. Verifikasi tur Guided Tooltip `fa-registration` tampil dari Step 1 dengan Title `See what's missing` bagi Bimo A
43. Ubah ukuran jendela browser hingga tur ditutup tanpa diselesaikan
44. Keluar dari aplikasi
45. Masuk kembali sebagai Bimo A
46. Klik tab `Registration`
47. Verifikasi sub tab `Draft` tampil bagi Bimo A sesudah masuk kembali
48. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Bimo A sesudah masuk kembali

### Done menyetel flag tur form Register Asset
49. Masuk sebagai Yoga Z
50. Klik tab `Registration`
51. Klik `[+ Register Asset]`
52. Verifikasi tur Guided Tooltip `fa-registration-form` tampil otomatis dengan Title `Choose a group` bagi Yoga Z
53. Klik `[Next]`
54. Klik `[Next]`
55. Klik `[Next]`
56. Klik `[Done]`
57. Klik `[Cancel]` pada footer form yang belum diubah, tanpa dialog Unsaved Changes
58. Keluar dari aplikasi
59. Masuk kembali sebagai Yoga Z
60. Klik tab `Registration`
61. Klik `[+ Register Asset]`
62. Verifikasi form `Register Asset` terbuka bagi Yoga Z sesudah masuk kembali
63. Verifikasi tur Guided Tooltip `fa-registration-form` tidak tampil bagi Yoga Z sesudah masuk kembali
