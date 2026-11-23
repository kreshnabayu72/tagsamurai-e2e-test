---
id: TC-FA-SU-E2E-464-tab-transaction-admin-log-assignment-pagination-dan-state-per-sub-tab
title: "Tab Transaction Admin Log Sub-tab Assignment: Pagination dan State per Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1166
  - TC-FA-SU-1173
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Pagination dan State per Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pre-setup untuk state sub-tab lain: sub-tab Borrow milik Budi Santoso (Pre-setup #29) dipakai sebagai tempat menerapkan kontrol berbeda (Search `Projector`, Sort `Date`, page size 50); keyword dipilih spec.

## Test Steps

### TC-FA-SU-1166: Pagination (page size, navigasi, dan kasus tepi)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Verifikasi footer pagination menampilkan 10 baris per halaman
3. Klik dropdown page size
4. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi `All`
5. Tutup dropdown page size dengan Esc
6. Isi nomor halaman `0`, tekan Enter
7. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
8. Isi nomor halaman `-1`, tekan Enter
9. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
10. Isi nomor halaman `999`, tekan Enter
11. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
12. Isi nomor halaman `abc`, tekan Enter
13. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
14. Ganti page size ke 25
15. Verifikasi tabel menampilkan halaman 1
16. Ganti page size kembali ke 10
17. Verifikasi tabel menampilkan halaman 1
18. Klik header `Transaction ID` satu kali
19. Verifikasi tabel menampilkan halaman 1
20. Klik header `Transaction ID` dua kali lagi hingga sort kembali netral
21. Ketik Search `0071`, tekan Enter
22. Verifikasi tabel menampilkan halaman 1
23. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1173: State sub-tab dipertahankan per sub-tab

24. Ketik Search `Laptop`, tekan Enter
25. Klik icon Filter, buka dropdown `Group`, centang `Branch Surabaya`, lalu klik `[Apply]`
26. Klik header `Transaction ID` satu kali
27. Ganti page size ke 25
28. Klik Sub-tab Borrow
29. Ketik Search `Projector`, klik header `Date` satu kali, lalu ganti page size ke 50
30. Klik Sub-tab Assignment
31. Verifikasi Search `Laptop` tersimpan pada sub-tab Assignment
32. Verifikasi Filter `Group` = `Branch Surabaya` tersimpan pada sub-tab Assignment
33. Verifikasi Sort pada kolom `Transaction ID` tersimpan pada sub-tab Assignment
34. Verifikasi page size 25 tersimpan pada sub-tab Assignment
35. Klik Sub-tab Borrow
36. Verifikasi state sub-tab Borrow (Search `Projector`, Sort `Date`, dan page size 50) tidak dipengaruhi state sub-tab Assignment
37. Klik Sub-tab Assignment
38. Klik Back breadcrumb ke User List, lalu buka Detail User Budi Santoso, klik Tab Transaction Admin Log, dan klik Sub-tab Assignment
39. Verifikasi state sub-tab Assignment dipulihkan setelah Back breadcrumb (Search, Filter, Sort, dan page size 25)
40. Tekan F5 pada halaman Detail
41. Verifikasi state sub-tab Assignment dipulihkan setelah refresh F5 (Search, Filter, Sort, dan page size 25)
42. Klik menu Settings > User pada sidebar, lalu buka Detail User Budi Santoso, klik Tab Transaction Admin Log, dan klik Sub-tab Assignment
43. Verifikasi state sub-tab Assignment kembali ke default (Search kosong, tanpa Filter, sort default Date descending, page size 10)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan dropdown page size, pengosongan Search, pemulihan sort ke netral, dan perpindahan sub-tab; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Fixture sub-tab Assignment satu halaman; perpindahan antar halaman tidak dapat dicapai pada surface ini (butir e TC-FA-SU-1166 menyatakan perilaku multi-halaman diuji pada TC-FA-SU-359 dan TC-FA-SU-1057) sehingga tidak diasersi di sini.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1173 Langkah Uji nomor 2 tidak menyebut sub-tab lain dan kontrol yang dipakai; spec memakai sub-tab Borrow (sesuai butir b) dengan Search `Projector`, Sort `Date`, dan page size 50, serta Search `Laptop` dan Filter Group `Branch Surabaya` pada sub-tab Assignment. (2) TC-FA-SU-1173 langkah 5 tidak menyebut sub-tab aktif sesudah F5; spec mengasersi state sub-tab Assignment sesuai Expected c. (3) Butir "nomor halaman aktif tidak diuji" pada TC-FA-SU-1173 butir a diikuti: nomor halaman tidak diasersi.
- Spec ini berjumlah 43 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
