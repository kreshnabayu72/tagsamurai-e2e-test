---
id: TC-GS-GSET-E2E-040-changelog-kolom-date-self-reference-hover-modified-by-dan-old-new-time-zone
title: "Changelog General Settings: Kolom Date Mengikuti Format dan Time Zone, Hover Modified By, dan Old/New Value Time Zone Utuh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-103
  - TC-GS-GSET-161
  - TC-GS-GSET-162
  - TC-GS-GSET-163
coverage:
  web: automated
---

# Changelog General Settings: Kolom Date Mengikuti Format dan Time Zone, Hover Modified By, dan Old/New Value Time Zone Utuh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`); akun aktor `Budi S` untuk hover Modified By.
- Seeding di hook `before` (precondition TC "Changelog berisi baris riwayat"; baris Field `Session Idle Timeout` dipakai sebagai objek asersi TC-163): dua PUT `/v2/enterprise-management/general-settings` (full-replace, `global-settings/general-settings/API/openapi.yaml`) oleh sesi API Budi Santoso yang mengubah `sessionIdleTimeout` dari 30 ke 60 lalu kembali ke 30, sehingga ada baris Field `Session Idle Timeout` oleh `Budi S`. Total entri Changelog tidak diasersi sebagai angka (audit trail permanen).
- Data uji: Date Format `M/d/yy` dan Time Format `hh:mm a` (TC-103); Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (`Asia/Jakarta`, default) dan `(UTC+00:00) UTC, Reykjavik, Accra` (`UTC`, label PRD §4.3a; Time Zone tujuan pada TC-163); selisih offset kedua label 7 jam; nilai `Budi S` dengan nama lengkap `Budi Santoso` (TC-161).
- Kemampuan teknis: membaca timestamp penyimpanan (`createdAt`, ISO UTC) baris Field `Session Idle Timeout` terbaru dari daftar Changelog (`global-settings/activity-log/API/openapi.yaml`, `POST /v2/analytics-reporting/change-logs/list`; disediakan tim FE/BE, TC tidak menyebut caranya) untuk menghitung tanggal dan jam yang diharapkan di UI; mengarahkan kursor ke sel tabel untuk membaca tooltip. Tanggal dan jam yang diharapkan pada langkah 15 dan 25 dihitung dari timestamp itu pada zona yang berlaku (`Asia/Jakarta` lalu `UTC`) dengan pola `M/d/yy hh:mm a`, tanpa percabangan.
- State global yang diubah dan dipulihkan: Date Format, Time Format, dan Time Zone record Client A (juga dibaca suite lain). Pemulihan: Time Zone dikembalikan ke `Asia/Jakarta` pada langkah 29 dan 30; Date Format `dd/MM/yy` dan Time Format `HH:mm` pada langkah 41 sampai 43; hook `after` (tetap jalan walau spec gagal di tengah) memulihkan record ke baseline lewat PUT dan hook suite `beforeEach` memulihkannya sebelum spec berikutnya.
- Suite berjalan serial (`parallel: false`): record Client A dan format tanggalnya dibagi seluruh spec.

## Test Steps

### TC-GS-GSET-103: Kolom Date Changelog mengikuti Date Format dan Time Format General Settings

1. Pilih Date Format `M/d/yy`
2. Pilih Time Format `hh:mm a`
3. Klik `[Save]`
4. Tunggu aksi selesai
5. Klik icon Changelog di pojok kanan atas halaman
6. Verifikasi tabel menampilkan sedikitnya satu baris
7. Verifikasi kolom Date pada setiap baris memakai tanggal berformat `M/d/yy` (bulan dan hari tanpa angka nol di depan)
8. Verifikasi kolom Date pada setiap baris memakai waktu berformat `hh:mm a` (12 jam dengan AM/PM)

### TC-GS-GSET-161: Hover nilai kolom Modified By menampilkan nama lengkap

9. Arahkan kursor ke nilai `Budi S` pada kolom Modified By
10. Verifikasi tooltip menampilkan nama lengkap `Budi Santoso`

### TC-GS-GSET-163: Mengubah Time Zone menggeser jam kolom Date Changelog sesuai selisih offset

11. Klik Filter di toolbar
12. Pilih Field `Session Idle Timeout`
13. Klik `[Apply]`
14. Catat tanggal dan jam kolom Date pada baris paling atas hasil Filter sebagai `{Date sebelum}`
15. Verifikasi `{Date sebelum}` sama dengan timestamp baris itu pada zona `Asia/Jakarta` (UTC+07:00) dengan pola `M/d/yy hh:mm a`
16. Tutup Modal Changelog dengan menekan `Esc`
17. Pilih Time Zone `(UTC+00:00) UTC, Reykjavik, Accra`
18. Klik `[Save]`
19. Tunggu aksi selesai
20. Klik icon Changelog di pojok kanan atas halaman
21. Klik Filter di toolbar
22. Pilih Field `Session Idle Timeout`
23. Klik `[Apply]`
24. Catat tanggal dan jam kolom Date pada baris paling atas hasil Filter (baris yang sama) sebagai `{Date sesudah}`
25. Verifikasi `{Date sesudah}` sama dengan timestamp baris yang sama pada zona `UTC` (UTC+00:00) dengan pola `M/d/yy hh:mm a`
26. Verifikasi `{Date sesudah}` sama dengan `{Date sebelum}` dikurangi 7 jam (tanggal dan jam, selisih offset `(UTC+07:00)` ke `(UTC+00:00)`)
27. Verifikasi Date Format `M/d/yy` dan Time Format `hh:mm a` pada kolom Date tidak berubah
28. Tutup Modal Changelog dengan menekan `Esc`
29. Pilih Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`
30. Klik `[Save]`
31. Tunggu aksi selesai

### TC-GS-GSET-162: Old Value dan New Value baris Time Zone tampil utuh tanpa pemotongan

32. Klik icon Changelog di pojok kanan atas halaman
33. Ketik Search `Time Zone`, tekan Enter
34. Verifikasi tabel menampilkan sedikitnya satu baris Field `Time Zone`
35. Verifikasi Old Value baris paling atas tampil utuh `(UTC+00:00) UTC, Reykjavik, Accra` tanpa karakter pemotong `..`
36. Verifikasi New Value baris paling atas tampil utuh `(UTC+07:00) Bangkok, Hanoi, Jakarta` tanpa karakter pemotong `..`
37. Verifikasi kolom Old Value dan New Value melebar mengikuti konten
38. Arahkan kursor ke nilai pada kolom Old Value baris paling atas
39. Verifikasi tidak ada tooltip pada kolom Old Value
40. Tutup Modal Changelog dengan menekan `Esc`
41. Pilih Date Format `dd/MM/yy`
42. Pilih Time Format `HH:mm`
43. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (Save lewat UI, Changelog dari backend nyata).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC dalam spec: 103, 161, 163, lalu 162 di akhir karena TC-162 membutuhkan baris Field `Time Zone` yang dibuat TC-163 (Data Uji Dinamis: dibuat di TC Save Time Zone) dan Time Zone dipulihkan ke `Asia/Jakarta` (langkah 29 sampai 31) sebelum asersi TC-162; baris Field `Time Zone` terbaru (Old Value `UTC` ke New Value `Asia/Jakarta`) dihasilkan langkah 30. Urutan di `tc-general-settings.md`: 103, 161, 162, 163.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 19, 31 (Tunggu aksi selesai: field kembali pada kondisi tersimpan dan `[Save]` kembali disabled; langkah berikutnya membuka Modal Changelog yang membaca data baru); langkah 5, 20, dan 32 (membuka Modal Changelog; modal tertutup oleh langkah 16, 28, dan 40); langkah 11 sampai 13 dan 21 sampai 23 (Filter Field `Session Idle Timeout` agar "baris Field `Session Idle Timeout`" TC-163 langkah 1 terlokalisasi; membuka ulang modal mereset Filter); langkah 14 dan 24 (mencatat nilai); langkah 29 sampai 31 dan 41 sampai 43 (memulihkan Time Zone, Date Format, dan Time Format). Langkah 33 (Search `Time Zone`) menemukan baris Field `Time Zone` (langkah 1 TC-162 "cari baris Field `Time Zone`").
- Asersi tambahan (konkretisasi, S-03): langkah 6 adalah pembanding generik "sedikitnya satu baris" sebelum asersi universal "setiap baris" pada langkah 7 dan 8 (bagian 8b butir 2). Langkah 15 mengasersi nilai baseline (jam sebelum Save) terhadap timestamp API supaya selisih 7 jam pada langkah 26 bermakna; langkah 25 mengasersi nilai sesudah Save terhadap timestamp yang sama. Langkah 34 adalah pembanding sebelum asersi isi baris `Time Zone`. Langkah 39 (absence tooltip) segera sesudah pemicu hover (langkah 38) dan didahului tooltip Modified By yang tampil pada kolom lain di spec yang sama (langkah 10) sebagai bukti hover memunculkan tooltip pada surface ini (bagian 8b butir 11).
- Langkah 7 dan 8 memecah Expected TC-103 per klausa (tanggal dan waktu, S-01); langkah 35, 36, dan 37 memecah Expected a TC-162 (Old Value utuh, New Value utuh, kolom melebar); langkah 25 dan 26 memetakan Expected a TC-163 (tanggal dan jam = nilai langkah 1 dikurangi 7 jam; langkah 25 menurunkan nilai dari timestamp pada zona `UTC`, langkah 26 membandingkannya dengan `{Date sebelum}`), langkah 27 memetakan Expected b (format tidak berubah), tanpa percabangan.
- Spec melewati sekitar 35 langkah (43 langkah) karena empat TC berbagi tabel Changelog yang sama pada satu kelas harness (fungsional), tiga Save lewat UI (langkah 3, 18, 30) dan tiga pemulihan state global (langkah 29 sampai 31, 41 sampai 43) wajib ada, serta Expected dipecah satu `Verifikasi` per klausa (S-01). Blok 163 mengubah Time Zone dan dipulihkan di dalam blok yang sama sebelum blok 162; kegagalan keras satu blok tidak membuat blok lain kehilangan makna kecuali ketergantungan baris `Time Zone` untuk TC-162 yang dicatat di atas.
- Pembagian TC lintas spec: TC-GS-GSET-36 dan 33, 34, 35 (Save per field) di spec 014 dan 015; TC-GS-GSET-60, 65, 85, 86, 96 (screening Changelog, urutan default, tooltip) di spec 027; TC-GS-GSET-77 (rentang Date pada Filter) di spec 030; TC-GS-GSET-98 (Date pada berkas export) di spec 036.
- Temuan untuk QA:
  - TC-GS-GSET-163: Post Condition ("Setelah Save baru muncul baris Field `Time Zone` di Changelog") tidak punya langkah observasi di TC; tidak diasersi di blok TC-163. Baris Field `Time Zone` teramati di blok TC-162 (langkah 34 sampai 36) sebagai prasyarat TC-162.
  - TC-GS-GSET-163: TC tidak menyebut cara memilih baris Field `Session Idle Timeout` bila ada beberapa baris; spec memakai baris paling atas (Date terbaru) hasil Filter Field `Session Idle Timeout` dan membaca timestamp barisnya dari API.
  - TC-GS-GSET-103: tanggal uji dapat memiliki bulan dan hari dua digit (mis. 30 Oktober), sehingga "tanpa angka nol di depan" tidak terbukti pada tanggal tersebut; asersi mengikuti pola `M/d/yy` apa adanya. Label opsi Date Format dan Time Format pada dropdown (apakah memuat contoh tanggal) tidak disebut TC-103; spec memilih berdasarkan pola `M/d/yy` dan `hh:mm a`.
  - TC-GS-GSET-162: langkah 1 meminta "cari baris Field `Time Zone` (dibuat di TC Save Time Zone)" tanpa menyebut bahwa baris itu bergantung pada TC lain; spec membuat baris itu lewat langkah 17 sampai 18 dan 29 sampai 30 di spec yang sama (S-04).
  - TC-GS-GSET-161: TC tidak menyebut aksi hover pada nilai tertentu bila ada beberapa baris; spec mengarahkan kursor ke nilai `Budi S` pertama pada kolom Modified By.
