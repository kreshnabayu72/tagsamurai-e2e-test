---
id: TC-AC-ACAL-E2E-038-bahasa-pengguna-kolom-translatable-dan-label-opsi-filter
title: "Bahasa Pengguna: Kolom Translatable dan Label Opsi Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-170
  - TC-AC-ACAL-180
coverage:
  web: automated
---

# Bahasa Pengguna: Kolom Translatable dan Label Opsi Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Bahasa: Language picker akun penguji berisi English dan Bahasa Indonesia. Hook `before` menyetel bahasa akun penguji ke English dan mencatat nilai awal; hook `after` mengembalikan bahasa awal.
- Fixture terjemahan (`Fixture.activityLog.terjemahan`, disediakan tim FE; TC dan PRD tidak menyebut teks terjemahan): `activitySession` (teks Bahasa Indonesia untuk Activity `Session`), `noteSessionEnded` (teks Bahasa Indonesia untuk Note `Session ended`), dan `kataNote` (satu kata dari `noteSessionEnded`). Teks `noteSessionEnded` dan `activitySession` tidak memuat kata Inggris `ended` (kondisi TC-AC-ACAL-170 Expected c).
- Data Dinamis (bersuffix `{runId}-038`), dibuat di hook `before`:
  - Tab Session: user `Uji Bahasa {runId}-038` dengan dua baris Session, `Session started` lalu `Session ended` (cap waktu `Session ended` lebih baru sehingga menjadi baris teratas pada urutan default Date terbaru di atas). Kemampuan seed BE baris Session disediakan tim FE/BE.
  - Tab User Action: Brand `Brand Bahasa {runId}-038` dibuat lalu di-rename menjadi `Brand Bahasa {runId}-038 Rename` oleh aktor lewat sesi API aktor, sehingga terbentuk baris `Create` dan baris `Edit` (Object `Brand`, Field `Name`, Modified By aktor) dengan Action berbeda.
  - Cleanup di hook `after` tanpa berasumsi seeding berhasil penuh: hapus Brand milik spec lewat API. Baris log tidak dapat dihapus (append-only).
- Kemampuan teknis (disediakan tim FE/BE): menangkap berkas unduhan browser ke direktori bersih dan membaca isi CSV (sel per kolom, lihat Temuan untuk QA tentang kelas binary buffer).
- State global yang diubah dan dipulihkan: bahasa akun penguji (dikembalikan ke English di langkah 33 dan di hook `after`), Search tab Session dan tab User Action (dibersihkan di langkah 27 dan 33). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-180: Label opsi filter Action, Object, dan Field mengikuti bahasa pengguna

1. Klik tab "User Action", ketik Search `{runId}-038`, tekan Enter
2. Catat teks sel Action, Object, dan Field pada baris `Edit` milik Brand `Brand Bahasa {runId}-038 Rename` (bahasa English)
3. Klik icon Filter, buka dropdown Action
4. Verifikasi ada opsi Action berlabel sama dengan teks sel Action yang dicatat
5. Buka dropdown Object
6. Verifikasi ada opsi Object berlabel sama dengan teks sel Object yang dicatat
7. Buka dropdown Field
8. Verifikasi ada opsi Field berlabel sama dengan teks sel Field yang dicatat
9. Tutup dropdown dengan Esc, lalu tutup Filter Panel tanpa [Apply] dengan klik icon Filter
10. Ganti bahasa pengguna lewat Language picker ke Bahasa Indonesia
11. Ganti isi kotak search dengan `{runId}-038`, tekan Enter, lalu catat teks sel Action, Object, dan Field pada baris `Edit` yang sama (bahasa Indonesia)
12. Klik icon Filter, buka dropdown Action
13. Verifikasi ada opsi Action berlabel sama dengan teks sel Action yang dicatat pada langkah 11
14. Buka dropdown Object
15. Verifikasi ada opsi Object berlabel sama dengan teks sel Object yang dicatat pada langkah 11
16. Buka dropdown Field
17. Verifikasi ada opsi Field berlabel sama dengan teks sel Field yang dicatat pada langkah 11
18. Tutup dropdown dengan Esc, lalu tutup Filter Panel tanpa [Apply] dengan klik icon Filter

### TC-AC-ACAL-170: Kolom Translatable mengikuti bahasa pengguna pada tampilan, Search, Sort, dan Download

19. Klik tab "Session", ketik Search `{runId}-038`, tekan Enter
20. Verifikasi kolom Activity baris teratas milik `Uji Bahasa {runId}-038` tampil `Fixture.activityLog.terjemahan.activitySession`
21. Verifikasi kolom Note baris teratas milik `Uji Bahasa {runId}-038` tampil `Fixture.activityLog.terjemahan.noteSessionEnded`
22. Ganti isi kotak search dengan `Fixture.activityLog.terjemahan.kataNote`, tekan Enter
23. Verifikasi sedikitnya satu baris tampil di tab Session
24. Verifikasi kolom Note baris hasil memuat `Fixture.activityLog.terjemahan.kataNote`
25. Ganti isi kotak search dengan `ended`, tekan Enter
26. Verifikasi `"No results found"` tampil di tab Session
27. Klik `(←)` pada kotak Search
28. Klik tab "User Action", klik icon sort pada header kolom Action sekali (ascending)
29. Verifikasi sedikitnya dua baris dengan Action berbeda tampil di tab User Action
30. Verifikasi urutan baris mengikuti teks Action yang tampil (A-Z, bahasa Indonesia)
31. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
32. Verifikasi sel Action, Object, dan Field baris `Edit` milik `Brand Bahasa {runId}-038 Rename` di berkas berisi teks yang sama dengan sel tabel (bahasa Indonesia)
33. Klik icon sort pada header kolom Action hingga netral, klik `(←)` pada kotak Search, lalu kembalikan bahasa ke English lewat Language picker

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 180 lalu 170 (TC-AC-ACAL-180 dimulai dari English dan berakhir pada Bahasa Indonesia, yang menjadi Precondition TC-AC-ACAL-170: bahasa platform diubah dari English ke Bahasa Indonesia). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 19 (Search `{runId}-038` menyempitkan tabel ke baris seed milik spec; pada TC-AC-ACAL-170 juga menyempitkan berkas Download), langkah 9 dan 18 (menutup dropdown dan Filter Panel tanpa [Apply]), langkah 11 (mengulang Search setelah ganti bahasa; mengasumsikan kotak Search tetap terbuka dan berisi kata kunci, dan mencatat teks sel yang sama), langkah 27 dan 33 (pemulihan Search, Sort, dan bahasa; S-09).
- Langkah 22 sampai 24 memakai Search dari kata Note bahasa pengguna; langkah 23 menjadi pembanding positif sebelum langkah 26 (`"No results found"` untuk kata Inggris).
- Langkah 29 adalah pembanding asersi sort (dua nilai Action berbeda, S-11); langkah 30 diasersi sesudah klik ascending pertama (siklus sort: ascending, descending, netral).
- Langkah 32 mengasersi isi sel berkas (kelas binary buffer, prinsip 13f). TC-AC-ACAL-170 mencampur tampilan, Search, Sort, dan isi berkas dalam satu TC sehingga tidak dapat dipecah (satu TC satu spec); klausa isi berkas ditempatkan di spec ini bersama klausa UI.
- Label menu Download: TC-AC-ACAL-170 menulis `Download > CSV|XLSX`, label UI adalah `Download as CSV|XLSX` (PRD §4.2); spec memakai label UI.
- Temuan untuk QA:
  - TC-AC-ACAL-170 tidak menyebut bahasa non-Inggris yang dipilih maupun teks terjemahan Activity, Note, Action, Object, dan Field; spec meminta fixture terjemahan dari tim FE dan memakai Bahasa Indonesia (disebut TC-AC-ACAL-180).
  - TC-AC-ACAL-170 Expected c memakai "bila kata Inggris tidak ada di teks tampil" tanpa menyebut bahwa kata `ended` tidak ada di kolom Searchable lain; spec menjadikannya kondisi di Prerequisites. Bila kolom lain (mis. nama user) memuat `ended`, langkah 26 gagal.
  - TC-AC-ACAL-170 langkah 2 menyebut "kata dari teks Note yang tampil" tanpa menyebut kata tertentu; spec memakai `kataNote` dari fixture.
  - TC-AC-ACAL-180 tidak menyebut keadaan kotak Search setelah ganti bahasa; spec mengasumsikan kotak tetap terbuka dan berisi kata kunci (langkah 11).
  - TC-AC-ACAL-180 tidak menyebut baris mana yang dibandingkan dengan label opsi; spec memakai baris `Edit` Brand milik spec.
  - Post Condition kedua TC bernilai `-`; tidak diasersi.
