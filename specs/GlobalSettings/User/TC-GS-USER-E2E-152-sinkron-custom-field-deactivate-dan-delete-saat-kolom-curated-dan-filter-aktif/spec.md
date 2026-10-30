---
id: TC-GS-USER-E2E-152-sinkron-custom-field-deactivate-dan-delete-saat-kolom-curated-dan-filter-aktif
title: "Sinkron Custom Field Deactivate, Activate, dan Delete saat Kolom Curated Tampil dan Filter Aktif di User List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1064
  - TC-GS-USER-1065
  - TC-GS-USER-1066
coverage:
  web: automated
---

# Sinkron Custom Field Deactivate, Activate, dan Delete saat Kolom Curated Tampil dan Filter Aktif di User List

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User). Spec memakai satu akun tanpa ganti akun; tab browser kedua memakai sesi akun yang sama. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 24) dibaca saja dan tidak diubah; spec memakai Custom Field milik sendiri bersuffix (S-06).
- Data Dinamis (suffix per run dan nomor spec), di-seed lewat API di hook `before` oleh akun Total Control (kemampuan seeding Custom Field, Login User, dan nilai Custom Field user lewat API; nilai field wajib lain user mengikuti fixture `fixtures/user.json` yang belum ada, disediakan tim FE):
  - Custom Field `Shirt Size {runId}-152`: Data Type Dropdown, Dropdown Values `L` dan `M`, Active (setara `Shirt Size` Dropdown pada TC-GS-USER-1064 dan 1066).
  - Custom Field `Blood Type {runId}-152`: Data Type Dropdown, Dropdown Values `O` dan `A`, Active (setara `Blood Type` Dropdown pada TC-GS-USER-1065).
  - Login User `Rina Susanti {runId}-152`, email `rinasusanti+{runId}-152@qwertysystem.net`, Activated, Active, Access `Fixed Asset`, nilai `Shirt Size {runId}-152` = `L`, nilai `Blood Type {runId}-152` = `O`.
  - Login User `Tomi Wijaya {runId}-152`, email `tomiwijaya+{runId}-152@qwertysystem.net`, Activated, Active, Access `Fixed Asset`, nilai `Shirt Size {runId}-152` = `M`, nilai `Blood Type {runId}-152` = `A` (dua nilai distinct pada kolom yang difilter, S-11).
- Kemampuan teknis: (a) membuka tab browser kedua dengan sesi akun yang sama untuk memicu perubahan Custom Field (konteks kedua hanya sebagai pemicu, P-2); (b) memuat ulang halaman User List; (c) mengembalikan konfigurasi Setup Column dan filter akun Total Control ke default di hook `after` (penyimpanan Setup Column dan filter disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah berhasil penuh): hapus lewat API Login User `rinasusanti+{runId}-152@qwertysystem.net` dan `tomiwijaya+{runId}-152@qwertysystem.net`, lalu Custom Field `Shirt Size {runId}-152` dan `Blood Type {runId}-152` bila masih ada; kembalikan Setup Column dan filter ke default.
- Tidak ada state global lain yang diubah.

## Test Steps

### Persiapan kolom curated dan filter untuk TC-GS-USER-1064

1. Buka Tab User List (sub-tab Login User), klik icon Search, ketik `{runId}-152`, tekan Enter
2. Buka Setup Column dari header kolom Actions `⋯` > `Setup Column...`
3. Centang `Shirt Size {runId}-152`, klik `[Save]`
4. Tunggu aksi selesai
5. Buka Filter Panel, pilih `L` pada filter `Shirt Size {runId}-152`, klik `[Apply]`
6. Verifikasi kolom `Shirt Size {runId}-152` tampil di tabel
7. Verifikasi baris `Rina Susanti {runId}-152` tampil dengan nilai `L`
8. Verifikasi baris `Tomi Wijaya {runId}-152` tidak tampil (filter `L` aktif)

### TC-GS-USER-1064: Deactivate Custom Field saat kolom curated tampil dan filter aktif

9. Buka tab browser kedua dengan sesi akun yang sama, buka Global Settings > User > Tab Custom Field
10. Klik icon Search, ketik `Shirt Size {runId}-152`, tekan Enter
11. Matikan switch Active baris `Shirt Size {runId}-152`, klik `[Deactivate]` pada dialog
12. Tunggu aksi selesai
13. Tutup tab kedua dan kembali ke tab pertama (User List)
14. Muat ulang halaman User List
15. Klik icon Search, ketik `{runId}-152`, tekan Enter
16. Verifikasi baris `Rina Susanti {runId}-152` tampil di tabel
17. Verifikasi baris `Tomi Wijaya {runId}-152` tampil di tabel (tabel memuat baris tanpa kriteria `L`)
18. Verifikasi kolom `Shirt Size {runId}-152` tidak tampil di tabel
19. Buka Filter Panel
20. Verifikasi filter `Blood Type {runId}-152` tampil di Filter Panel
21. Verifikasi filter `Shirt Size {runId}-152` tidak ada di Filter Panel
22. Verifikasi tidak ada kriteria `L` yang aktif pada Filter Panel
23. Tutup Filter Panel
24. Buka Setup Column dari header kolom Actions `⋯` > `Setup Column...`
25. Verifikasi `Blood Type {runId}-152` tampil di daftar kolom Popup Setup Column
26. Verifikasi `Shirt Size {runId}-152` tidak ada di daftar kolom Popup Setup Column
27. Klik `✕` pada Popup Setup Column

### TC-GS-USER-1066: Activate kembali Custom Field muncul sebagai curated default hidden

28. Buka tab browser kedua dengan sesi akun yang sama, buka Global Settings > User > Tab Custom Field
29. Klik icon Search, ketik `Shirt Size {runId}-152`, tekan Enter
30. Nyalakan switch Active baris `Shirt Size {runId}-152`, klik `[Activate]` pada dialog
31. Tunggu aksi selesai
32. Tutup tab kedua dan kembali ke tab pertama (User List)
33. Muat ulang halaman User List
34. Klik icon Search, ketik `{runId}-152`, tekan Enter
35. Verifikasi baris `Rina Susanti {runId}-152` tampil di tabel
36. Verifikasi kolom `Shirt Size {runId}-152` tidak tampil di tabel
37. Buka Setup Column dari header kolom Actions `⋯` > `Setup Column...`
38. Verifikasi `Shirt Size {runId}-152` tampil sebagai kolom curated dengan checkbox tidak tercentang pada Popup Setup Column
39. Verifikasi konfigurasi Setup Column lama untuk `Shirt Size {runId}-152` tidak dipulihkan (checkbox tetap tidak tercentang walaupun dicentang pada langkah 3)
40. Klik `✕` pada Popup Setup Column

### Persiapan kolom curated dan filter untuk TC-GS-USER-1065

41. Buka Setup Column dari header kolom Actions `⋯` > `Setup Column...`
42. Centang `Blood Type {runId}-152`, klik `[Save]`
43. Tunggu aksi selesai
44. Buka Filter Panel, pilih `O` pada filter `Blood Type {runId}-152`, klik `[Apply]`
45. Verifikasi kolom `Blood Type {runId}-152` tampil di tabel
46. Verifikasi baris `Rina Susanti {runId}-152` tampil dengan nilai `O`
47. Verifikasi baris `Tomi Wijaya {runId}-152` tidak tampil (filter `O` aktif)

### TC-GS-USER-1065: Delete Custom Field saat kolom curated tampil dan filter aktif

48. Buka tab browser kedua dengan sesi akun yang sama, buka Global Settings > User > Tab Custom Field
49. Klik icon Search, ketik `Blood Type {runId}-152`, tekan Enter
50. Klik `⋯` pada baris `Blood Type {runId}-152` > Delete, klik `[Delete]` pada dialog
51. Tunggu aksi selesai
52. Tutup tab kedua dan kembali ke tab pertama (User List)
53. Muat ulang halaman User List
54. Klik icon Search, ketik `{runId}-152`, tekan Enter
55. Verifikasi baris `Rina Susanti {runId}-152` tampil di tabel
56. Verifikasi baris `Tomi Wijaya {runId}-152` tampil di tabel (tabel memuat baris tanpa kriteria `O`)
57. Verifikasi kolom `Blood Type {runId}-152` tidak tampil di tabel
58. Buka Filter Panel
59. Verifikasi filter `Shirt Size {runId}-152` tampil di Filter Panel
60. Verifikasi filter `Blood Type {runId}-152` tidak ada di Filter Panel
61. Verifikasi tidak ada kriteria `O` yang aktif pada Filter Panel
62. Tutup Filter Panel
63. Buka Setup Column dari header kolom Actions `⋯` > `Setup Column...`
64. Verifikasi `Shirt Size {runId}-152` tampil di daftar kolom Popup Setup Column
65. Verifikasi `Blood Type {runId}-152` tidak ada di daftar kolom Popup Setup Column
66. Klik `✕` pada Popup Setup Column

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Sinkron Custom Field ke kolom curated dan filter User List; tidak ada TC kelas harness.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-GS-USER-1066 sebelum TC-GS-USER-1065, karena TC-GS-USER-1066 bergantung pada TC-GS-USER-1064 (Dependensi: `Shirt Size` Inactive setelah ditampilkan sebagai kolom) dan TC-GS-USER-1065 menghapus data sehingga ditaruh paling akhir (bagian 3 prinsip 5).
- Spec melewati sekitar 35 langkah (66 langkah). Alasan: tiga TC memakai satu tema, satu layar (User List), dan dua Custom Field seed; TC-GS-USER-1066 memakai state `Shirt Size` dari TC-GS-USER-1064 (Dependensi TC-GS-USER-1064 pada TC sumber), sedangkan tiap TC membutuhkan persiapan kolom curated dan filter sendiri (kolom ditampilkan lewat Setup Column dan kriteria di-Apply) serta pengamatan di tiga surface (tabel, Filter Panel, Popup Setup Column) dengan `Verifikasi` per klausa dan anchor pembanding (S-01, 8b butir 2).
- Tab browser kedua hanya memicu perubahan Custom Field dengan akun yang sama dan hasilnya tidak diasersi di tab itu (P-2); tab ditutup segera setelah pemicu selesai.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 5, 41 sampai 44 (menyiapkan kolom curated dan filter sesuai precondition d TC-GS-USER-1064 dan 1065); langkah 9 sampai 13, 28 sampai 32, 48 sampai 52 (memicu perubahan Custom Field di tab kedua); langkah 4, 12, 31, 43, 51 (menunggu aksi selesai); langkah 14, 15, 33, 34, 53, 54 (memuat ulang dan Search); langkah 19, 23, 24, 27, 37, 40, 58, 62, 63, 66 (membuka dan menutup Filter Panel dan Popup Setup Column).
- Asersi tambahan di luar Expected TC: langkah 6 sampai 8 dan 45 sampai 47 membuktikan precondition d (kolom tampil dan filter aktif) sebelum pemicu, agar asersi sesudah pemicu bermakna (S-03). Asersi absence (langkah 18, 21, 26, 36, 57, 60, 65) didahului `Verifikasi` pembanding pada surface yang sama (langkah 16 dan 17, 20, 25, 35, 55 dan 56, 59, 64; bagian 8b butir 2).
- TC-GS-USER-1066 butir b dan c: butir b diasersi pada langkah 38 (tampil sebagai curated tanpa centang) dan butir c pada langkah 39 (konfigurasi lama tidak dipulihkan); keduanya membaca checkbox yang sama dari sudut berbeda.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-1064 dan 1065: Post Condition (nilai `Shirt Size` tetap tersimpan; field dan nilai terhapus permanen) tanpa langkah observasi di TC; tidak diasersi.
  - TC-GS-USER-1064, 1065, 1066: "muat ulang tabel" tidak menyebut apakah memuat ulang halaman atau menyegarkan data tabel, dan TC tidak menyebut apakah Search dan filter bertahan sesudah muat ulang; spec memuat ulang halaman, membuka Search ulang, dan menganggap filter dan kolom curated bertahan sampai Custom Field berubah.
  - TC-GS-USER-1064 dan 1065: precondition d tidak menyebut data user yang bernilai `L` atau `O`; spec men-seed dua user dengan nilai distinct pada kolom yang difilter.
  - TC-GS-USER-1064 dan 1065: TC tidak menyebut cara mengamati "kriteria dilepas" pada Filter Panel; spec mengasersi tidak ada kriteria aktif dan tabel memuat baris tanpa kriteria itu.
  - TC-GS-USER-1066 butir b dan c: butir c ("konfigurasi lama tidak dipulihkan") tidak punya observasi terpisah dari butir b; spec mengasersi checkbox yang sama.
  - TC sumber menyebut "tab lain" tanpa menyatakan tab browser atau sub-tab modul; spec memakai tab browser kedua.
