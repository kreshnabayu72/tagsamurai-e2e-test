---
id: TC-AC-ACAL-E2E-035-kontrol-filter-panel-pencarian-opsi-chip-overflow-clear-dan-indikator
title: "Kontrol Filter Panel: Pencarian Opsi, Chip, Overflow, Tutup Tanpa Apply, Clear, dan Indikator"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-64
  - TC-AC-ACAL-65
  - TC-AC-ACAL-66
  - TC-AC-ACAL-67
  - TC-AC-ACAL-68
  - TC-AC-ACAL-69
  - TC-AC-ACAL-70
coverage:
  web: automated
---

# Kontrol Filter Panel: Pencarian Opsi, Chip, Overflow, Tutup Tanpa Apply, Clear, dan Indikator

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Pre-setup (nama literal, pengecualian S-12 Lampiran A-3 karena opsi dropdown dan chip bergantung pada nama; seeding idempotent, tidak dihapus spec ini):
  - Tab Session (Pre-setup No 9 dan 12): baris Session untuk enam user `John Doe` (Division `Marketing`, Position `Staff`), `Jane Smith` (Division `Finance`), `John Dalton`, `John Davis`, `Ani`, dan `Budi Santoso`, sehingga dropdown User berisi sedikitnya enam opsi, dropdown Division berisi `Finance` dan `Marketing`, dan tabel memuat baris Division `Marketing` serta `Finance`. Nama `John Doe`, `John Dalton`, dan `John Davis` memuat `jo`; `Jane Smith`, `Ani`, dan `Budi Santoso` tidak.
  - Tab User Action (Pre-setup No 10): sedikitnya satu entri Object `Partner` (contoh PRD §4.1.2, Action `Suspend`), sehingga dropdown Object memuat opsi `Partner`.
- Kondisi viewport TC-AC-ACAL-67: lebar viewport diatur sehingga enam chip user tidak muat dalam satu baris field User pada langkah 30 sampai 34; nilai lebar ditetapkan tim FE (TC tidak menyebut angkanya). Pengaturan viewport (langkah 29) dan pemulihannya (langkah 36) adalah langkah penghubung.
- Placeholder field Filter Panel tab Session (PRD §4.1.1): Date `Select date`, User `All users`, Position `All positions`, Division `All divisions`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah total `Z` pada pagination (`Showing X–Y of Z entries`) sebagai baseline (langkah 50 dan 58). Total entri audit trail tidak diasersi sebagai angka absolut; asersi memakai selisih terhadap `Z` yang dicatat.
- State yang diubah dan dipulihkan: Filter tab Session (dibersihkan di langkah 48 dan 57); draft Filter Panel tab User Action dibuang tanpa [Apply] (langkah 9). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-64: Pencarian di dalam dropdown filter, kedua tab

1. Klik icon Filter pada tab Session, buka dropdown User, ketik `jo` pada pencarian opsi
2. Verifikasi sedikitnya satu opsi tampil di dropdown User
3. Verifikasi setiap opsi yang tampil di dropdown User memuat `jo` (tidak case-sensitive)
4. Ganti isi pencarian opsi dropdown User dengan `zzz`
5. Verifikasi tidak ada opsi yang cocok di dropdown User
6. Tutup dropdown dengan Esc, tutup Filter Panel tanpa [Apply] dengan klik icon Filter, lalu klik tab "User Action"
7. Klik icon Filter, buka dropdown Object, ketik `PART` pada pencarian opsi
8. Verifikasi opsi `Partner` tampil di dropdown Object
9. Tutup dropdown dengan Esc, tutup Filter Panel tanpa [Apply] dengan klik icon Filter, lalu klik tab "Session"

### TC-AC-ACAL-65: Hapus chip lewat `✕` menghapus centang opsi terkait (chip ke checkbox)

10. Klik icon Filter, buka dropdown Division, centang `Finance` dan `Marketing`, lalu tutup dropdown dengan Esc
11. Verifikasi dua chip `Finance` dan `Marketing` tampil di dalam field Division
12. Klik `✕` pada chip `Finance` tanpa membuka dropdown
13. Verifikasi chip `Finance` hilang dari field Division
14. Verifikasi chip `Marketing` tetap tampil di field Division
15. Buka dropdown Division
16. Verifikasi opsi `Finance` ter-uncheck
17. Verifikasi opsi `Marketing` tetap tercentang
18. Klik [Apply]
19. Verifikasi sedikitnya satu baris tampil di tab Session
20. Verifikasi setiap baris tabel ber-Division `Marketing`

### TC-AC-ACAL-66: Uncheck opsi di dalam dropdown menghapus chip (checkbox ke chip)

21. Klik icon Filter, klik [Clear Field], buka dropdown Division, centang `Finance` dan `Marketing`
22. Verifikasi dua chip `Finance` dan `Marketing` tampil di dalam field Division
23. Di dalam dropdown yang terbuka, uncheck `Marketing`
24. Verifikasi chip `Marketing` hilang dari field Division
25. Verifikasi chip `Finance` tetap tampil di field Division
26. Klik [Apply]
27. Verifikasi sedikitnya satu baris tampil di tab Session
28. Verifikasi setiap baris tabel ber-Division `Finance`

### TC-AC-ACAL-67: Overflow chip menjadi `+N more`

29. Atur lebar viewport sehingga enam chip tidak muat dalam satu baris (nilai ditetapkan tim FE)
30. Klik icon Filter, klik [Clear Field], buka dropdown User, centang enam user `John Doe`, `Jane Smith`, `John Dalton`, `John Davis`, `Ani`, dan `Budi Santoso`, lalu tutup dropdown dengan Esc
31. Verifikasi chip user yang muat tampil di dalam field User dan sisanya diringkas dalam satu chip `+N more`
32. Verifikasi jumlah chip user yang tampil ditambah N sama dengan 6
33. Verifikasi field User tidak melebar keluar Filter Panel
34. Verifikasi field User tidak digulir horizontal
35. Klik [Clear Field], lalu tutup Filter Panel tanpa [Apply] dengan klik icon Filter
36. Pulihkan lebar viewport

### TC-AC-ACAL-68: Menutup Filter Panel tanpa [Apply] membuang perubahan

37. Klik icon Filter, klik [Clear Field], buka dropdown Division, centang `Finance`, klik [Apply]
38. Klik icon Filter, buka dropdown Division, centang `Marketing`, lalu klik icon Filter lagi (tutup)
39. Verifikasi sedikitnya satu baris tampil di tab Session
40. Verifikasi setiap baris tabel ber-Division `Finance` (tabel tetap hasil `Finance` saja)
41. Klik icon Filter
42. Verifikasi field Division hanya berisi `Finance`

### TC-AC-ACAL-70: Indikator dot pada icon Filter saat filter aktif

43. Klik [Clear Field], buka dropdown User, centang `John Doe` dan `Jane Smith`, buka dropdown Division, centang `Marketing`, klik [Apply]
44. Verifikasi icon Filter menampilkan indikator dot tanpa angka
45. Klik icon Filter, klik `✕` pada chip `Marketing` di field Division, klik [Apply]
46. Verifikasi indikator dot pada icon Filter tetap tampil
47. Verifikasi indikator dot pada icon Filter tanpa angka
48. Klik icon Filter, klik [Clear Field], klik [Apply]
49. Verifikasi indikator dot pada icon Filter hilang

### TC-AC-ACAL-69: [Clear Field] lalu [Apply] mengembalikan semua data

50. Catat jumlah total entri `Z` pada pagination tab Session tanpa filter
51. Klik icon Filter, buka dropdown User, centang `John Doe`, klik satu tanggal `1 Jan 2020` pada field Date, klik [Apply]
52. Klik icon Filter, klik [Clear Field]
53. Verifikasi field Date kembali ke placeholder `Select date`
54. Verifikasi field User kembali ke placeholder `All users`
55. Verifikasi field Position kembali ke placeholder `All positions`
56. Verifikasi field Division kembali ke placeholder `All divisions`
57. Klik [Apply]
58. Verifikasi jumlah total entri pada pagination sama dengan `Z` (tabel menampilkan semua data dalam scope)
59. Verifikasi indikator dot pada icon Filter hilang

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 64, 65, 66, 67, 68, 70, 69 (TC-AC-ACAL-69 terakhir karena memakai tabel tanpa filter sebagai pembanding setelah semua filter dibersihkan). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (59 langkah, tanpa perulangan sehingga nominal sama dengan ekspansi). Alasan: seluruh blok berada di satu kelas harness (fungsional kontrol Filter Panel), memakai satu dataset (log Session dan User Action Principal), dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap TC memulai dengan [Clear Field] atau membangun filternya sendiri. Tidak ada langkah berulang.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6 dan 9 (menutup dropdown dan Filter Panel tanpa [Apply], pindah tab), langkah 21, 30, 37, dan 43 ([Clear Field] membuang filter dari TC sebelumnya, S-09), langkah 35 (membuang draft overflow), langkah 48 dan 52 (pemulihan filter), langkah 50 (baseline `Z`, S-12), langkah 29 dan 36 (mengatur lebar viewport agar enam chip tidak muat dalam satu baris, nilai ditetapkan tim FE, dan memulihkannya setelah blok TC-AC-ACAL-67; S-03).
- Asersi "setiap baris" (langkah 20, 28, 40) didahului `Verifikasi` sedikitnya satu baris tampil (langkah 19, 27, 39) sebagai pembanding universal (bagian 8b butir 2).
- Langkah 5 (tidak ada opsi cocok) didahului langkah 2 yang membuktikan dropdown yang sama menampilkan opsi; langkah 49 dan 59 (dot hilang) adalah absence elemen UI dengan Table Tools sebagai anchor permukaan.
- Langkah 58 mengasersi "semua data dalam scope" lewat total `Z` yang dicatat di langkah 50, bukan angka absolut (S-12).
- Temuan untuk QA:
  - TC-AC-ACAL-64 Expected b tidak menyebut teks atau tampilan saat tidak ada opsi cocok; spec hanya mengasersi tidak ada opsi.
  - TC-AC-ACAL-65, 66, 68: TC tidak menyebut apakah [Apply] menutup Filter Panel; langkah "klik icon Filter" sesudah [Apply] (langkah 38 dan 41) mengikuti pola TC dan bergantung pada panel tertutup sesudah [Apply]. PRD `prd-conventions.md` §9.8 tidak menetapkannya.
  - TC-AC-ACAL-67 menyebut enam user `John Doe`, `Jane Smith`, `John Dalton`, `John Davis`, `Ani`, dan `Budi Santoso` serta kondisi viewport (lebar diatur sehingga enam chip tidak muat dalam satu baris); spec mengikuti keduanya. Nilai lebar viewport ditetapkan tim FE (langkah 29); bila enam chip muat seluruhnya `+N more` tidak muncul dan langkah 31 gagal.
  - TC-AC-ACAL-69 tidak menyebut nilai filter User dan Date yang aktif; spec memakai `John Doe` dan satu tanggal `1 Jan 2020`. TC menyebut placeholder tanpa teks; teks diambil dari PRD §4.1.1.
  - TC-AC-ACAL-70 langkah 2 ("Clear satu field") tidak menyebut cara; spec menghapus chip `Marketing` lewat `✕`.
  - Post Condition ketujuh TC bernilai `-`; tidak diasersi.
  - `AC_TC_PASSWORD` terdaftar di `.env.example` dan `spectra.config.ts`; Pre-setup TC memakai placeholder `{namaCompany}` pada email akun, nilainya ditetapkan tim FE.
