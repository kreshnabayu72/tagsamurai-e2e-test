---
id: TC-FA-LIC-E2E-093-group-license-allocation-paginasi-dan-kombinasi-search
title: "Group License Allocation: Kombinasi Search, Filter, Sort, dan Page Size serta Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-323
  - TC-FA-LIC-324
  - TC-FA-LIC-325
  - TC-FA-LIC-326
coverage:
  web: automated
---

# Group License Allocation: Kombinasi Search, Filter, Sort, dan Page Size serta Paginasi

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup (identitas dan nilai dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki`, belum ada, disiapkan tim FE; nilai pada langkah adalah nilai fixture itu):
  - Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`; diperlukan TC-FA-LIC-326): client Paid Pre-setup #1 dengan `License allocation per group` ON; tabel Group License Allocation pada node All Groups menampilkan empat baris level 1: Produksi (Used 1450), Cabang Medan (Used 880), Cabang Surabaya (Used di atas 700), Kantor Pusat (Used 700); kode grup berawalan `GRP-`.
  - Pre-setup #41 (hierarki paginasi T-FALIC-03; diperlukan TC-FA-LIC-323, 324, 325): Pre-setup #12 ditambah 9 grup child fixture tanpa alokasi (Used 0, Reserved 0, Group Code berawalan `GRP-`) di bawah Kantor Pusat, sehingga Kantor Pusat memiliki 12 child langsung (Divisi Logistik, Divisi IT, Divisi Keuangan, dan 9 grup fixture); node `All Groups` tetap empat grup level 1; Allocated to Subgroups dan Remaining Kantor Pusat tidak berubah. Penerapan lewat langkah penghubung (langkah 41) dan pemulihan ke Pre-setup #12 di hook `after` mengikuti pernyataan fixture BE pemulih Pre-setup #12 di `suite.md` (disediakan tim FE/BE).
  - Test Data TC-FA-LIC-325 (nilai TC): Search `GRP-` (hasil lebih dari 10 baris) dan Filter `Used by This Group` Min `0`, Max `1000`.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12.
- Kemampuan teknis (disediakan tim FE): mengirim tombol `Esc` ke browser (langkah 48).

## Test Steps

### TC-FA-LIC-326: Kombinasi Search, Filter, Sort, dan paginasi bekerja bersamaan dan lepas secara independen

1. Klik tab Allocation Quota di node All Groups
2. Ketik Search `an`, tekan Enter
3. Verifikasi tabel menampilkan: Cabang Medan, Cabang Surabaya, Kantor Pusat
4. Verifikasi Produksi tidak tampil
5. Buka Filter Panel, isi `Allocated Quota` Min `1000` (Max dikosongkan), klik `[Apply]`
6. Verifikasi tabel menampilkan: Cabang Medan, Kantor Pusat
7. Verifikasi Filter Panel tetap terbuka
8. Klik header kolom `Remaining Quota` dua kali
9. Ubah page size menjadi `25`
10. Verifikasi tabel menampilkan: Kantor Pusat, Cabang Medan
11. Verifikasi indikator Descending pada `Remaining Quota`
12. Verifikasi page size 25
13. Verifikasi Search `an` tidak berubah
14. Verifikasi Filter `Allocated Quota` Min `1000` tidak berubah
15. Klik header kolom `Group Name` sekali
16. Verifikasi tabel menampilkan: Cabang Medan, Kantor Pusat
17. Verifikasi `Remaining Quota` kembali netral
18. Verifikasi indikator Ascending pada `Group Name`
19. Verifikasi Search `an` tidak berubah
20. Verifikasi Filter `Allocated Quota` Min `1000` tidak berubah
21. Pada Filter Panel yang masih terbuka, klik `[Clear Field]`, lalu klik `[Apply]`
22. Verifikasi tabel menampilkan: Cabang Medan, Cabang Surabaya, Kantor Pusat
23. Verifikasi Search `an` tetap aktif
24. Verifikasi Sort `Group Name` tetap aktif
25. Isi lagi `Allocated Quota` Min `1000`, klik `[Apply]`
26. Kosongkan isi kotak search, tekan Enter
27. Verifikasi tabel menampilkan: Cabang Medan, Kantor Pusat, Produksi
28. Verifikasi Cabang Surabaya tidak tampil
29. Verifikasi Filter tetap aktif
30. Verifikasi Sort `Group Name` Ascending tetap aktif
31. Ketik Search `Surabaya`, tekan Enter
32. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
33. Kosongkan isi kotak search, tekan Enter
34. Verifikasi tabel pulih otomatis menampilkan: Cabang Medan, Kantor Pusat, Produksi
35. Verifikasi Filter tetap aktif
36. Verifikasi Sort `Group Name` Ascending tetap aktif
37. Klik `[Clear Field]`, lalu klik `[Apply]`
38. Klik header kolom `Group Name` dua kali lagi hingga sort netral
39. Ubah page size menjadi `10`
40. Klik ikon Filter untuk menutup panel

### Pindah ke hierarki Pre-setup #41 dengan 12 child pada Kantor Pusat

41. Terapkan Pre-setup #41 (9 grup child fixture di bawah Kantor Pusat) lewat fixture BE hingga berhasil tersimpan
42. Klik menu License pada sidebar, lalu tab Allocation Quota di node All Groups
43. Klik node `Kantor Pusat` pada Sidebar

### TC-FA-LIC-323: Paginasi default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

44. Verifikasi footer menampilkan page size 10 secara default
45. Verifikasi halaman 1 menampilkan 10 dari 12 child
46. Buka pilihan page size
47. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
48. Tutup pilihan page size dengan Esc
49. Verifikasi page size tetap 10
50. Ketik nomor halaman `2` pada input nomor halaman, tekan Enter
51. Verifikasi input nomor halaman 2 langsung membuka halaman 2
52. Verifikasi halaman 2 menampilkan 2 baris (baris ke-11 dan ke-12)
53. Buka pilihan page size, lalu pilih `25`
54. Verifikasi seluruh 12 baris tampil dalam satu halaman
55. Verifikasi tabel kembali ke halaman 1

### TC-FA-LIC-324: Nomor halaman tidak valid diabaikan; ganti sort tetap di halaman sekarang; ganti page size ke halaman 1

56. Buka pilihan page size, pilih `10`, lalu pindah ke halaman 2
57. Ketik `0` pada input nomor halaman, tekan Enter
58. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2
59. Ketik `99` pada input nomor halaman, tekan Enter
60. Verifikasi input `99` diabaikan dan tabel tetap di halaman 2
61. Ketik `abc` pada input nomor halaman, tekan Enter
62. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2
63. Klik header kolom `Allocated Quota` untuk sort
64. Verifikasi mengganti sort tetap di halaman 2
65. Ganti page size menjadi `25`
66. Verifikasi mengganti page size kembali ke halaman 1
67. Klik header kolom `Allocated Quota` hingga sort netral

### TC-FA-LIC-325: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

68. Buka pilihan page size, pilih `10`, lalu pindah ke halaman 2
69. Ketik Search `GRP-`, tekan Enter
70. Verifikasi setelah Search tabel kembali ke halaman 1
71. Pindah ke halaman 2
72. Buka Filter Panel, isi `Used by This Group` Min `0` dan Max `1000`, klik `[Apply]`
73. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
74. Klik `[Clear Field]`, lalu klik `[Apply]`, dan kosongkan isi kotak search, tekan Enter

## Notes

- Langkah penghubung tanpa `Verifikasi`: memilih page size 10 dan pindah ke halaman 2 sebagai awal TC-FA-LIC-324 dan TC-FA-LIC-325, membersihkan Search, Filter, Sort, page size, dan panel di akhir blok (S-09), membuka node `Kantor Pusat`, dan blok "Pindah ke hierarki Pre-setup #41 dengan 12 child pada Kantor Pusat" (langkah 41 dan 42: menerapkan fixture lalu membuka ulang tab lewat sidebar yang mereset Search, Sort, dan Filter). Filter Panel tetap terbuka sesudah `[Apply]` (prd-conventions.md §9.8), sehingga mengubah Filter dari panel itu tidak didahului membuka panel.
- Spec di atas 35 langkah (74 langkah nominal). Alasan: seluruh blok adalah paginasi dan kombinasi kontrol satu tabel, kegagalan satu blok tidak membuat blok lain kehilangan makna, dan dua kumpulan data (Pre-setup #12 dan Pre-setup #41) dipakai berurutan dengan penerapan fixture eksplisit.
- Urutan TC dalam spec: 326, 323, 324, 325 (TC-FA-LIC-326 memakai Pre-setup #12; TC-FA-LIC-323, 324, dan 325 memakai Pre-setup #41 sehingga fixture diterapkan sesudah TC-FA-LIC-326).
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-324 kolom sort `Allocated Quota` dipilih spec (TC menulis "klik header kolom untuk sort").
- Temuan untuk QA: TC-FA-LIC-324 menyebut "kolom" sort tanpa nilai; spec memakai `Allocated Quota`. TC-FA-LIC-323, 324, 325, dan 326 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
