---
id: TC-FA-LBL-E2E-019-delete-label-bersih-sisa-relasi-aset-deleted-dan-label-terhapus-admin-lain
title: "Delete Label bersih: sisa relasi aset Deleted dibersihkan dan label sudah dihapus admin lain"
priority: Critical
caseType: Positive
status: draft
sourceRules:
  - E-FALB-24
  - F-FALB-04.k2
  - E-FALB-10
  - FALB:must-not/menghapus-aset-fisik-saat-label-dihapus-d8
  - E-FALB-12
  - F-FALB-04.k3
coverage:
  web: automated
---

# Delete Label bersih: sisa relasi aset Deleted dibersihkan dan label sudah dihapus admin lain

## Prerequisites

- Mode: FE+BE
- Akun Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec ini membersihkan sisa data milik spec.
- Data uji: `DU-43` (label seed bersih bersuffix `{runId}-019` beserta satu aset berstatus Deleted yang masih menyimpan relasi dengan label itu); `DU-44` (label seed bersuffix `{runId}-019` yang dihapus pelaku kedua lewat sesi API setelah dialog konfirmasi dibuka).
- Kemampuan teknis: sesi API aktor `DU-01` (login API password; token tidak dihitung sebagai sesi web), fixture BE untuk seeding label dan aset berstatus Deleted serta untuk membaca relasi aset dengan label dan record aset, dan kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log (semuanya disediakan tim FE/BE).
- State global: spec membuat label `DU-43` dan `DU-44` serta satu aset Deleted; hook `after` menghapus sisa aset dan label yang masih ada lewat fixture BE.

## Test Steps

### E-FALB-10: Aset berstatus Deleted tidak dihitung dan tidak tampil

1. Ketik Search `DU-43`, tekan Enter.
2. Verifikasi baris Label `DU-43` tampil dengan Total Asset 0.
3. Klik chip Label pada baris `DU-43` untuk membuka Drawer Tagged Asset.
4. Verifikasi Drawer dengan judul `Tagged Assets` tampil.
5. Verifikasi daftar Drawer tidak memuat aset: empty state menampilkan ilustrasi dengan judul `No assets tagged` dan deskripsi `No assets are assigned this label yet.`.
6. Klik `[✕]` pada Drawer `Tagged Assets`.

### F-FALB-04.k2: Label bersih dapat dihapus

7. Klik `[⋯]` pada baris Label `DU-43`, pilih `Delete`.
8. Verifikasi dialog dengan judul `Delete Label` tampil (dialog konfirmasi, bukan dialog blokir).

### E-FALB-24: Delete label bersih menghapus label beserta sisa relasi pada aset Deleted

9. Verifikasi dialog `Delete Label` memuat nama label `DU-43`, teks `Are you sure you want to delete it? This action cannot be undone.`, serta tombol `[Cancel]` dan `[Delete]`.
10. Klik `[Delete]`.
11. Verifikasi toast `Success, label has been deleted.` tampil.
12. Verifikasi baris Label `DU-43` tidak tampil lagi di tabel Labels List.
13. Verifikasi lewat fixture BE relasi aset berstatus Deleted dengan label `DU-43` sudah dibersihkan.
14. Klik icon Changelog.
15. Ketik Search `DU-43` pada modal Changelog: Labels, tekan Enter.
16. Verifikasi modal Changelog: Labels memuat tepat satu baris Action `Delete` untuk label `DU-43`.
17. Klik `[✕]` pada modal Changelog: Labels.

### FALB:must-not/menghapus-aset-fisik-saat-label-dihapus-d8: Aset fisik tidak terhapus saat label dihapus

18. Verifikasi lewat fixture BE record aset berstatus Deleted milik `DU-43` masih ada (aset tidak terhapus).

### E-FALB-12: Hapus label yang sudah dihapus admin lain

19. Ganti isi kotak search dengan `DU-44`, tekan Enter.
20. Klik `[⋯]` pada baris Label `DU-44`, pilih `Delete`.
21. Verifikasi dialog dengan judul `Delete Label` dan nama label `DU-44` tampil.
22. Pelaku kedua (sesi API `DU-01`) menghapus label `DU-44` hingga penghapusan tersimpan.
23. Tunggu aksi selesai.
24. Catat baseline jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE.
25. Klik `[Delete]`.
26. Verifikasi toast `This label is no longer available.` tampil.
27. Verifikasi dialog `Delete Label` tertutup.
28. Verifikasi baris Label `DU-44` tidak tampil lagi di tabel Labels List (tabel disegarkan).
29. Verifikasi lewat kemampuan baca BE tidak ada entri log baru: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 24 sama dengan 0.

### F-FALB-04.k3: Label sudah dihapus pengguna lain

30. Verifikasi lewat fixture BE label `DU-44` tidak ada di katalog (sudah dihapus pelaku kedua).

## Notes

- Klausa `E-FALB-10` "sisa relasi penempelan pada aset itu dibersihkan bersama Delete label bersih" memerlukan aksi Delete yang sama dengan `E-FALB-24`, sehingga diasersi pada langkah 13 di bawah `E-FALB-24`.
- Urutan blok: Delete label bersih lebih dulu (langkah 7 sampai 17), lalu aset Deleted tetap dicek (langkah 18), lalu blok label yang dihapus admin lain di akhir (langkah 19 sampai 30), sesuai aturan aksi yang menghapus data di akhir.
- Langkah penghubung (S-03): langkah 1 dan 19 (Search untuk menemukan baris target, R-16, dan Search diganti isinya karena kotak sudah berisi), 3 dan 6 (membuka dan menutup Drawer), 14, 15, dan 17 (membuka, mencari, dan menutup modal Changelog), 23 (menunggu aksi pelaku kedua selesai sebelum aktor berpindah), dan 24 (baseline log dicatat sesudah penghapusan pelaku kedua supaya entri Delete pelaku kedua tidak terhitung, S-12).
- Anchor positif (S-03): langkah 4 dan 5 (Drawer dengan judul dan empty state) membuktikan Drawer termuat sebelum aset Deleted dinyatakan tidak tampil; langkah 11 (toast sukses) menjadi anchor `Verifikasi` baris hilang pada langkah 12, dan langkah 26 (toast) menjadi anchor `Verifikasi` baris hilang pada langkah 28.
- Entri Delete pada langkah 16 dibaca dengan Search nama label bersuffix unik (baseline nol untuk entri Delete); entri Create hasil seeding label ada di hasil yang sama dan tidak diasersi.
- Klausa di luar E2E: E-FALB-12 (server merespons data tidak ditemukan): respons server tidak teramati terpisah dari toast `This label is no longer available.` yang diasersi pada langkah 26.
