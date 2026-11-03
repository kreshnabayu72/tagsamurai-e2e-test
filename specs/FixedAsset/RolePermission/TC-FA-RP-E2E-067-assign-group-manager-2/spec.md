---
id: TC-FA-RP-E2E-067-assign-group-manager-2
title: "Assign Group Manager (2/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-223
  - TC-FA-RP-224
  - TC-FA-RP-225
  - TC-FA-RP-226
  - TC-FA-RP-227
coverage:
  web: automated
---

# Assign Group Manager (2/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, Dimas Pranata, Citra Lestari, ...), #16 (Siti Rahayu Inactive, Eka Saputra Pending Activation, Fitri Handayani Pending Email Confirmation), #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #12 (Maya Anggraeni Read Only), #3 (Rina Wulandari Total Control kedua), #1 (Admin Utama Default User), #18 (pohon group).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-223: Preview scope menampilkan node terpilih beserta seluruh descendant pada pohon empat level

1. Klik Tab `Group Manager`
2. Klik `[+ Assign]` di Tab Group Manager
3. Pilih group `IT Infrastructure` pada field Group
4. Amati preview scope
5. Verifikasi preview untuk `IT Infrastructure`: `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
6. Ubah group menjadi `Rack A1`
7. Verifikasi preview untuk `Rack A1`: hanya `Rack A1` (tanpa descendant)
8. Tutup popup lewat `✕`

### TC-FA-RP-224: Popup Assign Group Manager mengecualikan aktor, Default User, Total Control, Read Only, dan user yang sudah GM di group terpilih

9. Klik `[+ Assign]` di Tab Group Manager
10. Pilih group `Data Center`
11. Ketik Search `Siti Rahmawati`, tekan Enter
12. Verifikasi Siti Rahmawati (aktor) tidak ada di daftar (empty state hasil Search)
13. Ganti isi kotak search dengan `Admin Utama`, tekan Enter
14. Verifikasi Admin Utama (Default User) tidak ada di daftar (empty state hasil Search)
15. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
16. Verifikasi Rina Wulandari (Total Control) tidak ada di daftar (empty state hasil Search)
17. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
18. Verifikasi Maya Anggraeni (Read Only) tidak ada di daftar (empty state hasil Search)
19. Ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
20. Verifikasi Kevin Susanto (sudah GM di `Data Center`) tidak ada di daftar (empty state hasil Search)
21. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
22. Verifikasi Ahmad Fauzi (Standard) ada di daftar
23. Tutup popup lewat `✕`

### TC-FA-RP-225: Popup Assign Group Manager: Status dan Activation Status apa pun eligible

24. Klik `[+ Assign]` di Tab Group Manager
25. Pilih group `Helpdesk`
26. Verifikasi ketiga user Siti Rahayu (Inactive), Eka Saputra (Pending Activation), dan Fitri Handayani (Pending Email Confirmation) ada di daftar picker
27. Centang Siti Rahayu, Eka Saputra, dan Fitri Handayani lalu klik `[Assign]`
28. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
29. Klik node `Helpdesk` di Sidebar Group Tree
30. Verifikasi baris Siti Rahayu, Eka Saputra, dan Fitri Handayani tampil di Tab Group Manager dengan badge Group `Helpdesk`

### TC-FA-RP-226: Multi-manajer pada group yang sama bersifat aditif

31. Klik `[+ Assign]` di Tab Group Manager
32. Pilih group `Data Center`
33. Centang Ahmad Fauzi lalu klik `[Assign]`
34. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
35. Klik node `Data Center` di Sidebar Group Tree
36. Verifikasi Tab Group Manager memuat baris Kevin Susanto dan Ahmad Fauzi pada `Data Center`

### TC-FA-RP-227: Group dengan ancestor yang sudah punya Group Manager tetap dapat dipilih

37. Klik `All Groups`
38. Klik `[+ Assign]` di Tab Group Manager
39. Buka field Group dan amati node `Data Center` dan `Rack A1`
40. Verifikasi tidak ada node yang Disabled walau ancestor-nya punya Group Manager
41. Pilih `Rack A1`, centang Budi Santoso, klik `[Assign]`
42. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
43. Verifikasi baris Budi Santoso di `Rack A1` dan baris Fajar Nugroho di `IT Infrastructure` tampil bersamaan di Tab Group Manager (penugasan langsung dan wewenang warisan Fajar Nugroho berlaku berdampingan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 43 langkah.
- Langkah penghubung (S-03): langkah 1, 8, 23, 29, 35, 37. Akun aktor pertama sudah login di hook `before` (S-07).
- Pembukaan popup memakai node Sidebar yang sedang aktif; field Group diisi langkah TC ("pilih group"). Langkah klik node Sidebar sesudah Assign (penghubung) membatasi tabel pada group yang diasersi sehingga baris yang baru ditambahkan terlihat tanpa pagination.
- Absence pada TC-FA-RP-224 memakai empty state hasil Search sebagai anchor positif (butir 8b.2).
- Post Condition TC-FA-RP-226 (union wewenang Group Manager pada `Data Center` dan `Rack A1`) tidak punya langkah observasi dan tidak diasersi (S-01, S-15).
- Temuan untuk QA:
  - TC-FA-RP-225 Expected a ("ketiga user ada di daftar") tidak memberi langkah Search; spec memverifikasi ketiganya pada daftar picker sebelum mencentang.
  - TC-FA-RP-224: Kevin Susanto pada group `Data Center` dikecualikan karena sudah GM di group itu (Pre-setup #43).
- Ukuran spec (43 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
