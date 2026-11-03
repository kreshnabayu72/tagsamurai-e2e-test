---
id: TC-AC-DS-E2E-131-usage-search-kelas-teks-badge-angka-dan-siklus
title: "Search Usage: Kelas Teks dan Badge, Angka Total Stock, dan Siklus Interaksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-443
  - TC-AC-DS-444
  - TC-AC-DS-445
coverage:
  web: automated
---

# Search Usage: Kelas Teks dan Badge, Angka Total Stock, dan Siklus Interaksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris dan jaringan entitas (#32, #24): `PT Arunika Prima` 55, `PT Cakra Distribusi` 25, `PT Delta Retail` 5, `PT Mitra Lintas Nusa` 20 (dua badge), `PT Surya Logistik` 15. Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil
3. Verifikasi tabel Usage memuat sedikitnya satu baris

### TC-AC-DS-443: Search Usage kelas teks dan badge: Company dan Entity Type

4. Klik ikon Search pada popup, ketik Search `Cakra`, tekan Enter
5. Verifikasi Company `Cakra` menampilkan baris `PT Cakra Distribusi`
6. Ganti isi kotak search dengan `Client`, tekan Enter
7. Verifikasi Entity Type `Client` menampilkan `PT Delta Retail`, `PT Mitra Lintas Nusa` (salah satu badge Client), dan `PT Surya Logistik`

### TC-AC-DS-444: Search Usage mencocokkan angka Total Stock

8. Ganti isi kotak search dengan `55`, tekan Enter
9. Verifikasi kata kunci `55` menampilkan baris `PT Arunika Prima` (Total Stock 55) saja

### Pemulihan state antar TC

10. Klik `(←)` pada kotak Search

### TC-AC-DS-445: Siklus interaksi Search Usage: reveal, Enter, clear, dan collapse

11. Klik ikon Search pada popup
12. Verifikasi kotak melebar
13. Verifikasi kursor fokus pada kotak
14. Verifikasi placeholder "Search company, entity type..." tampil
15. Ketik `PT` tanpa Enter
16. Verifikasi tabel belum tersaring
17. Tekan Enter
18. Verifikasi semua baris yang mengandung `PT` tampil
19. Klik `(✕)`
20. Verifikasi input Search kosong
21. Verifikasi tabel tidak ter-reset
22. Tekan Enter pada input kosong
23. Verifikasi tabel ter-reset ke 5 baris
24. Ketik Search `Surya`, tekan Enter
25. Klik `(←)`
26. Verifikasi kotak Search tertutup
27. Verifikasi tabel langsung ter-reset

### Pemulihan state akhir

28. Tutup popup dengan ikon close `[✕]`

## Notes

- Langkah 1 sampai 3 adalah pembuka bersama ketiga TC (popup `HHR-ARC-100` dibuka sekali; TC memulai dari popup yang sama). Langkah 3 adalah pembanding generik sebelum asersi Search (8b butir 2).
- Langkah penghubung tanpa `Verifikasi`: langkah 10 (menutup kotak Search dan mereset tabel sebelum TC-AC-DS-445) dan langkah 28 (S-03, S-09). Langkah 1 membuka baris dari List tanpa Search.
- Expected 445 butir a dipecah menjadi langkah 12 sampai 14; butir c menjadi langkah 20 sampai 23; butir d menjadi langkah 26 dan 27.
- Temuan untuk QA:
  - S-11/S-14: kata kunci `PT` pada TC-AC-DS-445 mencocokkan seluruh lima baris (semua nama company berawalan `PT`), sehingga "tabel belum tersaring" (langkah 16), "semua baris yang mengandung PT" (langkah 18), dan "tabel tidak ter-reset" (langkah 21) tidak dapat dibedakan dari "tabel ter-reset ke 5 baris" (langkah 23). Spec mengikuti TC.
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
