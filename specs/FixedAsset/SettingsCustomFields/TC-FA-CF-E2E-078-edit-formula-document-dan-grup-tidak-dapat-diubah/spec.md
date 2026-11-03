---
id: TC-FA-CF-E2E-078-edit-formula-document-dan-grup-tidak-dapat-diubah
title: "Edit: Token Formula, File Document, dan Grup Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-283
  - TC-FA-CF-284
  - TC-FA-CF-285
  - TC-FA-CF-286
coverage:
  web: automated
---

# Edit: Token Formula, File Document, dan Grup Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Asset Serial Tag` (Text, Required Yes), `Global Doc File` (Document General Global, berkas `original.pdf`), dan `Total Cost` (Formula `Purchase Price + 10`). Berkas uji `replacement.pdf` (Pre-setup #36). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Kemampuan teknis: unggah berkas lewat kontrol Document; membaca jumlah dan isi entri Changelog tab General (disediakan tim FE/BE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Global Doc File` kembali ke `original.pdf`, `Total Cost` kembali ke `Purchase Price + 10`) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-286: Grup field tidak dapat diubah antar tab pada Edit

2. Klik row action `⋯` > `Edit` pada baris `Asset Serial Tag`
3. Verifikasi seluruh kontrol modal Edit tidak memuat kontrol pemilihan grup
4. Klik `[Save]` tanpa mengubah apa pun
5. Verifikasi field `Asset Serial Tag` tetap pada tab General: baris `Asset Serial Tag` tampil pada tabel tab General

### TC-FA-CF-285: File Global Document dapat diganti tetapi tidak dapat dikosongkan

6. Klik row action `⋯` > `Edit` pada baris `Global Doc File`
7. Klik tombol hapus pada file
8. Klik `[Save]`
9. Verifikasi pesan inline `Value must not be empty` tampil
10. Verifikasi Save ditolak: modal tetap terbuka
11. Klik icon close `[✕]`
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-FA-CF-284: Edit field Document ber-Global menampilkan nama file tersimpan dan file pengganti berlaku saat Save

14. Klik row action `⋯` > `Edit` pada baris `Global Doc File`
15. Verifikasi kontrol Value menampilkan nama file `original.pdf` pre-filled
16. Pilih berkas `replacement.pdf`
17. Klik `[Save]`
18. Klik row action `⋯` > `Edit` pada baris `Global Doc File`
19. Verifikasi kontrol Value menampilkan nama file `replacement.pdf`
20. Klik icon close `[✕]`

### TC-FA-CF-283: Mengubah token Formula adalah perubahan nyata yang tersimpan

21. Catat jumlah entri Edit properti `Formula` untuk `Total Cost` di Modal Changelog tab General
22. Klik row action `⋯` > `Edit` pada baris `Total Cost`
23. Ubah token Formula menjadi field `Purchase Price` × konstanta `2`
24. Klik `[Save]`
25. Verifikasi toast sukses `Success, custom field has been updated.` tampil
26. Verifikasi toast `No changes to save.` tidak tampil
27. Buka Modal Changelog tab General
28. Verifikasi Modal Changelog memuat tepat satu entri Edit properti `Formula` untuk `Total Cost` lebih banyak dari jumlah yang dicatat sebelum aksi
29. Tutup Modal Changelog

## Notes

- Urutan TC di spec: 286, 285, 284, 283. Kasus yang tidak mengubah data (286) dan yang ditolak (285) berjalan lebih dulu; aksi yang menyimpan (284, 283) berada di akhir (bagian 3 prinsip 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 4 (Save tanpa perubahan pada TC-FA-CF-286 adalah langkah TC; modal tertutup sebagai no-op), langkah 11 sampai 13 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 20 (menutup modal yang tidak diubah sejak disimpan), langkah 21 dan 29 (baseline dan penutupan Modal Changelog).
- Langkah 28 memakai selisih terhadap baseline (S-12), bukan jumlah absolut entri Changelog.
- Temuan untuk QA:
  - TC-FA-CF-286 tidak menyebut hasil `[Save]` tanpa perubahan (modal tertutup dengan toast netral); spec hanya mengasersi bahwa field tetap berada di tab General sesuai Expected.
  - TC-FA-CF-284 tidak menyebut toast sesudah Save; spec mengasersi hasil lewat kontrol Value pada Edit berikutnya.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
