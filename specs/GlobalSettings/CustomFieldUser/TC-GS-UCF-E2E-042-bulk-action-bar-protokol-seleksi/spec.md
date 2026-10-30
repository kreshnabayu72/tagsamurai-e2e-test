---
id: TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi
title: "Bulk Action Bar: Screening Bar, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-140
  - TC-GS-UCF-141
  - TC-GS-UCF-142
  - TC-GS-UCF-143
  - TC-GS-UCF-515
  - TC-GS-UCF-144
coverage:
  web: automated
---

# Bulk Action Bar: Screening Bar, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini bergantung pada total tepat 14 Custom Field Client A (kebersihan field sisa dijamin butir hook suite "Field sisa Client A" di `suite.md`) sehingga tidak berjalan bersamaan dengan spec lain yang menambah atau menghapus Custom Field.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah tidak mengulang pembukaan layar. Ukuran halaman tabel 10 per halaman (default).
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca, tidak diubah atau dihapus; spec ini tidak melakukan aksi tulis apa pun): 14 Custom Field (6 Pre-setup `Cost Center` Active, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date` Inactive dan 8 Population `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`) di-seed idempotent oleh hook `before` lewat API (disediakan tim FE/BE; dilewati bila sudah ada). Total N = 14 diturunkan dari seeding ini. Tidak ada Data Dinamis.
- Cleanup: tidak ada data yang dibuat spec ini. Hook `after` mengembalikan state tabel (Search, Sort, Filter, seleksi) ke default.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pembacaan state checkbox header (checked, indeterminate, unchecked), pindah halaman tabel, Sort Field Name, Filter Panel dengan `[Apply]` dan `[Clear Field]`, Search tabel.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite). Sort tabel diatur pada langkah 1 dan dipulihkan pada langkah 68.

## Test Steps

### TC-GS-UCF-140: Screening Bulk Action Bar saat satu baris dicentang

1. Urutkan tabel berdasarkan Field Name ascending
2. Centang baris `Cost Center`
3. Verifikasi Bulk Action Bar tampil di kiri sejajar Table Tools
4. Verifikasi Bulk Action Bar memuat berurutan: `Bulk Action` | counter `1 custom field selected` | `Select All (14 records)` | `(✕)`
5. Klik `Bulk Action`
6. Verifikasi overlay `Bulk Action` menampilkan `Deactivate` dan `Delete`
7. Verifikasi `Activate` disembunyikan (`Cost Center` Active)
8. Tutup overlay `Bulk Action`

### TC-GS-UCF-141: Counter realtime dan icon (✕) membatalkan seleksi

9. Centang baris `Bonus`
10. Verifikasi counter `2 custom fields selected`
11. Uncheck baris `Bonus`
12. Verifikasi counter `1 custom field selected`
13. Klik `(✕)` pada Bulk Action Bar
14. Verifikasi seluruh seleksi dibatalkan
15. Verifikasi Bulk Action Bar hilang

### TC-GS-UCF-142: Checkbox header memilih baris halaman aktif dan menampilkan status indeterminate

16. Klik checkbox header
17. Verifikasi checkbox header checked
18. Verifikasi 10 baris halaman 1 terpilih
19. Uncheck baris `Cost Center`
20. Verifikasi checkbox header berstatus indeterminate
21. Verifikasi counter `9 custom fields selected`
22. Klik checkbox header hingga tidak tercentang
23. Verifikasi checkbox header unchecked
24. Verifikasi seluruh seleksi kosong
25. Verifikasi Bulk Action Bar hilang

### TC-GS-UCF-143: Select All lintas halaman, toggle Unselect All, dan kembali saat uncheck parsial

26. Centang baris `Cost Center`
27. Klik `Select All (14 records)`
28. Verifikasi seluruh 14 baris terpilih lintas halaman (counter `14 custom fields selected`)
29. Verifikasi tombol berganti `Unselect All (14 records)`
30. Pindah ke halaman 2
31. Verifikasi baris halaman 2 berstatus checked
32. Klik `Unselect All (14 records)`
33. Verifikasi seluruh seleksi dibatalkan
34. Verifikasi Bulk Action Bar hilang
35. Centang baris `Work Notes` pada halaman 2, lalu klik `Select All (14 records)`
36. Uncheck baris `Work Notes`
37. Verifikasi counter `13 custom fields selected`
38. Verifikasi tombol kembali `Select All (14 records)` (`{N}` = total baris yang match, tetap 14)
39. Klik `(✕)` pada Bulk Action Bar, lalu pindah ke halaman 1

### TC-GS-UCF-515: Mencentang manual seluruh baris lintas halaman mengubah tombol menjadi Unselect All dan uncheck parsial mengembalikannya

40. Untuk setiap baris pada halaman 1 (10 baris), centang checkbox baris satu per satu
41. Pindah ke halaman 2, lalu untuk setiap baris pada halaman 2 (4 baris), centang checkbox baris satu per satu
42. Verifikasi counter `14 custom fields selected`
43. Verifikasi tombol berganti `Unselect All (14 records)`
44. Uncheck satu baris pada halaman 2
45. Verifikasi counter `13 custom fields selected`
46. Verifikasi tombol kembali `Select All (14 records)`
47. Klik `(✕)` pada Bulk Action Bar, lalu pindah ke halaman 1

### TC-GS-UCF-144: Seleksi dipertahankan saat pindah halaman, Search, Filter, dan Sort berubah

48. Centang baris `Cost Center` dan `Employee Grade`
49. Verifikasi counter `2 custom fields selected`
50. Pindah ke halaman 2 lalu kembali ke halaman 1
51. Verifikasi `Cost Center` dan `Employee Grade` tetap checked
52. Verifikasi counter tetap `2 custom fields selected`
53. Ketik Search `phone`, tekan Enter
54. Verifikasi counter tetap `2 custom fields selected` meski baris `Cost Center` dan `Employee Grade` tidak tampil
55. Klik `(←)` pada kotak Search
56. Verifikasi `Cost Center` dan `Employee Grade` tetap checked
57. Urutkan Field Name descending
58. Verifikasi `Cost Center` dan `Employee Grade` tetap checked
59. Verifikasi counter tetap `2 custom fields selected`
60. Terapkan Filter Required `Yes`, klik `[Apply]`
61. Verifikasi `Cost Center` tetap checked
62. Verifikasi counter tetap `2 custom fields selected` meski baris `Employee Grade` tidak tampil
63. Klik `[Clear Field]` pada Filter Panel, lalu klik `[Apply]`
64. Verifikasi `Cost Center` dan `Employee Grade` tetap checked
65. Verifikasi counter tetap `2 custom fields selected`
66. Klik `(✕)` pada Bulk Action Bar
67. Verifikasi Bulk Action Bar hilang

### Pemulihan state tabel

68. Pulihkan sort tabel ke default (klik menu sidebar Global Settings > User > Custom Field)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (68 langkah). Seluruhnya satu kelas (Bulk Action Bar dan protokol seleksi), satu dataset (14 field Pre-setup dan Population), tanpa aksi tulis dan tanpa kelas harness lain. Tiap blok TC memulai dari seleksi kosong (dibersihkan lewat `(✕)` di akhir blok sebelumnya) sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Langkah 40 dan 41 adalah idiom "untuk setiap baris" yang diulang 10 dan 4 kali dengan ekspansi 14 centang.
- Urutan TC mengikuti TC sumber (140, 141, 142, 143, 515, 144); tidak ada aksi yang menghapus atau mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Sort Field Name ascending agar `Cost Center`, `Bonus`, dan `Employee Grade` berada pada halaman 1 dengan 10 baris per halaman; TC tidak menyatakan urutan default yang menjamin hal itu, lihat Temuan untuk QA), langkah 8 (menutup overlay), langkah 39 dan 47 (membersihkan seleksi dan kembali ke halaman 1), langkah 55 (menutup input Search lewat `(←)`), langkah 68 (pemulihan sort tabel). Langkah 26 dan 35 adalah langkah 1 dan 5 TC-GS-UCF-143.
- TC-GS-UCF-141 melanjutkan seleksi `Cost Center` dari TC-GS-UCF-140: langkah 2 dan `Verifikasi` counter `1 custom field selected` pada langkah 4 menjadi "setelah centang pertama" TC-GS-UCF-141 butir a, dan langkah 9 melanjutkan dengan centang kedua.
- Temuan untuk QA:
  - TC-GS-UCF-142 langkah 3 ("Uncheck checkbox header sampai kosong") tidak menyebut jumlah klik pada checkbox header yang berstatus indeterminate; spec menulis "klik ... hingga tidak tercentang".
  - TC-GS-UCF-140 sampai 144 dan 515 mengandalkan baris `Cost Center`, `Bonus`, dan `Employee Grade` berada pada halaman 1 tanpa menyebut urutan default atau sort; spec mengurutkan Field Name ascending (langkah 1). TC-GS-UCF-143 langkah 5 menyebut "centang satu baris" tanpa nama; spec memakai `Work Notes` pada halaman 2.
  - TC-GS-UCF-144 butir a ("Cost Center dan Employee Grade tetap checked pada setiap langkah") tidak dapat diamati untuk baris yang tersaring keluar oleh Search atau Filter; spec mengasersi counter pada kondisi itu dan checked pada kondisi baris tampil.
  - TC-GS-UCF-141 dan 143 menulis Dependensi `TC-GS-UCF-1` (Population); spec mengganti dengan seeding API di hook `before`.
