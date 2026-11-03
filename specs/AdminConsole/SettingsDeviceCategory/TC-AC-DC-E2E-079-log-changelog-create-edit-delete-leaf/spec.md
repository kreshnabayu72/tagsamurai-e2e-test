---
id: TC-AC-DC-E2E-079-log-changelog-create-edit-delete-leaf
title: "Changelog Category Mencatat Tepat Satu Entri untuk Create, Edit, dan Delete Leaf"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-216
  - TC-AC-DC-217
  - TC-AC-DC-218
coverage:
  web: automated
---

# Changelog Category Mencatat Tepat Satu Entri untuk Create, Edit, dan Delete Leaf

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso; Modified By tampil `Budi S`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk tempat node milik spec; node literal Pre-setup #14 tidak diubah. Riwayat Changelog Pre-setup #17 dibaca pada langkah 15 (baris `Scanner Max`). General Settings Pre-setup #19 (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta) tidak diubah.
- Data Dinamis (suffix `{runId}-079`), dibuat lewat sesi API aktor di hook `before` sebagai leaf di bawah `Handheld Reader`: `Induk Uji {runId}-079` (induk Add TC-AC-DC-216), `Sumber Edit {runId}-079` (target Edit TC-AC-DC-217), `Daun Uji {runId}-079` (target Delete TC-AC-DC-218). Node yang dibuat spec lewat UI: `Pemindai Uji {runId}-079` (langkah 4); hasil rename: `Zebra Uji {runId}-079` (langkah 19).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API node `Induk Uji {runId}-079` (beserta anak `Pemindai Uji {runId}-079`), `Zebra Uji {runId}-079`, dan `Daun Uji {runId}-079` bila masih ada. Entri Changelog tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category sebelum dan sesudah aksi (N216, N217, N218 pada langkah 1, 17, dan 27) karena Changelog adalah audit trail permanen; jam server dan jam browser sinkron untuk asersi Date (toleransi satu menit).
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-216: Create mencatat tepat satu entri Changelog dengan nilai baru

1. Baca dan catat jumlah entri Changelog Category sebagai N216 (kemampuan baca)
2. Expand `Hardware`, lalu expand `Handheld Reader`
3. Hover node `Induk Uji {runId}-079`, lalu klik aksi `+ Subcategory`
4. Ketik "Pemindai Uji {runId}-079", lalu klik `[Submit]`
5. Tunggu aksi selesai
6. Catat waktu sesudah `[Submit]` sebagai T216
7. Klik ikon Changelog pada header Sidebar Category
8. Ketik Search `Pemindai Uji {runId}-079`, tekan Enter
9. Verifikasi jumlah entri Changelog Category bertambah tepat satu dibanding N216 (kemampuan baca)
10. Verifikasi hasil Search menampilkan tepat satu baris
11. Verifikasi baris tersebut: Action "Create", Category "Pemindai Uji {runId}-079", Field "Category", Old Value "—", New Value "Pemindai Uji {runId}-079", Modified By "Budi S"
12. Verifikasi Date baris tersebut sesuai T216 (toleransi satu menit) dalam Date Format `dd/MM/yy` dan Time Format 24 jam
13. Klik `(←)` pada kotak Search
14. Ketik Search `Scanner Max`, tekan Enter
15. Verifikasi baris lama tidak berubah: baris Action "Edit" dengan Old Value "Scanner Pro", New Value "Scanner Max", Modified By "Budi S", Date 10/09/26 12:25
16. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-217: Edit nama mencatat tepat satu entri Changelog dengan nilai lama dan baru

17. Baca dan catat jumlah entri Changelog Category sebagai N217 (kemampuan baca)
18. Hover node `Sumber Edit {runId}-079`, lalu klik aksi Edit
19. Ubah nama menjadi "Zebra Uji {runId}-079", lalu klik `[Save]`
20. Tunggu aksi selesai
21. Klik ikon Changelog pada header Sidebar Category
22. Ketik Search `Zebra Uji {runId}-079`, tekan Enter
23. Verifikasi jumlah entri Changelog Category bertambah tepat satu dibanding N217 (kemampuan baca)
24. Verifikasi hasil Search menampilkan tepat satu baris
25. Verifikasi baris tersebut: Action "Edit", Category "Zebra Uji {runId}-079" (nama sesudah perubahan), Field "Category", Old Value "Sumber Edit {runId}-079", New Value "Zebra Uji {runId}-079", Modified By "Budi S"
26. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-218: Delete leaf mencatat tepat satu entri Changelog dengan nilai lama

27. Baca dan catat jumlah entri Changelog Category sebagai N218 (kemampuan baca)
28. Hover node `Daun Uji {runId}-079`, lalu klik aksi Delete
29. Klik `[Delete]` pada dialog konfirmasi
30. Tunggu aksi selesai
31. Klik ikon Changelog pada header Sidebar Category
32. Ketik Search `Daun Uji {runId}-079`, tekan Enter
33. Verifikasi jumlah entri Changelog Category bertambah tepat satu dibanding N218 (kemampuan baca)
34. Verifikasi hasil Search menampilkan tepat satu baris dengan Action "Delete"
35. Verifikasi baris Delete tersebut: Category "Daun Uji {runId}-079", Field "Category", Old Value "Daun Uji {runId}-079", New Value "—", Modified By "Budi S"
36. Tutup modal Changelog lewat `[×]`

## Notes

- Alasan melewati 35 langkah (spec ini 36 langkah, tiga di antaranya langkah Tunggu aksi selesai): ketiga blok memakai satu surface (Changelog Category), data milik tiap blok sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 5, 20, dan 30 (Tunggu aksi selesai sesudah `[Submit]`, `[Save]`, dan `[Delete]` yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8), langkah 6 (mencatat waktu), 13, 16, 26, dan 36 (menutup modal dan mereset Search), serta Search pada langkah 8, 14, 22, dan 32 untuk menemukan baris target (R-16). Search menyaring baris berdasarkan nama bersuffix unik sehingga hasilnya tidak bergantung pada ukuran halaman audit trail.
- Pembagian TC lintas spec: asersi absence log (Save tanpa perubahan, Delete diblok, request gagal) ada di spec 083, 084, 097, dan 098 (S-05); Delete family ada di spec 080; System Log dan Activity Log ada di spec 081 dan 082.
- Temuan untuk QA:
  - TC-AC-DC-216, 217, dan 218 Expected a menulis jumlah absolut ("13 entri": halaman 1 berisi 10 baris, halaman 2 berisi 3 baris). Changelog adalah audit trail permanen yang tumbuh tiap run, sehingga angka absolut tidak dapat diasersi (S-12); spec mengasersi selisih tepat satu terhadap baseline N dan baris unik bersuffix. Langkah "klik halaman 2" TC tidak dipakai karena Search menyaring ke baris target.
  - TC-AC-DC-216 Expected c ("baris lama tidak berubah") tidak menyebut baris mana. Spec memakai satu baris literal Pre-setup #17 (`Scanner Max`) sebagai wakil; asersi ini bergantung pada nama literal itu dan pada keberadaan riwayat Pre-setup #17 di environment.
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`, `Hapus Daun`) sebagai target tulis; spec memakai node bersuffix milik spec (keputusan data tulis). Entri Create akibat seeding node itu bergantung pada apakah seeding lewat API menulis Changelog (tidak dinyatakan TC): asersi spec tidak bergantung padanya karena memakai selisih terhadap baseline dan nama unik, kecuali langkah 34 yang menghitung hanya baris Action "Delete".
