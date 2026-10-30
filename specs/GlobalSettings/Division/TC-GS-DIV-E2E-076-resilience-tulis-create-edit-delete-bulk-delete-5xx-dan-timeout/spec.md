---
id: TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout
title: "Resilience Tulis: Create, Edit, Delete, dan Bulk Delete Gagal 5xx atau Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-76
  - TC-GS-DIV-77
  - TC-GS-DIV-110
  - TC-GS-DIV-111
  - TC-GS-DIV-123
  - TC-GS-DIV-140
coverage:
  web: automated
---

# Resilience Tulis: Create, Edit, Delete, dan Bulk Delete Gagal 5xx atau Timeout

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi).
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), semua bebas relasi dan milik spec ini (tidak memakai Population D-02 bersama), di-seed lewat API (kemampuan seeding Division lewat API) di hook `before`, Code di-generate otomatis:
  - `Accounting {runId}-076`: target Edit pada TC-GS-DIV-110 dan 111.
  - `Supply Chain {runId}-076`: target Delete pada TC-GS-DIV-123.
  - `Quality Assurance {runId}-076` dan `Product Management {runId}-076`: target Bulk Delete pada TC-GS-DIV-140.
  - Input uji `Planning {runId}-076` dengan Code `PLN` (TC-GS-DIV-76 dan 77) dan Name baru `Accounting Retry {runId}-076` (TC-GS-DIV-110 dan 111) adalah input yang submit-nya dipaksa gagal sehingga tidak membuat atau mengubah data.
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada request tulis Division dan dilepas segera setelah dipakai:
  - respons simpan Create Division dipaksa HTTP 500 (respons dipaksa tanpa meneruskan request ke server);
  - respons simpan Create Division dipaksa timeout klien (respons ditahan melewati batas klien tanpa meneruskan request ke server);
  - respons simpan Edit Division dipaksa HTTP 500 (respons dipaksa tanpa meneruskan request ke server);
  - respons simpan Edit Division dipaksa timeout klien (tanpa meneruskan request ke server);
  - respons hapus Division single dipaksa HTTP 500 (respons dipaksa tanpa meneruskan request ke server);
  - respons hapus Bulk Delete Division dipaksa HTTP 500 (respons dipaksa tanpa meneruskan request ke server).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): lepaskan semua intercept; hapus lewat API `Accounting {runId}-076`, `Accounting Retry {runId}-076`, `Supply Chain {runId}-076`, `Quality Assurance {runId}-076`, `Product Management {runId}-076`, dan `Planning {runId}-076` bila ada.
- Tidak ada state global lain yang diubah.
- TC-GS-DIV-76, 77, 110, 111, 123, 140: login sebagai Total Control dan berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-76: Create gagal 5xx mempertahankan form dan input

1. Klik `[+ Division]`
2. Isi Division Name `Planning {runId}-076` dan Code `PLN`
3. Paksa respons simpan Create Division HTTP 500 (intercept)
4. Klik [Submit]
5. Verifikasi toast error: `Error, failed to create division.`
6. Verifikasi modal Create tetap terbuka
7. Verifikasi Division Name `Planning {runId}-076` dipertahankan
8. Verifikasi Code `PLN` dipertahankan
9. Verifikasi tombol [Submit] kembali enabled

### TC-GS-DIV-77: Create timeout mempertahankan form dan input

10. Lepas intercept 500, paksa respons simpan Create Division timeout (intercept)
11. Klik [Submit]
12. Verifikasi toast error: `Connection problem. Please try again.`
13. Verifikasi toast memuat tombol `[Try Again]`
14. Verifikasi modal Create tetap terbuka
15. Verifikasi Division Name `Planning {runId}-076` dipertahankan
16. Verifikasi Code `PLN` dipertahankan
17. Verifikasi tombol [Submit] kembali enabled
18. Lepas intercept timeout
19. Klik `✕` pada form Create Division
20. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
21. Klik `[Leave]`
22. Ketik Search `{runId}-076`, tekan Enter pada tabel Division
23. Verifikasi baris `Accounting {runId}-076` tampil di tabel
24. Verifikasi Division `Planning {runId}-076` tidak dibuat (tidak ada di tabel)

### TC-GS-DIV-110: Edit gagal 5xx mempertahankan form dan input

25. Ganti isi kotak search dengan `Accounting {runId}-076`, tekan Enter pada tabel Division
26. Klik `⋯` pada baris `Accounting {runId}-076` > Edit
27. Ubah Division Name menjadi `Accounting Retry {runId}-076`
28. Paksa respons simpan Edit Division HTTP 500 (intercept)
29. Klik [Save]
30. Verifikasi toast error: `Error, failed to update division.`
31. Verifikasi modal Edit tetap terbuka
32. Verifikasi Division Name `Accounting Retry {runId}-076` dipertahankan
33. Verifikasi tombol [Save] kembali enabled

### TC-GS-DIV-111: Edit timeout mempertahankan form dan input

34. Lepas intercept 500, paksa respons simpan Edit Division timeout (intercept)
35. Klik [Save]
36. Verifikasi toast error: `Connection problem. Please try again.`
37. Verifikasi toast memuat tombol `[Try Again]`
38. Verifikasi modal Edit tetap terbuka
39. Verifikasi Division Name `Accounting Retry {runId}-076` dipertahankan
40. Verifikasi tombol [Save] kembali enabled
41. Lepas intercept timeout
42. Klik `✕` pada form Edit Division
43. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
44. Klik `[Leave]`
45. Ganti isi kotak search dengan `{runId}-076`, tekan Enter pada tabel Division
46. Verifikasi perubahan tidak tersimpan: baris `Accounting {runId}-076` tetap tampil di tabel
47. Verifikasi Division `Accounting Retry {runId}-076` tidak ada di tabel

### TC-GS-DIV-123: Delete gagal 5xx tidak menghapus Division dan dialog tetap terbuka

48. Ganti isi kotak search dengan `Supply Chain {runId}-076`, tekan Enter pada tabel Division
49. Klik `⋯` pada baris `Supply Chain {runId}-076` > Delete
50. Paksa respons hapus Division HTTP 500 (intercept)
51. Klik [Delete] pada dialog `Delete Division`
52. Verifikasi toast error: `Error, failed to delete division.`
53. Verifikasi dialog `Delete Division` tetap terbuka
54. Verifikasi tombol [Delete] kembali enabled
55. Lepas intercept 500
56. Klik [Cancel] pada dialog `Delete Division`
57. Verifikasi Division `Supply Chain {runId}-076` tidak terhapus dan tetap tampil di tabel

### TC-GS-DIV-140: Bulk Delete gagal 5xx tidak menghapus satu pun Division

58. Ganti isi kotak search dengan `{runId}-076`, tekan Enter pada tabel Division
59. Centang baris `Quality Assurance {runId}-076` dan `Product Management {runId}-076`
60. Klik aksi [Delete] pada Bulk Action Bar
61. Paksa respons hapus Bulk Delete Division HTTP 500 (intercept)
62. Klik [Delete] pada dialog konfirmasi
63. Verifikasi toast error: `Error, failed to delete division.`
64. Verifikasi dialog konfirmasi tetap terbuka
65. Verifikasi tombol [Delete] kembali enabled
66. Lepas intercept 500
67. Klik [Cancel] pada dialog konfirmasi
68. Verifikasi `Quality Assurance {runId}-076` dan `Product Management {runId}-076` tetap ada di tabel (all-or-nothing)
69. Klik Unselect All
70. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE dengan intercept parsial (prinsip 13b); kegagalan dipicu dengan `Spectra.intercept()` pada request browser, sehingga bukan `Mode: mock`.
- Urutan TC di spec sama dengan urutan sumber (76, 77, 110, 111, 123, 140), dengan aksi yang menghapus data paling akhir: form Create dari TC-GS-DIV-76 dipakai ulang oleh TC-GS-DIV-77, dan form Edit dari TC-GS-DIV-110 dipakai ulang oleh TC-GS-DIV-111 (prinsip 6 dan 8, hemat buka form); Langkah Uji 1 dan 2 TC-GS-DIV-77 dan Langkah Uji 1 dan 2 TC-GS-DIV-111 tidak ditulis ulang karena form dan nilainya masih terbuka. TC-GS-DIV-77 dan 111 hanya mengganti intercept lalu klik ulang [Submit] atau [Save]; Division Name dan Code tetap sama dengan TC-GS-DIV-76 dan 110.
- Urutan dalam TC-GS-DIV-123 dan 140: Expected Result b (Division tetap tampil di tabel) dijalankan setelah dialog ditutup lewat [Cancel] (langkah 56 dan 67), karena tabel tertutup dialog selama dialog terbuka; Expected Result c (dialog tetap terbuka dan [Delete] enabled) diasersi lebih dulu (langkah 53, 54, 64, dan 65), sesuai urutan state.
- Expected Result d TC-GS-DIV-76 (record tidak dibuat) diasersi sesudah form ditutup (langkah 24); Expected Result c TC-GS-DIV-110 (perubahan tidak tersimpan) diasersi pada langkah 46 dan 47.
- Asersi absence (langkah 24 dan 47) didahului anchor positif pada tabel yang sama (langkah 23 dan 46; bagian 8b butir 2).
- Langkah penghubung: langkah 18, 41, 55, dan 66 (melepas intercept setelah dipakai; intercept dipasang pada langkah 3, 10, 28, 34, 50, dan 61 sesuai Langkah Uji TC); langkah 19 sampai 21 dan 42 sampai 44 (menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`; verifikasi dialog pada langkah 20 dan 43 adalah asersi tambahan yang tidak ada di TC, ditulis agar penutupan form deterministik, konvensi bagian 10 S-08); langkah 22, 25, 45, 48, dan 58 (Search nama yang diasersi atau menjadi target baris, sebagian menggantikan Search sebelumnya); langkah 56 dan 67 (membatalkan dialog); langkah 69 dan 70 (Unselect All dan mengosongkan Search).
- Spec melewati sekitar 35 langkah (70 langkah) karena memuat enam TC kelas fault injection dengan intercept parsial yang berbagi satu set data, satu akun, dan form yang dipakai ulang; satu kelas harness, tiap blok (Create, Edit, Delete, Bulk Delete) berdiri sendiri, dan hampir seluruh langkah adalah pemasangan atau pelepasan intercept serta verifikasi per klausa (S-01).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-DIV-110, 111, 123, 140: precondition menyebut Division `Accounting`, `Supply Chain`, `Quality Assurance`, `Product Management` dari Population TC-GS-DIV-30; spec memakai Division milik sendiri bersuffix `{runId}-076` (S-06) dengan Code auto-generate, sehingga Code `ACC` dan `SC` pada precondition tidak dipakai.
  - TC-GS-DIV-77 dan 111: TC tidak menyebut apakah request yang timeout diteruskan ke server (PRD §9.6 menyebut retry Edit pasca-timeout yang sudah tersimpan diperlakukan No-Op); spec memakai timeout tanpa meneruskan request, dan TC tidak mengasersi ada atau tidaknya record pada TC-GS-DIV-77.
  - TC-GS-DIV-76, 110, 123, 140: TC tidak menyebut apakah respons 5xx dipaksa dengan atau tanpa meneruskan request ke server; spec memaksa respons tanpa meneruskan request.
  - TC-GS-DIV-77 dan 111: TC tidak menyebut apakah toast 5xx dari langkah sebelumnya sudah hilang saat toast timeout diverifikasi; spec memverifikasi toast sesuai teks masing-masing.
  - TC-GS-DIV-123 dan 140: tombol dialog bulk yang diklik adalah [Delete] (bukan [Continue]) karena seluruh Division terpilih bebas relasi (PRD §4.2d Dialog 4).
