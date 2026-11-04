---
id: TC-FA-COA-E2E-049-list-state-dan-independensi-filter-dari-column-visibility
title: "List State dan Independensi Filter dari Column Visibility"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-231
  - TC-FA-COA-232
  - TC-FA-COA-233
  - TC-FA-COA-234
coverage:
  web: automated
---

# List State dan Independensi Filter dari Column Visibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hanya dibaca, tidak diubah; identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`): akun P2 `6-2001` Repairs & Maintenance Expense dan P5 `CAP-6100` Capitalization Clearing – Repairs (keduanya Function Capitalization Offset, Active).
- Tabel client default berisi lebih dari 25 akun dengan ukuran halaman 10 (seed P1 sampai P117 disediakan tim FE). Search `-` dan Filter Active = Active menyisakan lebih dari 10 akun sehingga halaman 2 terisi (asumsi pre-setup; lihat Temuan untuk QA).
- Kolom Function tampil secara default; TC-FA-COA-231 menyembunyikannya lewat Setup Column (langkah 2) dan memulihkannya pada langkah 11 (R-24).
- State yang diubah spec: Filter Panel, Search, sort, halaman, dan konfigurasi kolom (hanya kolom Function, dipulihkan). Tiap TC dipulihkan dengan langkah eksplisit (langkah 15, 27, 44). Tidak ada data yang ditulis. Hook `after` menghapus preferensi kolom dan tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-231: Filter independen dari Column Visibility: menyembunyikan kolom tidak menghilangkan filter, tetapi mengeluarkan kolom dari Search

1. Buka Filter Panel, pilih Function = Capitalization Offset, klik `[Apply]`
2. Klik header Actions ⋯ > `Setup Column...`, hilangkan centang kolom `Function`, klik `[Save]`
3. Buka Filter Panel
4. Verifikasi field Function tetap ada di Filter Panel dengan nilai Capitalization Offset
5. Verifikasi sedikitnya satu baris tampil di tabel
6. Verifikasi tabel tetap tersaring oleh Function = Capitalization Offset (chip filter Function tetap aktif)
7. Tutup Filter Panel dengan klik ulang ikon Filter
8. Ketik Search `Capitalization Offset`, tekan Enter
9. Verifikasi tabel menampilkan empty state `No results found`
10. Verifikasi baris akun P2 dan P5 tidak tampil
11. Klik header Actions ⋯ > `Setup Column...`, centang kembali kolom `Function`, klik `[Save]`
12. Ganti isi kotak search dengan `Capitalization Offset`, tekan Enter
13. Verifikasi baris akun P2 tampil
14. Verifikasi baris akun P5 tampil
15. Klik `(←)` pada kotak Search, lalu klik `Clear all`

### TC-FA-COA-232: List State: refresh manual mempertahankan sub-tab, Search, Filter, Sort, dan paginasi

16. Ketik Search `-`, tekan Enter
17. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
18. Klik header Function satu kali
19. Pindah ke halaman 2
20. Refresh halaman dengan `F5`
21. Verifikasi tab `Chart of Accounts` tetap aktif
22. Verifikasi Search `-` tetap terisi
23. Verifikasi filter Active = Active tetap aktif
24. Verifikasi sort Function naik (↑) tetap aktif
25. Verifikasi tabel tetap di halaman 2
26. Verifikasi ukuran halaman tetap 10
27. Klik menu sidebar Fixed Asset > Settings > Accounting, lalu buka tab `Chart of Accounts` untuk mereset state tabel

### TC-FA-COA-233: List State: klik ulang menu sidebar mereset Search, Sort, Filter, dan paginasi

28. Ketik Search `-`, tekan Enter
29. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
30. Klik header Function satu kali
31. Pindah ke halaman 2
32. Klik menu sidebar Fixed Asset > Settings > Accounting, lalu buka tab `Chart of Accounts`
33. Verifikasi Search kosong
34. Verifikasi tidak ada filter ter-Apply
35. Verifikasi sort kembali default Account Code A-Z
36. Verifikasi tabel di halaman 1
37. Verifikasi ukuran halaman 10

### TC-FA-COA-234: List State: pindah tab Accounting lalu kembali memulihkan state tabel Chart of Accounts

38. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
39. Klik header Function satu kali
40. Pindah ke tab `Preferences`
41. Kembali ke tab `Chart of Accounts`
42. Verifikasi filter Active = Active dipulihkan seperti sebelum pindah tab
43. Verifikasi sort Function naik (↑) dipulihkan seperti sebelum pindah tab
44. Klik menu sidebar Fixed Asset > Settings > Accounting, lalu buka tab `Chart of Accounts` untuk mereset state tabel

## Notes

- Alasan spec di atas sekitar 35 langkah (44 langkah): empat TC List State dan Filter pada satu layar dan satu dataset, kelas fungsional yang sama dan berdiri sendiri; tiap TC membangun kombinasi Search, Filter, Sort, dan halaman sendiri (TC-FA-COA-232 dan 233 masing-masing lima aksi) dan Expected dipecah satu `Verifikasi` per klausa (S-01), sehingga tidak ada langkah yang dapat dibuang tanpa menghilangkan butir.
- Langkah penghubung (S-03, S-09): langkah 7 (menutup Filter Panel), 15 (mengosongkan Search dan melepas filter), 27 dan 44 (klik menu sidebar untuk mereset state tabel; langkah 32 adalah aksi uji TC-FA-COA-233). Langkah 11 mengembalikan kolom Function sesuai langkah 5 TC-FA-COA-231 (dijalankan di spec ini pada langkah 11) sekaligus pemulihan Setup Column (R-24, 8b.14). Langkah 12 memakai "ganti isi kotak search" karena kotak Search masih terisi dari langkah 8 (8b.9).
- Langkah 33 sampai 37 mengasersi keadaan kosong dan default tepat setelah aksi sidebar; state sebelum aksi dibangun langkah 28 sampai 31.
- Spec ini hanya memuat TC-FA-COA-231, 232, 233, 234.
- Temuan untuk QA:
  - TC-FA-COA-231 butir a ("tabel tetap tersaring") tidak dapat dibuktikan dari isi kolom Function karena kolom itu disembunyikan; spec mengasersi chip filter Function tetap aktif dan sedikitnya satu baris tampil. Teks chip filter tidak tertulis di TC.
  - TC-FA-COA-232 mensyaratkan Search `-` dan Filter Active menyisakan lebih dari 10 akun agar halaman 2 ada; precondition TC hanya menulis "lebih dari 25 akun"; spec menulis asumsi itu di Prerequisites.
  - TC-FA-COA-234 tidak mengasersi Search dan halaman; hanya filter dan sort yang diasersi sesuai Expected.
  - TC-FA-COA-233 butir a menulis "tidak ada filter ter-Apply" tanpa menyebut indikator UI (chip); spec mengasersi tidak ada chip filter aktif.
