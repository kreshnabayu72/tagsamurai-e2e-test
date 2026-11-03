---
id: TC-FA-RP-E2E-141-tab-total-control-filter-3
title: "Tab Total Control: Filter (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-487
  - TC-FA-RP-488
  - TC-FA-RP-489
  - TC-FA-RP-490
  - TC-FA-RP-491
coverage:
  web: automated
---

# Tab Total Control: Filter (3/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Position memiliki delapan nilai distinct) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.

## Test Steps

### Hapus chip lewat `(X)` (TC 487)

1. Klik ikon Filter.
2. Pilih opsi `Finance Officer` dan `HR Manager` pada field Position.
3. Klik `(X)` pada chip `HR Manager` tanpa membuka dropdown.
4. Verifikasi chip `HR Manager` hilang dari field dan chip `Finance Officer` tetap ada.
5. Buka dropdown field Position.
6. Verifikasi checkbox opsi `HR Manager` di dalam dropdown tidak tercentang.
7. Tutup dropdown dengan Esc, lalu klik `[Clear Field]`.

### Hapus chip lewat uncheck di dalam dropdown (TC 488)

8. Pilih opsi `Finance Officer` dan `HR Manager` pada field Position.
9. Buka dropdown field Position dan hapus centang opsi `HR Manager`.
10. Verifikasi chip `HR Manager` hilang dari field dan chip `Finance Officer` tetap ada.
11. Tutup dropdown dengan Esc, lalu klik `[Clear Field]`.

### Penghapusan chip mengubah hasil hanya setelah `[Apply]` (TC 489)

12. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
13. Pilih opsi `Finance Officer` dan `HR Manager` pada field Position, lalu klik `[Apply]`.
14. Hapus chip `HR Manager`.
15. Verifikasi tabel masih menampilkan Siti Rahmawati, Fitri Handayani, dan Siti Rahayu (kriteria lama) sebelum Apply.
16. Klik `[Apply]`.
17. Verifikasi tabel menampilkan hanya Siti Rahmawati dan Fitri Handayani (opsi `Finance Officer`).
18. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Overflow banyak chip (TC 490)

19. Pilih kedelapan opsi field Position: `Asset Custodian`, `Facility Officer`, `Finance Officer`, `Finance Supervisor`, `HR Manager`, `Operations Manager, Region 1`, `System Administrator`, `Warehouse Staff`.
20. Verifikasi closed-state field Position meringkas chip yang tidak muat menjadi chip `+N more` sesuai komponen MultiSelect.
21. Verifikasi field Position tidak terpotong.
22. Klik `[Clear Field]`, lalu klik ikon Filter untuk menutup panel.

### Kombinasi Search lalu Filter (TC 491)

23. Klik ikon Search.
24. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
25. Ketik Search `Fina`, tekan Enter.
26. Klik ikon Filter, pilih opsi `Finance` pada field Division, lalu klik `[Apply]`.
27. Verifikasi tabel menampilkan irisan Search `Fina` dan Filter Division `Finance`: hanya baris Fitri Handayani dan Rudi Hartono.
28. Verifikasi Filter tidak mereset keyword Search (kotak Search masih berisi `Fina`).
29. Klik `✕` pada Search, tekan Enter.
30. Pada panel Filter yang masih terbuka, klik `[Clear Field]`, lalu klik `[Apply]`.

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 5, 7, 8, 9, 11, 13, 14, 16, 18, 19, 22, 23, 25, 26, 29, dan 30. Langkah 7, 11, 18, 22, 29, dan 30 membersihkan filter atau Search sebelum TC berikutnya (S-09). Langkah 12 dan 24 adalah pembanding positif untuk asersi universal langkah 15, 17, dan 27 (8b butir 2).
- Temuan untuk QA:
  - TC 490 Expected menyebut "bila ruang field habis" (klausa bersyarat); spec mengasersi chip `+N more` tanpa syarat karena delapan opsi Position sengaja dipilih seluruhnya.
  - Panel Filter diasumsikan tetap terbuka sesudah `[Apply]` (TC 489 menghapus chip sesudah Apply tanpa membuka ulang panel); TC tidak menyatakannya.
  - TC 487 sampai TC 490 tidak menulis Apply; spec membersihkan draft dengan `[Clear Field]` tanpa Apply karena tidak ada filter yang ter-Apply (kecuali TC 489 yang di-Apply dan dibersihkan pada langkah 18).
