---
id: TC-GS-ACTLOG-E2E-043-kontrol-umum-filter-panel-visibilitas-kolom-keyboard-opsi-dan-header
title: "Kontrol Umum Filter Panel: Visibilitas Kolom, Keyboard, Opsi Tanpa None, Header Kolom"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-111
  - TC-GS-ACTLOG-112
  - TC-GS-ACTLOG-115
  - TC-GS-ACTLOG-116
coverage:
  web: automated
---

# Kontrol Umum Filter Panel: Visibilitas Kolom, Keyboard, Opsi Tanpa None, Header Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Password user dinamis uji: `Spectra.env.ACTLOG_PASSWORD` (env baru) untuk aktivasi dan Login user dinamis di bawah.
- Data Dinamis (bersuffix `{runId}-043`, di-seed lewat API di hook `before`, dihapus di hook `after`):
  - Position `Supervisor {runId}-043` dan Division `Operations {runId}-043` serta `Finance {runId}-043`.
  - User `Budi Anwar {runId}-043` (email `budianwar+{runId}-043@qwertysystem.net`, Position `Supervisor {runId}-043`, Division `Operations {runId}-043`, Employee ID terisi) dan User `Siti Nurbaya {runId}-043` (email `sitinurbaya+{runId}-043@qwertysystem.net`, Division awal `Finance {runId}-043` lalu diubah ke `Operations {runId}-043` lewat API sehingga ada baris User Action Edit Field `Division`; tanpa Position dan tanpa Employee ID), nilai field wajib lain dari `Fixture.activityLog.userDasar` (fixture baru berisi Position, Employee ID, dan field wajib lain di luar Name, email, dan Division). Keduanya menjalankan Login lewat alur Auth sehingga memiliki baris Session; pembuatan `Siti Nurbaya {runId}-043` menghasilkan baris User Action Object `User`.
  - Brand `Acme Corp {runId}-043` dibuat lewat API sehingga menghasilkan baris User Action Object `Brand`.
- Kemampuan teknis (disediakan tim FE/BE): seed BE satu baris User Action dengan Name kosong dan Field kosong (kedua nilai tampil `—`) milik entitas Client A; baris dengan Name atau Field kosong tidak dapat dihasilkan lewat aksi nyata dalam satu run kecuali Import massal (TC-GS-ACTLOG-149 di spec 038).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- State global yang diubah: konfigurasi kolom tabel yang disembunyikan pada TC-GS-ACTLOG-111 (dikembalikan oleh langkah pemulihan; hook `after` memulihkan lewat [Reset to Default] sebagai cadangan). Hook `after` menghapus user, Position, Division, dan brand milik spec ini. Entri log tidak dapat dihapus (ACTLOG-LOGIC-01); seed memakai nama bersufiks run sehingga run berikutnya tidak bentrok, dan asersi tahan terhadap baris dari run lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-111: Menyembunyikan kolom tidak menghilangkan field Filter dan tidak membatalkan filter yang diterapkan

1. Buka Global Settings > Activity Log > Tab "Session", klik icon Filter, pilih Position `Supervisor {runId}-043`, klik [Apply]
2. Sembunyikan kolom Position lewat Overlay Column Visibility
3. Verifikasi baris `Budi Anwar {runId}-043` tampil di Tab Session
4. Verifikasi baris `Siti Nurbaya {runId}-043` tidak tampil di Tab Session
5. Klik icon Filter untuk membuka Filter Panel
6. Verifikasi field `Position` tetap ada di Filter Panel Tab Session
7. Verifikasi field `Position` bernilai `Supervisor {runId}-043`
8. Tutup Filter Panel tanpa [Apply], lalu tampilkan kembali kolom Position lewat Overlay Column Visibility
9. Klik tab "User Action", klik icon Filter, pilih Object `User`, klik [Apply]
10. Sembunyikan kolom Object lewat Overlay Column Visibility
11. Verifikasi baris Name `Siti Nurbaya {runId}-043` tampil di Tab User Action
12. Verifikasi baris Name `Acme Corp {runId}-043` tidak tampil di Tab User Action
13. Klik icon Filter untuk membuka Filter Panel
14. Verifikasi field `Object` tetap ada di Filter Panel Tab User Action
15. Verifikasi field `Object` bernilai `User`

### Pemulihan state antar TC

16. Tutup Filter Panel tanpa [Apply], tampilkan kembali kolom Object lewat Overlay Column Visibility, lalu klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-112: Field multi-select Filter Panel dapat dioperasikan dengan keyboard

17. Buka Global Settings > Activity Log > Tab "Session", klik icon Filter, tekan Tab hingga fokus tiba di field Activity (urutan field: Date, User, Position, Division, Activity, Status)
18. Verifikasi field Activity menerima fokus di Tab Session
19. Buka daftar opsi dengan Enter
20. Verifikasi daftar opsi field Activity terbuka di Tab Session
21. Pindah antar opsi dengan tombol panah, lalu centang `Login` dengan Spasi
22. Verifikasi opsi `Login` tercentang di Tab Session
23. Tutup daftar opsi dengan Esc
24. Verifikasi opsi `Login` menjadi chip di field Activity Tab Session
25. Pindahkan fokus ke [Apply] dengan tombol Tab, lalu tekan Enter
26. Verifikasi hasil tabel Tab Session sama dengan pemilihan Activity `Login` memakai mouse
27. Klik tab "User Action", klik icon Filter, tekan Tab hingga fokus tiba di field Action (urutan field: Date, Action, Object, Field, Modified By)
28. Verifikasi field Action menerima fokus di Tab User Action
29. Buka daftar opsi dengan Enter
30. Verifikasi daftar opsi field Action terbuka di Tab User Action
31. Pindah antar opsi dengan tombol panah, lalu centang `Create` dengan Spasi
32. Verifikasi opsi `Create` tercentang di Tab User Action
33. Tutup daftar opsi dengan Esc
34. Verifikasi opsi `Create` menjadi chip di field Action Tab User Action
35. Pindahkan fokus ke [Apply] dengan tombol Tab, lalu tekan Enter
36. Verifikasi hasil tabel Tab User Action sama dengan pemilihan Action `Create` memakai mouse

### Pemulihan state antar TC

37. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-115: Daftar opsi filter tidak memuat opsi kosong atau None

38. Pada Tab Session klik icon Filter, buka daftar opsi field Position
39. Verifikasi opsi `Supervisor {runId}-043` ada di daftar opsi Position
40. Verifikasi daftar opsi Position tidak memuat `None`, `—`, atau opsi kosong
41. Buka daftar opsi field Division
42. Verifikasi opsi `Operations {runId}-043` ada di daftar opsi Division
43. Verifikasi daftar opsi Division tidak memuat `None`, `—`, atau opsi kosong
44. Klik tab "User Action", klik icon Filter, buka daftar opsi field Field
45. Verifikasi opsi `Division` ada di daftar opsi Field
46. Verifikasi daftar opsi Field tidak memuat `None`, `—`, atau opsi kosong

### Pemulihan state antar TC

47. Tutup Filter Panel tanpa [Apply]

### TC-GS-ACTLOG-116: Header kolom Column Visibility (⋯) tidak memiliki ikon sort

48. Klik tab "Session", lalu catat urutan baris tabel
49. Amati header kolom `Column Visibility (⋯)` di Tab Session
50. Verifikasi tidak ada ikon sort pada header `Column Visibility (⋯)` di Tab Session
51. Klik header kolom `Column Visibility (⋯)`
52. Verifikasi klik header membuka Overlay Column Visibility di Tab Session
53. Verifikasi urutan baris Tab Session tidak berubah
54. Tutup Overlay Column Visibility, klik tab "User Action", lalu catat urutan baris tabel
55. Amati header kolom `Column Visibility (⋯)` di Tab User Action
56. Verifikasi tidak ada ikon sort pada header `Column Visibility (⋯)` di Tab User Action
57. Klik header kolom `Column Visibility (⋯)`
58. Verifikasi klik header membuka Overlay Column Visibility di Tab User Action
59. Verifikasi urutan baris Tab User Action tidak berubah

### Pemulihan state akhir

60. Tutup Overlay Column Visibility

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Urutan TC-GS-ACTLOG-111, 112, 115, 116 dipertahankan.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 49, 55 (mengamati header), langkah 48 dan 54 (mencatat urutan baris sebagai pembanding), serta langkah pemulihan 8, 16, 37, 47, 54 (bagian penutupan overlay), dan 60.
- Spec di atas smell 35 langkah (60 langkah nominal, tanpa perulangan). Alasan: keempat blok memakai kontrol Filter Panel dan header tabel yang sama pada dua tab, tiap blok dimulai dari state default dan berdiri sendiri; sebagian besar langkah adalah `Verifikasi` yang dipecah per klausa (S-01) untuk dua tab.
- Asersi tambahan di luar Expected TC: langkah 3, 4, 11, dan 12 menyebut baris contoh mana yang tampil atau tidak tampil sebagai bukti tabel tersaring, karena kolom Position dan Object disembunyikan dan penyaringan tidak lagi terbaca dari kolom itu. Langkah 39, 42, dan 45 (opsi `Supervisor {runId}-043`, `Operations {runId}-043`, dan `Division` ada di daftar) adalah anchor positif untuk asersi absence langkah 40, 43, dan 46 (8b.2); langkah 4 dan 12 didahului baris pembanding yang tampil (langkah 3 dan 11).
- Langkah 17 dan 27 memindahkan fokus dengan tombol Tab sesuai urutan field Filter Panel; langkah 25 dan 35 memindahkan fokus ke [Apply] dengan tombol Tab.
- Temuan untuk QA:
  - Env baru `ACTLOG_PASSWORD` perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-111 menyebut "Overlay Column Visibility" untuk menyembunyikan kolom, sedangkan TC lain (TC-117) memakai "Popup Setup Column" dengan [Save]; spec memakai istilah TC-111 dan tidak menyebut [Save], dan kebutuhan menyimpan konfigurasi kolom perlu dikonfirmasi QA.
  - TC-112 tidak menyebut jumlah tekan Tab menuju field maupun menuju [Apply], dan Expected "hasil tabel sama dengan pemilihan memakai mouse" tidak punya pembanding mouse dalam langkah TC; spec mengikuti TC apa adanya.
  - TC-115 mensyaratkan sel kosong pada Position dan Employee ID (Session) serta Name dan Field (User Action); kebutuhan seed kosong dicatat di Prerequisites.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah 5 dan 13 (klik icon Filter untuk membuka panel sesudah [Apply]) mengikuti pola TC.
  - Post Condition semua TC bernilai `-`; tidak diasersi.
