---
id: TC-FA-MYASSET-E2E-035-tab-borrowed-setup-column-tersimpan-dep-borrow
title: "Konfigurasi kolom tab Borrowed tersimpan di akun pengguna"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["EB-KOL-2@tabel-borrowed"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "EB-KOL-2@tabel-borrowed": [1, 9, 17, 19, 25, 27, 28, 29, 30, 35, 37, 38, 39, 45]
anchor: []
coverage:
  web: automated
---

# Konfigurasi kolom tab Borrowed tersimpan di akun pengguna

## Prerequisites
- Aktor: Borrower `Gita Wulandari {runId}`, pengguna karyawan ber-akun login tanpa role admin. Pengguna lain `Hendro Saputra {runId}`, juga Borrower tanpa role admin, yang belum pernah mengubah konfigurasi kolom tab Borrowed.
- Layar awal: halaman My Asset, tab `Borrowed`.
- Data:
  - DU-035-1: User `Gita Wulandari {runId}`, tanpa role admin, cakupan Group `Head Office`. Konfigurasi kolom tab Borrowed belum pernah diubah.
  - DU-035-2: User `Hendro Saputra {runId}`, tanpa role admin, cakupan Group `Head Office`. Konfigurasi kolom tab Borrowed belum pernah diubah.
  - DU-035-3: pinjaman Admin atas nama `Gita Wulandari {runId}`, aset `Printer Canon G3010 {runId}`, Brand `Canon`, Model/Type `G3010`, Group `Head Office`, Status `Borrowed`, Duration `2 days`, Handed Over At `T0`, Due Date `T0 + 2 hari`, Purpose `Presentasi klien`.
  - DU-035-4: pinjaman Admin atas nama `Gita Wulandari {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Borrowed`, Duration `5 days`, Handed Over At `T0`, Due Date `T0 + 5 hari`, Purpose `Pelatihan karyawan`.
  - DU-035-5: pinjaman Admin atas nama `Hendro Saputra {runId}`, aset `Kamera Canon EOS 90D {runId}`, Brand `Canon`, Model/Type `EOS 90D`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`, Due Date `T0 + 3 hari`, Purpose `Dokumentasi acara`.
  - DU-035-6: konfigurasi kolom tab Borrowed `Gita Wulandari {runId}` yang disimpan pada langkah spec: kolom `Brand` disembunyikan, kolom `Purpose` ditambahkan, kolom `Duration` menjadi kolom pertama, dan kolom `Duration` di-pin.
  - DU-035-7: nilai Filter `Gita Wulandari {runId}` pada field `Brand`: `Canon`.
  - DU-035-8: nilai rows per page `Gita Wulandari {runId}`: `25`, berbeda dari nilai bawaan `10`.
- Kondisi:
  - Akun `Gita Wulandari {runId}` dan `Hendro Saputra {runId}` aktif, dan kredensialnya disediakan fase 2.
  - Tab Borrowed `Gita Wulandari {runId}` berisi 2 baris aset, DU-035-3 dan DU-035-4. Tab Borrowed `Hendro Saputra {runId}` berisi 1 baris aset, DU-035-5.
  - Kolom bawaan tab Borrowed: `Brand` tampil, dan `Purpose` tidak tampil.

## Test Steps

### Konfigurasi kolom bawaan sebelum diubah
1. Verifikasi kolom `Brand` tampil dan kolom `Purpose` tidak tampil di tabel Borrowed

### Mengubah konfigurasi kolom lewat Setup Column
2. Klik header kolom Actions `⋯` untuk membuka Column Visibility
3. Klik `Setup Column...`
4. Hapus centang kolom `Brand`
5. Centang kolom `Purpose`
6. Seret kolom `Duration` ke posisi paling atas daftar kolom
7. Klik ikon pin pada kolom `Duration`
8. Klik `[Save]`
9. Verifikasi kolom `Duration` tampil sebagai kolom data pertama, kolom `Purpose` tampil, dan kolom `Brand` tidak tampil

### Konfigurasi bertahan sesudah muat ulang dan Search, Sort, Filter, serta paginasi tidak ikut tersimpan
10. Ketik Search `Printer Canon G3010 {runId}`, tekan Enter
11. Klik header kolom Name
12. Klik ikon `Filter` pada toolbar
13. Pilih `Canon` pada field Filter `Brand`
14. Klik `[Apply]`
15. Pilih `25` pada dropdown `Rows per page`
16. Muat ulang halaman
17. Verifikasi kolom `Duration` tampil sebagai kolom data pertama, kolom `Purpose` tampil, dan kolom `Brand` tidak tampil sesudah muat ulang
18. Gulir tabel ke kanan sampai kolom paling kanan terlihat
19. Verifikasi kolom `Duration` tetap tampil di tepi kiri tabel sesudah muat ulang karena ter-pin

### Konfigurasi bertahan sesudah keluar dan masuk lagi
20. Keluar dari akun
21. Masuk sebagai `Gita Wulandari {runId}`
22. Klik avatar di navbar untuk membuka menu profil
23. Klik `My Asset`
24. Klik tab `Borrowed`
25. Verifikasi kolom `Duration` tampil sebagai kolom data pertama, kolom `Purpose` tampil, dan kolom `Brand` tidak tampil sesudah masuk lagi
26. Gulir tabel ke kanan sampai kolom paling kanan terlihat
27. Verifikasi kolom `Duration` tetap tampil di tepi kiri tabel sesudah masuk lagi karena ter-pin
28. Verifikasi tabel memuat baris `Printer Canon G3010 {runId}` lalu `Laptop Dell Latitude 5420 {runId}` menurut urutan default Due Date terdekat tanpa Search yang tersisa
29. Verifikasi ikon `Filter` tidak menampilkan badge titik karena tidak ada Filter ter-Apply yang tersisa
30. Verifikasi dropdown `Rows per page` bernilai `10` sebagai nilai bawaan

### Konfigurasi ikut ke browser lain untuk pengguna yang sama
31. Di browser lain, masuk sebagai `Gita Wulandari {runId}`
32. Klik avatar di navbar untuk membuka menu profil
33. Klik `My Asset`
34. Klik tab `Borrowed`
35. Verifikasi kolom `Duration` tampil sebagai kolom data pertama, kolom `Purpose` tampil, dan kolom `Brand` tidak tampil di browser lain
36. Gulir tabel ke kanan sampai kolom paling kanan terlihat
37. Verifikasi kolom `Duration` tetap tampil di tepi kiri tabel di browser lain karena ter-pin
38. Verifikasi ikon `Filter` tidak menampilkan badge titik di browser lain
39. Verifikasi dropdown `Rows per page` bernilai `10` di browser lain

### Pengguna lain tetap melihat kolom bawaan
40. Keluar dari akun
41. Masuk sebagai `Hendro Saputra {runId}`
42. Klik avatar di navbar untuk membuka menu profil
43. Klik `My Asset`
44. Klik tab `Borrowed`
45. Verifikasi kolom `Brand` tampil, kolom `Purpose` tidak tampil, dan kolom `Duration` bukan kolom data pertama
