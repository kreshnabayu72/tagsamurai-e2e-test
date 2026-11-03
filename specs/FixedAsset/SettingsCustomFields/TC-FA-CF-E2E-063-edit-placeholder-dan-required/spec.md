---
id: TC-FA-CF-E2E-063-edit-placeholder-dan-required
title: "Edit: Placeholder dan Required"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-213
  - TC-FA-CF-214
  - TC-FA-CF-215
  - TC-FA-CF-216
  - TC-FA-CF-217
  - TC-FA-CF-218
  - TC-FA-CF-624
coverage:
  web: automated
---

# Edit: Placeholder dan Required

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Storage Capacity` (Numeric, Placeholder kustom `Capacity in GB`, Required No), `Maintenance Note` (Text General, bernilai `Checked` pada aset A1), dan `Total Cost` (Formula `Purchase Price + 10`). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Storage Capacity`, `Maintenance Note`) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Kemampuan teknis: injeksi nilai langsung ke DOM input (Pre-setup #26); pengetikan karakter emoji lewat keyboard.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-217: Kontrol Placeholder tidak tampil pada Edit field bertipe Formula

2. Klik row action `⋯` > `Edit` pada baris `Total Cost`
3. Verifikasi Body: kontrol Placeholder, Value Type, dan Required tidak tampil
4. Verifikasi Body: Formula Builder tampil dengan token tersimpan
5. Klik icon close `[✕]`

### TC-FA-CF-624: Emoji pada Placeholder Edit diblok saat mengetik tanpa pesan

6. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
7. Ketik `Cap😊` pada Placeholder
8. Verifikasi emoji tidak masuk ke input Placeholder
9. Verifikasi tidak ada pesan error

### TC-FA-CF-215: Placeholder 121 karakter pada Edit ditolak

10. Ganti isi Placeholder dengan 121 karakter (huruf `B` diulang 121 kali)
11. Klik `[Save]`
12. Verifikasi pesan inline `Max. 120 characters` tampil
13. Verifikasi Save ditolak: modal tetap terbuka

### TC-FA-CF-216: Emoji yang lolos filter klien pada Placeholder Edit ditolak server

14. Injeksi `Cap😊` ke DOM input Placeholder
15. Klik `[Save]`
16. Verifikasi pesan inline `Placeholder contains invalid characters` tampil
17. Verifikasi perubahan tidak tersimpan: modal tetap terbuka dan toast `Success, custom field has been updated.` tidak tampil

### TC-FA-CF-214: Placeholder dikosongkan pada Edit kembali ke placeholder default tipe data

18. Kosongkan Placeholder
19. Klik `[Save]`
20. Verifikasi kolom Placeholder baris `Storage Capacity` menampilkan `Enter storage capacity`

### TC-FA-CF-218: Required diubah dari No ke Yes tersimpan

21. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
22. Ubah toggle Required ke Yes
23. Klik `[Save]`
24. Verifikasi kolom Required baris `Storage Capacity` menampilkan `Yes`

### TC-FA-CF-213: Placeholder diubah setelah field memiliki nilai aset tetap diizinkan

25. Klik row action `⋯` > `Edit` pada baris `Maintenance Note`
26. Ubah Placeholder menjadi `Write a note`
27. Klik `[Save]`
28. Verifikasi toast sukses `Success, custom field has been updated.` tampil
29. Verifikasi kolom Placeholder baris `Maintenance Note` menampilkan `Write a note`

## Notes

- Urutan TC di spec: 217, 624, 215, 216, 214, 218, 213. Kasus tanpa Save dan kasus yang ditolak berjalan pada satu pembukaan modal `Storage Capacity` dengan isi Placeholder diganti di antara kasus; aksi yang menyimpan (214, 218, 213) berada di akhir (bagian 3 prinsip 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 5 (menutup modal `Total Cost` yang tidak diubah, tanpa dialog), langkah 10 dan 18 (mengganti atau mengosongkan isi Placeholder di antara kasus pada modal yang sama).
- TC-FA-CF-216 adalah satu TC objek-uji ringan kelas a (P-5 butir b): injeksi nilai ke DOM sebagai objek uji validasi server; hanya satu TC kelas a di spec ini. Asersi hanya pada pesan inline dan keadaan modal.
- Nama field tidak diubah di spec ini, sehingga tidak ada nilai Dinamis bersuffix; nilai Placeholder yang tersimpan (`Write a note`) dan kolom Required dikembalikan ke baseline oleh hook `after`.
- Temuan untuk QA:
  - Precondition TC-FA-CF-624 menyebut Company Alpha (Pre-setup #11 dan #12) sedangkan TC lain di spec ini memakai Company Nilai (Pre-setup #18). Spec memakai Company Nilai untuk seluruh TC karena #18 berdasar Company Alpha dan baris `Storage Capacity` identik; tidak ada ganti akun.
  - TC-FA-CF-213 menulis nilai Placeholder `Write a note` yang tersimpan; TC tidak menyebut apakah ini data Dinamis. Spec memperlakukannya sebagai perubahan baseline yang dipulihkan hook `after`.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
