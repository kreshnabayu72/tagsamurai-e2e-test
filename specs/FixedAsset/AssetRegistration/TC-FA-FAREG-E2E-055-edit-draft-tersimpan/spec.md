---
id: TC-FA-FAREG-E2E-055-edit-draft-tersimpan
title: "Edit draft: perubahan tersimpan dan Save tanpa perubahan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§9.4.2#r63, §9.7#r2, EB-FB-3@edit-draft, EB-FRM-9, FAREG-LOGIC-03r, T-REG-14]
smoke: [FAREG-LOGIC-03r, T-REG-14]
dependsOn: []
trace:
  §9.4.2#r63: [8, 12, 36]
  §9.7#r2: [16, 18, 28, 58]
  EB-FB-3@edit-draft: [12, 36]
  EB-FRM-9: [25, 26, 27, 41, 42, 46]
  FAREG-LOGIC-03r: [48, 54]
  T-REG-14: [8, 36]
anchor: [3, 11, 40]
coverage:
  web: automated
---

# Edit draft: perubahan tersimpan dan Save tanpa perubahan

## Prerequisites
- Aktor: `Rina W` (nama singkat `Rina W.`; Manage asset & TAG, Group terkelola `Gudang Edit A {runId}` dan `Gudang Edit B {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-055-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Edit A {runId}`. Item 1: `Laptop`, `Dell`, `Latitude 5440`, Quantity `2`. Aset 1: Serial Number `SN-0001`, Tag RFID `Verified`, Condition `Normal`, Alias Name `Laptop Direksi`, Photo `2`. Aset 2: Serial Number `SN-0002`, Tag RFID `Verified`, Condition `Damaged`, Damage note `Layar retak di sudut kiri`, tanpa Photo. Kedua aset berstatus `✓ Ready`, sehingga Progress batch `100%` (2 dari 2 aset Ready).
  - DU-055-2: Draft tersimpan milik `Rina W` untuk Group `Gudang Edit B {runId}`. Item 1: `Laptop`, `Dell`, `Latitude 5440`, Quantity `1`. Aset 1: Condition `Normal`, field opsional (Alias Name, Photo, Damage note) kosong.
  - Register Asset Bulk Limit bernilai `100`.

## Test Steps

### Save draft tanpa perubahan memberi toast netral dan tanpa log baru
1. Ketik Search `Gudang Edit A {runId}`, tekan Enter
2. Klik row action `Registration Log` pada baris
3. Verifikasi timeline memuat node `Draft created by Rina W.`[^drift-1]
4. Catat jumlah node pada timeline
5. Tekan `Esc` untuk menutup dialog Registration Log
6. Klik Group `Gudang Edit A {runId}` pada baris untuk membuka form Edit
7. Klik `[Save draft]` tanpa mengubah apa pun
8. Verifikasi toast `No changes to save.` tampil
9. Klik `[Cancel]` pada form (form belum diubah)
10. Klik row action `Registration Log` pada baris
11. Verifikasi timeline masih memuat node `Draft created by Rina W.`[^drift-1]
12. Verifikasi jumlah node sama dengan jumlah yang dicatat sebelum Save draft dan tidak ada node `Draft edited by Rina W.` baru[^drift-1]
13. Tekan `Esc` untuk menutup dialog Registration Log

### Perubahan nyata tersimpan, field lain tetap, dan bertahan setelah muat ulang
14. Klik Group `Gudang Edit A {runId}` pada baris untuk membuka form Edit
15. Klik tab `Asset`
16. Verifikasi kartu filter `Ready` menampilkan `2` aset dan kartu `Needs data` menampilkan `0`
17. Ganti Condition aset 1 menjadi `Damaged`
18. Verifikasi kartu filter `Ready` menampilkan `1` aset dan kartu `Needs data` menampilkan `1`
19. Klik `[Save draft]`
20. Klik `[Cancel]` pada form (form belum diubah sejak Save draft)
21. Muat ulang halaman
22. Ketik Search `Gudang Edit A {runId}`, tekan Enter
23. Klik Group `Gudang Edit A {runId}` pada baris untuk membuka form Edit
24. Klik tab `Asset`
25. Verifikasi Condition aset 1 `Damaged` setelah muat ulang halaman
26. Verifikasi Condition aset 2 tetap `Damaged`
27. Verifikasi Photo aset 1 tetap `2`
28. Verifikasi kartu filter `Ready` menampilkan `1` aset dan kartu `Needs data` menampilkan `1` setelah muat ulang halaman
29. Klik `[Cancel]` pada form (form belum diubah sejak dibuka)

### Nilai diubah lalu dikembalikan dianggap tanpa perubahan
30. Ketik Search `Gudang Edit B {runId}`, tekan Enter
31. Klik Group `Gudang Edit B {runId}` pada baris untuk membuka form Edit
32. Klik tab `Asset`
33. Ganti Condition aset 1 menjadi `Damaged`
34. Ganti Condition aset 1 kembali menjadi `Normal`, identik dengan nilai tersimpan
35. Klik `[Save draft]`
36. Verifikasi toast `No changes to save.` tampil untuk perubahan yang sudah dikembalikan

### Validasi yang gagal membiarkan form terbuka dan nilai tersimpan tidak berubah
37. Klik tab `General Information`
38. Isi Quantity Item 1 dengan `0`
39. Klik `[Save draft]`
40. Verifikasi pesan error inline `Quantity must be between 1 and 100` tampil pada Quantity Item 1
41. Verifikasi toast `Success, draft has been saved.` tidak tampil
42. Verifikasi form Register Asset tetap terbuka dengan footer `[Save draft]` masih tampil
43. Klik `[Cancel]` pada form
44. Klik `[Leave]` pada dialog Unsaved Changes
45. Klik Group `Gudang Edit B {runId}` pada baris untuk membuka form Edit
46. Verifikasi Quantity Item 1 tetap `1`

### Mengganti Asset Name menghitung ulang Name sementara
47. Klik tab `Asset`
48. Verifikasi Name aset 1 diawali `Laptop`
49. Klik tab `General Information`
50. Pilih Asset Name `Office Desk` pada Item 1
51. Pilih Brand `Kayu Jati` pada Item 1
52. Pilih Model `No Model` pada Item 1
53. Klik tab `Asset`
54. Verifikasi Name aset 1 kini diawali `Office Desk`, bukan `Laptop`
55. Klik `[Cancel]` pada form
56. Klik `[Leave]` pada dialog Unsaved Changes

### Progress batch di sub tab Draft turun sesudah edit disimpan
57. Ganti isi kotak search dengan `Gudang Edit A {runId}`, tekan Enter
58. Verifikasi Progress batch `Gudang Edit A {runId}` `50%` (1 dari 2 aset Ready), turun dari `100%` sebelum Condition aset 1 diubah menjadi `Damaged`

[^drift-1]: Drift PRD vs override. PRD §8.3 node log memakai nama singkat pengguna; `prd-conventions.md` §9.13: `[First Name] [Last Initial]` (contoh tanpa titik: `John L`). Baris O-4: nama singkat mengakhiri inisial dengan titik (`John L.`). Diasersi: override O-4 (SB-6), sehingga nama singkat `Rina W.`.
