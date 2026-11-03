---
id: TC-FA-CAT-E2E-167-absence-log-edit-no-op-zero-delta-seed-onboarding-aksi-gagal-dan-skip
title: "Absence Log Category: Edit Tanpa Perubahan (No-Op dan Zero-Delta), Seed Onboarding, Baris Skip Bulk Delete, Aksi Gagal 5xx atau Diblok Guard, serta Kategori Tidak Terlibat"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-191
  - TC-FA-CAT-192
  - TC-FA-CAT-201
  - TC-FA-CAT-464
  - TC-FA-CAT-467
  - TC-FA-CAT-477
  - TC-FA-CAT-478
  - TC-FA-CAT-473
coverage:
  web: automated
---

# Absence Log Category: Edit Tanpa Perubahan (No-Op dan Zero-Delta), Seed Onboarding, Baris Skip Bulk Delete, Aksi Gagal 5xx atau Diblok Guard, serta Kategori Tidak Terlibat

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua: Total Control (Pre-setup #1) pada client CatFresh (Pre-setup #25) untuk TC-FA-CAT-473, password dari `Spectra.env.FA_TC_PASSWORD`. Login lewat langkah Ganti akun eksplisit (langkah 62). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup yang hanya dibaca atau menjadi target aksi no-op yang tidak mengubah data (S-06, pengecualian 2026-10-21; Last Updated dan Modified By tidak berubah): pada CatMain `Furniture` (Code `FURN`, ditunjuk Asset Name `Office Chair`, in-use) untuk langkah 1 sampai 15, 22 sampai 27, dan Delete yang diblok guard (langkah 50 sampai 52); `Heavy Tools` (Pre-setup #39, Code `HT`, leaf, Total Asset 0) untuk Zero-Delta langkah 16 sampai 21; `Tools` (Code `TOOL`, ditunjuk `Drill Set`, in-use) sebagai baris yang dilewati Bulk Delete dan kategori yang tidak terlibat. Pada CatFresh (Pre-setup #25) `Default Category` (Code `DC`, Modified By System) hanya dibaca.
- Data milik spec pada CatMain (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after`): `Vehicle {runId}-167` (Code `V167`, leaf, Total Asset 0) dan `Accessory {runId}-167` (Code `A167`, internal) berisi `Cable {runId}-167` (Code `C167`, leaf) sebagai target Bulk Delete (langkah 29 sampai 31); `Fail Edit {runId}-167` (Code `FE167`, leaf) sebagai target Edit yang dipaksa gagal 500 (langkah 43 sampai 44); `Only Edit {runId}-167` (Code `OE167`, leaf, Description kosong) sebagai target Edit kategori yang terlibat (langkah 56 sampai 57).
- Kemampuan teknis: pemaksaan respons HTTP 500 pada request simpan Edit kategori lewat `Spectra.intercept()` di atas backend nyata, dilepas segera sesudah pemicu (S-09); membuka Modal Changelog, Detail User aktor > Tab System Log, dan Activity Log serta mencari baris dan menghitung jumlah baris per nama kategori (jumlah dibandingkan sebagai selisih terhadap baseline, bukan angka absolut; S-12); mekanisme pencarian di tiga surface tidak diuraikan TC dan disediakan tim FE/BE tanpa endpoint karangan. Format Last Updated mengikuti General Settings client.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-191: Edit tanpa perubahan, toast netral dan data tidak berubah

1. Catat Modified By dan Last Updated baris `Furniture`
2. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
3. Klik `[Save]` tanpa mengubah field
4. Verifikasi popup Edit tertutup normal
5. Verifikasi toast netral `No changes to save.`
6. Verifikasi tidak ada inline error duplikat terhadap diri sendiri
7. Verifikasi Modified By baris `Furniture` sama dengan nilai yang dicatat pada langkah 1
8. Verifikasi Last Updated baris `Furniture` sama dengan nilai yang dicatat pada langkah 1

### TC-FA-CAT-192: Edit yang hanya mengubah kapitalisasi dan spasi tepi diperlakukan sebagai No-Op

9. Catat baseline jumlah baris Changelog untuk Category Name `Furniture`
10. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
11. Ubah Category Name menjadi ` furniture ` (huruf kecil dengan spasi tepi) tanpa mengubah field lain
12. Klik `[Save]`
13. Verifikasi toast netral `No changes to save.`
14. Verifikasi nilai Category Name yang tersimpan tetap `Furniture`
15. Verifikasi jumlah baris Changelog untuk Category Name `Furniture` sama dengan baseline langkah 9 (tidak ada baris log baru)

### TC-FA-CAT-201: Edit yang mengosongkan Code dengan hasil generate sama dengan Code lama adalah Zero-Delta

16. Catat baseline jumlah baris Changelog Field `Code` untuk Category Name `Heavy Tools`
17. Klik elipsis (⋯) pada baris `Heavy Tools` > `Edit`
18. Kosongkan Code tanpa mengubah Category Name
19. Klik `[Save]`
20. Verifikasi Code `Heavy Tools` tetap `HT` (hasil generate sama dengan Code lama)
21. Verifikasi jumlah baris Changelog Field `Code` untuk `Heavy Tools` sama dengan baseline langkah 16 (Zero-Delta, tidak ada baris log baru)

### TC-FA-CAT-464: Edit tanpa perubahan tidak menulis baris di tiga surface

22. Catat baseline jumlah baris Changelog, System Log aktor, dan Activity Log untuk Category Name `Furniture`
23. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
24. Klik `[Save]` tanpa mengubah field
25. Verifikasi toast netral `No changes to save.`
26. Hitung jumlah baris Changelog, System Log aktor, dan Activity Log untuk Category Name `Furniture` sesudah aksi
27. Verifikasi jumlah baris Changelog, System Log aktor, dan Activity Log sama dengan baseline langkah 22

### TC-FA-CAT-467: Log Bulk Delete, satu baris per node terhapus dan baris yang di-skip tidak menulis entri

28. Catat baseline jumlah baris Changelog, System Log aktor, dan Activity Log untuk Category Name `Tools`
29. Centang checkbox baris `Vehicle {runId}-167`, `Accessory {runId}-167`, dan `Tools`
30. Klik `[Delete]` pada Bulk Action Bar
31. Klik `[Continue]`
32. Buka Modal Changelog dan cari baris Delete untuk `{runId}-167` serta Category Name `Tools`
33. Verifikasi Changelog memuat tiga baris Delete: `Vehicle {runId}-167`, `Accessory {runId}-167`, dan `Accessory {runId}-167 › Cable {runId}-167`
34. Verifikasi jumlah baris Changelog untuk Category Name `Tools` sama dengan baseline langkah 28 (tidak ada baris untuk `Tools`)
35. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Delete untuk `{runId}-167` serta Name `Tools`
36. Verifikasi System Log aktor memuat tiga baris Delete: `Vehicle {runId}-167`, `Accessory {runId}-167`, dan `Accessory {runId}-167 › Cable {runId}-167`
37. Verifikasi jumlah baris System Log aktor untuk Name `Tools` sama dengan baseline langkah 28
38. Buka Activity Log dan cari baris Delete untuk `{runId}-167` serta `Tools`
39. Verifikasi Activity Log memuat tiga baris Delete: `Vehicle {runId}-167`, `Accessory {runId}-167`, dan `Accessory {runId}-167 › Cable {runId}-167`
40. Verifikasi jumlah baris Activity Log untuk `Tools` sama dengan baseline langkah 28

### TC-FA-CAT-477: Aksi yang gagal 5xx atau diblok guard tidak menulis baris log di surface mana pun

41. Catat baseline jumlah baris Changelog, System Log aktor, dan Activity Log untuk Category Name `Fail Edit {runId}-167` dan `Furniture`
42. Aktifkan intercept respons 500 pada request simpan Edit kategori
43. Klik elipsis (⋯) pada baris `Fail Edit {runId}-167` > `Edit`
44. Ubah Description menjadi `Gagal 500`, lalu klik `[Save]`
45. Verifikasi pesan kegagalan (toast) tampil
46. Lepas intercept respons 500
47. Klik icon close (✕) pada popup Edit
48. Verifikasi dialog `Unsaved Changes` tampil
49. Klik `[Leave]`
50. Klik elipsis (⋯) pada baris `Furniture` > `Delete`
51. Verifikasi dialog D-07 tampil
52. Klik `[OK]`
53. Hitung jumlah baris Changelog, System Log aktor, dan Activity Log untuk `Fail Edit {runId}-167` dan `Furniture` sesudah kedua aksi
54. Verifikasi jumlah baris Changelog, System Log aktor, dan Activity Log sama dengan baseline langkah 41 pada kedua kasus

### TC-FA-CAT-478: Aksi pada satu kategori tidak menghasilkan log untuk kategori yang tidak terlibat

55. Catat baseline jumlah baris Changelog untuk Category Name `Tools`
56. Klik elipsis (⋯) pada baris `Only Edit {runId}-167` > `Edit`
57. Ubah Description menjadi `Only me`, lalu klik `[Save]`
58. Buka Modal Changelog dan filter Category Name `Only Edit {runId}-167`
59. Verifikasi Changelog memuat baris Edit Field `Description` untuk `Only Edit {runId}-167`
60. Filter Category Name `Tools`
61. Verifikasi jumlah baris Changelog untuk Category Name `Tools` sama dengan baseline langkah 55 (tidak ada baris baru untuk `Tools`)

### TC-FA-CAT-473: Seed onboarding tidak dicatat di tiga surface

62. Ganti akun: logout, login sebagai Total Control pada client CatFresh (Pre-setup #25) dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Settings > Categories
63. Buka Modal Changelog
64. Verifikasi Changelog menampilkan empty state
65. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Default Category`
66. Verifikasi System Log aktor menampilkan empty state `No results found`
67. Buka Activity Log dan cari baris `Default Category`
68. Verifikasi Activity Log menampilkan empty state `No results found`

## Notes

- Spec absence (kelas g) memuat TC-FA-CAT-191, 192, 201, 464, 467, 473, 477, dan 478 dengan aksi nyata dan baseline sendiri (S-05). TC-FA-CAT-191 butir Post Condition ("Changelog, System Log, dan Activity Log tidak memuat baris baru") tidak punya langkah observasi di TC dan tidak diasersi; asersi tiga surface untuk aksi yang sama ada pada TC-FA-CAT-464 (langkah 22 sampai 27).
- Spec melewati sekitar 35 langkah (68). Alasan: delapan blok TC satu kelas (absence log) yang berdiri sendiri dengan user dan baseline sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Sekitar 30 langkah di antaranya adalah blok baca-log berpola (buka surface, cari entri atau hitung baris, lalu `Verifikasi`) yang tidak dihitung terhadap ambang (prinsip 13 bagian 3).
- Pemicu kelas lain pada spec absence mengikuti `P-5` butir (a): respons 500 yang dipaksa (TC-FA-CAT-477 langkah 42 sampai 46) dan Delete yang diblok guard (langkah 50 sampai 52) hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji.
- Anchor positif (bagian 8b butir 2): toast netral (langkah 5, 13, 25) sebagai respons server selesai untuk Edit tanpa perubahan; pesan kegagalan (langkah 45) dan dialog D-07 (langkah 51) untuk aksi gagal atau diblok; tiga baris Delete (langkah 33, 36, 39) untuk `Tools` yang dilewati; baris Edit `Description` (langkah 59) untuk kategori tidak terlibat; empty state `No results found` hasil Search untuk absence System Log dan Activity Log (langkah 66 dan 68) dan empty state Changelog (langkah 64).
- Langkah penghubung (S-03, S-09, R-16): langkah 1, 9, 16, 22, 28, 41, 55 (baseline), langkah 26, 53 (menghitung jumlah baris), langkah 32, 35, 38, 58, 60, 63, 65, 67 (membuka surface dan mencari entri), langkah 42 dan 46 (intercept), langkah 47 sampai 49 (menutup popup dirty: icon close, dialog `Unsaved Changes`, `[Leave]`).
- Langkah 25 (toast netral sebagai anchor TC-FA-CAT-464) memakai teks dari Expected TC-FA-CAT-191 butir a; TC-FA-CAT-464 tidak menyebut toast.
- Data milik spec menggantikan `Vehicle`, `Accessory`, dan `Cable` Pre-setup yang disebut TC-FA-CAT-467 serta target Edit `Furniture` pada TC-FA-CAT-477 dan 478 (S-06).
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan, termasuk untuk client CatFresh.
  - TC-FA-CAT-191 Post Condition menyebut tiga surface tanpa langkah observasi; tidak diasersi di TC itu.
  - TC-FA-CAT-192 Expected b hanya menyebut Changelog (bukan System Log dan Activity Log); spec mengikuti Changelog.
  - TC-FA-CAT-201 Expected b tidak menyebut surface; spec memeriksa Changelog Field `Code`. Precondition menyebut Pre-setup #39 `Heavy Tools` (Code `HT`) yang dipakai literal tanpa suffix karena Code hasil generate diturunkan dari nama.
  - TC-FA-CAT-473 Expected untuk System Log dan Activity Log ("tidak memuat baris untuk `Default Category`") tidak menyebut anchor; spec memakai Search nama sebagai anchor empty state `No results found` (teks diambil dari TC-FA-CAT-596 Expected a).
  - TC-FA-CAT-477 langkah 2 ("Paksa Edit `Furniture` gagal 500") tidak menyebut perubahan yang disimpan dan endpoint; spec memakai kategori milik spec dengan perubahan Description dan intercept pada request simpan Edit. TC-FA-CAT-477 juga tidak menyebut pesan kegagalan 5xx; langkah 45 hanya memverifikasi bahwa toast kegagalan tampil.
  - TC-FA-CAT-477 menyebut "Delete `Furniture` hingga muncul dialog D-07 lalu `[OK]`"; label tombol `[OK]` mengikuti TC.
  - TC-FA-CAT-467 langkah 1 menyebut Bulk Delete dengan `Continue` tanpa menyebut dialog; spec mengikuti dialog campuran (D-12) seperti TC-FA-CAT-634.
