---
id: TC-FA-RP-E2E-066-assign-group-manager-1
title: "Assign Group Manager (1/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-219
  - TC-FA-RP-220
  - TC-FA-RP-221
  - TC-FA-RP-222
coverage:
  web: automated
---

# Assign Group Manager (1/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Dimas Pranata, Budi Santoso, dan kolam pengguna Standard) dan #18 (pohon group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`); tanpa penugasan Group Manager untuk Dimas Pranata dan Budi Santoso pada awal tiap blok.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): daftar penugasan Group Manager dicatat sebagai baseline sebelum TC-FA-RP-221.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-219: Assign Group Manager ke satu user pada satu group lewat popup

1. Klik Tab `Group Manager`
2. Klik `[+ Assign]` di Tab Group Manager
3. Pilih group `Data Center` pada field Group
4. Centang Dimas Pranata
5. Amati preview scope
6. Verifikasi preview scope menampilkan `Data Center` dan `Rack A1`
7. Klik `[Assign]`
8. Verifikasi popup tertutup
9. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
10. Klik node `Data Center` di Sidebar Group Tree
11. Verifikasi baris Dimas Pranata dengan badge Group `Data Center` tampil di Tab Group Manager
12. Verifikasi kolom Modified By baris Dimas Pranata berisi `Siti R`
13. Pulihkan Dimas Pranata tanpa penugasan Group Manager lewat seeding API

### TC-FA-RP-220: Field Group popup Assign Group Manager: default dari node Sidebar atau kosong bila All Groups

14. Klik node `IT Infrastructure` di Sidebar Group Tree
15. Klik `[+ Assign]` dan amati field Group
16. Verifikasi field Group terisi `IT Infrastructure`
17. Ubah field Group menjadi `Data Center`
18. Verifikasi field Group dapat diubah manual tanpa menutup popup
19. Ubah field Group kembali menjadi `IT Infrastructure`
20. Tutup popup lewat `✕`
21. Klik `All Groups`
22. Klik `[+ Assign]` dan amati field Group serta Table User Picker
23. Hover Table User Picker
24. Verifikasi field Group kosong dengan placeholder `Select group`
25. Verifikasi Table User Picker kosong dan Disabled sampai Group dipilih
26. Verifikasi tidak ada tooltip pada Table User Picker

### TC-FA-RP-221: Assign Group Manager tanpa memilih group menampilkan error field-level

27. Tutup popup lewat `✕`
28. Catat daftar penugasan Group Manager lewat fixture BE sebagai baseline
29. Klik `[+ Assign]`
30. Centang Dimas Pranata tanpa memilih group
31. Klik `[Assign]`
32. Verifikasi error field-level pada field Group: `You must select a group`
33. Verifikasi popup tetap terbuka
34. Verifikasi daftar penugasan Group Manager (fixture BE) sama dengan baseline: tidak ada penugasan tersimpan
35. Verifikasi tidak ada toast

### TC-FA-RP-222: Mengubah nilai field Group secara manual mengosongkan seleksi user dan memuat ulang kandidat

36. Tutup popup lewat `✕`
37. Klik node `Data Center` di Sidebar lalu `[+ Assign]`
38. Centang Dimas Pranata dan Budi Santoso
39. Ubah field Group menjadi `Helpdesk`
40. Amati counter dan daftar
41. Verifikasi seluruh pilihan user dikosongkan (counter kembali tidak tampil)
42. Verifikasi daftar kandidat dimuat ulang untuk group `Helpdesk`
43. Tutup popup lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 43 langkah.
- Langkah penghubung (S-03): langkah 1, 10, 17, 19, 27–28, 36, 43. Langkah 17 mengubah field Group menjadi `Data Center` sebagai aksi yang diperiksa langkah 18 (TC-FA-RP-220 butir c tidak memberi nilai tujuan; spec memilih `Data Center`); langkah 19 mengembalikan nilai awal `IT Infrastructure` tanpa `Verifikasi` supaya popup berikutnya ditutup dari keadaan yang sama dengan TC. Langkah yang memuat kata "amati" (5, 15, 22, 40) adalah penghubung yang langsung diikuti `Verifikasi` (R-03). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 13; tidak ada `Verifikasi`.
- Urutan (S-10): blok validasi TC-FA-RP-221 berada sesudah blok TC-FA-RP-219 yang sukses karena mengikuti urutan TC sumber; langkah 13 memulihkan state sebelum blok berikutnya sehingga validasi tidak bergantung pada hasil sukses.
- Pembukaan popup untuk TC-FA-RP-221 memakai Sidebar `All Groups` (precondition d TC-FA-RP-221); langkah 'Klik `All Groups`' pada TC-FA-RP-220 meninggalkan Sidebar pada keadaan itu.
- Absence "tidak ada toast" pada TC-FA-RP-221 didahului `Verifikasi` error field-level yang membuktikan respons validasi sudah tampil (butir 8b.2).
- Post Condition TC-FA-RP-219 (penugasan hanya pada node `Data Center`, wewenang dinamis atas `Rack A1`, tanpa notifikasi) tidak punya langkah observasi dan tidak diasersi (S-01, S-15).
- Temuan untuk QA:
  - TC-FA-RP-219 tidak menyatakan node Sidebar awal; spec mengikuti urutan TC (group dipilih sebelum user dicentang) dan mengandalkan Sidebar pada node yang field Group-nya sudah terisi. TC-FA-RP-220 dan 221 menyatakan Table User Picker kosong dan Disabled sampai Group dipilih pada Sidebar `All Groups`. TC-FA-RP-221 langkah 2 (mencentang user tanpa memilih group pada Sidebar `All Groups`) bertentangan dengan Disabled pada TC-FA-RP-220; spec mengikuti teks TC.
  - TC-FA-RP-221 Expected b "tidak ada penugasan tersimpan" dan "tidak ada toast" tidak punya baseline di TC; spec memakai baseline penugasan Group Manager lewat fixture BE (S-12).
- Ukuran spec (43 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
