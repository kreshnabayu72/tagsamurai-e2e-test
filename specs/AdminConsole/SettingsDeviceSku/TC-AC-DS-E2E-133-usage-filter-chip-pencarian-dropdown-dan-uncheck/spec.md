---
id: TC-AC-DS-E2E-133-usage-filter-chip-pencarian-dropdown-dan-uncheck
title: "Filter Usage: Penghapusan Chip, Un-check Opsi, Pencarian di Dalam Dropdown, dan Rentang Total Stock Inklusif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-449
  - TC-AC-DS-450
  - TC-AC-DS-564
  - TC-AC-DS-571
coverage:
  web: automated
---

# Filter Usage: Penghapusan Chip, Un-check Opsi, Pencarian di Dalam Dropdown, dan Rentang Total Stock Inklusif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris dan jaringan entitas (#32, #24): `PT Arunika Prima` (Principal) 55, `PT Cakra Distribusi` (Distributor) 25, `PT Delta Retail` (Client) 5, `PT Mitra Lintas Nusa` (Distributor dan Client) 20, `PT Surya Logistik` (Client) 15. Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil
3. Verifikasi tabel Usage memuat sedikitnya satu baris

### TC-AC-DS-449: Filter Total Stock rentang Min-Max inklusif pada Usage

4. Klik ikon Filter pada popup
5. Verifikasi Filter Panel popup tampil
6. Verifikasi placeholder field Total Stock adalah "Min" dan "Max"
7. Isi Min `20` dan Max `25`
8. Klik `[Apply]` pada Filter Panel popup
9. Verifikasi tabel memuat baris Total Stock 20 dan 25: `PT Cakra Distribusi` dan `PT Mitra Lintas Nusa` (kedua ujung inklusif)

### Pemulihan state antar TC

10. Klik `[Clear Field]`

### TC-AC-DS-450: Menghapus chip Filter Usage lewat ikon silang meng-uncheck checkbox di dalam dropdown

11. Pada field Entity Type pilih `Distributor` dan `Client`
12. Klik ikon `(✕)` pada chip `Client`
13. Verifikasi chip `Client` hilang
14. Verifikasi chip `Distributor` tetap ada
15. Buka dropdown Entity Type
16. Verifikasi checkbox `Client` tidak tercentang
17. Verifikasi checkbox `Distributor` tetap tercentang
18. Klik `[Apply]` pada Filter Panel popup
19. Verifikasi tabel memuat baris Entity Type `Distributor`: `PT Cakra Distribusi` dan `PT Mitra Lintas Nusa`

### Pemulihan state antar TC

20. Klik `[Clear Field]`

### TC-AC-DS-564: Pencarian di dalam dropdown Filter Entity Type Usage mempersempit opsi

21. Klik field Entity Type
22. Ketik `dis` pada kotak pencarian di dalam dropdown
23. Verifikasi hanya opsi `Distributor` tampil (substring, tidak membedakan huruf besar-kecil)
24. Ganti isi kotak pencarian di dalam dropdown dengan `zzz`
25. Verifikasi tidak ada opsi yang cocok
26. Verifikasi dropdown menampilkan teks "No results found" (teks saja, tanpa ilustrasi)

### Pemulihan state antar TC

27. Kosongkan kotak pencarian di dalam dropdown

### TC-AC-DS-571: Meng-uncheck opsi di dalam dropdown Filter Usage menghapus chip yang bersangkutan

28. Pada field Entity Type pilih `Distributor` dan `Client`
29. Buka dropdown Entity Type, hilangkan centang `Distributor`
30. Verifikasi chip `Distributor` hilang dari dalam field
31. Verifikasi chip `Client` tetap ada
32. Klik `[Apply]` pada Filter Panel popup
33. Verifikasi tabel memuat baris Entity Type `Client`: `PT Delta Retail`, `PT Mitra Lintas Nusa`, dan `PT Surya Logistik`

### Pemulihan state akhir

34. Klik `[Clear Field]`, klik `[Apply]`, lalu tutup popup dengan ikon close `[✕]`

## Notes

- Langkah 1 sampai 3 adalah pembuka bersama (popup `HHR-ARC-100` dibuka sekali). Langkah 3 adalah pembanding generik sebelum asersi filter (8b butir 2).
- Spec berisi 34 langkah (di bawah sekitar 35). Empat blok TC berdiri sendiri pada permukaan Filter Panel Usage yang sama.
- Langkah penghubung tanpa `Verifikasi`: langkah 10, 20, 27, dan 34 (S-03, S-09). Langkah 10 dan 20 mengklik `[Clear Field]` tepat setelah `[Apply]`, mengikuti pola TC-AC-DS-448.
- Expected 449 butir b ditulis langkah 6 (placeholder dicek saat field kosong, S-14); butir a langkah 9. Expected 450 butir a dan b dipecah per klausa (langkah 13, 14, 16, 17) dan butir c langkah 19. Expected 564 butir b dipecah langkah 25 dan 26. Expected 571 butir a dipecah langkah 30 dan 31, butir b langkah 33.
- Temuan untuk QA:
  - S-15: TC tidak menyebut apakah Filter Panel masih terbuka setelah `[Apply]`; spec mengikuti TC (langkah 10 dan 20 langsung `[Clear Field]`).
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
