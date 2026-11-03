---
id: TC-FA-RP-E2E-138-tab-total-control-search-4
title: "Tab Total Control: Search (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-479
  - TC-FA-RP-1060
  - TC-FA-RP-1061
  - TC-FA-RP-1104
coverage:
  web: automated
---

# Tab Total Control: Search (4/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Status `Active` delapan baris dan `Inactive` Siti Rahayu; Rudi Hartono Temporary Until terisi), #37 (Tab Read Only empat baris), #22 (Custom Field `Cost Center` CC-100 Ahmad Fauzi dan CC-200 Budi Santoso, `Joined Date` 10/01/26 Ahmad Fauzi). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`. Teks tanggal sel dibaca dari layar sesuai Date Format General Settings (Pre-setup #34, tidak diubah).
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### Search kolom badge dan kolom aksi (TC 479)

1. Klik ikon Search.
2. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
3. Ketik Search `active`, tekan Enter.
4. Verifikasi `active` hanya mencocokkan baris berstatus `Active` (delapan baris), dan baris Siti Rahayu berstatus `Inactive` tidak tampil.
5. Ganti isi kotak search dengan `Remove`, tekan Enter.
6. Verifikasi tabel menampilkan empty state `No results found` karena kolom aksi tidak dapat dicari.
7. Klik `✕` pada Search, tekan Enter.

### Search kolom Custom Field Dropdown (TC 1060)

8. Tampilkan kolom Cost Center lewat Setup Column, lalu klik `[Save]`.
9. Ketik Search `cc-100`, tekan Enter.
10. Verifikasi hanya baris Ahmad Fauzi yang tampil.
11. Klik `✕` pada Search, tekan Enter.
12. Ketik Search `CC-200`, tekan Enter.
13. Verifikasi hanya baris Budi Santoso yang tampil.
14. Klik `✕` pada Search, tekan Enter.

### Search tidak mencocokkan kolom Temporary Until (TC 1061)

15. Tampilkan kolom Temporary Until lewat Setup Column, lalu klik `[Save]`.
16. Catat teks sel Temporary Until baris Rudi Hartono dari layar.
17. Ketik Search teks tanggal yang dicatat pada langkah 16, tekan Enter.
18. Verifikasi tabel menampilkan empty state `No results found` karena kolom tanggal tidak dapat dicari.
19. Klik `✕` pada Search, tekan Enter.
20. Klik ikon Filter.
21. Verifikasi Filter Panel memuat field `Temporary Until` bertipe date range picker (penyaringan kolom tanggal hanya melalui Filter Panel).
22. Klik ikon Filter untuk menutup panel.

### Search tidak mencocokkan kolom Custom Field Date Joined Date (TC 1104)

23. Tampilkan kolom Joined Date lewat Setup Column, lalu klik `[Save]`.
24. Catat teks sel Joined Date baris Ahmad Fauzi dari layar.
25. Ketik Search teks tanggal yang dicatat pada langkah 24, tekan Enter.
26. Verifikasi tabel menampilkan empty state `No results found` karena kolom Custom Field bertipe Date tidak dapat dicari.
27. Klik `✕` pada Search, tekan Enter.
28. Klik ikon Filter.
29. Verifikasi Filter Panel memuat field `Joined Date` bertipe date range picker (penyaringan kolom tanggal hanya melalui Filter Panel).
30. Klik ikon Filter untuk menutup panel.
31. Sembunyikan kolom Cost Center, Temporary Until, dan Joined Date lewat Setup Column, lalu klik `[Save]`.

## Notes

- Langkah penghubung (S-03): langkah 1, 7, 8, 11, 14, 15, 16, 19, 20, 22, 23, 24, 27, 28, 30, dan 31. Langkah 7, 11, 14, 19, dan 27 mengosongkan Search (8b butir 9); langkah 31 memulihkan kolom (S-09). Langkah 2 adalah pembanding positif asersi universal langkah 4; langkah 6, 18, dan 26 memakai empty state `No results found` sebagai anchor positif absence hasil Search.
- Temuan untuk QA:
  - TC 1061 dan TC 1104 Expected b ("penyaringan kolom tanggal hanya melalui Filter Panel") bukan keadaan yang teramati langsung; spec mengasersi keberadaan field date range picker di Filter Panel sebagai langkah observasi (langkah 20 dan 21, 28 dan 29).
  - TC 479 Expected a menyebut `active` sebagai exact match nilai badge Status; Activation Status (nilai `Activated`) tidak tampil pada tabel saat langkah itu (kolom disembunyikan secara default), sehingga tidak ada risiko cocok substring.
