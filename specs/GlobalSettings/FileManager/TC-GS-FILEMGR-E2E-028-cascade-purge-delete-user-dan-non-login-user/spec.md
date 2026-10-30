---
id: TC-GS-FILEMGR-E2E-028-cascade-purge-delete-user-dan-non-login-user
title: "Cascade Purge: Delete User dan Non-Login User Menghapus Permanen Seluruh File"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-109
  - TC-GS-FILEMGR-110
  - TC-GS-FILEMGR-241
  - TC-GS-FILEMGR-287
coverage:
  web: automated
---

# Cascade Purge: Delete User dan Non-Login User Menghapus Permanen Seluruh File

## Prerequisites

- Mode: FE+BE (kelas harness eksternal: job latar cascade purge; pemicu fixture BE).
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run; user dan Non-Login User klon milik spec, diidentifikasi lewat email bersuffix `{runId}-028`, disediakan tim FE agar user Pre-setup tidak dihapus, S-06):
  - TC-GS-FILEMGR-109 (D04): user klon `Dewi Kartika` (email `dewikartika+{runId}-028@qwertysystem.net`) dengan foto aktif `dewi-kartika-{runId}-028.jpg` dan file di Recycle Bin `due-photo-{runId}-028.png` (Deleted Date sekarang - 31 hari, Auto-Purge In `0 days`).
  - TC-GS-FILEMGR-110: user klon `Eka Putri` (email `ekaputri+{runId}-028@qwertysystem.net`) tanpa file aktif maupun file di Recycle Bin.
  - TC-GS-FILEMGR-241: Non-Login User klon `Hadi Susanto` dengan foto aktif `hadi-photo-{runId}-028.jpg` dan file di Recycle Bin `hadi-old-{runId}-028.jpg`.
  - TC-GS-FILEMGR-287: user klon kedua `Dewi Kartika` (email `dewikartika+{runId}-028b@qwertysystem.net`) dengan foto aktif `dewi-kartika-{runId}-028b.jpg` dan file di Recycle Bin `due-photo-{runId}-028b.png`; fixture BE membuat satu penghapusan storage gagal sementara pada percobaan pertama cascade purge.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): seeding user dan Non-Login User klon beserta file; fixture BE kegagalan storage sementara pada percobaan pertama cascade purge dan retry otomatis; jam server dan jam browser sinkron; membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`).
- Jeda nyata: langkah "muat ulang berkala" dilakukan dengan refresh tiap 5 detik, batas tunggu 120 detik (batas harness; TC menyebut refresh berulang tanpa angka batas, Catatan TC).
- Job auto-purge harian tidak boleh berjalan selama spec (menghapus `due-photo-*` lebih awal dari cascade purge); dijeda di environment e2e.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen sisa file seed, hapus user dan Non-Login User klon yang masih ada.
- Suite serial (`parallel: false`). Spec ini menghabisi user (cascade purge): jalankan sesudah spec lain bila runner mengikuti nomor (belum terbukti). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-110: Delete User tanpa file

1. Buka Global Settings > User, cari user klon `Eka Putri` lewat email `ekaputri+{runId}-028@qwertysystem.net`
2. Delete user `Eka Putri`, lalu konfirmasi
3. Verifikasi Delete User sukses tanpa toast error terkait File Manager
4. Buka Global Settings > File Manager, lalu ketik Search `{runId}-028`, tekan Enter
5. Verifikasi tabel utama tidak berubah (jumlah baris sama dengan baseline sebelum Delete User)
6. Klik tombol Recycle Bin di toolbar, ketik Search `{runId}-028`, tekan Enter
7. Verifikasi Recycle Bin tidak berubah (jumlah baris sama dengan baseline sebelum Delete User)
8. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-109: Delete User menghapus permanen seluruh file milik user

9. Buka Global Settings > User, cari user klon `Dewi Kartika` lewat email `dewikartika+{runId}-028@qwertysystem.net`
10. Delete user `Dewi Kartika`, lalu konfirmasi
11. Verifikasi tidak ada toast File Manager terpisah
12. Buka Global Settings > File Manager, lalu muat ulang tabel berkala sampai `dewi-kartika-{runId}-028.jpg` hilang dari tabel utama
13. Klik tombol Recycle Bin di toolbar, lalu muat ulang berkala sampai `due-photo-{runId}-028.png` hilang
14. Verifikasi `dewi-kartika-{runId}-028.jpg` hilang permanen dari tabel utama
15. Verifikasi `due-photo-{runId}-028.png` hilang permanen dari Recycle Bin
16. Tutup modal Recycle Bin dengan `✕` di header
17. Klik ikon Changelog di toolbar, ketik Search `dewi-kartika-{runId}-028`, tekan Enter
18. Verifikasi Modal Changelog tidak memuat baris untuk `dewi-kartika-{runId}-028.jpg` (empty state "No results found")
19. Ganti isi kotak search dengan `due-photo-{runId}-028`, tekan Enter
20. Verifikasi Modal Changelog tidak memuat baris untuk `due-photo-{runId}-028.png` (empty state "No results found")
21. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-241: Delete Non-Login User menghapus permanen fotonya

22. Buka Global Settings > Non-Login User, cari `Hadi Susanto` (klon milik spec)
23. Delete Non-Login User `Hadi Susanto`, lalu konfirmasi
24. Buka Global Settings > File Manager, lalu muat ulang berkala sampai `hadi-photo-{runId}-028.jpg` hilang
25. Verifikasi `hadi-photo-{runId}-028.jpg` hilang dari tabel utama
26. Klik tombol Recycle Bin di toolbar, lalu muat ulang berkala sampai `hadi-old-{runId}-028.jpg` hilang
27. Verifikasi `hadi-old-{runId}-028.jpg` hilang dari Recycle Bin tanpa menunggu retensi
28. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-287: Retry cascade purge tidak menghapus ganda

29. Buka Global Settings > User, cari user klon `Dewi Kartika` lewat email `dewikartika+{runId}-028b@qwertysystem.net`
30. Delete user `Dewi Kartika`, lalu konfirmasi
31. Biarkan retry cascade purge berjalan sampai selesai (fixture BE)
32. Buka Global Settings > File Manager dan modal Recycle Bin, lalu muat ulang berkala sampai `dewi-kartika-{runId}-028b.jpg` dan `due-photo-{runId}-028b.png` hilang
33. Verifikasi `dewi-kartika-{runId}-028b.jpg` hilang permanen (retry berlanjut sampai selesai)
34. Verifikasi `due-photo-{runId}-028b.png` hilang permanen (retry berlanjut sampai selesai)
35. Verifikasi tidak ada toast error duplikat atau not found
36. Verifikasi kedua file awal (2 file) seluruhnya terhapus
37. Tutup modal Recycle Bin dengan `✕` di header

## Notes

- Mode: FE+BE (kelas d: harness eksternal, job latar cascade purge sebagai pemicu dan sebagian objek uji, bagian 3 prinsip 13d). Subjudul `###` memetakan langkah ke id TC granular. Semua blok satu kelas; seluruh aksi menghabisi user klon sehingga dikelompokkan di spec ini.
- Spec melewati sekitar 35 langkah (37 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: semua blok satu kelas dan satu harness (cascade purge job latar) dengan user klon dan file seed milik masing-masing blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC pada spec: 110, 109, 241, 287. TC-GS-FILEMGR-110 (tanpa file) lebih dulu karena tidak mengubah dataset; TC-GS-FILEMGR-287 di akhir karena membuka fixture kegagalan storage.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 4, 6, 9, 12, 13, 17, 19, 22, 24, 26, 29, 32 (navigasi dan Search untuk menemukan target), 8, 16, 21, 28, 37 (menutup modal), 31 (menunggu retry selesai), 12, 13, 24, 26, 32 (muat ulang berkala dengan batas 120 detik).
- Asersi tambahan di luar Expected TC (S-03): langkah 18 dan 20 memakai empty state "No results found" sebagai anchor absence baris Changelog (Expected c TC-GS-FILEMGR-109); langkah 36 mengasersi bahwa kedua file awal terhapus (lihat Temuan untuk QA).
- Temuan untuk QA:
  - Q-8/Q-4: pemicu cascade purge dan kegagalan storage sementara dilakukan "fixture BE" tanpa mekanisme di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" tanpa endpoint karangan.
  - Q-5/Q-7: TC menargetkan user Pre-setup/baris Pre-setup Dewi Kartika (F04, R04), Eka Putri, dan Hadi Susanto; spec memakai klon bersuffix agar Tabel A2/A3 tidak berubah. Nama klon literal belum terdaftar sebagai pengecualian S-12.
  - TC-GS-FILEMGR-109 Post Condition butir b ("Entri log Delete User hanya memuat nama user, assertion detail di TC modul User") tidak memiliki langkah observasi di TC; tidak diasersi di spec ini.
  - TC-GS-FILEMGR-287 Expected c ("Jumlah file terhapus untuk user sama dengan jumlah file awal, tidak dihitung dua kali") tidak memiliki cara cek di TC (hitungan dihitung server). Spec hanya mengasersi bahwa kedua file awal terhapus (langkah 36); hitungan internal "tidak dihitung dua kali" tidak teramati lewat UI.
  - PRD tidak menetapkan batas atas jeda cascade purge; spec memakai batas harness 120 detik yang tidak berasal dari TC.
  - TC-GS-FILEMGR-110 Expected b ("Tabel utama dan Recycle Bin tidak berubah") tidak menyebut pembanding; spec memakai baseline jumlah baris hasil Search `{runId}-028` sebelum Delete User (dicatat di hook `before`).
