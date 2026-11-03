---
id: TC-AC-RP-E2E-069-volume-selection-limit-role-detail-dan-picker
title: "Volume Selection Limit: Select All dan Centang Manual pada Role Detail serta Popup Assign Total Control"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-201
  - TC-AC-RP-202
  - TC-AC-RP-222
  - TC-AC-RP-432
coverage:
  web: automated
---

# Volume Selection Limit: Select All dan Centang Manual pada Role Detail serta Popup Assign Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Seleksi Besar `totalControlBigRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Gunawan`), password `Spectra.env.AC_RP_BIG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_RP_BIG_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #20 (entitas `Distributor Seleksi Besar` dengan 105 user Standard yang memegang `Manage group`), #21 (System Limits: Selection Limit 100). Volume 105 user disiapkan lewat seed atau API oleh tim FE/BE (kelas volume data, bagian 3 prinsip 13e).
- Data Dinamis: spec ini tidak membuat Data Dinamis dan tidak mengubah data (hanya seleksi sisi klien). Nilai bersuffix `+{runId}-069` tidak dipakai karena tidak ada data yang dibuat spec.
- Jumlah kandidat picker `Read Only` pada entitas ini lebih dari 10 sehingga halaman kedua tersedia (TC-AC-RP-222); ukuran halaman default 10.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-201: Selection Limit pada Select All Role Detail

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage group` lalu klik `Detail`
3. Centang satu baris, lalu klik tombol `Select All (105 records)` pada Bulk Action Bar
4. Verifikasi seleksi di-cap ke 100 baris pertama
5. Verifikasi toast "Error, only the first 100 of 105 rows were selected. Narrow your filter to include the rest."
6. Klik icon clear selection pada Bulk Action Bar

### TC-AC-RP-202: Selection Limit pada centang manual Role Detail

7. Pilih 100 baris per halaman
8. Untuk baris ke-1 sampai baris ke-100 pada halaman, centang checkbox baris satu per satu (100 klik)
9. Klik halaman berikutnya (halaman 2)
10. Arahkan kursor ke checkbox baris ke-101 (baris pertama halaman 2)
11. Verifikasi checkbox baris ke-101 diblok (disabled)
12. Verifikasi tooltip "You've reached the maximum selection of 100 rows."
13. Verifikasi counter seleksi tetap 100

### TC-AC-RP-222: Select All header picker hanya memilih kandidat di halaman aktif

14. Buka halaman `Settings > Role & Permission`
15. Klik tab `Read Only`
16. Klik tombol "+ Assign"
17. Klik checkbox Select All di header picker
18. Verifikasi hanya 10 kandidat di halaman aktif terpilih
19. Verifikasi counter "10 Users selected"
20. Klik halaman 2 pada pagination picker
21. Verifikasi kandidat di halaman 2 tidak terpilih
22. Klik `✕` pada popup

### TC-AC-RP-432: Selection Limit pada centang manual popup Assign Total Control

23. Klik tab `Total Control`
24. Klik tombol "+ Assign"
25. Pilih 100 baris per halaman
26. Untuk baris ke-1 sampai baris ke-100 pada halaman, centang checkbox baris satu per satu (100 klik)
27. Pindah ke halaman berikutnya
28. Arahkan kursor ke checkbox baris ke-101
29. Verifikasi checkbox baris ke-101 diblok (disabled)
30. Verifikasi tooltip "You've reached the maximum selection of 100 rows."
31. Verifikasi counter tetap "100 Users selected"

## Notes

- Mode: FE+BE. Kelas harness: volume data khusus (e). Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Alasan jumlah langkah melewati ±35 saat ekspansi (bagian 8b butir 7): langkah 8 dan 26 mengulang satu aksi identik (centang checkbox baris ke-1 sampai ke-100) dengan parameter jelas (nomor baris pada halaman, ukuran halaman 100) tanpa langkah bersyarat; ekspansi 100 iterasi per langkah. Semua blok berkelas sama (batas Selection Limit) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah langkah nominal 31.
- Langkah penghubung (S-03, S-09): langkah 6 (bersihkan seleksi sebelum blok berikutnya), 14 sampai 15 (navigasi ke Tab `Read Only`; membuka ulang halaman membuang seleksi blok sebelumnya), 22 (tutup popup tanpa dialog Unsaved Changes karena popup picker bukan form), 23 (pilih Tab `Total Control`), langkah 9, 20, dan 27 (pindah halaman, S-14).
- Temuan untuk QA:
  - TC-AC-RP-222 Langkah Uji tidak menyebut langkah pindah ke halaman 2; spec menambah langkah 20 agar asersi "kandidat di halaman 2 tidak terpilih" punya keadaan menuju (S-14).
  - TC-AC-RP-202 dan TC-AC-RP-432 Expected "counter tetap 100" tidak menyebut teks counter pada Role Detail; spec memakai "counter seleksi tetap 100" untuk TC-AC-RP-202 dan "100 Users selected" untuk TC-AC-RP-432 sesuai TC.
  - TC-AC-RP-201 Langkah 4 tidak menyebut bahwa 105 user ditampilkan dalam satu halaman atau beberapa halaman; tidak diasersi.
  - Pemulihan baseline tidak diperlukan karena spec tidak mengubah data; pernyataan "Data dipulihkan automation baseline" tidak ada pada TC sumber spec ini.
