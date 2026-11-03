---
id: TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1
title: "Assign User ke Group Role di Detail Role (1/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-247
  - TC-FA-RP-248
  - TC-FA-RP-249
  - TC-FA-RP-250
  - TC-FA-RP-251
  - TC-FA-RP-252
coverage:
  web: automated
---

# Assign User ke Group Role di Detail Role (1/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, Dimas Pranata, ...), #18 (pohon group), #1 (Admin Utama Default User), #3 (Rina Wulandari Total Control kedua). Pada TC-FA-RP-252 Ahmad Fauzi memegang `Manage files` di `Data Center` dan Budi Santoso memegang `Manage files` di `Helpdesk`, keduanya di-seed lewat seeding API.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): daftar penugasan Group Role Budi Santoso dicatat sebagai baseline untuk TC-FA-RP-250.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-247: Assign satu user ke Group Role pada node terpilih

1. Klik Tab `System`
2. Buka Detail Role `Manage files`
3. Klik node `Data Center` di Sidebar Group Tree
4. Klik `[+ Assign]`
5. Verifikasi header popup `Assign User — Manage files (Data Center)`
6. Centang Budi Santoso, klik `[Assign]`
7. Verifikasi muncul toast sukses: `Success, Manage files has been assigned.`
8. Verifikasi baris Budi Santoso dengan badge Group `Data Center` tampil
9. Verifikasi Read pada baris Budi Santoso tercentang dan terkunci
10. Verifikasi Delete pada baris Budi Santoso tidak aktif
11. Verifikasi Create dan Update pada baris Budi Santoso menampilkan `—`

### TC-FA-RP-248: Group popup berbeda dari node Sidebar: toast tetap tampil dan baris baru tersaring dari tampilan

12. Hapus penugasan `Manage files` Budi Santoso di `Data Center` lewat seeding API
13. Klik node `Helpdesk` lalu klik node `Data Center` di Sidebar Group Tree
14. Klik `[+ Assign]`, ubah field Group menjadi `Helpdesk`, centang Budi Santoso, klik `[Assign]`
15. Verifikasi muncul toast sukses: `Success, Manage files has been assigned.`
16. Verifikasi baris Budi Santoso tidak tampil pada node `Data Center`
17. Klik node `Helpdesk`
18. Verifikasi baris Budi Santoso tampil dengan badge Group `Helpdesk`

### TC-FA-RP-249: Assign Group Role: preview scope tampil sebelum `[Assign]` dan menyebut node beserta descendant

19. Klik segmen `System` pada breadcrumb
20. Buka Detail Role `Manage group`
21. Klik `[+ Assign]`
22. Pilih group `IT Infrastructure`
23. Verifikasi preview scope menampilkan `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
24. Tutup popup lewat `✕`

### TC-FA-RP-250: Assign Group Role dari All Groups tanpa memilih group: error field-level

25. Klik segmen `System` pada breadcrumb
26. Catat daftar penugasan Group Role Budi Santoso lewat fixture BE sebagai baseline
27. Buka Detail Role `Manage files` dengan Sidebar pada `All Groups`
28. Klik `[+ Assign]`, centang Budi Santoso, klik `[Assign]`
29. Verifikasi error field-level pada field Group: `You must select a group`
30. Verifikasi popup tetap terbuka
31. Verifikasi daftar penugasan Group Role Budi Santoso (fixture BE) sama dengan baseline: tidak ada penugasan tersimpan

### TC-FA-RP-251: Assign tiga user ke Group Role pada satu group menghasilkan satu toast

32. Tutup popup lewat `✕`
33. Klik segmen `System` pada breadcrumb
34. Tunggu toast lama hilang otomatis
35. Buka Detail Role `Manage group` dan pilih node `Helpdesk`
36. Klik `[+ Assign]`, centang Ahmad Fauzi, Budi Santoso, Dimas Pranata, klik `[Assign]`
37. Verifikasi muncul satu toast sukses: `Success, Manage group has been assigned.`
38. Verifikasi ketiga baris tampil dengan badge Group `Helpdesk`

### TC-FA-RP-252: Popup Assign Group Role mengecualikan aktor, penugasan sama pada node yang sama, Default User, dan Total Control

39. Tetapkan Ahmad Fauzi memegang `Manage files` di `Data Center` dan Budi Santoso memegang `Manage files` hanya di `Helpdesk` lewat seeding API
40. Klik segmen `System` pada breadcrumb
41. Buka Detail Role `Manage files` dan klik `[+ Assign]`
42. Pilih group `Data Center`
43. Ketik Search `Siti Rahmawati`, tekan Enter
44. Verifikasi Siti Rahmawati (aktor) tidak ada di daftar (empty state hasil Search)
45. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
46. Verifikasi Ahmad Fauzi (penugasan sama pada node yang sama) tidak ada di daftar (empty state hasil Search)
47. Ganti isi kotak search dengan `Admin Utama`, tekan Enter
48. Verifikasi Admin Utama (Default User) tidak ada di daftar (empty state hasil Search)
49. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
50. Verifikasi Rina Wulandari (Total Control) tidak ada di daftar (empty state hasil Search)
51. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
52. Verifikasi Budi Santoso (penugasan di node lain) ada di daftar
53. Ganti isi kotak search dengan `Dimas Pranata`, tekan Enter
54. Verifikasi Dimas Pranata ada di daftar

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 54 langkah.
- Langkah penghubung (S-03): langkah 1, 13, 19, 24–26, 32–34, 40. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 12, 39; tidak ada `Verifikasi`.
- Penyimpangan kecil TC-FA-RP-248: sebelum langkah Assign, Sidebar diatur ke node `Data Center` lewat klik node (penghubung) agar kondisi "node Sidebar `Data Center`" pada langkah TC terpenuhi. Asersi absence baris Budi Santoso pada node `Data Center` memakai toast sukses sebagai anchor (butir 8b.2).
- Absence di picker memakai empty state hasil Search sebagai anchor positif (butir 8b.2). Penghapusan penugasan lewat seeding API pada langkah 12 dan penataan ulang pada langkah 39 memastikan state Precondition tiap TC (S-04, S-09).
- Temuan untuk QA:
  - TC-FA-RP-250 langkah 2 mencentang Budi Santoso dengan Sidebar `All Groups` (precondition a), sedangkan TC-FA-RP-1087 menyatakan Table User Picker kosong dan Disabled sampai Group dipilih pada kondisi yang sama; spec mengikuti teks TC-FA-RP-250.
  - TC-FA-RP-250 Expected b ("tidak ada penugasan tersimpan") tidak punya baseline; spec memakai baseline lewat fixture BE (S-12).
  - TC-FA-RP-247 menyatakan Create/Update `—` dan Delete tidak aktif pada `Manage files`; konsisten dengan kolom berlaku Group Role `Manage files` (RD).
- Ukuran spec (54 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
