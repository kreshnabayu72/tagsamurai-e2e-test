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
- Data: tabel client default berisi lebih dari 25 akun (akun Pre-setup P1 sampai P115 hasil seed, disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`), dengan lebih dari 10 akun Active dan ukuran halaman default 10.
- Data TC-FA-COA-226 (asumsi pre-setup P43, bukan data PRD): sebelas akun sekali pakai (Used By 0, belum pernah diekspor, bukan nilai default company) yang tepat menghasilkan 11 baris untuk satu kombinasi Filter Panel. Akun dan kombinasi Filter Panel P43 disediakan tim FE (tidak tertulis di Pre-setup TC; lihat Temuan untuk QA). Satu akun P43 dihapus oleh langkah 35; sisa 10 akun dipulihkan oleh seed tim FE di hook `before` dan `after` spec ini.
- State yang diubah spec: Search, Filter Panel, sort, halaman, dan ukuran halaman tabel; tiap TC dipulihkan dengan langkah eksplisit (langkah 12, 26, 31, 40). Satu akun P43 terhapus (langkah 35).
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
15. Verifikasi input diabaikan dan tabel tetap di halaman 2
16. Ketik angka melebihi jumlah halaman (`9999`) pada input nomor halaman lalu Enter
17. Verifikasi input diabaikan dan tabel tetap di halaman 2
18. Ketik `-1` pada input nomor halaman lalu Enter
19. Verifikasi input diabaikan dan tabel tetap di halaman 2
20. Ketik `abc` pada input nomor halaman lalu Enter
21. Verifikasi input diabaikan dan tabel tetap di halaman 2

### TC-FA-COA-227: Paginasi: mengganti ukuran halaman mengembalikan tabel ke halaman 1

22. Pindah ke halaman 3
23. Ubah jumlah baris per halaman menjadi 25
24. Verifikasi tabel kembali ke halaman 1
25. Verifikasi ukuran halaman tabel 25
26. Ubah jumlah baris per halaman kembali menjadi 10

### TC-FA-COA-228: Paginasi: mengganti sort tidak mengubah nomor halaman

27. Pindah ke halaman 2
28. Klik header Function satu kali
29. Verifikasi nomor halaman tetap 2
30. Verifikasi isi halaman 2 mengikuti urutan sort Function naik (↑)
31. Klik header Function dua kali sampai netral

### TC-FA-COA-226: Paginasi: menghapus baris terakhir di halaman terakhir memindahkan tabel ke halaman terakhir yang masih ada

32. Terapkan kombinasi Filter Panel P43 (kombinasi disediakan tim FE)
33. Pindah ke halaman 2 (satu baris)
34. Klik row action `Delete` pada satu-satunya baris halaman 2
35. Klik `[Delete]` pada dialog D-07
36. Verifikasi toast `Success, account has been deleted.`
37. Verifikasi tabel pindah ke halaman 1
38. Verifikasi halaman 1 memuat 10 baris
39. Verifikasi tabel tidak menampilkan halaman kosong
40. Klik `Clear all`

## Notes

- Alasan spec di atas sekitar 35 langkah (40 langkah): lima TC Paginasi satu kelas fungsional pada satu layar dan satu dataset, tiap TC berdiri sendiri dan bagian sesudahnya tetap bermakna bila satu TC gagal; Expected dipecah satu `Verifikasi` per klausa (S-01) dan input tidak valid TC-FA-COA-225 diverifikasi satu per input. TC-FA-COA-226 menghapus baris sehingga berada di akhir spec (S-10).
- Langkah penghubung (S-03, S-09): langkah 4 (mengosongkan Search), 11 (menutup pilihan ukuran halaman), 12 (melepas filter), 26 (memulihkan ukuran halaman 10), 31 (mengembalikan sort ke netral), dan 40 (melepas filter P43). Langkah 33 dan 34 memakai posisi baris di halaman 2 karena baris target adalah satu-satunya baris halaman itu; Search nama baris tidak dipakai karena identitas akun P43 tidak tertulis di TC.
- Langkah 36 (toast sukses Delete) mengikuti teks toast Delete akun di TC-FA-COA-62 dan 267; TC-FA-COA-226 butir a hanya menulis "Delete berhasil".
- Tidak ada asersi pencatatan/log di spec ini; log Delete akun ditangani spec Delete (TC-FA-COA-62).
- Temuan untuk QA:
  - TC-FA-COA-226 tidak menyebut akun P43 dan kombinasi Filter Panel secara konkret (Pre-setup P43 hanya menulis "satu kombinasi Filter Panel"); spec menulis "disediakan tim FE" tanpa endpoint karangan.
  - TC-FA-COA-226 butir a tidak menyebut toast sukses; spec memakai teks toast Delete dari TC-FA-COA-62.
  - TC-FA-COA-81 langkah 1 sampai 3 tidak menyebut kata Search konkret; spec memakai `Depreciation` dan mengasumsikan hasilnya berisi lebih dari satu halaman atau tetap di halaman 1 setelah Enter.
  - TC-FA-COA-227 langkah 1 (halaman 3) mensyaratkan lebih dari 20 akun pada ukuran 10; terpenuhi oleh tabel lebih dari 25 akun.
