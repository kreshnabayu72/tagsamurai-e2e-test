---
id: TC-FA-LBL-E2E-036-modal-create-edit-label-screening-keyboard-form-kotor-dan-klik-ganda-submit
title: "Modal Create/Edit Label: screening, keyboard, form kotor, dan klik ganda Submit"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/modal-create-edit-label/screening
  - FALB:defaults-ordering-spec/default-warna-baru
  - FALB:obl/modal-create-edit-label/keyboard
  - FALB:obl/modal-create-edit-label/dirty-close
  - FALB:obl/modal-create-edit-label/double-submit
coverage:
  web: automated
---

# Modal Create/Edit Label: screening, keyboard, form kotor, dan klik ganda Submit

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-67` (label seed `Mdl-{runId}-036` berwarna `#3B82F6` untuk mode Edit, dibuat lewat sesi API di hook `before`). `DU-68` (nama `Dbl-{runId}-036`, label yang dibuat oleh klik ganda `[Submit]` pada langkah 34).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding dan penghapusan label.
- State global: tidak ada yang diubah selain label `DU-68` yang dibuat spec ini. Hook `after` menghapus label `DU-67` dan `DU-68` lewat sesi API walau spec gagal di tengah.

## Test Steps

### FALB:obl/modal-create-edit-label/screening: Screening Modal Create dan Edit

1. Ketik Search `DU-67` (nama dasar `Mdl-{runId}-036`), tekan Enter
2. Klik `[+ Label]`
3. Verifikasi Modal tampil dengan judul `Create Label` dan tombol `[✕]` di header
4. Verifikasi field Label Name wajib berupa input teks tunggal kosong dengan placeholder `Enter label name`
5. Verifikasi Swatch Trigger menampilkan lingkaran warna terpilih
6. Verifikasi section Live Preview berkaption `Live Preview` memuat chip pratinjau
7. Verifikasi checkbox `Stay on this form after submitting` tampil pada footer mode Create
8. Verifikasi footer memuat tombol `[Clear Field]` dan `[Submit]` tanpa tombol `[Cancel]`
9. Klik `[✕]` pada header Modal Create Label
10. Klik `[⋯]` pada baris label `DU-67`, pilih `Edit`
11. Verifikasi Modal tampil dengan judul `Edit Label` dan field Label Name terisi `DU-67`
12. Verifikasi checkbox `Stay on this form after submitting` tidak tampil pada Modal Edit
13. Verifikasi footer memuat tombol `[Clear Field]` dan `[Save]` tanpa tombol `[Cancel]`
14. Klik `[✕]` pada header Modal Edit Label

### FALB:defaults-ordering-spec/default-warna-baru: Warna bawaan form Create

15. Klik `[+ Label]`
16. Verifikasi Swatch Trigger menampilkan warna `#3B82F6`
17. Klik Swatch Trigger
18. Verifikasi kolom Hex pada Color Picker Overlay menampilkan `#3B82F6`, yaitu swatch baris 3 kolom 3 pada Palet Preset
19. Verifikasi chip Live Preview berlatar warna `#3B82F6`
20. Klik Swatch Trigger untuk menutup Color Picker Overlay

### FALB:obl/modal-create-edit-label/keyboard: Esc menutup Modal

21. Tekan Esc
22. Verifikasi Modal Create Label tertutup tanpa dialog `Unsaved Changes`

### FALB:obl/modal-create-edit-label/dirty-close: Menutup form kotor

23. Klik `[+ Label]`
24. Ketik Label Name `DU-68`
25. Klik area backdrop di luar Modal Create Label
26. Verifikasi Modal tetap terbuka dengan Label Name berisi `DU-68` dan dialog `Unsaved Changes` tidak tampil
27. Klik `[✕]` pada header Modal Create Label
28. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
29. Klik `[Leave]`
30. Verifikasi Modal Create Label tertutup

### FALB:obl/modal-create-edit-label/double-submit: Klik ganda Submit hanya memproses satu request

31. Klik `[+ Label]`
32. Ketik Label Name `DU-68`
33. Pastikan checkbox `Stay on this form after submitting` tidak tercentang
34. Klik `[Submit]` dua kali berturut-turut dengan cepat
35. Tunggu hingga Modal Create Label tertutup
36. Ketik Search `DU-68`, tekan Enter
37. Verifikasi tepat satu baris label `DU-68` tampil di Labels List

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-67`, R-16), langkah 2, 10, 15, 23, dan 31 (membuka modal), langkah 9 dan 14 (menutup modal yang belum diubah), langkah 17 dan 20 (membuka dan menutup Color Picker Overlay), langkah 33 (menjamin Modal menutup sesudah Submit), langkah 35 dan 36 (menunggu aksi selesai lalu mencari label hasil Submit, R-16).
- Urutan (S-10): aksi yang membuat data (klik ganda `[Submit]`, langkah 34) berada di akhir spec.
- Anchor positif (bagian 8b butir 2): langkah 26 menjadi anchor ketiadaan dialog `Unsaved Changes` pada klik backdrop; langkah 3 sampai 8 membuktikan Modal sudah termuat sebelum langkah 22 mengasersi penutupan tanpa dialog.
- Isi dialog `Unsaved Changes` mengikuti konvensi platform (`prd-conventions.md` §24.1c), bukan PRD modul; spec hanya mengasersi dialog dan tombolnya.
- Temuan PRD: `FALB:obl/modal-create-edit-label/keyboard` mencakup focus trap dan fokus kembali ke pemicu, tetapi PRD hanya menyatakan Modal ditutup lewat `[✕]` atau Esc dan klik backdrop tidak menutup; focus trap dan fokus kembali ke pemicu tidak dinyatakan sehingga tidak diasersi.
- Spec ini di atas smell 35 langkah (37 langkah). Alasan dipertahankan: seluruh blok satu kelas harness (form modal) dan tiap blok membuka modalnya sendiri dari keadaan bersih; data yang dibutuhkan (`DU-67`) disiapkan hook `before`, dan hanya blok terakhir yang membuat data.
