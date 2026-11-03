---
id: TC-FA-CF-E2E-085-delete-single-dialog-konfirmasi-dan-nilai-aset
title: "Delete Single: Dialog Konfirmasi, Cancel, Konfirmasi Hapus, dan Penghapusan Nilai Aset Tanpa Orphan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-317
  - TC-FA-CF-318
  - TC-FA-CF-319
  - TC-FA-CF-320
coverage:
  web: automated
---

# Delete Single: Dialog Konfirmasi, Cancel, Konfirmasi Hapus, dan Penghapusan Nilai Aset Tanpa Orphan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menghapus field baseline Company Nilai dan membaca log permanen yang dibagi suite.
- Akun aktor: Total Control Company Nilai (Pre-setup #18; pengguna Sarah Johnson, Modified By `Sarah J`), kredensial `Spectra.env.FA_TC_NILAI_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Company Nilai (Pre-setup #18, memuat baseline Company Alpha #11 dan #12 serta field dan aset tambahan): `Legacy Tag` (Text, Scope kosong, Specific), `Maintenance Note` (Text General, bernilai `Checked` pada aset `A1`), `Rated Power` (Numeric 1 Decimal Place {Generator, Pump}, bernilai `12.5` pada `A1`), `Required Hello` (Text General, bernilai `Hello` pada `A1`), aset `A1` (Asset Name `Pump`, Active). Spec ini menghapus `Legacy Tag` (langkah 19) dan `Maintenance Note` beserta nilainya (langkah 24). Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.nilai`); hook `after` memulihkan. Tabel Company Nilai memuat lebih dari sepuluh baris sehingga ukuran halaman diatur 25 (Pagination 10, 25, 50, dan 100).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: membaca jumlah entri Modal Changelog, System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log), dan Activity Log (Reports & Logs > Activity Log > Tab User Action) sebagai baseline (disediakan tim FE/BE; hanya selisih terhadap baseline yang diasersi); membuka Detail aset `A1` (Pre-setup #31).
- State global: tidak ada yang diubah selain data field baseline dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

1. Pilih ukuran halaman 25 pada Pagination
2. Catat jumlah entri awal pada Modal Changelog, System Log aktor, dan Activity Log sebagai baseline (aksi baca tanpa `Verifikasi`)

### TC-FA-CF-317 dan TC-FA-CF-320: Dialog Delete single dan Cancel

3. Klik row action `⋯` > `Delete` pada baris `Legacy Tag`
4. Verifikasi dialog konfirmasi danger berjudul `Delete Custom Field` dengan bullet `• Legacy Tag`, teks `All asset data for this field will be permanently lost. This action cannot be undone. Are you sure you want to delete it?`, serta tombol `[Cancel]` dan `[Delete]`
5. Klik `[Cancel]`
6. Verifikasi dialog tertutup
7. Verifikasi baris `Legacy Tag` tetap ada
8. Verifikasi tidak ada toast
9. Klik icon Changelog
10. Verifikasi jumlah entri Modal Changelog sama dengan baseline langkah 2 (tidak ada entri dari langkah 5)
11. Tutup modal Changelog dengan `✕`
12. Buka System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log)
13. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 2 (tidak ada entri dari langkah 5)
14. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action)
15. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 2 (tidak ada entri dari langkah 5)
16. Buka Fixed Asset > Settings > Custom Fields (tab General)
17. Pilih ukuran halaman 25 pada Pagination

### TC-FA-CF-318: Confirm Delete single

18. Klik row action `⋯` > `Delete` pada baris `Legacy Tag`
19. Klik `[Delete]`
20. Verifikasi dialog tertutup
21. Verifikasi toast sukses `Success, custom field has been deleted.` tampil
22. Verifikasi baris `Legacy Tag` hilang dari tabel

### TC-FA-CF-319: Delete field bernilai menghapus definisi dan nilai aset tanpa orphan

23. Klik row action `⋯` > `Delete` pada baris `Maintenance Note`
24. Klik `[Delete]`
25. Verifikasi baris `Rated Power` tampil di tabel
26. Verifikasi baris `Maintenance Note` hilang dari tabel
27. Buka Detail aset `A1`
28. Verifikasi Detail aset `A1` menampilkan field `Required Hello` bernilai `Hello`
29. Verifikasi Detail aset `A1` tidak memuat field `Maintenance Note` maupun nilai `Checked` (tidak ada nilai yang tertinggal tanpa field induk)

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 317 dan 320 (dialog yang dibuka pada langkah 3 dipakai bersama; tanpa mutasi), lalu 318 dan 319 (aksi Delete, paling akhir; S-10). Urutan menyimpang dari urutan TC sumber (317, 318, 319, 320) agar baseline log (langkah 2) belum terpengaruh tulisan log dari Delete.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 17 (ukuran halaman 25 agar baris target Company Nilai tampil tanpa Search), langkah 2 (baseline log), langkah 9, 12, dan 14 (membuka surface log), langkah 11 (menutup modal Changelog), dan langkah 16 (kembali ke layar Custom Fields).
- P-1: asersi "tanpa entri log" TC-FA-CF-320 (langkah 10, 13, dan 15) berada di spec ini karena bergantung pada state dialog Delete yang dibuka langkah 3; dipenuhi dengan baseline jumlah entri (langkah 2; S-12).
- Asersi tambahan di luar Expected TC (S-03): langkah 25 (baris pembanding `Rated Power` sebagai anchor absence baris `Maintenance Note`; TC-FA-CF-319 tidak mengasersi toast) dan langkah 28 (field `Required Hello` bernilai `Hello` sebagai anchor absence pada Detail aset `A1`).
- TC-FA-CF-317, 318, dan 320 menyebut Company Alpha dengan baseline Pre-setup #11 dan #12, sedangkan TC-FA-CF-319 menyebut Company Nilai. Spec menjalankan keempat TC di Company Nilai karena Company itu memuat baseline Company Alpha yang sama (Pre-setup #18) sehingga tidak ada pergantian akun atau Company di tengah spec.
- Temuan untuk QA:
  - Tata letak dan label Detail aset tidak didefinisikan PRD modul ini (NC-01); langkah 27 sampai 29 memakai istilah TC.
  - TC-FA-CF-319 butir b menyebut "tidak ada nilai yang tertinggal tanpa field induk" sebagai penjelasan atas Detail aset tanpa field dan nilai; ditulis satu `Verifikasi` (langkah 29).
  - TC-FA-CF-319 tidak mengasersi toast sukses Delete; anchor absence diambil dari baris pembanding (langkah 25).
  - Email akun Total Control Company Nilai tidak ada di Pre-setup TC.
