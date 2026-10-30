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
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE sesuai plan bagian 6) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
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
17. Verifikasi popup tertutup langsung tanpa dialog
18. Pilih `Bulk Action` > `Resolve` lagi
19. Isi Device Name `Queclink GV300`
20. Tekan `Esc`
21. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?`
22. Verifikasi dialog memiliki tombol `Cancel` dan `Leave`
23. Klik `Leave`

### TC-GS-TAG-86: Bulk Resolve dengan field wajib kosong

24. Pilih `Bulk Action` > `Resolve`
25. Isi hanya Model/Type `GV300`
26. Klik `Save`
27. Verifikasi error inline pada Device Name
28. Verifikasi error inline pada Brand
29. Verifikasi popup tetap terbuka
30. Verifikasi baris `356938035643101` dan `356938035643102` tetap `Needs Info`

### TC-GS-TAG-88: Bulk Resolve dan Row Edit Mode saling eksklusif

31. Klik `Resolve` row action baris `356938035643101` (di balik popup yang terbuka)
32. Verifikasi row action dan checkbox baris lain nonaktif selama popup Bulk Resolve aktif (hanya satu sesi edit aktif)
33. Klik `[✕]` pada popup
34. Verifikasi dialog `Unsaved Changes` muncul
35. Klik `Leave`

### TC-GS-TAG-338: Bulk Resolve dengan satu baris terpilih

36. Hapus centang baris `356938035643102` sehingga hanya baris `356938035643101` tercentang
37. Pilih `Resolve` pada Bulk Action Bar
38. Verifikasi popup `Resolve TAGs` dengan subtitle `1 row selected`
39. Klik `[✕]` pada popup

### TC-GS-TAG-85: Bulk Resolve menulis nilai identik

40. Centang baris `356938035643102` sehingga dua baris tercentang
41. Pilih `Bulk Action` > `Resolve`
42. Verifikasi popup berjudul `Resolve TAGs`
43. Verifikasi subtitle popup `2 rows selected`
44. Verifikasi field popup `Device Name* | SKU | Brand* | Model/Type`
45. Verifikasi footer popup `Clear Field | Save` dan tombol tutup `[✕]` (tanpa `Cancel`)
46. Isi Device Name `Queclink GV300` dan Brand `Queclink`
47. Klik `Save`
48. Verifikasi baris `356938035643101` dan `356938035643102` berstatus `Self-Purchased` dengan Device Name `Queclink GV300` dan Brand `Queclink` identik
49. Verifikasi aksi baris `Edit` tersedia pada kedua baris sehingga nilai dapat dikoreksi per baris
50. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi 2 (icon dan severity)

51. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-336: Icon dan severity row action serta Bulk Action Bar

52. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
53. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` (Template kosong sehingga baris `Needs Info`)
54. Buka section `Self-Purchased Template`
55. Isi Template Device Name `Queclink GV300` dan Brand `Queclink`
56. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643102` (baris `Self-Purchased`)
57. Buka row action baris `Official` `356938035643001`
58. Verifikasi aksi `Remove` (`DeleteBin6Line`, danger)
59. Tutup menu row action
60. Buka row action baris `Needs Info` `356938035643101`
61. Verifikasi aksi `Resolve` (`Edit2Line`, dark) di atas `Remove` (`DeleteBin6Line`, danger)
62. Tutup menu row action
63. Buka row action baris `Self-Purchased` `356938035643102`
64. Verifikasi aksi `Edit` (`Edit2Line`, dark) di atas `Remove` (`DeleteBin6Line`, danger)
65. Tutup menu row action
66. Centang baris `356938035643001` dan `356938035643101`
67. Verifikasi Bulk Action Bar pada seleksi campuran hanya `Remove` (`DeleteBin6Line`, danger)
68. Hapus centang baris `356938035643001`
69. Verifikasi Bulk Action Bar pada seleksi hanya `Needs Info` memuat `Resolve` (`Edit2Line`, dark) di atas `Remove` (`DeleteBin6Line`, danger)
70. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (Bulk Action Bar dan Bulk Resolve pada staging GPS).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah (70 langkah): satu kelas harness (staging GPS dengan popup Bulk Resolve) dan satu dataset baris `Needs Info`; sesi 1 memakai satu rangkaian baris untuk enam TC agar tidak membuka sesi dan menambah baris berulang (prinsip halaman yang sama dipakai berulang). Risiko yang diterima secara jujur: kegagalan keras pada popup Bulk Resolve (popup tidak terbuka) membuat blok sesudahnya dalam sesi 1 kehilangan makna; TC-336 dipisah ke sesi 2 karena membutuhkan baris Self-Purchased dengan Template terisi. Bila owner menilai terlalu panjang, spec ini dapat dipecah menjadi spec seleksi/bar (TC-84, TC-336) dan spec popup (TC-85 sampai TC-88, TC-338)
- Urutan sesi 1: TC-84 (screening bar) lebih dulu, lalu kasus ditutup/ditolak (TC-87, TC-86, TC-88, TC-338), dan Bulk Resolve sukses (TC-85) paling akhir karena mengubah baris `Needs Info` menjadi `Self-Purchased`. Baris `356938035643001` (Official, dari TC-84) tetap di staging selama sesi 1 tanpa tercentang, kecuali pada TC-84.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Tutup dropdown`, `Tutup menu row action`, hapus/centang baris, dan `Klik Leave` pada dialog menjaga state antar TC (S-09); `Verifikasi dialog Unsaved Changes muncul` pada TC-88 menjalankan S-08 (penutupan form dirty deterministik); `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini (`Leave` tanpa `Verifikasi` dialog).
- Temuan untuk QA:
  - TC-85 Expected c ("Nilai dapat dikoreksi per baris lewat `Edit` sesudahnya") tidak punya langkah koreksi; spec hanya mengasersi aksi `Edit` tersedia pada kedua baris.
  - TC-84 dan TC-338 tidak menyatakan apakah seleksi bertahan setelah popup Bulk Resolve ditutup; spec menyetel ulang centang secara eksplisit (hapus/centang baris) sebelum tiap TC.
  - TC-336 menyebut nama ikon (`DeleteBin6Line`, `Edit2Line`) dan severity (danger, dark); spec mengasersi sesuai TC, sedangkan cara membaca nama ikon di DOM ditentukan tahap script.
