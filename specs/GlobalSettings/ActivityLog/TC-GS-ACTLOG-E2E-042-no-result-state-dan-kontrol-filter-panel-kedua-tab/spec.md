---
id: TC-GS-ACTLOG-E2E-042-no-result-state-dan-kontrol-filter-panel-kedua-tab
title: "No-result State dan Kontrol Filter Panel Kedua Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-06
  - TC-GS-ACTLOG-07
  - TC-GS-ACTLOG-108
  - TC-GS-ACTLOG-109
  - TC-GS-ACTLOG-110
coverage:
  web: automated
---

# No-result State dan Kontrol Filter Panel Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Kondisi environment (hanya dibaca): Tab Session dan Tab User Action memuat data log, dan tidak ada entri Session maupun User Action bertanggal `1 Jan 2020` (TC-GS-ACTLOG-07). Keyword Search `zzznotfound` (TC-GS-ACTLOG-06) ditulis literal karena harus tidak cocok dengan data mana pun.
- Password user dinamis uji: `Spectra.env.ACTLOG_PASSWORD` (env baru) untuk aktivasi dan Login user dinamis di bawah.
- Fixture nilai Filter Panel TC-GS-ACTLOG-110 (fixture baru, nilainya berasal dari data seed spec ini):
  - `Fixture.activityLog.filterSession`: satu nilai untuk tiap field Date, User, Position, Division, Activity, dan Status Tab Session.
  - `Fixture.activityLog.filterUserAction`: satu nilai untuk tiap field Date, Action, Object, Field, dan Modified By Tab User Action.
- Data Dinamis (bersuffix `{runId}-042`):
  - User `John Doe {runId}-042` dan `Budi Anwar {runId}-042` (email `johndoe+{runId}-042@qwertysystem.net` dan `budianwar+{runId}-042@qwertysystem.net`, nilai field wajib lain dari `Fixture.activityLog.userDasar`, fixture baru berisi Position, Employee ID, dan field wajib lain di luar Name, email, dan Division) di-seed lewat API di hook `before`, masing-masing menjalankan Login lewat alur Auth sehingga memiliki baris Session. Search `Budi Anwar {runId}-042` tidak cocok dengan baris milik `John Doe {runId}-042`.
  - Satu baris Session Status `Failed` untuk `John Doe {runId}-042`, dibuat di hook `before` lewat satu percobaan Login gagal (`Spectra.env.LP_PASSWORD_WRONG`) sebelum langkah 23 sehingga opsi Status `Failed` ada di Filter Panel Session.
  - Entri User Action Name `Acme {runId}-042` ber-Action `Edit` saja (tanpa Create), dan Name `Beta {runId}-042` ber-Action `Create` (TC-GS-ACTLOG-108); keduanya ber-Object `Brand`.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action `Acme {runId}-042` (Action `Edit` tanpa `Create` tidak dapat dihasilkan lewat aksi nyata, karena pembuatan Brand selalu mencatat `Create`) dan `Beta {runId}-042`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- State global yang diubah: tidak ada di backend. State Search dan Filter tiap tab dibersihkan lewat langkah pemulihan dengan klik ulang menu sidebar Activity Log. Hook `after` menghapus user milik spec ini. Entri log tidak dapat dihapus (ACTLOG-LOGIC-01); seed memakai nama bersufiks run sehingga run berikutnya tidak bentrok, dan asersi tahan terhadap baris dari run lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-06: No-result state akibat Search

1. Buka Global Settings > Activity Log > Tab "Session", ketik Search `zzznotfound`, tekan Enter
2. Verifikasi ilustrasi no-result tampil di Tab Session dengan Title `"No results found"`
3. Verifikasi ilustrasi no-result Tab Session memuat Description `"Try adjusting your search or filter."`
4. Klik tab "User Action", ketik Search `zzznotfound`, tekan Enter
5. Verifikasi ilustrasi no-result tampil di Tab User Action dengan Title `"No results found"`
6. Verifikasi ilustrasi no-result Tab User Action memuat Description `"Try adjusting your search or filter."`

### Pemulihan state antar TC

7. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-07: No-result state akibat Filter

8. Pada Tab Session klik icon Filter, pilih Date `1 Jan 2020`, klik [Apply]
9. Verifikasi ilustrasi no-result tampil di Tab Session dengan Title `"No results found"`
10. Verifikasi ilustrasi no-result Tab Session memuat Description `"Try adjusting your search or filter."`
11. Klik tab "User Action", klik icon Filter, pilih Date `1 Jan 2020`, klik [Apply]
12. Verifikasi ilustrasi no-result tampil di Tab User Action dengan Title `"No results found"`
13. Verifikasi ilustrasi no-result Tab User Action memuat Description `"Try adjusting your search or filter."`

### Pemulihan state antar TC

14. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-108: Pemulihan dari no-result setelah salah satu saringan dilepas

15. Pada Tab Session ketik Search `Budi Anwar {runId}-042`, tekan Enter; klik icon Filter, pilih User `John Doe {runId}-042`, klik [Apply] sehingga tampil `"No results found"`
16. Kosongkan isi kotak search Tab Session, tekan Enter
17. Verifikasi tabel Tab Session pulih menampilkan baris milik `John Doe {runId}-042` sesuai Filter yang tersisa
18. Klik tab "User Action", ketik Search `Acme {runId}-042`, tekan Enter; klik icon Filter, pilih Action `Create`, klik [Apply] sehingga tampil `"No results found"`
19. Kosongkan isi kotak search Tab User Action, tekan Enter
20. Verifikasi tabel Tab User Action pulih menampilkan baris Action `Create` (termasuk Name `Beta {runId}-042`) sesuai Filter yang tersisa

### Pemulihan state antar TC

21. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-109: Menutup Filter Panel tanpa [Apply] membuang perubahan

22. Pada Tab Session klik icon Filter, pilih Activity `Login`, klik [Apply]
23. Klik icon Filter, tambah Status `Failed` tanpa klik [Apply], klik area di luar panel, buka kembali panel
24. Verifikasi panel Tab Session menampilkan Activity `Login` saja
25. Verifikasi Status `Failed` tidak terpilih di panel Tab Session
26. Verifikasi tabel Tab Session tetap menampilkan hasil Filter Activity `Login`
27. Klik icon Filter untuk menutup panel
28. Klik icon Filter, tambah Status `Failed` tanpa klik [Apply], klik icon Filter lagi untuk menutup, buka kembali panel
29. Verifikasi panel Tab Session menampilkan Activity `Login` saja
30. Verifikasi Status `Failed` tidak terpilih di panel Tab Session
31. Verifikasi tabel Tab Session tetap menampilkan hasil Filter Activity `Login`
32. Klik tab "User Action", klik icon Filter, pilih Action `Edit`, klik [Apply]
33. Klik icon Filter, tambah Object `Brand` tanpa klik [Apply], klik area di luar panel, buka kembali panel
34. Verifikasi panel Tab User Action menampilkan Action `Edit` saja
35. Verifikasi Object `Brand` tidak terpilih di panel Tab User Action
36. Verifikasi tabel Tab User Action tetap menampilkan hasil Filter Action `Edit`

### Pemulihan state antar TC

37. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-110: Tombol [Clear Field] mengosongkan seluruh field Filter Panel

38. Pada Tab Session klik icon Filter, isi Date, User, Position, Division, Activity, dan Status dengan nilai dari `Fixture.activityLog.filterSession`, klik [Clear Field]
39. Verifikasi field Date kosong dengan placeholder `"Select date"`
40. Verifikasi field User kosong dengan placeholder `"All users"`
41. Verifikasi field Position kosong dengan placeholder `"All positions"`
42. Verifikasi field Division kosong dengan placeholder `"All divisions"`
43. Verifikasi field Activity kosong dengan placeholder `"All activities"`
44. Verifikasi field Status kosong dengan placeholder `"All statuses"`
45. Klik tab "User Action", klik icon Filter, isi Date, Action, Object, Field, dan Modified By dengan nilai dari `Fixture.activityLog.filterUserAction`, klik [Clear Field]
46. Verifikasi field Date kosong dengan placeholder `"Select date"`
47. Verifikasi field Action kosong dengan placeholder `"All actions"`
48. Verifikasi field Object kosong dengan placeholder `"All objects"`
49. Verifikasi field Field kosong dengan placeholder `"All fields"`
50. Verifikasi field Modified By kosong dengan placeholder `"All users"`

### Pemulihan state akhir

51. Tutup Filter Panel tanpa [Apply], lalu klik menu Activity Log di sidebar

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Urutan TC-GS-ACTLOG-06, 7, 108, 109, 110 dipertahankan.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 15, 16, 18, dan 19 (menyiapkan kombinasi yang menghasilkan no-result sesuai Precondition TC lalu melepas Search), langkah 23, 28, dan 33 (aksi tanpa [Apply] dari TC), langkah 27 (menutup panel yang masih terbuka dari langkah 23 sebelum TC langkah 3 dimulai dengan klik icon Filter), dan langkah pemulihan 7, 14, 21, 37, dan 51.
- Spec di atas smell 35 langkah (51 langkah nominal, tanpa perulangan). Alasan: semua blok berada pada satu kelas (state tabel dan Filter Panel kedua tab dengan data yang sama), tiap blok dimulai dari state default hasil klik ulang menu sidebar dan berdiri sendiri; sebagian besar langkah adalah `Verifikasi` yang dipecah per klausa (S-01).
- Temuan untuk QA:
  - Env baru `ACTLOG_PASSWORD` perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-108 memakai kata Search `Budi` dan `Acme` serta Filter `John Doe`; spec memakai nama bersuffix agar kombinasi no-result deterministik.
  - TC-110 tidak menyebut nilai yang diisi pada tiap field Filter Panel; spec memakai fixture baru `filterSession` dan `filterUserAction`.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah 23, 27, 28, dan 33 mengikuti pola TC dan bergantung pada perilaku itu.
  - Post Condition semua TC bernilai `-`; tidak diasersi.
