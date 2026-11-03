---
id: TC-GS-USER-E2E-040-edit-referensi-position-division-custom-field-berubah-sesi-lain
title: "Edit: Position, Division, dan Custom Field Dropdown atau Multi-Dropdown Dihapus atau Di-rename Sesi Lain sebelum Save"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-213
  - TC-GS-USER-214
  - TC-GS-USER-215
  - TC-GS-USER-216
  - TC-GS-USER-217
coverage:
  web: automated
---

# Edit: Position, Division, dan Custom Field Dropdown atau Multi-Dropdown Dihapus atau Di-rename Sesi Lain sebelum Save

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca): Position `Staff` (No. 22), Division `Finance` (No. 23), Custom Field Blood Type (opsi `A`) dan Skills (opsi `Excel`) (No. 24), Custom Field Emergency Phone (No. 24).
- Data Dinamis (di-seed lewat API di hook `before`, dibersihkan di `after`):
  - User `Dewi Lestari {runId}-040` (email `dewilestari+{runId}-040@qwertysystem.net`, Activated, Basic, Access `Fixed Asset` dan `Global Settings`, Position `Staff`, Division `Finance` (Pre-setup No. 23, hanya dipilih, tidak diubah; Division wajib sehingga seed tidak dapat berdivisi kosong, TC-GS-USER-16 c), Blood Type `A`, Skills kosong, Emergency Phone kosong), pengganti Dewi Lestari Pre-setup (No. 12) agar data Pre-setup tidak diubah (S-06).
  - Position `Internal Auditor {runId}-040`.
  - Division `Legal {runId}-040` dan `Logistics {runId}-040`.
  - Opsi Custom Field Blood Type `AB {runId}-040` dan opsi Custom Field Skills `SQL {runId}-040` (opsi `Excel` Pre-setup hanya dipilih, tidak diubah).
  - Seeding tidak melewati Master Data Count Limit environment.
- Kemampuan teknis: pemicu "tab lain" memakai sesi API admin (P-2): menghapus Position, menghapus Division, menghapus opsi Custom Field, dan me-rename Division; nama endpoint ditentukan tim FE di tahap script. Popup Edit di UI tetap terbuka selama pemicu berjalan. Tidak ada sesi UI kedua.
- State global: tidak ada.
- Cleanup (`after`, tidak mengandalkan seeding berhasil penuh): hapus user `Dewi Lestari {runId}-040`, Position, Division (termasuk hasil rename), dan opsi Custom Field yang di-seed.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `Dewi Lestari {runId}-040`, tekan Enter

### TC-GS-USER-213: Position dihapus sesi lain sebelum Save ditolak di field

2. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
3. Pilih Position `Internal Auditor {runId}-040`
4. Hapus Position `Internal Auditor {runId}-040` lewat sesi API admin hingga penghapusan tersimpan
5. Klik `[Save]`
6. Verifikasi inline error `This position no longer exists. Please select another.` pada field Position
7. Verifikasi field Position kosong
8. Buka dropdown Position
9. Verifikasi dropdown Position memuat opsi `Staff` (pembanding)
10. Verifikasi dropdown Position tidak memuat opsi `Internal Auditor {runId}-040`
11. Tutup dropdown Position dengan menekan Esc
12. Verifikasi field lain tetap: Name `Dewi Lestari {runId}-040` dan Blood Type `A`
13. Klik `✕` pada header Popup Edit
14. Verifikasi dialog `Unsaved Changes`
15. Klik `[Leave]`
16. Verifikasi sel Position baris `Dewi Lestari {runId}-040` tetap `Staff` (data tidak tersimpan)

### TC-GS-USER-214: Division dihapus sesi lain sebelum Save ditolak di field

17. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
18. Pilih Division `Legal {runId}-040`
19. Hapus Division `Legal {runId}-040` lewat sesi API admin hingga penghapusan tersimpan
20. Klik `[Save]`
21. Verifikasi inline error `This division no longer exists. Please select another.` pada field Division
22. Verifikasi field Division kosong
23. Buka dropdown Division
24. Verifikasi dropdown Division memuat opsi `Logistics {runId}-040` (pembanding)
25. Verifikasi dropdown Division tidak memuat opsi `Legal {runId}-040`
26. Tutup dropdown Division dengan menekan Esc
27. Verifikasi field lain tetap: Name `Dewi Lestari {runId}-040` dan Position `Staff`
28. Klik `✕` pada header Popup Edit
29. Verifikasi dialog `Unsaved Changes`
30. Klik `[Leave]`
31. Verifikasi sel Division baris `Dewi Lestari {runId}-040` tetap `Finance` (data tidak tersimpan)

### TC-GS-USER-215: Custom Field dropdown stale ditolak

32. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
33. Pilih Blood Type `AB {runId}-040`
34. Hapus opsi `AB {runId}-040` pada Custom Field Blood Type lewat sesi API admin hingga penghapusan tersimpan
35. Klik `[Save]`
36. Verifikasi inline error `This blood type no longer exists. Please select another.` pada field Blood Type
37. Klik `✕` pada header Popup Edit
38. Verifikasi dialog `Unsaved Changes`
39. Klik `[Leave]`

### TC-GS-USER-216: Custom Field multi-dropdown stale hanya chip stale yang dihapus

40. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
41. Pilih Skills `Excel` dan `SQL {runId}-040`
42. Hapus opsi `SQL {runId}-040` pada Custom Field Skills lewat sesi API admin hingga penghapusan tersimpan
43. Klik `[Save]`
44. Verifikasi inline error `SQL {runId}-040 no longer exists. Please select another.` pada field Skills
45. Verifikasi chip `Excel` tetap pada field Skills
46. Klik `✕` pada header Popup Edit
47. Verifikasi dialog `Unsaved Changes`
48. Klik `[Leave]`

### TC-GS-USER-217: Division di-rename sesi lain sebelum Save tetap sukses

49. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
50. Pilih Division `Logistics {runId}-040`
51. Ubah nama Division `Logistics {runId}-040` menjadi `Logistics & Warehouse {runId}-040` lewat sesi API admin hingga perubahan nama tersimpan
52. Klik `[Save]`
53. Verifikasi toast sukses: "Success, user has been updated."
54. Verifikasi sel Division baris `Dewi Lestari {runId}-040` bernilai `Logistics & Warehouse {runId}-040`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (54 langkah) karena lima TC berada di satu kelas harness (fungsional, satu layar Edit, satu user seed); tiap blok TC berdiri sendiri (membuka Popup Edit sendiri dan ditutup dengan `[Leave]`) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-GS-USER-217 berada paling akhir karena satu-satunya yang menyimpan perubahan.
- P-2 (pemicu bukan objek uji): pemicu "di tab lain" memakai sesi API admin, bukan sesi UI kedua; yang diasersi hanya Popup Edit di sesi UI aktor.
- Data Pre-setup diganti data milik spec (S-06): Position `Internal Auditor`, Division `Legal` dan `Logistics`, opsi Blood Type `AB`, dan opsi Skills `SQL` di TC sumber adalah data bersama, sehingga spec memakai padanan bersuffix. Nama opsi bersuffix muncul pada teks error TC-GS-USER-216.
- Langkah buka layar User List tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`). Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (Search user seed), 8 dan 23 (membuka dropdown untuk membuktikan opsi dimuat ulang), 11 dan 26 (menutup dropdown), 13, 28, 37, dan 46 (menutup Popup Edit dirty lewat `✕`, dialog `Unsaved Changes`, `[Leave]`, S-08).
- Asersi tambahan di luar Expected TC (dicatat sesuai S-03): langkah 16 dan 31 membuktikan Expected "Data tidak tersimpan" TC-GS-USER-213 dan TC-GS-USER-214 lewat sel Position dan Division yang tidak berubah; langkah 9 dan 24 adalah pembanding (anchor) untuk absence opsi (8b butir 2).
- Temuan untuk QA:
  - TC-GS-USER-213 dan TC-GS-USER-214 Expected c "Field lain tetap" tidak merinci field; spec memeriksa Name dan field yang bernilai (Blood Type pada 213, Position pada 214).
  - TC-GS-USER-213 dan TC-GS-USER-214 Expected b "opsi dimuat ulang" tidak merinci cara observasi; spec membuktikannya lewat isi dropdown.
  - TC-GS-USER-215 hanya punya Expected inline error (tanpa "field dikosongkan" dan "data tidak tersimpan" seperti TC-GS-USER-213 dan TC-GS-USER-214); spec mengasersi hanya inline error.
  - TC-GS-USER-216 menulis pesan `"SQL no longer exists. Please select another."` dengan nama opsi `SQL`; spec memakai nama opsi bersuffix pada pesan, dengan asumsi pesan memuat nama opsi apa adanya.
  - Tabel Data Uji Pre-setup No. 24 menandai Emergency Phone `Required` sedangkan Dewi Lestari (No. 12) kosong dan TC-GS-USER-217 mengharapkan Save sukses; spec mengikuti TC (Emergency Phone tidak diisi).
  - TC-GS-USER-213 sampai 217 menyebut "tab lain" tanpa mekanisme; spec memakai sesi API admin (P-2), dan nama endpoint ditentukan tim FE.
