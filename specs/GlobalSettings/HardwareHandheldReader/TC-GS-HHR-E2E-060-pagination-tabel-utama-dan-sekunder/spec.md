---
id: TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder
title: "Pagination Tabel Utama dan Sekunder Handheld Reader: Navigasi, Rows per Page, Input Halaman, Reset ke Halaman 1, Sort, dan Hapus Baris Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-317
  - TC-GS-HHR-318
  - TC-GS-HHR-319
  - TC-GS-HHR-320
  - TC-GS-HHR-321
  - TC-GS-HHR-322
  - TC-GS-HHR-323
  - TC-GS-HHR-324
  - TC-GS-HHR-325
coverage:
  web: automated
---

# Pagination Tabel Utama dan Sekunder Handheld Reader: Navigasi, Rows per Page, Input Halaman, Reset ke Halaman 1, Sort, dan Hapus Baris Terakhir

## Prerequisites

- Mode: FE+BE (backend nyata). Spec membaca pagination dan satu aksi Delete di akhir spec; Delete memakai Client L2 yang khusus untuk uji ini.
- Akun aktor hook `before`: Total Control Client L, `totalControl_automated_{namaClient}@qwertysystem.net` dengan namaClient Client L; email persisnya tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTL_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik suite). Password tidak ditulis di spec atau fixture.
- Akun kedua (langkah 48 sampai 50, TC-GS-HHR-325): Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`.
- Akun ketiga (langkah 58 sampai 60, TC-GS-HHR-324): Total Control Client L2, `totalControl_automated_{namaClient}@qwertysystem.net` dengan namaClient Client L2; email persisnya disediakan tim FE; password `Spectra.env.GS_CLIENTL2_TC_PASSWORD` (nama env baru; didaftarkan oleh pemilik suite). Hook `after` mengembalikan sesi ke akun default suite.
- Environment variable: `GS_CLIENTL_TC_PASSWORD`, `GS_TC_PASSWORD`, `GS_CLIENTL2_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader pada akun aktif; spec mengulang langkah buka hanya sesudah ganti akun.
- Data: Client L memiliki 26 reader `Large Reader - 1` sampai `Large Reader - 26`, Rows per page awal 10, sehingga halaman 3 berisi 6 baris (N total 26 dari seeding). Client A memiliki Seed Reader A, Seed Usage Event reader DD-01, Seed Changelog Client A, dan Seed Event Log Client A (dipakai sebagai precondition TC, tidak diasersi; hanya footer yang diasersi). Client L2 memiliki 21 reader sehingga halaman 3 berisi 1 baris. Kondisi data Client L dan L2 (jumlah reader, Status `Available` untuk Filter) disediakan tim FE dan dipulihkan oleh fixture backend sebelum tiap eksekusi.
- Data uji surface (TC-GS-HHR-325; perulangan per baris tabel, langkah 51 sampai 57, 4 iterasi):

| Surface | Cara buka |
|---|---|
| `Modal Changelog` | Klik ikon Changelog |
| `Tab Usage Popup Detail` | Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`) lalu pilih tab `Usage` |
| `Popup Event Log Activate` | Klik ikon Event Log |
| `Tab Changelog Popup Detail` | Klik `Device Name` baris DD-03 (Serial Number `SN-HHR-00103`) lalu pilih tab `Changelog` |

- Data uji lain: nomor halaman `3` dan `1` (TC-GS-HHR-319); `<Nilai>` pada TC-GS-HHR-320 berturut-turut `0`, `99`, `abc` (perulangan langkah 20 sampai 21, 3 iterasi); Search `Large Reader` dan Filter `Status` = `Available` (TC-GS-HHR-322); header `Serial Number` (TC-GS-HHR-323).
- Kemampuan teknis: mengisi dan mengirim input nomor halaman (termasuk nilai non-angka); membaca teks footer pagination.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun Client L, Client A, dan Client L2; spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: Rows per page dikembalikan ke 10 (langkah penghubung sesudah TC-GS-HHR-318 dan 321), Search, Filter, dan Sort dikosongkan sesudah TC-GS-HHR-322 dan 323; data Client L2 (satu reader dihapus pada langkah 64) dipulihkan ke 21 reader oleh fixture backend di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-HHR-317: Pagination default dan navigasi halaman

1. Verifikasi footer menampilkan `Showing 1 - 10 of 26 readers`
2. Verifikasi footer menampilkan `Rows per page: 10`
3. Klik halaman berikutnya
4. Klik halaman berikutnya
5. Verifikasi halaman 3 menampilkan `Showing 21 - 26 of 26 readers`
6. Verifikasi halaman 3 menampilkan 6 baris
7. Klik halaman sebelumnya
8. Verifikasi tabel kembali ke halaman 2 (nomor halaman aktif 2)
9. Klik halaman sebelumnya (kembali ke halaman 1)

### TC-GS-HHR-318: Opsi Rows per page 10/25/50/100 tanpa opsi All

10. Buka Overlay Page Size
11. Verifikasi opsi Rows per page `10`, `25`, `50`, `100`
12. Verifikasi tidak ada opsi `All`
13. Pilih `25`
14. Verifikasi footer menampilkan `Showing 1 - 25 of 26 readers`
15. Buka Overlay Page Size
16. Pilih `10` (pemulihan Rows per page)

### TC-GS-HHR-319: Input nomor halaman langsung dengan Enter

17. Isi input nomor halaman dengan `3`, tekan Enter
18. Verifikasi tabel pindah ke halaman 3 (`Showing 21 - 26 of 26 readers`)
19. Isi input nomor halaman dengan `1`, tekan Enter (kembali ke halaman 1)

### TC-GS-HHR-320: Input nomor halaman tidak valid diabaikan

20. Isi input nomor halaman dengan `<Nilai>`, tekan Enter
21. Verifikasi input `<Nilai>` diabaikan dan tabel tetap di halaman 1 (`Showing 1 - 10 of 26 readers`)

### TC-GS-HHR-321: Mengganti Rows per page kembali ke halaman 1

22. Isi input nomor halaman dengan `3`, tekan Enter (pindah ke halaman 3)
23. Buka Overlay Page Size
24. Pilih `25`
25. Verifikasi tabel menampilkan halaman 1 (`Showing 1 - 25 of 26 readers`)
26. Buka Overlay Page Size
27. Pilih `10` (pemulihan Rows per page)

### TC-GS-HHR-322: Search dan Apply Filter mereset ke halaman 1

28. Isi input nomor halaman dengan `3`, tekan Enter (pindah ke halaman 3)
29. Ketik Search `Large Reader`, tekan Enter
30. Verifikasi tabel berada di halaman 1 setelah Search
31. Isi input nomor halaman dengan `3`, tekan Enter (pindah ke halaman 3 lagi)
32. Klik ikon Filter
33. Pilih `Available` pada field `Status`
34. Klik `[Apply]`
35. Verifikasi tabel berada di halaman 1 setelah Apply Filter
36. Klik `[Clear Field]` pada panel Filter
37. Klik `[Apply]`
38. Klik ikon Filter untuk menutup panel
39. Klik ikon panah `(←)` pada search box

### TC-GS-HHR-323: Mengganti sort mempertahankan nomor halaman

40. Klik halaman berikutnya (pindah ke halaman 2)
41. Klik header `Serial Number`
42. Verifikasi tabel tetap di halaman 2
43. Verifikasi tabel menampilkan sedikitnya dua baris pembanding pada halaman 2
44. Verifikasi baris pada halaman 2 terurut Serial Number Ascending
45. Klik header `Serial Number` kali kedua
46. Klik header `Serial Number` kali ketiga (reset sort)
47. Klik halaman sebelumnya (kembali ke halaman 1)

### TC-GS-HHR-325: Pagination default dan opsi pada tabel sekunder

48. Logout
49. Login sebagai Total Control Client A (`totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`)
50. Buka Global Settings > Hardware > Handheld Reader
51. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Data uji surface)
52. Verifikasi footer surface `<Surface>` menampilkan default 10 per halaman
53. Buka Overlay Page Size pada footer surface
54. Verifikasi opsi Rows per page `10`, `25`, `50`, `100`
55. Verifikasi tidak ada opsi `All`
56. Tekan `Esc` (tutup overlay)
57. Tutup surface `<Surface>`

### TC-GS-HHR-324: Menghapus baris terakhir di halaman terakhir memindahkan tabel ke halaman terakhir yang ada

58. Logout
59. Login sebagai Total Control Client L2 (`totalControl_automated_{namaClient}@qwertysystem.net` dengan namaClient Client L2, `Spectra.env.GS_CLIENTL2_TC_PASSWORD`)
60. Buka Global Settings > Hardware > Handheld Reader
61. Isi input nomor halaman dengan `3`, tekan Enter (pindah ke halaman 3; halaman 3 berisi 1 baris)
62. Buka Overlay row action baris tunggal pada halaman 3 (klik ikon `(⋯)` pada baris)
63. Klik `Delete`
64. Klik `[Delete]` pada dialog
65. Verifikasi tabel berpindah ke halaman 2 (`Showing 11 - 20 of 20 readers`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`, section 4a-6.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 317 sampai 323 (Client L, tanpa mengubah data), TC-GS-HHR-325 (ganti akun ke Client A), dan TC-GS-HHR-324 di paling akhir (ganti akun ke Client L2) karena Delete menghapus data. Urutan di `tc-hardware-handheld-reader.md`: 317 sampai 325.
- Langkah penghubung (aksi tanpa `Verifikasi`): kembali ke halaman 1 dan pemulihan Rows per page ke 10 antar blok; mengosongkan Filter (`[Clear Field]`, `[Apply]`, tutup panel) dan Search (`(←)`) sesudah TC-GS-HHR-322; reset sort lewat klik ketiga header `Serial Number` sesudah TC-GS-HHR-323; tutup overlay dengan `Esc` dan tutup surface pada tiap iterasi TC-GS-HHR-325; logout, login, dan membuka halaman pada langkah 48 sampai 50 dan 58 sampai 60.
- Langkah yang diulang per baris tabel Prerequisites (idiom "Untuk setiap baris tabel"): langkah 20 sampai 21 (3 nilai input) dan 51 sampai 57 (4 surface). Tiap `Verifikasi` yang diulang tetap satu per klausa.
- Spec memuat 65 langkah nominal (sekitar 90 langkah dengan ekspansi blok ulang; di atas smell sekitar 35 langkah). Alasan: seluruhnya topik Pagination satu dataset per akun, tanpa mengubah data kecuali Delete di akhir; ada dua Step ganti akun eksplisit (Client A, lalu Client L2) dan bagian sesudah tiap ganti akun tetap bermakna walau bagian sebelumnya gagal keras (prinsip 3, pemisah "Beda akun" butir b). Blok TC-GS-HHR-317 sampai 323 memulihkan Rows per page, Search, Filter, dan Sort sebelum blok berikutnya.
- Pembagian TC lintas spec: pagination yang dikombinasikan dengan Search, Filter, Sort, retensi, dan empty state (TC-GS-HHR-18, 19, 260 sampai 268) ada di spec 054; Setup Column di spec 055 dan 056; Download di spec 057 sampai 059.
- Temuan untuk QA:
  - TC-GS-HHR-317: Expected c ("Halaman sebelumnya kembali ke halaman 2") tidak menyebut teks footer halaman 2; spec mengasersi nomor halaman aktif 2.
  - TC-GS-HHR-318: TC tidak menyebut cara membuka Overlay Page Size; spec memakai kontrol `Rows per page` pada footer. TC tidak menyebut apakah pilihan Rows per page bertahan antar TC; spec memulihkan ke 10 dengan langkah penghubung.
  - TC-GS-HHR-320: nilai `abc` mungkin tidak dapat diketik bila input berjenis angka; TC tidak menyebut jenis input. Spec mengikuti TC (mengisi `abc` dan mengasersi diabaikan), kemampuan mengirim nilai non-angka disediakan tim FE.
  - TC-GS-HHR-322: Status reader Client L tidak disebut; Filter `Status` = `Available` mengasumsikan sedikitnya satu reader `Available` (jika tidak ada hasil, tabel menampilkan empty state dan asersi "halaman 1" tidak bermakna). Email akun Client L dan L2 tidak tertulis di Pre-setup TC dan env var passwordnya belum terdaftar; spec memakai `GS_CLIENTL_TC_PASSWORD` dan `GS_CLIENTL2_TC_PASSWORD` (env baru).
  - TC-GS-HHR-323: nilai Serial Number reader Client L tidak disebut; spec mengasersi urutan Ascending secara relatif pada baris halaman 2.
  - TC-GS-HHR-324: Status reader pada baris tunggal halaman 3 tidak disebut sehingga eligibility Delete tidak pasti; aksi Delete memakai data Client L2 yang khusus untuk TC ini (bukan data Pre-setup bersama) dan dipulihkan fixture backend. Expected tidak menyebut toast sukses Delete, sehingga tidak diasersi.
  - TC-GS-HHR-325: Expected "default 10 per halaman" tidak menyebut teks footer pada tabel sekunder; spec mengasersi nilai default 10 per halaman tanpa teks persis.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.
