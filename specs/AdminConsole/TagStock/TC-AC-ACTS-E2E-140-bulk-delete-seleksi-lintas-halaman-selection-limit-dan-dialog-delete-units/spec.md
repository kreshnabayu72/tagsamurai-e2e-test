---
id: TC-AC-ACTS-E2E-140-bulk-delete-seleksi-lintas-halaman-selection-limit-dan-dialog-delete-units
title: "Bulk Delete: Checkbox Header Halaman Aktif, Select All Lintas Halaman, Seleksi Bertahan, Selection Limit, dan Dialog Delete Units"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-841
  - TC-AC-ACTS-842
  - TC-AC-ACTS-843
  - TC-AC-ACTS-845
coverage:
  web: automated
---

# Bulk Delete: Checkbox Header Halaman Aktif, Select All Lintas Halaman, Seleksi Bertahan, Selection Limit, dan Dialog Delete Units

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (#12). Unit uji milik spec di-seed di hook `before` (idempoten) dan dipulihkan fixture BE: 25 unit eligible, page size 10, untuk TC-AC-ACTS-841, 842, dan 843; 15 unit eligible untuk TC-AC-ACTS-845.
- State global: Selection Limit (System Limits) diatur lewat fixture BE ke 12 untuk TC-AC-ACTS-843 dan dipulihkan ke nilai awal di hook `after` serta pada langkah penghubung sebelum TC-AC-ACTS-845. Notasi `{limit}` pada Expected TC diasersi sebagai 12 dan `{n}` sebagai 25.
- Kemampuan teknis: Pembacaan dan penyetelan Selection Limit lewat fixture BE disediakan tim FE/BE; kelas e ringan (satu TC, ambang diturunkan, tanpa seeding di atas 100 baris).

## Test Steps

### TC-AC-ACTS-841: Checkbox header memilih baris halaman aktif; Select All memilih lintas halaman

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik checkbox header
3. Verifikasi checkbox header memilih 10 baris halaman aktif
4. Verifikasi Bulk Action Bar `10 TAGs selected`
5. Klik `Select All (25 records)`
6. Verifikasi Bulk Action Bar `25 TAGs selected`
7. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-ACTS-842: Seleksi bertahan saat pindah halaman, filter, sort, dan tab

8. Centang dua baris di halaman 1
9. Pindah ke halaman 2 dan centang satu baris
10. Verifikasi Bulk Action Bar tetap `3 TAGs selected` setelah pindah halaman
11. Terapkan Filter Status = Damaged/Missing
12. Urutkan kolom Registered At
13. Verifikasi Bulk Action Bar tetap `3 TAGs selected` setelah filter dan sort
14. Pindah ke Tab In Use lalu kembali ke Tab Available
15. Verifikasi Bulk Action Bar tetap `3 TAGs selected` setelah pindah tab
16. Klik icon `×` pada Bulk Action Bar
17. Verifikasi seluruh seleksi dibatalkan dan Bulk Action Bar hilang
18. Kosongkan Filter dan pulihkan urutan kolom ke default

### TC-AC-ACTS-843: Selection Limit, Select All melebihi batas di-cap dengan toast; seleksi manual diblok di batas

19. Atur Selection Limit menjadi 12 lewat fixture BE, lalu muat ulang halaman
20. Klik `Select All`
21. Verifikasi Select All memilih 12 baris pertama (Bulk Action Bar `12 TAGs selected`)
22. Verifikasi toast error `Error, only the first 12 of 25 rows were selected. Narrow your filter to include the rest.`
23. Klik icon `×` pada Bulk Action Bar untuk menghapus seleksi
24. Centang baris satu per satu sampai Bulk Action Bar menunjukkan `12 TAGs selected`
25. Arahkan kursor ke checkbox baris berikutnya
26. Verifikasi checkbox tambahan Disabled dengan tooltip `You've reached the maximum selection of 12 rows.`
27. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi
28. Pulihkan Selection Limit ke nilai awal lewat fixture BE

### TC-AC-ACTS-845: Dialog Delete Units memuat semua TAG Code terpilih; Cancel tidak mereset seleksi

29. Reset dataset: 15 unit eligible lewat fixture BE, lalu muat ulang halaman
30. Klik `Select All`, lalu pilih Bulk Action > `Delete`
31. Verifikasi dialog `Delete Units` memuat 15 bullet `• [TAG Code]` lengkap dalam container scrollable tanpa ringkasan jumlah
32. Gulir daftar bullet
33. Verifikasi baris `For more accurate results, use Delete by Scan.` lalu `This action cannot be undone. Are you sure you want to delete them?`
34. Verifikasi tombol `[Cancel]` dan `[Delete]` (danger)
35. Klik `[Cancel]`
36. Verifikasi dialog tertutup dan tidak ada unit terhapus
37. Verifikasi Bulk Action Bar tetap `15 TAGs selected`
38. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness dan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah "Reset dataset" dan pembukaan Detail SKU diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pembatalan seleksi, "Kosongkan Filter", pengaturan dan pemulihan Selection Limit lewat fixture BE, "Reset dataset", dan muat ulang halaman (pemulihan state, S-09).
- Temuan untuk QA:
  - TC-AC-ACTS-843 Precondition menyebut Selection Limit 1000 dengan lebih dari 1000 unit eligible; spec mengatur Selection Limit menjadi 12 dengan 25 unit agar `{limit}` dan `{n}` pada Expected dapat diasersi tanpa seeding di atas 1000 baris. Nilai limit pada teks toast dan tooltip dibaca dari nilai yang diatur.
  - TC-AC-ACTS-841 dan 842 memakai 25 unit eligible; Pre-setup dan Dinamis TC tidak mendaftarnya, sehingga dari seeding spec.
