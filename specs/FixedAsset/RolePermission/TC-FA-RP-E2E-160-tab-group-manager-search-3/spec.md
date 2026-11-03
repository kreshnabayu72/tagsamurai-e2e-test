---
id: TC-FA-RP-E2E-160-tab-group-manager-search-3
title: "Tab Group Manager: Search (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1065
  - TC-FA-RP-1093
  - TC-FA-RP-1105
coverage:
  web: automated
---

# Tab Group Manager: Search (3/3)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris; lima baris `Active` dan satu baris `Inactive` Lina Marlina), #18 (pohon group), dan #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Date Format General Settings (#34) tidak diubah spec ini; teks tanggal dicatat dari sel sesuai format yang berlaku.
- State yang diubah: konfigurasi kolom Setup Column Tab Group Manager (kolom Temporary Until dan Joined Date ditampilkan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Kolom Temporary Until tidak dapat dicari (TC-FA-RP-1065)

1. Klik Tab `Group Manager`
2. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
3. Centang kolom `Temporary Until`, lalu klik `[Save]`
4. Catat teks sel Temporary Until baris Kevin Susanto
5. Ketik Search teks tanggal yang dicatat, tekan Enter
6. Verifikasi empty state `No results found` (kolom tanggal tidak dapat dicari)
7. Klik ikon Filter
8. Verifikasi Filter Panel memuat field `Temporary Until` sebagai jalur penyaringan kolom tanggal
9. Tutup Filter Panel
10. Kosongkan isi kotak search, tekan Enter

### Search Status memakai pencocokan exact (TC-FA-RP-1093)

11. Ketik Search `active`, tekan Enter
12. Verifikasi lima baris berstatus `Active` tampil
13. Verifikasi baris Lina Marlina (`Inactive`) tidak tampil
14. Kosongkan isi kotak search, tekan Enter
15. Ketik Search `inactive`, tekan Enter
16. Verifikasi hanya baris Lina Marlina yang tampil
17. Kosongkan isi kotak search, tekan Enter

### Kolom Joined Date tidak dapat dicari (TC-FA-RP-1105)

18. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
19. Centang kolom `Joined Date`, lalu klik `[Save]`
20. Catat teks sel Joined Date baris Fajar Nugroho
21. Ketik Search teks tanggal yang dicatat, tekan Enter
22. Verifikasi empty state `No results found` (kolom Custom Field bertipe Date tidak dapat dicari)
23. Klik ikon Filter
24. Verifikasi Filter Panel memuat field `Joined Date` sebagai jalur penyaringan kolom tanggal
25. Tutup Filter Panel
26. Kosongkan isi kotak search, tekan Enter

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membuka Setup Column dan menyimpan (langkah 2, 3, 18, 19); mencatat teks sel (langkah 4 dan 20); menutup Filter Panel (langkah 9 dan 25); mengosongkan Search (langkah 10, 14, 17, 26).
- Langkah 12 dan 13: baris `Active` yang tampil menjadi anchor positif bagi asersi absence baris Lina Marlina (bagian 8b butir 2).
- Temuan untuk QA:
  - TC tidak menyebut cara menutup Filter Panel tanpa `[Apply]`; spec menulis "Tutup Filter Panel" sebagai langkah penghubung.
  - TC-FA-RP-1093 Expected a menyebut "lima baris berstatus `Active`" tanpa nama baris; spec mengasersi jumlah lima baris dan ketiadaan Lina Marlina.
