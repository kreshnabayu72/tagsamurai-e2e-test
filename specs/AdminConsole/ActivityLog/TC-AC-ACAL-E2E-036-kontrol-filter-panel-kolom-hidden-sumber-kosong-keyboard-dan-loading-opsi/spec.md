---
id: TC-AC-ACAL-E2E-036-kontrol-filter-panel-kolom-hidden-sumber-kosong-keyboard-dan-loading-opsi
title: "Kontrol Filter Panel: Kolom Hidden, Sumber Kosong, Keyboard, dan Loading Opsi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-71
  - TC-AC-ACAL-72
  - TC-AC-ACAL-73
  - TC-AC-ACAL-167
coverage:
  web: automated
---

# Kontrol Filter Panel: Kolom Hidden, Sumber Kosong, Keyboard, dan Loading Opsi

## Prerequisites

- Mode: FE+BE (intercept parsial respons opsi filter di atas backend nyata; tidak seluruh API di-mock).
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Pre-setup (nama literal, pengecualian S-12 Lampiran A-3; seeding idempotent, tidak dihapus spec ini):
  - Tab Session (Pre-setup No 9 dan 12): baris Session untuk `John Doe` (Position `Staff`) dan sedikitnya satu baris dengan Position bukan `Staff` (mis. `Jane Smith` tanpa Position), sehingga filter Position `Staff` menyaring tabel secara bermakna.
  - Tab User Action (Pre-setup No 10): sedikitnya dua entri dengan Action berbeda, sehingga dropdown Action berisi sedikitnya dua opsi.
- Tabel "Tab dan field uji keyboard" (TC-AC-ACAL-73), dipakai langkah 14 sampai 27:

  | Tab | Field |
  |---|---|
  | Session | User |
  | User Action | Action |

- Kemampuan teknis (disediakan tim FE/BE):
  - Intercept respons opsi filter Session: `POST /v2/analytics-reporting/session-logs/options` (path dari `tc-activity-log-backend.md`). Untuk TC-AC-ACAL-72 respons dipaksa memuat `positionOptions` berupa array kosong (bentuk respons kosong menurut BE-008, tanpa opsi `None`). Untuk TC-AC-ACAL-167 respons ditahan (network throttle) lalu dilepas. Tiap intercept dilepas segera setelah pemicunya selesai (S-09); hook `after` melepas intercept sebagai cadangan.
  - Membaca jumlah total `Z` pada pagination sebagai baseline (langkah 2); total entri tidak diasersi sebagai angka absolut.
  - Mengamati indikator loading yang singkat secara tepat waktu selama respons ditahan (auto-wait tanpa intercept tambahan).
- State yang diubah dan dipulihkan: visibilitas kolom Position tab Session (dikembalikan di langkah 13; hook `after` suite menghapus preferensi kolom sebagai cadangan), Filter tab Session dan tab User Action (dibersihkan di langkah 12 dan 27). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-71: Filter tetap tersedia dan tetap aktif untuk kolom yang di-hide

1. Klik icon Filter pada tab Session, buka dropdown Position, centang `Staff`, klik [Apply]
2. Catat jumlah total entri `Z` pada pagination tab Session
3. Verifikasi sedikitnya satu baris tampil di tab Session
4. Verifikasi setiap baris tabel ber-Position `Staff`
5. Klik `⋯` pada header kolom Actions, hilangkan centang kolom Position di overlay Column Visibility
6. Verifikasi kolom Position hilang dari tabel
7. Verifikasi jumlah total entri pada pagination sama dengan `Z` (saringan tetap berlaku)
8. Verifikasi icon Filter menampilkan indikator dot
9. Klik icon Filter
10. Verifikasi field Position tetap ada di Filter Panel
11. Verifikasi field Position berisi `Staff`
12. Klik [Clear Field], klik [Apply]
13. Klik `⋯` pada header kolom Actions, centang kembali kolom Position di overlay Column Visibility

### TC-AC-ACAL-73: Dropdown Filter Panel dapat dioperasikan dengan keyboard, kedua tab

14. Untuk setiap baris tabel "Tab dan field uji keyboard" di Prerequisites, lakukan langkah 15 sampai 27
15. Klik tab pada kolom Tab, klik icon Filter, tekan Tab sampai fokus berada pada field pada kolom Field
16. Verifikasi field pada kolom Field mendapat fokus
17. Tekan Enter
18. Verifikasi daftar opsi field terbuka
19. Tekan panah bawah, tekan Spasi, lalu catat opsi yang tercentang
20. Verifikasi fokus pindah ke opsi berikutnya
21. Verifikasi opsi tersebut tercentang
22. Tekan Esc
23. Verifikasi daftar opsi field tertutup
24. Tekan Tab sampai fokus berada pada [Apply], tekan Enter
25. Verifikasi sedikitnya satu baris tampil di tab yang diuji
26. Verifikasi setiap baris tabel sesuai dengan opsi yang tercentang pada kolom Field (filter diterapkan)
27. Klik icon Filter, klik [Clear Field], klik [Apply]

### TC-AC-ACAL-72: Dropdown filter tanpa sumber data menampilkan `No options available`

28. Pasang intercept pada respons `POST /v2/analytics-reporting/session-logs/options` agar `positionOptions` berupa array kosong, klik tab "Session", lalu muat ulang halaman (F5)
29. Klik icon Filter, buka dropdown Position
30. Verifikasi teks `No options available` tampil di dropdown Position
31. Verifikasi dropdown Position tidak menampilkan pesan error
32. Lepas intercept, tutup dropdown dengan Esc, lalu tutup Filter Panel tanpa [Apply] dengan klik icon Filter

### TC-AC-ACAL-167: Loading state dropdown filter saat opsi masih dimuat

33. Tahan respons `POST /v2/analytics-reporting/session-logs/options` (network throttle), lalu muat ulang halaman (F5)
34. Klik icon Filter, buka dropdown User
35. Verifikasi indikator loading (skeleton atau spinner) tampil di dropdown User
36. Verifikasi dropdown User tidak menampilkan daftar kosong
37. Lepas penahanan respons
38. Verifikasi opsi tampil di dropdown User
39. Tutup dropdown dengan Esc, lalu tutup Filter Panel tanpa [Apply] dengan klik icon Filter

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 71, 73, 72, 167 (TC-AC-ACAL-72 dan 167 memakai intercept dan ditaruh sesudah kasus tanpa intercept; TC-AC-ACAL-167 terakhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah dihitung dengan ekspansi (39 langkah nominal; langkah 15 sampai 27 diulang untuk dua baris tabel Prerequisites sehingga sekitar 52 langkah). Alasan: seluruh blok satu kelas harness (fungsional Filter Panel, intercept hanya menahan atau mengosongkan opsi untuk mengamati state UI dan bukan kegagalan yang dipaksakan) dengan satu dataset, dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 14 sampai 27 memakai idiom "Untuk setiap baris tabel": parameter tiap iterasi (Tab, Field) ada di tabel Prerequisites, tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa. Pada iterasi tab Session, kolom User tampil sebagai nama ringkas `[first name lengkap] [huruf pertama last name]` dari opsi tercentang; pada iterasi tab User Action, kolom Action sama dengan label opsi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 2 (baseline `Z`, S-12), langkah 12, 13, dan 27 (pemulihan filter dan kolom, S-09), langkah 32 dan 39 (menutup dropdown dan Filter Panel), serta pelepasan intercept pada langkah 32 dan 37 segera setelah pemicu.
- Asersi "setiap baris" (langkah 4 dan 26) didahului `Verifikasi` sedikitnya satu baris tampil (langkah 3 dan 25) sebagai pembanding universal (bagian 8b butir 2). Langkah 31 (bukan error) dan 36 (bukan daftar kosong) memakai Verifikasi positif pada dropdown yang sama sebagai anchor (langkah 30 dan 35); langkah 36 ditulis sebelum respons dilepas (langkah 37).
- Langkah 8 dan 11 membuktikan "saringan tetap berlaku" dan "berisi `Staff`": saringan teramati lewat jumlah total yang tidak berubah (langkah 7) dan indikator dot (langkah 8), karena kolom Position sudah tidak tampil.
- Temuan untuk QA:
  - TC-AC-ACAL-72 menyebut "respons opsi filter Position dikembalikan kosong (di-intercept)" tanpa menyebut endpoint; spec memakai endpoint options Session dari `tc-activity-log-backend.md` (BE-007 dan BE-008). Bentuk respons kosong mengikuti BE-008 (array kosong tanpa opsi `None`).
  - TC-AC-ACAL-72 tidak menyebut apakah opsi diambil saat halaman dibuka atau saat dropdown dibuka; spec memasang intercept sebelum memuat ulang halaman (langkah 28).
  - TC-AC-ACAL-73 tidak menyebut berapa kali tekan Tab untuk mencapai field dan tombol; ditulis "sampai". TC juga tidak menyebut opsi mana yang tercentang oleh panah bawah lalu Spasi; spec mencatatnya pada langkah 19 dan mengasersi baris sesuai opsi itu.
  - TC-AC-ACAL-167 menyebut "network throttle"; spec menahan respons options Session dan melepasnya. TC tidak menyebut endpoint.
  - TC-AC-ACAL-71 tidak menyebut kontrol untuk menyembunyikan kolom; spec memakai overlay Column Visibility pada header `⋯` (TC-AC-ACAL-01).
  - Apakah [Apply] menutup Filter Panel belum ditetapkan PRD dan TC; langkah "klik icon Filter" sesudah [Apply] (langkah 9 dan 15) mengikuti pola TC.
  - Post Condition keempat TC bernilai `-`; tidak diasersi.
