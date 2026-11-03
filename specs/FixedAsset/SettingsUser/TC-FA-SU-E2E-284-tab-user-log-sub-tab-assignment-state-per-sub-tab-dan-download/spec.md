---
id: TC-FA-SU-E2E-284-tab-user-log-sub-tab-assignment-state-per-sub-tab-dan-download
title: "Tab User Log sub-tab Assignment: State per Sub-tab dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-864
  - TC-FA-SU-865
  - TC-FA-SU-870
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: State per Sub-tab dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Assignment Budi Santoso (Pre-setup #30, 5 baris; urutan default Date descending). Label baris = `Activity|Transaction ID`; alias dipakai langkah:
  - A-1: `Unassigned|ASG-20260618-0089`, Date `30/06/26`, PIC `Eka W` (keyword `Wulandari`)
  - A-2: `Assigned|ASG-20260625-0102`, Name `Lemari`, PIC `Ahmad D`
  - A-3: `Assigned|ASG-20260618-0089`, PIC `Eka W` (keyword `Wulandari`)
  - A-4: `Assigned|ASG-20260512-0067`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
  - A-5: `Assigned|ASG-20260505-0045`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
- Seed Tab User Log sub-tab Session Budi Santoso (sub-tab pembanding TC-FA-SU-870; hasilnya tidak diasersi) (Pre-setup #30, 9 baris; urutan default Date descending). Label baris = `Date|Note` (kolom Activity bernilai `Session`, kolom Status bernilai `—`); alias dipakai langkah:
  - S-1: `16/07/26 08:12|Session started`
  - S-2: `15/07/26 20:30|Session ended`
  - S-3: `15/07/26 08:00|Session started`
  - S-4: `14/07/26 08:40|Session ended`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-5: `14/07/26 08:05|Session started`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-6: `13/07/26 17:05|Session ended`
  - S-7: `13/07/26 08:10|Session started`
  - S-8: `12/07/26 17:15|Session ended`
  - S-9: `12/07/26 08:02|Session started`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-864: Download: format CSV dan XLSX, nama file, dan tanpa toast sukses

1. Buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Hover icon Download
3. Verifikasi tooltip ikon `Download`
4. Klik icon Download
5. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `User-Log-Assignment-Budi-Santoso.csv` terunduh
9. Klik icon Download, pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `User-Log-Assignment-Budi-Santoso.xlsx` terunduh
12. Verifikasi CSV berencoding UTF-8 dengan BOM
13. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
14. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-865: Cakupan baris dan kolom Download: Search, Filter, Sort, dan Column Visibility

15. Klik icon Download, pilih `Download as CSV`
16. Verifikasi berkas memuat seluruh baris (bukan hanya halaman aktif)
17. Verifikasi urutan baris pada berkas mengikuti sort aktif
18. Ketik Search `Lemari`, tekan Enter
19. Klik icon Filter, buka dropdown PIC, centang `Ahmad D`
20. Klik `[Apply]`
21. Klik icon Download, pilih `Download as CSV`
22. Verifikasi berkas hanya memuat baris yang cocok dengan Search `Lemari` dan Filter PIC `Ahmad D` (irisan: A-2)
23. Klik `[Clear Field]` lalu `[Apply]`, lalu klik icon ← pada kotak Search
24. Klik icon Filter untuk menutup panel
25. Klik header kolom Column Visibility (⋯), hilangkan centang Name, tekan Esc
26. Klik icon Download, pilih `Download as CSV`
27. Verifikasi tidak ada toast peringatan
28. Verifikasi kolom Name tidak ikut berkas
29. Klik header kolom Column Visibility (⋯), centang kembali Name, tekan Esc
30. Klik icon Download, pilih `Download as CSV`
31. Verifikasi kolom Name ikut kembali pada berkas
32. Ketik Search `zzzz`, tekan Enter
33. Klik icon Download, pilih `Download as CSV`
34. Verifikasi tidak ada toast
35. Verifikasi berkas terunduh
36. Verifikasi berkas hanya memuat baris header kolom yang visible
37. Klik icon ← pada kotak Search

### TC-FA-SU-870: State sub-tab dipertahankan per sub-tab

38. Ketik Search `0067`, tekan Enter
39. Klik icon Filter, buka dropdown PIC, centang `Ahmad D`
40. Klik `[Apply]`
41. Klik icon Filter untuk menutup panel
42. Klik header Name satu kali
43. Ganti page size ke 25
44. Pindah ke sub-tab Session
45. Ketik Search `Session`, tekan Enter
46. Klik header Date satu kali
47. Kembali ke sub-tab Assignment
48. Verifikasi Search `0067` sub-tab Assignment dipulihkan
49. Verifikasi Filter PIC sub-tab Assignment dipulihkan
50. Verifikasi Sort Name sub-tab Assignment dipulihkan
51. Verifikasi page size 25 sub-tab Assignment dipulihkan
52. Verifikasi state sub-tab Assignment tidak memengaruhi sub-tab Session (Search `Session` dan Sort Date sub-tab Session tetap)
53. Klik Back breadcrumb ke List, buka Detail pengguna Budi Santoso lagi, klik tab User Log, sub-tab Assignment
54. Verifikasi state sub-tab Assignment (Search, Filter, Sort, page size) dipulihkan setelah Back breadcrumb
55. Tekan F5 pada halaman Detail
56. Verifikasi state sub-tab Assignment dipulihkan setelah refresh F5
57. Klik menu Settings > User pada sidebar, buka Detail pengguna Budi Santoso lagi, klik tab User Log, sub-tab Assignment
58. Verifikasi state sub-tab Assignment kembali ke default setelah keluar lewat menu sidebar

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Panel Filter tetap terbuka sesudah `[Apply]` dan baru tertutup bila icon Filter diklik (keputusan produk); karena itu `[Clear Field]` + `[Apply]` dijalankan tanpa mengklik icon Filter lagi. Langkah 24 dan 41 (`Klik icon Filter untuk menutup panel`) adalah langkah penghubung yang menutup panel sebelum blok berikutnya (S-03, S-09).
- Spec ini berjumlah 58 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC-FA-SU-864: klausa BOM UTF-8, tanda kutip ganda, dan sheet `Sheet1` adalah isi berkas (kelas f); spec menulisnya sebagai `Verifikasi` dengan kemampuan baca berkas dari tim FE. TC-FA-SU-865: Expected a menyebut seluruh baris tanpa jumlah; spec tidak menambah angka. TC-FA-SU-870: Langkah Uji 2 menyebut "kontrol berbeda" pada sub-tab lain tanpa nilai; spec memakai Search `Session` dan Sort Date pada sub-tab Session, dan nomor halaman aktif tidak diuji (TC menyebut fixture satu halaman).
