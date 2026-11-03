---
id: TC-FA-RP-E2E-135-tab-total-control-search-1
title: "Tab Total Control: Search (1/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-471
coverage:
  web: automated
---

# Tab Total Control: Search (1/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris: Admin Utama, Siti Rahmawati, Rina Wulandari, Ahmad Fauzi, Budi Santoso, Siti Rahayu, Eka Saputra, Fitri Handayani, Rudi Hartono) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

1. Arahkan kursor ke ikon Search di toolbar Tab Total Control.
2. Verifikasi tooltip `Search`.
3. Klik ikon Search.
4. Verifikasi placeholder input `Search name, position, division...`
5. Verifikasi kotak Search melebar.
6. Verifikasi kursor otomatis fokus di input.
7. Ketik `rina` tanpa menekan Enter.
8. Verifikasi ikon `(✕)` muncul di dalam input.
9. Verifikasi tabel belum tersaring: sedikitnya dua baris tampil, termasuk baris selain Rina Wulandari.
10. Tekan Enter.
11. Verifikasi tabel tersaring: hanya baris Rina Wulandari.
12. Klik ikon `(✕)` pada kotak Search.
13. Verifikasi teks input terhapus.
14. Verifikasi kotak Search tetap terbuka dan kursor tetap fokus di input.
15. Verifikasi tabel tetap menampilkan hasil pencarian terakhir (hanya baris Rina Wulandari).
16. Tekan Enter pada input kosong.
17. Verifikasi tabel kembali menampilkan seluruh data (sembilan baris Pre-setup #36).
18. Ketik Search `rina`, tekan Enter.
19. Klik ikon `(←)`.
20. Verifikasi kotak Search menutup.
21. Verifikasi keyword dikosongkan.
22. Verifikasi tabel langsung kembali menampilkan seluruh data (sembilan baris Pre-setup #36).

## Notes

- Langkah penghubung (S-03): langkah 7 dan 18 adalah aksi tanpa Verifikasi sendiri; langkah 9 menjadi pembanding positif untuk asersi universal langkah 11 (8b butir 2). Langkah buka Tab Total Control (langkah 1 TC) tidak ditulis karena halaman dibuka hook `beforeEach` suite pada tab itu.
- Copy bertanda `copy usulan, PRD 12 #1` (placeholder Search) di-assert literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA: tidak ada.
