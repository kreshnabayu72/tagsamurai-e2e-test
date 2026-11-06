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
- Data Pre-setup: #15 (Budi Santoso, Ahmad Fauzi, ...), #17 (Gunawan Halim Home Group `Data Center`, Hesti Rahma Home Group `Logistics Warehouse`, Joko Santoso Home Group `IT Infrastructure`, Indra Kusuma tanpa Home Group), #18 (pohon group). Pada TC-FA-RP-231 (juga #24, #39) Ahmad Fauzi di-seed memegang Group Role `Manage files` Read saja (Delete tidak aktif) di `Data Center` dan Global Role `Manage accounting`.
- Sesi kedua: sesi API Total Control kedua (Pre-setup #3, Rina Wulandari, `Spectra.env.FA_TC2_PASSWORD`) menghapus group `Dock 1` pada TC-FA-RP-229; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): penugasan Group Manager, Group Role, dan Global Role dicatat sebagai baseline untuk Expected "tidak ada penugasan tersimpan" dan "tidak berubah".
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

### TC-FA-RP-231: Assign Group Manager menyelaraskan baris Group Role eksplisit yang sudah ada ke CRUD penuh sesuai kolom berlaku tanpa menyentuh baris Global Role

15. Tetapkan Ahmad Fauzi memegang Group Role `Manage files` Read saja (Delete tidak aktif) di `Data Center` dan Global Role `Manage accounting` lewat seeding API dan catat baris Global Role-nya sebagai baseline
16. Klik node `Data Center` di Sidebar Group Tree
17. Klik `[+ Assign]`, pilih `Data Center`, centang Ahmad Fauzi, klik `[Assign]`
18. Tunggu aksi selesai: popup tertutup
19. Buka Tab System lalu Detail Role `Manage files` dan pilih node `Data Center`
20. Verifikasi baris Ahmad Fauzi pada `Manage files` di `Data Center` memiliki Read dan Delete aktif (CRUD penuh sesuai kolom berlaku; Delete yang sebelumnya tidak aktif kini aktif)
21. Klik ikon Changelog di toolbar Detail Role dan amati entri Ahmad Fauzi
22. Verifikasi satu entri Action `Edit` Field `Delete`, Old Value `Inactive`, New Value `Active` untuk baris Ahmad Fauzi pada `Manage files` di `Data Center`
23. Verifikasi tidak ada entri untuk kolom Read dan tidak ada entri `Assign (via Group Manager)` untuk baris itu (baris sudah aktif)
24. Verifikasi Modified By entri itu berisi `Siti R`
25. Buka Detail Role Global Role `Manage accounting` dan amati baris Ahmad Fauzi
26. Verifikasi baris Global Role Ahmad Fauzi tidak berubah dari baseline

### TC-FA-RP-234: User ber-Home Group constraint tidak muncul di popup Assign Group Manager pada group di luar constraint-nya dan dapat ditugaskan pada group di dalamnya

27. Klik Tab `Group Manager`
28. Klik `[+ Assign]`
29. Pilih group `Data Center` lalu ketik Search `Hesti Rahma`, tekan Enter
30. Verifikasi Hesti Rahma tidak ada di daftar picker (group `Data Center` di luar Home Group constraint-nya; empty state hasil Search)
31. Ubah field Group menjadi `Dock 1` lalu ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
32. Verifikasi Hesti Rahma ada di daftar picker (`Dock 1` adalah descendant `Logistics Warehouse`)
33. Centang Hesti Rahma lalu klik `[Assign]`
34. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
35. Klik node `Dock 1` di Sidebar Group Tree
36. Verifikasi baris Hesti Rahma tampil dengan badge Group `Dock 1`

### TC-FA-RP-1037: Popup Assign Group Manager menyaring user ber-Home Group constraint: constraint sendiri dan descendant eligible, ancestor dan sibling tidak, user tanpa constraint bebas

37. Klik `[+ Assign]`
38. Pilih group `Logistics Warehouse` lalu ketik Search `Hesti Rahma`, tekan Enter
39. Verifikasi Hesti Rahma ada di daftar picker (node sama dengan constraint)
40. Ubah field Group menjadi `Head Office` lalu ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
41. Verifikasi Hesti Rahma tidak ada di daftar picker (ancestor di luar constraint; empty state hasil Search)
42. Ubah field Group menjadi `Data Center` lalu ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
43. Verifikasi Hesti Rahma tidak ada di daftar picker (sibling di luar constraint; empty state hasil Search)
44. Ganti isi kotak search dengan `Indra Kusuma`, tekan Enter
45. Verifikasi Indra Kusuma ada di daftar picker (user tanpa constraint bebas di group mana pun)
46. Tutup popup lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 46 langkah.
- Langkah penghubung (S-03): langkah 1, 5–6, 13, 16, 18, 27, 35, 46. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 14–15; tidak ada `Verifikasi`.
- TC-FA-RP-229 memakai dua sesi (Manual Only (d) di TC): sesi 2 adalah pelaku kedua yang hanya memicu penghapusan group sehingga memakai sesi API (suite.md; langkah ditulis "... hingga ... tersimpan", R-20), bukan konteks kedua kelas c. Group `Dock 1` dipulihkan di langkah 14 dan di hook `after`.
- Penyimpangan kecil TC-FA-RP-1037: popup tetap terbuka dan group diubah dari satu node ke node berikutnya (halaman yang dipakai berulang, konvensi bagian 3 prinsip 13) karena kasus hanya mengetik dan mengamati tanpa submit.
- Post Condition TC-FA-RP-229 (pemulihan group) dan TC-FA-RP-231 (Ahmad Fauzi dipulihkan ke state Pre-setup #15 oleh automation baseline) tidak punya langkah observasi dan tidak diasersi.
- Absence entri pada TC-FA-RP-231 (kolom Read, `Assign (via Group Manager)`) didahului `Verifikasi` entri `Edit` Field `Delete` pada Changelog yang sama sebagai anchor positif (butir 8b.2).
- Temuan untuk QA:
  - TC-FA-RP-231 Expected b tidak menyebut cara membuka atau menutup Changelog Detail Role selain ikon di toolbar; spec membuka Changelog di langkah 21 dan langsung membuka Detail Role Global Role di langkah 25 tanpa langkah menutupnya.
  - TC-FA-RP-234 dan 1037: Search di picker tetap aktif sesudah group diubah tidak dinyatakan TC; spec mengganti isi kotak search sesudah tiap perubahan group.
- Ukuran spec (46 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
