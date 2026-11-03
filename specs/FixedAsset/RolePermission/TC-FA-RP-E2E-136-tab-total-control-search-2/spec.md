---
id: TC-FA-RP-E2E-136-tab-total-control-search-2
title: "Tab Total Control: Search (2/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-472
  - TC-FA-RP-473
coverage:
  web: automated
---

# Tab Total Control: Search (2/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris dengan Position, Division, Status, Activation Status, Modified By, TAG, dan Custom Field `Badge No`) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`. Nilai kolom bernilai-banyak (dua nilai distinct atau lebih) tersedia pada kolom Position, Division, Modified By, dan Status.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### Search per kelas teks (TC 472)

1. Klik ikon Search.
2. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
3. Ketik Search `rina`, tekan Enter.
4. Verifikasi kolom Name: hanya baris Rina Wulandari yang tampil.
5. Klik `✕` pada Search, tekan Enter.
6. Ketik Search `CUSTOD`, tekan Enter.
7. Verifikasi kolom Position: hanya baris Ahmad Fauzi yang tampil (Asset Custodian).
8. Klik `✕` pada Search, tekan Enter.
9. Ketik Search `logis`, tekan Enter.
10. Verifikasi kolom Division: baris Ahmad Fauzi dan Budi Santoso tampil.
11. Klik `✕` pada Search, tekan Enter.
12. Ketik Search `prasetyo`, tekan Enter.
13. Verifikasi kolom Modified By: baris Budi Santoso dan Fitri Handayani tampil (Modified By `Prasetyo H`).
14. Klik `✕` pada Search, tekan Enter.
15. Tampilkan kolom Email lewat Setup Column, lalu klik `[Save]`.
16. Ketik Search `rudihartono`, tekan Enter.
17. Verifikasi kolom Email: hanya baris Rudi Hartono yang tampil.
18. Klik `✕` pada Search, tekan Enter.
19. Tampilkan kolom TAG lewat Setup Column, lalu klik `[Save]`.
20. Ketik Search `tag-1001`, tekan Enter.
21. Verifikasi kolom TAG: hanya baris Ahmad Fauzi yang tampil.
22. Klik `✕` pada Search, tekan Enter.
23. Tampilkan kolom Badge No lewat Setup Column, lalu klik `[Save]`.
24. Ketik Search `bn-77`, tekan Enter.
25. Verifikasi kolom Badge No (Custom Field Text): hanya baris Ahmad Fauzi yang tampil.
26. Klik `✕` pada Search, tekan Enter.

### Search per kelas badge dan enum (TC 473)

27. Ketik Search `inactive`, tekan Enter.
28. Verifikasi kolom Status: hanya baris Siti Rahayu yang tampil.
29. Klik `✕` pada Search, tekan Enter.
30. Tampilkan kolom Activation Status lewat Setup Column, lalu klik `[Save]`.
31. Ketik Search `pending activation`, tekan Enter.
32. Verifikasi kolom Activation Status: hanya baris Eka Saputra yang tampil.
33. Klik `✕` pada Search, tekan Enter.
34. Ketik Search `pending email`, tekan Enter.
35. Verifikasi kolom Activation Status: hanya baris Fitri Handayani yang tampil.
36. Klik `✕` pada Search, tekan Enter.
37. Tampilkan kolom Temporary User lewat Setup Column, lalu klik `[Save]`.
38. Ketik Search `yes`, tekan Enter.
39. Verifikasi kolom Temporary User: hanya baris Rudi Hartono yang tampil.
40. Klik `✕` pada Search, tekan Enter.
41. Sembunyikan kolom Email, TAG, Badge No, Activation Status, dan Temporary User lewat Setup Column, lalu klik `[Save]`.

## Notes

- Alasan di atas 35 langkah: seluruh blok berkelas fungsional sama (Search atas tabel dan dataset Pre-setup #36 yang sama), tiap kata kunci berdiri sendiri karena langkah pengosongan Search di antaranya, dan kegagalan satu kata kunci tidak membuat kata kunci lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1, langkah 5, 8, 11, 14, 18, 22, 26, 29, 33, 36, dan 40 (mengosongkan Search sesuai 8b butir 9), langkah 15, 19, 23, 30, dan 37 (menampilkan kolom lewat Setup Column sebagai precondition keyword), dan langkah 41 (pemulihan kolom, S-09). Langkah 2 adalah pembanding positif untuk asersi universal langkah 4 sampai 39 (8b butir 2); sesudah tiap pengosongan Search tabel kembali menampilkan seluruh data.
- Search untuk menemukan baris target adalah objek uji pada spec ini, bukan langkah penghubung (R-16).
- Temuan untuk QA:
  - TC 472 dan TC 473 menyatakan kolom Email, TAG, Badge No, Activation Status, dan Temporary User dicari sesudah ditampilkan lewat Setup Column; tabel Pre-setup #36 memuat nilai kolom itu hanya untuk baris yang disebut TC. Kata kunci `inactive` (TC 473) dicari sebelum kolom Activation Status tampil.
  - TC 472 menyebut Pre-setup #36 dan #37; #37 (Tab Read Only) tidak dipakai langkah dan hanya ditulis sebagai data tersedia.
