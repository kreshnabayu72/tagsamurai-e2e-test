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
- Data Pre-setup (hanya dibaca): Position `Staff` (No. 22), Custom Field Blood Type (opsi `A`) dan Skills (opsi `Excel`) (No. 24), Custom Field Emergency Phone (No. 24).
- Data Dinamis (di-seed lewat API di hook `before`, dibersihkan di `after`):
  - User `Dewi Lestari {runId}-040` (email `dewilestari+{runId}-040@qwertysystem.net`, Activated, Basic, Access `Fixed Asset` dan `Global Settings`, Position `Staff`, Division kosong, Blood Type `A`, Skills kosong, Emergency Phone kosong), pengganti Dewi Lestari Pre-setup (No. 12) agar data Pre-setup tidak diubah (S-06).
  - Position `Internal Auditor {runId}-040`.
  - Division `Legal {runId}-040` dan `Logistics {runId}-040`.
  - Opsi Custom Field Blood Type `AB {runId}-040` dan opsi Custom Field Skills `SQL {runId}-040` (opsi `Excel` Pre-setup hanya dipilih, tidak diubah).
  - Seeding tidak melewati Master Data Count Limit environment.
- Kemampuan teknis: pemicu "tab lain" memakai sesi API admin (P-2): menghapus Position, menghapus Division, menghapus opsi Custom Field, dan me-rename Division; nama endpoint ditentukan tim FE di tahap script. Popup Edit di UI tetap terbuka selama pemicu berjalan. Tidak ada sesi UI kedua.
- State global: tidak ada.
- Cleanup (`after`, tidak mengandalkan seeding berhasil penuh): hapus user `Dewi Lestari {runId}-040`, Position, Division (termasuk hasil rename), dan opsi Custom Field yang di-seed.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Dewi Lestari {runId}-040`, tekan Enter

### TC-GS-USER-213: Position dihapus sesi lain sebelum Save ditolak di field

3. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
4. Pilih Position `Internal Auditor {runId}-040`
5. Hapus Position `Internal Auditor {runId}-040` lewat sesi API admin
6. Klik `[Save]`
7. Verifikasi inline error `This position no longer exists. Please select another.` pada field Position
8. Verifikasi field Position kosong
9. Buka dropdown Position
10. Verifikasi dropdown Position memuat opsi `Staff` (pembanding)
11. Verifikasi dropdown Position tidak memuat opsi `Internal Auditor {runId}-040`
12. Tutup dropdown Position dengan menekan Esc
13. Verifikasi field lain tetap: Name `Dewi Lestari {runId}-040` dan Blood Type `A`
14. Klik `✕` pada header Popup Edit
15. Verifikasi dialog `Unsaved Changes`
16. Klik `[Leave]`
17. Verifikasi sel Position baris `Dewi Lestari {runId}-040` tetap `Staff` (data tidak tersimpan)

### TC-GS-USER-214: Division dihapus sesi lain sebelum Save ditolak di field

18. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
19. Pilih Division `Legal {runId}-040`
20. Hapus Division `Legal {runId}-040` lewat sesi API admin
21. Klik `[Save]`
22. Verifikasi inline error `This division no longer exists. Please select another.` pada field Division
23. Verifikasi field Division kosong
24. Buka dropdown Division
25. Verifikasi dropdown Division memuat opsi `Logistics {runId}-040` (pembanding)
26. Verifikasi dropdown Division tidak memuat opsi `Legal {runId}-040`
27. Tutup dropdown Division dengan menekan Esc
28. Verifikasi field lain tetap: Name `Dewi Lestari {runId}-040` dan Position `Staff`
29. Klik `✕` pada header Popup Edit
30. Verifikasi dialog `Unsaved Changes`
31. Klik `[Leave]`
32. Verifikasi sel Division baris `Dewi Lestari {runId}-040` tetap `—` (data tidak tersimpan)

### TC-GS-USER-215: Custom Field dropdown stale ditolak

33. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
34. Pilih Blood Type `AB {runId}-040`
35. Hapus opsi `AB {runId}-040` pada Custom Field Blood Type lewat sesi API admin
36. Klik `[Save]`
37. Verifikasi inline error `This blood type no longer exists. Please select another.` pada field Blood Type
38. Klik `✕` pada header Popup Edit
39. Verifikasi dialog `Unsaved Changes`
40. Klik `[Leave]`

### TC-GS-USER-216: Custom Field multi-dropdown stale hanya chip stale yang dihapus

41. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
42. Pilih Skills `Excel` dan `SQL {runId}-040`
43. Hapus opsi `SQL {runId}-040` pada Custom Field Skills lewat sesi API admin
44. Klik `[Save]`
45. Verifikasi inline error `SQL {runId}-040 no longer exists. Please select another.` pada field Skills
46. Verifikasi chip `Excel` tetap pada field Skills
47. Klik `✕` pada header Popup Edit
48. Verifikasi dialog `Unsaved Changes`
49. Klik `[Leave]`

### TC-GS-USER-217: Division di-rename sesi lain sebelum Save tetap sukses

50. Klik (⋯) baris `Dewi Lestari {runId}-040` → `Edit`
51. Pilih Division `Logistics {runId}-040`
52. Ubah nama Division `Logistics {runId}-040` menjadi `Logistics & Warehouse {runId}-040` lewat sesi API admin
53. Klik `[Save]`
54. Verifikasi toast sukses: "Success, user has been updated."
55. Verifikasi sel Division baris `Dewi Lestari {runId}-040` bernilai `Logistics & Warehouse {runId}-040`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (55 langkah) karena lima TC berada di satu kelas harness (fungsional, satu layar Edit, satu user seed); tiap blok TC berdiri sendiri (membuka Popup Edit sendiri dan ditutup dengan `[Leave]`) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-GS-USER-217 berada paling akhir karena satu-satunya yang menyimpan perubahan.
- P-2 (pemicu bukan objek uji): pemicu "di tab lain" memakai sesi API admin, bukan sesi UI kedua; yang diasersi hanya Popup Edit di sesi UI aktor.
- Data Pre-setup diganti data milik spec (S-06): Position `Internal Auditor`, Division `Legal` dan `Logistics`, opsi Blood Type `AB`, dan opsi Skills `SQL` di TC sumber adalah data bersama, sehingga spec memakai padanan bersuffix. Nama opsi bersuffix muncul pada teks error TC-GS-USER-216.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2 (Search user seed), 9 dan 24 (membuka dropdown untuk membuktikan opsi dimuat ulang), 12 dan 27 (menutup dropdown), 14, 29, 38, dan 47 (menutup Popup Edit dirty lewat `✕`, dialog `Unsaved Changes`, `[Leave]`, S-08).
- Asersi tambahan di luar Expected TC (dicatat sesuai S-03): langkah 17 dan 32 membuktikan Expected "Data tidak tersimpan" TC-GS-USER-213 dan TC-GS-USER-214 lewat sel Position dan Division yang tidak berubah; langkah 10 dan 25 adalah pembanding (anchor) untuk absence opsi (8b butir 2).
- Temuan untuk QA:
  - TC-GS-USER-213 dan TC-GS-USER-214 Expected c "Field lain tetap" tidak merinci field; spec memeriksa Name dan field yang bernilai (Blood Type pada 213, Position pada 214).
  - TC-GS-USER-213 dan TC-GS-USER-214 Expected b "opsi dimuat ulang" tidak merinci cara observasi; spec membuktikannya lewat isi dropdown.
  - TC-GS-USER-215 hanya punya Expected inline error (tanpa "field dikosongkan" dan "data tidak tersimpan" seperti TC-GS-USER-213 dan TC-GS-USER-214); spec mengasersi hanya inline error.
  - TC-GS-USER-216 menulis pesan `"SQL no longer exists. Please select another."` dengan nama opsi `SQL`; spec memakai nama opsi bersuffix pada pesan, dengan asumsi pesan memuat nama opsi apa adanya.
  - Tabel Data Uji Pre-setup No. 24 menandai Emergency Phone `Required` sedangkan Dewi Lestari (No. 12) kosong dan TC-GS-USER-217 mengharapkan Save sukses; spec mengikuti TC (Emergency Phone tidak diisi).
  - TC-GS-USER-213 sampai 217 menyebut "tab lain" tanpa mekanisme; spec memakai sesi API admin (P-2), dan nama endpoint ditentukan tim FE.
