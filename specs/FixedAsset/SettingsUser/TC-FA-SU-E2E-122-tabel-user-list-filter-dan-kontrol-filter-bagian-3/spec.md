---
id: TC-FA-SU-E2E-122-tabel-user-list-filter-dan-kontrol-filter-bagian-3
title: "Tabel User List: Filter dan Kontrol Filter (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-346
  - TC-FA-SU-347
  - TC-FA-SU-348
coverage:
  web: automated
---

# Tabel User List: Filter dan Kontrol Filter (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Keyword Search tanpa hasil: `zzzzqx` (nilai pilihan spec; TC-FA-SU-347 tidak menyebut keyword). Filter yang dipilih TC-FA-SU-348 langkah 2 dan 5 tidak disebut TC; spec memakai Division `Logistics`.
- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-346: Kombinasi Search dan Filter dua arah

1. Pindah ke halaman 2
2. Ketik Search `Budi`, tekan Enter
3. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah
4. Klik ikon Filter, buka dropdown Status, centang `Active`, klik `[Apply]`
5. Verifikasi hasil irisan Search `Budi` dan Filter Status `Active`: `Budi Santoso`, `Indra Wijaya`, `Putri Anggraeni`, `Vina Maharani` (4 baris)
6. Verifikasi keyword `Budi` tetap pada kotak Search setelah Filter di-Apply
7. Klik `[Clear Field]` lalu `[Apply]`, klik `(←)` pada kotak Search
8. Buka dropdown Status, centang `Active`, klik `[Apply]`
9. Ketik Search `Budi`, tekan Enter
10. Verifikasi hasil identik: `Budi Santoso`, `Indra Wijaya`, `Putri Anggraeni`, `Vina Maharani`
11. Verifikasi Filter Status `Active` tetap aktif setelah Search dijalankan
12. Klik `[Clear Field]` lalu `[Apply]`, klik `(←)` pada kotak Search

### TC-FA-SU-347: Pelepasan kontrol dan recovery empty state

13. Ketik Search `Budi`, tekan Enter
14. Buka dropdown Status, centang `Active`, klik `[Apply]`
15. Klik header `Active` satu kali
16. Klik `[Clear Field]` lalu `[Apply]`
17. Verifikasi Search `Budi` dan Sort kolom `Active` tetap berlaku setelah Clear Field pada Filter
18. Buka dropdown Status, centang `Active`, klik `[Apply]`
19. Kosongkan isi kotak search, tekan Enter
20. Verifikasi Filter Status `Active` dan Sort kolom `Active` tetap berlaku setelah Search dikosongkan
21. Ketik Search `Budi`, tekan Enter
22. Klik header `Name` satu kali
23. Verifikasi sort berpindah ke kolom `Name` tanpa mereset Search `Budi` dan Filter Status `Active`
24. Ganti isi kotak search dengan `zzzzqx`, tekan Enter
25. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
26. Klik `(←)` pada kotak Search
27. Verifikasi baris yang cocok dengan Filter Status `Active` pulih di tabel
28. Klik header `Name` dua kali lagi hingga sort netral, lalu klik `[Clear Field]` dan `[Apply]` pada panel Filter

### TC-FA-SU-348: Perilaku Filter Panel

29. Buka dropdown Division, centang `Logistics` tanpa `[Apply]`
30. Klik di luar panel Filter
31. Klik icon Filter
32. Verifikasi field Division kosong (nilai ter-Apply terakhir) pada panel yang dibuka lagi
33. Verifikasi tabel tidak berubah dan tidak tersaring
34. Centang `Logistics` pada Division, klik `[Apply]`
35. Klik icon Filter hingga panel tertutup
36. Verifikasi ikon Filter menampilkan badge titik saat panel tertutup
37. Klik icon Filter
38. Verifikasi ikon Filter menampilkan badge titik saat panel terbuka
39. Buka dropdown Division
40. Verifikasi dropdown Division tidak memiliki opsi untuk nilai kosong
41. Verifikasi tabel menampilkan sedikitnya satu baris
42. Verifikasi seluruh baris hasil ber-Division `Logistics` (baris ber-Division kosong tidak tampil)
43. Klik header ⋯, hapus centang `Division`
44. Verifikasi field Division tetap ada pada panel Filter
45. Verifikasi filter Division `Logistics` yang ter-Apply tetap berlaku
46. Klik header ⋯, centang kembali `Division`
47. Klik `[Clear Field]` lalu `[Apply]`
48. Verifikasi badge titik pada ikon Filter hilang

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (pindah ke halaman 2 agar kembali ke halaman 1 dapat diasersi, S-14), 7, 12, 28 (membersihkan Filter, Search, dan Sort, S-09), dan 21 (mengaktifkan Search lagi agar Expected c TC-FA-SU-347 bermakna).
- Temuan untuk QA (S-15): (1) TC-FA-SU-347 langkah 5 tidak menyebut kolom sort tujuan dan Search yang aktif; spec mengganti sort ke `Name` dan mengaktifkan Search `Budi` lagi pada langkah 21. Keyword tanpa hasil pada langkah 6 tidak disebut TC (spec: `zzzzqx`). (2) TC-FA-SU-348 tidak menyebut opsi yang dipilih (langkah 2) dan kolom yang di-hide (langkah 5); spec memakai Division `Logistics`. Expected c TC-FA-SU-348 (menyaring keluar baris bernilai kosong) tidak menyebut pengguna ber-Division kosong sehingga hanya hasil `Logistics` yang diasersi. (3) TC-FA-SU-346 tidak menyebut adanya langkah menuju halaman 2; asersi kembali ke halaman 1 memakai langkah penghubung.
- Alasan di atas sekitar 35 langkah: ketiga TC berkelas fungsional sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; setiap TC memuat banyak klausa Expected yang masing-masing satu `Verifikasi` (S-01) dan bagian 3 konvensi menetapkan Search, Filter, Sort tetap satu spec selama dataset dan harness sama; blok berdiri sendiri karena tiap TC mengawali dari kontrol yang dibersihkan.
