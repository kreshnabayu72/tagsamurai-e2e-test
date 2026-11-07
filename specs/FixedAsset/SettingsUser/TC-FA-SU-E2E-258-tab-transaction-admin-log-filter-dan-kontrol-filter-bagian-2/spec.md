---
id: TC-FA-SU-E2E-258-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-2
title: "Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-779
  - TC-FA-SU-780
  - TC-FA-SU-781
coverage:
  web: automated
---

# Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps


### TC-FA-SU-779: Kombinasi Search dan Filter dua arah

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment
2. Verifikasi tabel menampilkan lima baris
3. Ketik Search `0313`, tekan Enter
4. Klik icon Filter, buka dropdown `Group`, lalu centang `Branch Surabaya`
5. Klik `[Apply]`
6. Verifikasi irisan Search `0313` dan Filter Group `Branch Surabaya` tidak menyisakan baris (0 baris)
7. Verifikasi kotak Search tetap berisi `0313` setelah Filter diterapkan
8. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
9. Kosongkan isi kotak search, tekan Enter
10. Buka dropdown `Group`, lalu centang `Branch Surabaya`
11. Klik `[Apply]`
12. Ketik Search `0313`, tekan Enter
13. Verifikasi irisan Filter Group `Branch Surabaya` dan Search `0313` tidak menyisakan baris (0 baris), identik dengan urutan sebelumnya
14. Verifikasi chip `Branch Surabaya` tetap tampil di field `Group` setelah Search dijalankan
15. Verifikasi tabel berada di halaman 1
16. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
17. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-780: Pelepasan kontrol (Clear Field, Clear Search, ganti kolom sort, dan recovery empty state)

18. Ketik Search `0313`, tekan Enter
19. Buka dropdown `Group`, lalu centang `Branch Surabaya`
20. Klik `[Apply]`
21. Klik header `Transaction ID` satu kali
22. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
23. Verifikasi Search `0313` tetap berlaku (tabel menyisakan `BRW-20260715-0313`)
24. Verifikasi Sort pada kolom `Transaction ID` tetap berlaku (icon sort ascending (↑) pada header)
25. Buka dropdown `Group`, lalu centang `Branch Surabaya`
26. Klik `[Apply]`
27. Kosongkan isi kotak search, tekan Enter
28. Verifikasi Filter Group `Branch Surabaya` tetap berlaku (tabel menyisakan `BRW-20260716-0314`)
29. Verifikasi Sort pada kolom `Transaction ID` tetap berlaku
30. Klik header `Date` satu kali
31. Verifikasi sort pindah ke kolom `Date` (icon sort ascending (↑) pada header `Date`)
32. Verifikasi Filter Group `Branch Surabaya` tetap berlaku (tabel menyisakan `BRW-20260716-0314`)
33. Ketik Search `zzzz`, tekan Enter
34. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
35. Kosongkan isi kotak search, tekan Enter
36. Verifikasi tabel kembali menyisakan `BRW-20260716-0314`
37. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
38. Klik header `Date` dua kali untuk mengembalikan sort ke default

### TC-FA-SU-781: Perilaku Filter Panel (tutup tanpa Apply, indikator titik, dan nilai kosong)

39. Buka dropdown `Group`, lalu centang `Branch Surabaya` tanpa klik `[Apply]`
40. Klik di luar panel Filter
41. Klik icon Filter untuk membuka panel
42. Verifikasi field `Group` tidak berisi pilihan (nilai ter-Apply terakhir: kosong)
43. Verifikasi tabel tidak berubah dan menampilkan lima baris
44. Buka dropdown `Group`, lalu centang `Branch Surabaya`
45. Klik `[Apply]`
46. Verifikasi icon Filter menampilkan badge titik saat panel terbuka
47. Klik icon Filter untuk menutup panel
48. Verifikasi icon Filter menampilkan badge titik saat panel tertutup
49. Klik icon Filter untuk membuka panel
50. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
51. Verifikasi badge titik pada icon Filter hilang
52. Buka dropdown `Group`
53. Verifikasi dropdown `Group` memuat opsi data: `Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`
54. Verifikasi dropdown `Group` tidak memiliki opsi untuk nilai kosong
55. Centang `Branch Surabaya`
56. Klik `[Apply]`
57. Klik header `⋯`, hilangkan centang `Group`, lalu tutup overlay dengan Esc
58. Verifikasi field `Group` tetap ada pada panel Filter
59. Verifikasi Filter Group `Branch Surabaya` tetap berlaku (tabel menyisakan `BRW-20260716-0314`)
60. Klik header `⋯`, beri centang `Group`, lalu tutup overlay dengan Esc
61. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
62. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), semua `[Clear Field]` lalu `[Apply]`, pengosongan Search, pemulihan sort, penutupan overlay dan panel Filter (S-09).
- `Verifikasi` tabel lima baris di awal TC-FA-SU-779 adalah anchor positif untuk asersi "0 baris" (bagian 8b butir 2); asersi itu tambahan atas Expected TC dan dicatat di sini (S-03). Kata kunci tanpa hasil `zzzz` pada TC-FA-SU-780 dipilih spec karena TC tidak menyebut nilainya.
- Temuan untuk QA (S-15): (1) TC-FA-SU-780 meminta mengganti sort "tanpa mereset Search dan Filter", tetapi Search sudah dikosongkan pada langkah sebelumnya; spec hanya mengasersi Filter tetap berlaku. (2) TC-FA-SU-779 butir d "Tabel kembali ke halaman 1" tidak dapat dibuktikan pada fixture satu halaman; spec mengasersi tabel berada di halaman 1. (3) TC-FA-SU-781 butir c menyebut "menyaring keluar baris yang nilainya kosong", tetapi seed #29 tidak memiliki nilai kosong; hanya ketiadaan opsi nilai kosong yang diasersi. (4) TC-FA-SU-781 butir a tidak menyebut cara mengasersi "nilai ter-Apply terakhir"; spec mengasersi field `Group` kosong karena belum ada filter ter-Apply.
- Spec ini berjumlah 62 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Langkah 53 (`Verifikasi` dropdown `Group` memuat opsi data) adalah asersi tambahan di luar Expected TC-FA-SU-781 dan menjadi anchor positif untuk asersi absence opsi nilai kosong pada langkah 54 (bagian 8b butir 2, S-03).
