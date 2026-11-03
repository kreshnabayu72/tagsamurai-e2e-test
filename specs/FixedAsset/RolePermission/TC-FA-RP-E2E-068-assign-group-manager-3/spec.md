---
id: TC-FA-RP-E2E-068-assign-group-manager-3
title: "Assign Group Manager (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-228
  - TC-FA-RP-229
  - TC-FA-RP-231
  - TC-FA-RP-234
  - TC-FA-RP-1037
coverage:
  web: automated
---

# Assign Group Manager (3/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Budi Santoso, Ahmad Fauzi, ...), #17 (Gunawan Halim Home Group `Data Center`, Hesti Rahma Home Group `Logistics Warehouse`, Joko Santoso Home Group `IT Infrastructure`, Indra Kusuma tanpa Home Group), #18 (pohon group). Pada TC-FA-RP-231 Ahmad Fauzi di-seed memegang Group Role `Manage files` Read di `Data Center` dan Create, Update, Delete tidak aktif.
- Sesi kedua: sesi API Total Control kedua (Pre-setup #3, Rina Wulandari, `Spectra.env.FA_TC2_PASSWORD`) menghapus group `Dock 1` pada TC-FA-RP-229; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): penugasan Group Manager dan Group Role dicatat sebagai baseline untuk Expected "tidak ada penugasan tersimpan" dan "tidak berubah".
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC2_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-228: Field Group popup bagi Total Control memuat seluruh pohon yang dapat dipilih

1. Klik Tab `Group Manager`
2. Klik `[+ Assign]` di Tab Group Manager
3. Buka field Group
4. Verifikasi seluruh node `Head Office`, `IT Infrastructure`, `Data Center`, `Rack A1`, `Helpdesk`, `Logistics Warehouse`, dan `Dock 1` dapat dipilih (single-select)
5. Tutup popup lewat `✕`

### TC-FA-RP-229: Group dihapus sesi lain sebelum Submit: error field-level di bawah field Group

6. Catat daftar penugasan Group Manager lewat fixture BE sebagai baseline
7. Pada sesi 1 klik `[+ Assign]`, pilih group `Dock 1`, centang Budi Santoso
8. Hapus group `Dock 1` lewat sesi API Total Control kedua (Rina Wulandari) hingga tersimpan
9. Pada sesi 1 klik `[Assign]`
10. Verifikasi pesan inline tepat di bawah field Group: `This group no longer exists. Please select another.`
11. Verifikasi popup tetap terbuka
12. Verifikasi daftar penugasan Group Manager (fixture BE) sama dengan baseline: tidak ada penugasan tersimpan
13. Tutup popup lewat `✕`
14. Pulihkan group `Dock 1` lewat seeding API

### TC-FA-RP-231: Assign Group Manager tidak mengubah baris Group Role eksplisit milik user

15. Tetapkan Ahmad Fauzi memegang Group Role `Manage files` Read di `Data Center` lewat seeding API dan catat barisnya sebagai baseline
16. Klik node `Data Center` di Sidebar Group Tree
17. Klik `[+ Assign]`, pilih `Data Center`, centang Ahmad Fauzi, klik `[Assign]`
18. Tunggu aksi selesai: popup tertutup
19. Buka Tab System lalu Detail Role `Manage files` dan pilih node `Data Center`
20. Verifikasi baris Ahmad Fauzi pada `Manage files` di `Data Center` tetap Read aktif dan Create, Update, Delete tidak berubah dari baseline

### TC-FA-RP-234: User ber-Home Group constraint tidak muncul di popup Assign Group Manager pada group di luar constraint-nya dan dapat ditugaskan pada group di dalamnya

21. Klik Tab `Group Manager`
22. Klik `[+ Assign]`
23. Pilih group `Data Center` lalu ketik Search `Hesti Rahma`, tekan Enter
24. Verifikasi Hesti Rahma tidak ada di daftar picker (group `Data Center` di luar Home Group constraint-nya; empty state hasil Search)
25. Ubah field Group menjadi `Dock 1` lalu ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
26. Verifikasi Hesti Rahma ada di daftar picker (`Dock 1` adalah descendant `Logistics Warehouse`)
27. Centang Hesti Rahma lalu klik `[Assign]`
28. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
29. Klik node `Dock 1` di Sidebar Group Tree
30. Verifikasi baris Hesti Rahma tampil dengan badge Group `Dock 1`

### TC-FA-RP-1037: Popup Assign Group Manager menyaring user ber-Home Group constraint: constraint sendiri dan descendant eligible, ancestor dan sibling tidak, user tanpa constraint bebas

31. Klik `[+ Assign]`
32. Pilih group `Logistics Warehouse` lalu ketik Search `Hesti Rahma`, tekan Enter
33. Verifikasi Hesti Rahma ada di daftar picker (node sama dengan constraint)
34. Ubah field Group menjadi `Head Office` lalu ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
35. Verifikasi Hesti Rahma tidak ada di daftar picker (ancestor di luar constraint; empty state hasil Search)
36. Ubah field Group menjadi `Data Center` lalu ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
37. Verifikasi Hesti Rahma tidak ada di daftar picker (sibling di luar constraint; empty state hasil Search)
38. Ganti isi kotak search dengan `Indra Kusuma`, tekan Enter
39. Verifikasi Indra Kusuma ada di daftar picker (user tanpa constraint bebas di group mana pun)
40. Tutup popup lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 40 langkah.
- Langkah penghubung (S-03): langkah 1, 5–6, 13, 16, 18, 21, 29, 40. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 14–15; tidak ada `Verifikasi`.
- TC-FA-RP-229 memakai dua sesi (Manual Only (d) di TC): sesi 2 adalah pelaku kedua yang hanya memicu penghapusan group sehingga memakai sesi API (suite.md; langkah ditulis "... hingga ... tersimpan", R-20), bukan konteks kedua kelas c. Group `Dock 1` dipulihkan di langkah 14 dan di hook `after`.
- Penyimpangan kecil TC-FA-RP-1037: popup tetap terbuka dan group diubah dari satu node ke node berikutnya (halaman yang dipakai berulang, konvensi bagian 3 prinsip 13) karena kasus hanya mengetik dan mengamati tanpa submit.
- Post Condition TC-FA-RP-229 (pemulihan group) tidak punya langkah observasi dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-RP-231 Expected "C/U/D tidak berubah" pada `Manage files`: kolom Create dan Update berupa `—` pada Group Role `Manage files` (TC-FA-RP-247); spec mengasersi seluruh nilai sama dengan baseline.
  - TC-FA-RP-234 dan 1037: Search di picker tetap aktif sesudah group diubah tidak dinyatakan TC; spec mengganti isi kotak search sesudah tiap perubahan group.
- Ukuran spec (40 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
