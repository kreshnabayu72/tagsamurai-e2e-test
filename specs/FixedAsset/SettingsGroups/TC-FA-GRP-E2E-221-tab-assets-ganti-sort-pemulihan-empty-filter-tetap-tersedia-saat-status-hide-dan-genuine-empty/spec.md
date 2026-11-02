---
id: TC-FA-GRP-E2E-221-tab-assets-ganti-sort-pemulihan-empty-filter-tetap-tersedia-saat-status-hide-dan-genuine-empty
title: "Tab Assets: Ganti Target Sort, Pemulihan dari Empty State, Filter Tetap Berlaku Saat Kolom Status Di-Hide, dan Genuine Empty State Node Tanpa Aset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-702
  - TC-FA-GRP-703
  - TC-FA-GRP-1121
  - TC-FA-GRP-1129
coverage:
  web: automated
---

# Tab Assets: Ganti Target Sort, Pemulihan dari Empty State, Filter Tetap Berlaku Saat Kolom Status Di-Hide, dan Genuine Empty State Node Tanpa Aset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Data Pre-setup tambahan: Branch Office (Tabel A No 9, Assignable, tanpa aset aktif; hanya dibaca).
- Keyword Search Fixture.settingsGroups.searchKeywordKombinasi, Filter Status Fixture.settingsGroups.statusA dan Fixture.settingsGroups.statusB, serta keyword yang tidak beririsan (Fixture.settingsGroups.searchTanpaIrisan dengan Status Fixture.settingsGroups.statusA) yang menghasilkan 0 baris. Kolom sort A = Name, kolom sort B = Asset ID.
- Kemampuan teknis: pemeriksaan berkas CSV terunduh (baris header dan jumlah baris data).
- Preferensi kolom Setup Column: spec ini tidak menyimpan konfigurasi kolom; tampilan kolom yang diubah lewat Column Visibility bersifat sesi dan dipulihkan di langkah penghubung. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-GRP-702: Ganti target sort saat Search dan Filter aktif

1. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
2. Ketik Search `Fixture.settingsGroups.searchKeywordKombinasi`, tekan Enter
3. Klik icon Filter, pilih `Fixture.settingsGroups.statusA` pada Status, klik [Apply]
4. Klik header Name satu kali
5. Klik header Asset ID
6. Verifikasi sort berpindah ke kolom Asset ID (Ascending)
7. Verifikasi kolom Name kembali netral
8. Verifikasi sedikitnya satu baris tampil
9. Verifikasi setiap baris yang tampil memenuhi Search dan Filter

### TC-FA-GRP-703: Pemulihan dari empty state hasil Search + Filter

10. Klik header Asset ID dua kali sampai netral, klik `(←)` pada kotak Search, klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
11. Ketik Search `Fixture.settingsGroups.searchTanpaIrisan`, tekan Enter
12. Klik icon Filter, pilih `Fixture.settingsGroups.statusA` pada Status, klik [Apply]
13. Verifikasi empty state title "No results found", body "Try adjusting your search or filter."
14. Klik icon Filter, klik [Clear Field], klik [Apply]
15. Verifikasi sedikitnya satu baris tampil
16. Verifikasi setiap baris yang tampil cocok dengan keyword Search `Fixture.settingsGroups.searchTanpaIrisan`

### TC-FA-GRP-1121: Filter tetap berlaku saat kolom Status di-hide

17. Klik `(←)` pada kotak Search (langkah penghubung)
18. Klik icon Filter, pilih `Fixture.settingsGroups.statusB` pada Status, klik [Apply]
19. Verifikasi sedikitnya satu baris tampil
20. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusB`
21. Sembunyikan kolom Status lewat Column Visibility
22. Verifikasi baris yang tampil sama dengan sebelum kolom Status di-hide (filter tetap berlaku)
23. Klik icon Filter
24. Verifikasi Filter Panel memuat field Status
25. Tampilkan kembali kolom Status lewat Column Visibility
26. Verifikasi hasil dan nilai filter Status tidak berubah
27. Klik [Clear Field], klik [Apply] (langkah penghubung)

### TC-FA-GRP-1129: Genuine empty state node tanpa aset

28. Tutup Popup Detail Group Warehouse A, klik angka Total Asset Branch Office untuk membuka Detail Branch Office (Tab Assets)
29. Verifikasi Illustration, title "No assets assigned", body "No assets are currently assigned to this group."
30. Verifikasi icon Search, Filter, dan Download tampil
31. Klik Download, pilih Download as CSV
32. Verifikasi tidak ada toast
33. Verifikasi berkas CSV terunduh
34. Verifikasi berkas CSV hanya berisi baris header kolom yang visible
35. Verifikasi berkas CSV tidak berisi baris data
36. Klik icon Filter, buka dropdown Status
37. Verifikasi dropdown Status menampilkan teks "No options available"

## Notes

- Langkah penghubung (S-03): langkah 1 membuka Popup Detail Group Tab Assets; langkah pembuka TC-703 dan TC-1121 serta langkah penutup TC-1121 mengosongkan Search, Sort, dan Filter antar-TC (S-09); langkah penutup popup Warehouse A dan pembuka Branch Office berpindah node, sehingga blok TC-1129 ditaruh terakhir.
- Jumlah langkah (37) di atas smell 35 langkah; alasan: semua blok satu kelas harness (fungsional Tab Assets) dan satu dataset Warehouse A, tiap blok berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence toast TC-1129 diletakkan segera setelah klik pemicu dan sebelum asersi berkas (8b butir 11); berkas terunduh menjadi anchor positif bahwa respons diproses.
- Temuan untuk QA:
  - TC-703: precondition "Search K dan filter yang tidak beririsan" tidak menyebut nilai; spec memakai fixture. Expected b "tabel pulih menampilkan data yang cocok" diasersi sebagai baris yang cocok keyword Search.
  - TC-1129: unduhan CSV dibaca header dan jumlah baris data sebagai asersi fungsional; isi sel bukan objek uji.
