---
id: TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir
title: "Dialog Bulk Delete: Homogen, Campuran, Blokir In-Use, Single, Daftar Panjang, dan Esc"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-113
  - TC-GS-UOM-114
  - TC-GS-UOM-117
  - TC-GS-UOM-119
  - TC-GS-UOM-120
  - TC-GS-UOM-121
  - TC-GS-UOM-122
  - TC-GS-UOM-258
coverage:
  web: automated
---

# Dialog Bulk Delete: Homogen, Campuran, Blokir In-Use, Single, Daftar Panjang, dan Esc

## Prerequisites

- Mode: FE+BE. Dialog muncul sesudah cek referensi ke backend nyata (Check References). Semua dialog dibatalkan (`[Cancel]`, `[OK]`) dan tidak ada unit yang dihapus.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data pre-setup Client A (data baca, hanya dibuka dialognya dan dibatalkan; tidak pernah dihapus atau diubah, Last Updated tidak berubah; pengecualian S-06 untuk aksi dibatalkan atau ditolak guard in-use): in-use `Box` (FAMS: 4 asset names) dan `Gram` (FAMS: 1 asset name); bebas relasi `Liter`, `Meter`, dan `Pack`.
- Data dinamis: Population D-01 (12 unit bebas relasi, nama literal tanpa suffix; pengecualian S-12): `Centimeter`, `Foot`, `Gallon`, `Inch`, `Milliliter`, `Millimeter`, `Ounce`, `Pound`, `Roll`, `Set`, `Sheet`, `Ton`. Di-seed idempotent oleh hook `before` (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat spec ini. Total baris tabel 20 (8 Pre-setup + 12 Population) diturunkan dari seeding.
- Daftar 15 unit bebas relasi untuk TC-GS-UOM-122: 12 unit Population D-01 di atas ditambah `Liter`, `Meter`, dan `Pack`.
- Kemampuan teknis: penekanan Esc; pembacaan container scrollable pada dialog.
- State global yang diubah: page size pagination (diubah ke 25 di langkah 1, dikembalikan ke 10 di langkah 57; hook `after` menjadi cadangan). Tidak ada state global lain yang diubah.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-113, TC-GS-UOM-258 (homogen), dan TC-GS-UOM-114: Dialog Bulk Delete homogen

1. Ubah page size tabel menjadi 25
2. Centang `Centimeter` dan `Millimeter`
3. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
4. Verifikasi dialog Title `Delete Units` (severity danger)
5. Verifikasi Body: bullet `Centimeter` dan `Millimeter`
6. Verifikasi Body: kalimat `Are you sure you want to delete them? This action cannot be undone.`
7. Verifikasi tombol `[Cancel]` dan `[Delete]`
8. Tekan Esc
9. Verifikasi dialog `Delete Units` homogen tetap terbuka
10. Klik [Cancel]
11. Verifikasi dialog tertutup
12. Verifikasi `Centimeter` dan `Millimeter` tetap ada di tabel
13. Verifikasi seleksi `Centimeter` dan `Millimeter` dipertahankan

### TC-GS-UOM-117 dan TC-GS-UOM-258 (campuran): Dialog Bulk Delete campuran

14. Klik `[✕]` pada Bulk Action Bar (membersihkan seleksi)
15. Centang `Liter`, `Pack`, dan `Box`
16. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
17. Verifikasi dialog Title `Delete Units` (warning) campuran tampil
18. Tekan Esc
19. Verifikasi dialog `Delete Units` campuran tetap terbuka
20. Klik [Cancel]
21. Verifikasi dialog tertutup
22. Verifikasi `Liter`, `Pack`, dan `Box` tetap ada di tabel

### TC-GS-UOM-119 dan TC-GS-UOM-258 (blokir): Dialog blokir seluruhnya in-use

23. Klik `[✕]` pada Bulk Action Bar
24. Centang `Box` dan `Gram`
25. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
26. Verifikasi dialog `Cannot Delete Data`: bullet `Box` dengan sub-bullet `FAMS (4 asset names)`
27. Verifikasi dialog `Cannot Delete Data`: bullet `Gram` dengan sub-bullet `FAMS (1 asset name)`
28. Verifikasi teks `Remove the references before deleting.`
29. Verifikasi dialog hanya memuat tombol `[OK]`
30. Verifikasi dialog tidak memuat kelompok will be deleted yang kosong (bukan Dialog campuran)
31. Tekan Esc
32. Verifikasi dialog `Cannot Delete Data` tetap terbuka
33. Klik [OK]
34. Verifikasi dialog tertutup
35. Verifikasi tidak ada toast
36. Verifikasi `Box` dan `Gram` tetap ada di tabel
37. Verifikasi checkbox `Box` dan `Gram` tetap tercentang
38. Verifikasi Bulk Action Bar tetap tampil

### TC-GS-UOM-121: Bulk Delete dengan satu baris in-use memakai dialog blokir single

39. Klik `[✕]` pada Bulk Action Bar
40. Centang `Box`
41. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
42. Verifikasi dialog `Cannot Delete Data` dengan satu bullet `Box`
43. Klik [OK]

### TC-GS-UOM-120: Bulk Delete dengan satu baris bebas relasi memakai dialog single

44. Klik `[✕]` pada Bulk Action Bar
45. Centang `Inch`
46. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
47. Verifikasi dialog Title `Delete Unit` (singular) dengan satu bullet `Inch`
48. Verifikasi kalimat `Are you sure you want to delete it? This action cannot be undone.`
49. Klik [Cancel]

### TC-GS-UOM-122: Daftar unit di dialog bulk tampil penuh dalam container scrollable

50. Klik `[✕]` pada Bulk Action Bar
51. Centang 15 unit bebas relasi: 12 unit Population D-01, `Liter`, `Meter`, dan `Pack`
52. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
53. Verifikasi dialog `Delete Units` menampilkan ke-15 nama dalam container scrollable
54. Verifikasi daftar tidak diringkas menjadi angka summary
55. Klik [Cancel]
56. Klik `[✕]` pada Bulk Action Bar
57. Ubah page size tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 57.
- Urutan TC dalam spec: 113/258/114, 117/258, 119/258, 121, 120, 122 (urutan sumber 113, 114, 117, 119, 120, 121, 122, 258). TC-GS-UOM-258 terbelah per jenis dialog dan digabung ke aksi yang memakai dialog sama: langkah 1 (Box dan Gram, blokir) ke TC-119, langkah 2 (campuran) ke TC-117, langkah 3 (homogen) ke TC-113 dan TC-114. TC-258 memakai pasangan unit berbeda (`Meter` dan `Box` untuk campuran, `Meter` dan `Milliliter` untuk homogen); spec memakai pasangan unit TC-117 dan TC-113 untuk dialog yang sama jenisnya, karena perilaku Esc dan Cancel tidak bergantung pada nama unit (permutasi data yang tidak menambah alur baru, bagian 2 konvensi). Jumlah buka dialog menjadi lebih sedikit.
- Spec ini 57 langkah (di atas batas 35 langkah); alasan pertahanan: seluruhnya satu dataset dan satu kelas (dialog Bulk Delete dibuka lalu dibatalkan), tidak ada aksi yang mengubah data, dan tiap blok diawali pembersihan seleksi (`[✕]`) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Aksi `Delete` yang dikonfirmasi ada di spec 034.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14, 23, 39, 44, 50, dan 56 (membersihkan seleksi, S-09); langkah 43 dan 49 (menutup dialog yang kontennya sudah diasersi; TC-120 dan TC-121 tidak menyebut cara menutup dialog); langkah 1 dan 57 (mengubah dan memulihkan page size 25 agar ke-20 unit tabel tampil pada satu halaman, sehingga baris yang pada baseline ada di halaman 2 seperti `Millimeter` dan `Pack` dapat dicentang tanpa pindah halaman dan 15 unit dapat dicentang sekaligus).
- Langkah 5 dan 6 serta 27 dan 28: Expected dipecah per klausa (bullet, lalu kalimat atau teks penutup; untuk TC-119 butir a: bullet `Box`, bullet `Gram`, teks penutup); langkah 30 mengasersi butir b ("Must NOT" Dialog dengan kelompok will be deleted kosong).
- TC-GS-UOM-119 Expected butir c ("klik [OK]: 0 terhapus, tanpa toast") diasersi di langkah 35 dan 36; butir d di langkah 37 dan 38. Klik [OK] adalah langkah 33, setelah Esc dari TC-258 butir a (langkah 31 dan 32).
- Unit Population dan Pre-setup yang dicentang hanya dibuka dialog hapusnya dan dibatalkan; tidak ada penghapusan di spec ini (pengecualian S-06).
- Tidak ada pembagian TC lintas spec lain; TC-116 dan TC-118 (dialog campuran dengan konfirmasi `[Continue]`) ada di spec 034.
- Temuan untuk QA: TC-GS-UOM-122 menyebut "15 unit bebas relasi tersedia (Population + Data Dinamis)"; spec memakai 12 Population ditambah tiga Pre-setup bebas relasi (`Liter`, `Meter`, `Pack`) sehingga tidak bergantung data dinamis spec lain. Perlu konfirmasi bahwa ketiganya bebas relasi di environment automation.
