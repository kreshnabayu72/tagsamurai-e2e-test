---
id: TC-GS-UCF-E2E-073-sinkronisasi-ke-fixed-asset-dan-admin-console
title: "Sinkronisasi Custom Field ke Kolom Curated Fixed Asset Settings User, Admin Console Settings User, dan Popup Total User Detail Admin Console Settings Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-297
  - TC-GS-UCF-538
  - TC-GS-UCF-298
  - TC-GS-UCF-299
  - TC-GS-UCF-539
coverage:
  web: automated
---

# Sinkronisasi Custom Field ke Kolom Curated Fixed Asset Settings User, Admin Console Settings User, dan Popup Total User Detail Admin Console Settings Group

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) untuk TC-GS-UCF-297 dan 538. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control (Principal) Hendra Wijaya `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup TC; instance Principal) untuk TC-GS-UCF-298, 299, dan 539, login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`.
  - Pelaku pemicu pada TC-GS-UCF-539 (sesi A pada TC): Sari Dewi lewat sesi API (P-2) hanya menonaktifkan field; sesi B (objek asersi) adalah sesi utama Hendra Wijaya. Mekanisme sesi API disediakan tim FE/BE.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah pertama tiap TC berpindah ke Fixed Asset atau Admin Console.
- Data Pre-setup (baca-saja): Login User Rahmat Hidayat `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Pre-setup TC; tidak diubah selain nilai Custom Field milik spec) sebagai pemilik nilai. Group tempat Rahmat Hidayat berada di Admin Console tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Data Dinamis (nama bersuffix `{runId}-073`; fixture baru `Fixture.customFieldUser.consumer073`), di-seed lewat API oleh Sari Dewi di hook `before`:
  - `Consumer Probe {runId}-073` (Text, Active; nilai User Rahmat Hidayat = `Probe Value`; D-89) untuk TC-GS-UCF-297, 298, dan 299.
  - `Lifecycle FA Probe {runId}-073` (Text, Active; nilai User Rahmat Hidayat = `FA Value`; D-237) untuk TC-GS-UCF-538, di-rename oleh spec menjadi `Lifecycle FA Renamed {runId}-073`.
  - `Lifecycle Group Probe {runId}-073` (Text, Active; nilai User Rahmat Hidayat = `Group Value`; D-238) untuk TC-GS-UCF-539, dinonaktifkan oleh spec.
  - Mekanisme seeding nilai User (Rahmat Hidayat) disediakan tim FE/BE.
- State Setup Column default (precondition TC): tabel User Fixed Asset Settings, tabel User Admin Console Settings, dan popup Users Admin Console Settings Group; hook `beforeEach` membersihkan cache browser. Tiap TC yang mengubah konfigurasi memulihkannya lewat `[Reset to Default]` dan `[Save]` sebagai langkah eksplisit.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Custom Field bersuffix `{runId}-073` yang masih ada; kembalikan sesi ke Sari Dewi.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (Sari Dewi dan Hendra Wijaya) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: ganti akun (logout lalu login) dan akses ke Fixed Asset dan Admin Console; sesi API Sari Dewi untuk menonaktifkan field; seeding nilai User lewat API.
- State global: tidak ada yang diubah selain flag Guided Tooltip, sesi akun, dan konfigurasi Setup Column (dipulihkan seperti di atas).

## Test Steps

### TC-GS-UCF-297: Field aktif tersedia sebagai kolom curated di Fixed Asset > Settings > User

1. Buka Fixed Asset > Settings > User
2. Buka Modal Setup Column (header Column Visibility (⋯) > `Setup Column...`)
3. Verifikasi kolom `Consumer Probe {runId}-073` tersedia pada daftar Setup Column
4. Verifikasi kolom `Consumer Probe {runId}-073` dalam keadaan tidak tercentang (Curated)
5. Centang kolom `Consumer Probe {runId}-073`
6. Klik `[Save]`
7. Ketik Search `Rahmat Hidayat` pada tabel User, tekan Enter
8. Verifikasi kolom `Consumer Probe {runId}-073` tampil pada tabel
9. Verifikasi nilai `Probe Value` pada baris Rahmat Hidayat
10. Buka Modal Setup Column, klik `[Reset to Default]`, klik `[Save]`

### TC-GS-UCF-538: Rename Field Name tercermin pada label kolom curated Fixed Asset > Settings > User dengan nilai tetap

11. Buka Modal Setup Column (header Column Visibility (⋯) > `Setup Column...`)
12. Verifikasi daftar kolom curated memuat `Lifecycle FA Probe {runId}-073`
13. Klik `[✕]`
14. Buka Global Settings > User > Custom Field
15. Ketik Search `Lifecycle FA Probe {runId}-073`, tekan Enter
16. Klik `⋯` pada baris `Lifecycle FA Probe {runId}-073`, pilih `Edit`
17. Ubah Field Name menjadi `Lifecycle FA Renamed {runId}-073`
18. Klik `[Save]`
19. Tunggu aksi selesai (modal tertutup)
20. Buka Fixed Asset > Settings > User
21. Buka Modal Setup Column (header Column Visibility (⋯) > `Setup Column...`)
22. Verifikasi daftar kolom curated memuat `Lifecycle FA Renamed {runId}-073`
23. Verifikasi daftar kolom curated tidak memuat `Lifecycle FA Probe {runId}-073`
24. Centang kolom `Lifecycle FA Renamed {runId}-073`
25. Klik `[Save]`
26. Ketik Search `Rahmat Hidayat` pada tabel User, tekan Enter
27. Verifikasi header kolom berlabel `Lifecycle FA Renamed {runId}-073`
28. Verifikasi nilai `FA Value` pada baris Rahmat Hidayat
29. Buka Modal Setup Column, klik `[Reset to Default]`, klik `[Save]`

### TC-GS-UCF-298: Field aktif tersedia sebagai kolom curated dan accordion read-only di Admin Console > Settings > User

30. Ganti akun: logout dari Total Control Client A Sari Dewi
31. Login sebagai Total Control (Principal) Hendra Wijaya (`Spectra.env.GS_PRINCIPAL_TC_PASSWORD`)
32. Buka Admin Console > Settings > User
33. Aktifkan kolom curated `Consumer Probe {runId}-073` lewat Setup Column (centang, `[Save]`)
34. Ketik Search `Rahmat Hidayat` pada tabel User, tekan Enter
35. Verifikasi kolom `Consumer Probe {runId}-073` tampil pada tabel
36. Verifikasi nilai `Probe Value` pada baris Rahmat Hidayat
37. Buka Detail Rahmat Hidayat
38. Expand accordion Custom Field
39. Verifikasi accordion Custom Field memuat `Consumer Probe {runId}-073: Probe Value`
40. Verifikasi isi accordion Custom Field bersifat read-only
41. Kembali ke Admin Console > Settings > User
42. Buka Modal Setup Column, klik `[Reset to Default]`, klik `[Save]`

### TC-GS-UCF-299: Field aktif tersedia sebagai kolom di popup Total User Detail Admin Console > Settings > Group

43. Buka Admin Console > Settings > Group
44. Klik angka kolom Total User pada group tempat Rahmat Hidayat berada
45. Aktifkan kolom `Consumer Probe {runId}-073` lewat Setup Column popup Users (centang, `[Save]`)
46. Verifikasi popup `Users` memuat kolom `Consumer Probe {runId}-073`
47. Verifikasi nilai `Probe Value` pada baris Rahmat Hidayat
48. Buka Setup Column popup Users, klik `[Reset to Default]`, klik `[Save]`
49. Tutup popup `Users`

### TC-GS-UCF-539: Deactivate field menghilangkan kolom curated dari Setup Column popup Total User Detail Group

50. Klik angka kolom Total User pada group tempat Rahmat Hidayat berada
51. Buka Setup Column popup Users
52. Verifikasi Setup Column popup Users memuat kolom curated `Lifecycle Group Probe {runId}-073`
53. Tutup Setup Column popup Users
54. Sesi A (Sari Dewi, sesi API) menonaktifkan `Lifecycle Group Probe {runId}-073` hingga tersimpan
55. Tutup popup `Users`
56. Klik angka kolom Total User pada group yang sama
57. Buka Setup Column popup Users
58. Verifikasi Setup Column popup Users memuat kolom curated `Consumer Probe {runId}-073` (pembanding: daftar sudah termuat)
59. Verifikasi Setup Column popup Users tidak memuat kolom `Lifecycle Group Probe {runId}-073`
60. Tutup Setup Column popup Users
61. Tutup popup `Users`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 297, 538, 298, 299, 539. TC-GS-UCF-297 dan 538 (akun Sari Dewi, Fixed Asset) dikerjakan lebih dulu, lalu ganti akun ke Hendra Wijaya (Principal) untuk TC-GS-UCF-298, 299, dan 539. Urutan ini sama dengan urutan TC sumber setelah pengelompokan per akun.
- Pada TC-GS-UCF-539 sesi A (pemicu Deactivate) dilakukan lewat sesi API karena hanya berfungsi sebagai pemicu (P-2) dan objek asersi adalah sesi Principal; langkah pemicunya ditulis "hingga ... tersimpan". Kegagalan satu sesi tidak memengaruhi bagian lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): pindah halaman (Fixed Asset, Admin Console, Global Settings), pengisian Search tabel, pemulihan konfigurasi Setup Column lewat `[Reset to Default]` dan `[Save]` (S-09), penutupan popup Setup Column dan popup Users, ganti akun, dan "Tunggu aksi selesai (modal tertutup)" sesudah `[Save]` rename (bagian 8b butir 8).
- Spec melewati sekitar 35 langkah (61 langkah) mendekati ambang. Seluruhnya satu topik (sinkronisasi Custom Field ke konsumen lintas modul), tiap TC memakai field bersuffix sendiri dan berdiri sendiri; ganti akun (langkah eksplisit) membuat bagian Principal tetap bermakna walau bagian Sari Dewi gagal.
- Pembagian TC lintas spec: konsumen Create User, Detail User, dan My Profile ada di spec 072; Staging Table Import di spec 074.
- Temuan untuk QA:
  - Teks UI konsumen lintas modul diikuti TC dan tidak diverifikasi ke PRD modul lain: `Setup Column...`, kolom curated, accordion `Custom Field`, popup `Users`, dan kolom Total User berasal dari `fixed-asset/settings-user`, `admin-console/settings-user`, dan `admin-console/settings-group` (PRD modul lain); penulis spec tidak menelusuri teks yang diserahkan ke dokumen lain.
  - TC-GS-UCF-299 dan 539 menyebut "group tempat Rahmat Hidayat berada" tanpa nama group; Pre-setup TC modul ini tidak memuat group. Spec memakai group itu tanpa nama dan menyatakan identitas group sebagai disediakan tim FE.
  - TC-GS-UCF-298 menyebut "Total Control (Principal)" tanpa Client tempat Rahmat Hidayat berada; spec memakai Search `Rahmat Hidayat` pada tabel User Admin Console.
  - TC-GS-UCF-298 Expected b dan TC-GS-UCF-297 Expected b: sifat read-only dan tidak tercentang (Curated) mengikuti teks TC; TC tidak menjelaskan wujud read-only.
  - TC-GS-UCF-538 dan 539 menyebut dua sesi (A dan B); spec menyederhanakannya menjadi satu sesi utama dengan pemicu sesi API pada TC-GS-UCF-539 dan satu sesi pada TC-GS-UCF-538.
  - Post Condition TC-GS-UCF-538 (`Lifecycle FA Renamed`) dan 539 (`Lifecycle Group Probe` Inactive) tidak punya langkah observasi tambahan.
  - TC-GS-UCF-297 dan 538 menyebut "baris Rahmat Hidayat" tanpa cara menemukan baris pada tabel User Fixed Asset; spec memakai Search `Rahmat Hidayat` sebagai langkah penghubung.
