---
id: TC-AC-DC-E2E-097-log-absence-node-lain-tidak-terlibat
title: "Absence Log: Aksi pada Satu Node Tidak Menghasilkan Entri untuk Node Lain"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-230
coverage:
  web: automated
---

# Absence Log: Aksi pada Satu Node Tidak Menghasilkan Entri untuk Node Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso; Modified By tampil `Budi S`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah. Node literal Pre-setup #14 `Barcode Handheld` dan `Hapus Daun` hanya dibaca pada langkah 16 sampai 19 (nama literal dipakai oleh asersi absence TC).
- Data Dinamis (suffix `{runId}-097`), dibuat lewat sesi API aktor di hook `before` di bawah `Handheld Reader`: `Edit Uji {runId}-097` (leaf, target Edit langkah 3, direname menjadi `Zebra Bersih {runId}-097`); family `Keluarga Absen {runId}-097` dengan anak `Anak A Keluarga Absen {runId}-097` (leaf) dan `Anak B Keluarga Absen {runId}-097` yang memiliki anak `Cucu Keluarga Absen {runId}-097` (target Delete langkah 5); `Saudara Uji {runId}-097` (leaf sibling yang tidak disentuh aksi).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Zebra Bersih {runId}-097` dan `Saudara Uji {runId}-097` bila masih ada. Entri Changelog tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category sebelum aksi (B230, langkah 1) karena Changelog adalah audit trail permanen (S-12).
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-230: Aksi pada satu node tidak menghasilkan entri untuk node lain yang tidak terlibat

1. Baca dan catat jumlah entri Changelog Category sebagai B230 (kemampuan baca)
2. Expand `Hardware`, lalu expand `Handheld Reader`
3. Hover node `Edit Uji {runId}-097`, lalu klik aksi Edit
4. Ubah nama menjadi "Zebra Bersih {runId}-097", lalu klik `[Save]`
5. Hover node `Keluarga Absen {runId}-097`, lalu klik aksi Delete
6. Klik `[Delete]` pada dialog konfirmasi
7. Tunggu aksi selesai
8. Klik ikon Changelog pada header Sidebar Category
9. Verifikasi jumlah entri Changelog Category bertambah tepat lima dibanding B230 (kemampuan baca)
10. Ketik Search `Zebra Bersih {runId}-097`, tekan Enter
11. Verifikasi hasil Search memuat satu entri Edit dengan New Value "Zebra Bersih {runId}-097"
12. Ganti isi kotak search dengan `Keluarga Absen {runId}-097`, tekan Enter
13. Verifikasi hasil Search memuat empat entri Delete, satu per node family: `Keluarga Absen {runId}-097`, `Anak A Keluarga Absen {runId}-097`, `Anak B Keluarga Absen {runId}-097`, `Cucu Keluarga Absen {runId}-097`
14. Ganti isi kotak search dengan `Saudara Uji {runId}-097`, tekan Enter
15. Verifikasi tidak ada baris dengan Action "Edit" atau "Delete" untuk `Saudara Uji {runId}-097`
16. Ganti isi kotak search dengan `Barcode Handheld`, tekan Enter
17. Verifikasi tidak ada baris dengan Action "Edit" atau "Delete" untuk `Barcode Handheld`
18. Ganti isi kotak search dengan `Hapus Daun`, tekan Enter
19. Verifikasi tidak ada baris dengan Action "Edit" atau "Delete" untuk `Hapus Daun`
20. Tutup modal Changelog lewat `[×]`

## Notes

- P-5 (a): spec ini spec absence (kelas g) untuk asersi Expected b TC-AC-DC-230; Expected a (lima entri) adalah asersi presence yang menjadi anchor positif untuk asersi absence pada surface yang sama (bagian 8b butir 2): langkah 9, 11, dan 13 membuktikan Changelog termuat dan entri aksi ini tampil sebelum langkah 15, 17, dan 19.
- Langkah penghubung (S-03): langkah 7 (Tunggu aksi selesai sesudah `[Delete]` pada langkah 6 yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8), langkah 20 (menutup modal), dan Search pada langkah 10, 12, 14, 16, dan 18 untuk menemukan baris target (R-16). Search menyaring ke nama unik bersuffix sehingga hasilnya tidak bergantung pada ukuran halaman audit trail.
- Pembagian TC lintas spec: Delete family dengan urutan pre-order ada di spec 080; absence log lain di spec 083, 084, dan 098; presence log di spec 079 sampai 082 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-230 Expected a menulis "total 17 entri; halaman 1 memuat 10 entri terbaru". Karena audit trail permanen, spec mengasersi selisih tepat lima terhadap B230 (S-12, S-14), bukan angka absolut atau isi halaman 1.
  - Asersi absence untuk `Barcode Handheld` dan `Hapus Daun` (langkah 16 sampai 19) bergantung pada nama literal Pre-setup #14 dan pada kondisi bahwa node itu tidak pernah diubah atau dihapus di environment. Catatan Pre-setup TC menyebut automation baseline memulihkan node destruktif (mis. `Hapus Daun`) dan pemulihan itu dapat meninggalkan entri Edit atau Delete lama; bila ada, langkah 17 dan 19 gagal tanpa kaitan dengan aksi spec ini. Spec menambah `Saudara Uji {runId}-097` (node sibling milik spec) agar asersi absence tetap bermakna.
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`, `Hapus Keluarga`) sebagai target; spec memakai node bersuffix milik spec (keputusan data tulis).
