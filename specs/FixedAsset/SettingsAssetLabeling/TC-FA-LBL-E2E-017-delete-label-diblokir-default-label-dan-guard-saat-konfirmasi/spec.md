---
id: TC-FA-LBL-E2E-017-delete-label-diblokir-default-label-dan-guard-saat-konfirmasi
title: "Delete Label: diblokir Default Label dan guard dicek ulang saat konfirmasi"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-03
  - F-FALB-04.k1
  - F-FALB-10.k2
  - E-FALB-14
  - F-FALB-04.k4
  - FALB:must-not/menghapus-label-yang-sedang-dipakai-aset-fisik-atau-dija
  - FALB:must-not/melepas-penempelan-aset-atau-membersihkan-daftar-default
coverage:
  web: automated
---

# Delete Label: diblokir Default Label dan guard dicek ulang saat konfirmasi

## Prerequisites

- Mode: FE+BE
- Akun Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec ini membersihkan data milik spec.
- Data uji: `DU-40` (label seed yang dijadikan Default Label oleh 3 Asset Name bersuffix `{runId}-017`); `DU-41` (label guard seed bersih bersuffix `{runId}-017`, yang menjadi dipakai antara pembukaan dialog dan konfirmasi karena aset dilabeli lewat sesi API setelah dialog konfirmasi dibuka); `DU-55` (label hapus-dulu seed bersih bersuffix `{runId}-017`, yang dihapus lewat sesi API sebelum penempelan dikirim); `DU-26` (satu aset Active bersuffix `{runId}-017`, target penempelan label guard `DU-41` dan label hapus-dulu `DU-55`).
- Kemampuan teknis: sesi API aktor `DU-01` (login API password; token tidak dihitung sebagai sesi web), klien HTTP untuk permintaan langsung ke API `asset/` (attach label), fixture BE untuk seeding label, Asset Name, dan aset serta untuk membaca label, daftar Default Label tiap Asset Name, dan relasi aset dengan label, dan kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log (semuanya disediakan tim FE/BE).
- State global: spec membuat label `DU-40`, label guard `DU-41`, label hapus-dulu `DU-55`, tiga Asset Name, dan aset `DU-26`; hook `after` melepas relasi dan mengeluarkan label dari daftar Default Label lewat fixture BE lalu menghapus seluruh data seed itu.

## Test Steps

### E-FALB-03: Delete label yang menjadi Default Label pada 3 Asset Name diblokir

1. Ketik Search `DU-40`, tekan Enter.
2. Catat baseline jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE.
3. Klik `[⋯]` pada baris Label `DU-40`, pilih `Delete`.
4. Verifikasi dialog dengan judul `Cannot Delete Label`, nama label `DU-40`, teks `This label is used as Default Label by 3 asset names.`, teks `Remove it from those assets and Default Label lists before deleting it.`, dan tombol `[OK]` tampil.
5. Klik `[OK]`.
6. Verifikasi lewat fixture BE label `DU-40` masih tersimpan dengan nama dan warna semula (tidak ada mutasi).
7. Verifikasi lewat fixture BE daftar Default Label ketiga Asset Name masih memuat label `DU-40` (tidak berubah).
8. Verifikasi lewat kemampuan baca BE tidak ada entri log baru: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 2 sama dengan 0.

### F-FALB-04.k1: Label yang dijadikan Default Label diblokir

9. Verifikasi dialog `Cannot Delete Label` tertutup dan baris Label `DU-40` masih tampil di tabel Labels List.

### F-FALB-10.k2: Penolakan guard menulis nol entri log

10. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog sama dengan 0, selisih jumlah entri System Log sama dengan 0, dan selisih jumlah entri Activity Log sama dengan 0 terhadap baseline langkah 2.

### E-FALB-14: Guard dicek ulang saat Delete dikonfirmasi

11. Pelaku kedua (sesi API `DU-01`) menghapus label hapus-dulu `DU-55` hingga label terhapus
12. Kirim permintaan attach manual label hapus-dulu `DU-55` ke aset `DU-26` lewat klien HTTP
13. Verifikasi respons permintaan attach ditolak server karena label tidak ditemukan
14. Baca label hapus-dulu `DU-55` dan relasi aset `DU-26` lewat fixture BE
15. Verifikasi label hapus-dulu `DU-55` tidak ada di katalog dan aset `DU-26` tidak memiliki relasi baru dengan label itu
16. Ganti isi kotak search dengan label guard `DU-41`, tekan Enter.
17. Klik `[⋯]` pada baris label guard `DU-41`, pilih `Delete`.
18. Verifikasi dialog dengan judul `Delete Label`, nama label guard `DU-41`, teks `Are you sure you want to delete it? This action cannot be undone.`, serta tombol `[Cancel]` dan `[Delete]` tampil.
19. Pelaku kedua (sesi API `DU-01`) menempelkan label guard `DU-41` ke aset `DU-26` hingga relasi tersimpan.
20. Tunggu aksi selesai.
21. Catat baseline jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE.
22. Klik `[Delete]`.
23. Verifikasi dialog dengan judul `Cannot Delete Label` tampil menggantikan dialog konfirmasi.
24. Verifikasi dialog dengan judul `Delete Label` tidak tampil lagi.
25. Verifikasi lewat fixture BE label guard `DU-41` masih tersimpan (tidak ada mutasi).
26. Verifikasi lewat kemampuan baca BE tidak ada entri log baru: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 21 sama dengan 0.

### F-FALB-04.k4: Label menjadi dipakai antara pembukaan dialog dan konfirmasi

27. Verifikasi dialog `Cannot Delete Label` memuat nama label guard `DU-41` dan teks `This label is assigned to 1 asset.` (hitungan terbaru).
28. Klik `[OK]`.

### FALB:must-not/menghapus-label-yang-sedang-dipakai-aset-fisik-atau-dija: Label yang dipakai tidak terhapus

29. Verifikasi lewat fixture BE label `DU-40` dan label guard `DU-41` masih ada di katalog.

### FALB:must-not/melepas-penempelan-aset-atau-membersihkan-daftar-default: Penempelan dan daftar Default Label tidak dibersihkan otomatis

30. Verifikasi lewat fixture BE daftar Default Label ketiga Asset Name masih memuat label `DU-40` dan relasi aset `DU-26` dengan label guard `DU-41` masih ada.

## Notes

- Pengecualian P-1 (state berat): klausa absence log milik `F-FALB-10.k2` (langkah 8, 10, dan 26) diasersi di spec ini karena konteksnya bergantung pada state yang baru dibangun: tiga Asset Name berlabel Default dan penempelan oleh pelaku kedua setelah dialog konfirmasi dibuka. `F-FALB-10.k2` juga dikutip spec 014 dan 025 (state tenant), 015 dan 027 (batas katalog), dan 018 (label dipakai 500 aset).
- Pembagian klausa lintas spec: `F-FALB-04.k1` dikutip spec ini dan spec 018; spec ini mengasersi kasus label yang dijadikan Default Label (`E-FALB-03`), spec 018 kasus label yang dipakai 500 aset (`E-FALB-02`).
- Langkah penghubung (S-03): langkah 1 dan 16 (Search untuk menemukan baris target, R-16, dan Search diganti isinya karena kotak sudah berisi), 5 dan 28 (menutup dialog blokir), 20 (menunggu aksi pelaku kedua selesai sebelum aktor berpindah), dan 2 serta 21 (baseline log, S-12).
- Pembagian klausa lintas spec: `FALB:must-not/menghapus-label-yang-sedang-dipakai-aset-fisik-atau-dija` dikutip spec ini dan spec 020; spec ini mengasersi jalur single (blokir `Cannot Delete Label`, label tetap ada), spec 020 mengasersi jalur bulk (label yang dipakai dilewati dan tetap ada).
- Cabang `E-FALB-14` Delete commit lebih dulu diamati lewat klien HTTP dan fixture BE pada langkah 11 sampai 15 (hapus label dulu lewat sesi API, lalu kirim attach); hanya respons server dan state data yang diasersi (konvensi bagian 8b butir 1), label hapus-dulu tidak menjadi bagian UI spec ini.
- Pengecualian P-5 butir (b): langkah 11 sampai 15 adalah satu blok objek-uji ringan kelas a (request langsung tanpa harness eksternal dan tanpa state berat sendiri) yang berada di spec delete label. Sesuai bagian 8b butir 1, hanya respons server dan state data (fixture BE) yang diasersi; dialog tidak diasersi pada request langsung.
- Klausa di luar E2E: E-FALB-14 (tidak ada state antara yang menyisakan rujukan ke label terhapus): keadaan antara di dalam transaksi server tidak teramati dari luar; yang teramati hanya akibatnya: label guard tetap tersimpan (langkah 25) dan tidak ada relasi baru ke label yang terhapus (langkah 15).
- Temuan PRD: pesan dan tampilan penolakan penempelan di UI `asset/` pada cabang Delete commit lebih dulu (`E-FALB-14`) dimiliki PRD `asset/` dan tidak diatur di PRD ini, sehingga tidak diasersi.
