---
id: TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging
title: "Bulk Action Bar Staging dan Popup Bulk Resolve: Seleksi Homogen/Campuran, Nilai Identik, Validasi, Unsaved Changes, dan Icon/Severity"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-84
  - TC-GS-TAG-85
  - TC-GS-TAG-86
  - TC-GS-TAG-87
  - TC-GS-TAG-88
  - TC-GS-TAG-336
  - TC-GS-TAG-338
coverage:
  web: automated
---

# Bulk Action Bar Staging dan Popup Bulk Resolve: Seleksi Homogen/Campuran, Nilai Identik, Validasi, Unsaved Changes, dan Icon/Severity

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Stok resmi Admin Console Client A (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`) di-seed idempotent oleh fixture BE di hook `before`: GPS `356938035643001` (DD-S1) Available. Akun Admin Console untuk seeding stok disediakan tim FE (S-13).
- Data identifier: `356938035643101` (DD-N1), `356938035643102` (DD-N2) tidak ada di stok resmi dan tidak ada di registri Client A. Opsi mandiri (BYO) aktif; Template Self-Purchased kosong pada awal tiap sesi kecuali disebut.
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE, S-13) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### Sesi 1 (Template kosong)

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` lalu `356938035643102` (`Needs Info`) dan `356938035643001` (`Official`)

### TC-GS-TAG-84: Bulk Action Bar staging

3. Centang baris `356938035643101` dan `356938035643102`
4. Verifikasi Bulk Action Bar tampil dengan counter `2 TAGs selected`
5. Buka dropdown `Bulk Action`
6. Verifikasi opsi `Resolve` dan `Remove` tampil
7. Tutup dropdown `Bulk Action`
8. Centang juga baris `356938035643001`
9. Verifikasi counter `3 TAGs selected`
10. Buka dropdown `Bulk Action`
11. Verifikasi hanya opsi `Remove` yang tampil
12. Verifikasi checkbox tampil dan enabled di semua baris (semua status)
13. Tutup dropdown `Bulk Action`
14. Hapus centang baris `356938035643001`

### TC-GS-TAG-87: Menutup Bulk Resolve

15. Pilih `Bulk Action` > `Resolve`
16. Klik `[✕]` pada popup tanpa mengisi
17. Verifikasi popup tertutup
18. Verifikasi tidak ada dialog yang tampil
19. Pilih `Bulk Action` > `Resolve` lagi
20. Isi Device Name `Queclink GV300`
21. Tekan `Esc`
22. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?`
23. Verifikasi dialog memiliki tombol `Cancel` dan `Leave`
24. Klik `Leave`

### TC-GS-TAG-86: Bulk Resolve dengan field wajib kosong

25. Pilih `Bulk Action` > `Resolve`
26. Isi hanya Model/Type `GV300`
27. Klik `Save`
28. Verifikasi error inline pada Device Name
29. Verifikasi error inline pada Brand
30. Verifikasi popup tetap terbuka
31. Verifikasi baris `356938035643101` dan `356938035643102` tetap `Needs Info`

### TC-GS-TAG-88: Bulk Resolve dan Row Edit Mode saling eksklusif

32. Klik `Resolve` row action baris `356938035643101` (di balik popup yang terbuka)
33. Verifikasi row action dan checkbox baris lain nonaktif selama popup Bulk Resolve aktif (hanya satu sesi edit aktif)
34. Klik `[✕]` pada popup
35. Verifikasi dialog `Unsaved Changes` muncul
36. Klik `Leave`

### TC-GS-TAG-338: Bulk Resolve dengan satu baris terpilih

37. Hapus centang baris `356938035643102` sehingga hanya baris `356938035643101` tercentang
38. Pilih `Resolve` pada Bulk Action Bar
39. Verifikasi popup `Resolve TAGs` dengan subtitle `1 row selected`
40. Klik `[✕]` pada popup

### TC-GS-TAG-85: Bulk Resolve menulis nilai identik

41. Centang baris `356938035643102` sehingga dua baris tercentang
42. Pilih `Bulk Action` > `Resolve`
43. Verifikasi popup berjudul `Resolve TAGs`
44. Verifikasi subtitle popup `2 rows selected`
45. Verifikasi field popup `Device Name* | SKU | Brand* | Model/Type`
46. Verifikasi footer popup `Clear Field | Save` dan tombol tutup `[✕]` (tanpa `Cancel`)
47. Isi Device Name `Queclink GV300` dan Brand `Queclink`
48. Klik `Save`
49. Verifikasi baris `356938035643101` dan `356938035643102` berstatus `Self-Purchased`
50. Verifikasi baris `356938035643101` dan `356938035643102` memuat Device Name `Queclink GV300` identik
51. Verifikasi baris `356938035643101` dan `356938035643102` memuat Brand `Queclink` identik
52. Verifikasi aksi baris `Edit` tersedia pada kedua baris sehingga nilai dapat dikoreksi per baris
53. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog `Unsaved Changes` (staging berisi baris)

### Sesi 2 (icon dan severity)

54. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-336: Icon dan severity row action serta Bulk Action Bar

55. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
56. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` (Template kosong sehingga baris `Needs Info`)
57. Buka section `Self-Purchased Template`
58. Isi Template Device Name `Queclink GV300` dan Brand `Queclink`
59. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643102` (baris `Self-Purchased`)
60. Buka row action baris `Official` `356938035643001`
61. Verifikasi aksi `Remove` (`DeleteBin6Line`, danger)
62. Tutup menu row action
63. Buka row action baris `Needs Info` `356938035643101`
64. Verifikasi aksi `Resolve` (`Edit2Line`, dark) di atas `Remove` (`DeleteBin6Line`, danger)
65. Tutup menu row action
66. Buka row action baris `Self-Purchased` `356938035643102`
67. Verifikasi aksi `Edit` (`Edit2Line`, dark) di atas `Remove` (`DeleteBin6Line`, danger)
68. Tutup menu row action
69. Centang baris `356938035643001` dan `356938035643101`
70. Verifikasi Bulk Action Bar pada seleksi campuran hanya `Remove` (`DeleteBin6Line`, danger)
71. Hapus centang baris `356938035643001`
72. Verifikasi Bulk Action Bar pada seleksi hanya `Needs Info` memuat `Resolve` (`Edit2Line`, dark) di atas `Remove` (`DeleteBin6Line`, danger)
73. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog `Unsaved Changes` (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (Bulk Action Bar dan Bulk Resolve pada staging GPS).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah (73 langkah): satu kelas harness (staging GPS dengan popup Bulk Resolve) dan satu dataset baris `Needs Info`; sesi 1 memakai satu rangkaian baris untuk enam TC agar tidak membuka sesi dan menambah baris berulang (prinsip halaman yang sama dipakai berulang). Risiko yang diterima secara jujur: kegagalan keras pada popup Bulk Resolve (popup tidak terbuka) membuat blok sesudahnya dalam sesi 1 kehilangan makna; TC-336 dipisah ke sesi 2 karena membutuhkan baris Self-Purchased dengan Template terisi.
- Urutan sesi 1: TC-84 (screening bar) lebih dulu, lalu kasus ditutup/ditolak (TC-87, TC-86, TC-88, TC-338), dan Bulk Resolve sukses (TC-85) paling akhir karena mengubah baris `Needs Info` menjadi `Self-Purchased`. Baris `356938035643001` (Official, dari TC-84) tetap di staging selama sesi 1 tanpa tercentang, kecuali pada TC-84.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Tutup dropdown`, `Tutup menu row action`, hapus/centang baris, dan `Klik Leave` pada dialog menjaga state antar TC (S-09); `Verifikasi dialog Unsaved Changes muncul` pada TC-88 menjalankan S-08 (penutupan form dirty deterministik); `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03) karena dialog `Unsaved Changes` muncul pada sesi dengan baris staging, sedangkan definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini (`Leave` tanpa `Verifikasi` dialog).
- Temuan untuk QA:
  - TC-85 Expected c ("Nilai dapat dikoreksi per baris lewat `Edit` sesudahnya") tidak punya langkah koreksi; spec hanya mengasersi aksi `Edit` tersedia pada kedua baris.
  - TC-84 dan TC-338 tidak menyatakan apakah seleksi bertahan setelah popup Bulk Resolve ditutup; spec menyetel ulang centang secara eksplisit (hapus/centang baris) sebelum tiap TC.
  - TC-336 menyebut nama ikon (`DeleteBin6Line`, `Edit2Line`) dan severity (danger, dark); spec mengasersi sesuai TC, sedangkan cara membaca nama ikon di DOM ditentukan tahap script.
