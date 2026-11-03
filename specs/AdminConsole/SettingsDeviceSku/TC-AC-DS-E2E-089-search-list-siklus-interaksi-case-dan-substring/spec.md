---
id: TC-AC-DS-E2E-089-search-list-siklus-interaksi-case-dan-substring
title: "Search List: Siklus Interaksi, Tidak Membedakan Huruf Besar-Kecil, dan Substring"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-305
  - TC-AC-DS-306
  - TC-AC-DS-307
coverage:
  web: automated
---

# Search List: Siklus Interaksi, Tidak Membedakan Huruf Besar-Kecil, dan Substring

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti, termasuk `HHR-ARC-100`, `HHR-ARC-200`, `HHR-BIG-01`, `SFR-VEL-4P`) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten (dilewati bila sudah ada) oleh seeding di hook `before`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat, sehingga tidak ada cleanup.

## Test Steps

### TC-AC-DS-305: Siklus interaksi Search

1. Hover ikon Search
2. Verifikasi tooltip `Search` tampil
3. Klik ikon Search
4. Verifikasi kotak pencarian melebar
5. Verifikasi kursor fokus otomatis pada kotak pencarian
6. Verifikasi placeholder "Search SKU, device name, brand, model..." tampil
7. Ketik `HHR` tanpa menekan Enter
8. Verifikasi ikon `(✕)` muncul di dalam input
9. Verifikasi tabel belum tersaring: baris `BLE-KIN-GW1` masih tampil
10. Tekan Enter
11. Verifikasi tabel hanya memuat baris `HHR-ARC-100`, `HHR-ARC-200`, dan `HHR-BIG-01`
12. Klik ikon `(✕)` di dalam input
13. Verifikasi input kosong dan kotak pencarian tetap terbuka
14. Verifikasi kursor fokus pada kotak pencarian
15. Verifikasi tabel tidak reset (tetap hasil `HHR`: `HHR-ARC-100`, `HHR-ARC-200`, `HHR-BIG-01`)
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali menampilkan seluruh SKU (baris `BLE-KIN-GW1` tampil kembali)
18. Ketik Search `HHR`, tekan Enter
19. Klik ikon panah `(←)` di kiri toolbar
20. Verifikasi kotak pencarian menutup menjadi ikon Search
21. Verifikasi kata kunci dikosongkan dan tabel langsung reset ke kondisi awal (baris `BLE-KIN-GW1` tampil)

### TC-AC-DS-306: Search tidak membedakan huruf besar-kecil

22. Ketik Search `hhr-arc-100`, tekan Enter
23. Verifikasi tabel hanya menampilkan baris `HHR-ARC-100`
24. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
25. Verifikasi tabel hanya menampilkan baris `HHR-ARC-100` (hasil sama dengan `hhr-arc-100`)
26. Ganti isi kotak search dengan `Uhf HANDHELD`, tekan Enter
27. Verifikasi tabel menampilkan baris `HHR-ARC-100` dan `HHR-ARC-200` (Device Name `UHF Handheld Reader`)

### TC-AC-DS-307: Search mencocokkan substring dan spasi di tengah

28. Ganti isi kotak search dengan `ARC-1`, tekan Enter
29. Verifikasi tabel menampilkan baris `HHR-ARC-100` (bagian tengah SKU)
30. Ganti isi kotak search dengan `Fixed Reader`, tekan Enter
31. Verifikasi tabel menampilkan baris `SFR-VEL-4P` (Device Name `4-Port Fixed Reader`)

## Notes

- Langkah penghubung (S-03): langkah 18 sampai 19 menyiapkan keadaan Search aktif sebelum `(←)`; tidak ada asersi tambahan di luar Expected TC.
- Hasil Search pada langkah 11 dan 23 sampai 31 diasersi dengan baris yang dijamin tampil oleh kata kunci Search itu sendiri; tidak ada hasil kosong yang dibaca sebagai absence.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-100`, total 129 SKU). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Akun `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila muncul dan menutupi layar, diperlukan cara menyetel flag-nya (belum ditetapkan di TC, PRD, atau LLD).
