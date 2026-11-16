---
id: TC-FA-FATR-BE-115-aturan-asset-name-dep-asset-name
title: "Override saat Asset Name berubah"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§9.2#b121", "§9.2#b123", "§9.2#b132", "§9.2#b133", "§9.2#b134", "§9.2#b135", "§9.2#b136", "§9.2#b137", "§9.2#b138", "§9.2#b146", "§9.2#b148", "§9.4.2#r34", "§9.4.3#b11"]
smoke: []
dependsOn:
  - "Settings Asset Name: hapus, nonaktifkan, dan pindah Category"
trace:
  "§9.2#b121": [2, 6]
  "§9.2#b146": [2, 6]
  "§9.2#b138": [2, 6, 12]
  "§9.4.2#r34": [2, 6, 8, 12]
  "§9.2#b123": [4, 8]
  "§9.2#b148": 8
  "§9.4.3#b11": [8, 16]
  "§9.2#b136": [10, 16]
  "§9.2#b137": 14
  "§9.2#b135": 14
  "§9.2#b132": [18, 24]
  "§9.2#b134": 20
  "§9.2#b133": 22
---

# Override saat Asset Name berubah

## Prerequisites
- Aktor: Total Control.
- Data:
  - DU-115-1: Category `Alat Ukur {runId} > Jangka Sorong {runId}`.
  - DU-115-2: Category `Alat Ukur {runId} > Mikrometer {runId}`.
  - DU-115-3: Asset Name `Jangka Sorong Digital {runId}` di Category `Alat Ukur {runId} > Jangka Sorong {runId}`.
  - DU-115-4: aset `Jangka Sorong Digital Unit 1 {runId}` ber-Asset Name `Jangka Sorong Digital {runId}`, di Category `Alat Ukur {runId} > Jangka Sorong {runId}`.
  - DU-115-5: override transaksi pinjam, target Asset Name `Jangka Sorong Digital {runId}`, Category `Alat Ukur {runId} > Jangka Sorong {runId}`, Max duration `5`.
  - DU-115-6: override transaksi pinjam, target Asset Name `Jangka Sorong Digital {runId}`, Category All categories, Max duration `8`.
  - DU-115-7: Asset Name `Jangka Sorong Analog {runId}` di Category `Alat Ukur {runId} > Jangka Sorong {runId}`.
  - DU-115-8: aset `Jangka Sorong Analog Unit 1 {runId}` ber-Asset Name `Jangka Sorong Analog {runId}`, di Category `Alat Ukur {runId} > Jangka Sorong {runId}`.
  - DU-115-9: override transaksi pinjam, target Asset `Jangka Sorong Analog Unit 1 {runId}`, Category `Alat Ukur {runId} > Jangka Sorong {runId}`, Max duration `5`.
  - DU-115-10: override transaksi pinjam, target Asset `Jangka Sorong Analog Unit 1 {runId}`, Category All categories, Max duration `8`.
  - DU-115-11: Asset Name `Jangka Sorong Lama {runId}` di Category `Alat Ukur {runId} > Jangka Sorong {runId}`.
  - DU-115-12: override transaksi pinjam, target Asset Name `Jangka Sorong Lama {runId}`, Category `Alat Ukur {runId} > Jangka Sorong {runId}`, Max duration `5`.
  - DU-115-13: Asset Name `Waterpass {runId}` di Category `Alat Ukur {runId} > Jangka Sorong {runId}`, aktif.
  - DU-115-14: aset `Waterpass Unit 1 {runId}` ber-Asset Name `Waterpass {runId}`, di Category `Alat Ukur {runId} > Jangka Sorong {runId}`.
  - DU-115-15: override transaksi pinjam, target Asset Name `Waterpass {runId}`, Category `Alat Ukur {runId} > Jangka Sorong {runId}`, Max duration `5`.
  - DU-115-16: pengajuan pinjam selama `7` Days.
  - DU-115-17: pengajuan pinjam selama `10` Days.
- Kondisi:
  - Max duration bernilai `14` di Company default untuk transaksi pinjam.

## Test Steps

### Asset Name yang dihapus: override tetap tersimpan
1. Total Control menghapus Asset Name `Jangka Sorong Lama {runId}`
2. Verifikasi override target aset Name `Jangka Sorong Lama {runId}` tetap tersimpan dan tampil di tabel Overrides sesudah Asset Name dihapus

### Asset Name yang dinonaktifkan: override tidak berlaku
3. Total Control mengajukan peminjaman aset `Waterpass Unit 1 {runId}` selama `10` Days saat Asset Name `Waterpass {runId}` masih aktif
4. Verifikasi pengajuan selama `10` Days ditolak karena override Max duration `5` untuk Asset Name `Waterpass {runId}` berlaku selama Asset Name aktif
5. Total Control menonaktifkan Asset Name `Waterpass {runId}`
6. Verifikasi override target aset Name `Waterpass {runId}` tetap tersimpan dan tampil di tabel Overrides sesudah Asset Name dinonaktifkan
7. Total Control mengajukan peminjaman aset `Waterpass Unit 1 {runId}` selama `10` Days sesudah Asset Name `Waterpass {runId}` dinonaktifkan
8. Verifikasi pengajuan selama `10` Days diterima karena override pada Asset Name yang dinonaktifkan tidak berlaku, dan Max duration efektif adalah `14` dari Company default

### Asset Name pindah Category: override Asset Name ber-Category leaf tidak berlaku, All categories tetap berlaku
9. Total Control mengajukan peminjaman aset `Jangka Sorong Digital Unit 1 {runId}` selama `7` Days saat Asset Name `Jangka Sorong Digital {runId}` ada di Category `Alat Ukur {runId} > Jangka Sorong {runId}`
10. Verifikasi pengajuan selama `7` Days ditolak karena override Asset Name ber-Category leaf Max duration `5` menang atas override All categories Max duration `8` selama Asset Name ada di Category `Alat Ukur {runId} > Jangka Sorong {runId}`
11. Total Control memindahkan Asset Name `Jangka Sorong Digital {runId}` ke Category `Alat Ukur {runId} > Mikrometer {runId}`
12. Verifikasi kedua override target aset Name `Jangka Sorong Digital {runId}`, yaitu Category `Alat Ukur {runId} > Jangka Sorong {runId}` dan All categories, tetap tersimpan dan tampil di tabel Overrides sesudah Asset Name pindah Category
13. Total Control mengajukan peminjaman aset `Jangka Sorong Digital Unit 1 {runId}` selama `10` Days sesudah Asset Name pindah ke Category `Alat Ukur {runId} > Mikrometer {runId}`
14. Verifikasi pengajuan selama `10` Days ditolak karena override All categories Max duration `8` tetap berlaku sesudah Asset Name pindah Category, karena override Asset Name terikat pada Asset Name
15. Total Control mengajukan peminjaman aset `Jangka Sorong Digital Unit 1 {runId}` selama `7` Days sesudah Asset Name pindah ke Category `Alat Ukur {runId} > Mikrometer {runId}`
16. Verifikasi pengajuan selama `7` Days diterima karena override Asset Name ber-Category leaf Max duration `5` untuk Category `Alat Ukur {runId} > Jangka Sorong {runId}` tidak berlaku bagi Asset Name yang berpindah ke Category lain

### Asset Name pindah Category: override aset ber-Category leaf tidak berlaku, All categories tetap berlaku
17. Total Control mengajukan peminjaman aset `Jangka Sorong Analog Unit 1 {runId}` selama `7` Days saat Asset Name `Jangka Sorong Analog {runId}` ada di Category `Alat Ukur {runId} > Jangka Sorong {runId}`
18. Verifikasi pengajuan selama `7` Days ditolak karena override aset ber-Category leaf Max duration `5` untuk aset `Jangka Sorong Analog Unit 1 {runId}` berlaku selama Category aset `Alat Ukur {runId} > Jangka Sorong {runId}`
19. Total Control memindahkan Asset Name `Jangka Sorong Analog {runId}` ke Category `Alat Ukur {runId} > Mikrometer {runId}`
20. Verifikasi kedua override target aset `Jangka Sorong Analog Unit 1 {runId}`, yaitu Category `Alat Ukur {runId} > Jangka Sorong {runId}` dan All categories, tetap tersimpan dan tampil di tabel Overrides sesudah Category aset berubah
21. Total Control mengajukan peminjaman aset `Jangka Sorong Analog Unit 1 {runId}` selama `10` Days sesudah Category aset berubah ke `Alat Ukur {runId} > Mikrometer {runId}`
22. Verifikasi pengajuan selama `10` Days ditolak karena override aset All categories Max duration `8` tetap berlaku sesudah Category aset berubah
23. Total Control mengajukan peminjaman aset `Jangka Sorong Analog Unit 1 {runId}` selama `7` Days sesudah Category aset berubah ke `Alat Ukur {runId} > Mikrometer {runId}`
24. Verifikasi pengajuan selama `7` Days diterima karena override aset ber-Category leaf Max duration `5` untuk Category `Alat Ukur {runId} > Jangka Sorong {runId}` tidak berlaku bila Category aset berubah
