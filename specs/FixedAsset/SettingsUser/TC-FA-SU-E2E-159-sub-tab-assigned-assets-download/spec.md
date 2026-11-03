---
id: TC-FA-SU-E2E-159-sub-tab-assigned-assets-download
title: "Sub-tab Assigned Assets: Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-464
  - TC-FA-SU-465
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Download

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
- Kemampuan teknis (disediakan tim FE): menangkap unduhan browser dan membaca isi berkas CSV/XLSX yang terunduh (nama berkas, header kolom, baris).

## Test Steps

### TC-FA-SU-464: Download Sub-tab Assigned Assets: format CSV dan XLSX, nama file, dan tanpa toast sukses

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Hover icon Download
4. Verifikasi tooltip `Download` tampil
5. Klik icon Download
6. Verifikasi overlay Download menampilkan `Download as CSV` dan `Download as XLSX`
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Assigned-Assets-Budi-Santoso.csv` terunduh
10. Klik icon Download
11. Pilih `Download as XLSX`
12. Verifikasi berkas `Assigned-Assets-Budi-Santoso.xlsx` terunduh
13. Verifikasi CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
15. Verifikasi XLSX berisi satu sheet bernama `Sheet1`

### TC-FA-SU-465: Cakupan baris dan kolom Download Sub-tab Assigned Assets: Search, Filter, Sort, dan Column Visibility

16. Klik icon Download
17. Pilih `Download as CSV`
18. Verifikasi berkas memuat seluruh baris tabel, yaitu lima baris Pre-setup, bukan hanya halaman aktif
19. Verifikasi urutan baris berkas mengikuti sort aktif (default)
20. Ketik Search `Printer`, tekan Enter
21. Klik icon Filter
22. Buka dropdown PIC
23. Centang `Citra L`
24. Klik `[Apply]`
25. Klik icon Download
26. Pilih `Download as CSV`
27. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter, yaitu `Printer Multifungsi` (1 baris)
28. Klik header Actions (⋯)
29. Uncheck kolom `Brand` pada overlay Column Visibility
30. Klik icon Download
31. Pilih `Download as CSV`
32. Verifikasi tidak ada toast peringatan
33. Verifikasi kolom `Brand` tidak ikut berkas
34. Klik header Actions (⋯)
35. Check kolom `Brand` pada overlay Column Visibility
36. Klik icon Download
37. Pilih `Download as CSV`
38. Verifikasi tidak ada toast peringatan
39. Verifikasi kolom `Brand` ikut kembali pada berkas
40. Ganti isi kotak search dengan `zzz-tidak-ada`, tekan Enter
41. Verifikasi empty state `No results found` tampil
42. Klik icon Download
43. Pilih `Download as CSV`
44. Verifikasi tidak ada toast
45. Verifikasi berkas hanya memuat baris header kolom yang visible
46. Klik `(←)` pada kotak Search
47. Klik icon Filter
48. Klik `[Clear Field]`
49. Klik `[Apply]`
50. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Asersi "tidak ada toast" diletakkan tepat sesudah pemicu `Pilih Download as CSV` dan sebelum asersi berkas (bagian 8b butir 11).
- Nilai Search `Printer`, Filter PIC `Citra L`, kolom yang di-hide `Brand`, dan keyword tanpa hasil `zzz-tidak-ada` dipilih spec karena TC-FA-SU-465 tidak menyebut nilainya (kombinasi menyisakan satu baris).
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (50 langkah, 50 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets (Download), satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-466 (transformasi data) ada di spec 370; TC-FA-SU-467 (kegagalan unduhan) ada di spec 366.
- Temuan untuk QA (S-15):
  - TC-FA-SU-464 Expected d (BOM UTF-8, tanda kutip ganda, sheet `Sheet1`) berkelas harness binary buffer (kelas f, HINT f pada indeks) tetapi satu TC tetap satu spec; spec mengasersinya di sini dan klausa itu perlu keputusan pemilik proses (pindah ke spec kelas f). Data Pre-setup #24 juga tidak memuat nilai ber-koma, tanda kutip, atau baris baru, sehingga klausa pembungkus tanda kutip ganda tidak dapat dibuktikan dengan data ini.
  - TC-FA-SU-465 Expected a ("seluruh baris, bukan hanya halaman aktif") tidak dapat dibedakan pada fixture satu halaman.
