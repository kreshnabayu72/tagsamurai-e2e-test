---
id: TC-FA-CF-E2E-094-bulk-delete-dialog-konfirmasi-dan-cancel
title: "Bulk Delete: Dialog Konfirmasi, Varian Single, Cancel, dan Penghapusan Atomik Beserta Nilai Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-349
  - TC-FA-CF-350
  - TC-FA-CF-351
  - TC-FA-CF-352
coverage:
  web: automated
---

# Bulk Delete: Dialog Konfirmasi, Varian Single, Cancel, dan Penghapusan Atomik Beserta Nilai Aset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menghapus field baseline Company Nilai.
- Akun aktor: Total Control Company Nilai (Pre-setup #18; pengguna Sarah Johnson, Modified By `Sarah J`), kredensial `Spectra.env.FA_TC_NILAI_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Company Nilai (Pre-setup #18, memuat baseline Company Alpha #11 dan #12 serta field dan aset tambahan): `Legacy Tag` dan `Compliance File` (dibaca dan dibatalkan, tidak dihapus oleh langkah 2 sampai 15), `Maintenance Note` (Text General, bernilai `Checked` pada aset `A1`) dan `Rated Power` (Numeric 1 Decimal Place {Generator, Pump}, bernilai `12.5` pada `A1`) dihapus pada langkah 18, `Required Hello` (Text General, bernilai `Hello` pada `A1`; anchor Detail aset), aset `A1` (Asset Name `Pump`, Active). Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.nilai`); hook `after` memulihkan. Tabel Company Nilai memuat lebih dari sepuluh baris sehingga ukuran halaman diatur 25 (Pagination 10, 25, 50, dan 100).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: mencentang baris tabel; membuka Detail aset `A1` (Pre-setup #31).
- State global: tidak ada yang diubah selain data field baseline dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

1. Pilih ukuran halaman 25 pada Pagination

### TC-FA-CF-349 dan TC-FA-CF-352: Dialog Bulk Delete dan Cancel mempertahankan seleksi

2. Centang baris `Legacy Tag` dan `Compliance File`
3. Klik `[Delete]` pada Bulk Action Bar
4. Verifikasi dialog konfirmasi danger berjudul `Delete Custom Fields` dengan bullet `• Legacy Tag` dan `• Compliance File` dalam container scrollable, teks `All asset data for these fields will be permanently lost. This action cannot be undone. Are you sure you want to delete them?`, serta tombol `[Cancel]` dan `[Delete]`
5. Klik `[Cancel]`
6. Verifikasi dialog tertutup
7. Verifikasi seleksi `Legacy Tag` dan `Compliance File` dipertahankan
8. Verifikasi Bulk Action Bar dipertahankan
9. Verifikasi tidak ada perubahan data: baris `Legacy Tag` dan `Compliance File` tetap ada
10. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-351: Bulk Delete dengan satu baris terpilih memakai dialog varian single

11. Centang hanya baris `Legacy Tag`
12. Klik `[Delete]` pada Bulk Action Bar
13. Verifikasi dialog konfirmasi danger berjudul `Delete Custom Field` dengan bullet `• Legacy Tag`, teks `All asset data for this field will be permanently lost. This action cannot be undone. Are you sure you want to delete it?`, serta tombol `[Cancel]` dan `[Delete]`
14. Klik `[Cancel]`
15. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-350: Confirm Bulk Delete menghapus field beserta nilainya secara atomik

16. Centang baris `Maintenance Note` dan `Rated Power`
17. Klik `[Delete]` pada Bulk Action Bar
18. Klik `[Delete]` pada dialog
19. Verifikasi toast sukses `Success, custom field has been deleted.` tampil
20. Verifikasi baris `Maintenance Note` dan `Rated Power` hilang dari tabel
21. Verifikasi seleksi di-reset
22. Buka Detail aset `A1`
23. Verifikasi Detail aset `A1` menampilkan field `Required Hello` bernilai `Hello`
24. Verifikasi Detail aset `A1` tidak memuat field `Maintenance Note` dan `Rated Power` maupun nilai aset terkaitnya (tidak ada nilai yang tertinggal)

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 349 dan 352 (dialog yang dibuka pada langkah 3 dipakai bersama; seleksi dua baris TC-FA-CF-352 dipenuhi seleksi yang sama pada langkah 2), 351 (tanpa mutasi), lalu 350 (aksi Delete, paling akhir; S-10). Urutan menyimpang dari urutan TC sumber (349, 350, 351, 352).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 25 agar baris target Company Nilai tampil tanpa Search), langkah 5 dan 14 (menutup dialog dengan `[Cancel]`; TC-FA-CF-351 tidak menyebut cara menutup, TC-FA-CF-352 menyebutnya), dan langkah 10 dan 15 (membersihkan seleksi; S-09).
- Asersi tambahan di luar Expected TC (S-03): langkah 23 (field `Required Hello` bernilai `Hello` sebagai anchor absence pada Detail aset `A1`). Langkah 7 dan 8 memecah "seleksi dan Bulk Action Bar dipertahankan" menjadi dua `Verifikasi`.
- TC-FA-CF-349, 351, dan 352 menyebut Company Alpha dengan baseline Pre-setup #11 dan #12, sedangkan TC-FA-CF-350 menyebut Company Nilai. Spec menjalankan keempat TC di Company Nilai karena Company itu memuat baseline Company Alpha yang sama (Pre-setup #18) sehingga tidak ada pergantian akun atau Company di tengah spec.
- Temuan untuk QA:
  - TC-FA-CF-350 butir b menggabungkan "Detail aset `A1` tanpa field dan nilai" dengan "seleksi di-reset" dalam satu butir; spec memisahkan seleksi di-reset (langkah 21, diamati di tabel sebelum berpindah ke Detail aset) dari Detail aset (langkah 24).
  - TC-FA-CF-350 tidak mengasersi entri log Bulk Delete; TC-FA-CF-350 judul "secara atomik" teramati hanya lewat penghapusan kedua field dan nilainya.
  - Tata letak dan label Detail aset tidak didefinisikan PRD modul ini (NC-01); langkah 22 sampai 24 memakai istilah TC.
  - Email akun Total Control Company Nilai tidak ada di Pre-setup TC.
