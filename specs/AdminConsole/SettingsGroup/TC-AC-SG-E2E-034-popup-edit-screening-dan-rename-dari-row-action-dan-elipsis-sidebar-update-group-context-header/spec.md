---
id: TC-AC-SG-E2E-034-popup-edit-screening-dan-rename-dari-row-action-dan-elipsis-sidebar-update-group-context-header
title: "Popup Edit: Screening dan Rename dari Row Action dan Elipsis Sidebar, Update Group Context Header"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-113
  - TC-AC-SG-114
  - TC-AC-SG-115
  - TC-AC-SG-116
coverage:
  web: automated
---

# Popup Edit: Screening dan Rename dari Row Action dan Elipsis Sidebar, Update Group Context Header

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: screening TC-AC-SG-113 membaca node Pre-setup `Region B` (Pre-setup #16) tanpa menyimpan. Target rename TC-AC-SG-114, 115, dan 116 adalah node milik spec (di-seed Fixture BE di hook `before`, entitas Principal); nama TC diganti nama bersuffix karena target aksi tulis tidak memakai node Pre-setup bersama (S-06):

| TC | Nama di TC | Seed di spec | Nama baru di spec |
|---|---|---|---|
| TC-AC-SG-114 | `Region C` -> `Region C Edit` | `Region C-{runId}-034` (level 1) dengan anak `Anak Region C-{runId}-034` | `Region C Edit-{runId}-034` |
| TC-AC-SG-115 | `Head Office` -> `Head Office Edit` | `Head Office-{runId}-034` (level 1) | `Head Office Edit-{runId}-034` |
| TC-AC-SG-116 | `Warehouse Jakarta` -> `Warehouse Jakarta Edit` | `Warehouse Jakarta-{runId}-034` (level 1) | `Warehouse Jakarta Edit-{runId}-034` |

- Asersi Total User dan Total Member pada TC-AC-SG-114 dan TC-AC-SG-116 membandingkan nilai sebelum dan sesudah aksi pada node seed (dicatat sebelum aksi); angka absolut Pre-setup tidak dipakai.
- Asersi Last Updated memakai satu cara: waktu dicatat sesudah `[Save]`, Last Updated dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron. Modified By diasersi berformat `[First Name] [Last Initial]` (`Budi S`).
- Kemampuan teknis: Fixture BE (seeding dan penghapusan data milik spec) disediakan tim FE/BE (lihat `suite.md`).
- Pemulihan: hook `after` menghapus seluruh group milik spec lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-113: Screening Popup Edit Group

1. Ketik Search `Region B`, tekan Enter
2. Klik ikon `⋯` pada baris `Region B`, lalu pilih "Edit"
3. Verifikasi Header popup: Title "Edit Group" dan ikon close `[✕]`
4. Verifikasi Body: field Group Name terisi nilai saat ini "Region B"
5. Verifikasi tidak ada field parent pada popup
6. Verifikasi Footer: tombol `[Clear Field]` (varian teks) dan `[Save]` (filled, success)
7. Verifikasi tidak ada checkbox "Stay on this form after submitting"
8. Klik `[✕]` pada popup
9. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-114: Edit dari row action tabel

10. Ketik Search `Region C-{runId}-034`, tekan Enter
11. Catat Total User dan Total Member baris `Region C-{runId}-034` sebagai pembanding langkah 22
12. Klik ikon `⋯` pada baris `Region C-{runId}-034`, lalu pilih "Edit"
13. Ubah nama menjadi `Region C Edit-{runId}-034`, klik `[Save]`
14. Catat waktu sesudah `[Save]`
15. Verifikasi toast sukses: "Success, group has been updated."
16. Verifikasi popup tertutup
17. Ganti isi kotak Search tabel utama dengan `Region C Edit-{runId}-034`, tekan Enter
18. Verifikasi nama baru `Region C Edit-{runId}-034` tampil pada tabel
19. Verifikasi nama baru `Region C Edit-{runId}-034` tampil pada Sidebar Group Tree
20. Verifikasi kolom Modified By pada baris terbarui menjadi `Budi S`
21. Verifikasi kolom Last Updated pada baris terbarui sesuai waktu pada langkah 14 (toleransi satu menit)
22. Verifikasi Total User dan Total Member baris sama dengan nilai pada langkah 11
23. Verifikasi `Anak Region C-{runId}-034` tetap menjadi turunan `Region C Edit-{runId}-034` di sidebar
24. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-115: Edit dari elipsis sidebar

25. Klik ikon `⋯` pada node `Head Office-{runId}-034` di sidebar, lalu pilih "Edit"
26. Verifikasi popup Edit Group terbuka dengan nilai `Head Office-{runId}-034`
27. Ubah nama menjadi `Head Office Edit-{runId}-034`, klik `[Save]`
28. Verifikasi toast sukses: "Success, group has been updated."
29. Verifikasi nama baru `Head Office Edit-{runId}-034` tampil di sidebar
30. Ketik Search `Head Office Edit-{runId}-034`, tekan Enter
31. Verifikasi nama baru `Head Office Edit-{runId}-034` tampil di tabel
32. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-116: Rename node yang menjadi header

33. Klik node `Warehouse Jakarta-{runId}-034` di sidebar
34. Catat Total User dan Total Member pada Group Context Header sebagai pembanding langkah 38
35. Klik ikon `⋯` pada node `Warehouse Jakarta-{runId}-034` di sidebar, lalu pilih "Edit"
36. Ubah nama menjadi `Warehouse Jakarta Edit-{runId}-034`, klik `[Save]`
37. Verifikasi Group Context Header menampilkan `Warehouse Jakarta Edit-{runId}-034`
38. Verifikasi angka Total User dan Total Member pada Group Context Header sama dengan nilai pada langkah 34

## Notes

- Langkah penghubung (S-03): langkah 1, 10, dan 30 (Search untuk menemukan baris target, R-16), langkah 17 (mengganti isi Search dengan nama baru karena Search `Region C-{runId}-034` masih aktif setelah rename dan tidak lagi memuat baris itu, R-16), langkah 8 (menutup popup Edit yang tidak diubah; tertutup tanpa dialog Unsaved Changes), langkah 9, 24, dan 32 (reset Search, S-09), langkah 11, 14, dan 34 (pencatatan nilai pembanding dan waktu).
- Spec ini 38 langkah, di atas smell sekitar 35 langkah. Alasan: satu topik (Popup Edit dan rename) pada satu aktor dan satu halaman; tiap blok TC memakai node seed sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan langkah Search atau reset yang diulang per blok tidak dapat digabung.
- TC-AC-SG-113 memakai node Pre-setup `Region B` hanya untuk dibuka dan ditutup; nilai tidak berubah dan Last Updated tidak berubah.
- Temuan untuk QA: TC-AC-SG-114 Expected butir b "kolom Modified By dan Last Updated pada baris terbarui" tidak menyebut nilai; spec mengasersi Modified By berformat `[First Name] [Last Initial]` dan Last Updated sesuai waktu aksi dengan toleransi satu menit (S-12, R-14).
