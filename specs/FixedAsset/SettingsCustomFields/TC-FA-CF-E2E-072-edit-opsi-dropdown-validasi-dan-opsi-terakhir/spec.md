---
id: TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir
title: "Edit Opsi Dropdown: Tambah, Duplikat, Opsi Terakhir, dan Validasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-254
  - TC-FA-CF-255
  - TC-FA-CF-256
  - TC-FA-CF-257
  - TC-FA-CF-258
  - TC-FA-CF-259
  - TC-FA-CF-625
coverage:
  web: automated
---

# Edit Opsi Dropdown: Tambah, Duplikat, Opsi Terakhir, dan Validasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`; aset A1 = `Gold`) dan `Single Option` (Dropdown satu opsi `Only`, tidak dipakai aset). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Brand Tier` kembali tanpa opsi `Platinum`) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Kemampuan teknis: injeksi nilai langsung ke DOM input (Pre-setup #26); pengetikan karakter emoji lewat keyboard; jeda 600 ms (jeda pendek nyata, sebagai pilihan spec karena TC menyebutnya).
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100
2. Klik row action `⋯` > `Edit` pada baris `Brand Tier`

### TC-FA-CF-625: Emoji pada nama opsi Edit diblok saat mengetik tanpa pesan

3. Ketik `Gold😊` pada input Values
4. Verifikasi emoji tidak masuk ke input Values
5. Verifikasi tidak ada pesan error

### TC-FA-CF-255: Menamai opsi dengan nama opsi lain case-insensitive ditolak pada Edit

6. Ganti isi input Values dengan `gold` dan tunggu 600 ms
7. Verifikasi pesan inline `Option name already exists` tampil

### TC-FA-CF-257: Nama opsi 121 karakter pada Edit menampilkan pesan batas

8. Ganti isi input Values dengan 121 karakter (huruf `C` diulang 121 kali)
9. Verifikasi pesan inline `Max. 120 characters` tampil langsung

### TC-FA-CF-259: Opsi berisi spasi saja pada Edit ditolak saat Save

10. Injeksi opsi tiga spasi ke DOM input Values
11. Klik `[Save]`
12. Verifikasi pesan inline `Option name must not be empty` tampil

### TC-FA-CF-258: Emoji yang lolos filter klien pada nama opsi Edit ditolak server

13. Injeksi opsi `Gold😊` ke DOM input Values
14. Klik `[Save]`
15. Verifikasi pesan inline `Option name contains invalid characters` tampil
16. Verifikasi perubahan tidak tersimpan: modal tetap terbuka dan toast `Success, custom field has been updated.` tidak tampil
17. Klik icon close `[✕]`
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`

### TC-FA-CF-256: Menghapus opsi terakhir pada Edit tidak menampilkan dialog blok dan Save ditolak

20. Klik row action `⋯` > `Edit` pada baris `Single Option`
21. Klik `✕` pada badge `Only`
22. Klik `[Save]`
23. Verifikasi dialog blok tidak tampil
24. Verifikasi pesan inline `Dropdown options must not be empty` tampil
25. Verifikasi Save ditolak: modal tetap terbuka
26. Klik icon close `[✕]`
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Leave]`

### TC-FA-CF-254: Opsi baru dapat ditambahkan kapan saja pada field yang sudah bernilai

29. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
30. Ketik `Platinum` pada input Values lalu tekan Enter
31. Klik `[Save]`
32. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
33. Verifikasi opsi `Platinum` tersimpan di urutan terakhir: badge berurutan `Gold`, `Silver`, `Bronze`, `Platinum`
34. Klik icon close `[✕]`
35. Buka Detail aset `A1`
36. Verifikasi nilai aset `A1` untuk field `Brand Tier` tidak berubah (`Gold`)

## Notes

- Urutan TC di spec: 625, 255, 257, 259, 258, 256, 254. Kasus tanpa Save dan kasus yang ditolak berjalan pada satu pembukaan modal `Brand Tier` dengan isi input Values diganti di antara kasus; TC-FA-CF-256 memakai `Single Option`; TC-FA-CF-254 yang menyimpan opsi baru berada di akhir (bagian 3 prinsip 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 2, 6, 8, dan 10 (membuka modal dan mengganti isi input Values di antara kasus), langkah 17 sampai 19 dan 26 sampai 28 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- TC-FA-CF-258 adalah satu TC objek-uji ringan kelas a (P-5 butir b): injeksi nilai ke DOM sebagai objek uji validasi server; hanya satu TC kelas a di spec ini. Asersi hanya pada pesan inline dan keadaan modal.
- Spec melewati sekitar 35 langkah (36 langkah). Seluruhnya satu topik (validasi dan penambahan opsi pada modal Edit Dropdown), satu akun, satu dataset Company Nilai; kasus validasi berurutan pada modal yang sama dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Mengetik `Gold😊` (TC-FA-CF-625) memasukkan `Gold` yang sama dengan opsi yang sudah ada; pesan duplikat `Option name already exists` dapat muncul setelah debounce 600 ms. Spec mengasersi ketiadaan pesan error segera setelah mengetik.
  - TC-FA-CF-258 dan TC-FA-CF-259 tidak menyebut cara menutup modal sesudah penolakan; spec menutup lewat `[✕]` dan `[Leave]` karena form dirty.
  - Halaman Detail aset `A1` dan cara membukanya tidak dijelaskan di TC; spec menulisnya persis seperti TC.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
