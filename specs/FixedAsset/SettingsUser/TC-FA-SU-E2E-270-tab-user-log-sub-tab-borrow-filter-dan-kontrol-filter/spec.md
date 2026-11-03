---
id: TC-FA-SU-E2E-270-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter
title: "Tab User Log sub-tab Borrow: Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-818
  - TC-FA-SU-819
  - TC-FA-SU-820
  - TC-FA-SU-821
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-818: Filter kelas enum, kolom Activity

2. Klik icon Filter, lalu buka dropdown `Activity`
3. Verifikasi opsi dropdown = DISTINCT data tabel: `Borrowed`, `Returned`
4. Centang `Borrowed`
5. Klik `[Apply]`
6. Verifikasi tabel menyisakan `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Borrowed|BRW-20260205-0102` (3 baris)
7. Verifikasi chip `Borrowed` tampil di dalam field `Activity`
8. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`

### TC-FA-SU-819: Filter kelas fk, kolom PIC

9. Buka dropdown `PIC`
10. Verifikasi opsi dropdown = DISTINCT data tabel: `Ahmad D`, `Citra L`
11. Centang `Ahmad D`
12. Klik `[Apply]`
13. Verifikasi tabel menyisakan `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`, `Borrowed|BRW-20260205-0102` (5 baris)
14. Verifikasi chip `Ahmad D` tampil di dalam field `PIC`
15. Klik `[Clear Field]` pada field `PIC`, lalu klik `[Apply]`

### TC-FA-SU-820: Kombinasi Search dan Filter dua arah

16. Verifikasi tabel menampilkan enam baris
17. Ketik Search `Returned`, tekan Enter
18. Buka dropdown `Activity`, lalu centang `Borrowed`
19. Klik `[Apply]`
20. Verifikasi irisan Search `Returned` dan Filter Activity `Borrowed` tidak menyisakan baris (0 baris)
21. Verifikasi kotak Search tetap berisi `Returned` setelah Filter diterapkan
22. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
23. Kosongkan isi kotak search, tekan Enter
24. Buka dropdown `Activity`, lalu centang `Borrowed`
25. Klik `[Apply]`
26. Ketik Search `Returned`, tekan Enter
27. Verifikasi irisan Filter Activity `Borrowed` dan Search `Returned` tidak menyisakan baris (0 baris), identik dengan urutan sebelumnya
28. Verifikasi chip `Borrowed` tetap tampil di field `Activity` setelah Search dijalankan
29. Verifikasi tabel berada di halaman 1
30. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
31. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-821: Pelepasan kontrol (Clear Field, Clear Search, ganti kolom sort, dan recovery empty state)

32. Ketik Search `Returned`, tekan Enter
33. Buka dropdown `Activity`, lalu centang `Borrowed`
34. Klik `[Apply]`
35. Klik header `Date` satu kali
36. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
37. Verifikasi Search `Returned` tetap berlaku (tabel menyisakan `Returned|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102`)
38. Verifikasi Sort pada kolom `Date` tetap berlaku (icon sort ascending (↑) pada header `Date`)
39. Buka dropdown `Activity`, lalu centang `Borrowed`
40. Klik `[Apply]`
41. Kosongkan isi kotak search, tekan Enter
42. Verifikasi Filter Activity `Borrowed` tetap berlaku (tabel menyisakan `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Borrowed|BRW-20260205-0102`)
43. Verifikasi Sort pada kolom `Date` tetap berlaku
44. Klik header `Name` satu kali
45. Verifikasi sort pindah ke kolom `Name` (icon sort ascending (↑) pada header `Name`)
46. Verifikasi Filter Activity `Borrowed` tetap berlaku (tabel menyisakan `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Borrowed|BRW-20260205-0102`)
47. Ketik Search `zzzz`, tekan Enter
48. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
49. Kosongkan isi kotak search, tekan Enter
50. Verifikasi tabel kembali menyisakan `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Borrowed|BRW-20260205-0102`
51. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
52. Klik header `Name` dua kali lagi hingga sort kembali netral
53. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), semua `[Clear Field]` lalu `[Apply]`, pengosongan Search, pemulihan sort, dan penutupan panel Filter; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- `Verifikasi` enam baris di awal TC-FA-SU-820 adalah anchor positif untuk asersi "0 baris" (bagian 8b butir 2); asersi itu tambahan atas Expected TC dan dicatat di sini (S-03). Kata kunci tanpa hasil `zzzz` pada TC-FA-SU-821 dipilih spec karena TC tidak menyebut nilainya.
- Panel Filter diasumsikan tetap terbuka sesudah `[Apply]` (mengikuti urutan langkah TC-FA-SU-820).
- Temuan untuk QA (S-15): (1) TC-FA-SU-821 Langkah Uji nomor 5 meminta mengganti sort "tanpa mereset Search dan Filter", tetapi Search sudah dikosongkan pada langkah sebelumnya; spec hanya mengasersi Filter tetap berlaku. (2) TC-FA-SU-820 butir d "Tabel kembali ke halaman 1" tidak dapat dibuktikan pada fixture satu halaman; spec mengasersi tabel berada di halaman 1. (3) TC-FA-SU-818 dan TC-FA-SU-819 tidak memiliki langkah pemulihan filter; spec menambahkan `[Clear Field]` lalu `[Apply]` sebagai langkah penghubung.
- Spec ini berjumlah 53 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
