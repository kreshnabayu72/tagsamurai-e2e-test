---
id: TC-FA-SU-E2E-154-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-2
title: "Sub-tab Assigned Assets: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-453
  - TC-FA-SU-454
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-453: Kombinasi Search dan Filter Sub-tab Assigned Assets dua arah

1. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Ketik Search `Printer`, tekan Enter
4. Klik icon Filter
5. Buka dropdown Name
6. Centang `AC Split Ruang Kerja`
7. Klik `[Apply]`
8. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
9. Verifikasi hasil irisan Search lalu Filter tidak ada baris (0 baris)
10. Verifikasi keyword Search `Printer` tetap terisi setelah Filter di-Apply
11. Verifikasi tabel berada di halaman 1
12. Klik `[Clear Field]`
13. Klik `[Apply]`
14. Klik `(←)` pada kotak Search
15. Buka dropdown Name
16. Centang `AC Split Ruang Kerja`
17. Klik `[Apply]`
18. Ketik Search `Printer`, tekan Enter
19. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
20. Verifikasi hasil Filter lalu Search identik, tidak ada baris
21. Verifikasi chip Filter `AC Split Ruang Kerja` tetap berlaku setelah Search dijalankan
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Klik `(←)` pada kotak Search
25. Klik icon Filter untuk menutup panel

### TC-FA-SU-454: Pelepasan kontrol Sub-tab Assigned Assets: Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

26. Ketik Search `Printer`, tekan Enter
27. Klik icon Filter
28. Buka dropdown Name
29. Centang `AC Split Ruang Kerja`
30. Klik `[Apply]`
31. Klik header Name
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Verifikasi Search `Printer` tetap berlaku
35. Verifikasi Sort kolom Name tetap berlaku
36. Buka dropdown Name
37. Centang `AC Split Ruang Kerja`
38. Klik `[Apply]`
39. Kosongkan isi kotak search, tekan Enter
40. Verifikasi Filter Name `AC Split Ruang Kerja` tetap berlaku
41. Verifikasi Sort kolom Name tetap berlaku
42. Ketik Search `Printer`, tekan Enter
43. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
44. Klik header Brand
45. Verifikasi sort pindah ke kolom Brand
46. Verifikasi keyword Search `Printer` tidak direset
47. Verifikasi chip Filter `AC Split Ruang Kerja` tidak direset
48. Klik `(←)` pada kotak Search
49. Verifikasi baris yang cocok dengan Filter kembali tampil, yaitu `AC Split Ruang Kerja`
50. Klik `[Clear Field]`
51. Klik `[Apply]`
52. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): Search nama `Budi Santoso` serta pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Nilai Search `Printer` dan Filter Name `AC Split Ruang Kerja` mengikuti Data Uji TC; kombinasinya menghasilkan 0 baris (irisan kosong), sehingga asersi "tidak ada baris" didahului `Verifikasi` empty state sebagai anchor positif (bagian 8b butir 2; langkah 8 dan 19, asersi tambahan di luar Expected TC-FA-SU-453, S-03).
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (52 langkah, 52 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-451 dan 452 ada di spec 153; TC-FA-SU-455 ada di spec 169.
- Temuan untuk QA (S-15):
  - TC-FA-SU-454 Expected c ("mengganti kolom sort saat Search dan Filter aktif") dan Langkah Uji 4 ("kosongkan Search") tidak konsisten: Search dikosongkan sebelum sort diganti. Spec mengaktifkan Search dan Filter lagi sebelum mengganti sort; kombinasi itu 0 baris, sehingga pemindahan sort teramati dari indikator header, bukan dari urutan baris.
  - TC-FA-SU-453 Expected d ("tabel kembali ke halaman 1") tidak dapat dibedakan pada fixture satu halaman; spec mengasersi tabel berada di halaman 1.
