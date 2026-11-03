---
id: TC-FA-RP-E2E-169-tab-group-manager-pagination-dan-state-halaman
title: "Tab Group Manager: Pagination dan state halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-563
  - TC-FA-RP-564
  - TC-FA-RP-565
  - TC-FA-RP-566
coverage:
  web: automated
---

# Tab Group Manager: Pagination dan state halaman

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Tabel Nomor halaman tidak valid (TC-FA-RP-566):

| Nilai | Jenis |
|---|---|
| `0` | nol |
| `99` | melebihi jumlah halaman |
| `abc` | teks bukan angka |

## Test Steps

### Default 10 per halaman dan pilihan ukuran (TC-FA-RP-563)

1. Klik Tab `Group Manager`
2. Verifikasi default 10 data per halaman
3. Buka Overlay Page Size
4. Verifikasi pilihan ukuran 10, 25, 50, dan 100 tanpa opsi All

### Ganti ukuran halaman dan sort (TC-FA-RP-564)

5. Verifikasi ukuran terpilih sebelum diganti: 10
6. Pilih ukuran halaman 25
7. Verifikasi info pagination menampilkan total 6 baris (Pre-setup #38) dan ukuran halaman 25
8. Verifikasi keenam baris tampil dalam satu halaman
9. Klik header kolom Group sekali (Group ascending)
10. Verifikasi urutan baris: Kevin Susanto (`Data Center`), Lina Marlina (`Head Office`), Kevin Susanto (`Helpdesk`), Cahyo Aji (`International Operations Distribution Center`), Fajar Nugroho (`IT Infrastructure`), Dimas Pranata (`Rack A1`)
11. Verifikasi total tetap 6 baris
12. Klik header kolom Group dua kali (kembali ke default sort)
13. Ganti ukuran halaman menjadi 10

### State dipertahankan saat F5, reset saat klik ulang menu (TC-FA-RP-565)

14. Ketik Search `kevin`, tekan Enter
15. Klik ikon Filter, pilih opsi `IT Operations` pada field Division, klik `[Apply]`
16. Klik header kolom Group dua kali (Group descending)
17. Ganti ukuran halaman menjadi 25
18. Muat ulang halaman (F5)
19. Verifikasi Search `kevin` tetap terpasang setelah F5
20. Verifikasi Filter Division `IT Operations` tetap terpasang setelah F5
21. Verifikasi Sort Group descending tetap setelah F5
22. Verifikasi ukuran halaman 25 tetap setelah F5
23. Verifikasi tabel menampilkan Kevin Susanto (`Helpdesk`) lalu Kevin Susanto (`Data Center`)
24. Klik menu Settings > Role & Permission di sidebar
25. Klik Tab `Group Manager`
26. Verifikasi Search kosong
27. Verifikasi tidak ada Filter yang terpasang
28. Verifikasi Sort Name A-Z
29. Verifikasi ukuran halaman 10
30. Verifikasi tabel menampilkan 6 baris (Pre-setup #38) dalam satu halaman dengan baris pertama Cahyo Aji

### Kasus tepi nomor halaman (TC-FA-RP-566)

31. Untuk setiap baris pada Tabel Nomor halaman tidak valid, lakukan langkah 32 sampai 33
32. Masukkan nomor halaman `<Nilai>` pada input nomor halaman
33. Verifikasi nomor halaman tidak valid diabaikan (halaman aktif dan isi tabel tidak berubah)

## Notes

- Langkah yang diulang: 32 sampai 33 (tiga iterasi menurut Tabel Nomor halaman tidak valid); nominal 33 langkah, ekspansi 37 langkah.
- Pilihan ukuran halaman diasersi sekali pada langkah 4 dan berlaku untuk Expected b TC-FA-RP-563 dan Expected a TC-FA-RP-564; Overlay Page Size tetap terbuka dari langkah 3 sampai langkah 6 (TC-FA-RP-564 langkah 2 membuka pilihan yang sama).
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1, 25); membuka overlay (langkah 3); mengembalikan sort dan ukuran halaman ke default (langkah 12 dan 13); klik menu sidebar (langkah 24).
- Langkah 25 mengklik Tab `Group Manager` agar asersi default berada pada tab yang sama dengan sebelum klik menu.
- Temuan untuk QA:
  - TC-FA-RP-566 Expected hanya "Nomor halaman tidak valid diabaikan" tanpa menyebut halaman aktif atau isi tabel; spec mengasersi halaman aktif dan isi tabel tidak berubah.
  - Pre-setup #38 hanya enam baris dengan ukuran halaman 10 sehingga hanya ada satu halaman; TC-FA-RP-566 tidak menyebut apakah input nomor halaman tersedia pada tabel satu halaman.
  - TC-FA-RP-565 langkah 4 (klik menu sidebar) tidak menyebut tab yang aktif sesudahnya; spec mengklik Tab `Group Manager` (langkah 25).
  - TC-FA-RP-564 dan TC-FA-RP-565 menulis "Sort Name A-Z" sebagai default tanpa menyebut bahwa kolom Name menunjukkan ikon sort ascending; spec mengasersi urutan baris.
