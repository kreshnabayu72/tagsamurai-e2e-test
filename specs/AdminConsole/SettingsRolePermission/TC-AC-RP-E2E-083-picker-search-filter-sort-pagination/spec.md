---
id: TC-AC-RP-E2E-083-picker-search-filter-sort-pagination
title: "Table User Picker: Search, Filter, Sort, Pagination, nama kembar, Position kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-289
  - TC-AC-RP-290
  - TC-AC-RP-291
  - TC-AC-RP-292
  - TC-AC-RP-423
coverage:
  web: automated
---

# Table User Picker: Search, Filter, Sort, Pagination, nama kembar, Position kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Pool picker (Pre-setup #12): `Alex Tan` (IT Specialist, IT, `alex.tan@client.com`, Active), `Sarah Kimura` (Supervisor, Logistics), `Jane Smith` (Inactive), `Dewi Anggreni` (QA Staff, Operations, `dewi.anggreni@client.com`), `John Dohan` (Staff, Operations), `Fajar Nugroho` (Analyst, Operations), `Dewi Anggraini` (Auditor, Finance, `dewi.a@client.com`).
- Data Dinamis: user Standard ber-keyword nama `Tono` (nama lengkap bebas dan unik terhadap data Pre-setup sehingga Search `Tono` hanya menemukan user ini; tanpa Position, Division `Warehouse`; Tabel Data Uji Dinamis #5), dibuat hook `before` lewat seeding API/fixture BE dengan email `tono.wibowo+{runId}-083@qwertysystem.net` dan dihapus di hook `after`; baris user ini diidentifikasi lewat email bersuffix itu.
- Kemampuan teknis: fixture BE untuk membuat dan menghapus user Standard (tim FE/BE); Role Detail Global Role `Manage TAG stock` dengan section Approvers (Pre-setup #15, #17). Spec ini tidak menulis data Pre-setup.

## Test Steps

1. Klik tombol "+ Assign"

### TC-AC-RP-289: Search picker mencakup Name, Email, Position, Division, Status

2. Ketik Search `alex.tan@`, tekan Enter
3. Verifikasi baris `Alex Tan` tampil (Email)
4. Verifikasi tidak ada baris selain `Alex Tan`
5. Ganti isi kotak search dengan `logistics`, tekan Enter
6. Verifikasi baris `Sarah Kimura` tampil (Division)
7. Verifikasi tidak ada baris selain `Sarah Kimura`
8. Ganti isi kotak search dengan `Inactive`, tekan Enter
9. Verifikasi baris `Jane Smith` (Inactive) tampil
10. Verifikasi baris `Alex Tan` (Active) tidak tampil

### TC-AC-RP-290: Filter picker Position, Division, Status

11. Klik `(←)` pada kotak Search
12. Klik Filter
13. Verifikasi field Filter: Position, Division, dan Status
14. Verifikasi field Temporary User memakai placeholder "All options"
15. Pilih Division `Operations`
16. Klik `[Apply]`
17. Verifikasi kandidat Division Operations tampil (`Dewi Anggreni`, `Fajar Nugroho`, `Jane Smith` (Inactive), `John Dohan`)
18. Verifikasi tidak ada kandidat selain Division Operations

### TC-AC-RP-291: Sort dan Pagination picker

19. Klik `[Clear Field]`, lalu klik `[Apply]`
20. Klik header Email sekali
21. Verifikasi urutan Email A-Z
22. Verifikasi Pagination default 10
23. Verifikasi pilihan Pagination 10, 25, 50, dan 100

### TC-AC-RP-423: Position kosong tampil "—" dan terurut di akhir saat ascending dan di awal saat descending pada picker

24. Ketik Search `Tono`, tekan Enter
25. Verifikasi baris user ber-keyword `Tono` (email `tono.wibowo+{runId}-083@qwertysystem.net`) menampilkan "—" pada kolom Position
26. Klik `(←)` pada kotak Search
27. Klik header Position sekali
28. Pindah ke halaman terakhir
29. Verifikasi baris user ber-keyword `Tono` (email `tono.wibowo+{runId}-083@qwertysystem.net`) berada di akhir daftar pada urutan ascending
30. Klik header Position sekali lagi
31. Pindah ke halaman pertama
32. Verifikasi baris user ber-keyword `Tono` (email `tono.wibowo+{runId}-083@qwertysystem.net`) berada di awal daftar pada urutan descending

### TC-AC-RP-292: Nama kembar dibedakan lewat Email, Position, Division

33. Tutup popup Table User Picker dengan `✕`
34. Klik tab `System`
35. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
36. Klik "+ Assign" pada section Approvers
37. Ketik Search `dewi`, tekan Enter
38. Verifikasi dua baris `Dewi Anggraini` (`dewi.a@client.com`, Auditor, Finance) dan `Dewi Anggreni` (`dewi.anggreni@client.com`, QA Staff, Operations) tampil berdampingan dengan Email terlihat

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec ini di atas smell 35 langkah (38 langkah): lima TC sumber (Search, Filter, Sort dan Pagination, Position kosong, nama kembar) memakai picker Table User yang sama sehingga membelahnya berarti mengulang langkah buka picker; langkah dipertahankan dalam satu spec untuk menjaga satu alur picker, keputusan pemecahan diserahkan ke tinjauan QA.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Picker dibuka sekali di langkah 1 untuk TC-AC-RP-289, 290, 291, dan 423 (langkah membuka picker TC berikutnya tidak diulang; konvensi bagian 3, halaman yang sama dipakai berulang); TC-AC-RP-292 memakai picker Approvers pada Role Detail sehingga dijalankan terakhir.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 11 dan 26 mengosongkan Search; langkah 19 mengosongkan Filter; langkah 28 dan 31 memindahkan halaman agar posisi "di akhir" dan "di awal" dapat diamati (S-14); langkah 33 menutup picker sebelum pindah halaman.
- Ukuran spec (38 langkah, melewati sekitar 35): seluruh blok memakai satu komponen (Table User Picker, `ACRP-LOGIC-10`), satu akun, tanpa aksi tulis selain seeding dan penghapusan user ber-keyword `Tono`, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Verifikasi pembanding dan Verifikasi per klausa menaikkan jumlah langkah (S-01).
- Temuan untuk QA:
  - TC-AC-RP-423 menyebut baris berada "di akhir daftar" dan "di awal daftar" tanpa langkah pindah halaman; spec menambah langkah pindah ke halaman terakhir dan pertama karena pool melebihi 10 baris.
  - TC-AC-RP-423 Data Dinamis #5 tidak menyebut email; email bersuffix dipakai oleh spec untuk seeding dan untuk mengidentifikasi baris.
