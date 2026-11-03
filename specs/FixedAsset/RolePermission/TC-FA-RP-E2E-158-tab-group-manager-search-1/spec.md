---
id: TC-FA-RP-E2E-158-tab-group-manager-search-1
title: "Tab Group Manager: Search (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-539
  - TC-FA-RP-540
  - TC-FA-RP-541
coverage:
  web: automated
---

# Tab Group Manager: Search (1/3)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Tabel Search per kelas teks (TC-FA-RP-540):

| Kolom | Keyword | Baris yang tampil |
|---|---|---|
| Name | `FAJAR` | hanya Fajar Nugroho |
| Group | `data cen` | hanya Kevin Susanto di `Data Center` |
| Position | `network` | kedua baris Kevin Susanto (`Data Center` dan `Helpdesk`) |
| Division | `general` | hanya Fajar Nugroho |
| Modified By | `admin u` | Lina Marlina dan Cahyo Aji (Modified By `Admin U`) |

## Test Steps

### Siklus interaksi Search toolbar (TC-FA-RP-539)

1. Klik Tab `Group Manager`
2. Hover ikon Search di toolbar
3. Verifikasi tooltip `Search`
4. Klik ikon Search
5. Verifikasi kotak Search melebar dan kursor otomatis fokus di input
6. Verifikasi placeholder input `Search name, group, position...`
7. Ketik `fajar` tanpa menekan Enter
8. Verifikasi ikon `(✕)` muncul di dalam input
9. Verifikasi tabel belum tersaring (keenam baris Pre-setup #38 tetap tampil)
10. Tekan Enter
11. Verifikasi tabel tersaring: hanya baris Fajar Nugroho
12. Klik ikon `(✕)` pada kotak Search
13. Verifikasi teks input terhapus
14. Verifikasi kotak Search tetap terbuka dan kursor tetap fokus
15. Verifikasi tabel tetap menampilkan hasil pencarian terakhir
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali menampilkan seluruh data
18. Ketik Search `fajar`, tekan Enter
19. Klik ikon `(←)`
20. Verifikasi kotak Search menutup
21. Verifikasi keyword dikosongkan
22. Verifikasi tabel langsung kembali ke seluruh data

### Search per kelas teks: substring dan tidak case-sensitive (TC-FA-RP-540)

23. Untuk setiap baris pada Tabel Search per kelas teks, lakukan langkah 24 sampai 26
24. Ketik Search `<Keyword>`, tekan Enter
25. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel
26. Kosongkan isi kotak search, tekan Enter

### Search per kelas badge dan enum (TC-FA-RP-541)

27. Ketik Search `inactive`, tekan Enter
28. Verifikasi kolom Status: hanya baris Lina Marlina yang tampil
29. Kosongkan isi kotak search, tekan Enter

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 24 sampai 26 adalah blok berulang dengan parameter pada Tabel Search per kelas teks (lima iterasi); nominal 29 langkah, ekspansi 41. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #38), dan tiap iterasi berdiri sendiri karena Search dikosongkan di akhir iterasi. Langkah yang diulang: 24 sampai 26.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik Tab `Group Manager` dan hover ikon Search (langkah 1, 2, 4); mengosongkan Search (langkah 26 dan 29); langkah 18 membangun state hasil pencarian sebelum `(←)`.
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-539 Expected g ("keyword dikosongkan") tidak menyebut cara mengamati keyword pada kotak Search yang sudah menutup; spec mengasersi bahwa kotak yang tertutup tidak lagi memuat `fajar` (langkah 21).
  - TC-FA-RP-540 Expected c (kolom Position `network`) dan e (Modified By `admin u`) menyebut hasil dua baris tanpa urutan; spec mengasersi himpunan baris tanpa urutan.
