---
id: TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name
title: "Screening Modal Edit dan Validasi Field Name"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-205
  - TC-FA-CF-207
  - TC-FA-CF-208
  - TC-FA-CF-209
  - TC-FA-CF-210
  - TC-FA-CF-211
coverage:
  web: automated
---

# Screening Modal Edit dan Validasi Field Name

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Storage Capacity` (Numeric 0 Decimal Places, Placeholder `Capacity in GB`, Scope {Generator, Pump}, Value Type Specific, Required No) dan `Legacy Tag` (Text, Scope kosong). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (di sini `Storage Capacity` kembali ke nama baseline) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- Kemampuan teknis: injeksi nilai langsung ke DOM input (Pre-setup #26); pengetikan karakter emoji lewat keyboard.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-205: Screening modal Edit Custom Field dengan data pre-filled

2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Verifikasi Header: judul `Edit Custom Field`
4. Verifikasi Header: icon close `[✕]` tampil
5. Verifikasi Body: Field Name `Storage Capacity`
6. Verifikasi Body: Data Type `Numeric` dan dapat diubah
7. Verifikasi Body: Decimal Places `0 (Integer)` terpilih
8. Verifikasi Body: Placeholder `Capacity in GB`
9. Verifikasi Body: Scope `Specific Asset Name` dengan chip `Generator` dan `Pump`
10. Verifikasi Body: Value Type `Specific` terpilih
11. Verifikasi Body: Required `No`
12. Verifikasi Body: tidak ada input pemilihan grup dan tidak ada switch Active
13. Verifikasi Footer: tombol `[Clear Field]` dan `[Save]` rata kanan
14. Verifikasi Footer: tidak ada checkbox `Stay on this form after submitting`

### TC-FA-CF-207: Field Name dikosongkan pada Edit ditolak saat Save

15. Kosongkan Field Name
16. Klik `[Save]`
17. Verifikasi pesan inline `Field name must not be empty` tampil
18. Verifikasi modal tetap terbuka

### TC-FA-CF-208: Field Name 121 karakter pada Edit menampilkan pesan batas

19. Ganti isi Field Name dengan 121 karakter (huruf `A` diulang 121 kali)
20. Verifikasi pesan inline `Max. 120 characters` tampil langsung
21. Klik `[Save]`
22. Verifikasi Save ditolak: modal tetap terbuka

### TC-FA-CF-211: Emoji yang lolos filter klien pada Field Name Edit ditolak dengan pesan karakter terlarang

23. Injeksi nilai `Tag😊` ke DOM input Field Name
24. Klik `[Save]`
25. Verifikasi pesan inline `Field name contains invalid characters` tampil
26. Verifikasi perubahan tidak tersimpan: modal tetap terbuka dan toast `Success, custom field has been updated.` tidak tampil

### TC-FA-CF-209: Field Name tepat 120 karakter pada Edit diterima

27. Ganti isi Field Name dengan 120 karakter (huruf `A` diulang 120 kali)
28. Verifikasi tidak ada pesan batas karakter
29. Klik `[Save]`
30. Verifikasi toast sukses `Success, custom field has been updated.` tampil

### TC-FA-CF-210: Emoji pada Field Name Edit diblok saat mengetik tanpa pesan

31. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`
32. Ketik `Tag😊` pada Field Name
33. Verifikasi emoji tidak masuk ke input Field Name
34. Verifikasi tidak ada pesan error
35. Klik icon close `[✕]`
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`

## Notes

- Urutan TC di spec: 205, 207, 208, 211, 209, 210. Kasus yang ditolak (207, 208, 211) berjalan pada satu pembukaan modal `Storage Capacity` dengan Field Name diganti di antara kasus; TC-FA-CF-209 (Save sukses, mengganti nama field) ditaruh sesudahnya, dan TC-FA-CF-210 memakai baris `Legacy Tag` sebagai pembukaan terakhir. Aksi menyimpan berada di akhir (bagian 3 prinsip 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh 21 baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 15, 19, dan 27 (mengosongkan atau mengganti isi Field Name di antara kasus pada modal yang sama), langkah 35 sampai 37 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- Nama 120 dan 121 karakter adalah nilai batas literal (huruf `A`) dan tidak bersuffix; field hasil Save 120 karakter dikembalikan ke nama baseline oleh hook `after`.
- TC-FA-CF-211 adalah satu TC objek-uji ringan kelas a (P-5 butir b): injeksi nilai ke DOM sebagai objek uji validasi server; hanya satu TC kelas a di spec ini. Asersi hanya pada pesan inline dan keadaan modal.
- Spec melewati sekitar 35 langkah (37 langkah). Seluruhnya satu topik (modal Edit dan validasi Field Name), satu akun, satu dataset; kasus validasi berurutan pada modal yang sama dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Precondition TC-FA-CF-205 menyebut Company Alpha (Pre-setup #11 dan #12) sedangkan TC-FA-CF-207 sampai 211 menyebut Company Nilai (Pre-setup #18). Spec memakai Company Nilai untuk seluruh TC karena #18 berdasar Company Alpha dan baris `Storage Capacity` identik; tidak ada ganti akun di tengah spec.
  - Email Total Control Company Nilai dan nama env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
  - Pre-setup #18 diberi kategori "Custom field" padahal isinya definisi Company; tidak berdampak pada asersi.
  - TC-FA-CF-210 tidak menyebut cara menutup modal sesudah mengetik; spec menutup lewat `[✕]` dan `[Leave]` karena teks `Tag` tetap masuk ke input (form dirty).
