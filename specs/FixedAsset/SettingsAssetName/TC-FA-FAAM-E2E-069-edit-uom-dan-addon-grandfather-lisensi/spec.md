---
id: TC-FA-FAAM-E2E-069-edit-uom-dan-addon-grandfather-lisensi
title: "Edit: Ganti UoM dan Addon Tersimpan Tanpa Lisensi Aktif (Grandfather)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-208
  - TC-FA-FAAM-222
coverage:
  web: automated
---

# Edit: Ganti UoM dan Addon Tersimpan Tanpa Lisensi Aktif (Grandfather)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10c: Asset Name `Addon Grand Item` (Default Addon `Maps`, lisensi Maps sudah berakhir, Total Asset 0); dipakai lewat salinan seed `Addon Grand Item {runId}-069` (Code salinan mengikuti pola seed). Lisensi addon `Maps` tidak teralokasi aktif pada client Automation (Pre-setup #10b). Salinan tidak ada di Tabel Data Dinamis TC (lihat Temuan untuk QA).
- Data Dinamis (salinan seed fixture #13d, Dinamis #28): `Edit Target Item 222 {runId}-069` (Code `ETI222`). UoM `Set` (Pre-setup #24).
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-069` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-208: Addon tersimpan yang lisensinya tidak aktif tetap tampil terkunci, dapat dilepas, dan simpan tanpa ubah diterima

1. Ketik Search `Addon Grand Item {runId}-069`, tekan Enter
2. Klik `⋯` baris `Addon Grand Item {runId}-069` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Verifikasi chip `Maps` tampil terkunci 🔒
4. Ubah Code menjadi `AGI2`
5. Klik `[Save]`
6. Verifikasi Save tanpa mengubah addon diterima (toast `Success, asset name has been updated.`)
7. Klik `⋯` baris `Addon Grand Item {runId}-069` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
8. Lepas chip `Maps`
9. Coba pilih `Maps` lagi pada dropdown Default Addon
10. Verifikasi opsi `Maps` terkunci dengan tooltip `Requires an active Maps license`
11. Klik `[✕]` pada modal Edit
12. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
13. Klik `[Leave]`

### TC-FA-FAAM-222: Mengganti UoM pada Edit tersimpan dan menjadi nilai baru di List

14. Ganti isi kotak search dengan `Edit Target Item 222 {runId}-069`, tekan Enter
15. Klik `⋯` baris `Edit Target Item 222 {runId}-069` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
16. Ubah UoM menjadi `Set`
17. Klik `[Save]`
18. Verifikasi toast `Success, asset name has been updated.` tampil
19. Verifikasi kolom UoM baris `Edit Target Item 222 {runId}-069` menampilkan `Set`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 14 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 11 (✕, dialog Unsaved Changes, `[Leave]`, S-08).
- Langkah Uji TC-FA-FAAM-208 "Edit Code lalu `[Save]`" tidak menyebut Code baru; spec memakai `AGI2`. Modal Edit tertutup setelah Save sukses sehingga langkah berikutnya membukanya lagi untuk melepas chip `Maps`.
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-208 memakai fixture Pre-setup #10c langsung untuk aksi Save yang mengubah Code; Tabel Data Dinamis tidak memuat salinannya. Spec memakai salinan seed API bernama bersuffix agar Pre-setup bersama tidak berubah (S-06).
