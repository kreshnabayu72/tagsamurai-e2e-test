---
id: TC-FA-COA-E2E-048-paginasi-tabel-dan-hapus-baris-terakhir
title: "Paginasi Tabel: Reset Halaman, Input Halaman Tidak Valid, Ukuran Halaman, dan Hapus Baris Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-81
  - TC-FA-COA-225
  - TC-FA-COA-227
  - TC-FA-COA-228
  - TC-FA-COA-226
coverage:
  web: automated
---

# Paginasi Tabel: Reset Halaman, Input Halaman Tidak Valid, Ukuran Halaman, dan Hapus Baris Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data: tabel client default berisi lebih dari 25 akun (akun Pre-setup P1 sampai P117 hasil seed, disediakan tim FE lewat `Fixture.settingsChartOfAccounts.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`), dengan lebih dari 10 akun Active dan ukuran halaman default 10.
- Data TC-FA-COA-226 (asumsi pre-setup P43, bukan data PRD): sebelas akun sekali pakai (Used By 0, belum pernah diekspor, bukan nilai default company) yang tepat menghasilkan 11 baris untuk satu kombinasi Filter Panel. Akun P43 memakai Account Code `7-1101` sampai `7-1111` berurutan (Pre-setup TC); kombinasi Filter Panel P43 disediakan tim FE (tidak tertulis di Pre-setup TC; lihat Temuan untuk QA). Satu akun P43 dihapus oleh langkah 39; seed tim FE memulihkan kesebelas akun P43 di hook `before` dan `after` spec ini.
- Pengecualian A-18 (S-06 dan S-12; butir "Pengecualian A-18" di `suite.md`): akun sekali pakai P43 menjadi target hapus (satu akun, langkah 39). Seed idempotent dan pemulihan ke keadaan awal dijalankan di hook `before` dan `after` spec ini (kemampuan disediakan tim FE/BE); akun P43 hanya dipakai spec ini.
- State yang diubah spec: Search, Filter Panel, sort, halaman, dan ukuran halaman tabel; tiap TC dipulihkan dengan langkah eksplisit (langkah 12, 30, 35, 44). Satu akun P43 terhapus (langkah 39).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-81: Paginasi: pilihan 10/25/50/100 dengan default 10, dan kembali ke halaman 1 saat Search berubah atau Filter Panel di-Apply

1. Pindah ke halaman 2
2. Ketik Search `Depreciation`, tekan Enter
3. Verifikasi tabel kembali ke halaman 1
4. Klik `(←)` pada kotak Search
5. Pindah ke halaman 2
6. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
7. Verifikasi tabel kembali ke halaman 1
8. Buka pilihan jumlah baris per halaman
9. Verifikasi pilihan jumlah baris: 10, 25, 50, 100
10. Verifikasi pilihan default jumlah baris per halaman adalah 10
11. Tutup pilihan jumlah baris per halaman dengan `Esc`
12. Klik `Clear all`

### TC-FA-COA-225: Paginasi: nomor halaman tidak valid pada input halaman diabaikan

13. Pindah ke halaman 2
14. Ketik `0` pada input nomor halaman lalu Enter
15. Verifikasi input diabaikan
16. Verifikasi tabel tetap di halaman 2
17. Ketik angka melebihi jumlah halaman (`9999`) pada input nomor halaman lalu Enter
18. Verifikasi input diabaikan
19. Verifikasi tabel tetap di halaman 2
20. Ketik `-1` pada input nomor halaman lalu Enter
21. Verifikasi input diabaikan
22. Verifikasi tabel tetap di halaman 2
23. Ketik `abc` pada input nomor halaman lalu Enter
24. Verifikasi input diabaikan
25. Verifikasi tabel tetap di halaman 2

### TC-FA-COA-227: Paginasi: mengganti ukuran halaman mengembalikan tabel ke halaman 1

26. Pindah ke halaman 3
27. Ubah jumlah baris per halaman menjadi 25
28. Verifikasi tabel kembali ke halaman 1
29. Verifikasi ukuran halaman tabel 25
30. Ubah jumlah baris per halaman kembali menjadi 10

### TC-FA-COA-228: Paginasi: mengganti sort tidak mengubah nomor halaman

31. Pindah ke halaman 2
32. Klik header Function satu kali
33. Verifikasi nomor halaman tetap 2
34. Verifikasi isi halaman 2 mengikuti urutan sort Function naik (↑)
35. Klik header Function dua kali sampai netral

### TC-FA-COA-226: Paginasi: menghapus baris terakhir di halaman terakhir memindahkan tabel ke halaman terakhir yang masih ada

36. Terapkan kombinasi Filter Panel P43 (kombinasi disediakan tim FE)
37. Pindah ke halaman 2 (satu baris)
38. Klik row action `Delete` pada satu-satunya baris halaman 2
39. Klik `[Delete]` pada dialog D-07
40. Verifikasi toast `Success, account has been deleted.`
41. Verifikasi tabel pindah ke halaman 1
42. Verifikasi halaman 1 memuat 10 baris
43. Verifikasi tabel tidak menampilkan halaman kosong
44. Klik `Clear all`

## Notes

- Alasan spec di atas sekitar 35 langkah (44 langkah): lima TC Paginasi satu kelas fungsional pada satu layar dan satu dataset, tiap TC berdiri sendiri dan bagian sesudahnya tetap bermakna bila satu TC gagal; Expected dipecah satu `Verifikasi` per klausa (S-01) dan input tidak valid TC-FA-COA-225 diverifikasi satu per input. TC-FA-COA-226 menghapus baris sehingga berada di akhir spec (S-10).
- Langkah penghubung (S-03, S-09): langkah 4 (mengosongkan Search), 11 (menutup pilihan ukuran halaman), 12 (melepas filter), 30 (memulihkan ukuran halaman 10), 35 (mengembalikan sort ke netral), dan 44 (melepas filter P43). Langkah 37 dan 38 memakai posisi baris di halaman 2 karena baris target adalah satu-satunya baris halaman itu; Search nama baris tidak dipakai karena kombinasi Filter Panel P43 tidak tertulis di TC dan baris target adalah baris terakhir menurut urutan tabel.
- Langkah 40 (toast sukses Delete) mengikuti teks toast Delete akun di TC-FA-COA-62 dan 267; TC-FA-COA-226 butir a hanya menulis "Delete berhasil".
- Tidak ada asersi pencatatan/log di spec ini; log Delete akun ditangani spec Delete (TC-FA-COA-62).
- A-18: TC-226 memakai akun sekali pakai P43 sebagai target hapus; akun P43 hanya dipakai spec ini dan dipulihkan di hook `before` dan `after`.
- Temuan untuk QA:
  - TC-FA-COA-226 tidak menyebut kombinasi Filter Panel secara konkret (Pre-setup P43 menetapkan kode `7-1101` sampai `7-1111` tetapi hanya menulis "satu kombinasi Filter Panel"); spec menulis "disediakan tim FE" tanpa endpoint karangan.
  - TC-FA-COA-226 butir a tidak menyebut toast sukses; spec memakai teks toast Delete dari TC-FA-COA-62.
  - TC-FA-COA-81 langkah 1 sampai 3 tidak menyebut kata Search konkret; spec memakai `Depreciation` dan mengasumsikan hasilnya berisi lebih dari satu halaman atau tetap di halaman 1 setelah Enter.
  - TC-FA-COA-227 langkah 1 (halaman 3) mensyaratkan lebih dari 20 akun pada ukuran 10; terpenuhi oleh tabel lebih dari 25 akun.
