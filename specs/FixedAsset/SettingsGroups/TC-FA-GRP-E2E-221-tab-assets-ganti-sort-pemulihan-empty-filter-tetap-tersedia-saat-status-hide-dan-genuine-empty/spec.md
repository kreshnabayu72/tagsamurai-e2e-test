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

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
3. Ketik Search `Fixture.settingsGroups.searchKeywordKombinasi`, tekan Enter
4. Klik icon Filter, pilih `Fixture.settingsGroups.statusA` pada Status, klik [Apply]
5. Klik header Name satu kali
6. Klik header Asset ID
7. Verifikasi sort berpindah ke kolom Asset ID (Ascending)
8. Verifikasi kolom Name kembali netral
9. Verifikasi sedikitnya satu baris tampil
10. Verifikasi setiap baris yang tampil memenuhi Search dan Filter

### TC-FA-GRP-703: Pemulihan dari empty state hasil Search + Filter

11. Klik header Asset ID dua kali sampai netral, klik `(←)` pada kotak Search, klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
12. Ketik Search `Fixture.settingsGroups.searchTanpaIrisan`, tekan Enter
13. Klik icon Filter, pilih `Fixture.settingsGroups.statusA` pada Status, klik [Apply]
14. Verifikasi empty state title "No results found", body "Try adjusting your search or filter."
15. Klik icon Filter, klik [Clear Field], klik [Apply]
16. Verifikasi sedikitnya satu baris tampil
17. Verifikasi setiap baris yang tampil cocok dengan keyword Search `Fixture.settingsGroups.searchTanpaIrisan`

### TC-FA-GRP-1121: Filter tetap berlaku saat kolom Status di-hide

18. Klik `(←)` pada kotak Search (langkah penghubung)
19. Klik icon Filter, pilih `Fixture.settingsGroups.statusB` pada Status, klik [Apply]
20. Verifikasi sedikitnya satu baris tampil
21. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusB`
22. Catat baris yang tampil (jumlah baris dan nilai Name) sebelum kolom Status di-hide
23. Sembunyikan kolom Status lewat Column Visibility
24. Verifikasi baris yang tampil sama dengan catatan sebelum kolom Status di-hide (filter tetap berlaku)
25. Klik icon Filter
26. Verifikasi Filter Panel memuat field Status
27. Tampilkan kembali kolom Status lewat Column Visibility
28. Verifikasi baris yang tampil sama dengan catatan sebelum kolom Status di-hide
29. Verifikasi nilai filter Status tetap `Fixture.settingsGroups.statusB`
30. Klik [Clear Field], klik [Apply] (langkah penghubung)

### TC-FA-GRP-1129: Genuine empty state node tanpa aset

31. Tutup Popup Detail Group Warehouse A
32. Kosongkan Search dengan klik `✕`, lalu ketik Search `Branch Office`, tekan Enter
33. Klik angka Total Asset Branch Office untuk membuka Detail Branch Office (Tab Assets)
34. Verifikasi Illustration, title "No assets assigned", body "No assets are currently assigned to this group."
35. Verifikasi icon Search, Filter, dan Download tampil
36. Klik Download, pilih Download as CSV
37. Verifikasi tidak ada toast
38. Verifikasi berkas CSV terunduh
39. Verifikasi berkas CSV hanya berisi baris header kolom yang visible
40. Verifikasi berkas CSV tidak berisi baris data
41. Klik icon Filter, buka dropdown Status
42. Verifikasi dropdown Status menampilkan teks "No options available"

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets; langkah pembuka TC-703 dan TC-1121 serta langkah penutup TC-1121 mengosongkan Search, Sort, dan Filter antar-TC (S-09); langkah penutup popup Warehouse A dan pembuka Branch Office berpindah node, sehingga blok TC-1129 ditaruh terakhir.
- Jumlah langkah (42) di atas smell 35 langkah; alasan: semua blok satu kelas harness (fungsional Tab Assets) dan satu dataset Warehouse A, tiap blok berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence toast TC-1129 diletakkan segera setelah klik pemicu dan sebelum asersi berkas (8b butir 11); berkas terunduh menjadi anchor positif bahwa respons diproses.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-703: precondition "Search K dan filter yang tidak beririsan" tidak menyebut nilai; spec memakai fixture. Expected b "tabel pulih menampilkan data yang cocok" diasersi sebagai baris yang cocok keyword Search.
  - TC-1129: unduhan CSV dibaca header dan jumlah baris data sebagai asersi fungsional; isi sel bukan objek uji.
